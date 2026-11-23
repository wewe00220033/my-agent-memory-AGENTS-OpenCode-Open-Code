# 📋 المرحلة 2: بناء make_capsule وبوابة السمكة

- id: `ses_e02886f3bffe0Pb1qeWsjkjqpI`
- title: 📋 المرحلة 2: بناء make_capsule وبوابة السمكة
- date: 2026-11-21 09:37:13
- directory: duet_demo
- agent: planner-reviewer
- messages: 16 (user 1, assistant 15)
- children: 2
  - 2026-11-21_Fish-gate-review-S3_qacxPewC.md
  - 2026-11-21_Review-S3-plan-only_bgHsakHL.md
- archived: false

## 6 · user (2026-11-21 09:37:13)

مرحباً! طلب معتمد مسبقاً من المالك (لا تستخدم أداة question إطلاقاً في هذه الجلسة التلقائية):
نريد تنفيذ المرحلة S3 داخل المشروع القائم `~\Downloads\zizo\duet_demo` لبناء أداة حقيقية تخدم منظومتنا: **`make_capsule.py`** (مولّد كبسولة الفحص الأوتوماتيكي لوكيل السمكة) + اختبارات **`test_make_capsule.py`**، مع تطبيق كامل بروتوكول المرحلة 2 (التقسيم المتدرج `T1` أولاً كاختبار نبض + التحقق حصراً عبر `~\Downloads\zizo\duet_demo\run_tests.cmd` + بوابة السمكة `critic` بدون `sessionID` في النهاية).

## المواصفات التقنية الدقيقة المطلوبة للأداة (`make_capsule.py` — مكتبة قياسية stdlib فقط، مخرجات ASCII/English بلا ألوان):
1. ثابت الوحدة: `VALID_LENSES = ("fish", "scope-guard", "forensic")`
2. دالة `build_capsule(plan_path, tasks_path, resume_path, log_path, lens="fish", stage=None, diff_summary=None, test_evidence=None, concern=None) -> str`:
   - تتحقق من `lens in VALID_LENSES` (وإلا ترفع `ValueError(f"invalid lens: {lens}")`).
   - تقرأ `plan_path` (بترميز `utf-8-sig`)، و`tasks_path` (كائن JSON بترميز `utf-8-sig`؛ JSON فاسد أو غير dict يرفع `ValueError` تذكر المسار)، و`resume_path` (عبر `duet_status.load_resume`)، و`log_path` (عبر `duet_status.parse_log`).
   - ترفع `FileNotFoundError` لأي ملف مفقود.
   - إذا لم تُمرَّر `stage`: تأخذها من `resume.get("current_stage")` أو آخر سجل، وإلا `"-"`.
   - تنتج كبسولة Markdown مضغوطة **بحد أقصى 40 سطراً** تبدأ بالسطرين:
     `# Inspection Capsule`
     `LENS: <lens>`
     متبوعةً بالأقسام الخمسة الحرفية:
     `## 1. Goal` (ملخص قصير من `PLAN.md` واسم المشروع)
     `## 2. Constraints` (ملخص القيود ومعايير القبول للمرحلة المستهدفة أو العامة)
     `## 3. Actual Changes` (تستخدم `diff_summary` أو ملخص الملفات من `TASKS.json`)
     `## 4. Test Evidence` (تستخدم `test_evidence` أو آخر `verification_result` من `TASKS.json`)
     `## 5. Concern & Status` (تتضمن `concern` أو `"none"` وسطر الحالة الحرفي `current_stage=<v> | planning_round=<v> | rejections=<v>` مع آخر إجراء في `DUET_LOG.md`).
3. دالة `main(argv=None) -> int`:
   - عبر `argparse`: الخيارات المطلوبة `--plan` و`--tasks` و`--resume` و`--log` (كلها `required=True`)، والخيارات الاختيارية `--lens` (افتراضي `"fish"`), `--stage`, `--diff`, `--evidence`, `--concern`, `--out` (مسار اختياري لحفظ الكبسولة UTF-8 بالإضافة لطباعتها على stdout).
   - تلتقط `(FileNotFoundError, ValueError)` فقط، وتطبع `error: ...` على `sys.stderr` وتخرج بـ `2` **بدون أي Traceback**؛ وتعيد `0` عند النجاح. وتدعم `if __name__ == "__main__": sys.exit(main())`.

