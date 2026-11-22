"""T2 — denylist tests (two layers: READ / COPY), case-insensitive, path-component aware.

No real secret-looking strings live in this file; only file *names*.
"""
import json
import unittest

from tools import vaultlib
from tools.redact import DENYLIST_FILE, is_denied_path, load_denylist


class TestDenylistFile(unittest.TestCase):
    def test_file_shape(self):
        data = json.loads(vaultlib.read_text(DENYLIST_FILE))
        self.assertEqual(set(data), {"DENY_READ", "DENY_READ_DIRS", "DENY_COPY"})
        for key in data:
            self.assertIsInstance(data[key], list)
            self.assertTrue(data[key], key)
            self.assertTrue(all(isinstance(p, str) and p for p in data[key]), key)
        self.assertEqual(data["DENY_READ_DIRS"], ["secrets", ".ssh", ".aws", ".gnupg"])

    def test_patterns_mirror_gitignore(self):
        """Every deny pattern must also be ignored by git (PLAN §3.1: denylist == .gitignore)."""
        data = load_denylist()
        lines = {
            ln.strip()
            for ln in vaultlib.read_text(vaultlib.repo_root() / ".gitignore").splitlines()
            if ln.strip() and not ln.startswith("#")
        }
        for pat in data["DENY_READ"] + data["DENY_COPY"]:
            self.assertIn(pat, lines, f"{pat} missing from .gitignore")
        for d in data["DENY_READ_DIRS"]:
            self.assertIn(d + "/", lines, f"{d}/ missing from .gitignore")


class TestIsDeniedPath(unittest.TestCase):
    def test_key_files_denied_any_case(self):
        for name in ("keys.md", "KEYS.MD", "Keys.txt", "keystore.jks", "server.pem", "ID_RSA", "id_rsa.pub", "mykey.key"):
            with self.subTest(name=name):
                self.assertTrue(is_denied_path(name, "READ"))
                self.assertTrue(is_denied_path(name, "ANY"))

    def test_credential_and_account_files_denied(self):
        for name in (
            "oauth_creds.json", "google_accounts.json", "upstage_session.json", "my_accounts_backup.json",
            "credentials.json", "token_cache.json", "service.json", "unlimited-identity.json",
            "ACCOUNT_FUNDING_REGISTER.md", "account_funding_register.md", "app.cookies.txt", ".git-credentials",
            "my-secret-notes.md", "PASSWORD_LIST.txt", "wallet.dat", "seed_phrase.txt",
        ):
            with self.subTest(name=name):
                self.assertTrue(is_denied_path(name, "READ"))

    def test_session_env_log_files_denied(self):
        for name in ("crawler_user.session", "capture.har", ".env", ".ENV", ".env.local", "prod.env", "app.log", "client.ovpn", "kubeconfig.yaml"):
            with self.subTest(name=name):
                self.assertTrue(is_denied_path(name, "READ"))

    def test_file_inside_sensitive_dir_denied(self):
        for path in (
            "secrets/readme.md", "project/SECRETS/notes.md", "C:\\Users\\someone\\.ssh\\config",
            "/home/someone/.aws/config", "~/.gnupg/pubring.kbx", "D:\\proj\\.SSH\\known_hosts",
        ):
            with self.subTest(path=path):
                self.assertTrue(is_denied_path(path, "READ"))
                self.assertTrue(is_denied_path(path, "ANY"))

    def test_full_path_with_denied_component_denied(self):
        self.assertTrue(is_denied_path("D:\\SMS\\Root\\keys.md", "READ"))
        self.assertTrue(is_denied_path("/mnt/d/SMS/Root/Keys.TXT", "READ"))
        self.assertTrue(is_denied_path("memory/notes/credentials/overview.md", "READ"))

    def test_wal_denied_for_copy_not_read(self):
        for name in ("conversation_summaries.db-wal", "opencode.db-shm", "x.sqlite-wal"):
            with self.subTest(name=name):
                self.assertTrue(is_denied_path(name, "COPY"))
                self.assertFalse(is_denied_path(name, "READ"))
                self.assertTrue(is_denied_path(name, "ANY"))

    def test_db_and_pb_denied_for_copy(self):
        for name in ("opencode.db", "DATA.SQLITE", "x.sqlite3", "steps.pb"):
            with self.subTest(name=name):
                self.assertTrue(is_denied_path(name, "COPY"))
                self.assertFalse(is_denied_path(name, "READ"))

    def test_allowed_repo_files(self):
        for path in (
            "tools/redact.py", "tools\\redact.py", "skills/x/SKILL.md", "memory/HANDOFF.md",
            "rules/GEMINI.md", "conversations/summaries/2025-01.md", "profile/DECISIONS.md", "tools/patterns.json",
        ):
            with self.subTest(path=path):
                self.assertFalse(is_denied_path(path, "READ"))
                self.assertFalse(is_denied_path(path, "COPY"))
                self.assertFalse(is_denied_path(path, "ANY"))

    def test_layer_is_case_insensitive_and_validated(self):
        self.assertTrue(is_denied_path("keys.md", "read"))
        self.assertTrue(is_denied_path("x.db", "copy"))
        with self.assertRaises(ValueError):
            is_denied_path("keys.md", "WRITE")

    def test_empty_path_not_denied(self):
        self.assertFalse(is_denied_path("", "ANY"))


if __name__ == "__main__":
    unittest.main()
