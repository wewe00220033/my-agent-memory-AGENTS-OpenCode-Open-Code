"""T12 - snapshot_db: synthetic SQLite/JSON sources in a temp dir; never touches real sources or the repo tree."""
import json
import os
import sqlite3
import tempfile
import unittest
from pathlib import Path

from tools import snapshot_db as sd, vaultlib

REPO = vaultlib.repo_root()
_TMP_BASE = Path(os.environ.get("LOCALAPPDATA", tempfile.gettempdir())) / "Temp" / "opencode"

SKELETON = "\n".join([
    "# SNAPSHOT.md — لقطة المصادر / Source snapshot",
    "",
    "> ⚠️ **هيكل فارغ** — يُملأ آلياً في **S3/T12** بواسطة `tools/snapshot_db.py`.",
    "> EN: Empty skeleton, filled by `tools/snapshot_db.py` at the start of S3.",
    "",
    "## 1. بيانات اللقطة / Snapshot metadata",
    "- **تاريخ ووقت اللقطة (UTC):** `-`",
    "- **الطريقة:** `sqlite3.Connection.backup()`",
    "- **الأداة / الإصدار:** `tools/snapshot_db.py` / `-`",
    "- **عدد المصادر:** `-`",
    "",
    "## 2. جدول المصادر / Sources",
    "",
    "| المصدر | النوع | SHA-256 المصدر قبل النسخ | SHA-256 المصدر بعد النسخ | متطابق؟ | SHA-256 النسخة | عدد الجداول | إجمالي الصفوف | الحجم (bytes) |",
    "|---|---|---|---|---|---|---|---|---|",
    "| %s | sqlite | - | - | - | - | - | - | - |" % sd.ROW_SUMMARIES,
    "| %s | sqlite | - | - | - | - | - | - | - |" % sd.ROW_FTS,
    "| %s | sqlite | - | - | - | - | - | - | - |" % sd.ROW_OPENCODE,
    "| %s | json | - | - | - | - | - | - | - |" % sd.ROW_LEDGER,
    "| %s | json | - | - | - | - | - | - | - |" % sd.ROW_FORENSIC,
    "",
    "### 2.1 أعداد الصفوف لكل جدول / Per-table row counts",
    "",
    "| المصدر | الجدول | الصفوف |",
    "|---|---|---|",
    "| - | - | - |",
    "",
    "## 3. أعداد التصدير / Export counts (تُملأ بعد T13–T16)",
    "",
    "| المصدر | count(snapshot) | exported | skipped | exported + skipped == count | مجلد الناتج |",
    "|---|---|---|---|---|---|",
    "| summaries (T13) | - | - | - | - | `conversations/summaries/` |",
    "| opencode (T15) | - | - | - | - | `conversations/opencode/` |",
    "",
    "## 4. ملاحظات / Notes",
    "- تُحذف نسخ الـ temp بعد T21.",
    "",
])


def make_db(path: Path, wal: bool = True):
    """Create a tiny DB with two tables (+ an FTS5 table when available). Returns {table: rows}."""
    con = sqlite3.connect(str(path))
    if wal:
        con.execute("PRAGMA journal_mode=WAL")
    con.execute("CREATE TABLE alpha (id INTEGER PRIMARY KEY, v TEXT)")
    con.execute("CREATE TABLE beta (id INTEGER PRIMARY KEY)")
    con.executemany("INSERT INTO alpha (v) VALUES (?)", [("a",), ("b",), ("c",)])
    con.executemany("INSERT INTO beta DEFAULT VALUES", [()] * 5)
    expected = {"alpha": 3, "beta": 5}
    try:
        con.execute("CREATE VIRTUAL TABLE conversations_fts USING fts5(body)")
        con.executemany("INSERT INTO conversations_fts (body) VALUES (?)", [("x y",), ("z",)])
        expected["conversations_fts"] = 2
    except sqlite3.OperationalError:
        pass
    con.commit()
    con.close()
    return expected


