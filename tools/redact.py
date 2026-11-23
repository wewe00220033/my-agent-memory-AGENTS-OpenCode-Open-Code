"""Redaction engine for the Portable AI Memory Vault (stdlib only).

Pipeline of ``redact_text``:
  NFC -> protect allowlist -> regex categories in CATEGORY_ORDER -> ENCODED (base64 >= 200
  chars decoded and re-scanned) -> HIGH_ENTROPY (record only, never redacted) -> restore
  allowlist -> second pass (new matches counted under SECOND_PASS) -> unresolved PEM check.

Every redaction is replaced by ``[REDACTED:<CATEGORY>]`` except home-directory paths which
become ``~``.  ``redact_file`` refuses to write anything that is not fully clean.

CLI (dry-run only, nothing is written except the counters report):
  python tools/redact.py --dry-run <paths...> --report <out.md> [--max-files N]
      [--glob "*.md"] [--recursive] [--label NAME] [--append]
      [--sqlite "db|table|col1,col2[|group_col]"] [--max-rows N] [--temp-dir DIR]
"""
from __future__ import annotations

import argparse
import base64
import binascii
import fnmatch
import json
import math
import os
import re
import shutil
import sqlite3
import sys
import tempfile
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Tuple

if __package__ in (None, ""):  # executed as a script: make ``tools`` importable
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import vaultlib  # noqa: E402

TOOLS_DIR = Path(__file__).resolve().parent
PATTERNS_FILE = TOOLS_DIR / "patterns.json"
DENYLIST_FILE = TOOLS_DIR / "denylist.json"

CATEGORY_ORDER: Tuple[str, ...] = (
    "PRIVATE_KEY", "URL_WITH_CREDS", "URL_TOKEN", "OAUTH_JWT", "GITHUB_TOKEN", "WEBHOOK", "API_KEY",
    "KV_SECRET", "EMAIL", "PHONE", "PII", "PATH",
)
MARKER_PREFIX = "[REDACTED:"
ENTROPY_MIN_LEN = 32
ENTROPY_THRESHOLD = 4.0
ENCODED_MIN_LEN = 200
LAYERS = ("READ", "COPY", "ANY")

_FLAG_MAP = {"I": re.I, "M": re.M, "S": re.S, "X": re.X, "A": re.A}
_SECRET_WORDS = re.compile(r"(?i)(?:key|secret|token|pass|auth|cred)")
_PHONE_CTX = re.compile(
    r"(?i)(?:time|(?<![a-z])ts(?![a-z])|(?<![a-z])id(?![a-z])|_id(?![a-z])|created|epoch"
    r"|_at(?![a-z])|version|(?<![a-z])seq(?![a-z])|(?<![a-z])port(?![a-z]))"
)
_ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}(?:[T ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:?\d{2})?)?")
_HEX40 = re.compile(r"[0-9a-fA-F]{40}")
_HEX64 = re.compile(r"[0-9a-fA-F]{64}")
_HEX_CHAR = re.compile(r"[0-9a-fA-F]")
_UUID = re.compile(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}")
_TOKEN = re.compile(r"[A-Za-z0-9+=_\-]{%d,}" % ENTROPY_MIN_LEN)
_B64_STD = re.compile(r"(?<![A-Za-z0-9+/=])[A-Za-z0-9+/]{%d,}={0,2}(?![A-Za-z0-9+/=])" % ENCODED_MIN_LEN)
_B64_URL = re.compile(r"(?<![A-Za-z0-9_\-=])[A-Za-z0-9_\-]{%d,}={0,2}(?![A-Za-z0-9_\-=])" % ENCODED_MIN_LEN)
# PEM header WITHOUT a matching END (complete blocks are removed earlier by ``pem_block``).
_PK_RESIDUE = re.compile(r"-----B[E]GIN [A-Z0-9 ]*PRIV[A]TE KEY(?: BLOCK)?(?:-----)?")
_PK_BODY_LINE = re.compile(r"[ \t]*[A-Za-z0-9+/]{4,}={0,2}[ \t]*")
_PK_BODY_STRONG = 40  # one base64 line this long right below the header == a real key body
_PK_BODY_LINES = 2    # ... or this many consecutive base64 lines (a truncated key dump)
_HINT_RE = re.compile(r"([^\s:=\[\]\"',(){}<>]+)[\s:=\[\]\"',(){}<>]*$")
_HINT_NUM = re.compile(r"\d{6,}")
_DIGITS = re.compile(r"\D")
# card_luhn guard: a bare digit run right after an identifier word is an id, not a card.
_LUHN_ID_CTX = re.compile(
    r"(?i)(?:(?:\b|_)(?:id|ref|order|invoice|chat|msg|message|uid|hash|commit|txn|tracking|serial|imei"
    r"|isbn|barcode|sku|bot|sender|group|channel|user|file|job|run|task|session)[\s:=#_\-\"'`]*|#\s*)$"
)
# KV_SECRET guard: placeholders / variable references / keyboard chords are not secrets.
_KV_PLACEHOLDER = re.compile(
    r"^(?:<[^<>]{1,80}>|\$\{[A-Za-z_]\w*\}|\$[A-Za-z_]\w*|\{\{[^{}]{1,80}\}\}|%[A-Za-z_]\w*%)$"
)
_KEY_CHORD = re.compile(r"(?i)^(?:ctrl|control|shift|alt|cmd|meta|win|option|super)(?:\+[^\s+]+)+$")
# HIGH_ENTROPY guards: public build identifiers (Next.js ``next-action`` etc.) and markdown anchors.
_BUILD_ID_CTX = re.compile(r"(?i)(?:next-action|x-nextjs|__next|build-?id|chunk|webpack|integrity)")
_HEXISH = re.compile(r"[0-9a-fA-F]{32,}")


