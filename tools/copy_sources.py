"""Copy a source tree into the vault with redaction, two denylist layers, dedupe and a manifest.

Pipeline per file (PLAN 3 / 4, stdlib only; logic lives in tools/redact.py + tools/vaultlib.py):
  DENY_READ  (name or any path component)  -> never opened, recorded by name only
  DENY_COPY  (*.db, *.sqlite*, *-wal, *-shm, *.pb) -> skipped, recorded
  read utf-8 -> NFC -> redact_text (two passes inside) -> hash-pinned HIGH_ENTROPY redaction
  (optional ``redact_value_hashes``: an entropy-detected token whose sha256 is in the set becomes
  ``[REDACTED:HIGH_ENTROPY]``, counted under HIGH_ENTROPY and dropped from entropy_hits) -> whitespace cleanup
  unresolved private-key block -> SKIPPED_SENSITIVE (nothing written)
  residual secret match in the output -> error (nothing written, exit 1)
  > MAX_OUT_BYTES after redaction -> skipped_size
  SHA-256 dedupe of the redacted text (newest mtime wins)
  write utf-8 / LF / no BOM under sanitized relative path -> manifest.json

``dry_run=True`` writes nothing at all (no files, no manifest); only the report is produced.

CLI: python tools/copy_sources.py SRC DST [--ext .md .json ...] [--exclude GLOB ...] [--dry-run] [--top 20]
Exit 0 on success, 1 when the report has errors.
"""
from __future__ import annotations

import argparse
import fnmatch
import os
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence

if __package__ in (None, ""):  # executed as a script: make ``tools`` importable
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import redact, vaultlib  # noqa: E402

MAX_OUT_BYTES = 5 * 1024 * 1024
BINARY_PROBE_BYTES = 8 * 1024
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache"}
_TRAILING_WS = re.compile(r"[ \t]+$", re.M)
_MANY_BLANK = re.compile(r"\n{4,}")  # more than two consecutive blank lines -> two


@dataclass
class CopyReport:
    copied: List[dict] = field(default_factory=list)          # {src, dst, sha256, bytes, redactions}
    skipped_deny_read: List[str] = field(default_factory=list)  # names only, never opened
    skipped_deny_copy: List[str] = field(default_factory=list)
    skipped_sensitive: List[str] = field(default_factory=list)  # sanitized titles
    skipped_dedupe: List[dict] = field(default_factory=list)    # {src, kept}
    skipped_size: List[dict] = field(default_factory=list)      # {src, bytes}
    skipped_binary: List[str] = field(default_factory=list)
    counts: Counter = field(default_factory=Counter)            # redactions per category
    entropy_hits: List[dict] = field(default_factory=list)      # {path, length, entropy, context_hint}
    top_redacted: List[dict] = field(default_factory=list)      # {path, redactions}
    errors: List[dict] = field(default_factory=list)            # {src, error}

    @property
    def ok(self) -> bool:
        return not self.errors

    def summary(self) -> str:
        return ("copied=%d deny_read=%d deny_copy=%d sensitive=%d dedupe=%d size=%d binary=%d "
                "redactions=%d entropy_hits=%d errors=%d" % (
                    len(self.copied), len(self.skipped_deny_read), len(self.skipped_deny_copy),
                    len(self.skipped_sensitive), len(self.skipped_dedupe), len(self.skipped_size),
                    len(self.skipped_binary), sum(self.counts.values()), len(self.entropy_hits), len(self.errors)))


@dataclass
class _Candidate:
    src_rel: str
    dst_rel: str
    text: str
    sha256: str
    mtime: float
    redactions: int


# --------------------------------------------------------------------------- helpers

def _safe(label: str) -> str:
    """A path/title that is safe to record: redacted with the standard engine."""
    return redact.redact_text(label).text


def _norm_exts(exts: Optional[Iterable[str]]) -> Optional[frozenset]:
    if exts is None:
        return None
    return frozenset(("" if e.startswith(".") else ".") + e.lower() for e in exts if e)


