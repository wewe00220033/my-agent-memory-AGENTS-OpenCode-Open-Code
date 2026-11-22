"""Repository gate: fail when anything secret-looking could be published (PLAN 3.3).

Every violation is reported by KIND + location only, NEVER by value:
  DENIED_PATH               file name / path component matches DENY_READ (tools/denylist.json)
  BINARY_DB                 DENY_COPY artefact (*.db, *.sqlite*, *-wal, *-shm, *.pb) or SQLite header
  OVERSIZE                  file larger than MAX_FILE_BYTES (hard 5 MB limit, PLAN 4)
  SECRET_PATTERN:<CATEGORY> a redact.py pattern still matching in a text file (or ENCODED blob)
  HISTORY_SECRET:<CATEGORY> the same, in an ADDED line of ``git log -p <range>``
  COMMIT_EMAIL              a commit in <range> whose author e-mail is not a GitHub noreply address

File sets: ``git ls-files`` + ``git ls-files --others --exclude-standard`` (git mode) or a
recursive walk (``--root`` without git) minus ``.gitkeep``, ``.git/``, ``_local/``,
``__pycache__/`` and binary files (NUL byte in the first 8 KB).

Pattern scan rules:
  * ``.py`` sources: strong categories only (CODE_CATEGORIES) - the KV_SECRET / PHONE / PII
    heuristics are false positives by construction on code.
  * everything else: all categories except PATH.
  * an e-mail ending in ``@users.noreply.github.com`` is never a violation (public commit identity).
  * SELF_EXEMPT files (the engine, its config and the fixture-building tests) skip the pattern
    scan only; DENIED_PATH (except this tool's own name) / OVERSIZE / BINARY_DB still apply.

History range: ``HISTORY_BASELINE..HEAD`` when the baseline commit exists, otherwise ``--all``.

CLI: python tools/verify_no_secrets.py [--root DIR] [--no-history] [--json OUT.json] [--quiet]
Exit code 0 = CLEAN, 1 = FAIL, 2 = usage / environment error.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

if __package__ in (None, ""):  # executed as a script: make ``tools`` importable
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import redact, vaultlib  # noqa: E402

MAX_FILE_BYTES = 5 * 1024 * 1024
BINARY_PROBE_BYTES = 8 * 1024
NOREPLY_SUFFIX = "@users.noreply.github.com"
# COMPASS_NOTE_S0: the commits up to this baseline were created from the GitHub UI before the
# noreply identity was configured; identity + patch checks apply to <baseline>..HEAD only.
HISTORY_BASELINE = "d669dbda4263fbd0a9d74996c9ac69546eff580e"
TOOL_REL = "tools/verify_no_secrets.py"  # its own name matches ``*secret*`` -> DENY_READ exemption

# Pattern scan is skipped for exactly these files (fixtures there are assembled at runtime).
SELF_EXEMPT: Tuple[str, ...] = (
    TOOL_REL,
    "tools/redact.py",
    "tools/patterns.json",
    "tools/denylist.json",
    "tests/test_redact.py",
    "tests/test_denylist.py",
    "tests/test_verify_negative.py",
)

CODE_SUFFIXES = (".py",)
CODE_CATEGORIES = frozenset({
    "PRIVATE_KEY", "URL_WITH_CREDS", "OAUTH_JWT", "GITHUB_TOKEN", "WEBHOOK", "API_KEY", "EMAIL",
})
TEXT_SKIP_CATEGORIES = frozenset({"PATH"})

SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", "_local"}
SKIP_NAMES = {".gitkeep"}
SQLITE_HEADER = b"SQLite format 3\x00"
_NOREPLY_EMAIL = re.compile(r"^[A-Za-z0-9._%+\-]+@users\.noreply\.github\.com$")
_COMMIT_LINE = re.compile(r"^commit ([0-9a-f]{40})", re.M)
_DIFF_LINE = re.compile(r"^diff --git a/(.+?) b/(.+?)$", re.M)


@dataclass
class Violation:
    kind: str
    path: str
    line: int = 0
    category: str = ""
    detail: str = ""

    def key(self) -> str:
        return self.kind + (":" + self.category if self.category else "")

    def render(self) -> str:
        loc = self.path + (":%d" % self.line if self.line else "")
        return self.key() + " " + loc + ((" (" + self.detail + ")") if self.detail else "")


# --------------------------------------------------------------------------- helpers

def _rel(root: Path, p: Path) -> str:
    try:
        return p.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return p.as_posix()


def is_self_exempt(rel: str) -> bool:
    return rel.replace("\\", "/") in SELF_EXEMPT


def _git(root: Path, *args: str) -> Tuple[int, str]:
    env = dict(os.environ, GIT_PAGER="cat", PAGER="cat", LC_ALL="C.UTF-8")
    try:
        p = subprocess.run(["git", "-C", str(root), *args], capture_output=True, env=env)
    except (OSError, FileNotFoundError):
        return 127, ""
    out = p.stdout.decode("utf-8", "replace") if p.returncode == 0 else p.stderr.decode("utf-8", "replace")
    return p.returncode, out


def is_git_worktree(root: Path) -> bool:
    rc, out = _git(root, "rev-parse", "--is-inside-work-tree")
    return rc == 0 and out.strip() == "true"


def list_git_files(root: Path) -> List[str]:
    files: List[str] = []
    for args in (("ls-files", "-z"), ("ls-files", "-z", "--others", "--exclude-standard")):
        rc, out = _git(root, *args)
        if rc != 0:
            raise RuntimeError("git %s failed" % " ".join(args))
        files.extend(x for x in out.split("\0") if x)
    return sorted(set(files))


def walk_files(root: Path) -> List[str]:
    out: List[str] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for fn in sorted(filenames):
            out.append(_rel(root, Path(dirpath) / fn))
    return out


def _scan_patterns() -> List[redact.Pattern]:
    return [p for p in redact.load_patterns() if p.category not in TEXT_SKIP_CATEGORIES]


def patterns_for(rel: str, patterns: Sequence[redact.Pattern]) -> List[redact.Pattern]:
    """Pattern subset for *rel*: code files keep the strong categories only."""
    if rel.lower().endswith(CODE_SUFFIXES):
        return [p for p in patterns if p.category in CODE_CATEGORIES]
    return list(patterns)


def _allowed_value(value: str, allow_exact: frozenset) -> bool:
    return value in allow_exact or bool(_NOREPLY_EMAIL.match(value))


def find_secret_matches(text: str, patterns: Optional[Sequence[redact.Pattern]] = None) -> List[Tuple[int, str, str]]:
    """Return (line_number, category, pattern_name) for every live secret match in *text*.

    Values are never returned. Allow-listed exact terms, existing ``[REDACTED:..]`` markers and
    GitHub noreply addresses are ignored. Base64 blobs are decoded and re-scanned (ENCODED).
    """
    pats = list(patterns) if patterns is not None else _scan_patterns()
    allow_exact = frozenset(vaultlib.nfc(t) for t in redact.DEFAULT_ALLOWLIST if t)
    text = vaultlib.nfc(text)
    hits: List[Tuple[int, str, str]] = []
    for pt in pats:
        for m in pt.regex.finditer(text):
            s, e = redact._span(pt, m)
            if s < 0 or e <= s:
                continue
            value = text[s:e]
            if redact.MARKER_PREFIX in value or _allowed_value(value, allow_exact):
                continue
            if pt.check and not redact.CHECKS[pt.check](text, m, value):
                continue
            hits.append((text.count("\n", 0, s) + 1, pt.category, pt.name))
    for rx, name in ((redact._B64_STD, "base64_std"), (redact._B64_URL, "base64_url")):
        for m in rx.finditer(text):
            decoded = redact._decode_b64(m.group())
            if decoded and redact._has_secret(decoded, pats):
                hits.append((text.count("\n", 0, m.start()) + 1, "ENCODED", name))
    for m in redact._PK_RESIDUE.finditer(text):
        hits.append((text.count("\n", 0, m.start()) + 1, "PRIVATE_KEY", "pem_residue"))
    return sorted(set(hits))


# --------------------------------------------------------------------------- tree checks

def check_file(root: Path, rel: str, patterns: Sequence[redact.Pattern]) -> List[Violation]:
    v: List[Violation] = []
    p = root / rel
    if rel != TOOL_REL and redact.is_denied_path(rel, "READ"):
        v.append(Violation("DENIED_PATH", rel, detail="DENY_READ name/component"))
        return v  # never opened
    if redact.is_denied_path(rel, "COPY"):
        v.append(Violation("BINARY_DB", rel, detail="DENY_COPY artefact"))
        return v
    try:
        size = p.stat().st_size
    except OSError as exc:
        return [Violation("UNREADABLE", rel, detail=type(exc).__name__)]
    if size > MAX_FILE_BYTES:
        v.append(Violation("OVERSIZE", rel, detail="%d bytes > %d" % (size, MAX_FILE_BYTES)))
        return v  # not read
    try:
        with open(p, "rb") as f:
            head = f.read(BINARY_PROBE_BYTES)
    except OSError as exc:
        return [Violation("UNREADABLE", rel, detail=type(exc).__name__)]
    if head.startswith(SQLITE_HEADER):
        v.append(Violation("BINARY_DB", rel, detail="sqlite header"))
        return v
    if b"\x00" in head or is_self_exempt(rel):
        return v  # binary (nothing textual) or exempt from the pattern scan
    try:
        text = vaultlib.read_text(p)
    except UnicodeDecodeError:
        return v
    except OSError as exc:
        return [Violation("UNREADABLE", rel, detail=type(exc).__name__)]
    for line, cat, name in find_secret_matches(text, patterns_for(rel, patterns)):
        v.append(Violation("SECRET_PATTERN", rel, line, cat, "pattern=" + name))
    return v


# --------------------------------------------------------------------------- history checks

def history_range(root: Path, baseline: str = HISTORY_BASELINE) -> Tuple[List[str], str]:
    """(git revision args, note). ``[]`` + note when there is nothing to scan."""
    rc, _ = _git(root, "rev-parse", "--verify", "--quiet", "HEAD^{commit}")
    if rc != 0:
        return [], "no HEAD commit - history skipped"
    if baseline:
        rc, _ = _git(root, "cat-file", "-e", baseline + "^{commit}")
        if rc == 0:
            rng = baseline + "..HEAD"
            rc, out = _git(root, "rev-list", "--count", rng)
            if rc == 0 and out.strip() == "0":
                return [], "range %s..HEAD is empty - history skipped" % baseline[:7]
            return [rng], "range %s..HEAD" % baseline[:7]
    return ["--all"], "baseline commit not found - whole history scanned"


def _added_lines(body: str) -> str:
    return "\n".join(ln[1:] for ln in body.split("\n") if ln.startswith("+") and not ln.startswith("+++"))


def check_history(root: Path, patterns: Sequence[redact.Pattern],
                  baseline: str = HISTORY_BASELINE) -> Tuple[List[Violation], int, str, List[str]]:
    """Scan commit identities and ADDED patch lines over the history range.
    Returns (violations, commits_in_range, range_note, warnings)."""
    v: List[Violation] = []
    warnings: List[str] = []
    rev, note = history_range(root, baseline)
    if not rev:
        return v, 0, note, warnings

    rc, out = _git(root, "log", "--format=%h%x09%ae", *rev)
    if rc != 0:
        v.append(Violation("HISTORY_UNREADABLE", "history", detail="git log identities failed"))
        return v, 0, note, warnings
    commits = 0
    for ln in out.splitlines():
        if not ln.strip():
            continue
        commits += 1
        short, _, email = ln.partition("\t")
        if not email.strip().lower().endswith(NOREPLY_SUFFIX):
            v.append(Violation("COMMIT_EMAIL", "history:" + short, detail="author is not a GitHub noreply identity"))

    rc, cfg = _git(root, "config", "--get", "user.email")
    if rc == 0 and not cfg.strip().lower().endswith(NOREPLY_SUFFIX):
        warnings.append("git config user.email is not a GitHub noreply identity (future commits would fail COMMIT_EMAIL)")

    rc, log = _git(root, "log", "-p", "--no-color", "--format=commit %H", *rev)
    if rc != 0:
        v.append(Violation("HISTORY_UNREADABLE", "history", detail="git log -p failed"))
        return v, commits, note, warnings
    log = log.replace("\r\n", "\n")
    bounds = [(m.start(), m.group(1)) for m in _COMMIT_LINE.finditer(log)] + [(len(log), "")]
    for i in range(len(bounds) - 1):
        start, sha = bounds[i]
        chunk = log[start:bounds[i + 1][0]]
        diffs = [(m.start(), m.group(2)) for m in _DIFF_LINE.finditer(chunk)] + [(len(chunk), "")]
        for j in range(len(diffs) - 1):
            dstart, path = diffs[j]
            body = chunk[dstart:diffs[j + 1][0]]
            loc = "history:%s:%s" % (sha[:7], path)
            if path != TOOL_REL and redact.is_denied_path(path, "READ"):
                v.append(Violation("DENIED_PATH", loc, detail="DENY_READ path in history"))
                continue
            if redact.is_denied_path(path, "COPY"):
                v.append(Violation("BINARY_DB", loc, detail="DENY_COPY path in history"))
                continue
            if is_self_exempt(path):
                continue
            seen = set()
            for _line, cat, name in find_secret_matches(_added_lines(body), patterns_for(path, patterns)):
                if (cat, name) in seen:
                    continue
                seen.add((cat, name))
                v.append(Violation("HISTORY_SECRET", loc, 0, cat, "pattern=" + name))
    return v, commits, note, warnings


# --------------------------------------------------------------------------- driver

def verify(root: Path, history: bool = True, baseline: str = HISTORY_BASELINE) -> Dict[str, object]:
    root = Path(root).expanduser().resolve()
    if not root.is_dir():
        raise FileNotFoundError("root is not a directory: %s" % root.name)
    git_mode = is_git_worktree(root)
    files = [f for f in (list_git_files(root) if git_mode else walk_files(root))
             if Path(f).name not in SKIP_NAMES and (root / f).is_file()]
    patterns = _scan_patterns()
    violations: List[Violation] = []
    for rel in files:
        violations.extend(check_file(root, rel, patterns))
    commits, note, warnings = 0, "history not scanned", []
    history_scanned = bool(history and git_mode)
    if history_scanned:
        hv, commits, note, warnings = check_history(root, patterns, baseline)
        violations.extend(hv)
    return {
        "result": "CLEAN" if not violations else "FAIL",
        "root": root.name,
        "mode": "git" if git_mode else "tree",
        "files": len(files),
        "history_scanned": history_scanned,
        "history_note": note,
        "commits": commits,
        "max_file_bytes": MAX_FILE_BYTES,
        "warnings": warnings,
        "by_kind": dict(sorted(Counter(x.key() for x in violations).items())),
        "violations": [asdict(x) for x in violations],
        "_objects": violations,
    }


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Fail when the tree or git history contains anything secret-looking.")
    ap.add_argument("--root", default=str(vaultlib.repo_root()), help="directory to verify (default: repo root)")
    ap.add_argument("--no-history", action="store_true", help="skip git log / identity checks")
    ap.add_argument("--baseline", default=HISTORY_BASELINE,
                    help="scan history on REV..HEAD only (default: %(default)s; '' = all commits)")
    ap.add_argument("--json", default="", help="write a JSON report (kinds + locations only, never values)")
    ap.add_argument("--quiet", action="store_true", help="print only the final verdict line")
    a = ap.parse_args(argv)

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass
    try:
        res = verify(Path(a.root), history=not a.no_history, baseline=a.baseline)
    except (FileNotFoundError, RuntimeError) as exc:
        print("[verify_no_secrets] ERROR: %s" % exc)
        return 2

    objs: List[Violation] = res.pop("_objects")  # type: ignore[assignment]
    if a.json:
        vaultlib.write_text(a.json, json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    if not a.quiet:
        print("[verify_no_secrets] root=%s mode=%s files=%d history=%s commits=%d" % (
            res["root"], res["mode"], res["files"], res["history_note"] if res["history_scanned"] else "no", res["commits"]))
        for w in res["warnings"]:  # type: ignore[union-attr]
            print("WARNING: " + w)
        for x in objs:
            print(x.render())
        if objs:
            print("[verify_no_secrets] violations by kind: " + ", ".join(
                "%s=%d" % kv for kv in res["by_kind"].items()))  # type: ignore[union-attr]
    if objs:
        print("VERIFY: FAIL (%d)" % len(objs))
        return 1
    print("VERIFY: CLEAN (files=%d)" % res["files"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
