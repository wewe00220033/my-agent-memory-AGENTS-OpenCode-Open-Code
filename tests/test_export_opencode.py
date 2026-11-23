"""Tests for tools/export_opencode.py on a synthetic opencode.db (tempfile).

The database carries the T0 ``session_v2`` / ``session_message`` column shapes (plus an empty ``session_part``
as in the real snapshot); STATE.json is synthetic. Every secret-looking fixture is assembled at runtime by
concatenation; no literal secret, e-mail or phone number is stored here.
"""
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from tests.test_export_summaries import fake_egypt_phone, fake_email, open_pem_block
from tools import export_opencode as eo
from tools import vaultlib
from tools.shard import read_shards

SESSION_SQL = ("CREATE TABLE `session_v2` (`id` text PRIMARY KEY, `project_id` text NOT NULL, `workspace_id` text, "
               "`parent_id` text, `slug` text NOT NULL, `directory` text NOT NULL, `title` text, `version` text NOT NULL, "
               "`agent` text, `model` text, `time_created` integer NOT NULL, `time_updated` integer NOT NULL, "
               "`time_archived` integer)")
MESSAGE_SQL = ("CREATE TABLE `session_message` (`id` text PRIMARY KEY, `session_id` text NOT NULL, `type` text NOT NULL, "
               "`seq` integer NOT NULL, `time_created` integer NOT NULL, `time_updated` integer NOT NULL, `data` text NOT NULL)")
PART_SQL = ("CREATE TABLE `session_part` (`message_id` text NOT NULL, `session_id` text NOT NULL, `ordinal` integer NOT NULL, "
            "`type` text NOT NULL, `data` text NOT NULL, PRIMARY KEY (`message_id`, `ordinal`))")
MS = 1_795_132_800_000  # 2026-11-20 00:00:00 UTC in epoch milliseconds (the real column shape)
MODEL = json.dumps({"providerID": "upstage-studio", "id": "claude-fable-5-1", "variant": "max"})


def sid(n):
    return "ses_%026x" % n


def mid(n):
    return "msg_%026x" % n


def session(n, title="Session title", parent=None, directory="C:\\Users\\USER\\work\\proj-z", agent="build",
            model=MODEL, created=MS, archived=None):
    return (sid(n), "proj" + "0" * 36, None, parent, "slug-%d" % n, directory, title, "1.0.0", agent, model,
            created, created, archived)


_counter = [0]


def msg(n, mtype, seq, data, created=MS):
    _counter[0] += 1
    return (mid(_counter[0]), sid(n), mtype, seq, created, created, json.dumps(data))


def user(n, seq, text, created=MS):
    return msg(n, "user", seq, {"text": text, "agent": "build", "metadata": {"displayText": text}}, created)


def assistant(n, seq, parts, created=MS):
    content = []
    for kind, text in parts:
        p = {"type": kind, "time": {"start": created}}
        if kind == "text":
            p["text"] = text
        elif kind == "reasoning":
            p["text"] = text
        else:
            p.update({"name": "read", "id": "call_x", "state": {"status": "completed", "output": text}})
        content.append(p)
    return msg(n, "assistant", seq, {"content": content, "agent": "build", "finish": "stop"}, created)


def other(n, mtype, seq, created=MS):
    return msg(n, mtype, seq, {"time": {"created": created}}, created)


class Fixture:
    def __init__(self, sessions, messages):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.db = root / "snap" / "opencode.db"
        self.db.parent.mkdir()
        con = sqlite3.connect(str(self.db))
        con.execute(SESSION_SQL)
        con.execute(MESSAGE_SQL)
        con.execute(PART_SQL)
        con.executemany("INSERT INTO session_v2 VALUES (%s)" % ",".join("?" * 13), list(sessions))
        con.executemany("INSERT INTO session_message VALUES (%s)" % ",".join("?" * 7), list(messages))
        con.commit()
        con.close()
        self.out = root / "out"
        self.review = root / "review"
        self.state = root / "STATE.json"
        state = {"sources": {"opencode": {
            "copy_path": str(self.db), "sha_copy": vaultlib.sha256_file(self.db),
            "rows_by_table": {"session_v2": len(sessions), "session_message": len(messages), "session_part": 0}}}}
        vaultlib.write_text(self.state, json.dumps(state))

    def run(self, **kw):
        kw.setdefault("review_dir", self.review)
        return eo.export(self.state, self.out, **kw)

    def files(self):
        return sorted(p.relative_to(self.out).as_posix() for p in self.out.rglob("*") if p.is_file()) if self.out.exists() else []

    def read(self, rel):
        return vaultlib.read_text(self.out / rel)

    def close(self):
        self.tmp.cleanup()


