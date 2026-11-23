"""T2 — redaction engine tests (TDD).

Every fixture is BUILT AT RUNTIME from fragments so that no string resembling a
real key / token / e-mail / key header ever appears literally in this file.
"""
import base64
import json
import os
import re
import tempfile
import unicodedata
import unittest
from pathlib import Path

from tools import vaultlib
from tools.redact import (
    CATEGORY_ORDER,
    DEFAULT_ALLOWLIST,
    PATTERNS_FILE,
    RedactResult,
    RedactionIncomplete,
    load_patterns,
    luhn_ok,
    redact_file,
    redact_text,
    residual_matches,
    shannon_entropy,
)

_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
_HEX = "0123456789abcdef"


def tok(prefix: str, n: int, alphabet: str = _ALPHA) -> str:
    """Deterministic token-shaped filler: prefix + n cycling alphabet chars."""
    return prefix + "".join(alphabet[i % len(alphabet)] for i in range(n))


def marker(cat: str) -> str:
    return "[REDACTED:" + cat + "]"


def email(local: str = "user", domain: str = "example.org") -> str:
    return local + "@" + domain


def pem(kind: str = "RSA", lines: int = 3, truncated: bool = False) -> str:
    head = "-----" + "BEG" + "IN " + kind + " PRIV" + "ATE KEY-----"
    tail = "-----" + "E" + "ND " + kind + " PRIV" + "ATE KEY-----"
    body = "\n".join(tok("", 64, _ALPHA + "+/") for _ in range(lines))
    return head + "\n" + body + ("\n" if truncated else "\n" + tail + "\n")


def eg_mobile(sep: str = "", cc: str = "", lead: str = "0") -> str:
    """Egyptian-mobile-shaped fixture assembled from fragments (never a literal number)."""
    return cc + lead + "10" + sep + "1234" + sep + "5678"


_CARD_PARTIAL = "4539" + "1488" + "0343" + "646"  # 15 digits; check digit appended at runtime


def luhn_complete(partial: str) -> str:
    digits = [int(c) for c in partial]
    total = 0
    for i, d in enumerate(reversed(digits)):
        if i % 2 == 0:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return partial + str((10 - total % 10) % 10)


class TestPatternsFile(unittest.TestCase):
    def test_shape_and_order(self):
        data = json.loads(vaultlib.read_text(PATTERNS_FILE))
        self.assertIn("patterns", data)
        self.assertIn("allowlist", data)
        cats = []
        for p in data["patterns"]:
            self.assertEqual({"category", "name", "regex"} - set(p), set(), p.get("name"))
            self.assertIn(p["category"], CATEGORY_ORDER)
            re.compile(p["regex"])
            cats.append(p["category"])
        # every regex category present, and the compiled list is in CATEGORY_ORDER
        self.assertEqual(set(cats), set(CATEGORY_ORDER))
        compiled = load_patterns()
        order = [CATEGORY_ORDER.index(p.category) for p in compiled]
        self.assertEqual(order, sorted(order))
        for term in ("PHOENIX-9941", "gateway-service", "SMS"):
            self.assertIn(term, DEFAULT_ALLOWLIST)

    def test_helpers(self):
        valid = luhn_complete(_CARD_PARTIAL)
        self.assertTrue(luhn_ok(valid))
        self.assertFalse(luhn_ok(valid[:-1] + str((int(valid[-1]) + 1) % 10)))
        self.assertAlmostEqual(shannon_entropy("aaaa"), 0.0)
        self.assertAlmostEqual(shannon_entropy(_HEX * 4), 4.0)

    def test_result_type(self):
        r = redact_text("plain")
        self.assertIsInstance(r, RedactResult)
        self.assertEqual((r.text, r.counts, r.entropy_hits, r.unresolved_private_key), ("plain", {}, [], False))