class RedactionIncomplete(RuntimeError):
    """Raised by ``redact_file`` when the output could not be made fully clean."""


@dataclass(frozen=True)
class Pattern:
    category: str
    name: str
    regex: "re.Pattern[str]"
    group: int = 0
    check: Optional[str] = None
    replacement: Optional[str] = None


@dataclass
class RedactResult:
    text: str
    counts: Dict[str, int] = field(default_factory=dict)
    entropy_hits: List[dict] = field(default_factory=list)
    unresolved_private_key: bool = False
    pattern_counts: Dict[str, int] = field(default_factory=dict)
    hints: Dict[str, Dict[str, int]] = field(default_factory=dict)


def marker(category: str) -> str:
    return MARKER_PREFIX + category + "]"


# --------------------------------------------------------------------------- config loading

_PATTERN_CACHE: Dict[str, List[Pattern]] = {}
_ALLOW_CACHE: Dict[str, Tuple[str, ...]] = {}
_DENY_CACHE: Dict[str, dict] = {}


def _compile(entry: dict) -> Pattern:
    flags = 0
    for ch in str(entry.get("flags", "")):
        flags |= _FLAG_MAP[ch.upper()]
    return Pattern(
        category=entry["category"],
        name=entry["name"],
        regex=re.compile(entry["regex"], flags),
        group=int(entry.get("group", 0) or 0),
        check=entry.get("check"),
        replacement=entry.get("replacement"),
    )


def _patterns_data(path=None) -> dict:
    return json.loads(vaultlib.read_text(Path(path or PATTERNS_FILE)))


def load_patterns(path=None) -> List[Pattern]:
    """Compiled patterns, stably sorted by CATEGORY_ORDER (file order kept inside a category)."""
    key = str(Path(path or PATTERNS_FILE).resolve())
    if key not in _PATTERN_CACHE:
        data = _patterns_data(path)
        compiled = [_compile(e) for e in data["patterns"]]
        bad = sorted({p.category for p in compiled} - set(CATEGORY_ORDER))
        if bad:
            raise ValueError("unknown pattern categories: " + ", ".join(bad))
        compiled.sort(key=lambda p: CATEGORY_ORDER.index(p.category))
        _PATTERN_CACHE[key] = compiled
    return _PATTERN_CACHE[key]


