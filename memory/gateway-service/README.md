# 🌐 OpenCode Browser Gateway & Upstage Smart Bridge v3.5

كوبري محلي ذكي (Local AI Gateway Bridge) لربط محرر وبيئة عمل **OpenCode** بنماذج الذكاء الاصطناعي القوية في **Upstage Studio** (مثل Claude Sonnet 5.5, GPT-5.4, Solar Pro 4) مع محاكي استدعاء الأدوات الميداني (Tool Emulation Engine) لدعم قراءة وتعديل الملفات وتشغيل أوامر الشل مباشرة كـ Autonomous Agent.

---

## ⚡ المميزات الرئيسية (Key Architecture)

1. **محاكي الأدوات المتطور (Tool Emulation Engine v3.5):**
   - تحويل استجابات النماذج التي تقترح تشغيل أدوات إلى معيارية OpenAI `tool_calls` متوافقة 100% مع OpenCode.
   - حقن بروتوكول سيادي صريح في مقدمة البرومبت لإلزام الموديل بصيغة `tool_call`.
   - مرونة كاملة في معالجة مسارات الويندوز (`\t` Tab-Resilience) لمنع انهيار JSON.

2. **عازل التسمية اللحظي (Instant Zero-Latency Titling Resolver):**
   - الرد اللحظي خلال 1ms على طلبات التسمية المتوازية من OpenCode دون لمس السيرفر السحابي، لمنع تداخل الجلسات وتصادم `_active_chat_id`.

3. **دعم أوضاع الأذونات (Permission Modes):**
   - `bypass`: تفعيل وضع **`⚡ Skip permissions`** افتراضياً لتنفيذ الأدوات وأوامر الملفات فوراً دون مقاطعة.
   - `auto`: وضع متوازن يسأل فقط عند العمليات الحرجة.
   - `manual`: وضع الحذر الذي يطلب الإذن قبل كل خطوة.

4. **بث حي فائق السرعة (SSE Streaming):**
   - دعم كامل لبروتوكول Server-Sent Events مع تزويد حقول `index` الدقيقة لمصفوفات الأدوات.

---

## 🚀 البدء السريع (Quick Start)

### 1. تثبيت المتطلبات:
```bash
pip install -r requirements.txt
```

### 2. ضبط الجلسة (Environment Variables):
انسخ ملف `.env.example` إلى `.env`:
```bash
cp .env.example .env
```
وقم بملء بيانات الجلسة:
- `UPSTAGE_SESSION_COOKIE`: كوكي الجلسة من `studio.upstage.ai`.
- `UPSTAGE_ORG_ID`: معرف المنظمة النشط.
- `UPSTAGE_PERMISSION_MODE`: الوضع المفضل (الافتراضي: `bypass` لتفعيل `Skip permissions`).

### 3. تشغيل الكوبري:
يمكنك التشغيل بنقرة واحدة عبر:
- `تشغيل_كوبري_ابستيج.bat`
أو من سطر الأوامر:
```bash
python upstage_opencode_bridge.py
```
سيعمل الخادم المحلي على: `http://127.0.0.1:8002/v1`

### 4. ربط OpenCode:
انسخ إعدادات `opencode.json` إلى مسار إعدادات OpenCode الخاص بك:
`~\.config\opencode\opencode.json`

---

## 🧪 التحقق والاختبار (Verification)

لاختبار استدعاء الأدوات والتأكد من استجابة Claude Sonnet 5.5 بـ `tool_calls` لأداة `write`:
```bash
python test_v35_bulletproof.py
```
المخرجات المتوقعة:
- استجابة سريعة لطلب التسمية في 1ms.
- إرجاع استدعاء أداة سليم مع `finish_reason: "tool_calls"`.

---

