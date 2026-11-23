# 📋 المرحلة 2: بناء make_capsule وبوابة السمكة

- id: `ses_e0298619cffedM56G295qJ5tPS`
- title: 📋 المرحلة 2: بناء make_capsule وبوابة السمكة
- date: 2026-11-21 09:19:48
- directory: duet_demo
- agent: planner-reviewer
- messages: 1 (user 1, assistant 0)
- archived: false

## 6 · user (2026-11-21 09:19:48)

مرحباً! طلب معتمد مسبقاً من المالك (لا تستخدم أداة question إطلاقاً في هذه الجلسة التلقائية):
نريد تنفيذ المرحلة S3 داخل المشروع القائم `~\Downloads\zizo\duet_demo` لبناء أداة حقيقية تخدم منظومتنا: **`make_capsule.py`** (مولّد كبسولة الفحص الأوتوماتيكي لوكيل السمكة) + اختبارات **`test_make_capsule.py`**، مع تطبيق كامل بروتوكول المرحلة 2 (التقسيم المتدرج `T1` أولاً + التحقق عبر `run_tests.cmd` + بوابة السمكة `critic` في النهاية).

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
1. حدّث ملفات التخطيط الأربعة في `duet_demo` (`PLAN.md`, `TASKS.json`, `duet_resume.json`, `DUET_LOG.md`) بإضافة المرحلة **`S3`** مقسمة إلى تاسكين:
   - **`T1` (اختبار النبض الأول):** `VALID_LENSES` + `build_capsule` في `make_capsule.py` + اختبارات الوحدة لـ `T1` في `test_make_capsule.py`.
   - **`T2` (واجهة CLI):** إضافة `main` والخيارات (`--out`, exit code 2 بدون Traceback) + اختبارات CLI في `test_make_capsule.py`.
   (أبقِ كل سجلات واختبارات S1/S2 كما هي).
2. **(المرحلة أ):** استدعِ `executor` (بدون `sessionID` لفتح جلسة منفذ جديدة نظيفة ثم احفظ `executor_session_id` في `duet_resume.json`) لنقد خطة `S3` فقط **بدون كتابة أي ملف كود**؛ أدمج الملاحظات المفيدة في `PLAN.md`.
3. **(التنفيذ المتدرج — `T1` أولاً كاختبار نبض):**
   - كلّف `executor` (بنفس `executor_session_id`) بتنفيذ **`T1` فقط**.
   - عند عودته، اقرأ الملفات بـ `read` وشغّل `~\Downloads\zizo\duet_demo\run_tests.cmd unit` بنفسك، وسجّل اعتماد `T1` في `DUET_LOG.md` و`TASKS.json` و`duet_resume.json`.
4. **(استكمال **`T2`**):**
   - كلّف `executor` (بنفس `executor_session_id`) بتنفيذ **`T2`** دون كسر `T1` أو `test_duet_status.py`.
   - عند عودته، اقرأ الملفات بـ `read` وشغّل `~\Downloads\zizo\duet_demo\run_tests.cmd all` بنفسك.
5. **(بوابة الخروج بالسمكة `critic`):**
   - استدعِ `subagent(agent="critic", ...)` (**بدون تمرير `sessionID`** نهائياً ليعمل بذاكرة صفرية!)، ومرّر له رأساً `LENS: fish` مع كبسولة الفحص لـ `make_capsule.py` و`test_make_capsule.py` + المخرج الحرفي لـ `run_tests.cmd all`.
   - اعرض في ردك الكبسولة + حكم السمكة الحرفي (`VERDICT: ...`)، وفلتر أي ملاحظات (`Blocker`/`Major` تُعالج إن وجدت؛ `Nitpick` تُتجاهل مع السبب في سطر واحد)، ثم سجّل حكم السمكة واعتماد `[FINAL_APPROVED]` للمرحلة `S3` في `DUET_LOG.md` و`TASKS.json` و`duet_resume.json`.