class TestCleanInputs(unittest.TestCase):
    def test_arabic_clean_unchanged(self):
        t = "مرحباً يا زيزو، هذا نص عربي نظيف عن مشروع الذاكرة. رقم الطلب 2024 والسعر 1500 جنيه بتاريخ الجمعة."
        r = redact_text(t)
        self.assertEqual(r.text, unicodedata.normalize("NFC", t))
        self.assertEqual(r.counts, {})
        self.assertEqual(r.entropy_hits, [])

    def test_python_code_clean_unchanged(self):
        t = (
            "def add(a, b):\n    return a + b\n\n"
            "items = [1, 2, 3]\nfor i, x in enumerate(items):\n    print(f'{i}: {x * 2}')\n"
            "class Box:\n    size = 10\n"
        )
        r = redact_text(t)
        self.assertEqual(r.text, t)
        self.assertEqual(r.counts, {})

    def test_json_clean_unchanged(self):
        t = json.dumps({"name": "vault", "count": 3, "items": [1, 2, 3], "enabled": True, "ratio": 0.5}, indent=2)
        r = redact_text(t)
        self.assertEqual(r.text, t)
        self.assertEqual(r.counts, {})

    def test_sha40_and_uuid_untouched_and_not_logged(self):
        sha40 = _HEX * 2 + _HEX[:8]
        uid = "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
        t = "commit " + sha40 + " belongs to run " + uid + " done"
        r = redact_text(t)
        self.assertEqual(r.text, t)
        self.assertEqual(r.counts, {})
        self.assertEqual(r.entropy_hits, [])

    def test_sha64_logged_only_when_preceded_by_token(self):
        sha64 = _HEX * 4
        r1 = redact_text("digest " + sha64)
        self.assertEqual(r1.entropy_hits, [])
        self.assertEqual(r1.counts, {})
        r2 = redact_text("token " + sha64)
        self.assertEqual(r2.text, "token " + sha64)  # record only, never redacted
        self.assertEqual(len(r2.entropy_hits), 1)
        hit = r2.entropy_hits[0]
        self.assertEqual(hit["category"], "HIGH_ENTROPY")
        self.assertEqual(hit["length"], 64)
        self.assertEqual(hit["context_hint"], "token")
        self.assertNotIn(sha64, json.dumps(hit))

    def test_high_entropy_recorded_without_value(self):
        blob = tok("", 40)
        r = redact_text("blob " + blob + " end")
        self.assertEqual(r.text, "blob " + blob + " end")
        self.assertEqual(len(r.entropy_hits), 1)
        hit = r.entropy_hits[0]
        self.assertEqual(set(hit), {"category", "length", "entropy", "context_hint"})
        self.assertEqual(hit["length"], 40)
        self.assertGreaterEqual(hit["entropy"], 4.0)
        self.assertEqual(hit["context_hint"], "blob")
        self.assertNotIn(blob, json.dumps(hit))


class TestPrivateKey(unittest.TestCase):
    def test_multiline_block_redacted(self):
        t = "before\n" + pem("RSA", 4) + "after\n"
        r = redact_text(t)
        self.assertEqual(r.text, "before\n" + marker("PRIVATE_KEY") + "\nafter\n")
        self.assertEqual(r.counts.get("PRIVATE_KEY"), 1)
        self.assertFalse(r.unresolved_private_key)

    def test_ec_and_openssh_variants(self):
        t = pem("EC", 2) + pem("OPENSSH", 2) + pem("", 2).replace("  ", " ")
        r = redact_text(t)
        self.assertNotIn("PRIV" + "ATE KEY", r.text)
        self.assertEqual(r.counts.get("PRIVATE_KEY"), 3)

    def test_truncated_block_sets_unresolved(self):
        r = redact_text("x\n" + pem("RSA", 2, truncated=True))
        self.assertTrue(r.unresolved_private_key)


