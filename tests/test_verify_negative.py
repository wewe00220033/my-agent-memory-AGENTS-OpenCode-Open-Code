"""Negative tests for tools/verify_no_secrets.py on a synthetic (non-git) tree.

Every fixture value is assembled programmatically so that no secret-looking
literal is stored in this file. This file is in SELF_EXEMPT (pattern scan).
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools import verify_no_secrets as vns

repo = Path(__file__).resolve().parents[1]
tool = repo / "tools" / "verify_no_secrets.py"


def put(root, rel, content):
    p = Path(root) / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, bytes):
        p.write_bytes(content)
    else:
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
    return p


def run_verifier(root, *extra):
    env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
    p = subprocess.run(
        [sys.executable, str(tool), "--root", str(root), "--no-history", *extra],
        cwd=str(repo), capture_output=True, encoding="utf-8", errors="replace", env=env,
    )
    return p.returncode, p.stdout + p.stderr


def fake_github_pat():
    return "ghp" + "_" + ("Ab1" * 12)  # 36 alnum chars after the prefix


def fake_email():
    return "someone.here" + "@" + "example" + ".org"


class TestVerifyNegative(unittest.TestCase):
    def test_denied_file_name(self):
        with tempfile.TemporaryDirectory() as d:
            put(d, "notes/keys_backup.txt", "nothing here\n")
            rc, out = run_verifier(d)
            self.assertEqual(rc, 1, out)
            self.assertIn("DENIED_PATH", out)
            self.assertIn("VERIFY: FAIL", out)

    def test_github_token_in_markdown(self):
        with tempfile.TemporaryDirectory() as d:
            value = fake_github_pat()
            put(d, "docs/notes.md", "see " + value + " for details\n")
            rc, out = run_verifier(d)
            self.assertEqual(rc, 1, out)
            self.assertIn("SECRET_PATTERN:GITHUB_TOKEN", out)
            self.assertIn("docs/notes.md:1", out)
            self.assertIn("VERIFY: FAIL", out)
            self.assertNotIn(value, out)

    def test_email_in_text(self):
        with tempfile.TemporaryDirectory() as d:
            value = fake_email()
            put(d, "contact.md", "line one\nwrite to " + value + "\n")
            rc, out = run_verifier(d)
            self.assertEqual(rc, 1, out)
            self.assertIn("SECRET_PATTERN:EMAIL", out)
            self.assertIn("contact.md:2", out)
            self.assertNotIn(value, out)
            self.assertNotIn(value.split("@")[0], out)

    def test_binary_db_file(self):
        with tempfile.TemporaryDirectory() as d:
            put(d, "data/store.db", b"SQLite format 3\x00" + b"\x00" * 64)
            put(d, "data/store.db-wal", b"\x00" * 16)
            rc, out = run_verifier(d)
            self.assertEqual(rc, 1, out)
            self.assertIn("BINARY_DB", out)
            self.assertIn("VERIFY: FAIL", out)

    def test_oversize_file(self):
        with tempfile.TemporaryDirectory() as d:
            put(d, "big.md", "x" * (vns.MAX_FILE_BYTES + 1))
            rc, out = run_verifier(d)
            self.assertEqual(rc, 1, out)
            self.assertIn("OVERSIZE", out)

    def test_clean_tree_passes(self):
        with tempfile.TemporaryDirectory() as d:
            put(d, "README.md", "# clean\n\nplain text only\n")
            put(d, "src/app.py", "def main():\n    return 0\n")
            put(d, "empty/.gitkeep", "")
            rc, out = run_verifier(d)
            self.assertEqual(rc, 0, out)
            self.assertIn("VERIFY: CLEAN", out)

    def test_self_exempt_paths_skip_pattern_scan_only(self):
        with tempfile.TemporaryDirectory() as d:
            put(d, "tests/test_redact.py", "x = '" + fake_email() + "'\n")
            rc, out = run_verifier(d)
            self.assertEqual(rc, 0, out)
            put(d, "README.md", fake_email() + "\n")
            rc, out = run_verifier(d)
            self.assertEqual(rc, 1, out)
            self.assertIn("README.md:1", out)

    def test_python_code_skips_kv_heuristics_only(self):
        kv_line = "API_TOKEN = " + "'" + "placeholder-value-1234" + "'" + "\n"
        with tempfile.TemporaryDirectory() as d:
            put(d, "src/config.py", kv_line)
            rc, out = run_verifier(d)
            self.assertEqual(rc, 0, out)
            put(d, "notes/config.md", kv_line)
            rc, out = run_verifier(d)
            self.assertEqual(rc, 1, out)
            self.assertIn("SECRET_PATTERN:KV_SECRET", out)
            self.assertIn("notes/config.md:1", out)
            self.assertNotIn("src/config.py", out)

    def test_python_code_still_fails_on_strong_patterns(self):
        with tempfile.TemporaryDirectory() as d:
            value = fake_github_pat()
            put(d, "src/app.py", "TOKEN = '" + value + "'\n")
            rc, out = run_verifier(d)
            self.assertEqual(rc, 1, out)
            self.assertIn("SECRET_PATTERN:GITHUB_TOKEN", out)
            self.assertIn("src/app.py:1", out)
            self.assertNotIn(value, out)

    def test_noreply_github_email_is_clean(self):
        value = "12345678+someone" + "@" + "users.noreply.github" + ".com"
        with tempfile.TemporaryDirectory() as d:
            put(d, "docs/identity.md", "commits are signed as " + value + "\n")
            rc, out = run_verifier(d)
            self.assertEqual(rc, 0, out)
            self.assertIn("VERIFY: CLEAN", out)

    def test_python_plain_assignment_is_clean(self):
        with tempfile.TemporaryDirectory() as d:
            put(d, "src/consts.py",
                "NAME = \"manifest.json\"\n" + "keys = cur.execute(\"select 1\")\n" + "rows.sort(key=lambda r: r[0])\n")
            rc, out = run_verifier(d)
            self.assertEqual(rc, 0, out)
            self.assertIn("VERIFY: CLEAN", out)

    def test_json_report_has_kinds_but_no_values(self):
        with tempfile.TemporaryDirectory() as d:
            value = fake_github_pat()
            put(d, "a.md", value + "\n")
            put(d, "keys.md", "k\n")
            report = Path(d) / "out" / "report.json"
            rc, out = run_verifier(d, "--json", str(report))
            self.assertEqual(rc, 1, out)
            data = json.loads(report.read_text(encoding="utf-8"))
            kinds = sorted({v["kind"] for v in data["violations"]})
            self.assertEqual(kinds, ["DENIED_PATH", "SECRET_PATTERN"])
            self.assertEqual(data["result"], "FAIL")
            self.assertNotIn(value, report.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
