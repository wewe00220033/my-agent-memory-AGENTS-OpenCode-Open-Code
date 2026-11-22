#!/usr/bin/env python3
"""T0 - Schema discovery (READ-ONLY on sources).

Rules enforced by this script:
  * Sources are never opened directly; SQLite files are byte-copied to a temp dir
    (%LOCALAPPDATA%\\Temp\\opencode\\vault-t0) and only the COPY is opened read-only.
  * SHA-256 of every source file is taken BEFORE and AFTER; mismatch => reported.
  * No row content is ever selected/printed: only table/column names, types,
    counts, lengths, and distributions of short enum-like columns (<= 32 chars).
  * DENY_READ names are never opened.
  * Temp dir is removed at the end.

Outputs (inside the repo, git-ignored):
  _local/T0_SCHEMA_REPORT.md
  _local/T0_hashes.json
"""
from __future__ import annotations

import fnmatch
import hashlib
import json
import os
import shutil
import sqlite3
import sys
import time
from pathlib import Path

HOME = Path.home()
REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "_local"
TEMP_DIR = Path(os.environ.get("LOCALAPPDATA", str(HOME / "AppData" / "Local"))) / "Temp" / "opencode" / "vault-t0"

DB_SUMMARIES = HOME / ".gemini" / "antigravity" / "conversation_summaries.db"
DB_OPENCODE = HOME / ".local" / "share" / "opencode" / "opencode.db"
CONV_DIR = HOME / ".gemini" / "antigravity" / "conversations"

GATEWAY_ROOT = Path(r"D:\SMS\.hRhR_gateway-service\Root")
LEDGER_DIR = GATEWAY_ROOT / "ALL_CONVERSATIONS_LEDGER"
FORENSIC_JSON = GATEWAY_ROOT / "CONVERSATIONS_FORENSIC_DATABASE.json"

INVENTORY = [
    ("~/.gemini/GEMINI.md", HOME / ".gemini" / "GEMINI.md"),
    ("~/.gemini/config/rules", HOME / ".gemini" / "config" / "rules"),
    ("~/.gemini/config/workflows", HOME / ".gemini" / "config" / "workflows"),
    ("~/.gemini/config/skills", HOME / ".gemini" / "config" / "skills"),
    ("~/.config/opencode/commands", HOME / ".config" / "opencode" / "commands"),
    ("~/.gemini/antigravity/brain", HOME / ".gemini" / "antigravity" / "brain"),
    ("~/.gemini/antigravity-ide/brain", HOME / ".gemini" / "antigravity-ide" / "brain"),
    (r"D:\SMS\.hRhR_gateway-service\Root", GATEWAY_ROOT),
    (r"D:\SMS\.hRhR_gateway-service\.agents\memory", Path(r"D:\SMS\.hRhR_gateway-service\.agents\memory")),
    (r"D:\SMS\Bolla-Agentic-OS-EGM-SRE\Root", Path(r"D:\SMS\Bolla-Agentic-OS-EGM-SRE\Root")),
    (r"D:\SMS\.agents\memory", Path(r"D:\SMS\.agents\memory")),
    ("~/.gemini/antigravity/scratch/.agents/memory", HOME / ".gemini" / "antigravity" / "scratch" / ".agents" / "memory"),
]

DENY_READ = [
    "keys*", "*.env", ".env*", "*accounts*", "*.session", "*.har",
    "ACCOUNT_FUNDING_REGISTER.md", "service.json", "unlimited-identity.json",
    "*secret*", "*cred*", "*password*", "token*.json", "*.log",
]

ENUM_COL_NAMES = {"role", "type", "kind", "status", "mode", "source", "provider", "state", "category", "agent", "model"}
TEXTY = ("TEXT", "CHAR", "CLOB", "BLOB", "JSON", "")


def is_denied(name: str) -> bool:
    n = name.lower()
    return any(fnmatch.fnmatch(n, p.lower()) for p in DENY_READ)


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sidecars(db: Path) -> list[Path]:
    return [p for p in (db, Path(str(db) + "-wal"), Path(str(db) + "-shm")) if p.exists()]


