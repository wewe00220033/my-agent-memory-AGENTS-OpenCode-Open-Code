# FIELD TEST: bridge_doctor.py

- id: `ses_e02073e05ffehgYIVxPQ1PPyjI`
- title: FIELD TEST: bridge_doctor.py
- date: 2026-11-21 11:58:20
- directory: D:/SMS/.hRhR_gateway-service
- agent: planner-reviewer
- messages: 48 (user 1, assistant 47)
- children: 2
  - 2026-11-21_Fish-lens-review-of-S1-capsule_6VMGoHW5.md
  - 2026-11-21_Review-plan-only-(no-code-edits)_0CO0U65F.md
- archived: false

## 6 · user (2026-11-21 11:58:20)

هذه مهمة تنفيذ ميدانية كاملة ومعتمدة مسبقاً من المالك لبناء أداة `bridge_doctor.py` واختباراتها في `D:\SMS\.hRhR_gateway-service\tools\`؛ نفّذ المراحل تباعاً حتى الختام بـ `[FINAL_APPROVED]` ولا تتوقف لطلب إذن أو استدعاء `question`.

مسارات ملفات التخطيط الخاصة بهذه المهمة:
- `D:\SMS\.hRhR_gateway-service\tools\PLAN.md`
- `D:\SMS\.hRhR_gateway-service\tools\TASKS.json`
- `D:\SMS\.hRhR_gateway-service\tools\duet_resume.json`
- `D:\SMS\.hRhR_gateway-service\tools\DUET_LOG.md`

تنبيهات حوكمة إلزامية:
1. ممنوع قراءة أي ملف يطابق `*opencode.json*` عليك أو على المنفذ أو على الناقد (البنية المطلوبة موثقة كاملة في `tools\PLAN.md`).
2. التحقق بالأوامر لك وحدك عبر `D:\SMS\.hRhR_gateway-service\tools\run_tests.cmd unit` (بعد T1) و `D:\SMS\.hRhR_gateway-service\tools\run_tests.cmd all` (بعد T2)؛ لا تشغّل أوامر شيل أخرى.
3. المنفذ يعدّل فقط `D:\SMS\.hRhR_gateway-service\tools\bridge_doctor.py` و `D:\SMS\.hRhR_gateway-service\tools\test_bridge_doctor.py`، ويستخدم في اختبارات `check_agents_config` أسماء ملفات مؤقتة لا تطابق `*opencode.json*` (مثل `sample_agents_cfg.json`) ولا يجري اتصالات شبكة حقيقية.

خطوات التشغيل المطلوبة بالترتيب:
1) **المرحلة A (مراجعة الخطة بلا كود):**
   اقرأ `D:\SMS\.hRhR_gateway-service\tools\PLAN.md` ثم استدعِ `executor` لنقد الخطة فقط دون كتابة أو تعديل أي ملف، وادمج ملاحظاته المفيدة في `tools\PLAN.md` وحدّث `TASKS.json` و `duet_resume.json` و `DUET_LOG.md`.
2) **المرحلة B — نبض T1 ثم دفعة T2 (عبر نفس `session_id` للمنفذ):**
   - كلّف `executor` بـ `T1` فقط، ثم اقْرأ الملفين بنفسك وشغّل `D:\SMS\.hRhR_gateway-service\tools\run_tests.cmd unit` للتحقق المستقل.
   - استكمل مع نفس `executor` لـ `T2`، ثم اقْرأ الملفين وشغّل `D:\SMS\.hRhR_gateway-service\tools\run_tests.cmd all` للتحقق المستقل.
3) **بوابة الناقد السفرية (بدون `session_id` وبذاكرة صفرية):**
   كوّن كبسولة فحص نظيفة (`<= 40` سطراً تبدأ بـ `# Inspection Capsule` و `LENS: fish` مع Goal/Constraints/Actual Changes/Test Evidence الحرفي/Concern) واستدعِ وكيل الناقد القراءة-فقط (`critic`) في جلسة جديدة تماماً. إن وُجد Blocker أو Major عالجه مع المنفذ وأعد التحقق.
4) **الإقفال:**
   حدّث `tools\TASKS.json` (`status="approved"`, `critic_verdict="PASS"`, `verified_by_planner=true`, `final_status="all_stages_approved"`) و `tools\duet_resume.json` (`phase="C_final_approved"`, `current_stage="DONE"`, `final_approved=true`) وسجّل في `tools\DUET_LOG.md` ختام `[FINAL_APPROVED]` بالصيغة المعتمدة لـ `ENTRY_RE`.

