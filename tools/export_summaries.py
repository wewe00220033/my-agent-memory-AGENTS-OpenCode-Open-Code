"""T13 - Export Antigravity ``conversation_summaries`` into ``conversations/summaries/YYYY-MM.md``.

Source (PLAN section 4, Q3/Q16): ONLY the snapshot copy named in ``_local/SNAPSHOT_STATE.json``
(``sources.conversation_summaries.copy_path``). The copy's SHA-256 must equal ``sha_copy`` before
anything is read; it is opened through a ``mode=ro`` URI (no ``immutable=1``). ``count(snapshot)``
is ``rows_by_table["conversation_summaries"]`` from the same state file - never a constant.

Per row: text fields -> ``redact_text`` (two passes inside) -> ``raw_summary`` BLOB reduced to printable
runs only (no byte ever leaves) -> grouped by month of ``last_modified_time`` (ISO or epoch) or
``unknown-date`` -> markdown blocks (bullet lists, no tables) -> ``clean_whitespace`` ->
``residual_matches == {}`` (else error, nothing written) -> shard when > ``MD_MAX``.
A row with ``unresolved_private_key`` is skipped as *sensitive* and recorded by id only (Q6).

``--dry-run`` writes nothing under the output directory; the manifest and the human report are
always produced (counts and shapes only, never raw text). Writes are idempotent.

CLI: python tools/export_summaries.py [--dry-run] [--top 20] [--state PATH] [--out DIR]
     [--manifest PATH] [--report PATH] [--max-bytes N]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple
from urllib.parse import unquote

if __package__ in (None, ""):  # executed as a script: make ``tools`` importable
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import redact, vaultlib  # noqa: E402
from tools.copy_sources import _write_if_changed, clean_whitespace  # noqa: E402
from tools.shard import MD_MAX, shard_markdown, write_shards  # noqa: E402

TOOL_VERSION = "1.0.0"
SOURCE_KEY = "conversation_summaries"
TABLE = "conversation_summaries"
REPO = vaultlib.repo_root()
DEFAULT_STATE = REPO / "_local" / "SNAPSHOT_STATE.json"
DEFAULT_OUT = REPO / "conversations" / "summaries"
DEFAULT_MANIFEST = REPO / "_local" / "manifests" / "S3" / "summaries.manifest.json"
DEFAULT_REPORT = REPO / "_local" / "T13_DRYRUN.md"
UNKNOWN = "unknown-date"

# Columns we export (T0 confirmed). Anything else (source/group_id/battle_id/winning_conversation_id/
# app_data_dir/status/project_id/...) is dropped. Missing columns are tolerated (Q3: dynamic schema).
WANTED = ("conversation_id", "title", "preview", "step_count", "last_modified_time", "workspace_uris",
          "agent_name", "parent_conversation_id", "nesting_depth", "raw_summary")

_ISO_MONTH = re.compile(r"^\s*(\d{4})-(\d{2})-(\d{2})")
_EPOCH = re.compile(r"^\s*\d{10}(?:\d{3})?(?:\.\d+)?\s*$")
_PRINTABLE_RUN = re.compile(
    r"[\u0020-\u007e\u00a0-\u024f\u0600-\u06ff\u0750-\u077f\ufb50-\ufdff\ufe70-\ufeff]{12,}")
_LETTER = re.compile(r"[A-Za-z\u00c0-\u024f\u0600-\u06ff\u0750-\u077f\ufb50-\ufdff\ufe70-\ufeff]")
_WS = re.compile(r"\s+")
_FILE_URI = re.compile(r"^file:/{2,3}", re.I)
MIN_SEGMENT = 12
LETTER_RATIO = 0.5


class ExportError(RuntimeError):
    """Snapshot integrity or residual-secret failure: nothing is written."""


@dataclass
class Item:
    cid: str
    sort_key: str
    month: str
    date: str
    steps: int
    depth: int
    title: str
    preview: str
    agent: str
    parent: str
    workspace: str
    summary: str
    redactions: Counter = field(default_factory=Counter)


@dataclass
class Report:
    count_snapshot: int = 0
    exported: List[str] = field(default_factory=list)
    skipped_sensitive: List[str] = field(default_factory=list)
    skipped_empty: List[str] = field(default_factory=list)
    skipped_other: List[dict] = field(default_factory=list)
    counts: Counter = field(default_factory=Counter)
    entropy_hits: List[dict] = field(default_factory=list)
    per_item: Dict[str, Counter] = field(default_factory=dict)
    files: Dict[str, dict] = field(default_factory=dict)
    raw_summary_useful: int = 0
    lmt_shapes: Counter = field(default_factory=Counter)
    blob_stats: Counter = field(default_factory=Counter)  # wire_ok / fallback / empty

    @property
    def skipped(self) -> int:
        return len(self.skipped_sensitive) + len(self.skipped_empty) + len(self.skipped_other)

    @property
    def match(self) -> bool:
        return len(self.exported) + self.skipped == self.count_snapshot


# --------------------------------------------------------------------------- snapshot access

def load_state(path) -> dict:
    return json.loads(vaultlib.read_text(Path(path)))


def snapshot_copy(state: dict) -> Tuple[Path, str, int]:
    """(copy path, expected sha256, count(snapshot)) from the state file - raises ExportError when absent."""
    src = (state.get("sources") or {}).get(SOURCE_KEY)
    if not src or not src.get("copy_path"):
        raise ExportError("state has no %s.copy_path" % SOURCE_KEY)
    copy = Path(os.path.expandvars(src["copy_path"]))
    count = (src.get("rows_by_table") or {}).get(TABLE)
    if not isinstance(count, int):
        raise ExportError("state has no rows_by_table[%s]" % TABLE)
    return copy, str(src.get("sha_copy", "")), count


def verify_copy(copy: Path, sha_expected: str) -> str:
    if not copy.is_file():
        raise ExportError("snapshot copy missing: %s" % copy.name)
    actual = vaultlib.sha256_file(copy)
    if actual != sha_expected:
        raise ExportError("snapshot copy sha256 mismatch for %s (state=%s... actual=%s...)" % (
            copy.name, sha_expected[:12], actual[:12]))
    return actual


def _uri(p: Path) -> str:
    s = str(p.resolve()).replace("\\", "/")
    if not s.startswith("/"):
        s = "/" + s
    return "file:%s?mode=ro" % s


def _qi(ident: str) -> str:
    return '"' + ident.replace('"', '""') + '"'


def read_rows(copy: Path) -> List[dict]:
    """Rows of the summaries table as dicts limited to WANTED columns that really exist (read-only open)."""
    con = sqlite3.connect(_uri(copy), uri=True)
    try:
        cols = [r[1] for r in con.execute("PRAGMA table_info(%s)" % _qi(TABLE))]
        if not cols:
            raise ExportError("table %s not found in snapshot copy" % TABLE)
        use = [c for c in WANTED if c in cols]
        if "conversation_id" not in use:
            raise ExportError("table %s has no conversation_id column" % TABLE)
        sql = "SELECT %s FROM %s" % (", ".join(_qi(c) for c in use), _qi(TABLE))
        return [dict(zip(use, row)) for row in con.execute(sql)]
    finally:
        con.close()


# --------------------------------------------------------------------------- field helpers

def lmt_shape(value) -> str:
    """Shape of a timestamp value (digits -> 9) for the report; never the value itself."""
    return type(value).__name__ + ":" + re.sub(r"\d", "9", str(value))[:40]


def parse_time(value) -> Tuple[Optional[str], str, str]:
    """(month 'YYYY-MM' or None, display date, sort key) from an ISO string or an epoch (s / ms)."""
    if value is None:
        return None, "", ""
    if isinstance(value, (int, float)) or (isinstance(value, str) and _EPOCH.match(value)):
        try:
            num = float(value)
            if num > 1e11:  # milliseconds
                num /= 1000.0
            dt = datetime.fromtimestamp(num, timezone.utc)
        except (OverflowError, OSError, ValueError):
            return None, _WS.sub(" ", str(value)).strip(), str(value)
        iso = dt.strftime("%Y-%m-%d %H:%M:%S")
        return dt.strftime("%Y-%m"), iso, iso
    s = str(value).strip()
    m = _ISO_MONTH.match(s)
    if not m:
        return None, s, s
    return "%s-%s" % (m.group(1), m.group(2)), s[:19].replace("T", " "), s


def _raw(value) -> str:
    """Text of a column as stored (newlines kept so PEM-block detection in redact_text keeps working)."""
    if value is None:
        return ""
    if isinstance(value, bytes):
        value = value.decode("utf-8", "ignore")
    return str(value).strip()


def _text(value) -> str:
    """Single-line display form (whitespace collapsed)."""
    return _WS.sub(" ", _raw(value)).strip()


# --------------------------------------------------------------------------- protobuf wire walk

WIRE_MAX_DEPTH = 3
_CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]")
_STRAY_NEXT = re.compile(r"^(?:@\[|PS |[A-Za-z]:[\\/])")


def _varint(buf: bytes, i: int) -> Tuple[int, int]:
    """(value, index after it); ValueError on truncation or more than 10 bytes."""
    val = shift = 0
    while True:
        if i >= len(buf) or shift > 63:
            raise ValueError("bad varint")
        b = buf[i]
        i += 1
        val |= (b & 0x7F) << shift
        if not b & 0x80:
            return val, i
        shift += 7


def _is_text(s: str) -> bool:
    return len(s.strip()) >= MIN_SEGMENT and not _CONTROL.search(s)


def wire_strings(buf: bytes, depth: int = 0) -> List[str]:
    """Strings of every length-delimited field of a protobuf message, nested messages included (<= WIRE_MAX_DEPTH).

    Walks tag -> wire type: 0 varint (skipped), 1 eight bytes, 5 four bytes, 2 length-delimited. A chunk that
    parses *completely* as a nested message yielding at least one string is taken as such (its first bytes are
    a tag and a length, not text); otherwise it is a string when it decodes as UTF-8 without control characters
    and has >= MIN_SEGMENT chars; anything else is skipped. ValueError on any malformed byte (the caller falls back).
    """
    out: List[str] = []
    i, n = 0, len(buf)
    while i < n:
        tag, i = _varint(buf, i)
        wt, fno = tag & 7, tag >> 3
        if fno == 0:
            raise ValueError("field 0")
        if wt == 0:
            _, i = _varint(buf, i)
        elif wt == 1:
            i += 8
        elif wt == 5:
            i += 4
        elif wt == 2:
            ln, i = _varint(buf, i)
            if i + ln > n:
                raise ValueError("length overrun")
            chunk = buf[i:i + ln]
            i += ln
            nested: List[str] = []
            if chunk and depth < WIRE_MAX_DEPTH:
                try:
                    nested = wire_strings(chunk, depth + 1)
                except ValueError:
                    nested = []
            if nested:
                out.extend(nested)
                continue
            try:
                s = chunk.decode("utf-8")
            except UnicodeDecodeError:
                continue
            if _is_text(s):
                out.append(s)
        else:
            raise ValueError("wire type %d" % wt)
        if i > n:
            raise ValueError("overrun")
    return out


def _strip_stray_length_byte(seg: str) -> str:
    """Fallback only: drop a leading protobuf length byte that happens to be printable and got glued to the run."""
    if len(seg) >= 2 and (ord(seg[0]) in (len(seg) - 1, vaultlib.utf8_len(seg) - 1) or _STRAY_NEXT.match(seg[1:])):
        return seg[1:]
    return seg


def _candidate_strings(raw, stats: Optional[Counter]) -> List[str]:
    """Raw candidate strings of a BLOB: protobuf wire walk first, printable-run regex (with stray-byte drop) on error."""
    if isinstance(raw, bytes):
        try:
            found = wire_strings(raw)
            if stats is not None:
                stats["wire_ok"] += 1
            return found
        except ValueError:
            if stats is not None:
                stats["fallback"] += 1
        text = raw.decode("utf-8", "ignore")
    else:
        if stats is not None:
            stats["fallback"] += 1
        text = str(raw)
    return [_strip_stray_length_byte(seg) for seg in _PRINTABLE_RUN.findall(text)]


def printable_segments(raw, title: str, preview: str, stats: Optional[Counter] = None) -> List[str]:
    """Text segments (>= MIN_SEGMENT chars) of a BLOB that add text beyond title/preview.

    Candidates come from ``_candidate_strings`` (wire walk, regex fallback). Runs that are mostly non-letters,
    that are file/URI paths (already covered by ``workspace``), or that duplicate title/preview are dropped.
    """
    if not raw:
        if stats is not None:
            stats["empty"] += 1
        return []
    out: List[str] = []
    seen = set()
    for seg in _candidate_strings(raw, stats):
        seg = redact._UUID.sub("", seg).strip(" \"'$(#*")
        seg = _WS.sub(" ", seg).strip()
        if len(seg) < MIN_SEGMENT or "://" in seg or _FILE_URI.match(seg):
            continue
        if len(_LETTER.findall(seg)) < LETTER_RATIO * len(seg):
            continue
        if seg in title or seg in preview or seg in seen:
            continue
        seen.add(seg)
        out.append(seg)
    return out


def workspace_labels(ws_json: str) -> List[str]:
    """Normalized workspace entries: percent-decoded, ``file:///`` stripped, home -> ``~`` via redact_text,
    and shortened to the last folder name when the path lives under the home directory."""
    if not ws_json:
        return []
    try:
        items = json.loads(ws_json)
    except ValueError:
        items = [ws_json]
    if isinstance(items, str):
        items = [items]
    out: List[str] = []
    for u in items if isinstance(items, list) else []:
        s = unquote(str(u)).strip()
        s = _FILE_URI.sub("", s).replace("\\", "/")
        if not s:
            continue
        out.append(s)
    return out


def _redact_into(text: str, item_counts: Counter, hits: List[dict]) -> Tuple[str, bool]:
    if not text:
        return "", False
    res = redact.redact_text(text)  # on the raw text: line structure matters for PEM detection
    item_counts.update(res.counts)
    hits.extend(res.entropy_hits)
    return _WS.sub(" ", res.text).strip(), res.unresolved_private_key


def workspace_short(ws_text: str, counts: Counter, hits: List[dict]) -> Tuple[List[str], bool]:
    """Redacted workspace labels, shortened to the last folder name when they live under home (``~``).
    Returns (labels, unresolved_private_key). Shared with export_antigravity_fts (T14)."""
    out: List[str] = []
    unresolved = False
    for w in workspace_labels(ws_text):
        r, u = _redact_into(w, counts, hits)
        unresolved |= u
        if r.startswith("~/") or r == "~":
            r = r.rstrip("/").rsplit("/", 1)[-1] or "~"
        out.append(r)
    return out, unresolved


def build_item(row: dict, report: Report) -> Optional[Item]:
    """Redact one row into an Item; None when it is skipped (recorded in *report*)."""
    cid = _text(row.get("conversation_id"))
    if not cid:
        report.skipped_empty.append("")
        return None
    counts: Counter = Counter()
    hits: List[dict] = []
    unresolved = False
    title, u = _redact_into(_raw(row.get("title")), counts, hits); unresolved |= u
    preview, u = _redact_into(_raw(row.get("preview")), counts, hits); unresolved |= u
    agent, u = _redact_into(_raw(row.get("agent_name")), counts, hits); unresolved |= u
    parent = _text(row.get("parent_conversation_id"))
    ws, u = workspace_short(_text(row.get("workspace_uris")), counts, hits); unresolved |= u
    segs: List[str] = []
    raw_title, raw_preview = _text(row.get("title")), _text(row.get("preview"))
    for seg in printable_segments(row.get("raw_summary"), raw_title, raw_preview, report.blob_stats):
        r, u = _redact_into(seg, counts, hits); unresolved |= u
        if r and r not in segs:
            segs.append(r)
    report.lmt_shapes[lmt_shape(row.get("last_modified_time"))] += 1
    if unresolved:
        report.skipped_sensitive.append(cid)
        return None
    if segs:
        report.raw_summary_useful += 1
    report.counts.update(counts)
    if counts:
        report.per_item[cid] = counts
    for h in hits:
        report.entropy_hits.append({"item": cid[:8], "length": h["length"], "entropy": h["entropy"],
                                    "context_hint": h["context_hint"]})
    month, date, key = parse_time(row.get("last_modified_time"))
    try:
        steps = int(row.get("step_count") or 0)
    except (TypeError, ValueError):
        steps = 0
    try:
        depth = int(row.get("nesting_depth") or 0)
    except (TypeError, ValueError):
        depth = 0
    return Item(cid=cid, sort_key=key, month=month or UNKNOWN, date=date, steps=steps, depth=depth,
                title=title, preview=preview, agent=agent, parent=parent, workspace=", ".join(ws),
                summary=" | ".join(segs), redactions=counts)


# --------------------------------------------------------------------------- rendering

def render_item(it: Item) -> str:
    heading = it.title or it.cid[:8]
    lines = ["## " + heading, "", "- id: `%s`" % it.cid]
    if it.date:
        lines.append("- date: %s" % it.date)
    lines.append("- steps: %d" % it.steps)
    if it.agent:
        lines.append("- agent: %s" % it.agent)
    if it.parent:
        lines.append("- parent: `%s`" % it.parent)
    if it.depth:
        lines.append("- depth: %d" % it.depth)
    if it.workspace:
        lines.append("- workspace: %s" % it.workspace)
    if it.preview:
        lines.append("- preview: %s" % it.preview)
    if it.summary:
        lines.append("- summary: %s" % it.summary)
    return "\n".join(lines) + "\n"


def render_month(month: str, items: Sequence[Item]) -> str:
    ordered = sorted(items, key=lambda i: (i.sort_key, i.cid))
    head = "# Antigravity conversation summaries — %s\n\n- items: %d\n\n" % (month, len(ordered))
    return clean_whitespace(head + "\n".join(render_item(i) for i in ordered))


# --------------------------------------------------------------------------- export

def export(state_path=DEFAULT_STATE, out_dir=DEFAULT_OUT, *, dry_run: bool = False,
           max_bytes: int = MD_MAX, top_n: int = 20) -> Tuple[Report, dict]:
    out_dir = Path(out_dir)
    state = load_state(state_path)
    copy, sha_expected, count = snapshot_copy(state)
    verify_copy(copy, sha_expected)
    report = Report(count_snapshot=count)
    rows = read_rows(copy)
    if len(rows) != count:
        report.skipped_other.append({"reason": "row_count_differs", "rows_read": len(rows), "count_snapshot": count})
    by_month: Dict[str, List[Item]] = defaultdict(list)
    for row in rows:
        it = build_item(row, report)
        if it is not None:
            by_month[it.month].append(it)
    for month in sorted(by_month):
        text = render_month(month, by_month[month])
        left = redact.residual_matches(text)
        if left:
            raise ExportError("residual matches in %s.md: %s" % (month, sorted(left)))
        parts = shard_markdown(text, max_bytes)
        name = month + ".md"
        entry = {"bytes": vaultlib.utf8_len(text), "sha256": vaultlib.sha256_text(text),
                 "items": len(by_month[month]), "parts": []}
        if len(parts) > 1:
            entry["parts"] = ["%s.part%03d.md" % (month, i) for i in range(1, len(parts) + 1)]
            entry["parts_json"] = month + ".parts.json"
        report.files[name] = entry
        report.exported.extend(i.cid for i in by_month[month])
        if not dry_run:
            if len(parts) > 1:
                write_shards(out_dir / month, parts, ".md", max_bytes=max_bytes)
            else:
                _write_if_changed(out_dir / name, text)
    manifest = build_manifest(report, dry_run, top_n, max_bytes)
    return report, manifest


def _top(report: Report, n: int) -> List[dict]:
    ranked = sorted(report.per_item.items(), key=lambda kv: (-sum(kv[1].values()), kv[0]))
    return [{"id": cid[:8], "total": sum(c.values()), "by_category": dict(sorted(c.items()))} for cid, c in ranked[:n]]


def build_manifest(report: Report, dry_run: bool, top_n: int, max_bytes: int) -> dict:
    return {
        "tool": "export_summaries",
        "version": TOOL_VERSION,
        "dry_run": bool(dry_run),
        "max_bytes": max_bytes,
        "count_snapshot": report.count_snapshot,
        "exported": len(report.exported),
        "skipped": {"sensitive": len(report.skipped_sensitive), "empty": len(report.skipped_empty),
                    "other": len(report.skipped_other)},
        "skipped_total": report.skipped,
        "match": report.match,
        "files": dict(sorted(report.files.items())),
        "redaction_counts": dict(sorted(report.counts.items())),
        "entropy_hits": report.entropy_hits,
        "top_redacted": _top(report, top_n),
        "skipped_sensitive_ids": sorted(report.skipped_sensitive),
        "skipped_other": report.skipped_other,
        "raw_summary_useful": report.raw_summary_useful,
        "raw_summary_decode": dict(sorted(report.blob_stats.items())),
        "last_modified_time_shapes": dict(report.lmt_shapes.most_common()),
    }


def render_report(manifest: dict) -> str:
    L = ["# T13 dry-run — conversation summaries export (counts and shapes only)", ""]
    L.append("- dry_run: %s" % manifest["dry_run"])
    L.append("- count_snapshot: %d" % manifest["count_snapshot"])
    L.append("- exported: %d" % manifest["exported"])
    sk = manifest["skipped"]
    L.append("- skipped: %d (sensitive=%d, empty=%d, other=%d)" % (manifest["skipped_total"], sk["sensitive"], sk["empty"], sk["other"]))
    L.append("- exported + skipped == count_snapshot: %s" % manifest["match"])
    L.append("- raw_summary rows with useful extra text: %d" % manifest["raw_summary_useful"])
    L.append("- raw_summary decode: " + (", ".join("%s=%d" % kv for kv in manifest.get("raw_summary_decode", {}).items()) or "(none)"))
    L.append("- last_modified_time shapes: " + ", ".join("`%s` ×%d" % kv for kv in manifest["last_modified_time_shapes"].items()))
    L += ["", "## Months (file → items → expected bytes → parts)", ""]
    for name, f in manifest["files"].items():
        L.append("- %s → %d items → %s bytes%s" % (name, f["items"], format(f["bytes"], ","),
                                                  (" → %d parts" % len(f["parts"])) if f["parts"] else ""))
    L += ["", "## Redaction counts by category", ""]
    L += ["- %s: %d" % kv for kv in manifest["redaction_counts"].items()] or ["- (none)"]
    L += ["", "## Top redacted items (short id → total → by category)", ""]
    L += ["- %s → %d → %s" % (t["id"], t["total"], json.dumps(t["by_category"], ensure_ascii=False))
          for t in manifest["top_redacted"]] or ["- (none)"]
    hits = manifest["entropy_hits"]
    L += ["", "## HIGH_ENTROPY hits: %d (record only, shapes)" % len(hits), ""]
    shapes = Counter((h["length"], h["entropy"], h["context_hint"] or "<none>") for h in hits)
    L += ["- len=%d entropy=%.3f hint=%s ×%d" % (k[0], k[1], k[2], c) for k, c in shapes.most_common(20)] or ["- (none)"]
    L += ["", "## Skipped sensitive (ids only): %d" % sk["sensitive"], ""]
    L += ["- `%s`" % i for i in manifest["skipped_sensitive_ids"]] or ["- (none)"]
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------- CLI

def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Export conversation_summaries snapshot to monthly markdown.")
    ap.add_argument("--dry-run", action="store_true", help="write nothing under --out (manifest + report only)")
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--state", default=str(DEFAULT_STATE))
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    ap.add_argument("--report", default=str(DEFAULT_REPORT))
    ap.add_argument("--max-bytes", type=int, default=MD_MAX)
    a = ap.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass
    try:
        report, manifest = export(a.state, a.out, dry_run=a.dry_run, max_bytes=a.max_bytes, top_n=a.top)
    except (ExportError, OSError, sqlite3.DatabaseError, ValueError) as exc:
        print("[export_summaries] ERROR: %s: %s" % (type(exc).__name__, exc))
        return 1
    _write_if_changed(Path(a.manifest), json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    _write_if_changed(Path(a.report), render_report(manifest))
    print("[export_summaries] %scount_snapshot=%d exported=%d skipped=%d (sensitive=%d empty=%d other=%d) match=%s "
          "files=%d redactions=%d entropy_hits=%d" % (
              "DRY-RUN " if a.dry_run else "", manifest["count_snapshot"], manifest["exported"], manifest["skipped_total"],
              manifest["skipped"]["sensitive"], manifest["skipped"]["empty"], manifest["skipped"]["other"],
              manifest["match"], len(manifest["files"]), sum(manifest["redaction_counts"].values()),
              len(manifest["entropy_hits"])))
    return 0 if manifest["match"] else 1


if __name__ == "__main__":
    sys.exit(main())
