"""Tests for tools/export_ledger.py on a synthetic ALL_CONVERSATIONS_LEDGER directory (tempfile).

Files carry the T0 LEDGER top-level keys; STATE.json is synthetic and its ``sha_copy`` uses the exact
``snapshot_db`` combined-hash recipe. A fake FORENSIC file is registered in the state and must never be opened.
Every secret-looking fixture is assembled at runtime by concatenation; no literal secret is stored here.
"""
import hashlib
import json
import tempfile
import unittest
import unittest.mock
from pathlib import Path

from tests.test_export_summaries import fake_egypt_phone, fake_email, open_pem_block
from tools import export_ledger as el
from tools import vaultlib
from tools.shard import read_shards

KEYS = ("index", "cid", "date", "log_type", "projects", "total_user_prompts", "first_prompt", "user_prompts",
        "corrections_count", "corrections", "tools_used", "sample_agent_responses")


def item(n, prompts=("a plain user prompt",), responses=("a plain agent response",), extra=None):
    d = {"index": n, "cid": "%08x-0000-4000-8000-%012x" % (n, n), "date": "2026-04-%02d" % (n % 28 + 1),
         "log_type": "conversation", "projects": ["proj-x"], "total_user_prompts": len(prompts),
         "first_prompt": prompts[0], "user_prompts": list(prompts), "corrections_count": 0, "corrections": [],
         "tools_used": ["read", "edit"], "sample_agent_responses": list(responses)}
    if extra:
        d.update(extra)
    return d


def combined(files):
    h = hashlib.sha256()
    for p in sorted(files, key=lambda p: p.name):
        h.update(("%s\t%s\n" % (p.name, vaultlib.sha256_file(p))).encode("utf-8"))
    return h.hexdigest()


class Fixture:
    def __init__(self, items, raw_files=None, sha_override=None):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.src = root / "snap" / "ALL_CONVERSATIONS_LEDGER"
        self.src.mkdir(parents=True)
        files = []
        total_items = 0
        for i, it in enumerate(items, 1):
            p = self.src / ("%03d_20260422_%08x.json" % (i, i))
            vaultlib.write_text(p, json.dumps(it, ensure_ascii=False, indent=1))
            files.append(p)
            total_items += len(it)
        for name, text in (raw_files or {}).items():
            p = self.src / name
            vaultlib.write_text(p, text)
            files.append(p)
            try:
                obj = json.loads(text)
                total_items += len(obj) if isinstance(obj, (list, dict)) else 1
            except ValueError:
                pass
        self.forensic = root / "snap" / "CONVERSATIONS_FORENSIC_DATABASE.json"
        vaultlib.write_text(self.forensic, json.dumps([item(1)]))
        self.out = root / "out"
        self.review = root / "review"
        self.state = root / "STATE.json"
        state = {"sources": {
            "ledger": {"kind": "json_dir", "copy_path": str(self.src) + "\\", "sha_copy": sha_override or combined(files),
                       "rows_by_table": {"files": len(files), "top_level_items": total_items, "parse_failures": 0, "denied_by_name": 0}},
            "forensic": {"kind": "json_file", "copy_path": str(self.forensic), "sha_copy": vaultlib.sha256_file(self.forensic),
                         "rows_by_table": {"files": 1, "top_level_items": 1}}}}
        vaultlib.write_text(self.state, json.dumps(state))
        self.forensic_atime = self.forensic.stat().st_atime_ns

    def run(self, **kw):
        kw.setdefault("review_dir", self.review)
        return el.export(self.state, self.out, **kw)

    def files(self):
        return sorted(p.relative_to(self.out).as_posix() for p in self.out.rglob("*") if p.is_file()) if self.out.exists() else []

    def close(self):
        self.tmp.cleanup()


