# SNAPSHOT.md — لقطة المصادر / Source snapshot

> ⚠️ **لقطة مأخوذة آلياً بتاريخ 2026-11-22T21:34:45Z (UTC)** بواسطة `tools/snapshot_db.py` v1.0.0 (لقطة واحدة متزامنة قبل أي تصدير — Q16). **لا تُعدَّل القيم يدوياً.** أي SHA-256 أو عدد هنا هو **المرجع الوحيد** لقبول T13–T16 (`exported + skipped == count(snapshot)`) ولا تُكتب أعداد كثوابت في الكود (Q3).
> EN: Snapshot taken automatically at 2026-11-22T21:34:45Z UTC by `tools/snapshot_db.py` v1.0.0; never edit the values by hand.

---

## 1. بيانات اللقطة / Snapshot metadata
- **تاريخ ووقت اللقطة (UTC):** `2026-11-22T21:34:45Z`
- **الطريقة:** `sqlite3.Connection.backup()` (يشمل WAL) إلى مجلد temp خارج الريبو، ثم فتح **النسخة** فقط عبر URI `mode=ro` بدون `immutable=1`.
- **الأداة / الإصدار:** `tools/snapshot_db.py` / `1.0.0`
- **عدد المصادر:** `4`

## 2. جدول المصادر / Sources

| المصدر | النوع | SHA-256 المصدر قبل النسخ | SHA-256 المصدر بعد النسخ | متطابق؟ | SHA-256 النسخة | عدد الجداول | إجمالي الصفوف | الحجم (bytes) |
|---|---|---|---|---|---|---|---|---|
| antigravity — conversation_summaries | sqlite | `conversation_summaries.db`: `48ff19196a7cf5d008ddb4440a0ae92454a938d496c09a4ff3cace4e94443b64`<br>`conversation_summaries.db-shm`: `fd4c9fda9cd3f9ae7c962b0ddf37232294d55580e1aa165aa06129b8549389eb`<br>`conversation_summaries.db-wal`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `conversation_summaries.db`: `48ff19196a7cf5d008ddb4440a0ae92454a938d496c09a4ff3cace4e94443b64`<br>`conversation_summaries.db-shm`: `fd4c9fda9cd3f9ae7c962b0ddf37232294d55580e1aa165aa06129b8549389eb`<br>`conversation_summaries.db-wal`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | True | `e4be6a66bd14be5fa3ca0d17bef6d5601caf63170a8b1f80a855693793274a44` | 9 | 33,590 | 120,463,360 |
| antigravity — antigravity_fts | sqlite | (جدول `conversations_fts` داخل conversation_summaries.db — نفس اللقطة) | ↑ | ↑ | ↑ | 1 | 3,268 | ↑ |
| opencode | sqlite | `opencode.db`: `c53fdfaf10b0d92f50779b1f8ea0ecd02ddb2d5d06a4f6e6af5ee015e94eb9b7`<br>`opencode.db-shm`: `7064972ba4d863e4df689b774fb3de9db3bf8cc9eed6bbe52dd1a6bf2bf1f3e5`<br>`opencode.db-wal`: `007794000335d292368c0435db8b9690057869e28c37aee7e229faea18a918de` | `opencode.db`: `c53fdfaf10b0d92f50779b1f8ea0ecd02ddb2d5d06a4f6e6af5ee015e94eb9b7`<br>`opencode.db-shm`: `7064972ba4d863e4df689b774fb3de9db3bf8cc9eed6bbe52dd1a6bf2bf1f3e5`<br>`opencode.db-wal`: `007794000335d292368c0435db8b9690057869e28c37aee7e229faea18a918de` | True | `d2d6b5bc2325d3dcf97c089b9aab07f03b9380de84a27105cdbe34bc6e4e4891` | 24 | 4,120 | 71,067,792 |
| LEDGER | json | `a54580ede7eb5722def265f5651f2a263cdb0b331c13c0f2dc96278b7dcd4186` | `a54580ede7eb5722def265f5651f2a263cdb0b331c13c0f2dc96278b7dcd4186` | True | `a54580ede7eb5722def265f5651f2a263cdb0b331c13c0f2dc96278b7dcd4186` | 453 | 5,436 | 10,503,122 |
| FORENSIC (تكرار LEDGER — لا يُصدَّر، Q5) | json | `4b2b5ac291a10743660d214baf2474326b90e9997f385170480648d31028d7ea` | `4b2b5ac291a10743660d214baf2474326b90e9997f385170480648d31028d7ea` | True | `4b2b5ac291a10743660d214baf2474326b90e9997f385170480648d31028d7ea` | 1 | 453 | 10,570,976 |