## خطوات التنفيذ المطلوبة (التزم بها بدقة بدون كسر `duet_status.py` و`test_duet_status.py`):
1. اقرأ الملفات الأربعة الحالية في `duet_demo` (`PLAN.md`, `TASKS.json`, `duet_resume.json`, `DUET_LOG.md`) ثم حدّثها بإضافة المرحلة **`S3`** مقسمة إلى تاسكين:
   - **`T1` (اختبار النبض الأول):** `VALID_LENSES` + `build_capsule` في `make_capsule.py` + اختبارات الوحدة لـ `T1` في `test_make_capsule.py`.
   - **`T2` (واجهة CLI):** إضافة `main` والخيارات (`--out`, exit code 2 بدون Traceback) + اختبارات CLI في `test_make_capsule.py`.
   (أبقِ كل سجلات واختبارات S1/S2 كما هي).
2. **(المرحلة أ):** استدعِ `subagent(agent="executor", ...)` (بدون `sessionID` لفتح جلسة منفذ جديدة نظيفة ثم احفظ `executor_session_id` في `duet_resume.json`) لنقد خطة `S3` فقط **بدون كتابة أي ملف كود**؛ أدمج الملاحظات المفيدة في `PLAN.md`.
3. **(التنفيذ المتدرج — `T1` أولاً كاختبار نبض):**
   - كلّف `executor` (بنفس `executor_session_id`) بتنفيذ **`T1` فقط**.
   - عند عودته، اقرأ الملفات بـ `read` وشغّل `~\Downloads\zizo\duet_demo\run_tests.cmd unit` بنفسك، وسجّل اعتماد `T1` في `DUET_LOG.md` و`TASKS.json` و`duet_resume.json`.
4. **(استكمال `T2`):**
   - كلّف `executor` (بنفس `executor_session_id`) بتنفيذ **`T2`** دون كسر `T1` أو `test_duet_status.py`، واطلب منه إرجاع ملخص تقرير مضغوط بالكبسولة.
   - عند عودته، اقرأ الملفات بـ `read` وشغّل `~\Downloads\zizo\duet_demo\run_tests.cmd all` بنفسك.
5. **(بوابة الخروج بالسمكة `critic` — إلزامية):**
   - استدعِ `subagent(agent="critic", ...)` (**بدون تمرير `sessionID`** نهائياً ليعمل بذاكرة صفرية!)، ومرّر له رأساً `LENS: fish` مع كبسولة الفحص لـ `make_capsule.py` و`test_make_capsule.py` + المخرج الحرفي لـ `run_tests.cmd all`.
   - اعرض في ردك النهائي الكبسولة المرسلة + حكم السمكة الحرفي (`VERDICT: ...`)، وفلتر أي ملاحظات (`Blocker`/`Major` تُعالج إن وجدت؛ `Nitpick` تُتجاهل مع السبب في سطر واحد)، ثم سجّل حكم السمكة واعتماد `[FINAL_APPROVED]` للمرحلة `S3` في `DUET_LOG.md` و`TASKS.json` و`duet_resume.json`.

## 7 · assistant (2026-11-21 09:37:13)

بدء المرحلة S3: أولاً أقرأ ملفات العقد المشترك الحالية في `duet_demo` لتحديث الخطة قبل أي تكليف.

## 17 · assistant (2026-11-21 09:37:31)

أقرأ الآن ملفات العقد الأربعة مع `duet_status.py` و`run_tests.cmd` لمعرفة واجهة `load_resume`/`parse_log` وغلاف الفحص قبل صياغة خطة S3.

## 47 · assistant (2026-11-21 09:37:53)

بدء المرحلة أ لـ S3: الملفات الحالية مفهومة (`load_resume`/`parse_log`/`build_summary_line` متاحة في `duet_status.py`، وغلاف `run_tests.cmd` يقبل `unit`/`all`). أكتب الآن مسودة S3 في ملفات التخطيط الأربعة، ثم أستدعي `executor` بجلسة جديدة لنقد الخطة فقط دون كتابة كود.

## 81 · assistant (2026-11-21 09:41:05)

تم إطلاق جلسة المنفذ الجديدة لنقد خطة S3 (بدون كتابة كود). أحفظ الآن `executor_session_id` فوراً في `duet_resume.json` وأسجّل خطوة التكليف في `DUET_LOG.md`، ثم أنتظر عودة المنفذ بملاحظاته.

## 103 · assistant (2026-11-21 09:41:29)

تم حفظ `executor_session_id` وتسجيل خطوة التكليف بنجاح في ملفات العقد الثلاثة.

