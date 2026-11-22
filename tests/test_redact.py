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


if __name__ == "__main__":
    unittest.main()