### 2.1 أعداد الصفوف لكل جدول / Per-table row counts

| المصدر | الجدول | الصفوف |
|---|---|---|
| conversation_summaries | conversation_parents | 0 |
| conversation_summaries | conversation_summaries | 701 |
| conversation_summaries | conversations_fts | 3,268 |
| conversation_summaries | conversations_fts_config | 1 |
| conversation_summaries | conversations_fts_content | 3,268 |
| conversation_summaries | conversations_fts_data | 14,540 |
| conversation_summaries | conversations_fts_docsize | 3,268 |
| conversation_summaries | conversations_fts_idx | 8,543 |
| conversation_summaries | search_schema_version | 1 |
| opencode | account | 0 |
| opencode | account_state | 0 |
| opencode | automation | 0 |
| opencode | blob | 0 |
| opencode | blob_ref | 0 |
| opencode | control_account | 0 |
| opencode | credential | 0 |
| opencode | event | 0 |
| opencode | event_sequence | 141 |
| opencode | instruction_blob | 46 |
| opencode | instruction_entry | 0 |
| opencode | instruction_state | 138 |
| opencode | job | 1 |
| opencode | kv | 4 |
| opencode | migration | 62 |
| opencode | permission | 0 |
| opencode | project | 16 |
| opencode | project_directory | 0 |
| opencode | session_inbox | 1 |
| opencode | session_message | 3,570 |
| opencode | session_part | 0 |
| opencode | session_v2 | 139 |
| opencode | workspace | 0 |
| opencode | worktree | 2 |
| ledger | files | 453 |
| ledger | top_level_items | 5,436 |
| ledger | parse_failures | 0 |
| ledger | denied_by_name | 0 |
| forensic | files | 1 |
| forensic | top_level_items | 453 |
| forensic | parse_failures | 0 |

## 3. أعداد التصدير / Export counts (تُملأ بعد T13–T16)

| المصدر | count(snapshot) | exported | skipped | exported + skipped == count | مجلد الناتج |
|---|---|---|---|---|---|
| summaries (T13) | 701 | 701 | 0 | True | `conversations/summaries/` |
| antigravity (T14) | 3,268 مقطعاً / 565 محادثة | 3,268 / 565 | 0 / 0 | True (chunks) · True (conv) | `conversations/antigravity/` |
| opencode (T15) | 139 جلسة / 3,570 رسالة | 137 / 1,883 | 2 / 1,687 | True (sessions) · True (msgs) | `conversations/opencode/` |
| ledger (T16) | 453 ملفاً / 5,436 عنصراً (FORENSIC مكرر 100% — لم يُصدَّر، Q5) | 453 / 5,436 | 0 / 0 | True (files) · True (items) | `conversations/ledger/` (5 أجزاء JSON ≤ 2 MB + `ledger.parts.json` + `AUDIT.md` + `SUMMARY.md`) |

## 4. ملاحظات / Notes
- `skipped` يجمع: denylist (DENY_READ/DENY_COPY)، `SKIPPED_SENSITIVE`، dedupe، الحجم، binary — التفصيل في manifest كل مصدر تحت `_local/manifests/`.
- تُحذف نسخ الـ temp بعد T21.
- EN: `skipped` aggregates denylist, sensitive, dedupe, size and binary skips; per-source manifests hold the detail; temp copies are deleted after T21.
