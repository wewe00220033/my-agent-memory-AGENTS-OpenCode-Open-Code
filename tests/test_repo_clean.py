"""Repository-level gate (PLAN 3.3): the real tree must be clean.

No secret-looking literal lives in this file; only file names and rule checks.
"""
import os
import subprocess
import sys
import unittest
from pathlib import Path

from tools import vaultlib
from tools.redact import is_denied_path
from tools.verify_no_secrets import TOOL_REL

REPO = vaultlib.repo_root()
TOOL = REPO / TOOL_REL


def git_lines(*args):
    p = subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, encoding="utf-8", errors="replace")
    if p.returncode != 0:
        return None
    return [ln for ln in p.stdout.splitlines() if ln.strip()]


def repo_files():
    """tracked + untracked-not-ignored (git), or a plain walk when git is unavailable."""
    tracked = git_lines("ls-files")
    others = git_lines("ls-files", "--others", "--exclude-standard")
    if tracked is not None and others is not None:
        return sorted(set(tracked) | set(others))
    out = []
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in {".git", "_local", "__pycache__"}]
        for fn in filenames:
            out.append((Path(dirpath) / fn).relative_to(REPO).as_posix())
    return sorted(out)


class TestRepoClean(unittest.TestCase):
    def test_verifier_reports_clean_on_repo(self):
        env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
        p = subprocess.run([sys.executable, str(TOOL)], cwd=str(REPO), capture_output=True,
                           encoding="utf-8", errors="replace", env=env)
        out = p.stdout + p.stderr
        self.assertEqual(p.returncode, 0, out)
        self.assertIn("VERIFY: CLEAN", out)

    def test_no_denied_path_in_tree(self):
        bad = [f for f in repo_files() if f != TOOL_REL and is_denied_path(f, "READ")]
        self.assertEqual(bad, [], "DENY_READ names present in the tree")

    def test_no_database_artifacts_in_tree(self):
        suffixes = (".db", ".sqlite", ".sqlite3", ".db-wal", ".db-shm", "-wal", "-shm", ".pb")
        bad = []
        for dirpath, dirnames, filenames in os.walk(REPO):
            dirnames[:] = [d for d in dirnames if d not in {".git", "_local"}]
            for fn in filenames:
                if fn.lower().endswith(suffixes):
                    bad.append((Path(dirpath) / fn).relative_to(REPO).as_posix())
        self.assertEqual(bad, [], "database artefacts outside _local/")

    def test_gitignore_keeps_local_and_coordination_files_out(self):
        lines = {ln.strip() for ln in vaultlib.read_text(REPO / ".gitignore").splitlines() if ln.strip() and not ln.startswith("#")}
        for needed in ("_local/", "BRIEF_FOR_PLANNER.md", "OWNER_DECISIONS_R2.md", "COMPASS_NOTE_S0.md"):
            self.assertIn(needed, lines)
        self.assertIn("!" + TOOL_REL, lines)

    def test_local_dir_never_listed_by_git(self):
        files = repo_files()
        self.assertEqual([f for f in files if f.startswith("_local/")], [])


if __name__ == "__main__":
    unittest.main()