ارجع بتقرير عربي مختصر يذكر نتائج الاختبارات الحرفية وحكم الناقد ومعرّفات الجلسات.

## 7 · assistant (2026-11-21 11:58:20)

بدء المرحلة A: قراءة ملفات التخطيط الأربعة أولاً.

## 17 · assistant (2026-11-21 11:58:32)

قراءة `TASKS.json` لمعرفة حالة المهام الحالية قبل استدعاء المنفذ.

## 27 · assistant (2026-11-21 11:58:46)

قراءة `duet_resume.json` لمعرفة حالة الجولات ومفاتيح الاستئناف قبل استدعاء المنفذ.

## 37 · assistant (2026-11-21 11:59:01)

قراءة `DUET_LOG.md` لمعرفة صيغة `ENTRY_RE` المعتمدة قبل استدعاء المنفذ لنقد الخطة.

## 47 · assistant (2026-11-21 11:59:13)

اكتملت قراءة الملفات الأربعة. الآن المرحلة A: استدعاء المنفذ لنقد الخطة فقط دون أي كتابة أو تعديل.

## 57 · assistant (2026-11-21 12:00:07)

تم إطلاق المنفذ لنقد الخطة (المرحلة A). أثناء عمله، أحفظ معرّف جلسته فوراً في `duet_resume.json` لضمان الاستئناف.

## 67 · assistant (2026-11-21 12:00:21)

تم حفظ معرّف جلسة المنفذ. أسجّل الآن خطوة إطلاق مراجعة الخطة في `DUET_LOG.md` ريثما يعود المنفذ بنقده.

## 77 · assistant (2026-11-21 12:00:40)

تم تحديث `DUET_LOG.md` بنجاح. اكتملت تجهيزات المرحلة A:

- ✅ قراءة ملفات التخطيط الأربعة (`PLAN.md`, `TASKS.json`, `duet_resume.json`, `DUET_LOG.md`).
- ✅ إطلاق `executor` لنقد الخطة فقط (بلا كتابة/تعديل/شيل، وبلا قراءة `*opencode.json*`).
- ✅ حفظ `executor_session_id = ses_e02059baaffeHa0M6w0CO0U65F` في `duet_resume.json`.
- ✅ تسجيل خطوة `PLAN / executor_review_requested` في `DUET_LOG.md`.

بانتظار عودة المنفذ برسالة نقده؛ فور وصولها سأدمج الملاحظات الصائبة في `PLAN.md`، وأحدّث `TASKS.json` و`duet_resume.json` (`planning_round`, `plan_review_result`)، ثم أكلّف نفس الجلسة بـ `T1` وحده (اختبار النبض) وأتحقق مستقلاً عبر `run_tests.cmd unit`.

## 87 · assistant (2026-11-21 12:02:41)

وصل نقد المنفذ: `PLAN_REVIEW: NEEDS_CHANGES` مع 5 تغييرات ملزمة كلها صائبة تقنياً (حقن `opener` في `main`، فحص `isinstance(dict)`، تثبيت `format_report`/`--json.overall`، اختبار subprocess بمسارات مؤقتة كاملة + منفذ حر ديناميكي، واعتماد نص مخرج `unittest` كمعيار قبول بسبب عيب `%ERRORLEVEL%` في `run_tests.cmd` الذي لا يملك أحدنا تعديله). أدمجها الآن في `PLAN.md` (المسودة 2).

## 97 · assistant (2026-11-21 12:04:08)

تم اعتماد المسودة 2 من `PLAN.md`. أحدّث الآن `TASKS.json` بنتيجة مراجعة الخطة واعتمادها.

## 107 · assistant (2026-11-21 12:04:28)

تم تحديث `TASKS.json`. أحدّث الآن `duet_resume.json` (اعتماد الخطة + الانتقال للمرحلة B).

## 117 · assistant (2026-11-21 12:04:43)

تم تحديث `duet_resume.json`. أسجّل الآن اعتماد الخطة `[PLAN_APPROVED]` في `DUET_LOG.md` قبل تكليف T1.

## 127 · assistant (2026-11-21 12:05:02)

تم تسجيل `[PLAN_APPROVED]`. أبدأ الآن المرحلة B — نبض T1: تكليف نفس جلسة المنفذ بـ T1 وحده.

## 137 · assistant (2026-11-21 12:05:49)

تم إطلاق المنفذ على T1 (نفس الجلسة). أثناء عمله أسجّل التكليف في `TASKS.json` (حالة T1 = `assigned`).