**الحالة الآن (المرحلة أ — S3):**
- `PLAN.md` (الإصدار 3): قسم S3 مكتوب بتاسكين `T1` (النبض: `VALID_LENSES` + `build_capsule` + اختبارات الوحدة) و`T2` (CLI: `main` + `--out` + exit 2 بدون Traceback).
- `TASKS.json`: المرحلة S3 بحالة `planned` مع `[REDACTED:HIGH_ENTROPY]`.
- `duet_resume.json`: `phase=A_planning`، `current_stage=S3`، `planning_round=1`، `batch_size=1`، `critic_calls[S3]=0`.
- `DUET_LOG.md`: سطرا `PLAN status=draft` و`ASSIGN status=plan_review_requested` مسجّلان.

جلسة المنفذ الجديدة تعمل حالياً في الخلفية على **نقد خطة S3 فقط (قراءة فقط، بلا كتابة أي ملف)**. عند عودته سأدمج ملاحظات `[Blocker]`/`[Major]` الصائبة في `PLAN.md`، أرفع `planning_round` إلى 2، ثم أكلّفه بـ `T1` وحدها كاختبار نبض بنفس الجلسة.

## 113 · assistant (2026-11-21 09:43:57)

عاد المنفذ بـ 23 ملاحظة (0 Blocker، 8 Major). أدمج الآن القرارات المحسومة في `PLAN.md` (الجولة S3-2)، أرفع `planning_round` إلى 2 وأعتمد الخطة، ثم أكلّف المنفذ بنفس الجلسة بتنفيذ **`T1` وحدها** كاختبار نبض.

## 151 · assistant (2026-11-21 09:46:18)

تم اعتماد خطة S3 (الجولة S3-2) وتكليف المنفذ بـ `T1` كاختبار نبض بنجاح.

**الحالة الآن (المرحلة ب — S3 / T1):**
- `PLAN.md` (الإصدار 3): قسم "قرارات محسومة بعد نقد المنفذ" مُدمج (21 قراراً تغطي كل الـMajor ومعظم الـNitpick)، والخطة معتمدة — `STAGE_LIST: S1 | S2 | S3 (T1 → T2)`.
- `duet_resume.json`: `phase=B_execution`، `current_task=T1`، `planning_round=2`، `plan_approved=true`، `batch_size=1`.
- `TASKS.json`: المرحلة S3 و`T1` بحالة `in_progress` (`assigned_at=11:44`).
- `DUET_LOG.md`: سطرا `ACCEPT status=plan_approved` و`ASSIGN status=T1_in_progress` مسجّلان.

المنفذ (نفس الجلسة `ses_e0284e5a8ffetXsMqjbgHsakHL`) يعمل حالياً في الخلفية على **`T1` فقط**: `make_capsule.py` (`VALID_LENSES` + `build_capsule` + `cap_lines` + `_load_json_object` + ثوابت العلامات، بدون `main`) و`test_make_capsule.py` (≥ 9 اختبارات).

عند عودته سأقوم بالتدقيق المستقل: قراءة الملفين بـ `read` وتشغيل `run_tests.cmd unit` بنفسي (المتوقع `Ran ≥ 28 tests ... OK` دون كسر `test_duet_status.py`)، ثم تسجيل اعتماد `T1` في ملفات العقد الثلاثة قبل تكليف `T2`.

## 161 · assistant (2026-11-21 09:50:50)

عاد المنفذ بتقرير `T1` (32 اختباراً OK). أبدأ الآن التدقيق المستقل: أقرأ الملفين الجديدين بنفسي وأشغّل `run_tests.cmd unit` قبل اعتماد `T1`.

## 179 · assistant (2026-11-21 09:51:10)

تدقيق `T1` المستقل ناجح: الملفان مطابقان لمواصفات `PLAN.md` T1 والقرارات 1–14 (تحقق `lens` قبل القراءة، `_load_json_object` برسائل دقيقة، `cap_lines` عامة، قص 157+`...`، حراس النوع، fallback القيود/الهدف، بلا `main`)، و`run_tests.cmd unit` بنفسي → `Ran 32 tests ... OK` (19 S1/S2 + 13 T1 ≥ 28) دون كسر `test_duet_status.py`. أسجّل اعتماد `T1` في ملفات العقد الثلاثة ثم أكلّف المنفذ (نفس الجلسة) بـ `T2` وحدها.

## 213 · assistant (2026-11-21 09:52:38)

تم اعتماد `T1` رسمياً وتكليف المنفذ بـ `T2` بنجاح؛ ملفات العقد الثلاثة محدّثة.

