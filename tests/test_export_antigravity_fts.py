"""Tests for tools/export_antigravity_fts.py on a synthetic conversation_summaries.db (tempfile).

The database carries the exact T0 ``conversation_summaries`` schema (reused from test_export_summaries) plus an
FTS5 ``conversations_fts`` virtual table with the T0 column list; STATE.json is synthetic. Every secret-looking
fixture is assembled at runtime by concatenation; no literal secret, e-mail or phone number is stored here.
"""
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from tests.test_export_summaries import COLS, SCHEMA, fake_egypt_phone, fake_email, open_pem_block, row, uuid_like
from tools import export_antigravity_fts as ef
from tools import vaultlib
from tools.shard import read_shards

FTS_COLS = ("conversation_id", "chunk_index", "chunk_first_step", "chunk_last_step", "last_modified_time",
            "step_count", "last_step_created_at", "archived", "user_step_byte_offsets", "agent_step_byte_offsets",
            "title", "workspace", "project", "user_body", "agent_body")
FTS_SCHEMA = "CREATE VIRTUAL TABLE conversations_fts USING fts5(%s)" % ", ".join(FTS_COLS)
NS = 1_795_132_800_000_000_000  # 2026-11-20 00:00:00 UTC in integer nanoseconds (the real column shape)


def chunk(cid, idx, user="user text long enough", agent="agent text long enough", first=0, last=1, lmt=0,
          steps=2, archived=0, title="", workspace="", project=""):
    return (cid, idx, first, last, lmt, steps, 0, archived, "[]", "[]", title, workspace, project, user, agent)


class Fixture:
    def __init__(self, chunks, summaries=()):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.db = root / "snap" / "conversation_summaries.db"
        self.db.parent.mkdir()
        con = sqlite3.connect(str(self.db))
        con.execute(SCHEMA)
        con.execute(FTS_SCHEMA)
        con.executemany("INSERT INTO conversation_summaries VALUES (%s)" % ",".join("?" * len(COLS)), list(summaries))
        con.executemany("INSERT INTO conversations_fts VALUES (%s)" % ",".join("?" * len(FTS_COLS)), list(chunks))
        con.commit()
        con.close()
        self.out = root / "out"
        self.review = root / "review"
        self.state = root / "STATE.json"
        state = {"sources": {"conversation_summaries": {
            "copy_path": str(self.db), "sha_copy": vaultlib.sha256_file(self.db),
            "rows_by_table": {"conversation_summaries": len(summaries), "conversations_fts": len(chunks)}}}}
        vaultlib.write_text(self.state, json.dumps(state))

    def run(self, **kw):
        kw.setdefault("review_dir", self.review)
        return ef.export(self.state, self.out, **kw)

    def files(self):
        return sorted(p.relative_to(self.out).as_posix() for p in self.out.rglob("*") if p.is_file()) if self.out.exists() else []

    def read(self, rel):
        return vaultlib.read_text(self.out / rel)

    def close(self):
        self.tmp.cleanup()