def load_allowlist(path=None) -> Tuple[str, ...]:
    key = str(Path(path or PATTERNS_FILE).resolve())
    if key not in _ALLOW_CACHE:
        _ALLOW_CACHE[key] = tuple(str(t) for t in _patterns_data(path).get("allowlist", []) if t)
    return _ALLOW_CACHE[key]


def load_denylist(path=None) -> dict:
    key = str(Path(path or DENYLIST_FILE).resolve())
    if key not in _DENY_CACHE:
        data = json.loads(vaultlib.read_text(Path(path or DENYLIST_FILE)))
        for k in ("DENY_READ", "DENY_READ_DIRS", "DENY_COPY"):
            if not isinstance(data.get(k), list):
                raise ValueError("denylist.json missing list: " + k)
        _DENY_CACHE[key] = data
    return _DENY_CACHE[key]


DEFAULT_ALLOWLIST: Tuple[str, ...] = load_allowlist()


# --------------------------------------------------------------------------- denylist

def is_denied_path(path, layer: str = "READ") -> bool:
    """True when the file name or ANY path component matches the deny layer (case-insensitive)."""
    lyr = str(layer).upper()
    if lyr not in LAYERS:
        raise ValueError("layer must be one of READ/COPY/ANY, got %r" % (layer,))
    s = str(path or "").strip()
    if not s:
        return False
    comps = [c.lower() for c in s.replace("\\", "/").split("/") if c and c not in (".", "..", "~")]
    if not comps:
        return False
    dl = load_denylist()

    def hit(pats: Iterable[str]) -> bool:
        pats = [p.lower() for p in pats]
        return any(fnmatch.fnmatchcase(c, p) for c in comps for p in pats)

    if lyr in ("READ", "ANY"):
        dirs = {d.lower() for d in dl["DENY_READ_DIRS"]}
        if hit(dl["DENY_READ"]) or any(c in dirs for c in comps):
            return True
    if lyr in ("COPY", "ANY") and hit(dl["DENY_COPY"]):
        return True
    return False


# --------------------------------------------------------------------------- helpers / checks

def shannon_entropy(s: str) -> float:
    if not s:
        return 0.0
    n = len(s)
    return -sum((c / n) * math.log2(c / n) for c in Counter(s).values())


def luhn_ok(s: str) -> bool:
    """Luhn checksum over the digits of *s* (13-19 digits only)."""
    digits = [int(c) for c in s if c.isdigit()]
    if not 13 <= len(digits) <= 19:
        return False
    total = 0
    for i, d in enumerate(reversed(digits)):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def _only_digits(s: str) -> str:
    return _DIGITS.sub("", s)


def _epoch_ms_like(digits: str) -> bool:
    return len(digits) == 13 and digits[0] == "1" and digits[1] in "56789"


def _in_iso_date(text: str, start: int, end: int) -> bool:
    lo, hi = max(0, start - 32), min(len(text), end + 32)
    for dm in _ISO_DATE.finditer(text, lo, hi):
        if dm.start() <= start and dm.end() >= end:
            return True
    return False


def _numeric_context_excluded(text: str, start: int) -> bool:
    return bool(_PHONE_CTX.search(text[max(0, start - 24):start]))


def _check_phone(text: str, m: "re.Match[str]", value: str) -> bool:
    if _numeric_context_excluded(text, m.start()):
        return False
    if _epoch_ms_like(_only_digits(value)):
        return False
    return not _in_iso_date(text, m.start(), m.end())


def _in_hex_digest(text: str, start: int, end: int) -> bool:
    """True when digits sit inside a >=24-char hex token containing hex letters (SHA/MD5/ObjectId)."""
    lo, hi = start, end
    while lo > 0 and _HEX_CHAR.match(text[lo - 1]):
        lo -= 1
    while hi < len(text) and _HEX_CHAR.match(text[hi]):
        hi += 1
    tok = text[lo:hi]
    return len(tok) >= 24 and any("a" <= c.lower() <= "f" for c in tok)


