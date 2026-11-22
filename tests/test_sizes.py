"""Size gates (PLAN 2.1 / 4): hard 5 MB per file, .md <= 1 MB and .json <= 2 MB in export
directories, and a printed WARNING (never a failure) when AGENTS.md exceeds 64 KB.
"""
import os
import subprocess
import sys
import unittest
from pathlib import Path

from tools import vaultlib
from tools.shard import JSON_MAX, MD_MAX
from tools.verify_no_secrets import MAX_FILE_BYTES

REPO = vaultlib.repo_root()
AGENTS_WARN_BYTES = 64 * 1024
EXPORT_DIRS = ("conversations", "brain", "memory")


def repo_files():
    def git(*args):
        p = subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, encoding="utf-8", errors="replace")
        return None if p.returncode else [ln for ln in p.stdout.splitlines() if ln.strip()]

    tracked, others = git("ls-files"), git("ls-files", "--others", "--exclude-standard")
    if tracked is not None and others is not None:
        return sorted(set(tracked) | set(others))
    out = []
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in {".git", "_local", "__pycache__"}]
        out.extend((Path(dirpath) / fn).relative_to(REPO).as_posix() for fn in filenames)
    return sorted(out)


class TestSizes(unittest.TestCase):
    def test_every_file_within_hard_limit(self):
        too_big = []
        for rel in repo_files():
            p = REPO / rel
            if p.is_file() and p.stat().st_size > MAX_FILE_BYTES:
                too_big.append(rel)
        self.assertEqual(too_big, [])

    def test_agents_md_warns_only_when_large(self):
        p = REPO / "AGENTS.md"
        if not p.is_file():
            self.skipTest("AGENTS.md not written yet (S1/T7)")
        size = p.stat().st_size
        if size > AGENTS_WARN_BYTES:
            print("WARNING: AGENTS.md is %d bytes (> %d) - consider condensing" % (size, AGENTS_WARN_BYTES), file=sys.stderr)
        self.assertLessEqual(size, MAX_FILE_BYTES)

    def test_export_dirs_respect_shard_limits(self):
        bad = []
        for rel in repo_files():
            if not rel.startswith(tuple(d + "/" for d in EXPORT_DIRS)):
                continue
            p = REPO / rel
            if not p.is_file():
                continue
            size = p.stat().st_size
            suffix = p.suffix.lower()
            if suffix == ".md" and size > MD_MAX:
                bad.append((rel, size, MD_MAX))
            elif suffix == ".json" and size > JSON_MAX:
                bad.append((rel, size, JSON_MAX))
        self.assertEqual(bad, [])

    def test_limits_are_consistent(self):
        self.assertLess(MD_MAX, JSON_MAX)
        self.assertLess(JSON_MAX, MAX_FILE_BYTES)


if __name__ == "__main__":
    unittest.main()