## 🔒 الأمان وحماية البيانات (Security Policy)
- الكوبري لا يقوم بحفظ أو تخزين أي مفاتيح أو أسرار داخل المستودع.
- كافة الجلسات والتوكنات تُدار حصرياً عبر متغيرات البيئة أو ملفات `.env` المحلية المستبعدة في `.gitignore`.


---

## 🏛️ تشغيل بروكسي LiteLLM الموحد (Port 4000)

تم تدشين طبقة LiteLLM الموحدة لدمج مزودي الويب غير القياسيين (Upstage + DeepAI) مع المزودين الرسميين (Groq / OpenAI) في بوابة واحدة:
- **المسار:** `litellm_bridge/`
- **التشغيل:** `python litellm_bridge/run_proxy.py` (أو باستخدام بايثون 3.12)
- **المنفذ:** `http://127.0.0.1:4000/v1`
- **المفتاح (Master Key):** `bolla-litellm-2026`
- **النماذج المتاحة:** `claude-fable-5-1`, `claude-sonnet-5-5`, `gpt-6.1-sol`, `auto`, `deepai/standard`, `groq/llama-3.3-70b-versatile`
- **صمامات الأمان:** Lookahead Token Buffer لمنع تسريب الماركداون، معالجة مسارات ويندوز `C:\`، ودعم كامل للـ SSE Streaming و Multi-turn Tool History.

---

## ⚙️ التحديث المرجعي الحي: Upstage Smart Bridge `v4.6_ultimate_governed` (بورت `8020`)

> **تنويه:** القسم العلوي يوثّق النسخة التأسيسية `v3.5` تاريخياً؛ التشغيل الحي الحالي يعتمد كلياً على **`v4.6_ultimate_governed`** (`http://127.0.0.1:8020/v1`) عبر `C:\Python315\pythonw.exe` بدون نافذة تيرمينال.

### 🌟 المعمارية والحوكمة الديناميكية في `v4.6`
1. **حوكمة خارجية بدون إعادة تشغيل (`bridge_config.json` + Hot-Reload):**
   - تُدار الموديلات (`13` موديلاً مسجلاً + اختصارات `aliases`)، المهل (`timeouts`)، `permission_mode`، وإعدادات `runtime` (`host`, `port`, `upstream_base_url`, `db_prune_days`, `max_locks_cached`) من [bridge_config.json](bridge_config.json) بتحديث لحظي عبر `mtime`.
   - حماية **Last-Known-Good:** أي خطأ JSON أو `schema_version` غير مدعوم يُرفض مع الاحتفاظ بآخر إعدادات سليمة بدون تعطل الخدمة.
   - **سياسة الأسرار:** يُحظر تماماً وضع أي كوكيز أو مفاتيح أو توكنات داخل `bridge_config.json` (يُرفض التحميل تلقائياً وتُدار الجلسات حصراً عبر `.env` أو `upstage_session.json` مع إعادة تحميل تلقائية عند تغييرها).
2. **نافذة المليون الحقيقية و`verbatim_full` + `StreamSanitizer`:**
   - سياق **`1,000,000`** توكن (`128K` out لـ Fable 5.1) مع تعطيل كل قصّ صامت (`allow_silent_trim: false`) وإثبات تشفيري `📊 [PROOF]` (`sha256_in == sha256_sent`).
   - ماسح `StreamSanitizer` المتوازن يفصل أوامر الأدوات بدقة CommonMark دون كسر أسوار الكود المتداخلة ودون تسريب وسوم Upstage (`<w...>`, `<doc...>`, `<!--CHOICES:...-->`).
   - مع `strict_models: false`، يمر أي موديل مستقبلي غير مسجل تلقائياً (`Dynamic Pass-Through`) بحدود `default_context_limit` / `default_output_limit`، وتُحل الاختصارات (`fable`, `sol`, `luna`, `terra`, `flash`, `mini`, إلخ) حتمياً عبر `aliases`.