class TestCredentialPatterns(unittest.TestCase):
    def test_url_with_creds_keeps_host_any_scheme(self):
        for scheme in ("https", "postgres", "redis", "amqp", "mongodb+srv"):
            with self.subTest(scheme=scheme):
                t = "dsn " + scheme + "://admin:" + tok("", 12) + "@db.internal.example:5432/app ok"
                r = redact_text(t)
                self.assertEqual(r.text, "dsn " + scheme + "://" + marker("URL_WITH_CREDS") + "@db.internal.example:5432/app ok")
                self.assertEqual(r.counts, {"URL_WITH_CREDS": 1})

    def test_oauth_ya29_jwt_bearer(self):
        ya = tok("ya29.", 60, _ALPHA + "-_")
        jwt = "eyJ" + tok("", 20) + ".eyJ" + tok("", 40) + "." + tok("", 43, _ALPHA + "-_")
        bearer = "Bearer " + tok("", 40)
        for raw in (ya, jwt, bearer):
            with self.subTest(raw=raw[:8]):
                r = redact_text("x " + raw + " y")
                self.assertIn(marker("OAUTH_JWT"), r.text)
                self.assertNotIn(raw[-20:], r.text)
                self.assertEqual(r.counts.get("OAUTH_JWT"), 1)

    def test_github_tokens(self):
        for raw in (tok("ghp_", 36), tok("gho_", 36), tok("github_pat_", 60, _ALPHA + "_")):
            with self.subTest(raw=raw[:6]):
                r = redact_text("use " + raw + " now")
                self.assertEqual(r.text, "use " + marker("GITHUB_TOKEN") + " now")

    def test_webhooks(self):
        slack = "https://hooks.slack.com/services/" + tok("", 9).upper() + "/" + tok("", 11).upper() + "/" + tok("", 24)
        discord = "https://discord.com/api/webhooks/" + "1" * 18 + "/" + tok("", 68, _ALPHA + "-_")
        for raw in (slack, discord):
            with self.subTest(raw=raw[:20]):
                r = redact_text("hook: " + raw)
                self.assertEqual(r.text, "hook: " + marker("WEBHOOK"))

    def test_api_key_prefixes(self):
        fixtures = [
            tok("sk-", 48),
            tok("sk-proj-", 60, _ALPHA + "_-"),
            tok("AIza", 35, _ALPHA + "-_"),
            tok("up_", 32),
            tok("xoxb-", 40, _ALPHA + "-"),
            "AKIA" + "IOSFODNN7EXAMPLE",
            tok("sk_live_", 24),
            tok("rk_test_", 24),
            tok("GOCSPX-", 28, _ALPHA + "-_"),
            "SG." + tok("", 22, _ALPHA + "-_") + "." + tok("", 43, _ALPHA + "-_"),
            "AC" + _HEX * 2,
            tok("hf_", 34),
            tok("npm_", 36),
            "AccountKey=" + tok("", 86, _ALPHA + "+/") + "==",
            tok("sbp_", 40),
            "1" * 9 + ":" + tok("", 35, _ALPHA + "-_"),
        ]
        for raw in fixtures:
            with self.subTest(raw=raw[:8]):
                r = redact_text("val " + raw + " end")
                self.assertEqual(r.text, "val " + marker("API_KEY") + " end", raw[:8])
                self.assertEqual(r.counts.get("API_KEY"), 1)


class TestKvSecret(unittest.TestCase):
    def test_json_password_value_only(self):
        secret = tok("", 16)
        t = json.dumps({"user": "alice", "password": secret, "port": 5432})
        r = redact_text(t)
        self.assertIn('"password": "' + marker("KV_SECRET") + '"', r.text)
        self.assertIn('"user": "alice"', r.text)
        self.assertIn('"port": 5432', r.text)
        self.assertNotIn(secret, r.text)
        self.assertEqual(r.counts, {"KV_SECRET": 1})

    def test_env_line(self):
        secret = tok("", 20)
        t = "APP_NAME=vault\nDB_PASSWORD=" + secret + "\nDEBUG=1\n"
        r = redact_text(t)
        self.assertEqual(r.text, "APP_NAME=vault\nDB_PASSWORD=" + marker("KV_SECRET") + "\nDEBUG=1\n")

    def test_yaml_and_header(self):
        s1, s2 = tok("", 18), tok("", 30)
        t = "api_key: " + s1 + "\nX-Api-Key: " + s2 + "\nname: demo\n"
        r = redact_text(t)
        self.assertEqual(r.text, "api_key: " + marker("KV_SECRET") + "\nX-Api-Key: " + marker("KV_SECRET") + "\nname: demo\n")
        self.assertEqual(r.counts, {"KV_SECRET": 2})

    def test_cookie_header_value_only(self):
        t = "Cookie: session=" + tok("", 24) + "; theme=dark\n"
        r = redact_text(t)
        self.assertTrue(r.text.startswith("Cookie: " + marker("KV_SECRET")))
        self.assertNotIn("theme=dark", r.text)


