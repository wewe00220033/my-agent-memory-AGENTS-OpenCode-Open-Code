"""T6: export the owner's rules / workflows / skills / commands into the vault (PLAN S1).

Sources (under the user's home, never hard-coded absolute paths) -> targets (repo root):
  ~/.gemini/GEMINI.md                 -> rules/GEMINI.md        (copy_file)
  ~/.gemini/config/rules/*.md         -> rules/
  ~/.gemini/config/workflows/*.md     -> workflows/
  ~/.gemini/config/skills/**/*.md     -> skills/   (keeps <name>/SKILL.md structure)
  ~/.config/opencode/commands/*.md    -> commands/

Every file goes through tools/copy_sources (denylist -> redact -> residual check -> dedupe ->
idempotent write). Manifests are written OUTSIDE the published tree:
  _local/manifests/T6/<target>.manifest.json  (merged report per target)
After a real run ``skills/INDEX.md`` is regenerated (name | <= 10-word description | link).

CLI: python tools/export_rules.py [--dry-run] [--top 20] [--home DIR]
Exit 0 on success, 1 when any target reports errors.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Sequence

if __package__ in (None, ""):  # executed as a script: make ``tools`` importable
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import copy_sources, redact, vaultlib  # noqa: E402

REPO = vaultlib.repo_root()
MANIFEST_DIR = REPO / "_local" / "manifests" / "T6"
MAX_DESC_WORDS = 10
AUTO_START, AUTO_END = "<!-- AUTO-INDEX:START -->", "<!-- AUTO-INDEX:END -->"

# (target dir name, source relative to home, kind)  kind: "file" | "tree"
TARGETS = (
    ("rules", ".gemini/GEMINI.md", "file"),
    ("rules", ".gemini/config/rules", "tree"),
    ("workflows", ".gemini/config/workflows", "tree"),
    ("skills", ".gemini/config/skills", "tree"),
    ("commands", ".config/opencode/commands", "tree"),
)

_FRONT = re.compile(r"\A---[ \t]*\n(.*?)\n---[ \t]*\n", re.S)
_DESC = re.compile(r"^description[ \t]*:[ \t]*(.*)$", re.M | re.I)
_WS = re.compile(r"\s+")
_ALPHA = re.compile(r"[A-Za-z\u0600-\u06FF]")
_DECOR_START = ("#", "<!--", "---", "|", ">", "===", "***")


def _is_prose(line: str) -> bool:
    """True for a real sentence: not a heading/comment/rule/table/quote/decoration, and it
    contains at least one alphabetic (Latin or Arabic) character."""
    s = line.strip()
    if not s or s.startswith(_DECOR_START):
        return False
    if not _ALPHA.search(s):
        return False
    # lines that are mostly box-drawing / punctuation decoration (e.g. "══ title ══") are skipped
    letters = len(_ALPHA.findall(s))
    return letters * 3 >= len(s.replace(" ", ""))


# --------------------------------------------------------------------------- export

def _merge(into: copy_sources.CopyReport, other: copy_sources.CopyReport) -> None:
    for name in ("copied", "skipped_deny_read", "skipped_deny_copy", "skipped_sensitive",
                 "skipped_dedupe", "skipped_size", "skipped_binary", "entropy_hits", "top_redacted", "errors"):
        getattr(into, name).extend(getattr(other, name))
    into.counts.update(other.counts)


def export_all(home: Path, repo: Path, *, dry_run: bool, top_n: int,
               manifest_dir: Optional[Path] = None) -> Dict[str, copy_sources.CopyReport]:
    reports: Dict[str, copy_sources.CopyReport] = {}
    for target, src_rel, kind in TARGETS:
        rep = reports.setdefault(target, copy_sources.CopyReport())
        src = home / src_rel
        if kind == "file":
            copy_sources.copy_file(src, repo / target, src.name, report=rep, dry_run=dry_run)
            continue
        if not src.is_dir():
            rep.errors.append({"src": target, "error": "FileNotFoundError: source directory missing"})
            continue
        _merge(rep, copy_sources.copy_tree(src, repo / target, include_exts=(".md",), dry_run=True, top_n=top_n))
        if not dry_run:
            # second pass writes (idempotent); the dry pass above already produced the report
            copy_sources.copy_tree(src, repo / target, include_exts=(".md",), dry_run=False, top_n=top_n,
                                   manifest_dir=(manifest_dir or MANIFEST_DIR) / target)
    for rep in reports.values():
        rep.top_redacted.sort(key=lambda r: (-r["redactions"], r["path"]))
        del rep.top_redacted[top_n:]
    if not dry_run:
        mdir = manifest_dir or MANIFEST_DIR
        for target, rep in reports.items():
            vaultlib.write_text(mdir / (target + ".manifest.json"),
                                json.dumps(copy_sources.build_manifest(rep), indent=2, sort_keys=True,
                                           ensure_ascii=False) + "\n")
    return reports


# --------------------------------------------------------------------------- skills index

def skill_description(text: str) -> str:
    """<= MAX_DESC_WORDS words from front-matter ``description:`` or the first prose line (redacted)."""
    desc = ""
    fm = _FRONT.match(text)
    body = text[fm.end():] if fm else text
    if fm:
        m = _DESC.search(fm.group(1))
        if m:
            desc = m.group(1).strip().strip("\"'")
            if desc in ("", ">", "|", ">-", "|-"):  # block scalar: take the following indented lines
                lines = fm.group(1)[m.end():].split("\n")
                desc = " ".join(ln.strip() for ln in lines[1:] if ln.startswith((" ", "\t")) and ln.strip())
    if not desc:
        in_fence = False
        for ln in body.split("\n"):
            s = ln.strip()
            if s.startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence or not s or not _is_prose(s):
                continue
            desc = s
            break
    desc = redact.redact_text(desc).text
    words = _WS.sub(" ", desc.replace("|", "/")).strip().split(" ")
    return " ".join(w for w in words[:MAX_DESC_WORDS] if w) or "-"


def build_skills_index(skills_dir: Path) -> str:
    rows: List[str] = []
    for skill in sorted(p for p in skills_dir.glob("*/SKILL.md") if p.is_file()):
        name = skill.parent.name
        rows.append("| %s | %s | [%s/SKILL.md](%s/SKILL.md) |" % (name, skill_description(vaultlib.read_text(skill)), name, name))
    table = ["| المهارة | الوصف | الملف |", "|---|---|---|"] + rows
    return "\n".join([
        "# Skills Index",
        "",
        "> %d skills exported from the owner's agent config (redacted). Regenerated by `tools/export_rules.py`." % len(rows),
        "",
        AUTO_START,
        *table,
        AUTO_END,
        "",
    ])


# --------------------------------------------------------------------------- CLI

def _print_report(target: str, rep: copy_sources.CopyReport) -> None:
    print("[%s] %s" % (target, rep.summary()))
    if rep.counts:
        print("  redactions by category: " + ", ".join("%s=%d" % kv for kv in sorted(rep.counts.items())))
    for name in rep.skipped_deny_read:
        print("  DENY_READ  " + name)
    for name in rep.skipped_deny_copy:
        print("  DENY_COPY  " + name)
    for title in rep.skipped_sensitive:
        print("  SKIPPED_SENSITIVE  " + title)
    for e in rep.errors:
        print("  ERROR  %s (%s)" % (e["src"], e["error"]))


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Export rules/workflows/skills/commands into the vault.")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--home", default="", help="source home directory (default: the user's home)")
    a = ap.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass
    home = Path(a.home).expanduser() if a.home else Path.home()
    reports = export_all(home, REPO, dry_run=a.dry_run, top_n=a.top)

    print("[export_rules] %s" % ("DRY-RUN" if a.dry_run else "WRITE"))
    for target, rep in reports.items():
        _print_report(target, rep)
    skills_n = sum(1 for c in reports["skills"].copied if c["dst"].endswith("/SKILL.md"))
    print("[export_rules] counts: skills(SKILL.md)=%d rules=%d workflows=%d commands=%d" % (
        skills_n, len(reports["rules"].copied), len(reports["workflows"].copied), len(reports["commands"].copied)))
    top = sorted((r for rep in reports.values() for r in rep.top_redacted), key=lambda r: (-r["redactions"], r["path"]))[:a.top]
    if top:
        print("| # | path | redactions |\n|---|---|---|")
        for i, row in enumerate(top, 1):
            print("| %d | %s | %d |" % (i, row["path"], row["redactions"]))
    errors = sum(len(r.errors) for r in reports.values())
    sensitive = sum(len(r.skipped_sensitive) for r in reports.values())
    entropy = sum(len(r.entropy_hits) for r in reports.values())
    print("[export_rules] totals: errors=%d skipped_sensitive=%d entropy_hits=%d" % (errors, sensitive, entropy))

    if not a.dry_run and not errors:
        vaultlib.write_text(REPO / "skills" / "INDEX.md", build_skills_index(REPO / "skills"))
        print("[export_rules] skills/INDEX.md regenerated")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
