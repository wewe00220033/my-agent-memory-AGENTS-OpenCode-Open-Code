"""Every relative Markdown link in AGENTS.md / README.md / */INDEX.md must resolve (PLAN 7.4).

External links (http/https/mailto), anchors (#...) and absolute URLs are ignored; links inside
the AUTO-INDEX markers are checked like any other.
"""
import re
import tempfile
import unittest
from pathlib import Path
from urllib.parse import unquote

from tools import vaultlib

REPO = vaultlib.repo_root()
_LINK = re.compile(r'(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
_INLINE_CODE = re.compile(r"`[^`\n]*`")
_FENCE = re.compile(r"^```.*?^```", re.M | re.S)
_SKIP_PREFIX = ("http://", "https://", "mailto:", "#", "//", "ftp://")


def relative_links(text):
    text = _FENCE.sub("", text)
    text = _INLINE_CODE.sub("", text)
    out = []
    for m in _LINK.finditer(text):
        target = m.group(1).strip("<>")
        if target.lower().startswith(_SKIP_PREFIX) or re.match(r"^[a-z][a-z0-9+.\-]*:", target, re.I):
            continue
        out.append(unquote(target.split("#", 1)[0]))
    return [t for t in out if t]


def index_documents(root):
    docs = [root / "AGENTS.md", root / "README.md"]
    docs += sorted(p for p in root.rglob("INDEX.md")
                   if not any(part in {".git", "_local", "__pycache__"} for part in p.relative_to(root).parts))
    return [p for p in docs if p.is_file()]


def broken_links(doc, root):
    bad = []
    for target in relative_links(vaultlib.read_text(doc)):
        base = root if target.startswith("/") else doc.parent
        if not (base / target.lstrip("/")).exists():
            bad.append(target)
    return bad


class TestIndexLinks(unittest.TestCase):
    def test_repo_index_documents_have_valid_links(self):
        docs = index_documents(REPO)
        self.assertTrue(docs, "at least README.md must exist")
        broken = {d.relative_to(REPO).as_posix(): broken_links(d, REPO) for d in docs}
        self.assertEqual({k: v for k, v in broken.items() if v}, {})

    def test_link_extraction_skips_external_and_anchors(self):
        text = "[a](https://example.test/x) [b](mailto:x) [c](#top) [d](docs/a.md#sec) ![img](pic.png) `[e](code/only.md)`"
        self.assertEqual(relative_links(text), ["docs/a.md"])

    def test_links_inside_auto_index_block_are_checked(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "memory").mkdir()
            vaultlib.write_text(root / "memory" / "INDEX.md",
                                "# idx\n<!-- AUTO-INDEX:START -->\n| [ok](present.md) | [missing](absent.md) |\n<!-- AUTO-INDEX:END -->\n")
            vaultlib.write_text(root / "memory" / "present.md", "x\n")
            self.assertEqual(broken_links(root / "memory" / "INDEX.md", root), ["absent.md"])

    def test_document_without_links_passes(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            vaultlib.write_text(root / "README.md", "# no links here\n\nplain text\n")
            self.assertEqual(broken_links(root / "README.md", root), [])


if __name__ == "__main__":
    unittest.main()