## 147 · assistant (2026-11-21 12:06:04)

تم تسجيل التكليف على مستوى المرحلة. أحدّث الآن حالة المهمة `T1` نفسها إلى `assigned` داخل `TASKS.json`.

## 157 · assistant (2026-11-21 12:06:20)

تم تحديث حالة `T1` إلى `assigned`. أسجّل الآن سطر التكليف `ASSIGN` في `DUET_LOG.md` ريثما يعمل المنفذ.

## 167 · assistant (2026-11-21 12:06:39)

تم تسجيل سطر `ASSIGN` في `DUET_LOG.md`. اكتملت تجهيزات نبض T1:

- ✅ `PLAN.md` المسودة 2 معتمدة (بعد دمج 5 تغييرات ملزمة من نقد المنفذ).
- ✅ `TASKS.json`: المرحلة `S1 = in_progress`، المهمة `T1 = assigned` (14:06)، وتسجيل عيب `run_tests.cmd` في `known_issues`.
- ✅ `duet_resume.json`: `phase = B_execution`، `current_task = T1`، `batch_size = 1`، `planning_round = 2`.
- ✅ `DUET_LOG.md`: سطور `PLAN_APPROVED` و `ASSIGN / T1_assigned` مسجّلة.
- ✅ المنفذ يعمل على T1 في الجلسة `ses_e02059baaffeHa0M6w0CO0U65F`.

بانتظار عودة المنفذ بتقرير T1؛ فور وصوله سأقرأ `bridge_doctor.py` و `test_bridge_doctor.py` بنفسي، ثم أشغّل `D:\SMS\.hRhR_gateway-service\tools\run_tests.cmd unit` للتحقق المستقل (معيار القبول = نص `unittest` الحرفي `Ran N tests` + `OK` بلا `FAILED`/`ERROR`/`Traceback`)، وبعد نجاحه أكلّف نفس الجلسة بـ T2.

## 177 · assistant (2026-11-21 12:09:56)

عاد المنفذ بتقرير T1 (`Ran 23 tests` + `OK`). أبدأ التحقق المستقل: قراءة `bridge_doctor.py` بنفسي أولاً.

## 187 · assistant (2026-11-21 12:10:10)

قرأت `bridge_doctor.py` (274 سطراً): الثوابت والدوال الأربع مطابقة للمسودة 2 (`CATCH` موسّع، فحص `isinstance(dict)` صريح في السطور 76 و130 و133، تجميع الانتهاكات بـ `"; "` في السطر 196، فاصل `-` ديناميكي في السطر 267، ولا `main`/argparse كما هو مطلوب لـ T1). أكمل التحقق المستقل بقراءة ملف الاختبارات.

## 197 · assistant (2026-11-21 12:10:25)

قرأت `test_bridge_doctor.py` (351 سطراً، 23 اختباراً): كل الفيكسترز في `tempfile.TemporaryDirectory` باسم `sample_agents_cfg.json`، الـ opener الوهمي يعيد `io.BytesIO`، لا شبكة حقيقية ولا قراءة لأي `*opencode.json*`، ولا اختبارات T2. أشغّل الآن التحقق المستقل عبر غلاف `run_tests.cmd unit`.

## 207 · assistant (2026-11-21 12:10:42)

التحقق المستقل لـ T1 نجح حرفياً: `Ran 25 tests ... OK` (bridge) + `Ran 23 tests ... OK` (bridge_doctor) بلا `FAILED`/`ERROR`/`Traceback`. أعتمد T1 في `TASKS.json` أولاً.

## 217 · assistant (2026-11-21 12:10:59)

تم اعتماد T1 في `TASKS.json`. أحدّث الآن `duet_resume.json` (الانتقال إلى `current_task = T2`) قبل تكليف المنفذ.

## 227 · assistant (2026-11-21 12:11:13)

تم تحديث `duet_resume.json`. أسجّل الآن سطر `VERIFY/ACCEPT` لـ T1 في `DUET_LOG.md` قبل تكليف المنفذ بـ T2.

## 237 · assistant (2026-11-21 12:11:38)

تم تسجيل اعتماد T1 في `DUET_LOG.md`. أبدأ الآن دفعة T2: تكليف نفس جلسة المنفذ بواجهة CLI `main` + `--json` + اختبارات CLI/subprocess.

## 247 · assistant (2026-11-21 12:12:21)

تم إطلاق المنفذ على T2 (نفس الجلسة). أثناء عمله أسجّل تكليف T2 في `TASKS.json` (حالة T2 = `assigned`).

