#!/usr/bin/env python3
"""T12 - One synchronized source snapshot (PLAN section 4, Q16/Q3). stdlib only.

Rules:
  * SQLite sources are opened READ-ONLY (URI ``mode=ro``) and copied with
    ``sqlite3.Connection.backup()`` (WAL included) into
    %LOCALAPPDATA%/Temp/opencode/vault-snapshot/ (outside the repo).
  * SHA-256 of every source file (+ -wal / -shm) BEFORE and AFTER the copy, and of the copy.
    A mismatch never fails the run: it is retried once, then recorded (live database).
  * Only the COPY is opened afterwards (``mode=ro``, no ``immutable=1``) and ``sqlite_master`` is read
    dynamically: no table name and no count is hard-coded (Q3).
  * JSON sources (LEDGER directory, FORENSIC file) are byte-copied; DENY_READ names are never opened.
  * No row content is ever printed or written. The temp dir is NOT deleted here (T13-T16 read it; T21 deletes).

Outputs: _local/SNAPSHOT_STATE.json (git-ignored) and the filled sections 1 / 2 / 2.1 of SNAPSHOT.md.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import sqlite3
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tools import vaultlib  # noqa: E402
from tools.discover_schema import DB_OPENCODE, DB_SUMMARIES, FORENSIC_JSON, GATEWAY_ROOT, LEDGER_DIR, sidecars, uri  # noqa: E402
from tools.redact import is_denied_path  # noqa: E402

TOOL_VERSION = "1.0.0"
HOME = Path.home()
REPO = vaultlib.repo_root()
LOCALAPPDATA = Path(os.environ.get("LOCALAPPDATA", str(HOME / "AppData" / "Local")))
TEMP_DIR = LOCALAPPDATA / "Temp" / "opencode" / "vault-snapshot"
STATE_PATH = REPO / "_local" / "SNAPSHOT_STATE.json"
SNAPSHOT_MD = REPO / "SNAPSHOT.md"

# Row labels exactly as they appear in SNAPSHOT.md section 2 (documentation table).
ROW_SUMMARIES = "antigravity — conversation_summaries"
ROW_FTS = "antigravity — antigravity_fts"
ROW_OPENCODE = "opencode"
ROW_LEDGER = "LEDGER"
ROW_FORENSIC = "FORENSIC (تكرار LEDGER — لا يُصدَّر، Q5)"

DEFAULT_SOURCES = [
    {"key": "conversation_summaries", "kind": "sqlite", "path": DB_SUMMARIES, "row": ROW_SUMMARIES},
    {"key": "opencode", "kind": "sqlite", "path": DB_OPENCODE, "row": ROW_OPENCODE},
    {"key": "ledger", "kind": "json_dir", "path": LEDGER_DIR, "row": ROW_LEDGER},
    {"key": "forensic", "kind": "json_file", "path": FORENSIC_JSON, "row": ROW_FORENSIC},
]
# FTS table living INSIDE conversation_summaries.db (not a separate file): shown as its own row.
FTS_PARENT_KEY, FTS_TABLE = "conversation_summaries", "conversations_fts"


# --------------------------------------------------------------------------- helpers

def display_path(p: Path) -> str:
    """Path for documents: ``~/...`` for home, ``~/gateway-service/...`` for the gateway tree, never a drive letter."""
    p = Path(p)
    for base, label in ((HOME, "~"), (GATEWAY_ROOT.parent, "~/gateway-service")):
        try:
            return label + "/" + p.resolve().relative_to(base.resolve()).as_posix()
        except (ValueError, OSError):
            continue
    return "~/<external>/" + p.name


def env_path(p: Path) -> str:
    """Temp paths for the state file: ``%LOCALAPPDATA%\\...`` (expand with os.path.expandvars)."""
    s = str(p)
    la = str(LOCALAPPDATA)
    return "%LOCALAPPDATA%" + s[len(la):] if s.lower().startswith(la.lower()) else s


def _hashes(files: List[Path]) -> Dict[str, str]:
    return {p.name: vaultlib.sha256_file(p) for p in files if p.exists()}


def _combined(hashes: Dict[str, str]) -> str:
    h = hashlib.sha256()
    for name in sorted(hashes):
        h.update(("%s\t%s\n" % (name, hashes[name])).encode("utf-8"))
    return h.hexdigest()


def _rm(p: Path) -> None:
    for x in (p, Path(str(p) + "-wal"), Path(str(p) + "-shm"), Path(str(p) + "-journal")):
        if x.exists():
            x.unlink()


def _qi(ident: str) -> str:
    return '"' + ident.replace('"', '""') + '"'


# --------------------------------------------------------------------------- sqlite

def backup_sqlite(src: Path, dst: Path) -> None:
    """Read-only open of *src* then ``backup()`` into a fresh *dst* (WAL content included)."""
    _rm(dst)
    con = sqlite3.connect(uri(src, False), uri=True)
    try:
        out = sqlite3.connect(str(dst))
        try:
            con.backup(out)
        finally:
            out.close()
    finally:
        con.close()


def read_tables(copy: Path) -> Dict[str, int]:
    """``{table: row count}`` of the COPY, read dynamically from sqlite_master (mode=ro, no immutable)."""
    con = sqlite3.connect(uri(copy, False), uri=True)
    try:
        names = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
        rows: Dict[str, int] = {}
        for n in names:
            try:
                rows[n] = int(con.execute("SELECT count(*) FROM %s" % _qi(n)).fetchone()[0])
            except sqlite3.DatabaseError:
                rows[n] = -1  # unreadable table (e.g. missing FTS extension) - recorded, never silently dropped
        return rows
    finally:
        con.close()


def snapshot_sqlite(src: Path, temp_dir: Path, retries: int = 1) -> dict:
    temp_dir.mkdir(parents=True, exist_ok=True)
    copy = temp_dir / src.name
    attempts = 0
    while True:
        attempts += 1
        files = sidecars(src)
        before = _hashes(files)
        backup_sqlite(src, copy)
        after = _hashes(sidecars(src))
        match_data = all(before.get(k) == after.get(k) for k in before if not k.endswith("-shm"))
        match_all = before == after
        if match_all or attempts > retries:
            break
    sha_copy = vaultlib.sha256_file(copy)
    rows = read_tables(copy)
    note = ""
    if not match_all:
        note = ("القاعدة حيّة؛ النسخة متسقة داخلياً بفضل backup()" if not match_data
                else "تغيّر -shm فقط (فهرس القراء المؤقت)؛ بيانات .db/-wal متطابقة؛ النسخة متسقة داخلياً بفضل backup()")
    return {
        "kind": "sqlite", "source_path": display_path(src), "copy_path": env_path(copy),
        "sha_before": before, "sha_after": after, "match": match_all, "match_data": match_data,
        "sha_copy": sha_copy, "tables": len(rows), "rows_by_table": rows, "rows_total": sum(v for v in rows.values() if v > 0),
        "bytes": sum(p.stat().st_size for p in sidecars(src)), "copy_bytes": copy.stat().st_size,
        "attempts": attempts, "note": note,
    }


# --------------------------------------------------------------------------- json

def _top_level_items(p: Path) -> Optional[int]:
    try:
        with open(p, "r", encoding="utf-8") as f:
            obj = json.load(f)
    except (OSError, ValueError, UnicodeDecodeError):
        return None
    return len(obj) if isinstance(obj, (list, dict)) else 1


def snapshot_json_dir(src: Path, temp_dir: Path) -> dict:
    dst = temp_dir / src.name
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)
    files = sorted(p for p in src.iterdir() if p.is_file())
    denied = [p.name for p in files if is_denied_path(str(p), "READ")]
    use = [p for p in files if p.name not in denied]
    before = _hashes(use)
    items, failures = 0, 0
    for p in use:
        shutil.copy2(p, dst / p.name)
        n = _top_level_items(dst / p.name)
        if n is None:
            failures += 1
        else:
            items += n
    after = _hashes(use)
    copies = _hashes([dst / p.name for p in use])
    return {
        "kind": "json_dir", "source_path": display_path(src) + "/", "copy_path": env_path(dst) + "\\",
        "sha_before": _combined(before), "sha_after": _combined(after), "match": before == after,
        "sha_copy": _combined(copies), "tables": len(use),
        "rows_by_table": {"files": len(use), "top_level_items": items, "parse_failures": failures, "denied_by_name": len(denied)},
        "rows_total": items, "bytes": sum(p.stat().st_size for p in use), "attempts": 1, "note": "",
    }


def snapshot_json_file(src: Path, temp_dir: Path) -> dict:
    if is_denied_path(str(src), "READ"):
        return {"kind": "json_file", "source_path": display_path(src), "copy_path": "", "sha_before": "", "sha_after": "",
                "match": False, "sha_copy": "", "tables": 0, "rows_by_table": {}, "rows_total": 0, "bytes": 0,
                "attempts": 0, "note": "DENY_READ - لم يُفتح"}
    temp_dir.mkdir(parents=True, exist_ok=True)
    dst = temp_dir / src.name
    before = vaultlib.sha256_file(src)
    shutil.copy2(src, dst)
    after = vaultlib.sha256_file(src)
    items = _top_level_items(dst)
    return {
        "kind": "json_file", "source_path": display_path(src), "copy_path": env_path(dst),
        "sha_before": before, "sha_after": after, "match": before == after, "sha_copy": vaultlib.sha256_file(dst),
        "tables": 1, "rows_by_table": {"files": 1, "top_level_items": items if items is not None else 0,
                                       "parse_failures": 0 if items is not None else 1},
        "rows_total": items or 0, "bytes": src.stat().st_size, "attempts": 1, "note": "",
    }


# --------------------------------------------------------------------------- state

def build_state(sources: List[dict], temp_dir: Path) -> dict:
    previous = temp_dir.exists() and any(temp_dir.iterdir())
    temp_dir.mkdir(parents=True, exist_ok=True)
    state = {
        "taken_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "tool_version": TOOL_VERSION,
        "temp_dir": env_path(temp_dir),
        "previous_run_overwritten": bool(previous),
        "sources": {},
    }
    for s in sources:
        p = Path(s["path"])
        if not p.exists():
            state["sources"][s["key"]] = {"kind": s["kind"], "source_path": display_path(p), "copy_path": "", "sha_before": "",
                                          "sha_after": "", "match": False, "sha_copy": "", "tables": 0, "rows_by_table": {},
                                          "rows_total": 0, "bytes": 0, "attempts": 0, "note": "المصدر غير موجود"}
            continue
        if s["kind"] == "sqlite":
            state["sources"][s["key"]] = snapshot_sqlite(p, temp_dir)
        elif s["kind"] == "json_dir":
            state["sources"][s["key"]] = snapshot_json_dir(p, temp_dir)
        else:
            state["sources"][s["key"]] = snapshot_json_file(p, temp_dir)
    return state


def write_state(path: Path, state: dict) -> Path:
    return vaultlib.write_text(path, json.dumps(state, indent=1, ensure_ascii=False, sort_keys=True) + "\n")


# --------------------------------------------------------------------------- SNAPSHOT.md

def _sha_cell(v) -> str:
    if isinstance(v, dict):
        return "<br>".join("`%s`: `%s`" % (k, v[k]) for k in sorted(v)) or "-"
    return ("`%s`" % v) if v else "-"


def _match_cell(s: dict) -> str:
    if s.get("match"):
        return "True"
    return "False — %s" % s["note"] if s.get("note") else "False"


def _row(label: str, s: dict) -> str:
    kind = "sqlite" if s["kind"] == "sqlite" else "json"
    return "| %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
        label, kind, _sha_cell(s["sha_before"]), _sha_cell(s["sha_after"]), _match_cell(s), _sha_cell(s["sha_copy"]),
        format(s["tables"], ","), format(s["rows_total"], ","), format(s["bytes"], ","))


def _fts_row(state: dict) -> str:
    parent = state["sources"].get(FTS_PARENT_KEY, {})
    n = parent.get("rows_by_table", {}).get(FTS_TABLE)
    note = "(جدول `%s` داخل conversation_summaries.db — نفس اللقطة)" % FTS_TABLE
    if n is None:
        return "| %s | sqlite | %s | ↑ | ↑ | ↑ | 0 | (الجدول غير موجود في اللقطة) | ↑ |" % (ROW_FTS, note)
    return "| %s | sqlite | %s | ↑ | ↑ | ↑ | 1 | %s | ↑ |" % (ROW_FTS, note, format(n, ","))


def fill_snapshot_md(text: str, state: dict, sources: Optional[List[dict]] = None) -> str:
    """Replace ONLY the placeholders of sections 1 / 2 / 2.1 (+ the first warning lines); sections 3 and 4 untouched."""
    sources = sources if sources is not None else DEFAULT_SOURCES
    taken, ver = state["taken_at_utc"], state["tool_version"]
    lines = text.split("\n")
    out: List[str] = []
    in_21 = False
    seen_21_sep = False
    rows_21 = ["| %s | %s | %s |" % (k, t, format(c, ","))
               for k, s in state["sources"].items() for t, c in s["rows_by_table"].items()] or ["| - | - | - |"]
    warn = ("> ⚠️ **لقطة مأخوذة آلياً بتاريخ %s (UTC)** بواسطة `tools/snapshot_db.py` v%s (لقطة واحدة متزامنة قبل أي تصدير — Q16). "
            "**لا تُعدَّل القيم يدوياً.** أي SHA-256 أو عدد هنا هو **المرجع الوحيد** لقبول T13–T16 "
            "(`exported + skipped == count(snapshot)`) ولا تُكتب أعداد كثوابت في الكود (Q3)." % (taken, ver))
    warn_en = "> EN: Snapshot taken automatically at %s UTC by `tools/snapshot_db.py` v%s; never edit the values by hand." % (taken, ver)
    warned = warned_en = False
    for ln in lines:
        if ln.startswith("## "):
            in_21 = False
        if not warned and ln.startswith("> ⚠️"):
            out.append(warn)
            warned = True
            continue
        if not warned_en and re.match(r"^> EN: (Empty skeleton|Snapshot taken)", ln):
            out.append(warn_en)
            warned_en = True
            continue
        if "**تاريخ ووقت اللقطة (UTC):**" in ln:
            out.append(re.sub(r"`[^`]*`\s*$", "`%s`" % taken, ln))
            continue
        if "**الأداة / الإصدار:**" in ln:
            out.append(re.sub(r"/ `[^`]*`\s*$", "/ `%s`" % ver, ln))
            continue
        if "**عدد المصادر:**" in ln:
            out.append(re.sub(r"`[^`]*`\s*$", "`%d`" % len(state["sources"]), ln))
            continue
        if ln.startswith("### 2.1"):
            in_21, seen_21_sep = True, False
            out.append(ln)
            continue
        if in_21:
            if not seen_21_sep:
                out.append(ln)
                if ln.startswith("|---"):
                    seen_21_sep = True
                    out.extend(rows_21)
                continue
            if ln.startswith("|"):
                continue  # old body rows dropped (replaced above)
            out.append(ln)
            continue
        replaced = False
        for s in sources:
            if ln.startswith("| %s |" % s["row"]) and s["key"] in state["sources"]:
                out.append(_row(s["row"], state["sources"][s["key"]]))
                replaced = True
                break
        if replaced:
            continue
        if ln.startswith("| %s |" % ROW_FTS):
            out.append(_fts_row(state))
            continue
        out.append(ln)
    return "\n".join(out)


# --------------------------------------------------------------------------- main

def main(argv=None) -> int:
    t0 = time.time()
    state = build_state(DEFAULT_SOURCES, TEMP_DIR)
    write_state(STATE_PATH, state)
    vaultlib.write_text(SNAPSHOT_MD, fill_snapshot_md(vaultlib.read_text(SNAPSHOT_MD), state))
    print("[snapshot_db] v%s taken_at=%s temp=%s previous_overwritten=%s elapsed=%.1fs" % (
        TOOL_VERSION, state["taken_at_utc"], state["temp_dir"], state["previous_run_overwritten"], time.time() - t0))
    for k, s in state["sources"].items():
        print("  %-22s match=%-5s tables=%-3d rows=%-8d bytes=%-12d attempts=%d %s" % (
            k, s["match"], s["tables"], s["rows_total"], s["bytes"], s["attempts"], s["note"]))
    print("state=%s snapshot_md=%s" % (STATE_PATH.relative_to(REPO).as_posix(), SNAPSHOT_MD.name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
