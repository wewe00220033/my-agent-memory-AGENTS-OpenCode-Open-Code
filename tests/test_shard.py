"""Unit tests for tools/shard.py (stdlib only; Arabic payloads are generated programmatically)."""
import json
import re
import tempfile
import unittest
from pathlib import Path

from tools import shard
from tools import vaultlib as vl

AR_WORDS = ["ذاكرة", "وكيل", "جلسة", "ملخص", "سجل", "فهرس", "تحقق", "تعقيم"]


def ar_sentence(i, words=12):
    return " ".join(AR_WORDS[(i + k) % len(AR_WORDS)] + str(i) for k in range(words))


def md_with_h2(sections, lines_per_section=20):
    out = ["# مستند تجريبي\n\n"]
    for s in range(sections):
        out.append("## قسم %d\n\n" % s)
        for i in range(lines_per_section):
            out.append(ar_sentence(s * 100 + i) + "\n")
        out.append("\n")
    return "".join(out)


def all_within(parts, max_bytes):
    return all(vl.utf8_len(p) <= max_bytes for p in parts)


class TestShardMarkdown(unittest.TestCase):
    def test_defaults_match_plan(self):
        self.assertEqual(shard.MD_MAX, 1 * 1024 * 1024)
        self.assertEqual(shard.JSON_MAX, 2 * 1024 * 1024)

    def test_small_text_is_single_part(self):
        text = md_with_h2(3)
        parts = shard.shard_markdown(text, 1 << 20)
        self.assertEqual(parts, [text])

    def test_splits_at_h2_boundaries_and_roundtrips(self):
        text = md_with_h2(30)
        max_bytes = 8000
        self.assertGreater(vl.utf8_len(text), max_bytes)
        parts = shard.shard_markdown(text, max_bytes)
        self.assertGreater(len(parts), 1)
        self.assertTrue(all_within(parts, max_bytes))
        self.assertEqual("".join(parts), text)
        for p in parts[1:]:
            self.assertTrue(p.startswith("## "), repr(p[:20]))

    def test_h3_fallback_inside_one_big_h2(self):
        body = ["## قسم كبير\n\n"]
        for s in range(30):
            body.append("### فرع %d\n\n" % s)
            for i in range(5):
                body.append(ar_sentence(s * 10 + i) + "\n")
            body.append("\n")
        text = "".join(body)
        parts = shard.shard_markdown(text, 5000)
        self.assertGreater(len(parts), 1)
        self.assertTrue(all_within(parts, 5000))
        self.assertEqual("".join(parts), text)
        self.assertTrue(parts[0].startswith("## "))
        for p in parts[1:]:
            self.assertTrue(p.startswith("### "), repr(p[:20]))

    def test_no_headings_splits_at_paragraphs(self):
        text = "\n\n".join(ar_sentence(i) for i in range(200)) + "\n"
        self.assertNotIn("## ", text)
        parts = shard.shard_markdown(text, 1000)
        self.assertGreater(len(parts), 1)
        self.assertTrue(all_within(parts, 1000))
        self.assertEqual("".join(parts), text)
        for p in parts[:-1]:
            self.assertTrue(p.endswith("\n\n"), repr(p[-10:]))

    def test_huge_single_line_split_on_utf8_boundaries(self):
        text = "عa" * 25000  # 3 bytes per pair -> boundaries fall inside characters unless backed off
        self.assertNotIn("\n", text)
        parts = shard.shard_markdown(text, 1000)
        self.assertGreater(len(parts), 1)
        raw = b""
        for k, p in enumerate(parts):
            enc = p.encode("utf-8")  # every part is valid text (no broken character)
            self.assertLessEqual(len(enc), 1000)
            if k < len(parts) - 1:  # all but the trailing remainder must be packed tightly
                self.assertGreaterEqual(len(enc), 997)
            raw += enc
        self.assertEqual(raw, text.encode("utf-8"))
        self.assertEqual("".join(parts), text)

    def test_size_is_measured_in_bytes_not_chars(self):
        text = "ع" * 600_000  # 600 K chars but 1.2 MB
        self.assertLess(len(text), shard.MD_MAX)
        parts = shard.shard_markdown(text, shard.MD_MAX)
        self.assertGreater(len(parts), 1)
        self.assertTrue(all_within(parts, shard.MD_MAX))
        self.assertEqual("".join(parts), text)

    def test_rejects_tiny_limit(self):
        with self.assertRaises(ValueError):
            shard.shard_markdown("abc", 2)


