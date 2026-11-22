# PLAN.md — Portable AI Memory Vault (`my-agent-memory-AGENTS-OpenCode-Open-Code`)

> **الحالة:** **v3 — معتمدة** (planning_round = 3, plan_approved = true) بعد قرارات المالك في `OWNER_DECISIONS_R2.md`.
> **بوابة `critic` (LENS: scope-guard):** `VERDICT: PASS_WITH_MAJORS` — 3 Majors مدمجة: T0 بلا تعقيم/عينات (dry-run الأنماط → T2)، T0 يفتح نسخة temp بـ `mode=ro&immutable=1` مع hash قبل/بعد، T1 ليست 🔴 بينما T18/T19 🔴.
> **المالك:** زيزو (PHOENIX-9941) · **البوصلة:** Antigravity (commit + push لكل مرحلة) · **المخطط:** Claude Fable 5.1 Planner · **المنفذ:** `executor` (`ses_dfccd9a45ffetJWzftCFzrgxDK`) · **الناقد:** `critic`
> **المستودع العام:** https://github.com/wewe00220033/my-agent-memory-AGENTS-OpenCode-Open-Code.git
> **قيود الجلسة:** لا `question`، لا `git push`/`commit` من المخطط أو المنفذ (البوصلة فقط). `run_tests.cmd` موجود (أنشأته البوصلة).

---

## 0. الهدف في سطرين
خزنة ذاكرة عامة: أي وكيل (OpenCode / Antigravity / أي أداة) يأخذ رابط الريبو، يقرأ **`AGENTS.md` = الزتونة** (Bootloader مضغوط عالي الكثافة، عربي + إنجليزي) فيعرف المالك وأسلوبه وقواعده ومهاراته وقراراته وأين يبحث في الذاكرة والمحادثات — **بدون أي مفتاح/توكن/باسورد/إيميل/هاتف/PII**. الأولوية المطلقة للمالك: *"المفاتيح والتوكنات والإيميلات والباسوردات ما تترفعش — أي حاجة تانية مش فارقة"*. الأولوية الثانية: **أقل مساحة** مع بقاء كل شيء مقروءاً ومقسماً.

## 1. النطاق
| يدخل | يُستبعد |
|---|---|
| القواعد (`GEMINI.md`, `config/rules/*.md`)، الـ Workflows (2)، أوامر OpenCode (2)، المهارات (23) | أكواد المشاريع (Source Code)، أرشيفات مكررة |
| ذاكرة/Handoffs/سجلات `Root/` و`.agents/memory/` (بدون ملفات `DENY_READ`) | أي ملف `DENY_READ`؛ `.db`/`.pb` كملفات (تُقرأ من backup مؤقت فقط) |
| **كل** المحادثات بلا استثناء تاريخي (Q7): summaries + `conversations_fts` + `opencode.db` + LEDGER/FORENSIC | tool outputs (Q11) و reasoning (Q12) في جلسات OpenCode — تُسقَط كلياً |
| كل الـ Brain (96 + 1,255) بعد dedupe SHA-256 آلي (Q2) | Protobuf `steps` (Q3 — النص مغطّى بالمصادر الثلاثة) |
| `tools/` + `tests/` نظيفة عامة بلا مسارات/أسرار محلية (Q10) | `_local/` (تقارير الاستكشاف والـ manifests الخام) — في `.gitignore` |

