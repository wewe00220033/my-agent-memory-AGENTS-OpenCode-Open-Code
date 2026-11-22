"""Split large Markdown/JSON exports into size-bounded parts (bytes, UTF-8) and reassemble them.

Markdown is cut at ``\n## `` boundaries first, then ``\n### ``, then blank-line
paragraphs, then single lines, and as a last resort at valid UTF-8 character
boundaries (an Arabic character is never broken). Concatenating the parts
reproduces the original text byte for byte.

JSON lists are cut between elements and JSON objects between contiguous
top-level keys; every part is itself valid JSON. A single element larger than
the limit is emitted alone in its own part and recorded as a warning.

``write_shards`` emits ``<base>.partNNN.<ext>`` files plus ``<base>.parts.json``
(sha256 + byte size per part); ``read_shards`` verifies and reassembles.

stdlib only. Limits come from PLAN.md §4: ``.md`` <= 1 MB, ``.json`` <= 2 MB.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, List, Optional, Sequence, Tuple

if __package__ in (None, ""):  # executed as a script: make ``tools`` importable
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import vaultlib  # noqa: E402

MD_MAX = 1 * 1024 * 1024
JSON_MAX = 2 * 1024 * 1024

# (delimiter, number of leading delimiter chars that stay with the PREVIOUS piece)
_MD_LEVELS: Tuple[Tuple[str, int], ...] = (
    ("\n## ", 1),
    ("\n### ", 1),
    ("\n\n", 2),
    ("\n", 1),
)


class ShardError(Exception):
    """Base error for shard operations."""


class ShardIntegrityError(ShardError):
    """A part is missing, altered (sha256 mismatch) or parts.json is inconsistent."""


# --------------------------------------------------------------------------- markdown

def _split_units(text: str, delim: str, keep: int) -> List[str]:
    """Cut *text* at every *delim*; the first *keep* chars of the delimiter stay with the previous piece."""
    units: List[str] = []
    start = 0
    pos = text.find(delim)
    while pos != -1:
        cut = pos + keep
        if cut > start:
            units.append(text[start:cut])
            start = cut
        pos = text.find(delim, max(cut, pos + 1))
    units.append(text[start:])
    return [u for u in units if u]


def _split_utf8(text: str, max_bytes: int) -> List[str]:
    """Split at valid UTF-8 character boundaries so every chunk encodes to <= *max_bytes*."""
    data = text.encode("utf-8")
    out: List[str] = []
    i = 0
    n = len(data)
    while i < n:
        j = min(i + max_bytes, n)
        while j < n and j > i and (data[j] & 0xC0) == 0x80:  # back off from a continuation byte
            j -= 1
        if j == i:  # cannot happen for max_bytes >= 4, kept as a hard guard
            raise ValueError("max_bytes too small to hold one UTF-8 character")
        out.append(data[i:j].decode("utf-8"))
        i = j
    return out


def _split_text(text: str, max_bytes: int, level: int) -> List[str]:
    if vaultlib.utf8_len(text) <= max_bytes:
        return [text]
    if level >= len(_MD_LEVELS):
        return _split_utf8(text, max_bytes)
    delim, keep = _MD_LEVELS[level]
    units = _split_units(text, delim, keep)
    if len(units) <= 1:
        return _split_text(text, max_bytes, level + 1)
    out: List[str] = []
    buf: List[str] = []
    buf_len = 0
    for unit in units:
        ulen = vaultlib.utf8_len(unit)
        if ulen > max_bytes:
            if buf:
                out.append("".join(buf))
                buf, buf_len = [], 0
            out.extend(_split_text(unit, max_bytes, level + 1))
            continue
        if buf and buf_len + ulen > max_bytes:
            out.append("".join(buf))
            buf, buf_len = [], 0
        buf.append(unit)
        buf_len += ulen
    if buf:
        out.append("".join(buf))
    return out


def shard_markdown(text: str, max_bytes: int = MD_MAX) -> List[str]:
    """Split *text* into parts whose UTF-8 encoding is <= *max_bytes*; ``"".join(parts) == text``."""
    if max_bytes < 4:
        raise ValueError("max_bytes must be >= 4 (one UTF-8 character)")
    if not isinstance(text, str):
        raise TypeError("shard_markdown expects str")
    return _split_text(text, max_bytes, 0)


# --------------------------------------------------------------------------- json

def _dumps(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False)


def shard_json(obj: Any, max_bytes: int = JSON_MAX, warnings: Optional[list] = None) -> List[Any]:
    """Split a list (between elements) or a dict (between contiguous top-level keys).

    Each part serializes with ``json.dumps(ensure_ascii=False)`` to <= *max_bytes*.
    An element that alone exceeds the limit is emitted in its own part and a
    warning dict is appended to *warnings* (if given); ``write_shards`` records
    those in ``parts.json`` under ``oversize_warnings``.
    """
    if max_bytes < 2:
        raise ValueError("max_bytes must be >= 2")
    if isinstance(obj, list):
        items: List[Tuple[Any, Any]] = [(i, v) for i, v in enumerate(obj)]
        sizes = [vaultlib.utf8_len(_dumps(v)) for _, v in items]

        def build(chunk):
            return [v for _, v in chunk]
    elif isinstance(obj, dict):
        items = list(obj.items())
        sizes = [vaultlib.utf8_len(_dumps(k)) + 2 + vaultlib.utf8_len(_dumps(v)) for k, v in items]

        def build(chunk):
            return dict(chunk)
    else:
        raise TypeError("shard_json expects a list or a dict at top level")

    if 2 + sum(sizes) + 2 * max(0, len(items) - 1) <= max_bytes:
        return [obj]

    parts: List[Any] = []
    buf: List[Tuple[Any, Any]] = []
    buf_len = 0  # bytes of the serialized elements excluding brackets and separators

    def flush():
        nonlocal buf, buf_len
        if buf:
            parts.append(build(buf))
            buf, buf_len = [], 0

    for (key, value), size in zip(items, sizes):
        if 2 + size > max_bytes:
            flush()
            parts.append(build([(key, value)]))
            warn = {
                "part": len(parts),
                "bytes": 2 + size,
                "max_bytes": max_bytes,
                ("key" if isinstance(obj, dict) else "index"): key,
            }
            if warnings is not None:
                warnings.append(warn)
            continue
        if buf and 2 + buf_len + 2 * len(buf) + size > max_bytes:
            flush()
        buf.append((key, value))
        buf_len += size
    flush()

    for p in parts:  # defensive: the arithmetic above must match json.dumps exactly
        if vaultlib.utf8_len(_dumps(p)) > max_bytes and len(p) > 1:
            raise ShardError("internal size accounting error")
    return parts


# --------------------------------------------------------------------------- files

def _part_name(name: str, index: int, count: int, ext: str) -> str:
    if count == 1:
        return name + ext
    return "%s.part%03d%s" % (name, index, ext)


def write_shards(path_base, parts: Sequence[Any], ext: str, max_bytes: Optional[int] = None,
                 warnings: Optional[Sequence[dict]] = None) -> Path:
    """Write ``<base>.partNNN<ext>`` (or ``<base><ext>`` for a single part) and ``<base>.parts.json``.

    Returns the path of ``parts.json``. *ext* is ``".json"`` (parts are list/dict)
    or a text extension such as ``".md"`` (parts are str, LF only).
    """
    if not ext.startswith("."):
        raise ValueError("ext must start with a dot, e.g. '.md' or '.json'")
    if not parts:
        raise ValueError("no parts to write")
    base = Path(path_base)
    name = base.name
    is_json = ext == ".json"
    if max_bytes is None:
        max_bytes = JSON_MAX if is_json else MD_MAX
    count = len(parts)
    entries: List[dict] = []
    total = 0
    names: List[str] = []
    for i, part in enumerate(parts, 1):
        if is_json:
            if not isinstance(part, (list, dict)):
                raise TypeError("json parts must be lists or dicts")
            text = _dumps(part)
        else:
            if not isinstance(part, str):
                raise TypeError("text parts must be str")
            if "\r" in part:
                raise ValueError("text parts must be LF-normalized (use vaultlib.read_text)")
            text = part
        fname = _part_name(name, i, count, ext)
        vaultlib.write_text(base.with_name(fname), text)
        size = vaultlib.utf8_len(text)
        total += size
        names.append(fname)
        entries.append({"file": fname, "bytes": size, "sha256": vaultlib.sha256_text(text)})
    oversize: List[dict] = []
    for w in warnings or ():
        w2 = dict(w)
        idx = w2.get("part")
        if isinstance(idx, int) and 1 <= idx <= count:
            w2["file"] = names[idx - 1]
        oversize.append(w2)
    meta = {
        "source": name,
        "ext": ext,
        "max_bytes": max_bytes,
        "count": count,
        "parts": entries,
        "total_bytes": total,
        "oversize_warnings": oversize,
    }
    return vaultlib.write_text(base.with_name(name + ".parts.json"),
                               json.dumps(meta, indent=2, ensure_ascii=False) + "\n")


def read_shards(parts_json) -> Any:
    """Reassemble from ``parts.json``; verifies sha256 of every part (raises ShardIntegrityError)."""
    mp = Path(parts_json)
    try:
        meta = json.loads(vaultlib.read_text(mp))
    except (OSError, ValueError) as e:
        raise ShardIntegrityError("cannot read %s: %s" % (mp.name, e)) from e
    entries = meta.get("parts")
    if not isinstance(entries, list) or not entries:
        raise ShardIntegrityError("%s: missing or empty 'parts'" % mp.name)
    if meta.get("count") != len(entries):
        raise ShardIntegrityError("%s: count %r != %d parts" % (mp.name, meta.get("count"), len(entries)))
    is_json = meta.get("ext") == ".json"
    chunks: List[str] = []
    for e in entries:
        fp = mp.parent / e["file"]
        if not fp.is_file():
            raise ShardIntegrityError("missing part %s" % e["file"])
        if vaultlib.sha256_file(fp) != e.get("sha256"):
            raise ShardIntegrityError("sha256 mismatch in %s" % e["file"])
        chunks.append(vaultlib.read_text(fp))
    if not is_json:
        return "".join(chunks)
    objs = [json.loads(c) for c in chunks]
    if all(isinstance(o, list) for o in objs):
        merged: list = []
        for o in objs:
            merged.extend(o)
        return merged
    if all(isinstance(o, dict) for o in objs):
        out: dict = {}
        for o in objs:
            out.update(o)
        return out
    raise ShardIntegrityError("%s: mixed part types" % mp.name)


# --------------------------------------------------------------------------- CLI

def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Split a Markdown/JSON file into size-bounded parts.")
    ap.add_argument("file")
    ap.add_argument("--max-bytes", type=int, default=None,
                    help="limit per part in bytes (default: %d for .json, %d otherwise)" % (JSON_MAX, MD_MAX))
    ap.add_argument("--out", default=None, help="output directory (default: <file dir>/shards)")
    args = ap.parse_args(argv)
    src = Path(args.file)
    if not src.is_file():
        print("not a file: %s" % src, file=sys.stderr)
        return 1
    ext = src.suffix.lower() or ".md"
    is_json = ext == ".json"
    max_bytes = args.max_bytes or (JSON_MAX if is_json else MD_MAX)
    out_dir = Path(args.out) if args.out else src.parent / "shards"
    warnings: List[dict] = []
    try:
        text = vaultlib.read_text(src)
        if is_json:
            parts = shard_json(json.loads(text), max_bytes, warnings)
        else:
            parts = shard_markdown(text, max_bytes)
        mp = write_shards(out_dir / src.stem, parts, ext, max_bytes=max_bytes, warnings=warnings)
    except (OSError, ValueError, TypeError, ShardError) as e:
        print("error: %s" % e, file=sys.stderr)
        return 1
    print("%s -> %d part(s), %d oversize warning(s): %s" % (src.name, len(parts), len(warnings), mp))
    return 0


if __name__ == "__main__":
    sys.exit(main())
