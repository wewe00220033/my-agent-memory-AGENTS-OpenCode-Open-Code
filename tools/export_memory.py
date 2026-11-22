"""S2: export one project's agent memory into ``memory/<project>/`` (PLAN S2 / T8-T11).

Every part is run through ``tools/copy_sources`` (denylist -> redact -> residual check -> dedupe ->
idempotent write); nothing here re-implements that pipeline.  Per project a table of PARTS says
what to take:
  ("tree", <src subdir>, <dst subdir>, include_exts, exclude_globs)  -> copy_sources.copy_tree
  ("files", <src subdir or "">, <dst subdir>, (names...))             -> copy_sources.copy_file each
One merged manifest per project is written OUTSIDE the published tree:
  _local/manifests/S2/<project>.manifest.json   (also in --dry-run; memory/ is never touched then)
Optional owner review file (never published, hashes only — no values):
  _local/manifests/S2/<project>.review.json  -> its ``redact_hashes`` are passed to every part as
  ``redact_value_hashes`` (hash-pinned HIGH_ENTROPY redaction in copy_sources).

CLI: python tools/export_memory.py --project gateway-service [--src DIR] [--dry-run] [--top 20]
Exit 0 on success, 1 when any part reports errors.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Sequence

if __package__ in (None, ""):  # executed as a script: make ``tools`` importable
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import copy_sources, redact, vaultlib  # noqa: E402

REPO = vaultlib.repo_root()
MANIFEST_DIR = REPO / "_local" / "manifests" / "S2"
MD_ONLY = (".md",)
ROOT_FILES = ("AGENTS.md", "GEMINI.md", "HANDOFF.md", "PROGRESS.md", "README.md")

# project -> (default source root, parts). Default roots are overridable with --src.
PROJECTS: Dict[str, dict] = {
    "gateway-service": {
        "src": "D:/SMS/.hRhR_gateway-service",
        "parts": (
            ("tree", "Root", "root", MD_ONLY,
             ("CONVERSATIONS_*", "ALL_CONVERSATIONS_LEDGER/*", "*LEDGER*", "*FORENSIC*")),
            ("tree", ".agents/memory", "agents-memory", MD_ONLY, ()),
            ("files", "", "", ROOT_FILES),
        ),
    },
    "bolla-agentic-os": {
        "src": "D:/SMS/Bolla-Agentic-OS-EGM-SRE",
        "parts": (
            ("tree", "Root", "root", MD_ONLY,
             ("CONVERSATIONS_*", "ALL_CONVERSATIONS_LEDGER/*", "*LEDGER*", "*FORENSIC*")),
            ("tree", ".agents/memory", "agents-memory", MD_ONLY, ()),
            ("files", "", "", ROOT_FILES),
        ),
    },
    # T10: ONLY .agents/memory + two named root files — the walk starts at src/.agents/memory, so project
    # folders / .git / source code under D:/SMS are out of scope by design (never walked, not just excluded).
    "sms-root": {
        "src": "D:/SMS",
        "parts": (
            ("tree", ".agents/memory", "agents-memory", MD_ONLY,
             ("CONVERSATIONS_*", "ALL_CONVERSATIONS_LEDGER/*", "*LEDGER*", "*FORENSIC*")),
            ("files", "", "", ("handoff.md", "GEMINI_ARCHIVE_2026-09-02.md")),
        ),
    },
    # scratch: ONLY .agents/memory; this repository itself lives under scratch/ and is never walked.
    "scratch": {
        "src": "C:/Users/USER/.gemini/antigravity/scratch",
        "parts": (
            ("tree", ".agents/memory", "agents-memory", MD_ONLY,
             ("CONVERSATIONS_*", "*LEDGER*", "*FORENSIC*")),
        ),
    },
}


# --------------------------------------------------------------------------- helpers

def _merge(into: copy_sources.CopyReport, other: copy_sources.CopyReport) -> None:
    for name in ("copied", "skipped_deny_read", "skipped_deny_copy", "skipped_sensitive", "skipped_dedupe",
                 "skipped_size", "skipped_binary", "entropy_hits", "top_redacted", "errors"):
        getattr(into, name).extend(getattr(other, name))
    into.counts.update(other.counts)


def _would_copy_non_md(src_root: Path, exclude_globs: Sequence[str]) -> List[str]:
    """Names (redacted) of files that are neither excluded nor denied but are NOT .md — never opened.
    Informational only, so the owner can see what the extension filter kept out."""
    out: List[str] = []
    for rel in copy_sources._iter_sources(src_root):
        if copy_sources._excluded(rel, exclude_globs):
            continue
        if redact.is_denied_path(rel, "READ") or redact.is_denied_path(rel, "COPY"):
            continue
        if Path(rel).suffix.lower() not in MD_ONLY:
            out.append(copy_sources._safe(rel))
    return out


def load_review_hashes(project: str, manifest_dir: Path) -> set:
    """``redact_hashes`` from ``<manifest_dir>/<project>.review.json`` (empty set when absent)."""
    p = manifest_dir / (project + ".review.json")
    if not p.is_file():
        return set()
    data = json.loads(vaultlib.read_text(p))
    return {str(h).lower() for h in data.get("redact_hashes", []) if h}


# --------------------------------------------------------------------------- export

def export_project(project: str, src_root: Path, *, dry_run: bool, top_n: int,
                   manifest_dir: Optional[Path] = None) -> dict:
    spec = PROJECTS[project]
    dst_root = REPO / "memory" / project
    mdir = (manifest_dir or MANIFEST_DIR) / project
    hashes = load_review_hashes(project, manifest_dir or MANIFEST_DIR)
    merged = copy_sources.CopyReport()
    parts: Dict[str, dict] = {}
    info: Dict[str, object] = {"would_copy_non_md": {}, "missing_root_files": [],
                               "review_hashes": len(hashes)}

    for kind, src_rel, dst_rel, *rest in spec["parts"]:
        src = src_root / src_rel if src_rel else src_root
        dst = dst_root / dst_rel if dst_rel else dst_root
        rep = copy_sources.CopyReport()
        label = (src_rel or ".") + " -> memory/%s/%s" % (project, dst_rel)
        if kind == "tree":
            exts, excludes = rest
            if not src.is_dir():
                rep.errors.append({"src": src_rel, "error": "FileNotFoundError: source directory missing"})
            else:
                rep = copy_sources.copy_tree(src, dst, include_exts=exts, exclude_globs=excludes, dry_run=dry_run,
                                             top_n=top_n, manifest_dir=mdir / (dst_rel or "root-files"),
                                             redact_value_hashes=hashes)
                info["would_copy_non_md"][src_rel] = _would_copy_non_md(src, excludes)  # type: ignore[index]
        else:  # files
            (names,) = rest
            for name in names:
                if not (src / name).is_file():
                    info["missing_root_files"].append(name)  # type: ignore[union-attr]
                    continue
                copy_sources.copy_file(src / name, dst, name, report=rep, dry_run=dry_run,
                                       redact_value_hashes=hashes)
        parts[label] = copy_sources.build_manifest(rep)
        if dst_rel:  # merged manifest keys are relative to memory/<project>/ (no collisions across parts)
            for c in rep.copied:
                c["dst"] = dst_rel + "/" + c["dst"]
        _merge(merged, rep)

    merged.top_redacted.sort(key=lambda r: (-r["redactions"], r["path"]))
    del merged.top_redacted[top_n:]
    manifest = copy_sources.build_manifest(merged)
    manifest.update({"tool": "export_memory", "project": project, "dry_run": dry_run,
                     "src": src_root.name, "parts": parts, "info": info})
    vaultlib.write_text(mdir.parent / (project + ".manifest.json"),
                        json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    return manifest


def print_summary(m: dict, top_n: int) -> None:
    tag = "DRY-RUN " if m["dry_run"] else ""
    print("[export_memory] %sproject=%s" % (tag, m["project"]))
    for label, part in m["parts"].items():
        s = part["summary"]
        print("  %-40s copied=%d deny_read=%d deny_copy=%d sensitive=%d dedupe=%d size=%d binary=%d "
              "redactions=%d entropy_hits=%d errors=%d" % (
                  label, s["copied"], s["skipped_deny_read"], s["skipped_deny_copy"], s["skipped_sensitive"],
                  s["skipped_dedupe"], s["skipped_size"], s["skipped_binary"], s["redactions"],
                  s["entropy_hits"], s["errors"]))
    s = m["summary"]
    print("[export_memory] TOTAL copied=%d deny_read=%d deny_copy=%d sensitive=%d dedupe=%d size=%d binary=%d "
          "redactions=%d entropy_hits=%d errors=%d" % (
              s["copied"], s["skipped_deny_read"], s["skipped_deny_copy"], s["skipped_sensitive"],
              s["skipped_dedupe"], s["skipped_size"], s["skipped_binary"], s["redactions"], s["entropy_hits"],
              s["errors"]))
    if m["redaction_counts"]:
        print("[export_memory] redactions by category: " +
              ", ".join("%s=%d" % kv for kv in m["redaction_counts"].items()))
    if m["top_redacted"]:
        print("| # | path | redactions |\n|---|---|---|")
        for i, row in enumerate(m["top_redacted"][:top_n], 1):
            print("| %d | %s | %d |" % (i, row["path"], row["redactions"]))
    for layer in ("DENY_READ", "DENY_COPY"):
        for name in m["rejected_by_name"][layer]:
            print("%-10s %s" % (layer, name))
    for title in m["skipped_sensitive"]:
        print("SKIPPED_SENSITIVE  " + title)
    for d in m["skipped_dedupe"]:
        print("DEDUPE  %s (kept %s)" % (d["src"], d["kept"]))
    print("[export_memory] review_hashes=%d HIGH_ENTROPY applied=%d" % (
        m["info"].get("review_hashes", 0), m["redaction_counts"].get("HIGH_ENTROPY", 0)))
    hits = sorted(m["entropy_hits"], key=lambda h: (-h["entropy"], -h["length"]))
    print("[export_memory] entropy_hits=%d (review only, not redacted)" % len(hits))
    for h in hits[:5]:
        print("  ENTROPY len=%d H=%.2f ctx=%s path=%s" % (h["length"], h["entropy"], h["context_hint"], h["path"]))
    for src_rel, names in m["info"]["would_copy_non_md"].items():
        print("[export_memory] non-.md files kept out by the extension filter under %s: %d" % (src_rel, len(names)))
        for n in names:
            print("  NON_MD  " + n)
    for n in m["info"]["missing_root_files"]:
        print("MISSING_ROOT_FILE  " + n)
    for e in m["errors"]:
        print("ERROR  %s (%s)" % (e["src"], e["error"]))


# --------------------------------------------------------------------------- CLI

def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Export one project's agent memory into memory/<project>/.")
    ap.add_argument("--project", required=True, choices=sorted(PROJECTS))
    ap.add_argument("--src", default="", help="source root (default: the project's configured root)")
    ap.add_argument("--dry-run", action="store_true", help="report + _local manifest only; memory/ untouched")
    ap.add_argument("--top", type=int, default=20)
    a = ap.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass
    src_root = Path(a.src or PROJECTS[a.project]["src"])
    if not src_root.is_dir():
        print("[export_memory] ERROR: source root is not a directory")
        return 1
    m = export_project(a.project, src_root, dry_run=a.dry_run, top_n=a.top)
    print_summary(m, a.top)
    return 0 if not m["errors"] else 1


if __name__ == "__main__":
    sys.exit(main())