class TestEmailPhonePii(unittest.TestCase):
    def test_email_standard(self):
        e = email("zizo.dev", "mail.example.co.uk")
        r = redact_text("contact " + e + " please")
        self.assertEqual(r.text, "contact " + marker("EMAIL") + " please")

    def test_email_obfuscated(self):
        for e in ("user [at] example [dot] com", "user(at)example(dot)org", "first.last [AT] host [DOT] net"):
            with self.subTest(e=e):
                r = redact_text("mail: " + e + " .")
                self.assertEqual(r.text, "mail: " + marker("EMAIL") + " .")

    def test_phone_egyptian_variants(self):
        dashed = "0" + "12" + "0-" + "123" + "-" + "4567"
        for p in (eg_mobile(" "), eg_mobile(), "+20 " + eg_mobile(" ", lead=""), eg_mobile(cc="+2"), dashed):
            with self.subTest(p=p):
                r = redact_text("اتصل على " + p + " بكرة")
                self.assertEqual(r.text, "اتصل على " + marker("PHONE") + " بكرة")
                self.assertEqual(r.counts, {"PHONE": 1})

    def test_phone_international(self):
        intl = "+44" + " 20" + " 7946" + " 0958"
        r = redact_text("call " + intl + " now")
        self.assertEqual(r.text, "call " + marker("PHONE") + " now")

    def test_epoch_ms_not_phone(self):
        t = '{"time_created": 1700000000123, "seq": 7}'
        r = redact_text(t)
        self.assertEqual(r.text, t)
        self.assertEqual(r.counts, {})
        t2 = "stamp 1512345678901 end"
        self.assertEqual(redact_text(t2).text, t2)

    def test_iso_date_not_phone(self):
        t = "at 2024-01-15T10:12:30Z and 2025-11-22 10:11:12 ok"
        r = redact_text(t)
        self.assertEqual(r.text, t)
        self.assertEqual(r.counts, {})

    def test_phone_keyword_context_excluded(self):
        m = eg_mobile()
        for t in ("session_id: " + m, "version " + m, "port=" + m):
            with self.subTest(t=t):
                self.assertEqual(redact_text(t).text, t)

    def test_national_id(self):
        nid = "2" + "900101" + "".join(str(i) for i in range(1, 8))  # 14 digits, starts with 2
        r = redact_text("الرقم القومي " + nid + " .")
        self.assertEqual(r.text, "الرقم القومي " + marker("PII") + " .")
        self.assertEqual(r.counts, {"PII": 1})

    def test_iban(self):
        iban = "EG" + "".join(str(i % 10) for i in range(27))
        r = redact_text("IBAN " + iban + " end")
        self.assertEqual(r.text, "IBAN " + marker("PII") + " end")

    def test_card_luhn_valid_redacted_invalid_kept(self):
        valid = luhn_complete(_CARD_PARTIAL)
        invalid = valid[:-1] + str((int(valid[-1]) + 1) % 10)
        r = redact_text("card " + valid + " bad " + invalid)
        self.assertEqual(r.text, "card " + marker("PII") + " bad " + invalid)
        spaced = " ".join(valid[i:i + 4] for i in range(0, 16, 4))
        self.assertEqual(redact_text("c: " + spaced + " .").text, "c: " + marker("PII") + " .")

    def test_luhn_not_triggered_inside_hex_digest(self):
        valid = luhn_complete(_CARD_PARTIAL)
        digest = "a1b2c3d4e5f6" + valid + ("0" * (64 - 12 - len(valid)))
        self.assertEqual(len(digest), 64)
        t = "sha256 `" + digest + "` ok"
        r = redact_text(t)
        self.assertEqual(r.text, t)
        self.assertEqual(r.counts, {})


