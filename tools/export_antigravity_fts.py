"""T14 - Export Antigravity ``conversations_fts`` (FTS5 chunks) into ``conversations/antigravity/YYYY-MM/*.md``.

Source (PLAN section 4, Q3/Q16): the same snapshot copy of ``conversation_summaries.db`` named in
``_local/SNAPSHOT_STATE.json`` - opened read-only after its sha256 is verified (functions reused from
``export_summaries``). ``chunk_count`` is ``rows_by_table["conversations_fts"]`` from the state file and
``conv_count`` is ``COUNT(DISTINCT conversation_id)`` on the copy - never constants.

One markdown file per conversation: a bullet front-matter (id, title, date, workspace, project, steps, chunks,
archived, summary header of at most HEADER_MAX_LINES short lines taken from the matching
``conversation_summaries`` row) followed by every chunk in numeric ``chunk_index`` order as
``## chunk N (steps a-b)`` / ``### user`` / ``### agent``. The date and title come from ``conversation_summaries``
first, then from the chunk rows (integer nanoseconds), else the file goes to ``unknown-date/``.

Redaction: ``redact_text`` on every title / workspace / project / body (two passes inside), optional hash-pinned
values from ``_local/manifests/S3/antigravity_fts.review.json`` (same ``_hash_redact`` as copy_sources),
``residual_matches == {}`` per file or nothing is written. A conversation with any chunk reporting
``unresolved_private_key`` is skipped whole (Q6) and its chunks are counted under ``chunks_skipped``.
Files larger than ``MD_MAX`` are sharded at ``## chunk`` boundaries (``shard_markdown`` cuts at ``\n## `` first).

``--dry-run`` writes nothing under the output directory; manifest and report (counts and shapes only) are always
produced. Writes are idempotent.

CLI: python tools/export_antigravity_fts.py [--dry-run] [--top 20] [--state PATH] [--out DIR]
     [--manifest PATH] [--report PATH] [--max-bytes N] [--review-dir DIR]
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

if __package__ in (None, ""):  # executed as a script: make ``tools`` importable
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import redact, vaultlib  # noqa: E402
from tools.copy_sources import _hash_redact, _write_if_changed, clean_whitespace  # noqa: E402
from tools.export_memory import load_review_hashes  # noqa: E402
from tools.export_summaries import (  # noqa: E402
    DEFAULT_STATE, UNKNOWN, ExportError, _qi, _raw, _redact_into, _text, _uri, load_state, parse_time,
    printable_segments, read_rows, snapshot_copy, verify_copy, workspace_short)
from tools.shard import MD_MAX, shard_markdown, write_shards  # noqa: E402

TOOL_VERSION = "1.0.0"
TABLE = "conversations_fts"
REPO = vaultlib.repo_root()
DEFAULT_OUT = REPO / "conversations" / "antigravity"
MANIFEST_DIR = REPO / "_local" / "manifests" / "S3"
DEFAULT_MANIFEST = MANIFEST_DIR / "antigravity_fts.manifest.json"
DEFAULT_REPORT = REPO / "_local" / "T14_DRYRUN.md"
REVIEW_PROJECT = "antigravity_fts"  # -> <review dir>/antigravity_fts.review.json
HEADER_MAX_LINES = 3
HEADER_MAX_CHARS = 200
SLUG_MAX = 40
NS_THRESHOLD = 10 ** 16  # last_modified_time in conversations_fts is integer nanoseconds (0 on most chunks)

# Exported columns; ``*_byte_offsets`` and ``last_step_created_at`` are technical and dropped (T14 brief).
COLS = ("conversation_id", "chunk_index", "chunk_first_step", "chunk_last_step", "last_modified_time",
        "step_count", "archived", "title", "workspace", "project", "user_body", "agent_body")

_WS = re.compile(r"\s+")
_SEP = re.compile(r"[-_]+")
_ALPHA = re.compile(r"^[A-Za-z]+$")
_VOWEL = re.compile(r"[aeiouAEIOU]")


@dataclass
class Conv:
    cid: str
    month: str
    date: str
    title: str
    workspace: str
    project: str
    steps: int
    chunks: int
    archived: bool
    header: List[str]
    body: str
    counts: Counter = field(default_factory=Counter)


@dataclass
class Report:
    chunk_count: int = 0
    conv_count: int = 0
    exported: List[str] = field(default_factory=list)
    skipped_sensitive: List[dict] = field(default_factory=list)  # {"id", "chunks"}
    skipped_empty: List[dict] = field(default_factory=list)
    skipped_other: List[dict] = field(default_factory=list)
    chunks_exported: int = 0
    chunks_skipped: int = 0
    counts: Counter = field(default_factory=Counter)
    entropy_hits: List[dict] = field(default_factory=list)
    per_conv: Dict[str, Counter] = field(default_factory=dict)
    files: Dict[str, dict] = field(default_factory=dict)
    months: Dict[str, dict] = field(default_factory=dict)
    sharded: int = 0
    with_header: int = 0
    blob_stats: Counter = field(default_factory=Counter)

    @property
    def skipped(self) -> int:
        return len(self.skipped_sensitive) + len(self.skipped_empty) + len(self.skipped_other)

    @property
    def match_conv(self) -> bool:
        return len(self.exported) + self.skipped == self.conv_count

    @property
    def match_chunks(self) -> bool:
        return self.chunks_exported + self.chunks_skipped == self.chunk_count


# --------------------------------------------------------------------------- snapshot access

def chunk_count_from_state(state: dict) -> int:
    src = (state.get("sources") or {}).get("conversation_summaries") or {}
    n = (src.get("rows_by_table") or {}).get(TABLE)
    if not isinstance(n, int):
        raise ExportError("state has no rows_by_table[%s]" % TABLE)
    return n


def read_chunks(copy: Path) -> List[dict]:
    """All chunk rows (COLS that exist) ordered by conversation_id then numeric chunk_index (read-only open)."""
    con = sqlite3.connect(_uri(copy), uri=True)
    try:
        cols = [r[1] for r in con.execute("PRAGMA table_info(%s)" % _qi(TABLE))]
        if not cols:
            raise ExportError("table %s not found in snapshot copy" % TABLE)
        use = [c for c in COLS if c in cols]
        for need in ("conversation_id", "chunk_index"):
            if need not in use:
                raise ExportError("table %s has no %s column" % (TABLE, need))
        sql = "SELECT %s FROM %s ORDER BY conversation_id, CAST(chunk_index AS INTEGER)" % (
            ", ".join(_qi(c) for c in use), _qi(TABLE))
        return [dict(zip(use, row)) for row in con.execute(sql)]
    finally:
        con.close()


def count_conversations(copy: Path) -> int:
    con = sqlite3.connect(_uri(copy), uri=True)
    try:
        return int(con.execute("SELECT COUNT(DISTINCT conversation_id) FROM %s" % _qi(TABLE)).fetchone()[0])
    finally:
        con.close()


# --------------------------------------------------------------------------- helpers

def chunk_time(value) -> Tuple[Optional[str], str, str]:
    """``parse_time`` for the fts column: integer nanoseconds become seconds; 0 / None mean unknown."""
    if isinstance(value, (int, float)) and value >= NS_THRESHOLD:
        value = value / 1e9
    if not value:
        return None, "", ""
    return parse_time(value)


def _charset(tok: str) -> str:
    if re.fullmatch(r"[0-9a-f]+", tok):
        return "hex"
    if re.fullmatch(r"[A-Za-z0-9+/]+=*", tok) and ("+" in tok or "=" in tok):
        return "base64-std"
    if re.fullmatch(r"[A-Za-z0-9]+", tok):
        return "alnum"
    if re.fullmatch(r"[A-Za-z0-9\-]+", tok):
        return "kebab"
    if re.fullmatch(r"[A-Za-z0-9_]+", tok):
        return "snake"
    if re.fullmatch(r"[A-Za-z0-9_\-]+", tok):
        return "kebab+snake"
    return "mixed"


def _readable(tok: str) -> bool:
    """True when the token is a run of lexical segments (letters with vowels, almost no digits): a path piece."""
    segs = [s for s in _SEP.split(tok) if s]
    if not segs or sum(c.isdigit() for c in tok) > 0.1 * len(tok):
        return False
    lex = sum(1 for s in segs if _ALPHA.match(s) and 2 <= len(s) <= 24 and _VOWEL.search(s))
    return lex >= 0.8 * len(segs)


def _shape_hits(text: str, hits: List[dict]) -> None:
    """Add ``charset`` / ``readable`` to each entropy hit from the matching token (the token is never stored)."""
    for h in hits:
        if "charset" in h:
            continue
        key = (h["length"], h["entropy"])
        for m in redact._TOKEN.finditer(text):
            tok = m.group()
            if (len(tok), round(redact.shannon_entropy(tok), 3)) == key:
                h["charset"] = _charset(tok)
                h["readable"] = _readable(tok)
                break
        else:
            h["charset"], h["readable"] = "?", False


def _redact_block(text: str, counts: Counter, hits: List[dict], hashes) -> Tuple[str, bool]:
    """Multi-line redaction (line structure kept for bodies) + optional hash-pinned values."""
    if not text:
        return "", False
    # LF-normalize BEFORE redaction (as copy_sources._read_source does): ``^...$`` line patterns such as
    # env_assignment_line do not match before a stray ``\r``, while clean_whitespace() would later turn
    # CRLF into LF and residual_matches() would then see the un-redacted line.
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    res = redact.redact_text(text)
    counts.update(res.counts)
    local: List[dict] = list(res.entropy_hits)
    out = res.text
    if hashes:
        out = _hash_redact(out, hashes, counts, local)
    _shape_hits(out, local)
    hits.extend(local)
    return out.strip(), res.unresolved_private_key


def _line(text: str, counts: Counter, hits: List[dict], hashes) -> Tuple[str, bool]:
    out, u = _redact_block(text, counts, hits, hashes)
    return _WS.sub(" ", out).strip(), u


def _short(s: str) -> str:
    s = _WS.sub(" ", s).strip()
    return s if len(s) <= HEADER_MAX_CHARS else s[:HEADER_MAX_CHARS - 1].rstrip() + "…"


def summary_header(srow: Optional[dict], counts: Counter, hits: List[dict], stats: Counter) -> Tuple[List[str], bool]:
    """At most HEADER_MAX_LINES short lines from the summaries row: preview first, then raw_summary segments."""
    if not srow:
        return [], False
    lines: List[str] = []
    unresolved = False
    preview, u = _redact_into(_raw(srow.get("preview")), counts, hits)
    unresolved |= u
    if preview:
        lines.append(_short(preview))
    raw_title, raw_preview = _text(srow.get("title")), _text(srow.get("preview"))
    for seg in printable_segments(srow.get("raw_summary"), raw_title, raw_preview, stats):
        if len(lines) >= HEADER_MAX_LINES:
            break
        r, u = _redact_into(seg, counts, hits)
        unresolved |= u
        r = _short(r)
        if r and r not in lines:
            lines.append(r)
    return lines[:HEADER_MAX_LINES], unresolved


def slug_of(title: str) -> str:
    """Filename slug capped at SLUG_MAX characters. Dots become ``_`` first: ``sanitize_filename`` keeps
    everything after the last dot as an *extension* when truncating, so a title such as ``a.b<300 chars>``
    came back hundreds of characters long and the Windows path limit then failed the write (T14-2)."""
    s = vaultlib.sanitize_filename(_WS.sub("-", title.strip()).replace(".", "_"), SLUG_MAX)
    s = s.strip("_-. ")[:SLUG_MAX].strip("_-. ")
    return s or "untitled"


def rel_path(conv: Conv) -> str:
    base = "%s_%s" % (slug_of(conv.title), conv.cid[:8])
    if conv.month == UNKNOWN:
        return "%s/%s.md" % (UNKNOWN, base)
    return "%s/%s_%s.md" % (conv.month, conv.date[:10], base)


# --------------------------------------------------------------------------- build / render

def _int(v) -> int:
    try:
        return int(v or 0)
    except (TypeError, ValueError):
        return 0


def build_conversation(cid: str, rows: Sequence[dict], srow: Optional[dict], report: Report, hashes) -> Optional[Conv]:
    counts: Counter = Counter()
    hits: List[dict] = []
    unresolved = False
    # title / date: summaries row first, then the chunk rows, else unknown
    title_raw = _raw((srow or {}).get("title")) or next((_raw(r.get("title")) for r in rows if _raw(r.get("title"))), "")
    title, u = _line(title_raw, counts, hits, hashes)
    unresolved |= u
    month, date, _ = parse_time((srow or {}).get("last_modified_time")) if srow else (None, "", "")
    if not month:
        best = max((_int(r.get("last_modified_time")) for r in rows), default=0)
        month, date, _ = chunk_time(best)
    ws_raw = next((_raw(r.get("workspace")) for r in rows if _raw(r.get("workspace"))), "") or _text((srow or {}).get("workspace_uris"))
    ws, u = workspace_short(ws_raw, counts, hits)
    unresolved |= u
    project, u = _line(next((_raw(r.get("project")) for r in rows if _raw(r.get("project"))), ""), counts, hits, hashes)
    unresolved |= u
    header, u = summary_header(srow, counts, hits, report.blob_stats)
    unresolved |= u
    parts: List[str] = []
    for r in rows:
        user, u1 = _redact_block(_raw(r.get("user_body")), counts, hits, hashes)
        agent, u2 = _redact_block(_raw(r.get("agent_body")), counts, hits, hashes)
        unresolved |= u1 or u2
        parts.append("## chunk %d (steps %d–%d)\n\n### user\n\n%s\n\n### agent\n\n%s\n" % (
            _int(r.get("chunk_index")), _int(r.get("chunk_first_step")), _int(r.get("chunk_last_step")),
            user or "(empty)", agent or "(empty)"))
    if unresolved:
        report.skipped_sensitive.append({"id": cid, "chunks": len(rows)})
        report.chunks_skipped += len(rows)
        return None
    report.counts.update(counts)
    if counts:
        report.per_conv[cid] = counts
    for h in hits:
        report.entropy_hits.append({"item": cid[:8], "length": h["length"], "entropy": h["entropy"],
                                    "context_hint": h["context_hint"], "charset": h.get("charset", "?"),
                                    "readable": bool(h.get("readable"))})
    if header:
        report.with_header += 1
    return Conv(cid=cid, month=month or UNKNOWN, date=date, title=title, workspace=", ".join(ws), project=project,
                steps=max((_int(r.get("step_count")) for r in rows), default=0), chunks=len(rows),
                archived=any(_int(r.get("archived")) for r in rows), header=header, body="\n".join(parts), counts=counts)


def render(conv: Conv) -> str:
    L = ["# " + (conv.title or conv.cid[:8]), "", "- id: `%s`" % conv.cid]
    if conv.title:
        L.append("- title: " + conv.title)
    L.append("- date: " + (conv.date or UNKNOWN))
    if conv.workspace:
        L.append("- workspace: " + conv.workspace)
    if conv.project:
        L.append("- project: " + conv.project)
    L.append("- steps: %d" % conv.steps)
    L.append("- chunks: %d" % conv.chunks)
    L.append("- archived: %s" % ("true" if conv.archived else "false"))
    if conv.header:
        L.append("- summary:")
        L += ["  - " + h for h in conv.header]
    return clean_whitespace("\n".join(L) + "\n\n" + conv.body)


# --------------------------------------------------------------------------- export

def export(state_path=DEFAULT_STATE, out_dir=DEFAULT_OUT, *, dry_run: bool = False, max_bytes: int = MD_MAX,
           top_n: int = 20, review_dir=MANIFEST_DIR) -> Tuple[Report, dict]:
    out_dir = Path(out_dir)
    state = load_state(state_path)
    copy, sha_expected, _ = snapshot_copy(state)
    verify_copy(copy, sha_expected)
    report = Report(chunk_count=chunk_count_from_state(state))
    hashes = load_review_hashes(REVIEW_PROJECT, Path(review_dir))
    rows = read_chunks(copy)
    report.conv_count = count_conversations(copy)
    if len(rows) != report.chunk_count:
        report.skipped_other.append({"reason": "row_count_differs", "rows_read": len(rows), "chunk_count": report.chunk_count})
    summaries = {_text(r.get("conversation_id")): r for r in read_rows(copy)}
    groups: Dict[str, List[dict]] = defaultdict(list)
    order: List[str] = []
    for r in rows:
        cid = _text(r.get("conversation_id"))
        if cid not in groups:
            order.append(cid)
        groups[cid].append(r)
    for cid in order:
        group = groups[cid]
        if not cid:
            report.skipped_empty.append({"id": "", "chunks": len(group)})
            report.chunks_skipped += len(group)
            continue
        conv = build_conversation(cid, group, summaries.get(cid), report, hashes)
        if conv is None:
            continue
        text = render(conv)
        left = redact.residual_matches(text)
        if left:
            raise ExportError("residual matches in conversation %s: %s" % (cid[:8], sorted(left)))
        rel = rel_path(conv)
        parts = shard_markdown(text, max_bytes)
        entry = {"bytes": vaultlib.utf8_len(text), "sha256": vaultlib.sha256_text(text), "chunks": conv.chunks, "parts": []}
        if len(parts) > 1:
            stem = rel[:-3]
            entry["parts"] = ["%s.part%03d.md" % (stem, i) for i in range(1, len(parts) + 1)]
            entry["parts_json"] = stem + ".parts.json"
            report.sharded += 1
        report.files[rel] = entry
        m = report.months.setdefault(conv.month, {"conversations": 0, "chunks": 0, "bytes": 0, "largest_bytes": 0})
        m["conversations"] += 1
        m["chunks"] += conv.chunks
        m["bytes"] += entry["bytes"]
        m["largest_bytes"] = max(m["largest_bytes"], entry["bytes"])
        report.exported.append(cid)
        report.chunks_exported += conv.chunks
        if not dry_run:
            dst = out_dir / rel
            if len(parts) > 1:
                write_shards(dst.with_suffix(""), parts, ".md", max_bytes=max_bytes)
            else:
                _write_if_changed(dst, text)
    return report, build_manifest(report, dry_run, top_n, max_bytes)


def _top(report: Report, n: int) -> List[dict]:
    ranked = sorted(report.per_conv.items(), key=lambda kv: (-sum(kv[1].values()), kv[0]))
    return [{"id": cid[:8], "total": sum(c.values()), "by_category": dict(sorted(c.items()))} for cid, c in ranked[:n]]


def build_manifest(report: Report, dry_run: bool, top_n: int, max_bytes: int) -> dict:
    return {
        "tool": "export_antigravity_fts",
        "version": TOOL_VERSION,
        "dry_run": bool(dry_run),
        "max_bytes": max_bytes,
        "chunk_count": report.chunk_count,
        "conv_count": report.conv_count,
        "exported": len(report.exported),
        "skipped": {"sensitive": len(report.skipped_sensitive), "empty": len(report.skipped_empty),
                    "other": len(report.skipped_other)},
        "skipped_total": report.skipped,
        "chunks_exported": report.chunks_exported,
        "chunks_skipped": report.chunks_skipped,
        "match_conv": report.match_conv,
        "match_chunks": report.match_chunks,
        "files": dict(sorted(report.files.items())),
        "total_bytes": sum(f["bytes"] for f in report.files.values()),
        "months": dict(sorted(report.months.items())),
        "sharded": report.sharded,
        "with_summary_header": report.with_header,
        "raw_summary_decode": dict(sorted(report.blob_stats.items())),
        "redaction_counts": dict(sorted(report.counts.items())),
        "entropy_hits": report.entropy_hits,
        "top_redacted": _top(report, top_n),
        "skipped_sensitive": sorted(report.skipped_sensitive, key=lambda d: d["id"]),
        "skipped_other": report.skipped_other,
    }


def render_report(manifest: dict) -> str:
    L = ["# T14 dry-run — Antigravity conversations_fts export (counts and shapes only)", ""]
    L.append("- dry_run: %s" % manifest["dry_run"])
    L.append("- chunk_count: %d · conv_count: %d" % (manifest["chunk_count"], manifest["conv_count"]))
    sk = manifest["skipped"]
    L.append("- exported: %d · skipped: %d (sensitive=%d, empty=%d, other=%d) · match_conv: %s" % (
        manifest["exported"], manifest["skipped_total"], sk["sensitive"], sk["empty"], sk["other"], manifest["match_conv"]))
    L.append("- chunks_exported: %d · chunks_skipped: %d · match_chunks: %s" % (
        manifest["chunks_exported"], manifest["chunks_skipped"], manifest["match_chunks"]))
    L.append("- total_bytes: %s · sharded conversations: %d · with summary header: %d" % (
        format(manifest["total_bytes"], ","), manifest["sharded"], manifest["with_summary_header"]))
    L.append("- raw_summary decode: " + (", ".join("%s=%d" % kv for kv in manifest["raw_summary_decode"].items()) or "(none)"))
    L += ["", "## Months (month → conversations → chunks → bytes → largest file bytes)", ""]
    for month, m in manifest["months"].items():
        L.append("- %s → %d → %d → %s → %s" % (month, m["conversations"], m["chunks"], format(m["bytes"], ","), format(m["largest_bytes"], ",")))
    L += ["", "## Redaction counts by category", ""]
    L += ["- %s: %d" % kv for kv in manifest["redaction_counts"].items()] or ["- (none)"]
    L += ["", "## Top redacted conversations (short id → total → by category)", ""]
    L += ["- %s → %d → %s" % (t["id"], t["total"], json.dumps(t["by_category"], ensure_ascii=False))
          for t in manifest["top_redacted"]] or ["- (none)"]
    hits = manifest["entropy_hits"]
    L += ["", "## HIGH_ENTROPY hits: %d (record only, shapes)" % len(hits), ""]
    shapes = Counter((h["length"], h["entropy"], h["charset"], "readable" if h["readable"] else "opaque", h["context_hint"] or "<none>") for h in hits)
    L += ["- len=%d entropy=%.3f charset=%s %s hint=%s ×%d" % (k + (c,)) for k, c in shapes.most_common(25)] or ["- (none)"]
    L += ["", "## Skipped sensitive (ids only): %d" % sk["sensitive"], ""]
    L += ["- `%s` (%d chunks)" % (d["id"], d["chunks"]) for d in manifest["skipped_sensitive"]] or ["- (none)"]
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------- CLI

def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Export conversations_fts snapshot to per-conversation markdown.")
    ap.add_argument("--dry-run", action="store_true", help="write nothing under --out (manifest + report only)")
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--state", default=str(DEFAULT_STATE))
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    ap.add_argument("--report", default=str(DEFAULT_REPORT))
    ap.add_argument("--max-bytes", type=int, default=MD_MAX)
    ap.add_argument("--review-dir", default=str(MANIFEST_DIR))
    a = ap.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass
    try:
        report, manifest = export(a.state, a.out, dry_run=a.dry_run, max_bytes=a.max_bytes, top_n=a.top, review_dir=a.review_dir)
    except (ExportError, OSError, sqlite3.DatabaseError, ValueError) as exc:
        print("[export_antigravity_fts] ERROR: %s: %s" % (type(exc).__name__, exc))
        return 1
    _write_if_changed(Path(a.manifest), json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    _write_if_changed(Path(a.report), render_report(manifest))
    print("[export_antigravity_fts] %schunk_count=%d conv_count=%d exported=%d skipped=%d chunks_exported=%d "
          "chunks_skipped=%d match_conv=%s match_chunks=%s files=%d sharded=%d redactions=%d entropy_hits=%d" % (
              "DRY-RUN " if a.dry_run else "", manifest["chunk_count"], manifest["conv_count"], manifest["exported"],
              manifest["skipped_total"], manifest["chunks_exported"], manifest["chunks_skipped"], manifest["match_conv"],
              manifest["match_chunks"], len(manifest["files"]), manifest["sharded"],
              sum(manifest["redaction_counts"].values()), len(manifest["entropy_hits"])))
    return 0 if manifest["match_conv"] and manifest["match_chunks"] else 1


if __name__ == "__main__":
    sys.exit(main())