## 2. هيكل المستودع
```text
AGENTS.md                  # الزتونة: Bootloader مضغوط ثنائي اللغة — بلا سقف صلب (تحذير فقط > 64 KB)
README.md                  # تعريف + سياسة الأمان + "ما غير موجود هنا" + سطر الترخيص (Q8) + كيف تُحدَّث
INDEX.json                 # فهرس آلي: path, title, bytes, source, date, tags, redacted(bool)
SNAPSHOT.md                # تاريخ/hash/أعداد لقطة القواعد (Q16) — يُحدَّث في S3
.gitignore · .gitattributes
profile/   OWNER_PROFILE.md · DECISIONS.md · MISTAKES.md · ANCHORS.md
rules/  workflows/  commands/  skills/INDEX.md + skills/<name>/SKILL.md
memory/    INDEX.md · gateway-service/ · bolla-agentic-os/ · sms-root/ · scratch/
conversations/
  INDEX.md · index/<source>-<YYYY>.md
  summaries/YYYY-MM.md · antigravity/YYYY-MM/<id>.md (+unknown-date/) · opencode/YYYY-MM/<id>.md
  ledger/   # LEDGER ∪ FORENSIC بعد إزالة التكرار بينهما → أجزاء ≤ 2 MB JSON-صالحة + parts.json (Q5)
  audit/
brain/     INDEX.md · antigravity/ · antigravity-ide/
tools/     redact.py · patterns.json · denylist.json · snapshot_db.py · discover_schema.py
           export_summaries.py · export_antigravity_fts.py · export_opencode.py · export_ledger.py
           copy_sources.py · shard.py · build_index.py · verify_no_secrets.py · vaultlib.py (مشترك: io/utf8/manifest)
tests/     test_redact · test_denylist · test_shard · test_repo_clean · test_sizes · test_index_links · test_verify_negative
run_tests.cmd              # موجود (البوصلة) — unit: redact/denylist/shard · all: discover + verify_no_secrets
_local/                    # غير مرفوع: T0_SCHEMA_REPORT.md، manifests خام، entropy_hits.json
```
**مبدأ Q3:** بنية مرنة — السكربتات تقرأ الأعمدة والجداول من `sqlite_master` ديناميكياً (لا أسماء أعمدة ثابتة مكتوبة يدوياً إلا بعد تأكيدها في T0)، والأعداد المرجعية تأتي من `SNAPSHOT.md` لا من ثوابت.

### 2.1 `AGENTS.md` — الزتونة (Q4)
- **لا سقف صلب.** `test_sizes` يحذّر فقط > 64 KB. المعيار: **كثافة عالية، صفر حشو** — كل سطر إما قاعدة أو قرار أو مسار.
- **ثنائي اللغة:** كل قسم = عنوان EN + محتوى عربي مضغوط + سطر EN summary، بحيث يفهمه أي وكيل في العالم.
- **الأقسام:**
  1. `# WHO / من أنا` — زيزو / PHOENIX-9941، اللهجة المصرية، Zero-Guessing، Zero-Magic-Keywords، Zero-Compromise في الأمان، كيف يتعامل معه أي وكيل.
  2. `# CORE RULES / القواعد الأساسية` — **خلاصة مضغوطة فعلية** لأهم قواعد `GEMINI.md` + `rules/` (ليست روابط فقط) + روابط التفصيل.
  3. `# HOW I WORK / طريقة شغلي` — الأدوار (المالك/البوصلة/المخطط/المنفذ/الناقد)، الدفعات، بوابات الاختبار، كلمة `تابع`.
  4. `# SKILLS & COMMANDS` — جدول مضغوط للـ 23 مهارة (اسم + ≤ 10 كلمات) + commands/workflows.
  5. `# DECISIONS & MISTAKES` — أهم القرارات والأخطاء المتكررة (Top-N) + روابط `profile/`.
  6. `# MEMORY MAP` — لكل مشروع: سطر وصف + أحدث HANDOFF/PROGRESS.
  7. `# CONVERSATIONS — search, don't read` — بنية المجلدات، كيف تبحث (grep بالتاريخ/الكلمة)، `INDEX.json` schema.
  8. `# BRAIN` — ما هو وكيف تستخدمه.
  9. `# NOT HERE / ما غير موجود` — كود المصدر، الأسرار، tool outputs، reasoning، Protobuf.
  10. `# SECURITY` — علامة `[REDACTED:<CATEGORY>]`، لا تطلب قيمة معقّمة، الإيميلات/الهواتف كلها معمّاة.
  11. `# MAINTENANCE` — `tools/`، `run_tests.cmd`، `SNAPSHOT.md`، الرفع مرحلة بمرحلة.
- الجداول الآلية بين `<!-- AUTO-INDEX:START/END -->` من `build_index.py`؛ النص اليدوي خارجها. يُكتب v1 في T7 ويُكثَّف نهائياً في T20.