def _check_luhn(text: str, m: "re.Match[str]", value: str) -> bool:
    if _in_hex_digest(text, m.start(), m.end()):
        return False
    d = _only_digits(value)
    if _epoch_ms_like(d) or _numeric_context_excluded(text, m.start()):
        return False
    if _LUHN_ID_CTX.search(text[max(0, m.start() - 24):m.start()]):
        return False  # "id 1234…", "order #…", "chat_id=…": an identifier that passes Luhn by chance
    return luhn_ok(d)


def _check_denied_path(text: str, m: "re.Match[str]", value: str) -> bool:
    return is_denied_path(value, "READ")


def _check_kv_value(text: str, m: "re.Match[str]", value: str) -> bool:
    """False for placeholders (<token>, ${VAR}, {{x}}, %VAR%) and keyboard chords (ctrl+shift+p)."""
    v = value.strip()
    return not (_KV_PLACEHOLDER.match(v) or _KEY_CHORD.match(v))


CHECKS: Dict[str, Callable[[str, "re.Match[str]", str], bool]] = {
    "phone_context": _check_phone,
    "luhn": _check_luhn,
    "denied_path": _check_denied_path,
    "kv_value": _check_kv_value,
}


def _context_hint(text: str, start: int) -> str:
    """The single word preceding *start* (never a value: paths, long numbers, long / opaque words are masked)."""
    prefix = text[max(0, start - 40):start]
    if MARKER_PREFIX in prefix[-30:] and prefix.rstrip().endswith("]"):
        return "<redacted>"
    m = _HINT_RE.search(prefix)
    if not m:
        return ""
    w = m.group(1)
    if "~" in w or "/" in w or "\\" in w:
        return "<path>"  # never leak a path component (folder / bot / account names)
    if _HINT_NUM.search(w):
        return "<num>"  # never leak numeric ids (bot ids, chat ids, phone fragments)
    if len(w) > 24:
        return "<long>"
    if len(w) >= 12 and shannon_entropy(w) >= 3.6:
        return "<opaque>"
    return w


# --------------------------------------------------------------------------- core passes

def _span(pt: Pattern, m: "re.Match[str]") -> Tuple[int, int]:
    return m.span(pt.group) if pt.group else m.span()


def _apply(text: str, patterns: Sequence[Pattern], counts: Counter, pattern_counts: Counter,
           hints: Optional[dict] = None, count_key: Optional[str] = None,
           skip_values: Optional[frozenset] = None) -> str:
    """Replace matches in order. *skip_values*: exact matches equal to an allow-listed term are kept."""
    for pt in patterns:
        out: List[str] = []
        last = 0
        changed = False
        for m in pt.regex.finditer(text):
            s, e = _span(pt, m)
            if s < 0 or e <= s:
                continue
            value = text[s:e]
            if MARKER_PREFIX in value or (skip_values and value in skip_values):
                continue
            if pt.check and not CHECKS[pt.check](text, m, value):
                continue
            out.append(text[last:s])
            out.append(pt.replacement if pt.replacement is not None else marker(pt.category))
            last = e
            changed = True
            counts[count_key or pt.category] += 1
            pattern_counts[pt.name] += 1
            if hints is not None:
                hints[pt.name][_context_hint(text, s)] += 1
        if changed:
            out.append(text[last:])
            text = "".join(out)
    return text


def _has_secret(text: str, patterns: Sequence[Pattern]) -> bool:
    for pt in patterns:
        if pt.category == "PATH":
            continue
        for m in pt.regex.finditer(text):
            s, e = _span(pt, m)
            if s < 0 or e <= s:
                continue
            value = text[s:e]
            if MARKER_PREFIX in value:
                continue
            if pt.check and not CHECKS[pt.check](text, m, value):
                continue
            return True
    return False


def _decode_b64(s: str) -> Optional[str]:
    body = s.rstrip("=")
    body += "=" * (-len(body) % 4)
    try:
        if "-" in body or "_" in body:
            raw = base64.urlsafe_b64decode(body)
        else:
            raw = base64.b64decode(body, validate=True)
    except (binascii.Error, ValueError):
        return None
    return raw.decode("utf-8", "ignore")