class TestPathsAllowlistEncoded(unittest.TestCase):
    def test_home_six_forms(self):
        forms = [
            "C:\\Users\\zz\\proj\\a.md",
            "C:/Users/zz/proj/a.md",
            "/c/Users/zz/proj/a.md",
            "/mnt/c/Users/zz/proj/a.md",
            "/home/zz/proj/a.md",
            "%USERPROFILE%\\proj\\a.md",
            "$HOME/proj/a.md",
        ]
        r = redact_text("\n".join(forms))
        self.assertNotIn("zz", r.text)
        self.assertEqual(r.text.count("~"), len(forms))
        self.assertEqual(r.counts, {"PATH": len(forms)})

    def test_home_percent3a_file_uri(self):
        t = "app-resource:/c%3A/Users/zz/.gemini/a and file:///C%3A%2FUsers%2Fzz%2Fb and `C:\\Users\\zz`"
        r = redact_text(t)
        self.assertNotIn("zz", r.text)
        self.assertEqual(r.text, "app-resource:/~/.gemini/a and file:///~%2Fb and `~`")
        self.assertEqual(r.counts, {"PATH": 3})

    def test_home_glued_prefix_byte_still_normalized(self):
        # T13-3: a printable protobuf length byte can sit glued to the drive letter (e.g. ``NC:\Users\...``)
        r = redact_text("xC:\\Users\\zz\\a and NC:/Users/zz/Documents/b")
        self.assertNotIn("zz", r.text)
        self.assertEqual(r.text, "x~\\a and N~/Documents/b")
        self.assertEqual(r.counts, {"PATH": 2})

    def test_denied_name_in_path_redacted(self):
        t = "see /home/zz/.ssh/id_rsa and C:\\Users\\zz\\secrets\\keys.md but ~/notes/HANDOFF.md ok"
        r = redact_text(t)
        self.assertEqual(r.text, "see " + marker("PATH") + " and " + marker("PATH") + " but ~/notes/HANDOFF.md ok")

    def test_allowlist_preserved(self):
        t = "زيزو (PHOENIX-9941) يعمل على gateway-service و Bolla-Agentic-OS-EGM-SRE و SMS"
        r = redact_text(t)
        self.assertEqual(r.text, unicodedata.normalize("NFC", t))
        self.assertEqual(r.counts, {})
        self.assertEqual(r.entropy_hits, [])

    def test_custom_allowlist(self):
        e = email("ops", "example.org")
        self.assertEqual(redact_text("x " + e, allowlist=[e]).text, "x " + e)
        self.assertEqual(redact_text("x " + e, allowlist=[]).text, "x " + marker("EMAIL"))

    def test_base64_with_secret_becomes_encoded(self):
        inner = ("filler text " * 14) + "password=" + tok("", 20) + " tail"
        b64 = base64.b64encode(inner.encode()).decode()
        self.assertGreaterEqual(len(b64), 200)
        r = redact_text("data: " + b64 + " end")
        self.assertEqual(r.text, "data: " + marker("ENCODED") + " end")
        self.assertEqual(r.counts, {"ENCODED": 1})

    def test_benign_base64_kept(self):
        b64 = base64.b64encode(("nothing sensitive here " * 12).encode()).decode()
        self.assertGreaterEqual(len(b64), 200)
        r = redact_text("data: " + b64)
        self.assertEqual(r.text, "data: " + b64)
        self.assertEqual(r.counts, {})


