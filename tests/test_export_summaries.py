"""Tests for tools/export_summaries.py on a synthetic conversation_summaries.db (tempfile).

The database uses the exact T0 schema of ``conversation_summaries``; STATE.json is synthetic.
Every secret-looking fixture is assembled at runtime by concatenation; no literal secret,
e-mail or phone number is stored in this file.
"""
import json
import os
import sqlite3
from collections import Counter
import tempfile
import unittest
from pathlib import Path

from tools import export_summaries as es
from tools import vaultlib

SCHEMA = (
    'CREATE TABLE `conversation_summaries` (`conversation_id` text,`title` text NOT NULL DEFAULT "",'
    '`preview` text NOT NULL DEFAULT "",`step_count` integer NOT NULL DEFAULT 0,`last_modified_time` datetime NOT NULL,'
    '`workspace_uris` text NOT NULL,`status` text NOT NULL DEFAULT "",`source` text NOT NULL DEFAULT "",'
    '`project_id` text NOT NULL DEFAULT "",`agent_name` text NOT NULL DEFAULT "",`parent_conversation_id` text NOT NULL DEFAULT "",'
    '`nesting_depth` integer NOT NULL DEFAULT 0,`battle_id` text NOT NULL DEFAULT "",`winning_conversation_id` text NOT NULL DEFAULT "",'
    '`not_fully_idle` numeric NOT NULL DEFAULT false,`killed` numeric NOT NULL DEFAULT false,`last_user_input_time` datetime NOT NULL,'
    '`last_user_input_step_index` integer NOT NULL DEFAULT -1,`app_data_dir` text NOT NULL DEFAULT "",`raw_summary` blob,'
    '`group_id` text NOT NULL DEFAULT "",PRIMARY KEY (`conversation_id`))'
)
COLS = ("conversation_id", "title", "preview", "step_count", "last_modified_time", "workspace_uris", "status",
        "source", "project_id", "agent_name", "parent_conversation_id", "nesting_depth", "battle_id",
        "winning_conversation_id", "not_fully_idle", "killed", "last_user_input_time", "last_user_input_step_index",
        "app_data_dir", "raw_summary", "group_id")


def fake_email():
    return "person.name" + "@" + "example" + ".com"


def fake_egypt_phone():
    return "010" + "12345678"


def open_pem_block():
    body = "QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9w"
    return "-----" + "BEGIN PRIVATE KEY" + "-----\n" + body + "\n" + body + "\n"  # no END -> unresolved


def uuid_like(n):
    return "%08x-0000-4000-8000-%012x" % (n, n)


def row(cid, title="", preview="", steps=1, lmt="2026-11-20 10:00:00.1234567+02:00", ws='["file:///c%3A/Users/USER/proj-x"]',
        agent="", parent="", depth=0, raw=b""):
    return (cid, title, preview, steps, lmt, ws, "CASCADE_RUN_STATUS_IDLE", "", "", agent, parent, depth, "", "",
            0, 0, lmt, -1, "antigravity", raw, "")


class Fixture:
    def __init__(self, rows):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.db = root / "snap" / "conversation_summaries.db"
        self.db.parent.mkdir()
        con = sqlite3.connect(str(self.db))
        con.execute(SCHEMA)
        con.executemany("INSERT INTO conversation_summaries VALUES (%s)" % ",".join("?" * len(COLS)), rows)
        con.commit()
        con.close()
        self.out = root / "out"
        self.state = root / "STATE.json"
        self.write_state(len(rows))

    def write_state(self, count, sha=None):
        state = {"sources": {"conversation_summaries": {
            "copy_path": str(self.db), "sha_copy": sha or vaultlib.sha256_file(self.db),
            "rows_by_table": {"conversation_summaries": count}}}}
        vaultlib.write_text(self.state, json.dumps(state))

    def run(self, **kw):
        return es.export(self.state, self.out, **kw)

    def files(self):
        return sorted(p.name for p in self.out.rglob("*")) if self.out.exists() else []

    def close(self):
        self.tmp.cleanup()