class ExportOpencodeTests(unittest.TestCase):
    def setUp(self):
        self.fx = None

    def tearDown(self):
        if self.fx:
            self.fx.close()

    def test_only_text_parts_exported_tool_and_reasoning_dropped_and_counted(self):
        tool_out = "TOOL OUTPUT MARKER should never appear"
        reasoning = "REASONING MARKER should never appear"
        self.fx = Fixture([session(1, title="Parts")], [
            user(1, 2, "hello there from the user"),
            assistant(1, 3, [("reasoning", reasoning), ("tool", tool_out), ("text", "first visible answer"),
                             ("tool", tool_out), ("text", "second visible answer")]),
            assistant(1, 4, [("tool", tool_out), ("reasoning", reasoning)]),  # no text -> empty
        ])
        report, manifest = self.fx.run()
        text = self.fx.read(sorted(manifest["files"])[0])
        self.assertIn("hello there from the user", text)
        self.assertIn("first visible answer\n\nsecond visible answer", text)
        self.assertNotIn("TOOL OUTPUT MARKER", text)
        self.assertNotIn("REASONING MARKER", text)
        self.assertEqual(manifest["parts_seen"], {"reasoning": 2, "text": 3, "tool": 3})
        self.assertEqual(manifest["parts_exported"], {"text": 2})
        self.assertEqual(manifest["tool_parts_exported"], 0)
        self.assertEqual(manifest["msgs_exported"], 2)
        self.assertEqual(manifest["msg_skips"], {"empty": 1})
        self.assertTrue(manifest["match_msgs"] and manifest["match_sessions"])
        self.assertIn("- messages: 2 (user 1, assistant 1)", text)

    def test_non_user_assistant_rows_counted_not_exported_and_seq_order(self):
        self.fx = Fixture([session(1, title="Order")], [
            other(1, "idle", 5), other(1, "system", 1), other(1, "compaction", 6), other(1, "agent-switched", 7),
            assistant(1, 10, [("text", "answer ten")]), user(1, 2, "question two"), user(1, 9, "question nine"),
        ])
        report, manifest = self.fx.run()
        text = self.fx.read(sorted(manifest["files"])[0])
        heads = [l for l in text.splitlines() if l.startswith("## ")]
        self.assertEqual(heads, ["## 2 · user (2026-11-20 00:00:00)", "## 9 · user (2026-11-20 00:00:00)",
                                 "## 10 · assistant (2026-11-20 00:00:00)"])
        self.assertEqual(manifest["message_types"], {"agent-switched": 1, "assistant": 1, "compaction": 1, "idle": 1,
                                                     "system": 1, "user": 2})
        self.assertEqual(manifest["msg_skips"], {"type:agent-switched": 1, "type:compaction": 1, "type:idle": 1, "type:system": 1})
        self.assertEqual(manifest["msgs_exported"] + manifest["msgs_skipped"], 7)
        self.assertTrue(manifest["match_msgs"])

    def test_child_session_nested_under_parent_and_orphan_flagged(self):
        self.fx = Fixture([session(1, title="Parent"), session(2, title="Child", parent=sid(1)),
                           session(3, title="Orphan", parent=sid(99))], [
            user(1, 2, "parent question"), user(2, 2, "child question"), user(3, 2, "orphan question")])
        report, manifest = self.fx.run()
        files = sorted(manifest["files"])
        p = "2026-11/2026-11-20_Parent_%s" % eo.short_id(sid(1))
        parent, child = p + ".md", "%s/2026-11-20_Child_%s.md" % (p, eo.short_id(sid(2)))
        orphan = "2026-11/2026-11-20_Orphan_%s.md" % eo.short_id(sid(3))
        self.assertEqual(files, sorted([parent, child, orphan]))
        self.assertEqual(self.fx.files(), files)
        self.assertNotEqual(eo.short_id(sid(1)), eo.short_id(sid(2)))  # tail, not the shared time-ordered prefix
        self.assertIn("- children: 1\n  - 2026-11-20_Child_%s.md" % eo.short_id(sid(2)), self.fx.read(parent))
        self.assertIn("- parent: `%s`\n" % sid(1), self.fx.read(child))
        self.assertIn("- parent: `%s` (not in snapshot)" % sid(99), self.fx.read(orphan))
        self.assertEqual((manifest["children"], manifest["orphans"]), (1, 1))
        self.assertEqual(manifest["files"][parent]["children"], 1)

    def test_email_phone_home_path_and_crlf_env_line_redacted(self):
        body = "mail " + fake_email() + " call " + fake_egypt_phone() + " file C:\\Users\\USER\\secret\\a.txt"
        agent = "cfg:\r\nSECRET_TOKEN = abcdefghijklmnop\r\nnext line\r\n"
        self.fx = Fixture([session(1, title="Red " + fake_email())], [user(1, 2, body), assistant(1, 3, [("text", agent)])])
        report, manifest = self.fx.run()
        rel = sorted(manifest["files"])[0]
        text = self.fx.read(rel)
        self.assertNotIn(fake_email(), text)
        self.assertNotIn(fake_email(), rel)
        self.assertNotIn(fake_egypt_phone(), text)
        self.assertNotIn("abcdefghijklmnop", text)
        self.assertIn("SECRET_TOKEN = [REDACTED:KV_SECRET]", text)
        self.assertNotIn("Users\\USER", text)
        self.assertNotIn("\r", text)
        self.assertIn("- directory: proj-z\n", text)
        self.assertIn("- model: upstage-studio/claude-fable-5-1#max\n", text)
        for cat in ("EMAIL", "PHONE", "KV_SECRET"):
            self.assertGreaterEqual(manifest["redaction_counts"].get(cat, 0), 1, cat)
        self.assertEqual(manifest["top_redacted"][0]["id"], eo.short_id(sid(1)))

    def test_unresolved_private_key_skips_whole_session(self):
        self.fx = Fixture([session(1, title="Bad"), session(2, title="Good")], [
            user(1, 2, "fine"), assistant(1, 3, [("text", open_pem_block())]), user(1, 4, "also fine"),
            other(1, "idle", 5), user(2, 2, "good question")])
        report, manifest = self.fx.run()
        self.assertEqual(manifest["exported"], 1)
        self.assertEqual(manifest["skipped"], {"sensitive": 1, "empty": 0, "other": 0})
        self.assertEqual(manifest["skipped_sensitive"], [{"id": sid(1), "messages": 3}])
        self.assertEqual(manifest["msg_skips"], {"sensitive": 3, "type:idle": 1})
        self.assertEqual(manifest["msgs_exported"], 1)
        self.assertTrue(manifest["match_sessions"] and manifest["match_msgs"])
        self.assertEqual(len(self.fx.files()), 1)
        self.assertNotIn("BEGIN", self.fx.read(self.fx.files()[0]))

    def test_empty_session_and_parse_error_counted(self):
        bad = (mid(900), sid(2), "assistant", 3, MS, MS, "{not json")
        self.fx = Fixture([session(1, title="NoText"), session(2, title="Bad")],
                          [other(1, "idle", 2), user(2, 2, "ok"), bad])
        report, manifest = self.fx.run()
        self.assertEqual(manifest["skipped"], {"sensitive": 0, "empty": 1, "other": 0})
        self.assertEqual(manifest["skipped_empty"], [{"id": sid(1), "messages": 0}])
        self.assertEqual(manifest["msg_skips"], {"parse_error": 1, "type:idle": 1})
        self.assertTrue(manifest["match_sessions"] and manifest["match_msgs"])
        self.assertEqual(len(self.fx.files()), 1)

    def test_date_from_time_created_ms_and_unknown(self):
        self.fx = Fixture([session(1, title="Dated", created=1_793_000_000_000), session(2, title="NoDate", created=0)],
                          [user(1, 2, "a"), user(2, 2, "b")])
        report, manifest = self.fx.run()
        files = sorted(manifest["files"])
        self.assertTrue(files[0].startswith("2026-10/2026-10-"), files)
        self.assertEqual(files[1], "unknown-date/NoDate_%s.md" % eo.short_id(sid(2)))
        self.assertIn("- date: unknown-date", self.fx.read(files[1]))
        self.assertEqual(sorted(manifest["months"]), ["2026-10", "unknown-date"])

    def test_dry_run_writes_nothing_and_real_run_is_idempotent(self):
        self.fx = Fixture([session(1, title="Idem")], [user(1, 2, "q"), assistant(1, 3, [("text", "a")])])
        _, m_dry = self.fx.run(dry_run=True)
        self.assertEqual(self.fx.files(), [])
        self.assertTrue(m_dry["dry_run"])
        _, m1 = self.fx.run()
        files1 = self.fx.files()
        self.assertEqual(len(files1), 1)
        mtime1 = (self.fx.out / files1[0]).stat().st_mtime_ns
        _, m2 = self.fx.run()
        self.assertEqual(self.fx.files(), files1)
        self.assertEqual((self.fx.out / files1[0]).stat().st_mtime_ns, mtime1)
        self.assertEqual(json.dumps(m1, sort_keys=True), json.dumps(m2, sort_keys=True))
        self.assertEqual(m_dry["files"], m1["files"])

    def test_sharding_at_message_boundaries_roundtrip(self):
        msgs = [assistant(1, i + 2, [("text", "a" * 300 + " %d" % i)]) for i in range(6)]
        self.fx = Fixture([session(1, title="Big")], msgs)
        report, manifest = self.fx.run(max_bytes=800)
        rel = sorted(manifest["files"])[0]
        entry = manifest["files"][rel]
        self.assertEqual(manifest["sharded"], 1)
        self.assertGreater(len(entry["parts"]), 1)
        self.assertNotIn(rel, self.fx.files())
        for part in entry["parts"]:
            self.assertIn(part, self.fx.files())
            self.assertLessEqual(vaultlib.utf8_len(self.fx.read(part)), 800)
        for part in entry["parts"][1:]:
            self.assertTrue(self.fx.read(part).startswith("## "), part)
        joined = read_shards(self.fx.out / entry["parts_json"])
        self.assertEqual(vaultlib.sha256_text(joined), entry["sha256"])
        self.assertEqual(joined.count("\n## "), 6)

    def test_filename_sanitized_and_slug_capped(self):
        title = 'a<b>:c|d?e*f"g/h\\i ' + "x" * 60
        self.fx = Fixture([session(1, title=title)], [user(1, 2, "q")])
        report, manifest = self.fx.run()
        rel = sorted(manifest["files"])[0]
        name = rel.rsplit("/", 1)[1]
        for bad in '<>:|?*"\\':
            self.assertNotIn(bad, name)
        self.assertEqual(rel.count("/"), 1)
        self.assertTrue(name.startswith("2026-11-20_") and name.endswith("_%s.md" % eo.short_id(sid(1))))
        self.assertTrue((self.fx.out / rel).is_file())

    def test_cli_dry_run_exit_zero_and_report_shapes_only(self):
        self.fx = Fixture([session(1, title="Cli")], [user(1, 2, "mail " + fake_email()),
                                                       assistant(1, 3, [("tool", "TOOL MARKER"), ("text", "ok")])])
        manifest_p = self.fx.out.parent / "m.json"
        report_p = self.fx.out.parent / "r.md"
        rc = eo.main(["--dry-run", "--state", str(self.fx.state), "--out", str(self.fx.out), "--manifest", str(manifest_p),
                      "--report", str(report_p), "--review-dir", str(self.fx.review)])
        self.assertEqual(rc, 0)
        self.assertEqual(self.fx.files(), [])
        rep = vaultlib.read_text(report_p)
        self.assertNotIn(fake_email(), rep)
        self.assertNotIn("TOOL MARKER", rep)
        self.assertNotIn(fake_email(), vaultlib.read_text(manifest_p))
        self.assertIn("- exported: 1 ", rep)
        self.assertIn("match_msgs: True", rep)
        self.assertIn("tool/reasoning parts exported: 0", rep)


if __name__ == "__main__":
    unittest.main()
