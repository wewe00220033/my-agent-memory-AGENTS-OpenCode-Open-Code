"""Tests for tools/copy_sources.py on synthetic trees (tempfile).

Every secret-looking fixture is assembled at runtime by concatenation; no literal secret,
e-mail or phone number is stored in this file.
"""
import json
import os
import tempfile
import unittest
from pathlib import Path

from tools import copy_sources as cs
from tools import vaultlib


def put(root, rel, content, mtime=None):
    p = Path(root) / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, bytes):
        p.write_bytes(content)
    else:
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
    if mtime is not None:
        os.utime(p, (mtime, mtime))
    return p


def fake_email():
    return "person.name" + "@" + "example" + ".com"


def fake_egypt_phone():
    return "010" + "12345678"


def open_pem_block():
    return "-----" + "BEGIN PRIVATE KEY" + "-----\nQUJD\nREVG\n"  # no END marker -> unresolved


def tree_files(root):
    return sorted(p.relative_to(root).as_posix() for p in Path(root).rglob("*") if p.is_file())


def hex32_nonce():
    """32 hex chars assembled at runtime; Shannon entropy ~3.9 < ENTROPY_THRESHOLD (never an entropy hit)."""
    return ("a1b2c3d4" + "e5f60718") * 2


def high_entropy_value():
    """36 mixed-case alnum chars, assembled at runtime; not hex/uuid, matches no secret pattern."""
    return "Qz7" + "mW2pL" + "kX9vB" + "nR4tY" + "hJ6cF" + "dG1sA" + "uE8oI" + "wN3" + "Vb5"