class TestPassesAndFiles(unittest.TestCase):
    def test_second_pass_catches_token_revealed_after_restore(self):
        # 'SMS' is allow-listed; protecting it hides the token from pass 1, restore reveals it.
        raw = "ghp_" + "SMS" + tok("", 33)
        r = redact_text("t " + raw + " end")
        self.assertEqual(r.text, "t " + marker("GITHUB_TOKEN") + " end")
        self.assertEqual(r.counts.get("SECOND_PASS"), 1)

    def test_markers_are_not_rematched(self):
        t = ("Authorization: Bearer " + tok("", 40) + "\n" + "https://u:" + tok("", 10) + "@h.example/p\n"
             + "password: " + tok("", 12) + "\n" + email() + "\n")
        first = redact_text(t)
        self.assertEqual(residual_matches(first.text), {})
        again = redact_text(first.text)
        self.assertEqual(again.text, first.text)
        self.assertEqual(again.counts, {})

    def test_counts_accurate(self):
        t = email("a") + " " + email("b", "example.net") + " tel " + eg_mobile() + " " + tok("ghp_", 36)
        r = redact_text(t)
        self.assertEqual(r.counts, {"EMAIL": 2, "PHONE": 1, "GITHUB_TOKEN": 1})

    def test_redact_file_raises_and_does_not_write(self):
        with tempfile.TemporaryDirectory() as d:
            src = Path(d) / "in.md"
            dst = Path(d) / "out" / "in.md"
            vaultlib.write_text(src, "x\n" + pem("RSA", 2, truncated=True))
            with self.assertRaises(RedactionIncomplete):
                redact_file(src, dst)
            self.assertFalse(dst.exists())

    def test_redact_file_writes_clean_output(self):
        with tempfile.TemporaryDirectory() as d:
            src = Path(d) / "in.md"
            dst = Path(d) / "out" / "in.md"
            vaultlib.write_text(src, "hi " + email() + "\r\nline\r\n")
            res = redact_file(src, dst)
            self.assertIsInstance(res, RedactResult)
            self.assertTrue(dst.is_file())
            raw = dst.read_bytes()
            self.assertFalse(raw.startswith(b"\xef\xbb\xbf"))
            self.assertNotIn(b"\r", raw)
            self.assertEqual(raw.decode("utf-8"), "hi " + marker("EMAIL") + "\nline\n")


def pem_head(kind: str = "RSA") -> str:
    return "-----" + "BEG" + "IN " + kind + " PRIV" + "ATE KEY-----"


class TestT143Phone(unittest.TestCase):
    """T14-3 (Q1): an explicit international number (``+`` + country code + 8-12 digits) is ALWAYS redacted -
    no keyword-context exception, no ``\\w`` lookbehind (Arabic / arrows / parens before ``+``), 9+ digits.
    The keyword-context exception stays for local numbers without ``+`` (ids / epochs)."""

    def test_intl_after_track_id_keyword_is_redacted(self):
        t = "track_id=ab12 \u0644\u0644\u0631\u0642\u0645 " + eg_mobile(cc="+2") + " end"
        r = redact_text(t)
        self.assertEqual(r.text, "track_id=ab12 \u0644\u0644\u0631\u0642\u0645 " + marker("PHONE") + " end")
        self.assertEqual(r.counts, {"PHONE": 1})

    def test_intl_in_tree_line_with_arrow_is_redacted(self):
        t = "SMS \u2192 " + eg_mobile(cc="+2") + " \u2705"
        r = redact_text(t)
        self.assertEqual(r.text, "SMS \u2192 " + marker("PHONE") + " \u2705")

    def test_intl_keyword_on_previous_line_is_redacted(self):
        t = "ts: 17\n" + eg_mobile(cc="+2") + "\n"
        self.assertEqual(redact_text(t).text, "ts: 17\n" + marker("PHONE") + "\n")

    def test_intl_preceded_by_arabic_letter_or_paren_is_redacted(self):
        for t in ("\u0631\u0642\u0645" + eg_mobile(cc="+2") + " x", "(" + eg_mobile(cc="+2") + ")"):
            with self.subTest(t=t):
                self.assertEqual(redact_text(t).counts, {"PHONE": 1})
                self.assertNotIn("1234", redact_text(t).text)

    def test_intl_nine_digits_is_redacted(self):
        t = "x +" + "44" + "1234567" + " y"
        self.assertEqual(redact_text(t).text, "x " + marker("PHONE") + " y")

    def test_intl_after_digit_is_redacted_zero_compromise(self):
        # ``9+123456789`` may be a sum, but the explicit '+' + 9 digits form is never left in place (Q1)
        r = redact_text("`1+" + "123456789" + "+2`")
        self.assertEqual(r.text, "`1" + marker("PHONE") + "+2`")

    def test_intl_glued_to_identifier_letter_not_matched(self):
        for t in ("C+" + "123456789", "x_+" + "123456789", "a++" + "123456789"):
            with self.subTest(t=t):
                self.assertEqual(redact_text(t).text, t)

    def test_bare_e164_egypt_without_plus_is_redacted(self):
        bare = "20" + eg_mobile(lead="")  # 201012345678 - E.164 without the plus sign
        for t in ("send to " + bare + " now", "`" + bare + "`", "[" + bare + "]"):
            with self.subTest(t=t):
                self.assertEqual(redact_text(t).counts, {"PHONE": 1})
                self.assertNotIn(bare, redact_text(t).text)

    def test_bare_e164_is_explicit_no_context_exception_and_underscore_ok(self):
        # explicit country code == explicit form: a phone used as a login id / inside a file name is still a phone
        bare = "20" + eg_mobile(lead="")
        for t in ("session_id: " + bare, "ID: `" + bare + "`", "sms_" + bare + "_out.txt"):
            with self.subTest(t=t):
                self.assertEqual(redact_text(t).counts, {"PHONE": 1})
                self.assertNotIn(bare, redact_text(t).text)

    def test_local_01x_keeps_keyword_context_exception(self):
        m = eg_mobile()
        self.assertEqual(redact_text("session_id: " + m).text, "session_id: " + m)

    def test_users_dir_without_drive_letter_is_normalized(self):
        for t in ("see `Users\\zz\\Documents\\x`", "folder Users\\zz here", "path \\Users\\zz\\a"):
            with self.subTest(t=t):
                r = redact_text(t)
                self.assertNotIn("zz", r.text)
                self.assertIn("~", r.text)
        self.assertEqual(redact_text("C:\\Users\\zz\\f").text, "~\\f")
        kept = "AllUsers\\zz stays"  # not a home dir: letters glued before 'Users'
        self.assertEqual(redact_text(kept).text, kept)

    def test_plus_form_counted_once_no_stray_plus(self):
        r = redact_text("to " + eg_mobile(cc="+2") + " .")
        self.assertEqual(r.text, "to " + marker("PHONE") + " .")
        self.assertEqual(r.pattern_counts.get("phone_international"), 1)
        self.assertIsNone(r.pattern_counts.get("phone_egypt_e164_bare"))