## 3. سياسة الأمان (Zero Compromise)
### 3.1 `tools/denylist.json` — طبقتان
- **`DENY_READ`** (لا تُفتح أبداً): `keys.md`, `keys.txt`, `keys*`, `*.env`, `.env*`, `oauth_creds.json`, `google_accounts.json`, `upstage_session.json`, `*accounts*.json`, `*.session`, `*.har`, `ACCOUNT_FUNDING_REGISTER.md`, `service.json`, `unlimited-identity.json`, `*.pem`, `*.key`, `*.p12`, `*.pfx`, `*.jks`, `*.keystore`, `*.ppk`, `id_rsa*`, `.netrc`, `.npmrc`, `.pypirc`, `.git-credentials`, `*.gpg`, `*.asc`, `kubeconfig*`, `*.ovpn`, `wallet*`, `seed*`, `mnemonic*`, `*secret*`, `*cred*`, `*password*`, `credentials*.json`, `token*.json`, `*.cookies*`, `*.log`؛ وأي ملف تحت `secrets/`, `.ssh/`, `.aws/`, `.gnupg/`.
- **`DENY_COPY`** (تُقرأ من backup فقط): `*.db`, `*.sqlite*`, `*.pb`, `*-wal`, `*-shm`.
- تُطبَّق على الاسم والمسار الكامل (case-insensitive) في `copy_sources.py` + `.gitignore` + `test_denylist`/`test_repo_clean`.

### 3.2 `tools/redact.py`
- **API:** `redact_text(text) -> RedactResult` بالحقول `text`, `counts`, `entropy_hits`, وعلم منطقي `unresolved_private_key`؛ و`is_denied_path(path, layer)`. stdlib فقط.
- **الفئات (كل نمط له حالة اختبار، fixtures مركّبة وقت التشغيل ضد Push Protection):**
  (الأنماط الحرفية لكل فئة موجودة في `tools/patterns.json` — المصدر الوحيد للحقيقة منذ T2؛ هنا الوصف فقط حتى لا تُلتقط الوثيقة نفسها بالفاحص.) `API_KEY` (بوادئ مزوّدي الخدمات الشائعة: OpenAI، Google، Upstage، Slack، AWS، Stripe، SendGrid، Twilio، HuggingFace، npm، Azure Storage، Supabase، Firebase، Telegram bot) · `KV_SECRET` (أزواج مفتاح/قيمة في JSON/YAML/.env/هيدرز HTTP حين يدل اسم المفتاح على سرّ — تُعمَّى القيمة فقط) · `GITHUB_TOKEN` · `OAUTH_JWT` (توكنات Google OAuth، JWT، Bearer) · `WEBHOOK` (Slack/Discord) · `PRIVATE_KEY` (كتل PEM من BEGIN إلى END) · `URL_WITH_CREDS` (أي scheme، تُعمَّى بيانات المستخدم فقط) · **`EMAIL`** (قياسي + مموّه `[at]`/`(at)`/`[dot]`) → `[REDACTED:EMAIL]` **كاملة دائماً (Q1)** · **`PHONE`** (مصري `(\+2)?0?1[0125][\s-]?\d{3}[\s-]?\d{4}[\s-]?\d{0,2}` + دولي `\+\d{10,15}`؛ استثناء الملاصق لـ `time|ts|id|created|epoch|_at|version` و13-digit epochs) → `[REDACTED:PHONE]` · **`PII`** (رقم قومي 14 رقم، IBAN `EG\d{27}`، بطاقات Luhn 13–19) (Q13) · `PATH` (تطبيع كل صيغ الهوم → `~`؛ مسار يحوي اسماً من `DENY_READ` → `[REDACTED:PATH]`) (Q14) · `ENCODED` (base64 ≥ 200 يُفكّ ويُفحص؛ تطابق → الكتلة كلها تُعمَّى) · `HIGH_ENTROPY` (≥ 32 حرفاً، Shannon ≥ 4.0، استثناء hex40/hex64/UUID بلا كلمة مفتاحية قبلها) → **تسجيل في `_local/entropy_hits.json` + manifest فقط، بلا تعمية آلية (Q18)**.