class ExportSummariesTests(unittest.TestCase):
    def setUp(self):
        self.fx = None

    def tearDown(self):
        if self.fx:
            self.fx.close()

    def test_month_grouping_and_unknown_date(self):
        self.fx = Fixture([
            row(uuid_like(1), title="Alpha", lmt="2026-11-20 10:00:00.1234567+02:00"),
            row(uuid_like(2), title="Beta", lmt="2026-10-01T08:00:00Z"),
            row(uuid_like(3), title="Gamma", lmt="2026-11-21 09:00:00+02:00"),
            row(uuid_like(4), title="Delta", lmt="not-a-date"),
            row(uuid_like(5), title="Epoch", lmt="1700000000"),
        ])
        report, manifest = self.fx.run()
        self.assertEqual(sorted(manifest["files"]), ["2023-11.md", "2026-10.md", "2026-11.md", "unknown-date.md"])
        self.assertEqual(manifest["files"]["2026-11.md"]["items"], 2)
        text = vaultlib.read_text(self.fx.out / "2026-11.md")
        self.assertTrue(text.startswith("# Antigravity conversation summaries — 2026-11\n"))
        self.assertIn("- items: 2", text)
        self.assertLess(text.index("## Alpha"), text.index("## Gamma"))  # ascending last_modified_time
        self.assertNotIn("|---", text)  # no markdown tables
        self.assertEqual(sorted(self.fx.files()), ["2023-11.md", "2026-10.md", "2026-11.md", "unknown-date.md"])

    def test_empty_fields_dropped_and_workspace_shortened(self):
        self.fx = Fixture([row(uuid_like(1), title="T", preview="", agent="", parent="", depth=0,
                               ws='["file:///c%3A/Users/USER/.gemini/antigravity/scratch/proj-x"]'),
                           row(uuid_like(2), title="", preview="child preview", agent="planner", parent=uuid_like(1), depth=1)])
        self.fx.run()
        text = vaultlib.read_text(self.fx.out / "2026-11.md")
        block1, block2 = text.split("## ")[1], text.split("## ")[2]
        for absent in ("- agent:", "- parent:", "- depth:", "- preview:", "- summary:"):
            self.assertNotIn(absent, block1)
        self.assertIn("- workspace: proj-x", block1)
        self.assertNotIn("Users/USER", text)
        self.assertNotIn("status", text)
        self.assertNotIn("CASCADE", text)
        self.assertTrue(block2.startswith(uuid_like(2)[:8]))  # empty title -> short id heading
        self.assertIn("- agent: planner", block2)
        self.assertIn("- parent: `%s`" % uuid_like(1), block2)
        self.assertIn("- depth: 1", block2)

    def test_email_and_phone_in_preview_are_redacted(self):
        self.fx = Fixture([row(uuid_like(1), title="Contact", preview="mail %s phone %s" % (fake_email(), fake_egypt_phone()))])
        report, manifest = self.fx.run()
        text = vaultlib.read_text(self.fx.out / "2026-11.md")
        self.assertNotIn(fake_email(), text)
        self.assertNotIn(fake_egypt_phone(), text)
        self.assertIn("[REDACTED:EMAIL]", text)
        self.assertIn("[REDACTED:PHONE]", text)
        self.assertEqual(manifest["redaction_counts"].get("EMAIL"), 1)
        self.assertEqual(manifest["redaction_counts"].get("PHONE"), 1)
        self.assertEqual(manifest["top_redacted"][0]["id"], uuid_like(1)[:8])

    def test_unresolved_private_key_is_skipped_not_exported(self):
        self.fx = Fixture([row(uuid_like(1), title="Clean", preview="fine"),
                           row(uuid_like(2), title="Leak", preview=open_pem_block())])
        report, manifest = self.fx.run()
        self.assertEqual(manifest["skipped"]["sensitive"], 1)
        self.assertEqual(manifest["skipped_sensitive_ids"], [uuid_like(2)])
        self.assertEqual(manifest["exported"], 1)
        text = vaultlib.read_text(self.fx.out / "2026-11.md")
        self.assertNotIn("Leak", text)
        self.assertNotIn("PRIVATE KEY", text)
        self.assertIn("## Clean", text)

    def test_exported_plus_skipped_equals_count(self):
        self.fx = Fixture([row(uuid_like(1), title="A"), row(uuid_like(2), title="B", preview=open_pem_block()),
                           row(uuid_like(3), title="C", lmt="garbage")])
        report, manifest = self.fx.run()
        self.assertEqual(manifest["count_snapshot"], 3)
        self.assertEqual(manifest["exported"] + manifest["skipped_total"], 3)
        self.assertTrue(manifest["match"])
        self.assertTrue(report.match)

    def test_dry_run_writes_nothing(self):
        self.fx = Fixture([row(uuid_like(1), title="A"), row(uuid_like(2), title="B", lmt="2025-01-01 00:00:00+00:00")])
        report, manifest = self.fx.run(dry_run=True)
        self.assertFalse(self.fx.out.exists())
        self.assertTrue(manifest["dry_run"])
        self.assertEqual(manifest["exported"], 2)
        self.assertEqual(sorted(manifest["files"]), ["2025-01.md", "2026-11.md"])

    def test_idempotent_rerun(self):
        self.fx = Fixture([row(uuid_like(1), title="A", preview="p " + fake_email())])
        _, m1 = self.fx.run()
        f = self.fx.out / "2026-11.md"
        mtime = os.stat(f).st_mtime_ns
        _, m2 = self.fx.run()
        self.assertEqual(m1, m2)
        self.assertEqual(os.stat(f).st_mtime_ns, mtime)  # unchanged file is not rewritten
        self.assertEqual(self.fx.files(), ["2026-11.md"])

    def test_sharding_when_over_limit(self):
        rows = [row(uuid_like(i), title="Item %02d" % i, preview="x" * 200, lmt="2026-11-%02d 10:00:00+02:00" % (i + 1))
                for i in range(1, 11)]
        self.fx = Fixture(rows)
        report, manifest = self.fx.run(max_bytes=600)
        entry = manifest["files"]["2026-11.md"]
        self.assertGreater(len(entry["parts"]), 1)
        self.assertEqual(entry["parts_json"], "2026-11.parts.json")
        names = self.fx.files()
        self.assertIn("2026-11.parts.json", names)
        self.assertIn("2026-11.part001.md", names)
        self.assertNotIn("2026-11.md", names)
        from tools.shard import read_shards
        joined = read_shards(self.fx.out / "2026-11.parts.json")
        self.assertEqual(vaultlib.sha256_text(joined), entry["sha256"])
        self.assertEqual(joined.count("\n## "), 10)

    def test_raw_summary_binary_never_leaks_bytes(self):
        blob = b"\x0a\x21\x00\x01\x02\xff\xfe" + "this is a useful summary sentence".encode("utf-8") + b"\x00\x80\x81" \
            + "file:///c%3A/Users/USER/proj".encode("utf-8") + b"\x07short\x00" + fake_email().encode("utf-8") + b"\xc3\x28"
        self.fx = Fixture([row(uuid_like(1), title="Raw", preview="pre", raw=blob),
                           row(uuid_like(2), title="Dup", preview="same text here again", raw=b"\x00same text here again\x00")])
        report, manifest = self.fx.run()
        text = vaultlib.read_text(self.fx.out / "2026-11.md")
        data = text.encode("utf-8")
        for b in (b"\x00", b"\x01", b"\x02", b"\xff", b"\xfe", b"\x07", b"\x80\x81", b"\xc3\x28"):
            self.assertNotIn(b, data)
        self.assertIn("- summary: this is a useful summary sentence", text)
        self.assertNotIn("Users/USER", text)
        self.assertNotIn("file:///", text)
        self.assertNotIn(fake_email(), text)
        self.assertEqual(manifest["raw_summary_useful"], 1)  # the duplicate of preview adds nothing
        self.assertNotIn("- summary:", text.split("## Dup")[1])

    def test_wire_walk_home_path_not_glued_to_length_byte(self):
        # T13-3 Blocker 1: field 1, wire type 2, length 78 (= 'N'). The old regex extraction glued the
        # length byte to the text and produced ``NC:\Users\...`` which the home pattern did not match.
        text = "C:\\Users\\x\\Documents\\notes about the gateway service handoff and the review"
        text = text + "x" * (78 - len(text.encode("utf-8")))
        self.assertEqual(len(text.encode("utf-8")), 78)
        blob = b"\x08\x05" + b"\x0a" + bytes([78]) + text.encode("utf-8") + b"\x15\x01\x02\x03\x04"
        self.assertEqual(es.wire_strings(blob), [text])
        self.fx = Fixture([row(uuid_like(1), title="Wire", preview="pre", raw=blob)])
        report, manifest = self.fx.run()
        out = vaultlib.read_text(self.fx.out / "2026-11.md")
        self.assertIn("- summary: ~\\Documents\\notes about", out)
        self.assertNotIn("NC:", out)
        self.assertNotIn("Users", out)
        self.assertEqual(manifest["raw_summary_decode"], {"wire_ok": 1})

    def test_wire_walk_nested_message_and_fallback_strips_stray_byte(self):
        inner = "nested message string that is long enough".encode("utf-8")
        nested = b"\x12" + bytes([len(inner)]) + inner
        blob = b"\x0a" + bytes([len(nested)]) + nested + b"\x19" + b"\x00" * 8
        self.assertEqual(es.wire_strings(blob), [inner.decode("utf-8")])
        # fallback: field number 0 is malformed -> regex extraction; the run is 'm' (0x6D = 109) + 109 chars
        body = "@[" + "a" * 107
        self.assertEqual(len(body), 0x6D)
        bad = b"\x00" + b"m" + body.encode("utf-8") + b"\x00"
        with self.assertRaises(ValueError):
            es.wire_strings(bad)
        self.assertEqual(es.printable_segments(bad, "", ""), [body])
        self.assertEqual(es._strip_stray_length_byte("KPS D:/proj/x"), "PS D:/proj/x")
        self.assertEqual(es._strip_stray_length_byte("plain words here"), "plain words here")
        stats = Counter()
        es.printable_segments(bad, "", "", stats)
        self.assertEqual(stats, {"fallback": 1})

    def test_sha_mismatch_refuses_to_read(self):
        self.fx = Fixture([row(uuid_like(1), title="A")])
        self.fx.write_state(1, sha="0" * 64)
        with self.assertRaises(es.ExportError):
            self.fx.run()
        self.assertFalse(self.fx.out.exists())

    def test_cli_dry_run_writes_manifest_and_report_only(self):
        self.fx = Fixture([row(uuid_like(1), title="A", preview=fake_email())])
        root = Path(self.fx.tmp.name)
        mf, rp = root / "m" / "summaries.manifest.json", root / "T13.md"
        rc = es.main(["--dry-run", "--state", str(self.fx.state), "--out", str(self.fx.out),
                      "--manifest", str(mf), "--report", str(rp)])
        self.assertEqual(rc, 0)
        self.assertFalse(self.fx.out.exists())
        m = json.loads(vaultlib.read_text(mf))
        self.assertTrue(m["dry_run"] and m["match"])
        report_text = vaultlib.read_text(rp)
        self.assertIn("count_snapshot: 1", report_text)
        self.assertNotIn(fake_email(), report_text)
        self.assertNotIn(fake_email(), vaultlib.read_text(mf))


if __name__ == "__main__":
    unittest.main()