def uri(p: Path, immutable: bool) -> str:
    s = str(p.resolve()).replace("\\", "/")
    if not s.startswith("/"):
        s = "/" + s
    return f"file:{s}?mode=ro" + ("&immutable=1" if immutable else "")


def q(ident: str) -> str:
    return '"' + ident.replace('"', '""') + '"'


def md_table(headers: list[str], rows: list[list]) -> str:
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c).replace("|", "\\|").replace("\n", " ") for c in r) + " |")
    return "\n".join(out)


def fmt(n):
    return f"{n:,}" if isinstance(n, int) else (f"{n:,.1f}" if isinstance(n, float) else str(n))


# --------------------------------------------------------------------------- SQLite

def analyze_db(label: str, src: Path, report: list[str], hashes: dict, deep: bool = True) -> None:
    report.append(f"\n## DB: {label}\n")
    report.append(f"- Source: `{src}`")
    files = sidecars(src)
    before = {p.name: {"size": p.stat().st_size, "sha256": sha256_file(p)} for p in files}
    hashes[label] = {"path": str(src), "before": before}
    report.append(md_table(["file", "bytes", "sha256 (before)"], [[n, fmt(v["size"]), v["sha256"]] for n, v in before.items()]))

    tmp_db = TEMP_DIR / src.name
    for p in files:
        shutil.copy2(p, TEMP_DIR / p.name)

    for immutable in (True, False):
        tag = "immutable=1 (WAL ignored)" if immutable else "mode=ro (WAL applied)"
        report.append(f"\n### Opened copy with `{tag}`\n")
        try:
            con = sqlite3.connect(uri(tmp_db, immutable), uri=True)
        except Exception as e:  # noqa: BLE001
            report.append(f"- OPEN FAILED: `{type(e).__name__}: {e}`")
            continue
        try:
            cur = con.cursor()
            try:
                jm = cur.execute("PRAGMA journal_mode").fetchone()[0]
                pc = cur.execute("PRAGMA page_count").fetchone()[0]
                ps = cur.execute("PRAGMA page_size").fetchone()[0]
                report.append(f"- journal_mode={jm}, page_size={ps}, page_count={fmt(pc)}")
            except Exception as e:  # noqa: BLE001
                report.append(f"- pragma error: `{type(e).__name__}: {e}`")

            master = cur.execute("SELECT type, name, tbl_name, sql FROM sqlite_master ORDER BY type, name").fetchall()
            report.append("\n#### sqlite_master\n")
            report.append(md_table(["type", "name", "tbl_name", "sql"], [[t, n, tn, (s or "")] for t, n, tn, s in master]))

            tables = [(n, s or "") for t, n, tn, s in master if t == "table"]
            # FTS detection
            fts = []
            for n, s in tables:
                su = s.upper()
                if "VIRTUAL TABLE" in su and "FTS" in su:
                    kind = "fts5" if "FTS5" in su else ("fts4" if "FTS4" in su else "fts3")
                    contentless = "CONTENT=''" in su.replace(" ", "") or "CONTENT=\"\"" in su.replace(" ", "")
                    external = ("CONTENT=" in su.replace(" ", "")) and not contentless
                    fts.append([n, kind, contentless, external])
            if fts:
                report.append("\n#### FTS virtual tables\n")
                report.append(md_table(["table", "kind", "contentless", "external content="], fts))

            if not deep and not immutable:
                continue
            if not deep:
                # sample conv db: counts + column stats only (small)
                pass

            report.append("\n#### Tables: columns / counts / length stats\n")
            shadow_suffixes = ("_data", "_idx", "_docsize", "_config", "_content", "_segments", "_segdir", "_stat")
            for n, s in tables:
                is_shadow = any(n.endswith(sfx) for sfx in shadow_suffixes) and any(n.startswith(f[0] + "_") for f in fts)
                try:
                    cnt = cur.execute(f"SELECT COUNT(*) FROM {q(n)}").fetchone()[0]
                except Exception as e:  # noqa: BLE001
                    report.append(f"\n**{n}** — COUNT failed: `{type(e).__name__}: {e}`")
                    continue
                report.append(f"\n**{n}** — rows: {fmt(cnt)}" + (" (FTS shadow table)" if is_shadow else ""))
                cols = cur.execute(f"PRAGMA table_info({q(n)})").fetchall()
                rows = []
                for cid, cname, ctype, notnull, dflt, pk in cols:
                    stat = ["", "", "", ""]
                    ctu = (ctype or "").upper()
                    texty = any(t in ctu for t in TEXTY if t) or ctu == ""
                    if cnt and not is_shadow and texty:
                        try:
                            mn, av, mx, nl = cur.execute(
                                f"SELECT MIN(length({q(cname)})), AVG(length({q(cname)})), MAX(length({q(cname)})), SUM({q(cname)} IS NULL) FROM {q(n)}"
                            ).fetchone()
                            stat = [fmt(mn), fmt(av) if av is not None else "", fmt(mx), fmt(nl)]
                        except Exception as e:  # noqa: BLE001
                            stat = [f"err:{type(e).__name__}", "", "", ""]
                    elif cnt and not is_shadow and ("INT" in ctu or "REAL" in ctu or "NUM" in ctu):
                        try:
                            mn, mx, nl = cur.execute(f"SELECT MIN({q(cname)}), MAX({q(cname)}), SUM({q(cname)} IS NULL) FROM {q(n)}").fetchone()
                            stat = [f"min={mn}", "", f"max={mx}", fmt(nl)]
                        except Exception as e:  # noqa: BLE001
                            stat = [f"err:{type(e).__name__}", "", "", ""]
                    rows.append([cid, cname, ctype or "(none)", "Y" if notnull else "", "Y" if pk else "", *stat])
                report.append(md_table(["cid", "column", "type", "notnull", "pk", "min len/val", "avg len", "max len/val", "nulls"], rows))

                if is_shadow or not cnt:
                    continue
                # enum-like distributions (short values only)
                for cid, cname, ctype, *_ in cols:
                    if cname.lower() not in ENUM_COL_NAMES:
                        continue
                    try:
                        mx = cur.execute(f"SELECT MAX(length({q(cname)})) FROM {q(n)}").fetchone()[0]
                        if mx is None or mx > 32:
                            continue
                        dist = cur.execute(
                            f"SELECT {q(cname)}, COUNT(*) FROM {q(n)} GROUP BY 1 ORDER BY 2 DESC LIMIT 40"
                        ).fetchall()
                        report.append(f"\n- distribution of `{n}.{cname}`:")
                        report.append(md_table(["value", "count"], [[v, fmt(c)] for v, c in dist]))
                    except Exception as e:  # noqa: BLE001
                        report.append(f"- distribution of `{n}.{cname}` failed: `{type(e).__name__}`")
                # JSON columns: key names + enum-ish keys (role/type) distribution, never values of free text
                for cid, cname, ctype, *_ in cols:
                    ctu = (ctype or "").upper()
                    if not ("TEXT" in ctu or "JSON" in ctu or ctu == ""):
                        continue
                    try:
                        valid = cur.execute(
                            f"SELECT SUM(json_valid({q(cname)})), COUNT(*) FROM (SELECT {q(cname)} FROM {q(n)} LIMIT 200)"
                        ).fetchone()
                    except Exception:  # noqa: BLE001
                        continue
                    if not valid or not valid[0] or valid[0] < max(1, valid[1] // 2):
                        continue
                    try:
                        keys = cur.execute(
                            f"SELECT j.key, COUNT(*), MIN(length(j.value)), MAX(length(j.value)), MIN(j.type), MAX(j.type) "
                            f"FROM (SELECT {q(cname)} AS v FROM {q(n)} LIMIT 500) s, json_each(s.v) j "
                            f"WHERE json_type(s.v)='object' GROUP BY j.key ORDER BY 2 DESC LIMIT 60"
                        ).fetchall()
                        report.append(f"\n- JSON top-level keys of `{n}.{cname}` (sample 500 rows; key / rows / min len / max len / json types):")
                        report.append(md_table(["key", "rows", "min len", "max len", "type", "type2"], [[k, fmt(c), fmt(a), fmt(b), t1, t2] for k, c, a, b, t1, t2 in keys]))
                        for ek in ("role", "type", "kind", "status", "agent", "mode"):
                            try:
                                mx = cur.execute(
                                    f"SELECT MAX(length(json_extract({q(cname)}, '$.{ek}'))) FROM {q(n)}"
                                ).fetchone()[0]
                                if mx is None or mx > 32:
                                    continue
                                dist = cur.execute(
                                    f"SELECT json_extract({q(cname)}, '$.{ek}'), COUNT(*) FROM {q(n)} GROUP BY 1 ORDER BY 2 DESC LIMIT 40"
                                ).fetchall()
                                report.append(f"\n- distribution of `{n}.{cname}` → `$.{ek}`:")
                                report.append(md_table(["value", "count"], [[v, fmt(c)] for v, c in dist]))
                            except Exception:  # noqa: BLE001
                                pass
                        # nested keys one level under common containers (names only)
                        for ck in ("parts", "content", "state", "metadata", "data"):
                            try:
                                sub = cur.execute(
                                    f"SELECT j.key, COUNT(*) FROM (SELECT json_extract({q(cname)}, '$.{ck}') AS v FROM {q(n)} LIMIT 300) s, json_each(s.v) j "
                                    f"WHERE s.v IS NOT NULL AND json_type(s.v)='object' GROUP BY j.key ORDER BY 2 DESC LIMIT 40"
                                ).fetchall()
                                if sub:
                                    report.append(f"\n- keys under `{n}.{cname}` → `$.{ck}` (object):")
                                    report.append(md_table(["key", "rows"], [[k, fmt(c)] for k, c in sub]))
                                arr = cur.execute(
                                    f"SELECT COUNT(*), MIN(json_array_length(json_extract({q(cname)}, '$.{ck}'))), MAX(json_array_length(json_extract({q(cname)}, '$.{ck}'))) "
                                    f"FROM {q(n)} WHERE json_type(json_extract({q(cname)}, '$.{ck}'))='array'"
                                ).fetchone()
                                if arr and arr[0]:
                                    report.append(f"- `$.{ck}` is an array in {fmt(arr[0])} rows (len min={arr[1]}, max={arr[2]})")
                                    ek = cur.execute(
                                        f"SELECT e.key, COUNT(*) FROM (SELECT json_extract({q(cname)}, '$.{ck}') AS v FROM {q(n)} LIMIT 300) s, "
                                        f"json_each(s.v) a, json_each(a.value) e WHERE json_type(s.v)='array' AND json_type(a.value)='object' GROUP BY e.key ORDER BY 2 DESC LIMIT 40"
                                    ).fetchall()
                                    if ek:
                                        report.append(f"- element keys of `$.{ck}[]`:")
                                        report.append(md_table(["key", "rows"], [[k, fmt(c)] for k, c in ek]))
                                    for tk in ("type", "role"):
                                        td = cur.execute(
                                            f"SELECT json_extract(a.value, '$.{tk}'), COUNT(*) FROM (SELECT json_extract({q(cname)}, '$.{ck}') AS v FROM {q(n)}) s, json_each(s.v) a "
                                            f"WHERE json_type(s.v)='array' AND length(json_extract(a.value, '$.{tk}')) <= 32 GROUP BY 1 ORDER BY 2 DESC LIMIT 40"
                                        ).fetchall()
                                        if td and any(v is not None for v, _ in td):
                                            report.append(f"- distribution of `$.{ck}[].{tk}`:")
                                            report.append(md_table(["value", "count"], [[v, fmt(c)] for v, c in td]))
                            except Exception:  # noqa: BLE001
                                pass
                    except Exception as e:  # noqa: BLE001
                        report.append(f"- JSON key scan of `{n}.{cname}` failed: `{type(e).__name__}`")
        finally:
            con.close()

    after = {p.name: {"size": p.stat().st_size, "sha256": sha256_file(p)} for p in files}
    match = all(before[k]["sha256"] == after.get(k, {}).get("sha256") for k in before) and set(before) == set(after)
    hashes[label]["after"] = after
    hashes[label]["match"] = match
    report.append(f"\n**Source hash match (before == after): `{match}`**")
    if not match:
        report.append("> NOTE: a live application may have written to the source meanwhile (WAL); the COPY analysed above is still a consistent snapshot.")


# --------------------------------------------------------------------------- JSON sources

def canon_hash(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()


def str_len_stats(obj, acc: dict) -> None:
    if isinstance(obj, str):
        acc["n"] += 1
        acc["total"] += len(obj)
        acc["max"] = max(acc["max"], len(obj))
    elif isinstance(obj, dict):
        for v in obj.values():
            str_len_stats(v, acc)
    elif isinstance(obj, list):
        for v in obj:
            str_len_stats(v, acc)


def analyze_ledger(report: list[str]) -> tuple[dict, dict]:
    report.append("\n## LEDGER: ALL_CONVERSATIONS_LEDGER\n")
    ids: dict = {}
    hashes: dict = {}
    if not LEDGER_DIR.exists():
        report.append(f"- MISSING: `{LEDGER_DIR}`")
        return ids, hashes
    files = sorted(p for p in LEDGER_DIR.iterdir() if p.is_file())
    denied = [p.name for p in files if is_denied(p.name)]
    jsons = [p for p in files if p.suffix.lower() == ".json" and not is_denied(p.name)]
    total = sum(p.stat().st_size for p in files)
    report.append(f"- files: {fmt(len(files))} (json: {fmt(len(jsons))}, denied by name: {fmt(len(denied))}), total bytes: {fmt(total)}")
    if denied:
        report.append("- denied names: " + ", ".join(f"`{d}`" for d in denied[:20]))
    sizes = sorted(p.stat().st_size for p in jsons)
    if sizes:
        report.append(f"- json size bytes: min={fmt(sizes[0])}, median={fmt(sizes[len(sizes)//2])}, max={fmt(sizes[-1])}")
    ext = {}
    for p in files:
        ext[p.suffix.lower()] = ext.get(p.suffix.lower(), 0) + 1
    report.append("- extensions: " + ", ".join(f"`{k or '(none)'}`={v}" for k, v in sorted(ext.items())))

    id_keys = ("id", "conversation_id", "conv_id", "uuid", "session_id", "conversationId", "sessionId")
    key_rows = []
    parse_fail = 0
    for i, p in enumerate(jsons):
        try:
            with open(p, "r", encoding="utf-8") as f:
                obj = json.load(f)
        except Exception as e:  # noqa: BLE001
            parse_fail += 1
            if i < 5:
                key_rows.append([p.name, f"PARSE FAIL {type(e).__name__}", "", ""])
            continue
        hashes[p.name] = canon_hash(obj)
        if isinstance(obj, dict):
            for k in id_keys:
                if k in obj and isinstance(obj[k], (str, int)):
                    ids[str(obj[k])] = p.name
                    break
        ids[p.stem] = p.name
        if i < 5:
            acc = {"n": 0, "total": 0, "max": 0}
            str_len_stats(obj, acc)
            top = "dict:" + ",".join(sorted(obj.keys())[:40]) if isinstance(obj, dict) else f"{type(obj).__name__}[{len(obj) if hasattr(obj, '__len__') else ''}]"
            key_rows.append([p.name, top, f"{acc['n']} strings, avg {fmt(acc['total']/acc['n']) if acc['n'] else 0}, max {fmt(acc['max'])}", fmt(p.stat().st_size)])
    report.append(f"- parse failures: {parse_fail}")
    report.append("\nSample (first 5 alphabetically) — top-level keys only:\n")
    report.append(md_table(["file", "top-level", "string value lengths", "bytes"], key_rows))
    return ids, hashes


def analyze_forensic(report: list[str], ledger_ids: dict, ledger_hashes: dict) -> None:
    report.append("\n## FORENSIC: CONVERSATIONS_FORENSIC_DATABASE.json\n")
    if not FORENSIC_JSON.exists():
        report.append(f"- MISSING: `{FORENSIC_JSON}`")
        return
    if is_denied(FORENSIC_JSON.name):
        report.append("- DENIED by name")
        return
    report.append(f"- bytes: {fmt(FORENSIC_JSON.stat().st_size)}")
    try:
        with open(FORENSIC_JSON, "r", encoding="utf-8") as f:
            obj = json.load(f)
    except Exception as e:  # noqa: BLE001
        report.append(f"- PARSE FAIL: `{type(e).__name__}: {e}`")
        return
    report.append(f"- top-level type: `{type(obj).__name__}`")
    items = None
    if isinstance(obj, list):
        items = obj
        report.append(f"- elements: {fmt(len(obj))}")
    elif isinstance(obj, dict):
        report.append("- top-level keys: " + ", ".join(f"`{k}`({type(v).__name__}{'['+str(len(v))+']' if isinstance(v,(list,dict)) else ''})" for k, v in list(obj.items())[:40]))
        # pick the largest list/dict container as the item collection
        best = max(((k, v) for k, v in obj.items() if isinstance(v, (list, dict))), key=lambda kv: len(kv[1]), default=None)
        if best:
            k, v = best
            items = v if isinstance(v, list) else list(v.values())
            report.append(f"- item collection: `{k}` with {fmt(len(items))} items" + (" (dict keyed)" if isinstance(v, dict) else ""))
            if isinstance(v, dict):
                for kk in v.keys():
                    ledger_ids.setdefault("__forensic_keys__", set()).add(str(kk)) if False else None
    if not items:
        return
    keyc: dict = {}
    for it in items:
        if isinstance(it, dict):
            for k in it.keys():
                keyc[k] = keyc.get(k, 0) + 1
    report.append("\nItem top-level keys (name / items having it):\n")
    report.append(md_table(["key", "items"], [[k, fmt(c)] for k, c in sorted(keyc.items(), key=lambda kv: -kv[1])[:60]]))
    acc = {"n": 0, "total": 0, "max": 0}
    str_len_stats(items, acc)
    report.append(f"- string values: {fmt(acc['n'])}, avg len {fmt(acc['total']/acc['n']) if acc['n'] else 0}, max len {fmt(acc['max'])}")

    id_keys = ("id", "conversation_id", "conv_id", "uuid", "session_id", "conversationId", "sessionId", "file", "filename", "source_file", "path")
    by_id = 0
    by_hash = 0
    ledger_hash_set = set(ledger_hashes.values())
    for it in items:
        if not isinstance(it, dict):
            continue
        hit = False
        for k in id_keys:
            v = it.get(k)
            if isinstance(v, (str, int)):
                sv = str(v)
                stem = Path(sv).stem if "/" in sv or "\\" in sv or sv.endswith(".json") else sv
                if sv in ledger_ids or stem in ledger_ids:
                    hit = True
                    break
        if hit:
            by_id += 1
        if canon_hash(it) in ledger_hash_set:
            by_hash += 1
    n = len(items)
    report.append(f"- overlap with LEDGER by identifier/filename: {fmt(by_id)}/{fmt(n)} = {100*by_id/n:.1f}%")
    report.append(f"- overlap with LEDGER by exact canonical SHA-256 of item: {fmt(by_hash)}/{fmt(n)} = {100*by_hash/n:.1f}%")


# --------------------------------------------------------------------------- inventory

def analyze_inventory(report: list[str]) -> None:
    report.append("\n## Inventory (counts + bytes only)\n")
    rows = []
    denied_names: dict = {}
    for label, p in INVENTORY:
        if not p.exists():
            rows.append([label, "MISSING", "", "", "", ""])
            continue
        if p.is_file():
            rows.append([label, "file", 1, fmt(p.stat().st_size), 1 if p.suffix.lower() == ".md" else 0, 1 if is_denied(p.name) else 0])
            continue
        n = md = denied = size = 0
        dl = []
        for root, dirs, files in os.walk(p):
            for fn in files:
                fp = Path(root) / fn
                n += 1
                try:
                    size += fp.stat().st_size
                except OSError:
                    pass
                if fn.lower().endswith(".md"):
                    md += 1
                if is_denied(fn):
                    denied += 1
                    dl.append(fn)
        rows.append([label, "dir", fmt(n), fmt(size), fmt(md), fmt(denied)])
        if dl:
            denied_names[label] = sorted(set(dl))
    report.append(md_table(["source", "kind", "files", "bytes", ".md files", "DENY_READ by name"], rows))
    if denied_names:
        report.append("\nDenied file NAMES per source (names only, never opened):\n")
        for label, names in denied_names.items():
            report.append(f"- `{label}`: " + ", ".join(f"`{x}`" for x in names[:40]) + (f" … (+{len(names)-40})" if len(names) > 40 else ""))


# --------------------------------------------------------------------------- main

def main() -> int:
    t0 = time.time()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    report: list[str] = [
        "# T0 — Schema Discovery Report",
        f"- generated: {time.strftime('%Y-%m-%d %H:%M:%S')}  · python {sys.version.split()[0]} · sqlite {sqlite3.sqlite_version}",
        f"- temp dir (deleted at end): `{TEMP_DIR}`",
        "- policy: sources byte-copied, copies opened read-only; no row content printed; DENY_READ respected.",
    ]
    hashes: dict = {}
    try:
        if DB_SUMMARIES.exists():
            analyze_db("conversation_summaries.db", DB_SUMMARIES, report, hashes)
        else:
            report.append(f"\n## DB: conversation_summaries.db\n- MISSING `{DB_SUMMARIES}`")
        if DB_OPENCODE.exists():
            analyze_db("opencode.db", DB_OPENCODE, report, hashes)
        else:
            report.append(f"\n## DB: opencode.db\n- MISSING `{DB_OPENCODE}`")
        if CONV_DIR.exists():
            sample = sorted(p for p in CONV_DIR.glob("*.db") if p.is_file())
            report.append(f"\n## Per-conversation DBs (Q3 deferred) — `{CONV_DIR}`: {fmt(len(sample))} `.db` files, total {fmt(sum(p.stat().st_size for p in sample))} bytes")
            if sample:
                analyze_db(f"sample conversations/{sample[0].name}", sample[0], report, hashes, deep=True)
        ledger_ids, ledger_hashes = analyze_ledger(report)
        analyze_forensic(report, ledger_ids, ledger_hashes)
        analyze_inventory(report)
    finally:
        shutil.rmtree(TEMP_DIR, ignore_errors=True)
        report.append(f"\n---\n- temp removed: `{not TEMP_DIR.exists()}` · elapsed {time.time()-t0:.1f}s")
        (OUT_DIR / "T0_SCHEMA_REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8", newline="\n")
        (OUT_DIR / "T0_hashes.json").write_text(json.dumps(hashes, indent=2, ensure_ascii=False), encoding="utf-8", newline="\n")
    ok = all(v.get("match") for v in hashes.values())
    print(f"report: {OUT_DIR / 'T0_SCHEMA_REPORT.md'}")
    print(f"hashes: {OUT_DIR / 'T0_hashes.json'}  all_match={ok}  temp_removed={not TEMP_DIR.exists()}")
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
