"""Shared stdlib helpers for the vault tools (I/O, hashing, normalization, manifests).

All text I/O is UTF-8 without BOM and uses LF line endings. No local absolute
paths live here: the repo root is derived from this file's location.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import unicodedata
from pathlib import Path
from typing import Iterable, Iterator, Optional

MANIFEST_NAME = "manifest.json"

_WIN_RESERVED = {
    "CON", "PRN", "AUX", "NUL",
    *(f"COM{i}" for i in range(1, 10)),
    *(f"LPT{i}" for i in range(1, 10)),
}
_BAD_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')


def repo_root() -> Path:
    """Return the repository root (parent of the ``tools/`` package directory)."""
    return Path(__file__).resolve().parent.parent


def read_text(path) -> str:
    """Read a UTF-8 text file (BOM tolerated, stripped) and normalize line endings to LF."""
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def write_text(path, text: str) -> Path:
    """Write text as UTF-8 (no BOM) with LF endings, creating parent directories."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(normalized)
    return p


def sha256_file(path) -> str:
    """Hex SHA-256 of a file's bytes (streamed)."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text: str) -> str:
    """Hex SHA-256 of a string's UTF-8 encoding."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def nfc(text: str) -> str:
    """Unicode NFC normalization (stable hashing / dedupe for Arabic text)."""
    return unicodedata.normalize("NFC", text)


def utf8_len(text: str) -> int:
    """Byte length of the text when encoded as UTF-8 (size limits are in bytes)."""
    return len(text.encode("utf-8"))


def write_manifest(directory, data: dict) -> Path:
    """Write ``manifest.json`` (sorted keys, UTF-8, LF) inside *directory*."""
    p = Path(directory) / MANIFEST_NAME
    return write_text(p, json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n")


def read_manifest(directory) -> Optional[dict]:
    """Read ``manifest.json`` from *directory*; return None when absent."""
    p = Path(directory) / MANIFEST_NAME
    if not p.is_file():
        return None
    return json.loads(read_text(p))


def sanitize_filename(name: str, max_len: int = 120) -> str:
    """Make *name* safe for Windows/POSIX filesystems and cap its length.

    Replaces reserved characters with ``_``, strips trailing dots/spaces,
    guards reserved device names, and keeps the extension when truncating.
    """
    name = nfc(name or "")
    name = _BAD_CHARS.sub("_", name).strip().rstrip(". ")
    if not name:
        name = "_"
    stem, dot, ext = name.rpartition(".")
    if not dot:
        stem, ext = name, ""
    if stem.upper() in _WIN_RESERVED:
        stem = "_" + stem
    ext = ("." + ext) if ext and dot else ""
    if max_len and len(stem) + len(ext) > max_len:
        stem = stem[: max(1, max_len - len(ext))]
    return stem + ext


def iter_files(root, exts: Optional[Iterable[str]] = None) -> Iterator[Path]:
    """Yield files under *root* recursively (sorted), optionally filtered by extensions.

    *exts* entries are case-insensitive and may be given with or without a dot.
    """
    wanted = None
    if exts is not None:
        wanted = {("" if e.startswith(".") else ".") + e.lower() for e in exts}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        for fn in sorted(filenames):
            if wanted is not None and Path(fn).suffix.lower() not in wanted:
                continue
            yield Path(dirpath) / fn