class TestSnapshotDb(unittest.TestCase):
    def setUp(self):
        _TMP_BASE.mkdir(parents=True, exist_ok=True)
        self._td = tempfile.TemporaryDirectory(dir=str(_TMP_BASE), prefix="snap-test-")
        self.tmp = Path(self._td.name)
        self.src_dir = self.tmp / "src"
        self.temp_dir = self.tmp / "vault-snapshot"
        self.src_dir.mkdir()

    def tearDown(self):
        self._td.cleanup()

    def test_backup_includes_wal_rows_written_after_writer_opened(self):
        db = self.src_dir / "live.db"
        make_db(db, wal=True)
        writer = sqlite3.connect(str(db))  # keeps the WAL un-checkpointed
        writer.execute("INSERT INTO alpha (v) VALUES ('late')")
        writer.commit()
        self.assertTrue(Path(str(db) + "-wal").exists(), "fixture must have a live WAL")
        try:
            res = sd.snapshot_sqlite(db, self.temp_dir)
        finally:
            writer.close()
        self.assertEqual(res["rows_by_table"]["alpha"], 4, "row living only in the WAL must be in the copy")
        copy = self.temp_dir / "live.db"
        self.assertTrue(copy.is_file())
        con = sqlite3.connect(str(copy))
        try:
            self.assertEqual(con.execute("SELECT count(*) FROM alpha").fetchone()[0], 4)
        finally:
            con.close()

    def test_source_hash_before_equals_after_for_static_db(self):
        db = self.src_dir / "static.db"
        make_db(db, wal=False)
        res = sd.snapshot_sqlite(db, self.temp_dir)
        self.assertTrue(res["match"])
        self.assertEqual(res["sha_before"], res["sha_after"])
        self.assertEqual(res["attempts"], 1)
        self.assertEqual(res["sha_copy"], vaultlib.sha256_file(self.temp_dir / "static.db"))
        self.assertEqual(res["note"], "")

    def test_rows_by_table_is_dynamic_from_sqlite_master(self):
        db = self.src_dir / "dyn.db"
        expected = make_db(db, wal=False)
        res = sd.snapshot_sqlite(db, self.temp_dir)
        for t, n in expected.items():
            self.assertEqual(res["rows_by_table"].get(t), n, t)
        self.assertGreaterEqual(res["tables"], len(expected))
        self.assertEqual(res["tables"], len(res["rows_by_table"]))
        # a table added later is discovered without any code change
        con = sqlite3.connect(str(db))
        con.execute("CREATE TABLE gamma (x)")
        con.execute("INSERT INTO gamma VALUES (1)")
        con.commit()
        con.close()
        res2 = sd.snapshot_sqlite(db, self.temp_dir)
        self.assertEqual(res2["rows_by_table"]["gamma"], 1)
        self.assertEqual(res2["tables"], res["tables"] + 1)

    def test_live_db_mismatch_is_recorded_not_raised(self):
        db = self.src_dir / "churn.db"
        make_db(db, wal=False)
        real = sd.backup_sqlite

        def churn(src, dst):
            real(src, dst)
            con = sqlite3.connect(str(src))
            con.execute("INSERT INTO beta DEFAULT VALUES")
            con.commit()
            con.close()
        sd.backup_sqlite = churn
        try:
            res = sd.snapshot_sqlite(db, self.temp_dir)
        finally:
            sd.backup_sqlite = real
        self.assertFalse(res["match"])
        self.assertEqual(res["attempts"], 2, "exactly one automatic retry")
        self.assertIn("حيّة", res["note"])
        self.assertNotEqual(res["sha_before"], res["sha_after"])

    def test_state_file_has_required_keys_and_json_sources(self):
        db = self.src_dir / "conversation_summaries.db"
        make_db(db, wal=False)
        ledger = self.src_dir / "LEDGER"
        ledger.mkdir()
        for i in range(3):
            vaultlib.write_text(ledger / ("c%d.json" % i), json.dumps({"id": i, "items": [1, 2]}))
        vaultlib.write_text(ledger / "secret_notes.json", "{}")  # DENY_READ by name -> never opened/copied
        forensic = self.src_dir / "FORENSIC.json"
        vaultlib.write_text(forensic, json.dumps([{"a": 1}, {"b": 2}]))
        sources = [
            {"key": "conversation_summaries", "kind": "sqlite", "path": db, "row": sd.ROW_SUMMARIES},
            {"key": "ledger", "kind": "json_dir", "path": ledger, "row": sd.ROW_LEDGER},
            {"key": "forensic", "kind": "json_file", "path": forensic, "row": sd.ROW_FORENSIC},
            {"key": "missing", "kind": "sqlite", "path": self.src_dir / "nope.db", "row": sd.ROW_OPENCODE},
        ]
        state = sd.build_state(sources, self.temp_dir)
        out = sd.write_state(self.tmp / "SNAPSHOT_STATE.json", state)
        data = json.loads(vaultlib.read_text(out))
        for k in ("taken_at_utc", "tool_version", "temp_dir", "sources"):
            self.assertIn(k, data)
        for key, s in data["sources"].items():
            for k in ("source_path", "copy_path", "sha_before", "sha_after", "match", "sha_copy", "tables", "rows_by_table", "bytes"):
                self.assertIn(k, s, "%s.%s" % (key, k))
        led = data["sources"]["ledger"]
        self.assertEqual(led["rows_by_table"]["files"], 3)
        self.assertEqual(led["rows_by_table"]["denied_by_name"], 1)
        self.assertEqual(led["rows_by_table"]["top_level_items"], 6)
        self.assertTrue(led["match"])
        self.assertFalse((self.temp_dir / "LEDGER" / "secret_notes.json").exists())
        self.assertEqual(data["sources"]["forensic"]["rows_by_table"]["top_level_items"], 2)
        self.assertEqual(data["sources"]["missing"]["note"], "المصدر غير موجود")
        # previous run is overwritten, never appended
        state2 = sd.build_state(sources, self.temp_dir)
        self.assertTrue(state2["previous_run_overwritten"])
        self.assertFalse(state["previous_run_overwritten"])

    def test_fill_snapshot_md_replaces_placeholders_only_and_keeps_section_3(self):
        db = self.src_dir / "conversation_summaries.db"
        expected = make_db(db, wal=False)
        sources = [{"key": "conversation_summaries", "kind": "sqlite", "path": db, "row": sd.ROW_SUMMARIES}]
        state = sd.build_state(sources, self.temp_dir)
        filled = sd.fill_snapshot_md(SKELETON, state, sources)
        self.assertIn("**تاريخ ووقت اللقطة (UTC):** `%s`" % state["taken_at_utc"], filled)
        self.assertIn("/ `%s`" % sd.TOOL_VERSION, filled)
        self.assertIn("**عدد المصادر:** `1`", filled)
        self.assertIn("لقطة مأخوذة آلياً بتاريخ %s" % state["taken_at_utc"], filled)
        self.assertNotIn("هيكل فارغ", filled)
        row = [ln for ln in filled.splitlines() if ln.startswith("| %s |" % sd.ROW_SUMMARIES)][0]
        self.assertNotIn("| - |", row)
        self.assertIn(state["sources"]["conversation_summaries"]["sha_copy"], row)
        self.assertIn("| True |", row)
        for t, n in expected.items():
            self.assertIn("| conversation_summaries | %s | %d |" % (t, n), filled)
        self.assertNotIn("| - | - | - |", filled.splitlines(), "2.1 placeholder row must be gone")
        if "conversations_fts" in expected:
            fts = [ln for ln in filled.splitlines() if ln.startswith("| %s |" % sd.ROW_FTS)][0]
            self.assertIn("داخل conversation_summaries.db", fts)
            self.assertIn("| %d |" % expected["conversations_fts"], fts)
        # untouched: rows of sources not snapshotted, section 3 and 4 verbatim
        self.assertIn("| %s | sqlite | - | - | - | - | - | - | - |" % sd.ROW_OPENCODE, filled)
        sec3 = SKELETON[SKELETON.index("## 3."):]
        self.assertTrue(filled.endswith(sec3))
        # idempotent: filling an already-filled file yields the same text again
        self.assertEqual(sd.fill_snapshot_md(filled, state, sources), filled)

    def test_no_database_artifacts_inside_repo_and_temp_outside_repo(self):
        db = self.src_dir / "x.db"
        make_db(db, wal=True)
        sd.snapshot_sqlite(db, self.temp_dir)
        self.assertFalse(str(sd.TEMP_DIR.resolve()).lower().startswith(str(REPO.resolve()).lower()))
        self.assertTrue(str(sd.TEMP_DIR).lower().endswith(os.path.join("temp", "opencode", "vault-snapshot")))
        self.assertEqual(sd.env_path(sd.TEMP_DIR), "%LOCALAPPDATA%\\Temp\\opencode\\vault-snapshot")
        suffixes = (".db", ".sqlite", ".sqlite3", "-wal", "-shm")
        bad = []
        for dirpath, dirnames, filenames in os.walk(REPO):
            dirnames[:] = [d for d in dirnames if d not in {".git", "_local"}]
            bad += [fn for fn in filenames if fn.lower().endswith(suffixes)]
        self.assertEqual(bad, [])
        self.assertTrue(sd.display_path(Path.home() / "a" / "b.db").startswith("~/"))
        self.assertNotIn(":\\", sd.display_path(sd.DB_SUMMARIES))


if __name__ == "__main__":
    unittest.main()