## 257 · assistant (2026-11-21 12:12:34)

تم تحديث حالة `T2` إلى `assigned`. أسجّل الآن سطر التكليف `ASSIGN / T2_assigned` في `DUET_LOG.md` ريثما يعمل المنفذ.

## 267 · assistant (2026-11-21 12:12:56)

تم تسجيل سطر `ASSIGN / T2_assigned` في `DUET_LOG.md`. اكتملت تجهيزات دفعة T2:

- ✅ `T1` معتمد بالتحقق المستقل (`run_tests.cmd unit` → `Ran 25 tests OK` + `Ran 23 tests OK`).
- ✅ `TASKS.json`: `T1 = approved` (14:12)، `T2 = assigned` (14:13).
- ✅ `duet_resume.json`: `current_task = T2`، `batch_size = 1`.
- ✅ `DUET_LOG.md`: سطور `ACCEPT / T1_approved` و `ASSIGN / T2_assigned` مسجّلة.
- ✅ المنفذ يعمل على T2 في الجلسة `ses_e02059baaffeHa0M6w0CO0U65F`.

بانتظار عودة المنفذ بتقرير `[STAGE T2 DONE]`؛ فور وصوله سأقرأ `bridge_doctor.py` و `test_bridge_doctor.py` بنفسي، ثم أشغّل `D:\SMS\.hRhR_gateway-service\tools\run_tests.cmd all` للتحقق المستقل (معيار القبول = نص `unittest` الحرفي `Ran N tests` + `OK` لكل مجموعة بلا `FAILED`/`ERROR`/`Traceback`)، وبعد نجاحه أكوّن كبسولة الفحص (`# Inspection Capsule` + `LENS: fish`) وأستدعي `critic` في جلسة جديدة بذاكرة صفرية، ثم الإقفال بـ `[FINAL_APPROVED]`.

## 277 · assistant (2026-11-21 12:14:58)

عاد المنفذ بتقرير `[STAGE T2 DONE]` (`Ran 29 tests` + `OK`). أبدأ التحقق المستقل لـ T2: قراءة `bridge_doctor.py` بنفسي أولاً (قسم CLI المضاف).

## 287 · assistant (2026-11-21 12:15:12)

قرأت قسم CLI في `bridge_doctor.py` (السطور 283–381): `_safe_streams` بحارس `hasattr(reconfigure)` (السطر 291)، `_build_parser` بالوسائط السبعة وقيمها من ثوابت الوحدة بلا `%` حرفي، `main(argv=None, opener=None)` يمرّر `opener` لـ `check_health` (السطر 351)، و`--json` يطبع `overall/passed/total/checks` (السطور 367–373). أكمل التحقق المستقل بقراءة ملف الاختبارات كاملاً (الاستيرادات الجديدة + صنف `MainCliTests`).

## 297 · assistant (2026-11-21 12:15:28)

قرأت `test_bridge_doctor.py` كاملاً (478 سطراً، 29 اختباراً = 23 من T1 + 6 في `MainCliTests`): كل اختبارات CLI تمرر `--config/--run-tests/--duet-status/--make-capsule` صراحةً عبر `_cli_fixture` (السطور 357–371)، المنفذ الحر المغلق ديناميكي (السطور 374–380)، `--timeout 1` و`timeout=30` في subprocess (السطور 460/468)، ولا شبكة حقيقية. أشغّل الآن التحقق المستقل الكامل عبر `run_tests.cmd all`.

## 307 · assistant (2026-11-21 12:15:45)

التحقق المستقل الكامل لـ T2 نجح حرفياً عبر `run_tests.cmd all`: `Ran 25 tests ... OK` (bridge) + `Ran 29 tests ... OK` (bridge_doctor: 23 من T1 + 6 من `MainCliTests`) + `Ran 41 tests ... OK` (duet_demo: `test_duet_status` + `test_make_capsule`)، بلا أي `FAILED`/`ERROR`/`Traceback`. أعتمد T2 في `TASKS.json` أولاً.

## 317 · assistant (2026-11-21 12:16:04)

تم اعتماد T2 في `TASKS.json`. أحدّث الآن `duet_resume.json` (حالة T2 + الانتقال لبوابة الناقد).

## 327 · assistant (2026-11-21 12:16:21)

تم تحديث `duet_resume.json`. أسجّل الآن سطر `ACCEPT / T2_approved` في `DUET_LOG.md` قبل الانتقال لبوابة الناقد السفرية.