- **Allowlist (بعد التعقيم):** `زيزو`, `PHOENIX-9941`, أسماء المشاريع (`gateway-service`, `Bolla-Agentic-OS-EGM-SRE`, `SMS`…) (Q1/Q14). الأرقام التجارية/المالية خارج التعقيم (Q15).
- **سياسة الإسقاط (Q6 — جديدة):** **لا تُسقَط محادثة/ملف لمجرد احتواء أسرار** — تُعمَّى كلها وتُصدَّر نظيفة. الاستثناءان الوحيدان: (أ) ملف من `DENY_READ` (لا يُفتح أصلاً)، (ب) `unresolved_private_key = true` أي بقيت كتلة `PRIVATE KEY` غير مكتملة التعمية بعد التمريرة الثانية → يُسقَط ويُسجَّل `SKIPPED_SENSITIVE` بعنوان معقّم.
- **تمريرتان:** تعقيم → إعادة فحص الناتج بنفس الأنماط؛ أي تطابق متبقٍ = فشل كتابة الملف (لا كتابة لنص غير نظيف أبداً).

### 3.3 بوابة التحقق (`run_tests.cmd` — أنشأته البوصلة)
- `unit` → `test_redact` + `test_denylist` + `test_shard`. `all` → discover كل `tests/test_*.py` + `tools/verify_no_secrets.py`.
- `verify_no_secrets.py` يفحص: `git ls-files` + `git ls-files --others --exclude-standard` + `git log -p` (كل التاريخ) + `git log --format=%ae` = `wewe00220033@users.noreply.github.com` فقط (Q17) + لا `.db`/`-wal` في الشجرة + لا ملف `DENY_READ`.
- `test_verify_negative`: سر مزيّف في temp يجب أن يُفشل الفاحص. `tests` تستورد `tools.*` من جذر الريبو (namespace packages).
- **القاعدة:** لا تسليم مرحلة للبوصلة بدون `run_tests.cmd all` = 100% + مراجعة `entropy_hits` (Q18).

### 3.4 سياسة Git — مرحلة بمرحلة (Q9/Q17)
- بعد اعتماد كل مرحلة (S0…S5): المخطط يسجل `[STAGE_APPROVED <id>]` في `DUET_LOG.md` ويتوقف → **البوصلة** تفحص وتعمل commit نظيف بهوية `noreply` + `git push` → ثم تبدأ المرحلة التالية.
- لأن التاريخ يُدفع تدريجياً: `verify_no_secrets` يمسح `git log -p` في كل مرحلة؛ أي اكتشاف لاحق → `git filter-repo` بواسطة البوصلة فوراً.
- المخطط والمنفذ: **لا commit ولا push إطلاقاً.**