class TestShardJson(unittest.TestCase):
    def _dumps(self, o):
        return json.dumps(o, ensure_ascii=False)

    def test_small_object_is_single_part(self):
        obj = [{"a": 1}]
        self.assertEqual(shard.shard_json(obj, 1000), [obj])

    def test_list_of_1000_objects_valid_parts_and_roundtrip(self):
        items = [{"id": i, "نص": ar_sentence(i)} for i in range(1000)]
        max_bytes = 20_000
        parts = shard.shard_json(items, max_bytes)
        self.assertGreater(len(parts), 1)
        merged = []
        for p in parts:
            self.assertIsInstance(p, list)
            s = self._dumps(p)
            self.assertLessEqual(vl.utf8_len(s), max_bytes)
            self.assertEqual(json.loads(s), p)
            merged.extend(p)
        self.assertEqual(merged, items)

    def test_dict_top_level_keys_contiguous_and_roundtrip(self):
        obj = {"مفتاح%d" % i: {"v": i, "t": ar_sentence(i, 6)} for i in range(300)}
        max_bytes = 6000
        parts = shard.shard_json(obj, max_bytes)
        self.assertGreater(len(parts), 1)
        merged = {}
        keys = []
        for p in parts:
            self.assertIsInstance(p, dict)
            self.assertLessEqual(vl.utf8_len(self._dumps(p)), max_bytes)
            merged.update(p)
            keys.extend(p.keys())
        self.assertEqual(merged, obj)
        self.assertEqual(keys, list(obj.keys()))

    def test_oversize_item_isolated_with_warning(self):
        big = {"big": "ع" * 5000}
        items = [{"i": 1}, big, {"i": 3}]
        warnings = []
        parts = shard.shard_json(items, 2000, warnings)
        self.assertEqual(parts, [[{"i": 1}], [big], [{"i": 3}]])
        self.assertEqual(len(warnings), 1)
        with tempfile.TemporaryDirectory() as d:
            mp = shard.write_shards(Path(d) / "x", parts, ".json", max_bytes=2000, warnings=warnings)
            meta = json.loads(vl.read_text(mp))
            self.assertTrue(meta["oversize_warnings"])
            self.assertIn("x.part002.json", {w.get("file") for w in meta["oversize_warnings"]})