def _excluded(rel: str, globs: Sequence[str]) -> bool:
    name = rel.rsplit("/", 1)[-1]
    return any(fnmatch.fnmatchcase(rel, g) or fnmatch.fnmatchcase(name, g) for g in globs)


def _dst_rel(src_rel: str) -> str:
    return "/".join(vaultlib.sanitize_filename(part) for part in src_rel.split("/"))


def clean_whitespace(text: str) -> str:
    """Strip trailing spaces, collapse >2 consecutive blank lines to 2, end with one LF."""
    text = _TRAILING_WS.sub("", text.replace("\r\n", "\n").replace("\r", "\n"))
    text = _MANY_BLANK.sub("\n\n\n", text)
    return text.strip("\n") + "\n" if text.strip() else ""


def _read_source(p: Path) -> Optional[str]:
    """UTF-8 text (replacement on decode errors) or None for binary content."""
    with open(p, "rb") as f:
        head = f.read(BINARY_PROBE_BYTES)
    if b"\x00" in head:
        return None
    try:
        return vaultlib.read_text(p)
    except UnicodeDecodeError:
        with open(p, "rb") as f:
            return f.read().decode("utf-8", "replace").replace("\r\n", "\n").replace("\r", "\n")


def _iter_sources(src_root: Path) -> List[str]:
    out: List[str] = []
    for dirpath, dirnames, filenames in os.walk(src_root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for fn in sorted(filenames):
            out.append((Path(dirpath) / fn).relative_to(src_root).as_posix())
    return out


# --------------------------------------------------------------------------- core

def _hash_redact(text: str, hashes, counts: Counter, hits: List[dict]) -> str:
    """Check every ``_TOKEN`` candidate (>= ENTROPY_MIN_LEN chars) in *text* against *hashes* and replace
    each one whose ``sha256_text`` is pinned with ``[REDACTED:HIGH_ENTROPY]``. Pinning is explicit, so neither
    the entropy threshold nor the hex/uuid exclusions of the record-only entropy pass apply here (a pinned
    hex32 nonce below the threshold is still redacted). Each replacement is counted under HIGH_ENTROPY and
    its (length, entropy) record, when the entropy pass reported one, is dropped from *hits*.
    Values never leave this function: only the marker is written and only the hash is ever stored."""
    out: List[str] = []
    last = 0
    for m in redact._TOKEN.finditer(text):
        tok = m.group()
        if vaultlib.sha256_text(tok) not in hashes:
            continue
        ent = redact.shannon_entropy(tok)
        out.append(text[last:m.start()])
        out.append(redact.marker("HIGH_ENTROPY"))
        last = m.end()
        counts["HIGH_ENTROPY"] += 1
        key = (len(tok), round(ent, 3))
        for i, h in enumerate(hits):
            if (h["length"], h["entropy"]) == key:
                del hits[i]
                break
    if not out:
        return text
    out.append(text[last:])
    return "".join(out)


def _process(src_root: Path, rel: str, report: CopyReport,
             redact_value_hashes: Optional[set] = None) -> Optional[_Candidate]:
    p = src_root / rel
    text = _read_source(p)
    if text is None:
        report.skipped_binary.append(_safe(rel))
        return None
    res = redact.redact_text(vaultlib.nfc(text))
    if res.unresolved_private_key:
        report.skipped_sensitive.append(_safe(rel))
        return None
    counts: Counter = Counter(res.counts)
    hits: List[dict] = list(res.entropy_hits)
    redacted = res.text
    if redact_value_hashes:
        redacted = _hash_redact(redacted, redact_value_hashes, counts, hits)
    out = clean_whitespace(redacted)
    left = redact.residual_matches(out)
    if left:
        raise redact.RedactionIncomplete("residual matches after redaction: %s" % ",".join(sorted(left)))
    report.counts.update(counts)
    safe_rel = _safe(rel)
    for h in hits:
        report.entropy_hits.append({"path": safe_rel, "length": h["length"], "entropy": h["entropy"],
                                    "context_hint": h["context_hint"]})
    size = vaultlib.utf8_len(out)
    if size > MAX_OUT_BYTES:
        report.skipped_size.append({"src": safe_rel, "bytes": size})
        return None
    return _Candidate(rel, _dst_rel(rel), out, vaultlib.sha256_text(out), p.stat().st_mtime,
                      sum(counts.values()))


def _dedupe(cands: List[_Candidate], report: CopyReport) -> List[_Candidate]:
    kept: Dict[str, _Candidate] = {}
    losers: List[tuple] = []
    for c in cands:
        prev = kept.get(c.sha256)
        if prev is None:
            kept[c.sha256] = c
        elif c.mtime > prev.mtime:  # newest wins, ties keep the first (sorted) path
            kept[c.sha256] = c
            losers.append((prev, c))
        else:
            losers.append((c, prev))
    for lost, winner in losers:
        final = kept[winner.sha256]
        report.skipped_dedupe.append({"src": _safe(lost.src_rel), "kept": _safe(final.src_rel)})
    return sorted(kept.values(), key=lambda c: c.src_rel)


def _write_if_changed(dst: Path, text: str) -> None:
    if dst.is_file():
        try:
            if vaultlib.read_text(dst) == text:
                return
        except (OSError, UnicodeDecodeError):
            pass
    vaultlib.write_text(dst, text)


def copy_file(src_path, dst_root, dst_rel: str, *, report: Optional[CopyReport] = None,
              dry_run: bool = False, redact_value_hashes: Optional[set] = None) -> CopyReport:
    """Run ONE file through the same pipeline as ``copy_tree`` (denylist on its name -> read ->
    NFC -> redact -> hash-pinned HIGH_ENTROPY -> unresolved PK -> residual -> whitespace -> size ->
    idempotent write). Never writes a manifest. *dst_rel* is sanitized per path component."""
    src_path, dst_root = Path(src_path), Path(dst_root).resolve()
    report = report if report is not None else CopyReport()
    name = src_path.name
    if redact.is_denied_path(name, "READ"):
        report.skipped_deny_read.append(_safe(name))  # never opened
        return report
    if redact.is_denied_path(name, "COPY"):
        report.skipped_deny_copy.append(_safe(name))
        return report
    if not src_path.is_file():
        report.errors.append({"src": _safe(name), "error": "FileNotFoundError: source missing"})
        return report
    try:
        c = _process(src_path.parent, name, report, redact_value_hashes)
    except (OSError, redact.RedactionIncomplete) as exc:
        report.errors.append({"src": _safe(name), "error": type(exc).__name__ + ": " + _safe(str(exc))})
        return report
    if c is None:
        return report
    c.dst_rel = _dst_rel(dst_rel.replace("\\", "/"))
    if c.redactions:
        report.top_redacted.append({"path": _safe(name), "redactions": c.redactions})
        report.top_redacted.sort(key=lambda r: (-r["redactions"], r["path"]))
    report.copied.append({"src": _safe(name), "dst": c.dst_rel, "sha256": c.sha256,
                          "bytes": vaultlib.utf8_len(c.text), "redactions": c.redactions})
    if not dry_run:
        _write_if_changed(dst_root / c.dst_rel, c.text)
    return report


def copy_tree(src_root, dst_root, *, include_exts: Optional[Iterable[str]] = None,
              exclude_globs: Sequence[str] = (), dry_run: bool = False, top_n: int = 20,
              manifest_dir=None, redact_value_hashes: Optional[set] = None) -> CopyReport:
    src_root, dst_root = Path(src_root).resolve(), Path(dst_root).resolve()
    if not src_root.is_dir():
        raise FileNotFoundError("source root is not a directory: %s" % src_root.name)
    exts = _norm_exts(include_exts)
    report = CopyReport()
    cands: List[_Candidate] = []
    for rel in _iter_sources(src_root):
        if _excluded(rel, exclude_globs):
            continue
        if redact.is_denied_path(rel, "READ"):
            report.skipped_deny_read.append(_safe(rel))  # never opened
            continue
        if redact.is_denied_path(rel, "COPY"):
            report.skipped_deny_copy.append(_safe(rel))
            continue
        if exts is not None and Path(rel).suffix.lower() not in exts:
            continue
        try:
            c = _process(src_root, rel, report, redact_value_hashes)
        except (OSError, redact.RedactionIncomplete) as exc:
            report.errors.append({"src": _safe(rel), "error": type(exc).__name__ + ": " + _safe(str(exc))})
            continue
        if c is not None:
            cands.append(c)

    per_file = sorted(((c.redactions, c.src_rel) for c in cands), key=lambda t: (-t[0], t[1]))
    report.top_redacted = [{"path": _safe(rel), "redactions": n} for n, rel in per_file[:top_n] if n]

    for c in _dedupe(cands, report):
        report.copied.append({"src": _safe(c.src_rel), "dst": c.dst_rel, "sha256": c.sha256,
                              "bytes": vaultlib.utf8_len(c.text), "redactions": c.redactions})
        if not dry_run:
            _write_if_changed(dst_root / c.dst_rel, c.text)
    if not dry_run:
        vaultlib.write_manifest(Path(manifest_dir).resolve() if manifest_dir else dst_root, build_manifest(report))
    return report


def build_manifest(report: CopyReport) -> dict:
    return {
        "tool": "copy_sources",
        "summary": {
            "copied": len(report.copied),
            "skipped_deny_read": len(report.skipped_deny_read),
            "skipped_deny_copy": len(report.skipped_deny_copy),
            "skipped_sensitive": len(report.skipped_sensitive),
            "skipped_dedupe": len(report.skipped_dedupe),
            "skipped_size": len(report.skipped_size),
            "skipped_binary": len(report.skipped_binary),
            "errors": len(report.errors),
            "redactions": sum(report.counts.values()),
            "entropy_hits": len(report.entropy_hits),
        },
        "files": {c["dst"]: {"sha256": c["sha256"], "bytes": c["bytes"], "redactions": c["redactions"], "src": c["src"]}
                  for c in report.copied},
        "redaction_counts": dict(sorted(report.counts.items())),
        "entropy_hits": report.entropy_hits,
        "rejected_by_name": {"DENY_READ": report.skipped_deny_read, "DENY_COPY": report.skipped_deny_copy},
        "skipped_sensitive": report.skipped_sensitive,
        "skipped_dedupe": report.skipped_dedupe,
        "skipped_size": report.skipped_size,
        "skipped_binary": report.skipped_binary,
        "top_redacted": report.top_redacted,
        "errors": report.errors,
    }


# --------------------------------------------------------------------------- CLI

def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Copy a source tree into the vault with redaction + denylist + dedupe.")
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--ext", nargs="*", default=None, help="only these extensions (e.g. .md .json)")
    ap.add_argument("--exclude", nargs="*", default=[], help="glob patterns (relative path or file name)")
    ap.add_argument("--dry-run", action="store_true", help="report only; write nothing")
    ap.add_argument("--top", type=int, default=20)
    a = ap.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass
    try:
        rep = copy_tree(a.src, a.dst, include_exts=a.ext, exclude_globs=a.exclude, dry_run=a.dry_run, top_n=a.top)
    except FileNotFoundError as exc:
        print("[copy_sources] ERROR: %s" % exc)
        return 1
    print("[copy_sources] %s%s" % ("DRY-RUN " if a.dry_run else "", rep.summary()))
    if rep.counts:
        print("[copy_sources] redactions by category: " + ", ".join("%s=%d" % kv for kv in sorted(rep.counts.items())))
    if rep.top_redacted:
        print("| # | path | redactions |\n|---|---|---|")
        for i, row in enumerate(rep.top_redacted, 1):
            print("| %d | %s | %d |" % (i, row["path"], row["redactions"]))
    for name in rep.skipped_deny_read:
        print("DENY_READ  " + name)
    for name in rep.skipped_deny_copy:
        print("DENY_COPY  " + name)
    for title in rep.skipped_sensitive:
        print("SKIPPED_SENSITIVE  " + title)
    for e in rep.errors:
        print("ERROR  %s (%s)" % (e["src"], e["error"]))
    return 0 if rep.ok else 1


if __name__ == "__main__":
    sys.exit(main())