class TestT21Tuning(unittest.TestCase):
    """T2.1 — (a) PEM residue, (b) context_hint stripping, (c) URL_TOKEN / proxy / guards / exclusions."""

    # ---- (a) PRIVATE_KEY header without END
    def test_pk_header_mentioned_as_text_is_redacted_not_unresolved(self):
        t = "the engine matches " + pem_head() + " literally\nnext line\n"
        r = redact_text(t)
        self.assertEqual(r.text, "the engine matches " + marker("PRIVATE_KEY") + " literally\nnext line\n")
        self.assertFalse(r.unresolved_private_key)
        self.assertEqual(r.counts.get("PRIVATE_KEY"), 1)
        self.assertEqual(r.pattern_counts.get("pem_residue"), 1)
        self.assertEqual(residual_matches(r.text), {})

    def test_pk_header_followed_by_prose_keeps_prose(self):
        t = "x\n" + pem_head("EC") + "\nthis is prose, not base64\n"
        r = redact_text(t)
        self.assertEqual(r.text, "x\n" + marker("PRIVATE_KEY") + "\nthis is prose, not base64\n")
        self.assertFalse(r.unresolved_private_key)

    def test_pk_header_with_real_body_line_is_unresolved_and_body_removed(self):
        body = tok("", 64, _ALPHA + "+/")
        r = redact_text("x\n" + pem_head() + "\n" + body + "\nafter\n")
        self.assertTrue(r.unresolved_private_key)
        self.assertNotIn(body, r.text)
        self.assertEqual(r.text, "x\n" + marker("PRIVATE_KEY") + "\nafter\n")

    def test_pk_header_with_two_short_body_lines_is_unresolved(self):
        r = redact_text(pem_head() + "\nQUJD\nREVG\n")
        self.assertTrue(r.unresolved_private_key)
        self.assertNotIn("QUJD", r.text)

    def test_redact_file_writes_when_header_only_mentioned(self):
        with tempfile.TemporaryDirectory() as d:
            src, dst = Path(d) / "in.md", Path(d) / "out" / "in.md"
            vaultlib.write_text(src, "we grep for " + pem_head() + " in scans\n")
            res = redact_file(src, dst)
            self.assertTrue(dst.is_file())
            self.assertFalse(res.unresolved_private_key)
            self.assertNotIn("PRIV" + "ATE KEY", dst.read_text(encoding="utf-8"))

    # ---- (b) context_hint never leaks numbers >= 6 digits or path components
    def test_context_hint_masks_long_numbers(self):
        blob = tok("", 40)
        r = redact_text("123456789 " + blob)
        self.assertEqual(len(r.entropy_hits), 1)
        self.assertEqual(r.entropy_hits[0]["context_hint"], "<num>")
        r2 = redact_text("bot7654321 " + blob)
        self.assertEqual(r2.entropy_hits[0]["context_hint"], "<num>")

    def test_context_hint_masks_path_components(self):
        blob = tok("", 40)
        for prefix in ("~/bots/mybot ", "C:/proj/x ", "a\\b "):
            with self.subTest(prefix=prefix):
                r = redact_text(prefix + blob)
                self.assertEqual(r.entropy_hits[0]["context_hint"], "<path>")
        r = redact_text("api_token: " + tok("", 12) + "\n", collect_hints=True)
        for hc in r.hints.values():
            for k in hc:
                self.assertFalse(re.search(r"\d{6,}", k) or "/" in k or "\\" in k, k)

    # ---- (c) explicit URL_TOKEN instead of entropy
    def test_url_token_fragment_and_query(self):
        v = tok("", 32)
        r = redact_text("open https://app.example/magic#/token=" + v + " now")
        self.assertEqual(r.text, "open https://app.example/magic#/token=" + marker("URL_TOKEN") + " now")
        self.assertEqual(r.counts, {"URL_TOKEN": 1})
        r2 = redact_text("GET /cb?state=1&access_token=" + v + "&x=1")
        self.assertEqual(r2.text, "GET /cb?state=1&access_token=" + marker("URL_TOKEN") + "&x=1")
        self.assertIn("URL_TOKEN", CATEGORY_ORDER)

    def test_proxy_four_part_creds_redacted_bare_ip_port_kept(self):
        bare = "203.0.113.5:8080"
        r = redact_text("proxy " + bare + ":alpha:bravo99 end")
        self.assertEqual(r.text, "proxy " + bare + ":" + marker("URL_WITH_CREDS") + " end")
        self.assertEqual(redact_text("proxy " + bare + " end").text, "proxy " + bare + " end")
        r3 = redact_text("p.example.net:3128:alpha:bravo99")
        self.assertEqual(r3.text, "p.example.net:3128:" + marker("URL_WITH_CREDS"))

    def test_card_luhn_identifier_context_kept(self):
        valid = luhn_complete(_CARD_PARTIAL)
        for t in ("invoice " + valid, "order # " + valid, "tracking: " + valid, "chat_id=" + valid):
            with self.subTest(t=t):
                self.assertEqual(redact_text(t).text, t)
        self.assertEqual(redact_text("card " + valid).text, "card " + marker("PII"))

    def test_kv_placeholders_and_keyboard_chords_kept(self):
        for t in ("token: <your-token>", "API_KEY=${API_KEY}", 'secret = "{{ vault.secret }}"',
                  '"key": "ctrl+shift+p"', "password: %DB_PASSWORD%"):
            with self.subTest(t=t):
                r = redact_text(t)
                self.assertEqual(r.text, t)
                self.assertEqual(r.counts, {})
        r = redact_text("token: " + tok("", 12))
        self.assertEqual(r.counts, {"KV_SECRET": 1})

    def test_entropy_skips_markdown_anchors_and_link_targets(self):
        blob = tok("", 40)
        self.assertEqual(redact_text("see [x](#" + blob + ")").entropy_hits, [])
        self.assertEqual(redact_text("see [x](" + blob + ")").entropy_hits, [])
        self.assertEqual(len(redact_text("blob " + blob).entropy_hits), 1)

    def test_entropy_skips_public_build_ids(self):
        hex48 = _HEX * 3  # entropy exactly 4.0, not a sha40/sha64
        self.assertEqual(redact_text("next-action: " + hex48).entropy_hits, [])
        self.assertEqual(len(redact_text("digest " + hex48).entropy_hits), 1)
        self.assertEqual(len(redact_text("next-action token " + hex48).entropy_hits), 1)


if __name__ == "__main__":
    unittest.main()
