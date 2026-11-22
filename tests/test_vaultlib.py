"""Unit tests for tools/vaultlib.py (stdlib only)."""
import os
import tempfile
import unittest
from pathlib import Path

from tools import vaultlib as vl


class TestVaultlib(unittest.TestCase):
    def test_write_read_roundtrip_utf8_lf_no_bom(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "sub" / "a.md"
            text = "سطر أول\r\nسطر ثانٍ\rثالث\n"
            vl.write_text(p, text)
            raw = p.read_bytes()
            self.assertFalse(raw.startswith(b"\xef\xbb\xbf"))
            self.assertNotIn(b"\r", raw)
            self.assertEqual(vl.read_text(p), "سطر أول\nسطر ثانٍ\nثالث\n")

    def test_read_text_strips_bom_and_crlf(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "bom.txt"
            p.write_bytes(b"\xef\xbb\xbfa\r\nb\n")
            self.assertEqual(vl.read_text(p), "a\nb\n")

    def test_sha256_text_is_stable(self):
        self.assertEqual(
            vl.sha256_text("abc"),
            "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
        )
        self.assertEqual(vl.sha256_text(""), vl.sha256_text(""))

    def test_sha256_file_matches_text(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "f.txt"
            p.write_bytes(b"abc")
            self.assertEqual(vl.sha256_file(p), vl.sha256_text("abc"))

    def test_nfc_normalizes_decomposed_form(self):
        decomposed = "e\u0301"  # e + combining acute
        self.assertEqual(vl.nfc(decomposed), "\u00e9")
        self.assertEqual(vl.nfc("سلام"), "سلام")

    def test_utf8_len_arabic_is_two_bytes_per_char(self):
        self.assertEqual(vl.utf8_len("سلام"), 8)
        self.assertEqual(vl.utf8_len("abc"), 3)
        self.assertEqual(vl.utf8_len(""), 0)

    def test_sanitize_filename_windows_chars_and_reserved(self):
        self.assertEqual(vl.sanitize_filename('a<b>c:"d/e\\f|g?h*i.md'), "a_b_c__d_e_f_g_h_i.md")
        self.assertEqual(vl.sanitize_filename("CON.txt"), "_CON.txt")
        self.assertEqual(vl.sanitize_filename("trailing. "), "trailing")
        self.assertEqual(vl.sanitize_filename(""), "_")
        long = "x" * 300 + ".md"
        out = vl.sanitize_filename(long, max_len=50)
        self.assertEqual(len(out), 50)
        self.assertTrue(out.endswith(".md"))

    def test_repo_root_ends_with_repo_name_and_contains_tools(self):
        root = vl.repo_root()
        self.assertEqual(root.name, "my-agent-memory-AGENTS-OpenCode-Open-Code")
        self.assertTrue((root / "tools" / "vaultlib.py").is_file())

    def test_manifest_roundtrip_sorted_keys(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertIsNone(vl.read_manifest(d))
            vl.write_manifest(d, {"b": 2, "a": {"z": 1, "y": "نص"}})
            text = vl.read_text(Path(d) / vl.MANIFEST_NAME)
            self.assertLess(text.index('"a"'), text.index('"b"'))
            self.assertEqual(vl.read_manifest(d), {"a": {"y": "نص", "z": 1}, "b": 2})

    def test_iter_files_filters_and_sorts(self):
        with tempfile.TemporaryDirectory() as d:
            for name in ("b.md", "a.MD", "c.txt", os.path.join("sub", "d.md")):
                p = Path(d) / name
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text("x", encoding="utf-8")
            got = [p.relative_to(d).as_posix() for p in vl.iter_files(d, exts=["md"])]
            self.assertEqual(got, ["a.MD", "b.md", "sub/d.md"])
            self.assertEqual(len(list(vl.iter_files(d))), 4)


if __name__ == "__main__":
    unittest.main()