## 337 · assistant (2026-11-21 12:16:47)

تم تسجيل اعتماد T2. أنتقل الآن لبوابة الناقد السفرية: كبسولة فحص نظيفة (`LENS: fish`) وإطلاق `critic` في جلسة جديدة تماماً بذاكرة صفرية (بدون `sessionID`).

## 347 · assistant (2026-11-21 12:17:21)

تم إطلاق الناقد السفري (`critic`) في جلسة جديدة بذاكرة صفرية. أثناء عمله أسجّل استدعاءه الآلي الأول (1/2 من سقف المرحلة) في `duet_resume.json`.

## 357 · assistant (2026-11-21 12:17:37)

تم حفظ معرّف جلسة الناقد. أحدّث الآن عدّاد استدعاءات الناقد في `TASKS.json` ريثما يعود بحكمه.

## 367 · assistant (2026-11-21 12:17:52)

تم تحديث عدّاد الناقد في `TASKS.json`. أسجّل الآن سطر إطلاق بوابة الناقد السفرية في `DUET_LOG.md` ريثما يعود بحكمه.

## 377 · assistant (2026-11-21 12:18:11)

تم تسجيل سطر `VERIFY / critic_fish_requested` في `DUET_LOG.md`. اكتملت تجهيزات بوابة الناقد السفرية:

- ✅ `T1` و `T2` معتمدان بالتحقق المستقل (`run_tests.cmd all` → `Ran 25 tests OK` + `Ran 29 tests OK` + `Ran 41 tests OK`، بلا `FAILED`/`ERROR`/`Traceback`).
- ✅ `critic` أُطلق في جلسة جديدة بذاكرة صفرية (`ses_e01f5d49cffeG092186VMGoHW5`، `LENS: fish`، كبسولة من 5 بنود، قراءة فقط وبلا `*opencode.json*`).
- ✅ `duet_resume.json`: `current_task = CRITIC_GATE`، `critic_calls[S1] = 1`، `critic_status = awaiting_verdict`.
- ✅ `TASKS.json`: `critic_calls = 1` + `critic_session_id` مسجّل.
- ✅ `DUET_LOG.md`: سطر `VERIFY / critic_fish_requested` مسجّل.

بانتظار عودة الناقد بحكمه؛ فور وصوله سأعرض للمالك الكبسولة + `VERDICT` الحرفي مع فلتر النتائج (اعتماد `[Blocker]`/`[Major]` المدعومين بـ `file:line` أو مخرج اختبار فقط، وتجاهل `[Nitpick]` مع ذكر السبب). إن كان `PASS` ⇒ الإقفال فوراً (`TASKS.json`: `status="approved"`, `critic_verdict="PASS"`, `verified_by_planner=true`, `final_status="all_stages_approved"`؛ `duet_resume.json`: `phase="C_final_approved"`, `current_stage="DONE"`, `final_approved=true`؛ وختام `[FINAL_APPROVED]` في `DUET_LOG.md`)، وإن كان `BLOCK` ⇒ معالجة مع المنفذ (نفس الجلسة، `batch_size = 1`) ثم إعادة التحقق عبر `run_tests.cmd all`.

## 387 · assistant (2026-11-21 12:19:07)

عاد الناقد السفري بحكم `VERDICT: PASS` (3 ملاحظات `[Nitpick]` فقط، لا `Blocker`/`Major`). أبدأ الإقفال: تحديث `TASKS.json` (حكم الناقد + التحقق + اعتماد المرحلة).

## 397 · assistant (2026-11-21 12:19:29)

تم تسجيل حكم الناقد. أكمل إقفال المرحلة S1 في `TASKS.json` (حالة المرحلة + `approved_at` + `final_status`).

## 407 · assistant (2026-11-21 12:19:44)

تم تحديث حالة المرحلة. ألاحظ أن المرحلة تحتوي أيضاً على مفتاح `"approved_at": null` القديم من المسودة الأولى — أزيله لتجنب تكرار المفتاح في JSON، وأضبط `assigned_at` للمرحلة.

## 417 · assistant (2026-11-21 12:20:05)

تم تنظيف المفاتيح المكررة. أضبط الآن `final_status` على مستوى الملف في `TASKS.json`.

## 427 · assistant (2026-11-21 12:20:19)

تم ضبط `final_status` في `TASKS.json`. أحدّث الآن `duet_resume.json` للإقفال النهائي (`phase`, `current_stage`, `final_approved`).

## 437 · assistant (2026-11-21 12:20:33)