class TestWriteAndReadShards(unittest.TestCase):
    def test_single_part_has_no_part_suffix(self):
        with tempfile.TemporaryDirectory() as d:
            mp = shard.write_shards(Path(d) / "doc", ["نص صغير\n"], ".md", max_bytes=1000)
            self.assertEqual(mp.name, "doc.parts.json")
            self.assertTrue((Path(d) / "doc.md").is_file())
            self.assertEqual(sorted(p.name for p in Path(d).iterdir()), ["doc.md", "doc.parts.json"])
            self.assertEqual(json.loads(vl.read_text(mp))["count"], 1)
            self.assertEqual(shard.read_shards(mp), "نص صغير\n")

    def test_part_numbering_three_digits_sorted(self):
        parts = ["جزء %d\n" % i for i in range(5)]
        with tempfile.TemporaryDirectory() as d:
            mp = shard.write_shards(Path(d) / "x", parts, ".md", max_bytes=100)
            meta = json.loads(vl.read_text(mp))
            names = [e["file"] for e in meta["parts"]]
            self.assertEqual(names, ["x.part%03d.md" % i for i in range(1, 6)])
            for n in names:
                self.assertRegex(n, r"^x\.part\d{3}\.md$")
                self.assertTrue((Path(d) / n).is_file())

    def test_parts_json_keys_and_total_bytes(self):
        text = md_with_h2(12)
        parts = shard.shard_markdown(text, 3000)
        with tempfile.TemporaryDirectory() as d:
            mp = shard.write_shards(Path(d) / "doc", parts, ".md", max_bytes=3000)
            meta = json.loads(vl.read_text(mp))
            self.assertEqual(
                set(meta),
                {"source", "ext", "max_bytes", "count", "parts", "total_bytes", "oversize_warnings"},
            )
            self.assertEqual(meta["source"], "doc")
            self.assertEqual(meta["ext"], ".md")
            self.assertEqual(meta["max_bytes"], 3000)
            self.assertEqual(meta["count"], len(parts))
            self.assertEqual(meta["oversize_warnings"], [])
            self.assertEqual(meta["total_bytes"], sum(e["bytes"] for e in meta["parts"]))
            self.assertEqual(meta["total_bytes"], vl.utf8_len(text))
            for e in meta["parts"]:
                self.assertEqual(set(e), {"file", "bytes", "sha256"})
                fp = Path(d) / e["file"]
                self.assertEqual(fp.stat().st_size, e["bytes"])
                self.assertEqual(vl.sha256_file(fp), e["sha256"])
                raw = fp.read_bytes()
                self.assertFalse(raw.startswith(b"\xef\xbb\xbf"))
                self.assertNotIn(b"\r", raw)

    def test_read_shards_roundtrip_md_and_json(self):
        text = md_with_h2(12)
        items = [{"id": i, "نص": ar_sentence(i)} for i in range(400)]
        obj = {"k%d" % i: ar_sentence(i, 5) for i in range(200)}
        with tempfile.TemporaryDirectory() as d:
            mp_md = shard.write_shards(Path(d) / "m", shard.shard_markdown(text, 3000), ".md", max_bytes=3000)
            mp_li = shard.write_shards(Path(d) / "l", shard.shard_json(items, 8000), ".json", max_bytes=8000)
            mp_ob = shard.write_shards(Path(d) / "o", shard.shard_json(obj, 3000), ".json", max_bytes=3000)
            self.assertGreater(json.loads(vl.read_text(mp_li))["count"], 1)
            self.assertEqual(shard.read_shards(mp_md), text)
            self.assertEqual(shard.read_shards(mp_li), items)
            self.assertEqual(shard.read_shards(mp_ob), obj)

    def test_read_shards_detects_tampering(self):
        text = md_with_h2(12)
        with tempfile.TemporaryDirectory() as d:
            mp = shard.write_shards(Path(d) / "m", shard.shard_markdown(text, 3000), ".md", max_bytes=3000)
            victim = Path(d) / "m.part002.md"
            self.assertTrue(victim.is_file())
            with open(victim, "a", encoding="utf-8", newline="\n") as f:
                f.write("x")
            with self.assertRaises(shard.ShardIntegrityError):
                shard.read_shards(mp)


class TestCli(unittest.TestCase):
    def test_cli_markdown_and_json(self):
        text = md_with_h2(12)
        items = [{"id": i, "نص": ar_sentence(i)} for i in range(300)]
        with tempfile.TemporaryDirectory() as d:
            src_md = vl.write_text(Path(d) / "in" / "notes.md", text)
            src_js = vl.write_text(Path(d) / "in" / "ledger.json", json.dumps(items, ensure_ascii=False))
            out = Path(d) / "out"
            self.assertEqual(shard.main([str(src_md), "--max-bytes", "3000", "--out", str(out)]), 0)
            self.assertEqual(shard.main([str(src_js), "--max-bytes", "8000", "--out", str(out)]), 0)
            mp_md = out / "notes.parts.json"
            mp_js = out / "ledger.parts.json"
            self.assertTrue(mp_md.is_file() and mp_js.is_file())
            self.assertGreater(json.loads(vl.read_text(mp_md))["count"], 1)
            self.assertEqual(shard.read_shards(mp_md), text)
            self.assertEqual(shard.read_shards(mp_js), items)
            # sources untouched
            self.assertEqual(vl.read_text(src_md), text)


if __name__ == "__main__":
    unittest.main()