## 4. التفريغ والتقسيم (مرن — Q3)
- **T0 أولاً** (قراءة فقط — **بلا أي تعقيم أو عينات نصية**): `discover_schema.py` ينسخ بايتات كل `.db` (+ `-wal`/`-shm` إن وُجدت) إلى temp خارج الريبو، يسجل SHA-256 للمصدر **قبل وبعد** (يجب أن يتطابقا = دليل "لا تعديل لأي مصدر")، ثم يفتح **النسخة** فقط عبر URI `mode=ro&immutable=1` ويطبع `sqlite_master` + الأعمدة + الأنواع + أعداد الصفوف + إحصاءات أطوال النصوص (min/avg/max) لكل جدول للقواعد الثلاث — **بدون طباعة أي محتوى نصي خام**. ويفحص بنية LEDGER/FORENSIC (المفاتيح العليا، عدد العناصر، نسبة التكرار بالـ id/hash) → `_local/T0_SCHEMA_REPORT.md`. (الأعداد هنا استرشادية؛ المرجع النهائي لقطة T12.) **تجربة الأنماط على عينة تُنقل إلى T2** (dry-run بعد بناء `redact.py`).
- **القراءة الآمنة:** `snapshot_db.py` → `sqlite3.Connection.backup()` (يشمل WAL) إلى `%LOCALAPPDATA%\Temp\opencode\vault-snapshot\` + SHA-256 + أعداد → `SNAPSHOT.md` (لقطة واحدة متزامنة في بداية S3 — Q16). الفتح بـ `mode=ro` عبر URI **بدون `immutable=1`** (T0 أثبت أن immutable يُسقط آخر سجلات الـ WAL في opencode: 2,739 بدل 2,754 رسالة). حذف النسخ بعد T21.
- **نتائج T0 المعتمدة (`_local/T0_SCHEMA_REPORT.md`):**
  - `conversation_summaries` (699): الحقول المفيدة `conversation_id, title, preview, step_count, last_modified_time, workspace_uris, agent_name, parent_conversation_id, nesting_depth, raw_summary(BLOB)`. `source/group_id/battle_id` فارغة دائماً → لا تُصدَّر.
  - `conversations_fts`: FTS5 عادي (SELECT مباشر)، 3,255 صف، الترتيب `GROUP BY conversation_id ORDER BY chunk_index`، النص في `user_body` + `agent_body` (أقصى ~350 KB/مقطع)، + `title/workspace/project/last_modified_time`.
  - `opencode.db`: `session_part` **فارغ** — الأجزاء مضمّنة في `session_message.data` JSON تحت `content[]` بـ `type ∈ {text, reasoning, tool}` → T15 يستخرج `type == text` فقط (Q11/Q12). الترتيب `seq`، الزمن `time_created` epoch-ms. `session_message.type` يشمل `user/assistant/system/synthetic/idle/agent-switched/model-switched/compaction` → يُصدَّر `user` و`assistant` فقط. 125 جلسة (15 فرعية بـ `parent_id`).
  - `conversations/*.db` (500 ملف، 5.96 GB): Protobuf بلا schema → Q3 مؤجل مُبرَّر.
  - **FORENSIC_DATABASE = تكرار 100% لـ LEDGER** (453/453 بـ SHA-256) → T16 يصدّر LEDGER فقط ويذكر ذلك في `conversations/INDEX.md` (Q5 — أقل مساحة).
  - **الـ Brain الحقيقي ضخم:** `antigravity/brain` 38,127 ملف/1.78 GB (172 `.md`)، `antigravity-ide/brain` 62,050 ملف/4.44 GB (1,528 `.md`، 19,375 اسم ممنوع منها `.har`/`credentials`/`accounts_*.json`) → **T18/T19 تقتصر صراحةً على `*.md` فقط** + denylist على المسار الكامل.
  - ممنوعات بالاسم مؤكدة في gateway Root: `keys.md`, `keys.txt`, `crawler_user.session`, `ACCOUNT_FUNDING_REGISTER.md`؛ في Bolla: `keys.example.txt` — كلها تُرفض بـ `DENY_READ`.
  - القواعد حيّة: `-wal` لـ conversation_summaries تغيّر أثناء 22 ثانية (الملف الرئيسي ثابت) → يؤكد لقطة T12.
- **المخرجات:** summaries شهر/ملف · antigravity ملف/محادثة (تاريخ من join وإلا `unknown-date/`) · opencode ملف/جلسة (نص user/assistant فقط؛ الجلسات الفرعية تحت الأب) · ledger: دمج LEDGER ∪ FORENSIC بإزالة التكرار (hash للمحتوى/المعرّف) ثم أجزاء JSON-صالحة ≤ 2 MB + `parts.json` (Q5) · brain: NFC + تعقيم + dedupe SHA-256، الاحتفاظ بالأحدث وتسجيل المكررات.
- **`shard.py`:** JSON عند عناصر المصفوفة/المفاتيح العليا، Markdown عند `\n## `/حدود السجل؛ قياس بالبايت UTF-8. `.md` ≤ 1 MB، `.json` ≤ 2 MB، منسوخ كما هو ≤ 5 MB (صلب).
- **توفير المساحة:** إزالة الأسطر الفارغة المتكررة والمسافات الزائدة، لا تكرار للـ front-matter، لا نسخ مزدوج بين summaries والمحادثات (الملخص يُدمج كسطر header في ملف المحادثة إن وُجد).
- أسماء ملفات sanitized + `core.longpaths`؛ كل `open()` utf-8/`\n`/بلا BOM. كل سكربت idempotent + `manifest.json` (العدد، hash، التعقيمات/فئة، entropy_hits، المرفوض بالاسم). القبول العددي: `exported + skipped == count(snapshot)`.

## 5. المراحل والمهام
> **🔴** = تاسك واحد/دفعة + dry-run + تقرير أعلى 20 ملف تعقيماً قبل الكتابة. **كل مرحلة تنتهي ببوابة:** `run_tests.cmd all` + مراجعة entropy_hits + (critic في S0/S5) → `[STAGE_APPROVED]` → البوصلة commit+push.

### S0 — الاستكشاف والهيكل وبوابة الأمان
- **T0** (قراءة فقط للمصادر) `tools/discover_schema.py` + `_local/T0_SCHEMA_REPORT.md` + `.gitignore` أولي يحوي `_local/` فقط. *قبول:* (أ) التقرير يذكر الجداول/الأعمدة/الأنواع/أعداد الصفوف/إحصاءات الأطوال للقواعد الثلاث + بنية LEDGER/FORENSIC ونسبة التكرار؛ (ب) **SHA-256 لكل ملف مصدر قبل وبعد متطابق** مسجَّل في التقرير؛ (ج) الفتح من نسخة temp فقط عبر `mode=ro&immutable=1`؛ (د) **صفر محتوى نصي خام** في التقرير (أسماء أعمدة وأرقام فقط)؛ (هـ) لا كتابة خارج `_local/` و`tools/discover_schema.py` و`.gitignore`.
- **T1** `.gitignore` الكامل (DENY_COPY + `_local/` + temp) + `.gitattributes` + هيكل المجلدات بـ `.gitkeep` + placeholders لكل `INDEX.md` + `tools/vaultlib.py`. *قبول:* `run_tests.cmd unit` و`all` = exit 0.
- **T2 🔴** TDD: `tests/test_redact.py` (≥ 30 حالة) + `tests/test_denylist.py` + `patterns.json` + `denylist.json` + `redact.py` (تمريرتان + unresolved_private_key) + **dry-run الأنماط على عينة** (من نسخة temp للقواعد + ملفات md مختارة) → `_local/T2_PATTERN_DRYRUN.md` (أعلى 20 نمط hits + الإيجابيات الكاذبة المرصودة، بعدّادات فقط بلا نص خام). *قبول:* `unit` = 100%؛ فحص import ثابت = stdlib؛ تقرير dry-run موجود في `_local/`.
- **T3** `shard.py` + `test_shard.py`. *قبول:* `unit` = 100%.
- **T4** `verify_no_secrets.py` + `test_repo_clean` + `test_sizes` (تحذير AGENTS.md > 64 KB) + `test_index_links` + `test_verify_negative`. *قبول:* `all` ناجح والسلبي يُفشل الفاحص.
- **بوابة S0:** `critic LENS: scope-guard` (تمت على الخطة) → `[STAGE_APPROVED S0]` → البوصلة push.

### S1 — القواعد والمهارات + AGENTS.md v1
- **T5** `copy_sources.py` (تعقيم + طبقتا denylist + dedupe + manifest + dry-run). *قبول:* اختبار dry-run.
- **T6 🔴** نسخ `GEMINI.md`/rules/workflows/skills/commands + `skills/INDEX.md`. *قبول:* 23/3/2/2؛ `all` ناجح.
- **T7 🔴** `AGENTS.md` v1 (الأقسام 1–11 بخلاصة القواعد الفعلية) + `README.md` + `profile/OWNER_PROFILE.md` + هيكل `SNAPSHOT.md`. *قبول:* `test_index_links`؛ مراجعة المخطط للكثافة.
- **بوابة S1** → البوصلة push.

### S2 — الذاكرة والـ Handoffs (🔴 كلها)
- **T8 🔴** gateway-service → `memory/gateway-service/` (بدون CONVERSATIONS_*/LEDGER). **T9 🔴** Bolla → `memory/bolla-agentic-os/`. **T10 🔴** `D:\SMS` + scratch → `memory/sms-root/`, `memory/scratch/`. *قبول:* manifest يذكر المرفوض بالاسم؛ 0 ملف `DENY_READ` فُتح.
- **T11 🔴** `profile/DECISIONS/MISTAKES/ANCHORS.md` + `memory/INDEX.md`. *قبول:* `all` ناجح.
- **بوابة S2** → البوصلة push.