def _encoded_pass(text: str, patterns: Sequence[Pattern], counts: Counter, pattern_counts: Counter) -> str:
    for rx, name in ((_B64_STD, "base64_std"), (_B64_URL, "base64_url")):
        out: List[str] = []
        last = 0
        changed = False
        for m in rx.finditer(text):
            decoded = _decode_b64(m.group())
            if not decoded or not _has_secret(decoded, patterns):
                continue
            out.append(text[last:m.start()])
            out.append(marker("ENCODED"))
            last = m.end()
            changed = True
            counts["ENCODED"] += 1
            pattern_counts[name] += 1
        if changed:
            out.append(text[last:])
            text = "".join(out)
    return text


def _pk_residue_pass(text: str, counts: Counter, pattern_counts: Counter) -> Tuple[str, bool]:
    """Redact every PEM header that has no END (``pem_block`` already removed complete blocks).

    The header (and, when it ends its line, every base64-looking line directly below it) becomes
    ``[REDACTED:PRIVATE_KEY]``.  Returns ``(text, unresolved)``: *unresolved* is True only when a
    real key body followed (a base64 line of >= _PK_BODY_STRONG chars), so a conversation that merely
    MENTIONS the header text is kept instead of being dropped."""
    out: List[str] = []
    last = 0
    unresolved = False
    n = len(text)

    def body_line(line: str) -> bool:
        s = line.strip()
        # short lines must be a whole base64 quantum so an ordinary word is not taken for key body
        return bool(s) and bool(_PK_BODY_LINE.fullmatch(line)) and (len(s) >= 16 or len(s) % 4 == 0)

    for m in _PK_RESIDUE.finditer(text):
        if m.start() < last:
            continue
        end = m.end()
        eol = text.find("\n", end)
        eol = n if eol == -1 else eol
        rest = text[end:eol]
        lines = 0
        if body_line(rest):
            lines += 1
            unresolved = unresolved or len(rest.strip()) >= _PK_BODY_STRONG
            rest = ""
        if not rest.strip():
            pos = eol
            while pos < n:
                nl = text.find("\n", pos + 1)
                nl = n if nl == -1 else nl
                line = text[pos + 1:nl]
                if not body_line(line):
                    break
                lines += 1
                unresolved = unresolved or len(line.strip()) >= _PK_BODY_STRONG
                pos = nl
            end = pos
        unresolved = unresolved or lines >= _PK_BODY_LINES
        out.append(text[last:m.start()])
        out.append(marker("PRIVATE_KEY"))
        last = end
        counts["PRIVATE_KEY"] += 1
        pattern_counts["pem_residue"] += 1
    if not out:
        return text, False
    out.append(text[last:])
    return "".join(out), unresolved


def _entropy_pass(text: str, hits: List[dict]) -> None:
    for m in _TOKEN.finditer(text):
        tokv = m.group()
        before = text[max(0, m.start() - 60):m.start()]
        keyword_before = bool(_SECRET_WORDS.search(before[-40:]))
        if not keyword_before:
            if _HEX40.fullmatch(tokv) or _HEX64.fullmatch(tokv) or _UUID.fullmatch(tokv):
                continue
            if before.endswith("#") or before.endswith("]("):
                continue  # markdown anchor / link target (docs slugs), not a credential
            if _HEXISH.fullmatch(tokv) and _BUILD_ID_CTX.search(before):
                continue  # public build identifier (e.g. Next.js ``next-action`` header)
        ent = shannon_entropy(tokv)
        if ent < ENTROPY_THRESHOLD:
            continue
        hits.append({
            "category": "HIGH_ENTROPY",
            "length": len(tokv),
            "entropy": round(ent, 3),
            "context_hint": _context_hint(text, m.start()),
        })


def _protect(text: str, allow: Sequence[str]) -> Tuple[str, List[Tuple[str, str]]]:
    mapping: List[Tuple[str, str]] = []
    terms = sorted({vaultlib.nfc(t) for t in allow if t}, key=len, reverse=True)
    for i, term in enumerate(terms):
        if term in text:
            ph = "\ue000" + chr(0xE100 + i) + "\ue001"
            text = text.replace(term, ph)
            mapping.append((ph, term))
    return text, mapping