**الحالة الآن (المرحلة ب — S3 / T2):**
- `TASKS.json`: `T1` بحالة `approved` (`Ran 32 tests ... OK`، 13 اختباراً، `verified_by_planner=true`)، و`T2` بحالة `in_progress` (`assigned_at=11:51`).
- `duet_resume.json`: `current_task=T2`، `task_status[S3] = {T1: approved, T2: in_progress}`، `batch_size=1`، `rejections[S3]=0`، `critic_calls[S3]=0`.
- `DUET_LOG.md`: سطرا `ACCEPT status=T1_approved` و`ASSIGN status=T2_in_progress` مسجّلان.

المنفذ (نفس الجلسة `ses_e0284e5a8ffetXsMqjbgHsakHL`) يعمل حالياً في الخلفية على **`T2` فقط**: إضافة `main` + `_safe_streams` + `argparse` (الوسائط المطلوبة الأربعة، `--lens` بلا `choices`، `--out` داخل `try`، التقاط `FileNotFoundError`/`ValueError` فقط → `error: ...` وexit 2 بدون Traceback) وصنف `CliTests` (≥ 6 اختبارات + اختبار subprocess واحد) دون كسر `T1` أو `test_duet_status.py`.

**الخطوة التالية عند عودته:**
1. تدقيق مستقل: قراءة الملفين بـ `read` + تشغيل `run_tests.cmd all` بنفسي (المتوقع `Ran ≥ 38 tests ... OK`).
2. عند النجاح: تسجيل اعتماد `T2` في ملفات العقد الثلاثة.
3. بوابة الخروج الإلزامية: استدعاء `critic` **بدون `sessionID`** بعدسة `LENS: fish` مع كبسولة الفحص + المخرج الحرفي لـ `run_tests.cmd all`، ثم عرض الكبسولة وحكم `VERDICT` للمالك وتسجيل `[FINAL_APPROVED]` لـ S3.

## 223 · assistant (2026-11-21 09:55:10)

عاد المنفذ بتقرير `T2` (39 اختباراً OK). أبدأ التدقيق المستقل: أقرأ الملفين المعدّلين بنفسي وأشغّل `run_tests.cmd all` قبل اعتماد `T2` وفتح بوابة السمكة.

## 241 · assistant (2026-11-21 09:55:25)

تدقيق `T2` المستقل ناجح: `make_capsule.py` (س317–383) مطابق للقرارات 15–18 (`_safe_streams` لكلا التيارين، `--lens` بلا `choices` مع `help`، كتابة `--out` داخل `try`، التقاط `FileNotFoundError`/`ValueError` فقط برسائل `error: ...`، `sys.exit(main())`)، و`CliTests` بـ 7 اختبارات دون المساس بـ T1، و`run_tests.cmd all` بنفسي → `Ran 39 tests in 0.147s ... OK` (19 + 13 + 7 ≥ 38). أسجّل اعتماد `T2` في ملفات العقد الثلاثة، ثم أفتح بوابة الخروج الإلزامية باستدعاء `critic` بذاكرة صفرية (بدون `sessionID`) بعدسة `LENS: fish`.

## 287 · assistant (2026-11-21 09:56:52)

تم اعتماد `T2` وتسجيله في ملفات العقد الثلاثة، وأُطلقت بوابة الخروج الإلزامية: وكيل السمكة `critic` يعمل الآن في الخلفية **بذاكرة صفرية (بدون `sessionID` مُمرَّر)** بعدسة `LENS: fish` على كبسولة فحص `make_capsule.py`/`test_make_capsule.py` + المخرج الحرفي لـ `run_tests.cmd all`.

**الحالة الآن (المرحلة ج — S3 / بوابة السمكة):**
- `TASKS.json`: `T1` و`T2` بحالة `approved` (`Ran 32` ثم `Ran 39 tests ... OK` بتحقق مستقل)، `critic_calls=1`، `critic_verdict=pending`، `[REDACTED:HIGH_ENTROPY]`.
- `duet_resume.json`: `phase=C_critic_gate`، `current_task=CRITIC_GATE`، `critic_calls[S3]=1` (السقف 2)، `rejections[S3]=0`.
- `DUET_LOG.md`: سطرا `ACCEPT status=T2_approved` و`ASSIGN status=critic_gate_requested` مسجّلان.

**عند عودة السمكة سأقوم بـ:**
1. عرض الكبسولة المرسلة + حكمها الحرفي `VERDICT: ...` للمالك.
2. فلترة الملاحظات: `Blocker`/`Major` المدعومة بـ `file:line` أو مخرج اختبار تُعالج عبر المنفذ (بدفعة تاسك واحد)؛ `Nitpick` تُتجاهل مع ذكر السبب في سطر واحد.
3. عند `PASS` (أو بعد معالجة أي `Blocker`/`Major`): تسجيل `[FINAL_APPROVED]` للمرحلة S3 في `DUET_LOG.md` و`TASKS.json` و`duet_resume.json` وتقديم كارت الملخص النهائي.