تم تحديث `phase`/`current_stage`. أضبط الآن `final_approved = true` وحالة الناقد في `duet_resume.json`.

## 447 · assistant (2026-11-21 12:20:47)

تم تحديث حالة الناقد. أضبط الآن `final_approved = true` في `duet_resume.json`.

## 457 · assistant (2026-11-21 12:21:00)

تم ضبط `final_approved = true`. الخطوة الأخيرة من الإقفال: تسجيل ختام `[FINAL_APPROVED]` في `DUET_LOG.md` بصيغة `ENTRY_RE` المعتمدة.

## 467 · assistant (2026-11-21 12:21:29)

اكتمل الإقفال بنجاح — ختام `[FINAL_APPROVED]` مسجّل في `DUET_LOG.md`.

## 📋 التقرير الختامي — مهمة `bridge_doctor.py` (المرحلة S1)

**الحالة النهائية:** `[FINAL_APPROVED]` ✅

### 1) مسار التنفيذ
- **المرحلة A (مراجعة الخطة):** المنفذ أعاد `PLAN_REVIEW: NEEDS_CHANGES` بخمسة تغييرات ملزمة، دُمجت كلها في `PLAN.md` (المسودة 2) ثم `[PLAN_APPROVED]`.
- **المرحلة B — نبض T1:** تحقق مستقل عبر `run_tests.cmd unit`:
  - `Ran 25 tests in 0.211s / OK` (bridge)
  - `Ran 23 tests in 0.019s / OK` (bridge_doctor)
- **المرحلة B — دفعة T2:** تحقق مستقل عبر `run_tests.cmd all`:
  - `Ran 25 tests in 0.222s / OK` (bridge)
  - `Ran 29 tests in 1.105s / OK` (bridge_doctor: 23 من T1 + 6 في `MainCliTests`)
  - `Ran 41 tests in 0.181s / OK` (duet_demo)
  - لا `FAILED` / `ERROR` / `Traceback` في أي مخرج.

### 2) حكم الناقد السفري (`LENS: fish`, ذاكرة صفرية)
- **`VERDICT: PASS`** — لا `[Blocker]` ولا `[Major]`؛ 3 ملاحظات `[Nitpick]` فقط تُجوهلت مع السبب:
  - `http.client.HTTPException` خارج `CATCH` ⇒ فجوة مواصفة لا عيب تنفيذ (مرشّح لمتابعة لاحقة).
  - TOCTOU للمنفذ الحر في اختبار subprocess ⇒ نادر ومحدود بـ `--timeout 1` + `timeout=30`.
  - انزياح أرقام سطور الكبسولة ~3 أسطر ⇒ لا يمس الكود.

### 3) معرّفات الجلسات
- `executor_session_id`: `ses_e02059baaffeHa0M6w0CO0U65F` (استُخدمت لنقد الخطة + T1 + T2).
- `critic_session_id`: `ses_e01f5d49cffeG092186VMGoHW5` (جلسة جديدة بدون `sessionID` موروث).

### 4) حالة ملفات التخطيط
- `TASKS.json`: `S1.status = approved`, `critic_verdict = PASS`, `verified_by_planner = true`, `final_status = all_stages_approved`.
- `duet_resume.json`: `phase = C_final_approved`, `current_stage = DONE`, `final_approved = true`, `rejections[S1] = 0`, `critic_calls[S1] = 1/2`.
- `DUET_LOG.md`: سلسلة كاملة `PLAN → PLAN_APPROVED → ASSIGN T1 → ACCEPT T1 → ASSIGN T2 → ACCEPT T2 → VERIFY critic → ACCEPT FINAL_APPROVED`.

### 5) الحوكمة
- المنفذ عدّل فقط `bridge_doctor.py` (381 سطراً) و `test_bridge_doctor.py` (478 سطراً، 29 اختباراً).
- لم يقرأ أحد من الثلاثي أي ملف `*opencode.json*`؛ لا اتصالات شبكة حقيقية في الاختبارات.

### ⚠️ قرار مرفوع للمالك (خارج نطاق هذه المهمة)
`run_tests.cmd` يستخدم `exit /b %ERRORLEVEL%` داخل بلوك أقواس (توسيع مبكر) ⇒ كود الخروج غير موثوق وقد يعيد `0` رغم الفشل. الإصلاح المقترح: `setlocal EnableDelayedExpansion` + `!ERRORLEVEL!`، أو إخراج `exit` من الأقواس. مسجّل في `TASKS.json.known_issues`.
