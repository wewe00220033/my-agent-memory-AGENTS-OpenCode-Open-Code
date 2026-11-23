"""T16 - Export the gateway LEDGER (``ALL_CONVERSATIONS_LEDGER/*.json``) into ``conversations/ledger/`` as one
redacted JSON list sharded into parts of at most ``JSON_MAX`` bytes (+ ``ledger.parts.json``, ``AUDIT.md``, ``SUMMARY.md``).

Source (PLAN section 4, Q5/Q16): the snapshot copy named under ``sources.ledger`` in ``_local/SNAPSHOT_STATE.json``
(``kind: json_dir``). The copy's combined sha256 (``sorted name\\tsha256\\n`` - same recipe as ``snapshot_db``) is
verified against ``sha_copy`` before anything is parsed; a mismatch stops the export. The original source on the
other drive is never opened. ``files_total`` / ``items_total`` come from ``rows_by_table`` - never constants.

FORENSIC (``sources.forensic``) is a byte-for-byte duplicate of LEDGER (T0: 453/453 items by canonical sha256) and is
**never read**; the manifest only records ``forensic_skipped_as_duplicate: true``.

One list element per LEDGER file, in filename order: the file's object with every string redacted recursively via
``redact.redact_text`` (two passes inside; CRLF normalized to LF first) plus optional hash-pinned values from
``_local/manifests/S3/ledger.review.json``. A file reporting ``unresolved_private_key`` anywhere is skipped whole (Q6);
an element whose canonical redacted sha256 repeats an earlier one is skipped as ``duplicate``. ``residual_matches``
must be empty on every serialized element or the export raises. Entropy hits are recorded as sha256 + shape +
location only - never the value.

``--dry-run`` writes nothing under the output directory; the sharding plan is computed and a roundtrip
(``write_shards`` -> ``read_shards`` in a temp dir outside the repo) proves reassembly == the redacted list.
Manifest and report (counts, hashes and shapes only) are always produced. Real writes are idempotent.

CLI: python tools/export_ledger.py [--dry-run] [--top 20] [--state PATH] [--out DIR]
     [--manifest PATH] [--report PATH] [--max-bytes N] [--review-dir DIR]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

if __package__ in (None, ""):  # executed as a script: make ``tools`` importable
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import redact, vaultlib  # noqa: E402
from tools.copy_sources import _hash_redact, _write_if_changed  # noqa: E402
from tools.export_antigravity_fts import _charset, _readable  # noqa: E402
from tools.export_memory import load_review_hashes  # noqa: E402
from tools.export_summaries import DEFAULT_STATE, ExportError, load_state  # noqa: E402
from tools.shard import JSON_MAX, _dumps, read_shards, shard_json, write_shards  # noqa: E402

TOOL_VERSION = "1.0.1"
SOURCE_KEY = "ledger"
FORENSIC_KEY = "forensic"
REPO = vaultlib.repo_root()
DEFAULT_OUT = REPO / "conversations" / "ledger"
MANIFEST_DIR = REPO / "_local" / "manifests" / "S3"
DEFAULT_MANIFEST = MANIFEST_DIR / "ledger.manifest.json"
DEFAULT_REPORT = REPO / "_local" / "T16_DRYRUN.md"
REVIEW_PROJECT = "ledger"  # -> <review dir>/ledger.review.json
BASE_NAME = "ledger"  # ledger.json | ledger.partNNN.json + ledger.parts.json
SOURCE_FIELD = "_source_file"
# ``file:///c%3A/Users/<name>/...`` - the percent-encoded drive colon hides the home path from every ``home_*``
# pattern (T16-2 finding: 70 real-string hits). Decode just that colon before redaction so ``home_windows_drive``
# turns it into ``~``. Root fix belongs to patterns.json (planner decision).
_FILE_URI_DRIVE = re.compile(r"(file:/{2,3}[A-Za-z])%3[Aa](?=[\\/])")


@dataclass
class Report:
    files_total: int = 0
    items_total: int = 0
    exported: List[str] = field(default_factory=list)
    items_exported: int = 0
    skipped_sensitive: List[str] = field(default_factory=list)
    skipped_duplicate: List[str] = field(default_factory=list)
    skipped_denied: List[str] = field(default_factory=list)
    skipped_parse: List[str] = field(default_factory=list)
    items_skipped: int = 0
    counts: Counter = field(default_factory=Counter)
    per_file: Dict[str, Counter] = field(default_factory=dict)
    entropy_hits: List[dict] = field(default_factory=list)
    file_shapes: Dict[str, dict] = field(default_factory=dict)  # name -> {bytes_in, bytes_out, keys, strings}
    parts: List[dict] = field(default_factory=list)
    oversize: List[dict] = field(default_factory=list)
    merged_sha256: str = ""
    merged_bytes: int = 0
    roundtrip_ok: Optional[bool] = None
    warnings: List[str] = field(default_factory=list)

    @property
    def skipped(self) -> int:
        return len(self.skipped_sensitive) + len(self.skipped_duplicate) + len(self.skipped_denied) + len(self.skipped_parse)

    @property
    def match_files(self) -> bool:
        return len(self.exported) + self.skipped == self.files_total

    @property
    def match_items(self) -> bool:
        return self.items_exported + self.items_skipped == self.items_total


# --------------------------------------------------------------------------- snapshot access

def snapshot_dir(state: dict) -> Tuple[Path, str, int, int]:
    """(copy dir, expected combined sha256, files_total, items_total) from the state file."""
    src = (state.get("sources") or {}).get(SOURCE_KEY)
    if not src or not src.get("copy_path"):
        raise ExportError("state has no %s.copy_path" % SOURCE_KEY)
    copy = Path(os.path.expandvars(str(src["copy_path"]).rstrip("\\/")))
    rbt = src.get("rows_by_table") or {}
    n_files, n_items = rbt.get("files"), rbt.get("top_level_items")
    if not isinstance(n_files, int) or not isinstance(n_items, int):
        raise ExportError("state has no rows_by_table[files]/[top_level_items] for %s" % SOURCE_KEY)
    return copy, str(src.get("sha_copy", "")), n_files, n_items


def list_files(copy: Path) -> List[Path]:
    if not copy.is_dir():
        raise ExportError("snapshot copy directory missing: %s" % copy.name)
    return sorted(p for p in copy.iterdir() if p.is_file())


def combined_sha(files: Sequence[Path]) -> str:
    """Same recipe as ``snapshot_db._combined(_hashes(files))``."""
    hashes = {p.name: vaultlib.sha256_file(p) for p in files}
    h = hashlib.sha256()
    for name in sorted(hashes):
        h.update(("%s\t%s\n" % (name, hashes[name])).encode("utf-8"))
    return h.hexdigest()


def verify_dir(files: Sequence[Path], sha_expected: str) -> str:
    actual = combined_sha(files)
    if actual != sha_expected:
        raise ExportError("snapshot copy sha256 mismatch for %s (state=%s... actual=%s...)" % (
            SOURCE_KEY, sha_expected[:12], actual[:12]))
    return actual


# --------------------------------------------------------------------------- redaction

def _item_count(obj: Any) -> int:
    """Same rule as ``snapshot_db._top_level_items``."""
    return len(obj) if isinstance(obj, (list, dict)) else 1


def _shape_hits(text: str, hits: List[dict], item: str, where: str) -> None:
    """Add sha256 / charset / readable / location to each entropy hit (the token itself is never stored)."""
    for h in hits:
        if "sha256" in h:
            continue
        key = (h["length"], h["entropy"])
        for m in redact._TOKEN.finditer(text):
            tok = m.group()
            if (len(tok), round(redact.shannon_entropy(tok), 3)) == key:
                h["sha256"], h["charset"], h["readable"] = vaultlib.sha256_text(tok), _charset(tok), _readable(tok)
                break
        else:
            h["sha256"], h["charset"], h["readable"] = "", "?", False
        h["item"], h["where"] = item, where


def _redact_str(text: str, counts: Counter, hits: List[dict], hashes, item: str, where: str) -> Tuple[str, bool]:
    if not text:
        return text, False
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = _FILE_URI_DRIVE.sub(r"\1:", text)
    res = redact.redact_text(text)
    counts.update(res.counts)
    local: List[dict] = list(res.entropy_hits)
    out = res.text
    if hashes:
        out = _hash_redact(out, hashes, counts, local)
    _shape_hits(out, local, item, where)
    hits.extend(local)
    return out, res.unresolved_private_key


def redact_obj(obj: Any, counts: Counter, hits: List[dict], hashes, item: str, where: str = "$",
               stats: Optional[Counter] = None) -> Tuple[Any, bool]:
    """Recursively redact every string (keys included); returns (new object, unresolved_private_key)."""
    if isinstance(obj, str):
        if stats is not None:
            stats["strings"] += 1
        return _redact_str(obj, counts, hits, hashes, item, where)
    if isinstance(obj, list):
        out: List[Any] = []
        u = False
        for i, v in enumerate(obj):
            r, uu = redact_obj(v, counts, hits, hashes, item, "%s[%d]" % (where, i), stats)
            out.append(r)
            u |= uu
        return out, u
    if isinstance(obj, dict):
        od: Dict[str, Any] = {}
        u = False
        for k, v in obj.items():
            rk, uk = _redact_str(str(k), counts, hits, hashes, item, where + ".<key>")
            rv, uv = redact_obj(v, counts, hits, hashes, item, "%s.%s" % (where, rk[:40]), stats)
            od[rk] = rv
            u |= uk or uv
        return od, u
    return obj, False


def residual_in_obj(obj: Any) -> Dict[str, int]:
    """``residual_matches`` over every string (keys included) in their REAL form. The serialized JSON is not
    checked: its ``\\n`` escapes glue consecutive lines into one and ``kv_bare_value`` then fires on
    ``label:\\nnext line`` although ``redact_text`` already judged the multi-line text clean (T16-1 finding)."""
    counts: Counter = Counter()
    if isinstance(obj, str):
        counts.update(redact.residual_matches(obj))
    elif isinstance(obj, list):
        for v in obj:
            counts.update(residual_in_obj(v))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            counts.update(redact.residual_matches(str(k)))
            counts.update(residual_in_obj(v))
    return dict(counts)


def canonical_sha(obj: Any) -> str:
    return vaultlib.sha256_text(json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":")))


# --------------------------------------------------------------------------- export

def _plan_parts(merged: list, max_bytes: int, report: Report) -> List[Any]:
    warnings: List[dict] = []
    parts = shard_json(merged, max_bytes, warnings) if merged else []
    report.parts = [{"index": i, "elements": len(p), "bytes": vaultlib.utf8_len(_dumps(p)), "sha256": vaultlib.sha256_text(_dumps(p))}
                    for i, p in enumerate(parts, 1)]
    report.oversize = warnings
    return parts


def _roundtrip(parts: List[Any], max_bytes: int, warnings: List[dict], expected_sha: str) -> bool:
    """Write the parts into a temp dir OUTSIDE the repo, reassemble, compare canonical sha256."""
    if not parts:
        return True
    base = Path(os.environ.get("LOCALAPPDATA", tempfile.gettempdir())) / "Temp" / "opencode"
    base = base if base.is_dir() else Path(tempfile.gettempdir())
    with tempfile.TemporaryDirectory(prefix="vault-ledger-rt-", dir=str(base)) as tmp:
        pj = write_shards(Path(tmp) / BASE_NAME, parts, ".json", max_bytes=max_bytes, warnings=warnings)
        back = read_shards(pj)
    return canonical_sha(back) == expected_sha


def _write_parts(out_dir: Path, parts: List[Any], max_bytes: int, warnings: List[dict]) -> None:
    """Idempotent equivalent of ``write_shards`` (same file names and ``parts.json`` layout, unchanged files untouched)."""
    count = len(parts)
    entries: List[dict] = []
    names: List[str] = []
    total = 0
    for i, part in enumerate(parts, 1):
        text = _dumps(part)
        fname = BASE_NAME + ".json" if count == 1 else "%s.part%03d.json" % (BASE_NAME, i)
        _write_if_changed(out_dir / fname, text)
        size = vaultlib.utf8_len(text)
        total += size
        names.append(fname)
        entries.append({"file": fname, "bytes": size, "sha256": vaultlib.sha256_text(text)})
    oversize = []
    for w in warnings:
        w2 = dict(w)
        if isinstance(w2.get("part"), int) and 1 <= w2["part"] <= count:
            w2["file"] = names[w2["part"] - 1]
        oversize.append(w2)
    meta = {"source": BASE_NAME, "ext": ".json", "max_bytes": max_bytes, "count": count, "parts": entries,
            "total_bytes": total, "oversize_warnings": oversize}
    _write_if_changed(out_dir / (BASE_NAME + ".parts.json"), json.dumps(meta, indent=2, ensure_ascii=False) + "\n")


def export(state_path=DEFAULT_STATE, out_dir=DEFAULT_OUT, *, dry_run: bool = False, max_bytes: int = JSON_MAX,
           top_n: int = 20, review_dir=MANIFEST_DIR) -> Tuple[Report, dict]:
    out_dir = Path(out_dir)
    state = load_state(state_path)
    copy, sha_expected, n_files, n_items = snapshot_dir(state)
    files = list_files(copy)
    verify_dir(files, sha_expected)
    report = Report(files_total=n_files, items_total=n_items)
    if len(files) != n_files:
        report.warnings.append("files in copy %d != files_total %d" % (len(files), n_files))
    hashes = load_review_hashes(REVIEW_PROJECT, Path(review_dir))
    merged: List[Any] = []
    seen: Dict[str, str] = {}
    for p in files:
        name = p.name
        if redact.is_denied_path(name, "READ"):
            report.skipped_denied.append(name)
            continue
        raw = vaultlib.read_text(p)
        try:
            obj = json.loads(raw)
        except ValueError:
            report.skipped_parse.append(name)
            continue
        n = _item_count(obj)
        counts: Counter = Counter()
        hits: List[dict] = []
        stats: Counter = Counter()
        item = name.rsplit(".", 1)[0]
        red, unresolved = redact_obj(obj, counts, hits, hashes, item, stats=stats)
        if unresolved:
            report.skipped_sensitive.append(name)
            report.items_skipped += n
            continue
        if isinstance(red, dict):
            element: Any = {SOURCE_FIELD: name}
            element.update(red)
        else:
            element = {SOURCE_FIELD: name, "value": red}
        text = _dumps(element)
        left = residual_in_obj(element)
        if left:
            raise ExportError("residual matches in %s: %s" % (name, sorted(left)))
        sha = canonical_sha(red)
        if sha in seen:
            report.skipped_duplicate.append(name)
            report.items_skipped += n
            continue
        seen[sha] = name
        merged.append(element)
        report.exported.append(name)
        report.items_exported += n
        report.counts.update(counts)
        if counts:
            report.per_file[name] = counts
        for h in hits:
            report.entropy_hits.append({"item": h["item"], "where": h["where"], "sha256": h["sha256"], "length": h["length"],
                                        "entropy": h["entropy"], "context_hint": h["context_hint"],
                                        "charset": h["charset"], "readable": bool(h["readable"])})
        report.file_shapes[name] = {"bytes_in": vaultlib.utf8_len(raw), "bytes_out": vaultlib.utf8_len(text),
                                    "keys": n, "strings": stats["strings"], "sha256_out": sha}
    report.merged_sha256 = canonical_sha(merged)
    report.merged_bytes = vaultlib.utf8_len(_dumps(merged)) if merged else 0
    parts = _plan_parts(merged, max_bytes, report)
    if dry_run:
        report.roundtrip_ok = _roundtrip(parts, max_bytes, report.oversize, report.merged_sha256)
    elif merged:
        _write_parts(out_dir, parts, max_bytes, report.oversize)
        back = read_shards(out_dir / (BASE_NAME + ".parts.json"))
        report.roundtrip_ok = canonical_sha(back) == report.merged_sha256
        if not report.roundtrip_ok:
            raise ExportError("written parts do not reassemble to the redacted ledger")
    manifest = build_manifest(report, dry_run, top_n, max_bytes)
    if not dry_run and merged:
        _write_if_changed(out_dir / "AUDIT.md", render_audit(manifest))
        _write_if_changed(out_dir / "SUMMARY.md", render_summary(manifest))
    return report, manifest


def _top(report: Report, n: int) -> List[dict]:
    ranked = sorted(report.per_file.items(), key=lambda kv: (-sum(kv[1].values()), kv[0]))
    return [{"file": name, "total": sum(c.values()), "by_category": dict(sorted(c.items()))} for name, c in ranked[:n]]


def build_manifest(report: Report, dry_run: bool, top_n: int, max_bytes: int) -> dict:
    return {
        "tool": "export_ledger",
        "version": TOOL_VERSION,
        "dry_run": bool(dry_run),
        "max_bytes": max_bytes,
        "forensic_skipped_as_duplicate": True,
        "files_total": report.files_total,
        "items_total": report.items_total,
        "exported": len(report.exported),
        "skipped": {"sensitive": len(report.skipped_sensitive), "duplicate": len(report.skipped_duplicate),
                    "denied": len(report.skipped_denied), "parse_error": len(report.skipped_parse)},
        "skipped_total": report.skipped,
        "match_files": report.match_files,
        "items_exported": report.items_exported,
        "items_skipped": report.items_skipped,
        "match_items": report.match_items,
        "merged_sha256": report.merged_sha256,
        "merged_bytes": report.merged_bytes,
        "sharded": len(report.parts) > 1,
        "parts_planned": len(report.parts),
        "largest_part_bytes": max((p["bytes"] for p in report.parts), default=0),
        "parts": report.parts,
        "oversize_warnings": report.oversize,
        "roundtrip_ok": report.roundtrip_ok,
        "redactions_by_kind": dict(sorted(report.counts.items())),
        "entropy_hits": report.entropy_hits,
        "residual": 0,
        "top_redacted": _top(report, top_n),
        "files": dict(sorted(report.file_shapes.items())),
        "skipped_sensitive": sorted(report.skipped_sensitive),
        "skipped_duplicate": sorted(report.skipped_duplicate),
        "skipped_denied": sorted(report.skipped_denied),
        "skipped_parse": sorted(report.skipped_parse),
        "warnings": report.warnings,
    }


def render_report(manifest: dict) -> str:
    L = ["# T16 dry-run — LEDGER export (counts, hashes and shapes only)", ""]
    L.append("- dry_run: %s · forensic_skipped_as_duplicate: %s" % (manifest["dry_run"], manifest["forensic_skipped_as_duplicate"]))
    L.append("- files_total: %d · items_total: %d" % (manifest["files_total"], manifest["items_total"]))
    sk = manifest["skipped"]
    L.append("- exported: %d · skipped: %d (sensitive=%d, duplicate=%d, denied=%d, parse_error=%d) · match_files: %s" % (
        manifest["exported"], manifest["skipped_total"], sk["sensitive"], sk["duplicate"], sk["denied"], sk["parse_error"], manifest["match_files"]))
    L.append("- items_exported: %d · items_skipped: %d · match_items: %s" % (manifest["items_exported"], manifest["items_skipped"], manifest["match_items"]))
    L.append("- merged_bytes: %s · merged_sha256: `%s`" % (format(manifest["merged_bytes"], ","), manifest["merged_sha256"]))
    L.append("- sharded: %s · parts_planned: %d · largest_part_bytes: %s · max_bytes: %s · oversize: %d · roundtrip_ok: %s · residual: %d" % (
        manifest["sharded"], manifest["parts_planned"], format(manifest["largest_part_bytes"], ","), format(manifest["max_bytes"], ","),
        len(manifest["oversize_warnings"]), manifest["roundtrip_ok"], manifest["residual"]))
    if manifest["warnings"]:
        L += ["- warnings:"] + ["  - " + w for w in manifest["warnings"]]
    L += ["", "## Planned parts (index → elements → bytes → sha256)", ""]
    L += ["- %d → %d → %s → `%s`" % (p["index"], p["elements"], format(p["bytes"], ","), p["sha256"]) for p in manifest["parts"]] or ["- (none)"]
    L += ["", "## Redaction counts by category", ""]
    L += ["- %s: %d" % kv for kv in manifest["redactions_by_kind"].items()] or ["- (none)"]
    L += ["", "## Top redacted files (file → total → by category)", ""]
    L += ["- %s → %d → %s" % (t["file"], t["total"], json.dumps(t["by_category"], ensure_ascii=False)) for t in manifest["top_redacted"]] or ["- (none)"]
    hits = manifest["entropy_hits"]
    L += ["", "## HIGH_ENTROPY hits: %d (record only, shapes)" % len(hits), ""]
    shapes = Counter((h["length"], h["entropy"], h["charset"], "readable" if h["readable"] else "opaque", h["context_hint"] or "<none>") for h in hits)
    L += ["- len=%d entropy=%.3f charset=%s %s hint=%s ×%d" % (k + (c,)) for k, c in shapes.most_common(30)] or ["- (none)"]
    L.append("- opaque: %d · readable: %d · distinct sha256: %d" % (
        sum(1 for h in hits if not h["readable"]), sum(1 for h in hits if h["readable"]), len({h["sha256"] for h in hits if h["sha256"]})))
    L += ["", "## Skipped (file names only)", ""]
    for key in ("skipped_sensitive", "skipped_duplicate", "skipped_denied", "skipped_parse"):
        L.append("- %s: %s" % (key, ", ".join("`%s`" % n for n in manifest[key]) or "(none)"))
    return "\n".join(L) + "\n"


def render_audit(manifest: dict) -> str:
    L = ["# AUDIT — conversations/ledger (counts and hashes only)", "",
         "- tool: export_ledger %s" % manifest["version"],
         "- FORENSIC_DATABASE: NOT exported - 100%% duplicate of LEDGER (T0: 453/453 items identical by canonical sha256; Q5) · forensic_skipped_as_duplicate: %s" % manifest["forensic_skipped_as_duplicate"],
         "- files_total: %d · exported: %d · skipped: %d · match_files: %s" % (manifest["files_total"], manifest["exported"], manifest["skipped_total"], manifest["match_files"]),
         "- items_total: %d · items_exported: %d · items_skipped: %d · match_items: %s" % (manifest["items_total"], manifest["items_exported"], manifest["items_skipped"], manifest["match_items"]),
         "- merged canonical sha256: `%s` · roundtrip_ok: %s · residual: %d" % (manifest["merged_sha256"], manifest["roundtrip_ok"], manifest["residual"]),
         "", "## Parts", ""]
    L += ["- part %03d: %d elements, %s bytes, sha256 `%s`" % (p["index"], p["elements"], format(p["bytes"], ","), p["sha256"]) for p in manifest["parts"]]
    L += ["", "## Redactions by category", ""] + (["- %s: %d" % kv for kv in manifest["redactions_by_kind"].items()] or ["- (none)"])
    L += ["", "## Elements (source file → keys → bytes out → sha256 out)", ""]
    L += ["- %s → %d → %s → `%s`" % (n, f["keys"], format(f["bytes_out"], ","), f["sha256_out"]) for n, f in manifest["files"].items()]
    return "\n".join(L) + "\n"


def render_summary(manifest: dict) -> str:
    return "\n".join([
        "# SUMMARY — LEDGER export", "",
        "- %d LEDGER files → %d elements in %d JSON part(s) (≤ %s bytes each, largest %s) + `ledger.parts.json`." % (
            manifest["files_total"], manifest["exported"], manifest["parts_planned"], format(manifest["max_bytes"], ","), format(manifest["largest_part_bytes"], ",")),
        "- FORENSIC_DATABASE is a 100% duplicate of LEDGER (T0) and is not exported (Q5).",
        "- Every string is redacted (`[REDACTED:*]`), home paths become `~`; HIGH_ENTROPY hits recorded by hash only.",
        "- Reassemble with `tools.shard.read_shards('conversations/ledger/ledger.parts.json')`; canonical sha256 `%s`." % manifest["merged_sha256"],
        "- EN: %d files, %d elements, %d part(s); FORENSIC skipped as duplicate; see AUDIT.md for per-element hashes." % (
            manifest["files_total"], manifest["exported"], manifest["parts_planned"]),
    ]) + "\n"


# --------------------------------------------------------------------------- CLI

def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Export the LEDGER snapshot as redacted, sharded JSON.")
    ap.add_argument("--dry-run", action="store_true", help="write nothing under --out (manifest + report only)")
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--state", default=str(DEFAULT_STATE))
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    ap.add_argument("--report", default=str(DEFAULT_REPORT))
    ap.add_argument("--max-bytes", type=int, default=JSON_MAX)
    ap.add_argument("--review-dir", default=str(MANIFEST_DIR))
    a = ap.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass
    try:
        report, manifest = export(a.state, a.out, dry_run=a.dry_run, max_bytes=a.max_bytes, top_n=a.top, review_dir=a.review_dir)
    except (ExportError, OSError, ValueError) as exc:
        print("[export_ledger] ERROR: %s: %s" % (type(exc).__name__, exc))
        return 1
    _write_if_changed(Path(a.manifest), json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    _write_if_changed(Path(a.report), render_report(manifest))
    print("[export_ledger] %sfiles_total=%d items_total=%d exported=%d skipped=%d items_exported=%d items_skipped=%d "
          "match_files=%s match_items=%s parts_planned=%d largest_part_bytes=%d oversize=%d roundtrip_ok=%s residual=%d "
          "redactions=%d entropy_hits=%d forensic_skipped_as_duplicate=%s" % (
              "DRY-RUN " if a.dry_run else "", manifest["files_total"], manifest["items_total"], manifest["exported"],
              manifest["skipped_total"], manifest["items_exported"], manifest["items_skipped"], manifest["match_files"],
              manifest["match_items"], manifest["parts_planned"], manifest["largest_part_bytes"], len(manifest["oversize_warnings"]),
              manifest["roundtrip_ok"], manifest["residual"], sum(manifest["redactions_by_kind"].values()),
              len(manifest["entropy_hits"]), manifest["forensic_skipped_as_duplicate"]))
    ok = manifest["match_files"] and manifest["match_items"] and manifest["roundtrip_ok"] is not False
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