def _restore(text: str, mapping: List[Tuple[str, str]]) -> str:
    for ph, term in mapping:
        text = text.replace(ph, term)
    return text


def redact_text(text: str, *, allowlist: Optional[Sequence[str]] = None,
                patterns: Optional[Sequence[Pattern]] = None, collect_hints: bool = False) -> RedactResult:
    """Redact *text* in memory. ``allowlist=None`` -> DEFAULT_ALLOWLIST; ``[]`` -> none."""
    pats = list(patterns) if patterns is not None else load_patterns()
    allow = DEFAULT_ALLOWLIST if allowlist is None else tuple(allowlist)
    counts: Counter = Counter()
    pattern_counts: Counter = Counter()
    hints = defaultdict(Counter) if collect_hints else None

    text = vaultlib.nfc(text)
    text, mapping = _protect(text, allow)
    text = _apply(text, pats, counts, pattern_counts, hints)
    text, unresolved = _pk_residue_pass(text, counts, pattern_counts)
    text = _encoded_pass(text, pats, counts, pattern_counts)
    hits: List[dict] = []
    _entropy_pass(text, hits)
    text = _restore(text, mapping)
    allow_exact = frozenset(vaultlib.nfc(t) for t in allow if t)
    text = _apply(text, pats, counts, pattern_counts, hints, count_key="SECOND_PASS", skip_values=allow_exact)
    unresolved = unresolved or bool(_PK_RESIDUE.search(text))
    return RedactResult(
        text=text,
        counts=dict(counts),
        entropy_hits=hits,
        unresolved_private_key=unresolved,
        pattern_counts=dict(pattern_counts),
        hints={k: dict(v) for k, v in hints.items()} if hints else {},
    )


def residual_matches(text: str, patterns: Optional[Sequence[Pattern]] = None,
                     allowlist: Optional[Sequence[str]] = None) -> Dict[str, int]:
    """Categories that would STILL be redacted in *text* (empty dict == clean).
    Exact matches equal to an allow-listed term are not counted (same rule as the second pass)."""
    pats = list(patterns) if patterns is not None else load_patterns()
    allow = DEFAULT_ALLOWLIST if allowlist is None else tuple(allowlist)
    allow_exact = frozenset(vaultlib.nfc(t) for t in allow if t)
    counts: Counter = Counter()
    _apply(text, pats, counts, Counter(), skip_values=allow_exact)
    if _PK_RESIDUE.search(text):
        counts["PRIVATE_KEY_UNRESOLVED"] += 1
    return dict(counts)


def redact_file(src, dst, **kw) -> RedactResult:
    """Redact *src* into *dst* (UTF-8, LF). Raises RedactionIncomplete and writes NOTHING when unclean."""
    res = redact_text(vaultlib.read_text(src), **kw)
    if res.unresolved_private_key:
        raise RedactionIncomplete("unresolved private-key block in %s" % Path(src).name)
    left = residual_matches(res.text, kw.get("patterns"), kw.get("allowlist"))
    if left:
        raise RedactionIncomplete("residual matches in %s: %s" % (Path(src).name, sorted(left)))
    vaultlib.write_text(dst, res.text)
    return res


# --------------------------------------------------------------------------- dry-run CLI

class _Agg:
    def __init__(self, label: str) -> None:
        self.label = label
        self.items = 0
        self.chars = 0
        self.unreadable = 0
        self.unresolved = 0
        self.counts: Counter = Counter()
        self.pattern_counts: Counter = Counter()
        self.entropy_hints: Counter = Counter()
        self.entropy_total = 0
        self.hints: Dict[str, Counter] = defaultdict(Counter)
        self.per_item: Counter = Counter()
        self.denied: List[str] = []
        self.notes: List[str] = []

    def add(self, name: str, res: RedactResult) -> None:
        self.items += 1
        self.counts.update(res.counts)
        self.pattern_counts.update(res.pattern_counts)
        self.entropy_total += len(res.entropy_hits)
        self.entropy_hints.update(h["context_hint"] or "<none>" for h in res.entropy_hits)
        for pname, hc in res.hints.items():
            self.hints[pname].update(hc)
        if res.unresolved_private_key:
            self.unresolved += 1
        self.per_item[name] += sum(res.counts.values())