class ExportAntigravityFtsTests(unittest.TestCase):
    def setUp(self):
        self.fx = None

    def tearDown(self):
        if self.fx:
            self.fx.close()

    def test_chunks_ordered_numerically_and_empty_marked(self):
        cid = uuid_like(1)
        chunks = [chunk(cid, i, user="user body number %d here" % i, first=i * 2, last=i * 2 + 1) for i in (10, 2, 9, 1)]
        chunks.append(chunk(cid, 11, user="", agent=""))
        self.fx = Fixture(chunks, [row(cid, title="Order")])
        report, manifest = self.fx.run()
        text = self.fx.read(manifest["files"] and sorted(manifest["files"])[0])
        heads = [l for l in text.splitlines() if l.startswith("## chunk ")]
        self.assertEqual(heads, ["## chunk 1 (steps 2–3)", "## chunk 2 (steps 4–5)", "## chunk 9 (steps 18–19)",
                                 "## chunk 10 (steps 20–21)", "## chunk 11 (steps 0–1)"])
        self.assertLess(text.index("## chunk 9 "), text.index("## chunk 10 "))
        self.assertIn("### user\n\n(empty)\n\n### agent\n\n(empty)", text)
        self.assertEqual(text.count("### user"), 5)
        self.assertIn("- chunks: 5", text)
        self.assertNotIn("byte_offsets", text)

    def test_date_title_join_then_fts_fallback_then_unknown(self):
        a, b, c = uuid_like(1), uuid_like(2), uuid_like(3)
        self.fx = Fixture([
            chunk(a, 0, lmt=NS, title="fts title"),              # summaries row wins
            chunk(b, 0, lmt=NS, title="Only in fts"), chunk(b, 1, lmt=0),
            chunk(c, 0, lmt=0),                                   # nothing -> unknown-date
        ], [row(a, title="Summary title", lmt="2026-10-05 09:00:00+02:00")])
        report, manifest = self.fx.run()
        files = sorted(manifest["files"])
        self.assertEqual(files, ["2026-10/2026-10-05_Summary-title_%s.md" % a[:8],
                                 "2026-11/2026-11-20_Only-in-fts_%s.md" % b[:8],
                                 "unknown-date/untitled_%s.md" % c[:8]])
        self.assertIn("# Summary title\n", self.fx.read(files[0]))
        self.assertIn("- date: 2026-11-20 ", self.fx.read(files[1]))
        self.assertIn("- date: unknown-date", self.fx.read(files[2]))
        self.assertEqual(sorted(manifest["months"]), ["2026-10", "2026-11", "unknown-date"])

    def test_summary_header_short_and_not_full_preview(self):
        cid = uuid_like(1)
        preview = "preview sentence " * 30  # ~510 chars, must be shortened
        blob = b"".join(b"\x0a" + bytes([len(s)]) + s for s in (
            b"first extra summary segment text", b"second extra summary segment text",
            b"third extra summary segment text", b"fourth extra summary segment text"))
        self.fx = Fixture([chunk(cid, 0)], [row(cid, title="Hdr", preview=preview, raw=blob)])
        report, manifest = self.fx.run()
        text = self.fx.read(sorted(manifest["files"])[0])
        front = text.split("\n## chunk")[0]
        header = [l for l in front.splitlines() if l.startswith("  - ")]
        self.assertEqual(len(header), ef.HEADER_MAX_LINES)
        self.assertLessEqual(len(header[0]), ef.HEADER_MAX_CHARS + 4)
        self.assertTrue(header[0].endswith("…"))
        self.assertNotIn(preview.strip(), text)
        self.assertIn("first extra summary segment text", front)
        self.assertNotIn("fourth extra", front)
        self.assertEqual(manifest["with_summary_header"], 1)
        self.assertEqual(manifest["raw_summary_decode"], {"wire_ok": 1})

    def test_email_phone_and_crlf_env_line_redacted_in_bodies(self):
        cid = uuid_like(1)
        user = "please mail " + fake_email() + " or call " + fake_egypt_phone() + " today"
        agent = "settings:\r\nSECRET_TOKEN = abcdefghijklmnop\r\nnext line of text\r\n"
        self.fx = Fixture([chunk(cid, 0, user=user, agent=agent)], [row(cid, title="Red")])
        report, manifest = self.fx.run()
        text = self.fx.read(sorted(manifest["files"])[0])
        self.assertNotIn(fake_email(), text)
        self.assertNotIn(fake_egypt_phone(), text)
        self.assertNotIn("abcdefghijklmnop", text)
        self.assertIn("SECRET_TOKEN = [REDACTED:KV_SECRET]", text)
        self.assertNotIn("\r", text)
        for cat in ("EMAIL", "PHONE", "KV_SECRET"):
            self.assertGreaterEqual(manifest["redaction_counts"].get(cat, 0), 1, cat)
        self.assertEqual(manifest["top_redacted"][0]["id"], cid[:8])

    def test_unresolved_private_key_skips_whole_conversation(self):
        a, b = uuid_like(1), uuid_like(2)
        self.fx = Fixture([chunk(a, 0), chunk(a, 1, agent=open_pem_block()), chunk(a, 2), chunk(b, 0)],
                          [row(a, title="Bad"), row(b, title="Good")])
        report, manifest = self.fx.run()
        self.assertEqual(manifest["exported"], 1)
        self.assertEqual(manifest["skipped"], {"sensitive": 1, "empty": 0, "other": 0})
        self.assertEqual(manifest["skipped_sensitive"], [{"id": a, "chunks": 3}])
        self.assertEqual(manifest["chunks_skipped"], 3)
        self.assertEqual(manifest["chunks_exported"], 1)
        self.assertTrue(manifest["match_conv"] and manifest["match_chunks"])
        self.assertEqual(len(self.fx.files()), 1)
        self.assertNotIn("BEGIN", self.fx.read(self.fx.files()[0]))

    def test_counts_match_both_conditions_from_state(self):
        chunks = [chunk(uuid_like(n), i) for n in range(1, 5) for i in range(n)]  # 1+2+3+4 = 10 chunks, 4 convs
        self.fx = Fixture(chunks, [row(uuid_like(n), title="T%d" % n) for n in range(1, 4)])  # conv 4 not in summaries
        report, manifest = self.fx.run(dry_run=True)
        self.assertEqual((manifest["chunk_count"], manifest["conv_count"]), (10, 4))
        self.assertEqual(manifest["exported"] + manifest["skipped_total"], manifest["conv_count"])
        self.assertEqual(manifest["chunks_exported"] + manifest["chunks_skipped"], manifest["chunk_count"])
        self.assertTrue(manifest["match_conv"] and manifest["match_chunks"])
        self.assertEqual(sum(f["chunks"] for f in manifest["files"].values()), 10)

    def test_dry_run_writes_nothing_and_real_run_is_idempotent(self):
        cid = uuid_like(1)
        self.fx = Fixture([chunk(cid, 0), chunk(cid, 1)], [row(cid, title="Idem")])
        _, m_dry = self.fx.run(dry_run=True)
        self.assertEqual(self.fx.files(), [])
        self.assertTrue(m_dry["dry_run"])
        _, m1 = self.fx.run()
        files1 = self.fx.files()
        self.assertEqual(len(files1), 1)
        mtime1 = (self.fx.out / files1[0]).stat().st_mtime_ns
        _, m2 = self.fx.run()
        self.assertEqual(self.fx.files(), files1)
        self.assertEqual((self.fx.out / files1[0]).stat().st_mtime_ns, mtime1)  # not rewritten
        self.assertEqual(json.dumps(m1, sort_keys=True), json.dumps(m2, sort_keys=True))
        self.assertEqual(m_dry["files"], m1["files"])  # dry-run predicts the same bytes/sha

    def test_sharding_at_chunk_boundaries_roundtrip(self):
        cid = uuid_like(1)
        chunks = [chunk(cid, i, user="u" * 150 + " %d" % i, agent="a" * 150 + " %d" % i) for i in range(6)]
        self.fx = Fixture(chunks, [row(cid, title="Big")])
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
            self.assertTrue(self.fx.read(part).startswith("## chunk "), part)
        joined = read_shards(self.fx.out / entry["parts_json"])
        self.assertEqual(vaultlib.sha256_text(joined), entry["sha256"])
        self.assertEqual(joined.count("\n## chunk "), 6)

    def test_filename_sanitized_for_windows_and_slug_capped(self):
        cid = uuid_like(1)
        title = 'a<b>:c|d?e*f"g/h\\i ' + "x" * 60
        self.fx = Fixture([chunk(cid, 0)], [row(cid, title=title)])
        report, manifest = self.fx.run()
        rel = sorted(manifest["files"])[0]
        name = rel.rsplit("/", 1)[1]
        for bad in '<>:|?*"\\':
            self.assertNotIn(bad, name)
        self.assertEqual(rel.count("/"), 1)  # the title's slash did not create a sub-folder
        self.assertTrue(name.startswith("2026-11-20_") and name.endswith("_%s.md" % cid[:8]))
        self.assertLessEqual(len(name), len("2026-11-20_") + ef.SLUG_MAX + 1 + 8 + 3)
        self.assertTrue((self.fx.out / rel).is_file())

    def test_slug_capped_when_title_has_early_dot_and_long_tail(self):
        # T14-2 regression: ``sanitize_filename`` treats the text after the last dot as an extension and
        # keeps it whole while truncating, so ``@.<300 chars>`` produced a 300+ char name (Windows path error).
        cid = uuid_like(1)
        title = "@.hRhR " + "-".join(["Model%d" % i for i in range(60)]) + " Note.Gpt"
        self.fx = Fixture([chunk(cid, 0)], [row(cid, title=title)])
        report, manifest = self.fx.run()
        rel = sorted(manifest["files"])[0]
        name = rel.rsplit("/", 1)[1]
        self.assertLessEqual(len(name), len("2026-11-20_") + ef.SLUG_MAX + 1 + 8 + 3)
        self.assertLessEqual(len(ef.slug_of(title)), ef.SLUG_MAX)
        self.assertEqual(ef.slug_of("..."), "untitled")
        self.assertTrue((self.fx.out / rel).is_file())

    def test_workspace_home_shortened_and_project_kept(self):
        cid = uuid_like(1)
        self.fx = Fixture([chunk(cid, 0, workspace="file:///c%3A/Users/USER/work/proj-y", project="proj-y")],
                          [row(cid, title="Ws")])
        report, manifest = self.fx.run()
        text = self.fx.read(sorted(manifest["files"])[0])
        self.assertIn("- workspace: proj-y\n", text)
        self.assertIn("- project: proj-y\n", text)
        self.assertNotIn("Users", text)
        self.assertNotIn("file:///", text)

    def test_cli_dry_run_exit_zero_and_report_shapes_only(self):
        cid = uuid_like(1)
        self.fx = Fixture([chunk(cid, 0, user="mail " + fake_email())], [row(cid, title="Cli")])
        manifest_p = self.fx.out.parent / "m.json"
        report_p = self.fx.out.parent / "r.md"
        rc = ef.main(["--dry-run", "--state", str(self.fx.state), "--out", str(self.fx.out), "--manifest", str(manifest_p),
                      "--report", str(report_p), "--review-dir", str(self.fx.review)])
        self.assertEqual(rc, 0)
        self.assertEqual(self.fx.files(), [])
        rep = vaultlib.read_text(report_p)
        self.assertNotIn(fake_email(), rep)
        self.assertNotIn(fake_email(), vaultlib.read_text(manifest_p))
        self.assertIn("- exported: 1 ", rep)
        self.assertIn("match_chunks: True", rep)


if __name__ == "__main__":
    unittest.main()