3. **التشغيل الصامت ونقاط التحكم والاختبار:**
   - **تشغيل / إعادة تشغيل صامت:** `restart_bridge_silent.bat` أو `run_silent.vbs` (تعمل جميع المشغلات الصامتة عبر `run_silent.vbs`).
   - **فحص الصحة والتشخيص:** `GET http://127.0.0.1:8020/health` و`GET http://127.0.0.1:8020/v1/diagnostics` (مع `Authorization: [REDACTED:KV_SECRET]
   - **تصفير الجلسات:** `POST /v1/session/reset` يدعم تصفير جلسة واحدة (`{"session_id": "..."}` أو `{"session_key": "..."}`) مع تنظيف شاتاتها البعيدة وقفلهـا، أو تصفير الكل (`{"all": true}`).
   - **الاختبارات المعتمدة:**
     - اختبارات الوحدة (`20` اختباراً): `python fable_eval_lab\test_bridge_v4_unit.py`
     - الاختبار التكاملي الحي (`8` مراحل + تنظيف تلقائي): `python fable_eval_lab\test_live_v4_e2e.py`
4. **أرشيف النسخ والاستعادة الفورية:**
   - معاينة الاستعادة: `python bridge_versions\restore_version.py --to v4.6_ultimate_governed --dry-run`
   - عرض النسخ: `python bridge_versions\restore_version.py --list`
   - الاستعادة والتشغيل: `python bridge_versions\restore_version.py --to <version_dir> --restart`
   - الدليل المعماري وتاريخ الإصدارات الكامل: [bridge_versions/BRIDGE_VERSIONS_ARCHIVE_AND_AUDIT.md](bridge_versions/BRIDGE_VERSIONS_ARCHIVE_AND_AUDIT.md)

---

## 🧭 ترقية `v4.7_triad_governed` + نظام الثلاثي المعزول (`Dual-Fable Triad Pipeline`)

> **الإصدار الحي الحالي:** **`v4.7_triad_governed`** على `http://127.0.0.1:8020/v1` (`15` موديلاً مسجلاً + اختصارات `aliases`، ومعاملات حوكمة صريحة بدون ثوابت).

### 🔺 معمارية الثلاثي (`البوصلة + المخطط المراجع + المنفذ المستقل`)
1. **البوصلة والناقد (`Antigravity` + المالك):** يحتفظ بالسياق العام ومشاريع المالك، ويتفق مع المالك على الهدف ويُطلق الأوركسترا عبر `fable_duet.py`، ويبتّ في أي توقف عند `[NEEDS_OWNER_DECISION]`.
2. **شات المراجع والمخطط (`claude-fable-5-1-planner`):** معزول في جلسة `oc:planner:<id>` عبر [roles/planner.md](roles/planner.md). يكتب الخطة والمراحل وملف الاستئناف، يراجع مع المنفذ، ثم يكلّف ويدقق مرحلة بمرحلة ولا ينفّذ بنفسه أبداً.
3. **شات المنفذ المستقل (`claude-fable-5-1-executor`):** معزول في جلسة `oc:executor:<id>` عبر [roles/executor.md](roles/executor.md). في **المرحلة أ** ينقد الخطة بدون أي تنفيذ (`[EXECUTOR_FEEDBACK]`)، وفي **المرحلة ب** ينفذ المرحلة المكلف بها فقط ويرفع تقريره (`[EXEC_REPORT <id>]`).
4. **أوامر تشغيل الأوركسترا [`fable_duet.py`](fable_duet.py):**
   ```powershell
   # بدء دورة جديدة (أو --plan-only للتوقف بعد اعتماد الخطة)
   python fable_duet.py start --brief "وصف الهدف أو مسار ملف البريف" --work-dir duet_work

   # استئناف بعد قرار المالك عند التوقف على [NEEDS_OWNER_DECISION] (exit code 3)
   python fable_duet.py resume --owner-answer "القرار المعتمد من المالك" --work-dir duet_work

   # فحص الحالة أو تنظيف الشاتين والجلسات بعد الانتهاء
   python fable_duet.py status --work-dir duet_work
   python fable_duet.py clean --work-dir duet_work
   ```

### 🗝️ مرجع مفاتيح الحوكمة في [`bridge_config.json`](bridge_config.json)
```text
المفتاح                                  | الافتراضي      | الوظيفة والأثر
-----------------------------------------|----------------|------------------------------------------------------------
preserve_full_system_prompt              | true           | يمرر كامل System Prompt وقواعد المشروع بدون أي قص
max_project_instructions_chars           | 0              | 0 = بلا سقف (أي رقم > 0 يُسجل ⚠️ [CONFIG-CAP] عند تطبيقه)
max_tool_description_chars               | 0              | 0 = بلا قص لوصف الأدوات (0% حذف خفي)
compact_tool_schema                      | false          | يحفظ schemas الأدوات كاملة بما فيها وصف كل معامل
show_server_cut_notice                   | true           | يلحق تنبيه [SERVER-CUT] عند finish_reason=length دون تعديله
bridge_upstage_choices_to_question_tool  | true           | يحوّل كروت request_user_input التفاعلية إلى أداة question في OpenCode
choices_comment_mode                     | "strip"        | "strip" لإزالة <!--CHOICES:...--> أو "footer" لعرضها كاقتراحات
role_profiles_dir                        | "roles"        | مجلد ملفات أدوار المخطط والمنفذ (*.md)
account_profiles                         | {"default":..} | ربط أي موديل بحساب Upstage مختلف مستقبلاً بسطر كونفج واحد
```

---

## 🎯 ترقية `v4.9_self_healing_pool` — المعالجة الذاتية لاتصالات Upstage والوكلاء المعزولون (`planner` / `executor` / `critic`)

> **الإصدار الحي الحالي:** **`v4.9_self_healing_pool`** على `http://127.0.0.1:8020/v1` | **الدليل الشامل للتشغيل والطوارئ والاستئناف بكلمة `تابع`:** [docs/TROUBLESHOOTING_AND_PLAYBOOK.md](docs/TROUBLESHOOTING_AND_PLAYBOOK.md).

0. **الشفاء الذاتي لاتصالات HTTP واستئناف `"تابع"` (`v4.9`, `PID: 14904` | `sha=aeedbada4e82`):** تعيين `keepalive_expiry=15.0`، تدوير `_http_client` آلياً عبر `_recycle_http_client()` عند أي `TimeoutException` أو خطأ نقل أو أكواد `502/503/504`، وإعادة محاولة `POST /api/chats` حتى **3 مرات** (للاستثناءات وأكواد `429/502/503/504` بمهلة `30s`) مع عدادات `pool_recycles` و`consecutive_upstream_errors` في `/health` و[tools/bridge_doctor.py](tools/bridge_doctor.py)، وإضافة بروتوكول الاستئناف الذكي بكلمة واحدة **`تابع`** في [roles/planner.md](roles/planner.md).
1. **تكامل أداة OpenCode التفاعلية (`question` Tool):** يوجّه الكوبري النماذج تلقائياً عند وجود `question` ضمن الأدوات المعلنة لاستدعاء واجهة الاختيارات التفاعلية داخل OpenCode (`1/N .. N/N`، `3..K+` خيارات، Single أو `multiple: true`، مع حقل `"Type your own answer"` التلقائي من OpenCode).
2. **ترجمة كروت Upstage السحابية (`request_user_input`) تلقائياً:** إذا بعث Upstage حدث `request_user_input` سحابياً أو نطق الموديل كتلة `request_user_input`، يحوّلها الكوبري تلقائياً عبر `convert_upstage_requests_to_opencode_questions()` إلى أداة `question` التفاعلية مع التدوير التلقائي للشات السحابي (`needs_rotation`) أو قائمة Markdown مرقمة (`1/N .. N/N`) عند غياب الأداة.
3. **منظومة الوكلاء المعزولين داخل OpenCode (`2 دائم + 1 سفري بذاكرة صفرية` في `opencode.json` + [roles/](roles/)):**
   - إبقاء البوصلة `🧭` خارج OpenCode تماماً، وتشغيل **`📋 Claude Fable 5.1 (Planner & Reviewer)`** كـ Primary Agent (`planner-reviewer`: مالك ملفات التخطيط الأربعة، يستعمل `run_tests.cmd` فقط بدون شيل حر عبر `shell: * deny` وقائمة بيضاء حرفية، ويطبّق بوابة `"هل أنت متأكد؟"` وتقسيم `T1` ثم دفعات بالخطر حتى 5 مهام).
   - **`🛠️ Claude Fable 5.1 (Executor)`** كـ Subagent مستمر المعرّف (`executor`، معزول عن ملفات التخطيط الأربعة وعن `*run_tests.cmd`/`*fable_eval_lab*` ومعه فرامل `[توقف - تكرار مرتين]`).
   - **`🐟 Claude Fable 5.1 (Stateless Goldfish Critic)`** كـ Subagent سفري للقراءة فقط (`critic` على `claude-fable-5-1` بدون إضافة موديل رابع، بذاكرة صفرية بدون `sessionID`، ورد بـ `VERDICT: PASS|PASS_WITH_MAJORS|BLOCK` + أقصى 3 ملاحظات موثقة بـ `file:line`).
4. **الاختبارات المعتمدة حالياً:** **`30/30`** اختبار وحدة وقبول محمي للكوبري + **`30/30`** اختبار لأداة الفحص اليومية [tools/bridge_doctor.py](tools/bridge_doctor.py) + **`43/43`** لحزمة `duet_demo` (**إجمالي `103/103 OK`** عبر `tools\run_tests.cmd all`) + البروب الأحمر (**`6/6 permission.rejected`**) + الباج المزروع (**`VERDICT: BLOCK`**) + معاينة الاستعادة: `python bridge_versions\restore_version.py --to v4.9_self_healing_pool --dry-run`.
5. **القفل الميكانيكي للأدوار والتكيّف بالبلدي (`Round 73` | `sha=9b5858681103` | `PID 22368`):** تفعيل `_partition_role_tools` و`_check_role_tool_violation` داخل الكوبري لحماية دوري `planner` و`executor` ميكانيكياً حتى عند تشغيل OpenCode على وكيل `build` (منع كتابة/تعديل أي ملف غير ملفات التخطيط الأربعة للمخطط وتقييد `shell` بـ `run_tests.cmd [unit|all]` فقط مع رفض `&&`/`&`/`|`/`cmd /c`/تجاوز `workdir` عبر `_normalize_guard_path` + جولة تصحيح داخلية واحدة أو `hard-block` بلا تسريب في `stream`/`non-stream`، مع حماية `PLAN.md`/`DUET_LOG.md`/`TASKS.json`/`duet_resume.json`/`run_tests.cmd`/`fable_eval_lab`/`roles/*`/`opencode.json*`/`AGENTS.md`/`bridge_config.json`/`upstage_opencode_bridge.py` من المنفذ) + قواعد `"action": "write"` في نسختي `opencode.json` وفحصها في `tools/bridge_doctor.py` + سد ثغرة "الملف المؤقت" والتكيّف مع كلام المالك بالبلدي (`Zero Magic Keywords`) في [roles/planner.md](roles/planner.md) + إزالة مقدمة الوكلاء الفرعيين من عناوين Upstage (`[مخطط]` / `[منفذ]` / `[سمكة]`) مع إثبات حي (`role_guard_blocks: 0 → 2` وبروب ساندبوكس `build` `104.38s`) وحكم الناقد الصريح **`VERDICT: PASS`**.