def _md_table(headers: List[str], rows: List[list]) -> List[str]:
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c).replace("|", "\\|").replace("\n", " ") for c in r) + " |")
    return out


def _render(agg: _Agg) -> str:
    L: List[str] = ["", "## Source: %s" % agg.label, ""]
    L.append("- items scanned: %d · chars: %s · unreadable: %d · unresolved_private_key: %d · entropy_hits: %d"
             % (agg.items, format(agg.chars, ","), agg.unreadable, agg.unresolved, agg.entropy_total))
    for n in agg.notes:
        L.append("- " + n)
    if agg.denied:
        L.append("- denied by `is_denied_path` (%d, names only): %s" % (len(agg.denied), ", ".join("`%s`" % d for d in agg.denied)))
    L += ["", "### Counts per category", ""]
    cats = [c for c in CATEGORY_ORDER + ("ENCODED", "SECOND_PASS") if agg.counts.get(c)]
    L += _md_table(["category", "redactions"], [[c, agg.counts[c]] for c in cats] or [["(none)", 0]])
    L += ["", "### Top 20 patterns", ""]
    L += _md_table(["pattern", "hits", "top context words (count)"], [
        [name, n, ", ".join("%s(%d)" % (w or "<none>", c) for w, c in agg.hints[name].most_common(5))]
        for name, n in agg.pattern_counts.most_common(20)
    ] or [["(none)", 0, ""]])
    L += ["", "### HIGH_ENTROPY hits by context_hint (record only, never redacted)", ""]
    L += _md_table(["context_hint", "hits"], [[w, c] for w, c in agg.entropy_hints.most_common(25)] or [["(none)", 0]])
    L += ["", "### Top 20 items by redaction count", ""]
    L += _md_table(["item", "redactions"], [[n, c] for n, c in agg.per_item.most_common(20)] or [["(none)", 0]])
    return "\n".join(L) + "\n"


def _collect_files(paths: Sequence[str], pattern: str, recursive: bool, max_files: int, agg: _Agg) -> List[Path]:
    files: List[Path] = []
    for raw in paths:
        p = Path(raw).expanduser()
        if p.is_dir():
            found = sorted(x for x in (p.rglob(pattern) if recursive else p.glob(pattern)) if x.is_file())
        elif p.is_file():
            found = [p]
        else:
            agg.notes.append("missing path skipped: `%s`" % p.name)
            continue
        for f in found:
            if is_denied_path(str(f), "READ"):
                agg.denied.append(f.name)
            else:
                files.append(f)
    if max_files and len(files) > max_files:
        agg.notes.append("capped at --max-files %d (of %d)" % (max_files, len(files)))
        files = files[:max_files]
    return files


def _scan_files(files: List[Path], agg: _Agg) -> None:
    for f in files:
        try:
            text = vaultlib.read_text(f)
        except (OSError, UnicodeDecodeError):
            agg.unreadable += 1
            continue
        agg.chars += len(text)
        agg.add(f.name, redact_text(text, collect_hints=True))


def _sqlite_uri(p: Path) -> str:
    s = str(p.resolve()).replace("\\", "/")
    if not s.startswith("/"):
        s = "/" + s
    return "file:%s?mode=ro" % s


def _sidecars(db: Path) -> List[Path]:
    return [p for p in (db, Path(str(db) + "-wal"), Path(str(db) + "-shm")) if p.exists()]


def _qi(ident: str) -> str:
    return '"' + ident.replace('"', '""') + '"'


