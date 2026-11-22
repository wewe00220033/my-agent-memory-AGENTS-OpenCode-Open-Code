# SNAPSHOT.md — لقطة المصادر / Source snapshot

> ⚠️ **هيكل فارغ** — يُملأ آلياً في **S3/T12** بواسطة `tools/snapshot_db.py` (لقطة واحدة متزامنة قبل أي تصدير — Q16). لا تعدّل القيم يدوياً. أي SHA-256 أو عدد هنا هو **المرجع الوحيد** لقبول T13–T16 (`exported + skipped == count(snapshot)`) ولا تُكتب أعداد كثوابت في الكود (Q3).
> EN: Empty skeleton, filled by `tools/snapshot_db.py` at the start of S3. Every value below is a placeholder (`-`) until then.

---

## 1. بيانات اللقطة / Snapshot metadata
- **تاريخ ووقت اللقطة (UTC):** `-`
- **الطريقة:** `sqlite3.Connection.backup()` (يشمل WAL) إلى مجلد temp خارج الريبو، ثم فتح **النسخة** فقط عبر URI `mode=ro` بدون `immutable=1`.
- **الأداة / الإصدار:** `tools/snapshot_db.py` / `-`
- **عدد المصادر:** `-`

## 2. جدول المصادر / Sources

| المصدر | النوع | SHA-256 المصدر قبل النسخ | SHA-256 المصدر بعد النسخ | متطابق؟ | SHA-256 النسخة | عدد الجداول | إجمالي الصفوف | الحجم (bytes) |
|---|---|---|---|---|---|---|---|---|
| antigravity — conversation_summaries | sqlite | - | - | - | - | - | - | - |
| antigravity — antigravity_fts | sqlite | - | - | - | - | - | - | - |
| opencode | sqlite | - | - | - | - | - | - | - |
| LEDGER | json | - | - | - | - | - | - | - |
| FORENSIC (تكرار LEDGER — لا يُصدَّر، Q5) | json | - | - | - | - | - | - | - |

### 2.1 أعداد الصفوف لكل جدول / Per-table row counts

| المصدر | الجدول | الصفوف |
|---|---|---|
| - | - | - |

## 3. أعداد التصدير / Export counts (تُملأ بعد T13–T16)

| المصدر | count(snapshot) | exported | skipped | exported + skipped == count | مجلد الناتج |
|---|---|---|---|---|---|
| summaries (T13) | - | - | - | - | `conversations/summaries/` |
| antigravity (T14) | - | - | - | - | `conversations/antigravity/` |
| opencode (T15) | - | - | - | - | `conversations/opencode/` |
| ledger (T16) | - | - | - | - | `conversations/ledger/` |

## 4. ملاحظات / Notes
- `skipped` يجمع: denylist (DENY_READ/DENY_COPY)، `SKIPPED_SENSITIVE`، dedupe، الحجم، binary — التفصيل في manifest كل مصدر تحت `_local/manifests/`.
- تُحذف نسخ الـ temp بعد T21.
- EN: `skipped` aggregates denylist, sensitive, dedupe, size and binary skips; per-source manifests hold the detail; temp copies are deleted after T21.
