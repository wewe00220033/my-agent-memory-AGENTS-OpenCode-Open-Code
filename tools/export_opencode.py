"""T15 - Export OpenCode ``opencode.db`` sessions into ``conversations/opencode/YYYY-MM/*.md``.

Source (PLAN section 4, Q11/Q12/Q16): the snapshot copy of ``opencode.db`` named under ``sources.opencode`` in
``_local/SNAPSHOT_STATE.json`` - opened read-only after its sha256 is verified. ``session_count`` is
``rows_by_table["session_v2"]`` and ``message_count`` is ``rows_by_table["session_message"]`` - never constants.

T0 facts this relies on: ``session_part`` is empty - the parts live inside ``session_message.data`` (JSON) under
``content[]`` with ``type in {text, reasoning, tool}``; user rows carry ``data.text`` (and ``metadata.displayText``).
Only ``session_message.type in (user, assistant)`` is exported and only ``content[].type == "text"`` parts
(``reasoning`` and ``tool`` parts are dropped and merely counted - Q11/Q12). Every other row type
(idle, system, synthetic, agent-switched, model-switched, compaction) is counted under ``msg_skips["type:<t>"]``.

One markdown file per session: bullet front-matter (id, title, date, directory, parent, agent, model, counts,
children, archived) then every text-bearing message in numeric ``seq`` order as ``## <seq> · <type> (<time>)``.
A child session (``parent_id`` set) is written **under its parent**: ``<month>/<parent_base>/<child>.md`` next to
``<month>/<parent_base>.md``; a child whose parent is not in the snapshot is written like a root session with a
``- parent: ... (not in snapshot)`` line.

Redaction: ``redact_text`` on title / directory / agent / model / every message body (two passes inside), optional
hash-pinned values from ``_local/manifests/S3/opencode.review.json``, ``residual_matches == {}`` per file or nothing
is written. A session with any message reporting ``unresolved_private_key`` is skipped whole (Q6) and its messages
are counted under ``msg_skips["sensitive"]``. Files larger than ``MD_MAX`` are sharded at ``## `` boundaries.

Acceptance (PLAN T15): ``exported + skipped == session_count`` for sessions, ``msgs_exported + msgs_skipped ==
message_count`` for messages, and ``parts_exported`` holds no ``tool`` / ``reasoning`` key.

``--dry-run`` writes nothing under the output directory; manifest and report (counts and shapes only) are always
produced. Writes are idempotent.

CLI: python tools/export_opencode.py [--dry-run] [--top 20] [--state PATH] [--out DIR]
     [--manifest PATH] [--report PATH] [--max-bytes N] [--review-dir DIR]
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
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

if __package__ in (None, ""):  # executed as a script: make ``tools`` importable
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import redact, vaultlib  # noqa: E402
from tools.copy_sources import _write_if_changed, clean_whitespace  # noqa: E402
from tools.export_antigravity_fts import _line, _redact_block, slug_of  # noqa: E402
from tools.export_memory import load_review_hashes  # noqa: E402
from tools.export_summaries import (  # noqa: E402
    DEFAULT_STATE, UNKNOWN, ExportError, _qi, _raw, _uri, load_state, parse_time, verify_copy)
from tools.shard import MD_MAX, shard_markdown, write_shards  # noqa: E402

TOOL_VERSION = "1.0.0"
SOURCE_KEY = "opencode"
SESSIONS = "session_v2"
MESSAGES = "session_message"
EXPORT_TYPES = ("user", "assistant")
TEXT_PART = "text"
REPO = vaultlib.repo_root()
DEFAULT_OUT = REPO / "conversations" / "opencode"
MANIFEST_DIR = REPO / "_local" / "manifests" / "S3"
DEFAULT_MANIFEST = MANIFEST_DIR / "opencode.manifest.json"
DEFAULT_REPORT = REPO / "_local" / "T15_DRYRUN.md"
REVIEW_PROJECT = "opencode"  # -> <review dir>/opencode.review.json
SESSION_COLS = ("id", "project_id", "parent_id", "slug", "directory", "title", "agent", "model",
                "time_created", "time_updated", "time_archived")
MESSAGE_COLS = ("id", "session_id", "type", "seq", "time_created", "data")

_WS = re.compile(r"\s+")


@dataclass
class Msg:
    seq: int
    kind: str
    date: str
    text: str


@dataclass
class Sess:
    sid: str
    parent: str
    month: str
    date: str
    title: str
    directory: str
    agent: str
    model: str
    archived: bool
    msgs: List[Msg]
    rows: int  # user/assistant rows read for this session
    rel: str = ""
    parent_note: str = ""
    children: List[str] = field(default_factory=list)
    counts: Counter = field(default_factory=Counter)

    @property
    def n_user(self) -> int:
        return sum(1 for m in self.msgs if m.kind == "user")

    @property
    def n_assistant(self) -> int:
        return sum(1 for m in self.msgs if m.kind == "assistant")


@dataclass
class Report:
    session_count: int = 0
    message_count: int = 0
    type_counts: Counter = field(default_factory=Counter)
    exported: List[str] = field(default_factory=list)
    skipped_sensitive: List[dict] = field(default_factory=list)  # {"id", "messages"}
    skipped_empty: List[dict] = field(default_factory=list)
    skipped_other: List[dict] = field(default_factory=list)
    msgs_exported: int = 0
    msg_skips: Counter = field(default_factory=Counter)  # type:<t> / empty / parse_error / sensitive / no_session
    parts_seen: Counter = field(default_factory=Counter)
    parts_exported: Counter = field(default_factory=Counter)
    counts: Counter = field(default_factory=Counter)
    entropy_hits: List[dict] = field(default_factory=list)
    per_session: Dict[str, Counter] = field(default_factory=dict)
    files: Dict[str, dict] = field(default_factory=dict)
    months: Dict[str, dict] = field(default_factory=dict)
    sharded: int = 0
    children: int = 0
    orphans: int = 0
    warnings: List[str] = field(default_factory=list)

    @property
    def skipped(self) -> int:
        return len(self.skipped_sensitive) + len(self.skipped_empty) + len(self.skipped_other)

    @property
    def msgs_skipped(self) -> int:
        return sum(self.msg_skips.values())

    @property
    def match_sessions(self) -> bool:
        return len(self.exported) + self.skipped == self.session_count

    @property
    def match_msgs(self) -> bool:
        return self.msgs_exported + self.msgs_skipped == self.message_count


# --------------------------------------------------------------------------- snapshot access

def snapshot_copy(state: dict) -> Tuple[Path, str, int, int]:
    """(copy path, expected sha256, session_count, message_count) from the state file."""
    src = (state.get("sources") or {}).get(SOURCE_KEY)
    if not src or not src.get("copy_path"):
        raise ExportError("state has no %s.copy_path" % SOURCE_KEY)
    copy = Path(os.path.expandvars(src["copy_path"]))
    rbt = src.get("rows_by_table") or {}
    n_sess, n_msg = rbt.get(SESSIONS), rbt.get(MESSAGES)
    if not isinstance(n_sess, int) or not isinstance(n_msg, int):
        raise ExportError("state has no rows_by_table[%s]/[%s]" % (SESSIONS, MESSAGES))
    return copy, str(src.get("sha_copy", "")), n_sess, n_msg


def _select(con: sqlite3.Connection, table: str, wanted: Sequence[str], needed: Sequence[str],
            where: str = "", params: Sequence = (), order: str = "") -> List[dict]:
    cols = [r[1] for r in con.execute("PRAGMA table_info(%s)" % _qi(table))]
    if not cols:
        raise ExportError("table %s not found in snapshot copy" % table)
    use = [c for c in wanted if c in cols]
    for need in needed:
        if need not in use:
            raise ExportError("table %s has no %s column" % (table, need))
    sql = "SELECT %s FROM %s%s%s" % (", ".join(_qi(c) for c in use), _qi(table), where, order)
    return [dict(zip(use, row)) for row in con.execute(sql, tuple(params))]


def read_sessions(copy: Path) -> List[dict]:
    con = sqlite3.connect(_uri(copy), uri=True)
    try:
        return _select(con, SESSIONS, SESSION_COLS, ("id",), order=" ORDER BY time_created, id")
    finally:
        con.close()


def read_messages(copy: Path) -> Tuple[List[dict], Counter]:
    """(user/assistant rows ordered by session then numeric seq, COUNT(*) of every row type)."""
    con = sqlite3.connect(_uri(copy), uri=True)
    try:
        type_counts = Counter({str(t): int(n) for t, n in con.execute(
            "SELECT type, COUNT(*) FROM %s GROUP BY type" % _qi(MESSAGES))})
        rows = _select(con, MESSAGES, MESSAGE_COLS, ("id", "session_id", "type", "seq", "data"),
                       where=" WHERE type IN (%s)" % ",".join("?" * len(EXPORT_TYPES)), params=EXPORT_TYPES,
                       order=" ORDER BY session_id, CAST(seq AS INTEGER), id")
        return rows, type_counts
    finally:
        con.close()


# --------------------------------------------------------------------------- helpers

def short_id(sid: str) -> str:
    """Last 8 characters of the id: OpenCode ids are time-ordered (ULID-like), so their *prefix* collides across
    sessions created close together while the random tail does not."""
    s = sid[4:] if sid.startswith("ses_") else sid
    return s[-8:] or sid[-8:]


def when(value) -> Tuple[Optional[str], str, str]:
    """``parse_time`` for epoch-ms columns; 0 / None mean unknown (as T14 ``chunk_time``)."""
    if not value:
        return None, "", ""
    return parse_time(value)


def _int(v) -> int:
    try:
        return int(v or 0)
    except (TypeError, ValueError):
        return 0


def message_text(data: dict, parts: Counter) -> str:
    """Text of one message: ``content[]`` text parts joined (tool / reasoning parts counted and dropped), else
    ``data.text``, else ``metadata.displayText``. Returns "" when the message carries no text."""
    content = data.get("content")
    if isinstance(content, list):
        texts: List[str] = []
        for p in content:
            if not isinstance(p, dict):
                parts["invalid"] += 1
                continue
            kind = str(p.get("type") or "?")
            parts[kind] += 1
            if kind == TEXT_PART and isinstance(p.get("text"), str) and p["text"].strip():
                texts.append(p["text"].strip())
        return "\n\n".join(texts)
    text = data.get("text")
    if isinstance(text, str) and text.strip():
        parts[TEXT_PART] += 1
        return text.strip()
    meta = data.get("metadata")
    if isinstance(meta, dict) and isinstance(meta.get("displayText"), str) and meta["displayText"].strip():
        parts["displayText"] += 1
        return meta["displayText"].strip()
    return ""


def model_label(value) -> str:
    raw = _raw(value)
    if not raw:
        return ""
    try:
        obj = json.loads(raw)
    except ValueError:
        return raw
    if not isinstance(obj, dict):
        return raw
    label = "/".join(s for s in (str(obj.get("providerID") or ""), str(obj.get("id") or "")) if s)
    if obj.get("variant"):
        label += "#" + str(obj["variant"])
    return label


def dir_short(path: str, counts: Counter, hits: List[dict], hashes) -> Tuple[str, bool]:
    """Redacted directory (home -> ``~``), shortened to its last folder name when it lives under home."""
    r, u = _line(path, counts, hits, hashes)
    r = r.replace("\\", "/")
    if r == "~" or r.startswith("~/"):
        r = r.rstrip("/").rsplit("/", 1)[-1] or "~"
    return r, u


def base_name(s: Sess) -> str:
    base = "%s_%s" % (slug_of(s.title), short_id(s.sid))
    return base if s.month == UNKNOWN else "%s_%s" % (s.date[:10], base)


# --------------------------------------------------------------------------- build / render

def build_session(srow: dict, rows: Sequence[dict], report: Report, hashes) -> Optional[Sess]:
    counts: Counter = Counter()
    hits: List[dict] = []
    local_skips: Counter = Counter()
    local_parts: Counter = Counter()
    local_exported: Counter = Counter()
    unresolved = False
    sid = _raw(srow.get("id"))
    title, u = _line(_raw(srow.get("title")) or _raw(srow.get("slug")), counts, hits, hashes)
    unresolved |= u
    directory, u = dir_short(_raw(srow.get("directory")), counts, hits, hashes)
    unresolved |= u
    agent, u = _line(_raw(srow.get("agent")), counts, hits, hashes)
    unresolved |= u
    model, u = _line(model_label(srow.get("model")), counts, hits, hashes)
    unresolved |= u
    month, date, _ = when(srow.get("time_created"))
    msgs: List[Msg] = []
    for r in rows:
        try:
            data = json.loads(_raw(r.get("data")) or "null")
            if not isinstance(data, dict):
                raise ValueError("data is not an object")
        except (TypeError, ValueError):
            local_skips["parse_error"] += 1
            continue
        text = message_text(data, local_parts)
        if not text:
            local_skips["empty"] += 1
            continue
        red, u = _redact_block(text, counts, hits, hashes)
        unresolved |= u
        if not red:
            local_skips["empty"] += 1
            continue
        local_exported[TEXT_PART] += 1
        _, mdate, _ = when(r.get("time_created"))
        msgs.append(Msg(seq=_int(r.get("seq")), kind=str(r.get("type") or ""), date=mdate, text=red))
    report.parts_seen.update(local_parts)
    if unresolved:
        report.skipped_sensitive.append({"id": sid, "messages": len(rows)})
        report.msg_skips["sensitive"] += len(rows)
        return None
    report.msg_skips.update(local_skips)
    if not msgs:
        report.skipped_empty.append({"id": sid, "messages": len(rows)})
        return None
    report.parts_exported.update(local_exported)
    report.counts.update(counts)
    if counts:
        report.per_session[sid] = counts
    for h in hits:
        report.entropy_hits.append({"item": short_id(sid), "length": h["length"], "entropy": h["entropy"],
                                    "context_hint": h["context_hint"], "charset": h.get("charset", "?"),
                                    "readable": bool(h.get("readable"))})
    return Sess(sid=sid, parent=_raw(srow.get("parent_id")), month=month or UNKNOWN, date=date, title=title,
                directory=directory, agent=agent, model=model, archived=srow.get("time_archived") is not None,
                msgs=msgs, rows=len(rows), counts=counts)


def assign_paths(built: Dict[str, Sess], known_ids: set, report: Report) -> None:
    """``rel`` for every built session: roots at ``<month>/<base>.md``, children at ``<parent dir>/<base>.md``."""
    memo: Dict[str, str] = {}

    def rel_of(sid: str, trail: Tuple[str, ...] = ()) -> str:
        if sid in memo:
            return memo[sid]
        s = built[sid]
        base = base_name(s)
        parent = s.parent
        if parent and parent in built and parent not in trail and parent != sid:
            prel = rel_of(parent, trail + (sid,))
            rel = "%s/%s.md" % (prel[:-3], base)
            built[parent].children.append(base + ".md")
            report.children += 1
        else:
            rel = "%s/%s.md" % (s.month, base)
            if parent:
                s.parent_note = "(skipped)" if parent in known_ids else "(not in snapshot)"
                report.orphans += 1
        memo[sid] = rel
        return rel

    for sid in built:
        built[sid].rel = rel_of(sid)


def render(s: Sess) -> str:
    L = ["# " + (s.title or short_id(s.sid)), "", "- id: `%s`" % s.sid]
    if s.title:
        L.append("- title: " + s.title)
    L.append("- date: " + (s.date or UNKNOWN))
    if s.directory:
        L.append("- directory: " + s.directory)
    if s.parent:
        L.append("- parent: `%s`%s" % (s.parent, (" " + s.parent_note) if s.parent_note else ""))
    if s.agent:
        L.append("- agent: " + s.agent)
    if s.model:
        L.append("- model: " + s.model)
    L.append("- messages: %d (user %d, assistant %d)" % (len(s.msgs), s.n_user, s.n_assistant))
    if s.children:
        L.append("- children: %d" % len(s.children))
        L += ["  - " + c for c in sorted(s.children)]
    L.append("- archived: %s" % ("true" if s.archived else "false"))
    body = "\n".join("## %d · %s (%s)\n\n%s\n" % (m.seq, m.kind, m.date or UNKNOWN, m.text) for m in s.msgs)
    return clean_whitespace("\n".join(L) + "\n\n" + body)


# --------------------------------------------------------------------------- export

def export(state_path=DEFAULT_STATE, out_dir=DEFAULT_OUT, *, dry_run: bool = False, max_bytes: int = MD_MAX,
           top_n: int = 20, review_dir=MANIFEST_DIR) -> Tuple[Report, dict]:
    out_dir = Path(out_dir)
    state = load_state(state_path)
    copy, sha_expected, n_sess, n_msg = snapshot_copy(state)
    verify_copy(copy, sha_expected)
    report = Report(session_count=n_sess, message_count=n_msg)
    hashes = load_review_hashes(REVIEW_PROJECT, Path(review_dir))
    sessions = read_sessions(copy)
    rows, type_counts = read_messages(copy)
    report.type_counts = type_counts
    for t, n in type_counts.items():
        if t not in EXPORT_TYPES:
            report.msg_skips["type:" + t] += n
    if len(sessions) != n_sess:
        report.warnings.append("session rows read %d != session_count %d" % (len(sessions), n_sess))
    if sum(type_counts.values()) != n_msg:
        report.warnings.append("message rows counted %d != message_count %d" % (sum(type_counts.values()), n_msg))
    by_session: Dict[str, List[dict]] = defaultdict(list)
    for r in rows:
        by_session[_raw(r.get("session_id"))].append(r)
    known_ids = {_raw(s.get("id")) for s in sessions}
    for sid, group in by_session.items():
        if sid not in known_ids:
            report.msg_skips["no_session"] += len(group)
    built: Dict[str, Sess] = {}
    for srow in sessions:
        sid = _raw(srow.get("id"))
        if not sid:
            report.skipped_other.append({"id": "", "reason": "empty_id"})
            continue
        s = build_session(srow, by_session.get(sid, []), report, hashes)
        if s is not None:
            built[sid] = s
    assign_paths(built, known_ids, report)
    for sid, s in built.items():
        text = render(s)
        left = redact.residual_matches(text)
        if left:
            raise ExportError("residual matches in session %s: %s" % (short_id(sid), sorted(left)))
        parts = shard_markdown(text, max_bytes)
        entry = {"bytes": vaultlib.utf8_len(text), "sha256": vaultlib.sha256_text(text), "messages": len(s.msgs),
                 "children": len(s.children), "parts": []}
        if len(parts) > 1:
            stem = s.rel[:-3]
            entry["parts"] = ["%s.part%03d.md" % (stem, i) for i in range(1, len(parts) + 1)]
            entry["parts_json"] = stem + ".parts.json"
            report.sharded += 1
        report.files[s.rel] = entry
        m = report.months.setdefault(s.month, {"sessions": 0, "messages": 0, "bytes": 0, "largest_bytes": 0})
        m["sessions"] += 1
        m["messages"] += len(s.msgs)
        m["bytes"] += entry["bytes"]
        m["largest_bytes"] = max(m["largest_bytes"], entry["bytes"])
        report.exported.append(sid)
        report.msgs_exported += len(s.msgs)
        if not dry_run:
            dst = out_dir / s.rel
            if len(parts) > 1:
                write_shards(dst.with_suffix(""), parts, ".md", max_bytes=max_bytes)
            else:
                _write_if_changed(dst, text)
    return report, build_manifest(report, dry_run, top_n, max_bytes)


def _top(report: Report, n: int) -> List[dict]:
    ranked = sorted(report.per_session.items(), key=lambda kv: (-sum(kv[1].values()), kv[0]))
    return [{"id": short_id(sid), "total": sum(c.values()), "by_category": dict(sorted(c.items()))} for sid, c in ranked[:n]]


def build_manifest(report: Report, dry_run: bool, top_n: int, max_bytes: int) -> dict:
    return {
        "tool": "export_opencode",
        "version": TOOL_VERSION,
        "dry_run": bool(dry_run),
        "max_bytes": max_bytes,
        "session_count": report.session_count,
        "message_count": report.message_count,
        "message_types": dict(sorted(report.type_counts.items())),
        "exported": len(report.exported),
        "skipped": {"sensitive": len(report.skipped_sensitive), "empty": len(report.skipped_empty),
                    "other": len(report.skipped_other)},
        "skipped_total": report.skipped,
        "match_sessions": report.match_sessions,
        "msgs_exported": report.msgs_exported,
        "msgs_skipped": report.msgs_skipped,
        "msg_skips": dict(sorted(report.msg_skips.items())),
        "match_msgs": report.match_msgs,
        "parts_seen": dict(sorted(report.parts_seen.items())),
        "parts_exported": dict(sorted(report.parts_exported.items())),
        "tool_parts_exported": report.parts_exported.get("tool", 0) + report.parts_exported.get("reasoning", 0),
        "children": report.children,
        "orphans": report.orphans,
        "files": dict(sorted(report.files.items())),
        "total_bytes": sum(f["bytes"] for f in report.files.values()),
        "months": dict(sorted(report.months.items())),
        "sharded": report.sharded,
        "redaction_counts": dict(sorted(report.counts.items())),
        "entropy_hits": report.entropy_hits,
        "top_redacted": _top(report, top_n),
        "skipped_sensitive": sorted(report.skipped_sensitive, key=lambda d: d["id"]),
        "skipped_empty": sorted(report.skipped_empty, key=lambda d: d["id"]),
        "skipped_other": report.skipped_other,
        "warnings": report.warnings,
    }


def render_report(manifest: dict) -> str:
    L = ["# T15 dry-run — OpenCode sessions export (counts and shapes only)", ""]
    L.append("- dry_run: %s" % manifest["dry_run"])
    L.append("- session_count: %d · message_count: %d" % (manifest["session_count"], manifest["message_count"]))
    L.append("- message_types: " + (", ".join("%s=%d" % kv for kv in manifest["message_types"].items()) or "(none)"))
    sk = manifest["skipped"]
    L.append("- exported: %d · skipped: %d (sensitive=%d, empty=%d, other=%d) · match_sessions: %s" % (
        manifest["exported"], manifest["skipped_total"], sk["sensitive"], sk["empty"], sk["other"], manifest["match_sessions"]))
    L.append("- msgs_exported: %d · msgs_skipped: %d · match_msgs: %s" % (
        manifest["msgs_exported"], manifest["msgs_skipped"], manifest["match_msgs"]))
    L.append("- msg_skips: " + (", ".join("%s=%d" % kv for kv in manifest["msg_skips"].items()) or "(none)"))
    L.append("- parts_seen: " + (", ".join("%s=%d" % kv for kv in manifest["parts_seen"].items()) or "(none)"))
    L.append("- parts_exported: %s · tool/reasoning parts exported: %d" % (
        ", ".join("%s=%d" % kv for kv in manifest["parts_exported"].items()) or "(none)", manifest["tool_parts_exported"]))
    L.append("- children nested under parent: %d · orphans (parent missing/skipped): %d" % (manifest["children"], manifest["orphans"]))
    L.append("- total_bytes: %s · sharded sessions: %d" % (format(manifest["total_bytes"], ","), manifest["sharded"]))
    if manifest["warnings"]:
        L += ["- warnings:"] + ["  - " + w for w in manifest["warnings"]]
    L += ["", "## Months (month → sessions → messages → bytes → largest file bytes)", ""]
    for month, m in manifest["months"].items():
        L.append("- %s → %d → %d → %s → %s" % (month, m["sessions"], m["messages"], format(m["bytes"], ","), format(m["largest_bytes"], ",")))
    L += ["", "## Redaction counts by category", ""]
    L += ["- %s: %d" % kv for kv in manifest["redaction_counts"].items()] or ["- (none)"]
    L += ["", "## Top redacted sessions (short id → total → by category)", ""]
    L += ["- %s → %d → %s" % (t["id"], t["total"], json.dumps(t["by_category"], ensure_ascii=False))
          for t in manifest["top_redacted"]] or ["- (none)"]
    hits = manifest["entropy_hits"]
    L += ["", "## HIGH_ENTROPY hits: %d (record only, shapes)" % len(hits), ""]
    shapes = Counter((h["length"], h["entropy"], h["charset"], "readable" if h["readable"] else "opaque", h["context_hint"] or "<none>") for h in hits)
    L += ["- len=%d entropy=%.3f charset=%s %s hint=%s ×%d" % (k + (c,)) for k, c in shapes.most_common(25)] or ["- (none)"]
    L += ["", "## Skipped sensitive (ids only): %d" % sk["sensitive"], ""]
    L += ["- `%s` (%d messages)" % (d["id"], d["messages"]) for d in manifest["skipped_sensitive"]] or ["- (none)"]
    L += ["", "## Skipped empty (no text messages, ids only): %d" % sk["empty"], ""]
    L += ["- `%s` (%d rows)" % (d["id"], d["messages"]) for d in manifest["skipped_empty"]] or ["- (none)"]
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------- CLI

def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Export opencode.db snapshot to per-session markdown (text parts only).")
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
        print("[export_opencode] ERROR: %s: %s" % (type(exc).__name__, exc))
        return 1
    _write_if_changed(Path(a.manifest), json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    _write_if_changed(Path(a.report), render_report(manifest))
    print("[export_opencode] %ssession_count=%d message_count=%d exported=%d skipped=%d msgs_exported=%d "
          "msgs_skipped=%d match_sessions=%s match_msgs=%s tool_parts_exported=%d children=%d files=%d sharded=%d "
          "redactions=%d entropy_hits=%d" % (
              "DRY-RUN " if a.dry_run else "", manifest["session_count"], manifest["message_count"], manifest["exported"],
              manifest["skipped_total"], manifest["msgs_exported"], manifest["msgs_skipped"], manifest["match_sessions"],
              manifest["match_msgs"], manifest["tool_parts_exported"], manifest["children"], len(manifest["files"]),
              manifest["sharded"], sum(manifest["redaction_counts"].values()), len(manifest["entropy_hits"])))
    ok = manifest["match_sessions"] and manifest["match_msgs"] and manifest["tool_parts_exported"] == 0
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