def _scan_sqlite(spec: str, max_rows: int, temp_dir: Path, agg: _Agg) -> None:
    """spec = "db_path|table|col1,col2[|group_col]" — copy to temp, open copy read-only, scan rows in memory."""
    parts = spec.split("|")
    if len(parts) < 3:
        raise SystemExit("--sqlite spec must be db|table|cols[|group_col]")
    src, table, cols = Path(parts[0]).expanduser(), parts[1], [c.strip() for c in parts[2].split(",") if c.strip()]
    group_col = parts[3].strip() if len(parts) > 3 and parts[3].strip() else None
    if not src.is_file():
        agg.notes.append("database missing: `%s`" % src.name)
        return
    files = _sidecars(src)
    before = {p.name: vaultlib.sha256_file(p) for p in files}
    temp_dir.mkdir(parents=True, exist_ok=True)
    try:
        for p in files:
            shutil.copy2(p, temp_dir / p.name)
        con = sqlite3.connect(_sqlite_uri(temp_dir / src.name), uri=True)
        try:
            sel = ", ".join(_qi(c) for c in cols)
            if group_col:
                sql = "SELECT %s FROM %s WHERE %s IN (SELECT DISTINCT %s FROM %s LIMIT %d)" % (
                    sel, _qi(table), _qi(group_col), _qi(group_col), _qi(table), max_rows)
            else:
                sql = "SELECT %s FROM %s LIMIT %d" % (sel, _qi(table), max_rows)
            n = 0
            for row in con.execute(sql):
                n += 1
                pieces = []
                for v in row:
                    if v is None:
                        continue
                    if isinstance(v, bytes):
                        v = v.decode("utf-8", "ignore")
                    pieces.append(str(v))
                text = "\n".join(pieces)
                agg.chars += len(text)
                agg.add("%s#row%d" % (table, n), redact_text(text, collect_hints=True))
            agg.notes.append("sqlite `%s`.`%s` cols=%s rows=%d%s" % (
                src.name, table, ",".join(cols), n, (" (grouped by %s, limit %d)" % (group_col, max_rows)) if group_col else ""))
        finally:
            con.close()
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
    after = {p.name: vaultlib.sha256_file(p) for p in files}
    for name in before:
        agg.notes.append("sha256 `%s` before=`%s` after=`%s` match=%s" % (
            name, before[name], after.get(name, "-"), before[name] == after.get(name)))
    agg.notes.append("temp copy removed: %s" % (not temp_dir.exists()))


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Vault redaction engine (dry-run CLI).")
    ap.add_argument("--dry-run", action="store_true", required=True, help="scan in memory only; never writes redacted files")
    ap.add_argument("paths", nargs="*", help="files or directories to scan")
    ap.add_argument("--report", required=True, help="markdown report path (counters only)")
    ap.add_argument("--max-files", type=int, default=0)
    ap.add_argument("--glob", default="*.md", help="pattern for directory arguments (default *.md)")
    ap.add_argument("--recursive", action="store_true")
    ap.add_argument("--label", default="", help="section label in the report")
    ap.add_argument("--append", action="store_true", help="append a section instead of overwriting the report")
    ap.add_argument("--sqlite", action="append", default=[], help="db|table|col1,col2[|group_col] (repeatable)")
    ap.add_argument("--max-rows", type=int, default=400)
    ap.add_argument("--temp-dir", default="")
    a = ap.parse_args(argv)

    label = a.label or (", ".join(Path(p).name for p in a.paths) or "sqlite")
    agg = _Agg(label)
    temp_dir = Path(a.temp_dir) if a.temp_dir else (
        Path(os.environ.get("LOCALAPPDATA") or tempfile.gettempdir()) / "Temp" / "opencode" / "vault-t2")
    if a.paths:
        _scan_files(_collect_files(a.paths, a.glob, a.recursive, a.max_files, agg), agg)
    for spec in a.sqlite:
        _scan_sqlite(spec, a.max_rows, temp_dir, agg)

    section = _render(agg)
    report = Path(a.report)
    if a.append and report.is_file():
        vaultlib.write_text(report, vaultlib.read_text(report) + section)
    else:
        vaultlib.write_text(report, "# Redaction dry-run report (counters only, no raw content)\n" + section)
    print("[redact --dry-run] %s: items=%d redactions=%d entropy_hits=%d unresolved=%d denied=%d" % (
        label, agg.items, sum(agg.counts.values()), agg.entropy_total, agg.unresolved, len(agg.denied)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