### S3 — تفريغ المحادثات (🔴 كلها)
- **T12 🔴** `snapshot_db.py` → لقطة متزامنة + `SNAPSHOT.md`. **T13 🔴** summaries. **T14 🔴** antigravity_fts. **T15 🔴** opencode (بلا tool outputs/reasoning). **T16 🔴** `export_ledger.py` (دمج + dedupe + أجزاء). *قبول:* `exported + skipped == count(snapshot)` لكل مصدر؛ `parts.json` يعيد التجميع؛ 0 tool parts.
- **T17** `conversations/INDEX.md` + `index/<source>-<YYYY>.md` + قائمة 20 مساراً عشوائياً + كل entropy_hits للمراجعة (critic/البوصلة). *قبول:* `all` ناجح؛ المراجعة موثقة.
- **بوابة S3** → البوصلة push.

### S4 — الـ Brain
- **T18 🔴** `brain/antigravity/` (96) اختبار دخان dedupe (dry-run + تقرير أعلى 20 ملف تعقيماً قبل الكتابة). **T19 🔴** `brain/antigravity-ide/` (الكل بعد dedupe — Q2؛ dry-run + تقرير قبل الكتابة). + `brain/INDEX.md`. *قبول:* `all` ناجح؛ manifest بالمكررات وعدّادات التعقيم.
- **بوابة S4** → البوصلة push.