class TestCopySources(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.src = Path(self._tmp.name) / "src"
        self.dst = Path(self._tmp.name) / "dst"
        self.src.mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def test_dry_run_writes_nothing(self):
        put(self.src, "a.md", "# a\nplain\n")
        put(self.src, "b/c.md", "mail " + fake_email() + "\n")
        rep = cs.copy_tree(self.src, self.dst, dry_run=True)
        self.assertEqual(len(rep.copied), 2)
        self.assertEqual(rep.counts.get("EMAIL"), 1)
        self.assertFalse(self.dst.exists())
        self.assertTrue(rep.ok)

    def test_deny_read_never_opened(self):
        put(self.src, "keys.md", "k\n")
        put(self.src, "secrets/plan.md", "s\n")
        put(self.src, "cfg/.env", "e\n")
        put(self.src, "ok.md", "fine\n")
        rep = cs.copy_tree(self.src, self.dst)
        self.assertEqual(sorted(rep.skipped_deny_read), ["cfg/.env", "keys.md", "secrets/plan.md"])
        self.assertEqual([c["src"] for c in rep.copied], ["ok.md"])
        self.assertEqual(tree_files(self.dst), ["manifest.json", "ok.md"])

    def test_deny_copy_skipped(self):
        put(self.src, "x.db", b"SQLite format 3\x00" + b"\x00" * 8)
        put(self.src, "x.db-wal", b"\x00" * 8)
        put(self.src, "notes.md", "n\n")
        rep = cs.copy_tree(self.src, self.dst)
        self.assertEqual(sorted(rep.skipped_deny_copy), ["x.db", "x.db-wal"])
        self.assertEqual(tree_files(self.dst), ["manifest.json", "notes.md"])

    def test_email_and_phone_redacted(self):
        email, phone = fake_email(), fake_egypt_phone()
        put(self.src, "contact.md", "write to " + email + "\ncall me on " + phone + " please\n")
        rep = cs.copy_tree(self.src, self.dst)
        out = vaultlib.read_text(self.dst / "contact.md")
        self.assertIn("[REDACTED:EMAIL]", out)
        self.assertIn("[REDACTED:PHONE]", out)
        self.assertNotIn(email, out)
        self.assertNotIn(phone, out)
        self.assertEqual(rep.counts["EMAIL"], 1)
        self.assertEqual(rep.counts["PHONE"], 1)
        manifest = vaultlib.read_text(self.dst / "manifest.json")
        self.assertNotIn(email, manifest)
        self.assertNotIn(phone, manifest)

    def test_dedupe_keeps_newest(self):
        body = "same text\nmail " + fake_email() + "\n"
        put(self.src, "old/a.md", body, mtime=1_600_000_000)
        put(self.src, "new/a.md", body, mtime=1_700_000_000)
        rep = cs.copy_tree(self.src, self.dst)
        self.assertEqual([c["src"] for c in rep.copied], ["new/a.md"])
        self.assertEqual(rep.skipped_dedupe, [{"src": "old/a.md", "kept": "new/a.md"}])
        self.assertEqual(tree_files(self.dst), ["manifest.json", "new/a.md"])

    def test_deny_read_reported_even_when_exclude_glob_matches(self):
        put(self.src, "keys.md", "k\n")
        put(self.src, "ok.md", "fine\n")
        rep = cs.copy_tree(self.src, self.dst, exclude_globs=["keys*"])
        self.assertEqual(rep.skipped_deny_read, ["keys.md"])  # never silently dropped by a glob
        self.assertEqual([c["src"] for c in rep.copied], ["ok.md"])

    def test_unresolved_private_key_skipped(self):
        put(self.src, "broken.md", "intro\n" + open_pem_block())
        put(self.src, "fine.md", "ok\n")
        rep = cs.copy_tree(self.src, self.dst)
        self.assertEqual(rep.skipped_sensitive, ["broken.md"])
        self.assertEqual(tree_files(self.dst), ["fine.md", "manifest.json"])
        self.assertTrue(rep.ok)

    def test_manifest_counts_and_hashes(self):
        put(self.src, "a.md", "alpha\n")
        put(self.src, "keys.txt", "k\n")
        put(self.src, "d.db", b"\x00")
        rep = cs.copy_tree(self.src, self.dst)
        data = json.loads(vaultlib.read_text(self.dst / "manifest.json"))
        self.assertEqual(data["summary"]["copied"], 1)
        self.assertEqual(data["summary"]["skipped_deny_read"], 1)
        self.assertEqual(data["summary"]["skipped_deny_copy"], 1)
        self.assertEqual(data["rejected_by_name"]["DENY_READ"], ["keys.txt"])
        expected = vaultlib.sha256_text(vaultlib.read_text(self.dst / "a.md"))
        self.assertEqual(data["files"]["a.md"]["sha256"], expected)
        self.assertEqual(rep.copied[0]["sha256"], expected)
        self.assertIn("redaction_counts", data)
        self.assertIn("entropy_hits", data)

    def test_idempotent_rerun(self):
        put(self.src, "a.md", "line  \n\n\n\n\nend\n")
        put(self.src, "sub/b.md", "mail " + fake_email() + "\n")
        rep1 = cs.copy_tree(self.src, self.dst)
        snap1 = {f: vaultlib.read_text(self.dst / f) for f in tree_files(self.dst)}
        mt1 = {f: (self.dst / f).stat().st_mtime_ns for f in snap1}
        rep2 = cs.copy_tree(self.src, self.dst)
        snap2 = {f: vaultlib.read_text(self.dst / f) for f in tree_files(self.dst)}
        self.assertEqual(snap1, snap2)
        self.assertEqual(rep1.summary(), rep2.summary())
        self.assertEqual(mt1["a.md"], (self.dst / "a.md").stat().st_mtime_ns)
        self.assertEqual(snap1["a.md"], "line\n\n\nend\n")

    def test_hash_pinned_high_entropy_redaction(self):
        value = high_entropy_value()
        body = "value one " + value + " here\nand again " + value + "\n"
        put(self.src, "notes.md", body)
        # without a pinned hash: recorded as entropy hits, value kept verbatim
        rep = cs.copy_tree(self.src, self.dst, dry_run=True)
        self.assertEqual(len(rep.entropy_hits), 2)
        self.assertNotIn("HIGH_ENTROPY", rep.counts)
        self.assertTrue(rep.ok)
        # with the pinned hash: every occurrence redacted, counted, dropped from entropy_hits
        rep = cs.copy_tree(self.src, self.dst, redact_value_hashes={vaultlib.sha256_text(value)})
        out = vaultlib.read_text(self.dst / "notes.md")
        self.assertNotIn(value, out)
        self.assertEqual(out.count("[REDACTED:HIGH_ENTROPY]"), 2)
        self.assertEqual(rep.counts["HIGH_ENTROPY"], 2)
        self.assertEqual(rep.entropy_hits, [])
        self.assertEqual(rep.copied[0]["redactions"], 2)
        self.assertNotIn(value, vaultlib.read_text(self.dst / "manifest.json"))
        self.assertTrue(rep.ok)
        # copy_file honours the same parameter
        rep2 = cs.copy_file(self.src / "notes.md", self.dst / "single", "notes.md",
                            redact_value_hashes={vaultlib.sha256_text(value)})
        self.assertEqual(rep2.counts["HIGH_ENTROPY"], 2)
        self.assertNotIn(value, vaultlib.read_text(self.dst / "single" / "notes.md"))

    def test_hash_pinned_hex32_below_threshold_redacted(self):
        value = hex32_nonce()
        put(self.src, "link.md", "magic link fragment " + value + " expires soon\n")
        rep = cs.copy_tree(self.src, self.dst, dry_run=True)
        self.assertEqual(rep.entropy_hits, [])  # below the threshold: the entropy pass never reports it
        self.assertNotIn("HIGH_ENTROPY", rep.counts)
        rep = cs.copy_tree(self.src, self.dst, redact_value_hashes={vaultlib.sha256_text(value)})
        out = vaultlib.read_text(self.dst / "link.md")
        self.assertNotIn(value, out)
        self.assertEqual(out.count("[REDACTED:HIGH_ENTROPY]"), 1)
        self.assertEqual(rep.counts["HIGH_ENTROPY"], 1)
        self.assertEqual(rep.entropy_hits, [])
        self.assertTrue(rep.ok)

    def test_cli_dry_run_exit_zero(self):
        put(self.src, "a.md", "x\n")
        rc = cs.main([str(self.src), str(self.dst), "--dry-run", "--ext", ".md"])
        self.assertEqual(rc, 0)
        self.assertFalse(self.dst.exists())


if __name__ == "__main__":
    unittest.main()