## 297 · assistant (2026-11-21 10:00:13)

عادت السمكة بحكم `VERDICT: PASS` (3 ملاحظات كلها `Nitpick` بلا أي Blocker/Major). أسجّل الآن حكمها واعتماد `[FINAL_APPROVED]` للمرحلة S3 في ملفات العقد الثلاثة، ثم أقدّم كارت الملخص النهائي.

## 339 · assistant (2026-11-21 10:01:13)

اكتمل تسجيل حكم السمكة واعتماد `[FINAL_APPROVED]` للمرحلة S3 في ملفات العقد الثلاثة بنجاح. إليك كارت الملخص النهائي للمالك.

## 🎯 S3 مكتملة — `make_capsule.py` + `test_make_capsule.py`

### 🐟 الكبسولة المرسلة للسمكة (`LENS: fish`، بذاكرة صفرية — بدون `sessionID`)
- **1. Goal:** أداة stdlib تولّد كبسولة فحص Markdown مضغوطة (≤ 40 سطراً، 5 أقسام حرفية) من `PLAN.md`/`TASKS.json`/`duet_resume.json`/`DUET_LOG.md`، مع CLI واختبارات.
- **2. Constraints:** `VALID_LENSES` + `ValueError("invalid lens: …")` قبل أي قراءة؛ `FileNotFoundError`/`ValueError` تذكر المسار؛ قص 160 حرفاً + `cap_lines(…, 40)`؛ CLI بـ 4 وسائط مطلوبة، `--lens` بلا `choices`، `--out` داخل `try`، exit 2 بلا Traceback؛ ممنوع لمس `duet_status.py`/`test_duet_status.py`/ملفات التخطيط.
- **3. Actual Changes:** ملفان جديدان فقط — `make_capsule.py` (383 سطراً) و`test_make_capsule.py` (20 اختباراً: 13 وحدة + 7 CLI).
- **4. Test Evidence:** المخرج الحرفي لتشغيلي المستقل `run_tests.cmd all` → `Ran 39 tests in 0.147s` / `OK` + تشغيل حقيقي للأداة على ملفات `duet_demo` → exit 0 بكبسولة 17 سطراً.
- **5. Concern:** (أ) قص 160 يُفقد معلومة؟ (ب) أثر `_safe_streams` كمكتبة؟ (ج) `PermissionError` عند `--out`.

### ⚖️ حكم السمكة الحرفي
**`VERDICT: PASS`** — 3 ملاحظات كلها `[Nitpick]`، **0 Blocker، 0 Major**. أكدت مطابقة الكود لـ `PLAN.md` بالكامل (`file:line` لكل بند) وأن العدد 39 = 20 + 19 يطابق المخرج الحرفي.

### 🔍 فلترة الملاحظات (الثلاث متجاهلة مع السبب)
1. `_safe_streams` بعد `parse_args` — يؤثر فقط على رسائل argparse عبر pipe بترميز قديم؛ لا أثر على الاختبارات أو المسارات الواقعية.
2. مجلد بدل ملف → `PermissionError` غير ملتقط — متسق حرفياً مع القرار 16 المعتمد.
3. القلقان (أ)/(ب) مُبرَّآن من السمكة نفسها: القص هو القرار 2 حرفياً، و`reconfigure` داخل `main` فقط.

### 📊 الزتونة
| البند | القيمة |
|---|---|
| T1 (نبض) | `run_tests.cmd unit` → `Ran 32 tests … OK` (تحقق مستقل) |
| T2 (CLI) | `run_tests.cmd all` → `Ran 39 tests … OK` (تحقق مستقل) |
| planning_round | 2 (نقد المنفذ: 23 ملاحظة أُدمج 22 منها) |
| rejections[S3] | 0 |
| critic_calls[S3] | 1 من 2 |
| executor_session_id | `ses_e0284e5a8ffetXsMqjbgHsakHL` |
| critic_session_id | `ses_e02767241ffesWhTgxqacxPewC` |
| الحالة النهائية | `all_stages_approved` — `STAGE_LIST: S1 \| S2 \| S3` |

ملفات العقد الأربعة محدّثة: `DUET_LOG.md` (سطرا `VERIFY status=critic_pass` و`FINAL action=ACCEPT status=final_approved` + `[FINAL_APPROVED]`)، `TASKS.json` (`final_status=all_stages_approved`)، `duet_resume.json` (`phase=C_final_approved`، `current_stage=DONE`).

**[FINAL_APPROVED]**