### S5 — الفهرسة النهائية والتسليم
- **T20** `build_index.py` → `INDEX.json` + AUTO-INDEX + كل `INDEX.md` + **تكثيف `AGENTS.md` النهائي** (Q4). *قبول:* كل مسار موجود؛ صفر حشو.
- **T21 🔴** الفحص الشامل: `all` + حذف لقطات temp + لا `.db` + حجم الريبو + `git status` + تقرير. *قبول:* 0 أسرار.
- **بوابة S5:** `critic LENS: fish` → `[FINAL_APPROVED]` → البوصلة push نهائي.

## 6. الدفعات والتراجع
S0 تاسك/دفعة. 🔴 مفردة. العادي ≤ 3. `[توقف - تكرار مرتين]` أو `VERDICT: BLOCK` → تاسك واحد حتى تحققين ناجحين. `critic` ≤ 2/مرحلة. رفض ≤ 3/مرحلة ثم تصعيد.

## 7. معايير القبول العامة
1. `run_tests.cmd all` = 100% (مع السلبي). 2. أحجام §4. 3. لا ملف `DENY_READ`/`DENY_COPY` tracked أو untracked. 4. كل روابط `AGENTS.md`/`INDEX.md` صحيحة. 5. manifest لكل مخرج. 6. لا commit/push من المخطط/المنفذ. 7. entropy_hits مُراجَعة قبل كل تسليم.

## 8. المخاطر
| الخطر | التخفيف |
|---|---|
| سر يفلت من الأنماط | تمريرتان + ENCODED + entropy_hits مُراجَعة + `git log -p` كل مرحلة + `filter-repo` طوارئ |
| الدفع التدريجي يُسرّب تاريخاً | `verify_no_secrets` قبل كل تسليم + Push Protection كطبقة إضافية |
| تعقيم زائد يفسد كود/معرّفات | allowlist بعد التعقيم + استثناءات hex/UUID/epoch + اختبارات نص نظيف |
| WAL/قفل SQLite | `backup()` إلى temp |
| schema غير متوقع | T0 قبل أي سكربت + قراءة ديناميكية |
| حجم الريبو | إسقاط tool outputs/reasoning + dedupe + تقسيم + تنظيف المسافات |

## 9. القرارات المعتمدة (مرجع سريع)
Q1 إيميل/هاتف معمّاة كاملاً، الاسم ظاهر · Q2 brain كله dedupe · Q3 نص فقط، بنية مرنة · Q4 AGENTS.md زتونة مضغوطة ثنائية بلا سقف · Q5 ledger أقل مساحة ≤ 2 MB · Q6 تعقيم بلا إسقاط (إلا DENY_READ/مفتاح خاص غير قابل للتعمية) · Q7 ارفع كله · Q8 سطر في README · Q9 push مرحلة بمرحلة · Q10 tools/tests داخل الريبو · Q11 إسقاط tool outputs · Q12 حذف reasoning · Q13 PII معمّاة · Q14 أسماء المشاريع تبقى، الهوم → `~` · Q15 الأرقام التجارية تبقى · Q16 لقطة واحدة بداية S3 · Q17 noreply + push كل مرحلة · Q18 entropy للمراجعة فقط · Q19 `run_tests.cmd` من البوصلة.

## Open Questions for Owner
— لا أسئلة حاجبة. الخطة معتمدة.
