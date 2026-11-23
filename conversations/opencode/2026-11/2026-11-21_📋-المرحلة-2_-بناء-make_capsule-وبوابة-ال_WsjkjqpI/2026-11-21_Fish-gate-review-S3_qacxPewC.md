# Fish gate review S3

- id: `ses_e02767241ffesWhTgxqacxPewC`
- title: Fish gate review S3
- date: 2026-11-21 09:56:52
- directory: duet_demo
- parent: `ses_e02886f3bffe0Pb1qeWsjkjqpI`
- agent: critic
- model: upstage-studio/claude-fable-5-1
- messages: 7 (user 1, assistant 6)
- archived: false

## 4 · user (2026-11-21 09:56:52)

You are a subagent spawned by another session.
أنت الناقد الصريح / السمكة (critic) — قراءة فقط، ذاكرة صفرية. ممنوع كتابة أو تعديل أي ملف أو تشغيل أي أمر يغيّر الحالة. مسموح لك فقط قراءة الملفات المذكورة أدناه.

LENS: fish

# Inspection Capsule (S3 — مشروع ~\Downloads\zizo\duet_demo)
## 1. Goal
أداة stdlib `make_capsule.py` تولّد كبسولة فحص Markdown مضغوطة (<= 40 سطراً، أقسام خمسة حرفية) من PLAN.md/TASKS.json/duet_resume.json/DUET_LOG.md لوكيل السمكة، مع CLI (`main`) واختبارات `test_make_capsule.py`.
## 2. Constraints
- stdlib فقط؛ يستورد `duet_status` (load_resume/parse_log/build_summary_line) دون تعديله؛ نصوص ثابتة ASCII بلا ألوان (استثناء: ثابتا المطابقة GOAL_MARKERS/CONSTRAINT_MARKERS لا يُطبعان).
- `VALID_LENSES = ("fish", "scope-guard", "forensic")`؛ lens غير صالح -> `ValueError("invalid lens: <lens>")` قبل قراءة أي ملف؛ ملف مفقود -> FileNotFoundError؛ TASKS فاسد/غير dict -> ValueError تذكر المسار.
- كل سطر لا يبدأ بـ `#` يُقص إلى 160 (157 + `...`)؛ كل قسم <= 5 عناصر؛ حارس `cap_lines(lines, 40)`؛ بلا سطر ختامي فارغ.
- CLI: `--plan/--tasks/--resume/--log` مطلوبة؛ `--lens` بلا choices؛ `--out` داخل try؛ يلتقط FileNotFoundError/ValueError فقط -> `error: ...` على stderr وexit 2 بلا Traceback؛ `_safe_streams()` reconfigure(errors="replace") لـ stdout+stderr.
- ممنوع لمس duet_status.py/test_duet_status.py/run_tests.cmd/ملفات التخطيط الأربعة. الاختبارات tempfile فقط.
## 3. Actual Changes
- جديد: `~\Downloads\zizo\duet_demo\make_capsule.py` (383 سطراً: VALID_LENSES، cap_lines، _load_json_object، build_capsule، _safe_streams، main، sys.exit(main())).
- جديد: `~\Downloads\zizo\duet_demo\test_make_capsule.py` (417 سطراً: MakeCapsuleTests 13 اختباراً + CliTests 7 اختبارات، helper مستقل، لا استيراد من test_duet_status).
- المرجع للمواصفات: `~\Downloads\zizo\duet_demo\PLAN.md` قسم `## S3` + `### قرارات محسومة بعد نقد المنفذ (الجولة S3-2)` (القرارات 1-21).
## 4. Test Evidence (المخرج الحرفي للمخطط — run_tests.cmd all)
```
~\Downloads\zizo\duet_demo\run_tests.cmd all
test_main_invalid_lens_returns_2 (test_make_capsule.CliTests...) ... ok
test_main_missing_log_argument_raises_system_exit_2 (test_make_capsule.CliTests...) ... ok
test_main_missing_plan_and_invalid_tasks_return_2 (test_make_capsule.CliTests...) ... ok
test_main_options_appear_in_output (test_make_capsule.CliTests...) ... ok
test_main_out_writes_utf8_and_missing_dir_returns_2 (test_make_capsule.CliTests...) ... ok
test_main_success_matches_build_capsule (test_make_capsule.CliTests...) ... ok
test_subprocess_missing_files_exit_2_without_traceback (test_make_capsule.CliTests...) ... ok
test_bom_and_crlf_in_plan_and_tasks ... ok | test_cap_lines_direct ... ok | test_default_stage_resolution ... ok
test_diff_evidence_concern_present_and_absent ... ok | test_each_missing_file_raises_file_not_found ... ok
test_full_capsule_structure ... ok | test_invalid_lens_raises_before_reading_files ... ok
test_long_content_line_clipped_to_160 ... ok | test_long_plan_and_long_diff_capped_at_40 ... ok
test_summary_line_literal ... ok | test_tasks_invalid_json_raises_value_error_with_path ... ok
test_tasks_not_an_object_raises_value_error_with_path ... ok | test_valid_lenses_constant ... ok
(+ 19 اختبار test_duet_status كلها ok)
----------------------------------------------------------------------
Ran 39 tests in 0.147s

OK
```
- تشغيل المنفذ الحقيقي للأداة على ملفات duet_demo (`--stage S3 --lens fish`) -> exit 0، كبسولة 17 سطراً (سطر Test Evidence مقصوص إلى 160 بـ `...`).
## 5. Concern & Status
concern: (أ) هل قص سطر واحد إلى 160 حرفاً يُفقد معلومة حرجة من verification_result الطويل بدل تقسيمه؟ (ب) `_safe_streams` تعيد ضبط sys.stderr/stdout عالمياً — هل من أثر جانبي عند الاستيراد كمكتبة (تُستدعى داخل main فقط)؟ (ج) `PermissionError` عند `--out` يترك Traceback عمداً (القرار 16).
current_stage=S3 | planning_round=2 | rejections=0
last_log: [2026-11-21 11:55] stage=S3 action=ASSIGN status=critic_gate_requested