class ExportLedgerTests(unittest.TestCase):
    def setUp(self):
        self.fx = None

    def tearDown(self):
        if self.fx:
            self.fx.close()

    def test_dry_run_writes_nothing_counts_match_and_forensic_not_opened(self):
        self.fx = Fixture([item(1), item(2), item(3)])
        with unittest.mock.patch("builtins.open", wraps=open) as mo:
            report, manifest = self.fx.run(dry_run=True)
            opened = [str(c.args[0]) for c in mo.call_args_list if c.args]
        self.assertFalse(any("FORENSIC" in p for p in opened), opened)
        self.assertEqual(self.fx.files(), [])
        self.assertTrue(manifest["dry_run"])
        self.assertTrue(manifest["forensic_skipped_as_duplicate"])
        self.assertEqual((manifest["files_total"], manifest["items_total"]), (3, 36))
        self.assertEqual(manifest["exported"] + manifest["skipped_total"], 3)
        self.assertEqual(manifest["items_exported"] + manifest["items_skipped"], 36)
        self.assertTrue(manifest["match_files"] and manifest["match_items"])
        self.assertTrue(manifest["roundtrip_ok"])
        self.assertEqual(manifest["residual"], 0)
        self.assertEqual(manifest["parts_planned"], 1)

    def test_sha_mismatch_stops_before_reading(self):
        self.fx = Fixture([item(1)], sha_override="0" * 64)
        with self.assertRaises(el.ExportError):
            self.fx.run(dry_run=True)
        self.assertEqual(self.fx.files(), [])

    def test_email_phone_home_path_redacted_recursively_and_keys_kept(self):
        body = "mail " + fake_email() + " call " + fake_egypt_phone() + " at C:\\Users\\USER\\proj\\a.txt"
        self.fx = Fixture([item(1, prompts=(body, "second " + fake_email()), responses=("ok",),
                                extra={"nested": {"deep": [body]}})])
        report, manifest = self.fx.run(dry_run=True)
        text = json.dumps(manifest, ensure_ascii=False)
        self.assertNotIn(fake_email(), text)
        self.assertNotIn(fake_egypt_phone(), text)
        self.assertGreaterEqual(manifest["redactions_by_kind"].get("EMAIL", 0), 3)
        self.assertGreaterEqual(manifest["redactions_by_kind"].get("PHONE", 0), 2)
        self.assertGreaterEqual(manifest["redactions_by_kind"].get("PATH", 0), 1)
        # real write to inspect the element: keys preserved, strings redacted, home path shortened
        _, m = self.fx.run()
        back = read_shards(self.fx.out / "ledger.parts.json")
        self.assertEqual(len(back), 1)
        for k in KEYS:
            self.assertIn(k, back[0])
        self.assertEqual(back[0][el.SOURCE_FIELD], "001_20260422_00000001.json")
        flat = json.dumps(back, ensure_ascii=False)
        self.assertNotIn(fake_email(), flat)
        self.assertNotIn(fake_egypt_phone(), flat)
        self.assertNotIn("Users", flat)
        self.assertIn("[REDACTED:EMAIL]", back[0]["nested"]["deep"][0])
        self.assertEqual(back[0]["index"], 1)

    def test_percent_encoded_drive_file_uri_home_becomes_tilde(self):
        # T16-2 finding: ``file:///c%3A/Users/<name>/...`` escaped every home pattern (70 real hits).
        uri = "file:///c%3A/Users/zz/.gemini/antigravity/x.md"
        self.fx = Fixture([item(1, prompts=("open " + uri + " now",), responses=(uri,))])
        _, m = self.fx.run()
        back = read_shards(self.fx.out / "ledger.parts.json")
        flat = json.dumps(back, ensure_ascii=False)
        self.assertNotIn("Users", flat)
        self.assertNotIn("%3A", flat)
        self.assertIn("~", flat)
        self.assertGreaterEqual(m["redactions_by_kind"].get("PATH", 0), 2)

    def test_unresolved_private_key_skips_file_and_counts_items(self):
        self.fx = Fixture([item(1, responses=(open_pem_block(),)), item(2)])
        report, manifest = self.fx.run(dry_run=True)
        self.assertEqual(manifest["exported"], 1)
        self.assertEqual(manifest["skipped"], {"sensitive": 1, "duplicate": 0, "denied": 0, "parse_error": 0})
        self.assertEqual(manifest["skipped_sensitive"], ["001_20260422_00000001.json"])
        self.assertEqual(manifest["items_skipped"], 12)
        self.assertTrue(manifest["match_files"] and manifest["match_items"])
        self.assertNotIn("BEGIN", json.dumps(manifest))

    def test_duplicate_and_parse_error_counted(self):
        self.fx = Fixture([item(1), item(1)], raw_files={"zzz_bad.json": "{not json"})
        report, manifest = self.fx.run(dry_run=True)
        self.assertEqual(manifest["exported"], 1)
        self.assertEqual(manifest["skipped"], {"sensitive": 0, "duplicate": 1, "denied": 0, "parse_error": 1})
        self.assertEqual(manifest["skipped_duplicate"], ["002_20260422_00000002.json"])
        self.assertTrue(manifest["match_files"] and manifest["match_items"])

    def test_sharding_parts_within_limit_valid_json_and_roundtrip(self):
        items = [item(i, prompts=tuple("p%d-" % i + "x" * 200 for _ in range(4))) for i in range(1, 13)]
        self.fx = Fixture(items)
        _, m_dry = self.fx.run(dry_run=True, max_bytes=3000)
        self.assertTrue(m_dry["sharded"])
        self.assertGreater(m_dry["parts_planned"], 1)
        self.assertLessEqual(m_dry["largest_part_bytes"], 3000)
        self.assertTrue(m_dry["roundtrip_ok"])
        self.assertEqual(self.fx.files(), [])
        _, m = self.fx.run(max_bytes=3000)
        files = self.fx.files()
        parts = [f for f in files if f.startswith("ledger.part") and f != "ledger.parts.json"]
        self.assertEqual(len(parts), m["parts_planned"])
        self.assertIn("ledger.parts.json", files)
        self.assertIn("AUDIT.md", files)
        self.assertIn("SUMMARY.md", files)
        for p in parts:
            text = vaultlib.read_text(self.fx.out / p)
            self.assertLessEqual(vaultlib.utf8_len(text), 3000)
            self.assertIsInstance(json.loads(text), list)
        back = read_shards(self.fx.out / "ledger.parts.json")
        self.assertEqual(len(back), 12)
        self.assertEqual(el.canonical_sha(back), m["merged_sha256"])
        self.assertEqual(m_dry["merged_sha256"], m["merged_sha256"])
        self.assertEqual(m_dry["parts"], m["parts"])

    def test_real_run_is_idempotent(self):
        self.fx = Fixture([item(1), item(2)])
        _, m1 = self.fx.run()
        files1 = self.fx.files()
        self.assertEqual(sorted(files1), ["AUDIT.md", "SUMMARY.md", "ledger.json", "ledger.parts.json"])
        mt = {f: (self.fx.out / f).stat().st_mtime_ns for f in files1}
        _, m2 = self.fx.run()
        self.assertEqual(self.fx.files(), files1)
        self.assertEqual({f: (self.fx.out / f).stat().st_mtime_ns for f in files1}, mt)
        self.assertEqual(json.dumps(m1, sort_keys=True), json.dumps(m2, sort_keys=True))
        self.assertTrue(m2["roundtrip_ok"])

    def test_entropy_hits_carry_hash_not_value(self):
        token = "".join(chr(65 + (i * 7) % 26) + str(i % 10) for i in range(24))  # 48 opaque chars
        self.fx = Fixture([item(1, responses=("see build " + token + " above",))])  # neutral context: no secret keyword
        report, manifest = self.fx.run(dry_run=True)
        hits = manifest["entropy_hits"]
        self.assertGreaterEqual(len(hits), 1)
        self.assertNotIn(token, json.dumps(manifest))
        self.assertEqual(hits[0]["sha256"], vaultlib.sha256_text(token))
        self.assertIn("where", hits[0])

    def test_cli_dry_run_exit_zero_and_report_shapes_only(self):
        self.fx = Fixture([item(1, prompts=("mail " + fake_email(),))])
        manifest_p = self.fx.out.parent / "m.json"
        report_p = self.fx.out.parent / "r.md"
        rc = el.main(["--dry-run", "--state", str(self.fx.state), "--out", str(self.fx.out), "--manifest", str(manifest_p),
                      "--report", str(report_p), "--review-dir", str(self.fx.review)])
        self.assertEqual(rc, 0)
        self.assertEqual(self.fx.files(), [])
        rep = vaultlib.read_text(report_p)
        self.assertNotIn(fake_email(), rep)
        self.assertNotIn(fake_email(), vaultlib.read_text(manifest_p))
        self.assertIn("- exported: 1 ", rep)
        self.assertIn("roundtrip_ok: True", rep)
        self.assertIn("forensic_skipped_as_duplicate: True", rep)


if __name__ == "__main__":
    unittest.main()