**المطلوب منك:** اقرأ `make_capsule.py` و`test_make_capsule.py` كاملين، وقسم S3 من `PLAN.md`، وعند الحاجة `duet_status.py` و`run_tests.cmd`. ابحث بصراحة عن: ثغرات منطقية تخالف المواصفات، استثناءات غير ملتقطة تُنتج Traceback في مسارات الإدخال الواقعية، اختبارات تمر دون أن تثبت ما تدّعيه، تعارضات مع duet_status.py، مخاطر ويندوز (ترميز/CRLF/مسارات)، وأي تجاوز للنطاق (ملفات لُمست خارج الملفين الجديدين). أعد قائمة مرقّمة مضغوطة مصنفة `[Blocker]`/`[Major]`/`[Nitpick]`، كل بند مدعوم بـ `file:line` أو بمخرج اختبار محدد (بدون دعم = Nitpick). اختم ردك حصراً بسطر واحد: `VERDICT: PASS` أو `VERDICT: BLOCK` (BLOCK فقط عند وجود Blocker أو Major مدعوم بدليل). وأكد صراحة أنك لم تكتب أو تعدّل أي ملف.

## 5 · assistant (2026-11-21 09:56:52)

سأبدأ بقراءة `make_capsule.py` كاملاً.

## 15 · assistant (2026-11-21 09:57:07)

جاري قراءة ملف الاختبارات `test_make_capsule.py` كاملاً.

## 25 · assistant (2026-11-21 09:57:19)

جاري تحديد موقع قسم S3 والقرارات المحسومة داخل `PLAN.md` قبل قراءتها.

## 35 · assistant (2026-11-21 09:57:39)

جاري قراءة قسم S3 كاملاً (السطور 119–223) من `PLAN.md` بما فيه القرارات المحسومة.

## 45 · assistant (2026-11-21 09:57:50)

جاري قراءة `duet_status.py` للتحقق من توافق `load_resume`/`parse_log`/`build_summary_line` مع استخدامها في `make_capsule.py` (نوع المُرجَع، مفاتيح السجل، الاستثناءات).

## 55 · assistant (2026-11-21 09:58:51)

VERDICT: PASS
1. [Nitpick] `_safe_streams()` تُستدعى بعد `parser.parse_args` (make_capsule.py:351-353) بينما القرار 15 يقول "في بداية `main`" (PLAN.md:207)؛ رسائل خطأ argparse التي تُعيد قيمة وسيط غير ASCII (مسار عربي) تخرج قبل الحارس عند توجيه stderr إلى pipe بترميز قديم. الإصلاح نقل سطر واحد قبل 351؛ لا أثر على الاختبارات (StringIO).
2. [Nitpick] تمرير مجلد بدل ملف في `--plan/--tasks` → `open` (make_capsule.py:57, 71) يرفع `PermissionError` على ويندوز، غير ملتقط (369-376) → Traceback وexit 1. متسق مع القرار 16 (PLAN.md:208) لكنه غير مغطى باختبار؛ مقبول.
3. [Nitpick] القلق (ب): `reconfigure` يحدث فقط داخل `main` (make_capsule.py:317-325، 353) ولا شيء عند `import make_capsule` — لا أثر جانبي كمكتبة. القلق (أ): قص 160 مطلوب حرفياً بالقرار 2 (PLAN.md:192) وليس عيباً؛ `verification_result` متعدد الأسطر يُقسَّم أصلاً (make_capsule.py:219-223، 237-238).
تحقق المطابقة: VALID_LENSES/ValueError قبل القراءة (19، 258-259)، `_load_json_object` برسائل القرار 13 (50-67)، ميزانية 29 سطراً (280-310 + MAX_ITEMS)، `cap_lines` (38-47)، `_pick_stage` القرار 7 (109-119)، `--lens` بلا choices (341-345)، `--out` داخل try (366-368) — كلها مطابقة لـ PLAN.md:131-215. توافق duet_status: مفاتيح `date/stage/action/status` (duet_status.py:40-48) و`load_resume` ValueError/FileNotFoundError (52-69) مستخدمة بصحة. الاختبارات تثبت ما تدّعيه (الكبسولة الكاملة 144-161، BOM+CRLF 225-243، subprocess 398-413) والعدد 39 = 20 + 19 يطابق المخرج الحرفي `Ran 39 tests ... OK`. ادعاء عدم لمس ملفات خارج الملفين الجديدين غير قابل للتحقق بأدوات القراءة بلا git؛ أُخذ من الكبسولة.
أؤكد صراحة: لم أكتب أو أعدّل أي ملف ولم أشغّل أي أمر؛ قراءة فقط.
VERDICT: PASS
