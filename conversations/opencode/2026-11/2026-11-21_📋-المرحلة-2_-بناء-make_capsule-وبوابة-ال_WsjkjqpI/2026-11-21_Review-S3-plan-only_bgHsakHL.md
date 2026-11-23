# Review S3 plan only

- id: `ses_e0284e5a8ffetXsMqjbgHsakHL`
- title: Review S3 plan only
- date: 2026-11-21 09:41:05
- directory: duet_demo
- parent: `ses_e02886f3bffe0Pb1qeWsjkjqpI`
- agent: executor
- model: upstage-studio/claude-fable-5-1-executor
- messages: 16 (user 3, assistant 13)
- archived: false

## 4 · user (2026-11-21 09:41:05)

You are a subagent spawned by another session.
أنت المنفذ المعزول (Executor) في منظومة الثنائي داخل المشروع `~\Downloads\zizo\duet_demo`.

**المرحلة الحالية: أ — نقد الخطة فقط. ممنوع منعاً باتاً كتابة أو تعديل أي ملف (لا كود، لا اختبارات، لا ملفات تخطيط). مسموح لك القراءة فقط** (اقرأ `PLAN.md` قسم S3، و`duet_status.py` لمعرفة واجهات `load_resume`/`parse_log`/`build_summary_line`، و`run_tests.cmd`، و`test_duet_status.py` كمرجع أسلوب).

المطلوب منك: انقد خطة المرحلة **S3** فقط (في `PLAN.md`، القسم `## S3 — make_capsule.py ...` بتاسكيها T1 وT2) ثم أعد قائمة ملاحظات مرقّمة ومضغوطة (كل ملاحظة سطر أو سطرين) مصنّفة `[Blocker]`/`[Major]`/`[Nitpick]`، تركّز على:
1. أي غموض أو تناقض في مواصفات `build_capsule` (تحديد `stage`، شكل الأقسام الخمسة الحرفي، سقف 40 سطراً، قص الأسطر إلى 160 حرفاً، سلوك القيم الغائبة، استخدام `duet_status.build_summary_line`).
2. قابلية الاختبار على ويندوز: BOM/CRLF، `tempfile`، `redirect_stdout`، `sys.stdout.reconfigure(errors="replace")` مع `StringIO`، اختبار subprocess الوحيد وإعدادات البيئة.
3. واجهة CLI (`argparse` بدون `choices` لـ `--lens`، التقاط `FileNotFoundError`/`ValueError` فقط، صيغة `error: ...`، `--out` بـ UTF-8، exit 2 بدون Traceback).
4. أي خطر لكسر `duet_status.py` أو `test_duet_status.py` (مثل تعارض أسماء أو استيراد دائري) أو خطر على `unittest discover` (مثل اسم الملف أو التجميع).
5. أرقام معايير القبول (عدد الاختبارات ≥ 28 بعد T1 و≥ 34 بعد T2 علماً أن S1/S2 فيهما 19 اختباراً) — هل هي واقعية؟

ملخص مواصفات S3 من `PLAN.md` (اقرأ الملف للنص الكامل):
- `VALID_LENSES = ("fish", "scope-guard", "forensic")`.
- `build_capsule(plan_path, tasks_path, resume_path, log_path, lens="fish", stage=None, diff_summary=None, test_evidence=None, concern=None) -> str`: تتحقق من lens أولاً (`ValueError(f"invalid lens: {lens}")`)، تقرأ PLAN بـ utf-8-sig، TASKS كـ JSON dict (فاسد/غير dict → ValueError تذكر المسار)، resume عبر `duet_status.load_resume`، log عبر `duet_status.parse_log`؛ مفقود → FileNotFoundError. stage: الممرَّرة ثم `current_stage` ثم آخر سجل ثم `-`. المخرج: `# Inspection Capsule` / `LENS: <lens>` / `## 1. Goal` (project, plan, goal) / `## 2. Constraints` (stage + acceptance ≤5) / `## 3. Actual Changes` (diff_summary أو files) / `## 4. Test Evidence` (test_evidence أو آخر verification_result) / `## 5. Concern & Status` (concern أو none + سطر `current_stage=.. | planning_round=.. | rejections=..` عبر `duet_status.build_summary_line` + `last_log: ...`). كل قسم ≤ 5 أسطر محتوى، كل سطر ≤ 160 حرفاً، إجمالي ≤ 40 سطراً مع حارس أخير، بلا سطر ختامي فارغ.
- T2: `main(argv=None)` بـ argparse: `--plan/--tasks/--resume/--log` مطلوبة، `--lens` (افتراضي fish بدون choices)، `--stage/--diff/--evidence/--concern/--out`؛ تلتقط `(FileNotFoundError, ValueError)` فقط → `error: ...` على stderr وexit 2؛ نجاح → `--out` يكتب capsule+"\n" بـ utf-8 ثم print على stdout وتعيد 0؛ `sys.exit(main())`.
- الاختبارات في `test_make_capsule.py` بـ unittest + tempfile فقط؛ التحقق عبر `run_tests.cmd unit` ثم `run_tests.cmd all`.

اختم ردك بسطر واحد: `PLAN_REVIEW_DONE: <عدد الملاحظات> notes, <عدد Blocker> blockers` وأكد صراحة أنك لم تكتب أو تعدّل أي ملف.

## 5 · assistant (2026-11-21 09:41:05)

بدء المرحلة أ (نقد فقط، بدون أي كتابة). سأقرأ `PLAN.md` أولاً لاستخراج قسم S3 بنصه الكامل.

## 15 · assistant (2026-11-21 09:41:21)

قرأت قسم S3 كاملاً. الآن أقرأ `duet_status.py` و`run_tests.cmd` و`test_duet_status.py` (قراءة فقط) للتحقق من الواجهات وأسلوب الاختبار قبل كتابة النقد.

## 33 · assistant (2026-11-21 09:41:38)

اكتملت القراءة (PLAN.md قسم S3، `duet_status.py`، `run_tests.cmd`، `test_duet_status.py`). الواجهات الثلاث المطلوبة موجودة فعلاً (`load_resume` س52، `parse_log` س25، `build_summary_line` س108)، وعدد اختبارات S1/S2 الحالي = 19 بالضبط (5+4+2+3+5). إليك النقد:

[EXECUTOR_FEEDBACK]

**أ) مواصفات `build_capsule`**
1. [Major] تناقض حسابي: القسم 2 يحوي سطر `stage:` + حتى 5 أسطر acceptance = 6 أسطر محتوى، بينما النص يقول "كل قسم ≤ 5 أسطر". الإجمالي الأقصى الفعلي = 2+(1+3)+(1+6)+(1+5)+(1+5)+(1+3) = 29 ≤ 40، فالسقف آمن لكن يلزم تصحيح الصياغة (acceptance ≤ 5 **بالإضافة** إلى سطر stage).
2. [Major] قاعدة 160 حرفاً غامضة: هل الطول النهائي 160 (157 + `...`) أم 160 + `...` = 163؟ وهل تنطبق على سطور الملخص/`last_log`/`LENS`/`project`? أقترح: تُطبّق على **كل** سطر عدا العناوين، والناتج ≤ 160 شاملاً `...`.
3. [Major] `tasks.get("stages", [])` بلا حارس نوع: إن كانت `stages` dict أو str فالحلقة تنتج `AttributeError` غير ملتقط → Traceback. يلزم `isinstance(stages, list)` وكذلك `acceptance`/`files` (غير list → تُعامل كغائبة، والعناصر غير str → `str()`).
4. [Major] تعارض قيود: "كل النصوص الثابتة ASCII" (س125) بينما مطلوب مطابقة الثابت `**الهدف:**` (غير ASCII). يلزم استثناء صريح لـ"علامات المطابقة" أو استخدام regex/قائمة علامات معرّفة في ثابت وحدة.
5. [Major] fallback القيود: "أول عنوان يحتوي القيود/Constraints" — في PLAN.md الحقيقي `**القيود العامة:**` سطر عريض لا عنوان `#`. يجب تعريف "عنوان" (يبدأ بـ `#` أو `**`) وحدّ نهاية الكتلة (حتى أول سطر لا يبدأ بـ `- `/عنوان تالٍ).
6. [Nitpick] `goal`: حدّد حالة الأحرف لـ `Goal:` وهل سطر يبدأ بـ `**` أو `- ` يُعد "غير عنوان" في الـfallback الثاني.
7. [Nitpick] `stage`: حدّد `stage is not None` أم truthiness (`--stage ""`)، وتحويل `current_stage` غير النصي عبر `str()`. لاحظ أن `build_summary_line` تطبع `current_stage=` فارغاً عند `""` بينما تحديد المرحلة يتجاوزه — سلوك مقبول لكن يستحق تثبيتاً.
8. [Nitpick] `project`: استخدم `os.path.basename(os.path.dirname(os.path.abspath(plan_path)))` وإلا يُعاد `""` لمسار نسبي مثل `PLAN.md`.
9. [Nitpick] القسم 3: `files` قائمة فارغة → هل تُطبع `files: ` أم تسقط للاتحاد ثم `none`؟ اقترح: تسقط فقط إن كانت غير قائمة أو فارغة.
10. [Nitpick] القسم 4: `verification_result` متعدد الأسطر — سطر واحد مقصوص أم حتى 5 أسطر؟ وحدّد `strip()` للأسطر المهملة (بيضاء فقط = فارغة) في `diff_summary`/`test_evidence`.
11. [Nitpick] `concern=""` → `none` أم سطر فارغ؟ اقترح: `None` أو بيض → `none`.
12. [Nitpick] الحارس الأخير (39 + `... (truncated)`) غير قابل للوصول بالبناء → غير قابل للاختبار بلا monkeypatch؛ إما استبعاده من معايير القبول صراحةً أو عزله في دالة `_cap_lines(lines, limit=40)` قابلة للاختبار المباشر.
13. [Nitpick] قراءة TASKS.json تعيد منطق `load_resume` حرفياً؛ يمكن السماح صراحةً بإعادة استخدام `duet_status.load_resume(tasks_path)` (الاختبار يطلب فقط ذكر المسار) مع ملاحظة أن رسالة non-dict ستقول "invalid resume file".

**ب) قابلية الاختبار على ويندوز**
14. [Nitpick] BOM/CRLF آمنان: `open(..., "r", encoding="utf-8-sig")` بـ `newline=None` يترجم `\r\n` → `\n` و`json.loads` لا يبالي. ثبّت مع ذلك `read().splitlines()` وأضف assertion `"\r" not in text` في اختبار BOM+CRLF.
15. [Nitpick] اختبار `--out`: اقرأ الملف بـ `newline=""` (أو binary) لإثبات أن الفاصل LF حرفياً وأن النهاية `"\n"` واحدة.
16. [Nitpick] لا تستورد `TempDirMixin` من `test_duet_status` (تزاوج بين ملفي اختبار)؛ كرّر helper صغيراً أو استخدم `tempfile.TemporaryDirectory` + `addCleanup` كما نصّت الخطة.
17. [Nitpick] `run_tests.cmd` يثبّت `C:\Python315\python.exe` بينما subprocess يستخدم `sys.executable` — متطابقان عند التشغيل عبر السكربت، لكن `unit`/`all` وضعان متطابقان (كلاهما discover كامل) فليُذكر أن الفرق وصفي فقط.

**ج) واجهة CLI**
18. [Major] `reconfigure(errors="replace")` مطلوب لـ stdout فقط؛ لكن رسائل `error: ... (<path>)` تذهب إلى stderr وقد تحوي مساراً غير ASCII → `UnicodeEncodeError` → Traceback على كونسول cp1256. اقترح نفس الحارس لـ `sys.stderr` (الـsubprocess test محصّن بـ `PYTHONUTF8=1` فلن يكشفه).
19. [Major] موضع كتابة `--out` غير محدد: إن كانت داخل `try` فمجلد غير موجود → `FileNotFoundError` → `error:` exit 2 (منطقي)، لكن `PermissionError` يبقى Traceback. حدّد أن الكتابة داخل `try` وأن هذا السلوك مقبول.
20. [Nitpick] اتساق مع S2: هناك `main` تُلحق `(<current_path>)` بـ `ValueError`؛ S3 تطبع `error: <message>` فقط. مقبول (الرسالة تحوي المسار) لكن اذكره كقرار واعٍ.
21. [Nitpick] `--lens` بلا `choices` صحيح لتمرير الخطأ عبر `build_capsule`؛ أضف `help` يذكر القيم المسموحة حتى لا يبدو الوسيط حراً.

**د) خطر الكسر والتجميع**
22. [Nitpick] لا استيراد دائري (`duet_status` لا يستورد `make_capsule`)، لا تعارض أسماء، واسم `test_make_capsule.py` يطابق `test_*.py`. أضف `sys.path.insert(0, dirname(abspath(__file__)))` كما في `test_duet_status.py` ليعمل الاستيراد خارج discover أيضاً.

**هـ) أرقام القبول**
23. [Nitpick] 19 + 9 = 28 و+6 = 34 واقعية لكن **بلا هامش**: حلقات `subTest` تُحسب اختباراً واحداً، فأي دمج بندين يكسر الرقم. اذكر صراحةً أن 9 و6 أرضيات بعدّ `unittest` (Ran N tests) لا بعدّ الـsubTests.

**تأكيد:** لم أكتب أو أعدّل أي ملف في هذه المرحلة (قراءة فقط).

PLAN_REVIEW_DONE: 23 notes, 0 blockers

## 42 · user (2026-11-21 09:46:18)

شكراً على النقد؛ أُدمجت كل ملاحظاتك الـMajor ومعظم الـNitpick في `PLAN.md` تحت قسم جديد `### قرارات محسومة بعد نقد المنفذ (الجولة S3-2)` (داخل قسم S3، قبل "أوامر التحقق (المخطط)"). الخطة معتمدة الآن.

**المرحلة ب — تكليف بتنفيذ `T1` فقط (اختبار النبض). ممنوع تنفيذ أي جزء من T2 (لا `main`، لا argparse، لا اختبارات CLI).**

**قبل الكتابة:** أعد قراءة `PLAN.md` قسم S3 كاملاً (T1 + قسم القرارات المحسومة) — القرارات المحسومة تُغلّب على أي صياغة سابقة.

**الملفات المسموح بإنشائها فقط:** `~\Downloads\zizo\duet_demo\make_capsule.py` و`~\Downloads\zizo\duet_demo\test_make_capsule.py`. **ممنوع** لمس `duet_status.py` أو `test_duet_status.py` أو `PLAN.md`/`DUET_LOG.md`/`TASKS.json`/`duet_resume.json` أو `run_tests.cmd`.

**المطلوب في `make_capsule.py` (stdlib فقط، نصوص ثابتة ASCII/English بلا ألوان، `import duet_status`):**
- `VALID_LENSES = ("fish", "scope-guard", "forensic")`.
- ثوابت المطابقة (لا تُطبع أبداً): `GOAL_MARKERS = ("**الهدف:**", "**Goal:**", "Goal:")`، `CONSTRAINT_MARKERS = ("القيود", "Constraints")`.
- `cap_lines(lines, limit=40) -> list`: إن `len(lines) > limit` → أول `limit-1` + `"... (truncated)"`؛ وإلا القائمة كما هي.
- `_load_json_object(path)`: قراءة `utf-8-sig`؛ JSON فاسد → `ValueError(f"invalid JSON in {path}: {e}")`؛ غير dict → `ValueError(f"invalid tasks file {path}: expected a JSON object, got {type(data).__name__}")`؛ مفقود → `FileNotFoundError`.
- `build_capsule(plan_path, tasks_path, resume_path, log_path, lens="fish", stage=None, diff_summary=None, test_evidence=None, concern=None) -> str` بالضبط كما في PLAN.md T1 + القرارات 1–13: التحقق من lens أولاً قبل أي قراءة (`ValueError(f"invalid lens: {lens}")`)؛ PLAN بـ `utf-8-sig`؛ TASKS عبر `_load_json_object`؛ resume عبر `duet_status.load_resume`؛ log عبر `duet_status.parse_log`؛ تحديد stage (القرار 7)؛ المخرج الحرفي `# Inspection Capsule` / `LENS: <lens>` / `## 1. Goal` (project, plan, goal) / `## 2. Constraints` (سطر `stage: <stage> - <title>` + حتى 5 acceptance أو fallback القيود بالقرار 5 أو `- none`) / `## 3. Actual Changes` / `## 4. Test Evidence` / `## 5. Concern & Status` (`concern: ...` + `duet_status.build_summary_line(resume)` حرفياً + `last_log: [<date>] stage=<stage> action=<action> status=<status>` أو `last_log: none`)؛ قص كل سطر لا يبدأ بـ `#` إلى 160 حرفاً (157 + `...`)؛ المرور عبر `cap_lines`؛ `"\n".join(lines)` بلا سطر ختامي فارغ؛ حراس النوع (القرار 3)؛ `project` (القرار 8)؛ `concern` مطوي لسطر واحد أو `none` (القرار 11).

**المطلوب في `test_make_capsule.py` (unittest + tempfile فقط، ≥ 9 اختبارات بعدّ `Ran N tests`؛ `sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))` في الرأس؛ helper مستقل `_write_fixture_set(dirpath)`؛ لا استيراد من `test_duet_status`):** الاختبارات المذكورة في PLAN.md T1 البند 3 (lens غير صالح برسالة `invalid lens: bad` بمسارات وهمية؛ كل ملف مفقود بحلقة subTest → FileNotFoundError؛ TASKS فاسد/قائمة → ValueError تحوي المسار؛ الكبسولة الكاملة: السطران الأولان والعناوين الخمسة بترتيبها و`<= 40` سطراً وبلا سطر ختامي فارغ؛ stage الافتراضي بثلاث حالات subTest؛ ظهور diff/evidence/concern وغيابها (`concern: none`، آخر `verification_result`)؛ سطر الحالة الحرفي `current_stage=S3 | planning_round=1 | rejections=0` مع `rejections={"S3": 0}`؛ BOM+CRLF في PLAN وTASKS مع تأكيد `"\r" not in capsule`؛ PLAN بـ 300 سطر قيود + diff بـ 30 سطراً → `<= 40`) + اختبار مباشر لـ `cap_lines` (45 سطراً → 40 وآخرها `... (truncated)`؛ 10 أسطر تبقى كما هي).

**التحقق المطلوب منك قبل الإرجاع:** شغّل `~\Downloads\zizo\duet_demo\run_tests.cmd unit` وتأكد أن كل اختبارات S1/S2 (19) + T1 تمر (`Ran >= 28 tests ... OK`) بلا كسر لـ `test_duet_status.py`.

**صيغة الإرجاع (مضغوطة):** قائمة الملفات المنشأة + عدد اختبارات T1 + المخرج الحرفي لسطر `Ran N tests` والنتيجة `OK` + أي انحراف واعٍ عن PLAN.md مع سببه (سطر لكل انحراف) + تأكيد صريح أنك لم تلمس أي ملف آخر. إن فشل نفس الاختبار مرتين متتاليتين بعد محاولتي إصلاح، توقف وأعد `[توقف - تكرار مرتين]` مع الخطأ الحرفي بدلاً من المحاولة الثالثة.

## 43 · assistant (2026-11-21 09:46:18)

بدء المرحلة ب (T1). أولاً أعيد قراءة `PLAN.md` قسم S3 مع قسم القرارات المحسومة الجديد قبل أي كتابة.

## 53 · assistant (2026-11-21 09:46:32)

قرأت القرارات المحسومة (1–14 لـT1). أبدأ الآن بإنشاء `make_capsule.py` ثم `test_make_capsule.py` (الملفان المسموح بهما فقط)، ثم أشغّل `run_tests.cmd unit`.

## 63 · assistant (2026-11-21 09:48:13)

تم إنشاء `make_capsule.py`. الآن أكتب `test_make_capsule.py` (helper مستقل + tempfile + addCleanup، بدون أي استيراد من `test_duet_status`).

## 73 · assistant (2026-11-21 09:49:41)

تم إنشاء ملف الاختبار. قبل التشغيل أصلح سطراً غير أنيق في `test_default_stage_resolution` (استخدام `os.mkdir` داخل تعبير شرطي) إلى صيغة صريحة، ثم أشغّل `run_tests.cmd unit`.

## 83 · assistant (2026-11-21 09:50:00)

تم التصحيح. الآن أشغّل أمر التحقق `run_tests.cmd unit` كما تنص الخطة.

## 93 · assistant (2026-11-21 09:50:14)

اكتمل التحقق بنجاح: 32 اختباراً كلها OK بلا أي كسر في `test_duet_status.py`.

[STAGE S3-T1 DONE]

**1. الملفات المنشأة (ملفان جديدان فقط):**
- `~\Downloads\zizo\duet_demo\make_capsule.py` — جديد: `VALID_LENSES`، ثوابت المطابقة `GOAL_MARKERS`/`CONSTRAINT_MARKERS` (لا تُطبع)، `cap_lines(lines, limit=40)`، `_load_json_object(path)` برسائل القرار 13، `build_capsule(...)` بالمخرج الحرفي للأقسام الخمسة + القرارات 1–12 (تحقق lens قبل أي قراءة، تحديد stage بالقرار 7، حراس النوع، `project` بالقرار 8، fallback القيود بالقرار 5، fallback الهدف بالقرار 6، concern مطوي، قص 157+`...` لكل سطر لا يبدأ بـ `#`، ثم `cap_lines`، ثم `"\n".join` بلا سطر ختامي).
- `~\Downloads\zizo\duet_demo\test_make_capsule.py` — جديد: 13 اختباراً (`Ran` فعلي) بـ `unittest` + `tempfile.TemporaryDirectory` + `addCleanup`، helper مستقل `_write_fixture_set(dirpath, ...)`، `sys.path.insert` في الرأس، بلا أي استيراد من `test_duet_status`.
- تصريح بتعديل ملف اختبار: عدّلت `test_make_capsule.py` مرة واحدة بعد إنشائه (استبدال تعبير `os.mkdir` داخل شرط بسطور صريحة في `test_default_stage_resolution`) — تنظيف أسلوبي فقط، لا تغيير في شروط أي assertion.

**2. عدد اختبارات T1:** 13 (الأرضية 9؛ تغطي كل بنود PLAN.md T1 البند 3 + القرار 14 + اختبار `cap_lines` المباشر + اختبار قص 160 حرفاً + اختبار ثابت `VALID_LENSES`).

**3. أمر التحقق والمخرج الحرفي:**
```
~\Downloads\zizo\duet_demo\run_tests.cmd unit
...
test_tasks_not_an_object_raises_value_error_with_path (test_make_capsule.MakeCapsuleTests.test_tasks_not_an_object_raises_value_error_with_path) ... ok
test_valid_lenses_constant (test_make_capsule.MakeCapsuleTests.test_valid_lenses_constant) ... ok

----------------------------------------------------------------------
Ran 32 tests in 0.137s

OK
exit=0
```
(19 اختبار `test_duet_status` كلها ok + 13 `test_make_capsule` كلها ok؛ 32 ≥ 28.)

**4. الانحرافات الواعية عن PLAN.md:**
- لا انحراف جوهري. إضافتان فوق الأرضية: `test_long_content_line_clipped_to_160` (تثبيت القرار 2 حرفياً: الطول = 160 بالضبط) و`test_valid_lenses_constant` — زيادة تغطية فقط.
- اختبار "300 سطر قيود + 30 سطر diff" يستخدم `stage="ZZ"` (مرحلة غير موجودة في TASKS) حتى يُفعّل fallback القيود من PLAN.md فعلاً؛ وإلا لكانت acceptance المرحلة تحجب الـfallback — اختيار مقصود ليختبر البند كما قُصد.

**5. تأكيد:** لم ألمس `duet_status.py` ولا `test_duet_status.py` ولا `run_tests.cmd` ولا أياً من ملفات التخطيط الأربعة؛ ولم أنفّذ أي جزء من T2 (لا `main`، لا argparse، لا اختبارات CLI).

[EXEC_REPORT S3-T1]

## 102 · user (2026-11-21 09:52:38)

تقرير T1 مقبول: تحقق المخطط المستقل أعاد `Ran 32 tests ... OK` والملفان مطابقان للخطة. **T1 معتمدة.**

**المرحلة ب — تكليف بتنفيذ `T2` فقط (واجهة CLI). ممنوع كسر أي اختبار من T1 أو من `test_duet_status.py`، وممنوع لمس `duet_status.py` أو `test_duet_status.py` أو `run_tests.cmd` أو `PLAN.md`/`DUET_LOG.md`/`TASKS.json`/`duet_resume.json`.** الملفان المسموح تعديلهما فقط: `~\Downloads\zizo\duet_demo\make_capsule.py` و`~\Downloads\zizo\duet_demo\test_make_capsule.py`.

**قبل الكتابة:** أعد قراءة `PLAN.md` قسم S3 → `### T2` + القرارات المحسومة 15–21.

**المطلوب في `make_capsule.py` (إضافة فقط؛ لا تغيير في سلوك `build_capsule`/`cap_lines`/`_load_json_object`):**
- `import argparse` و`import sys`.
- `_safe_streams()`: لكل من `sys.stdout` و`sys.stderr`: `if hasattr(stream, "reconfigure"): stream.reconfigure(errors="replace")` (آمن مع `StringIO`).
- `main(argv=None) -> int` بـ `argparse.ArgumentParser(prog="make_capsule", description=...)`:
  - مطلوبة `required=True`: `--plan`, `--tasks`, `--resume`, `--log`.
  - اختيارية: `--lens` (`default="fish"`، **بدون** `choices`، `help="inspection lens: fish | scope-guard | forensic (default: fish)"`)، `--stage`, `--diff`, `--evidence`, `--concern`, `--out` (كلها `default=None`).
  - غياب وسيط مطلوب → `argparse` يرفع `SystemExit(2)` طبيعياً (لا يُلتقط).
  - استدعِ `_safe_streams()` في بداية `main` بعد `parse_args`.
  - داخل كتلة `try` واحدة: `capsule = build_capsule(args.plan, args.tasks, args.resume, args.log, lens=args.lens, stage=args.stage, diff_summary=args.diff, test_evidence=args.evidence, concern=args.concern)` ثم إن `args.out` غير None: `with open(args.out, "w", encoding="utf-8", newline="\n") as fh: fh.write(capsule + "\n")` (كتابة `--out` **داخل** الـtry — القرار 16؛ `PermissionError` لا يُلتقط ومقصود).
  - `except FileNotFoundError as e:` → `path = e.filename if e.filename else "-"`، `message = e.strerror if e.strerror else "file not found"`، `print(f"error: {message} ({path})", file=sys.stderr)`، `return 2`.
  - `except ValueError as e:` → `print(f"error: {e}", file=sys.stderr)`، `return 2` (بلا لاحقة مسار — القرار 17).
  - لا `except Exception` عام. نجاح: `print(capsule)` على stdout ثم `return 0`.
- `if __name__ == "__main__": sys.exit(main())`.
- حدّث docstring الوحدة لذكر S3/T2: main (CLI).

**المطلوب في `test_make_capsule.py` (إضافة صنف `CliTests` بـ ≥ 6 اختبارات بعدّ `Ran N tests`، دون المساس باختبارات T1؛ استخدم `contextlib.redirect_stdout/redirect_stderr` مع `io.StringIO`):**
1. `main([...])` بملفات صالحة → يعيد `0`، و`stdout.getvalue()` يبدأ بـ `"# Inspection Capsule\nLENS: fish\n"` ويساوي `build_capsule(...) + "\n"`، و`stderr` فارغ.
2. `--lens scope-guard --stage S1 --diff x --evidence y --concern z` → `0` وتظهر `LENS: scope-guard` و`stage: S1 - Core` و`- x` و`- y` و`concern: z` في stdout.
3. `--lens bad` → يعيد `2` و`stderr` يحوي `error: invalid lens: bad` و`stdout` فارغ.
4. `--out <tmp>` → يعيد `0`، الملف موجود، قراءته بـ `open(out, "r", encoding="utf-8", newline="")` تساوي `build_capsule(...) + "\n"` بنفس الوسائط، و`"\r" not in content`؛ وكذلك `--out` إلى مجلد غير موجود → `2` و`stderr` يبدأ بـ `error:` (القرار 16).
5. مسار `--plan` مفقود → `2` و`stderr` يحوي `error:` والمسار المفقود؛ `TASKS.json` فاسد → `2` و`stderr` يحوي `invalid JSON` والمسار.
6. `main(["--plan", p, "--tasks", t, "--resume", r])` بدون `--log` → `assertRaises(SystemExit)` و`ctx.exception.code == 2`.
7. اختبار subprocess واحد فقط: `SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "make_capsule.py")`، `m = os.path.join(tmpdir, "missing.txt")`، `subprocess.run([sys.executable, SCRIPT, "--plan", m, "--tasks", m, "--resume", m, "--log", m], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30, env={**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"})` → `returncode == 2`، `"Traceback" not in stderr`، `"error:" in stderr`.

**التحقق المطلوب منك قبل الإرجاع:**
- شغّل `~\Downloads\zizo\duet_demo\run_tests.cmd all` → المتوقع `Ran >= 38 tests ... OK` (19 + 13 + ≥ 6) بلا أي فشل.
- شغّل الأداة فعلياً على ملفات المشروع كدليل: `python ~\Downloads\zizo\duet_demo\make_capsule.py --plan ~\Downloads\zizo\duet_demo\PLAN.md --tasks ~\Downloads\zizo\duet_demo\TASKS.json --resume ~\Downloads\zizo\duet_demo\duet_resume.json --log ~\Downloads\zizo\duet_demo\DUET_LOG.md --stage S3 --lens fish` → يجب أن يخرج بـ 0 ويطبع كبسولة ≤ 40 سطراً (لا تكتب `--out` داخل مجلد المشروع؛ إن أردت اختبار `--out` يدوياً فاكتب إلى `%TEMP%`).

**صيغة الإرجاع — كبسولة مضغوطة (≤ 25 سطراً):** `## Goal` (سطر) / `## Constraints` (سطران) / `## Actual Changes` (الملفان المعدّلان + الدوال المضافة + عدد اختبارات CLI) / `## Test Evidence` (المخرج الحرفي لسطر `Ran N tests` + `OK` + مخرج التشغيل الحقيقي للأداة على ملفات duet_demo كاملاً) / `## Concern` (أي انحراف واعٍ عن PLAN.md مع سببه، أو `none`) + تأكيد صريح أنك لم تلمس أي ملف آخر ولم تكسر T1. إن فشل نفس الاختبار مرتين متتاليتين بعد محاولتي إصلاح، توقف وأعد `[توقف - تكرار مرتين]` مع الخطأ الحرفي بدلاً من المحاولة الثالثة.

## 103 · assistant (2026-11-21 09:52:38)

بدء تنفيذ T2. أعيد قراءة قسم T2 والقرارات 15–21 من `PLAN.md` قبل أي كتابة.

## 113 · assistant (2026-11-21 09:52:56)

قرأت T2 والقرارات 15–21. أبدأ بإضافة CLI إلى `make_capsule.py` (ثلاث تعديلات إضافية: docstring، الاستيرادات، `_safe_streams` + `main`) وصنف `CliTests` إلى `test_make_capsule.py`، بدون المساس بسلوك T1.

## 143 · assistant (2026-11-21 09:54:16)

تمت التعديلات الستة بنجاح. الآن أشغّل التحقق `run_tests.cmd all` والتشغيل الحقيقي للأداة على ملفات المشروع (`--stage S3 --lens fish`) كدليل.

## 157 · assistant (2026-11-21 09:54:34)

اكتمل التحقق: `run_tests.cmd all` → 39 اختباراً كلها OK، والأداة تعمل على ملفات المشروع وتخرج بـ 0 بكبسولة 17 سطراً.

[STAGE S3-T2 DONE]

## Goal
إضافة واجهة CLI (`main`) لـ `make_capsule.py` مع `--out` وexit 2 بلا Traceback، واختبارات CLI في `test_make_capsule.py`.

## Constraints
- stdlib فقط؛ لا تغيير في سلوك `build_capsule`/`cap_lines`/`_load_json_object`؛ التقاط `FileNotFoundError`/`ValueError` فقط؛ `--lens` بلا `choices`.
- لا لمس لـ `duet_status.py`/`test_duet_status.py`/`run_tests.cmd`/ملفات التخطيط الأربعة؛ لا كسر لاختبارات T1 (13) أو S1/S2 (19).

## Actual Changes
- `make_capsule.py`: docstring (+ `S3/T2: main (CLI)`)، `import argparse`/`import sys`، دالة `_safe_streams()` (القرار 15)، `main(argv=None)` (argparse بـ `prog="make_capsule"`، 4 وسائط مطلوبة + `--lens/--stage/--diff/--evidence/--concern/--out`، كتابة `--out` داخل `try` بالقرار 16، `error: <strerror> (<filename>)` لـ FileNotFoundError و`error: <message>` لـ ValueError بالقرار 17، `print(capsule)` + `return 0`)، `if __name__ == "__main__": sys.exit(main())`.
- `test_make_capsule.py` (تصريح بتعديل ملف اختبار — إضافة فقط): استيراد `contextlib`/`io`/`subprocess`/`main`، ثابت `SCRIPT`، helper `_argv`، صنف `CliTests` بـ **7 اختبارات** (نجاح مطابق لـ `build_capsule`+`"\n"`، الخيارات في المخرج، `--lens bad`→2، `--out` UTF-8 بلا `\r` + مجلد مفقود→2، `--plan` مفقود/TASKS فاسد→2، غياب `--log`→SystemExit 2، subprocess واحد). اختبارات T1 لم تُمس.

## Test Evidence
`run_tests.cmd all` → `Ran 39 tests in 0.154s` / `OK` / `exit=0` (19 duet_status + 13 T1 + 7 CLI؛ 39 ≥ 38).
التشغيل الحقيقي (`--stage S3 --lens fish`) → `exit=0`، 17 سطراً:
```
# Inspection Capsule
LENS: fish
## 1. Goal
project: duet_demo
plan: PLAN.md — duet_demo (أدوات duet_status + make_capsule) — الإصدار 3 (S3 معتمدة بعد نقد المنفذ — الجولة S3-2)
goal: بناء أداة صغيرة `duet_status.py` تقرأ سجل الثنائي `DUET_LOG.md` وملف الاستئناف `duet_resume.json` وتعرض حالة المراحل، مع اختبارات `unittest` كاملة.
## 2. Constraints
stage: S3 - make_capsule.py: مولّد كبسولة الفحص للسمكة + test_make_capsule.py
- T1 و T2 معتمدتان بالتحقق المستقل للمخطط (read + run_tests.cmd)
- بوابة الخروج: critic بعدسة fish (بلا sessionID) يعيد PASS أو تُعالج كل Blocker/Major
- لا تعديل على duet_status.py أو test_duet_status.py أو ملفات التخطيط الأربعة
## 3. Actual Changes
files: make_capsule.py, test_make_capsule.py
## 4. Test Evidence
- Ran 19 tests ... OK (independent run by planner); real run printed table (S1/S2/PLAN rows) exit=0; missing file -> exit=2 without Traceback; planning files...
## 5. Concern & Status
concern: none
current_stage=S3 | planning_round=2 | rejections=0
last_log: [2026-11-21 11:51] stage=S3 action=ASSIGN status=T2_in_progress
```

## Concern
none — لا انحراف عن PLAN.md؛ الفرق الوحيد أن `CliTests` تحوي 7 اختبارات (الأرضية 6) لأن بند `--out` وبند "مسار مفقود/TASKS فاسد" اختبار واحد لكل منهما كما كُلّفت. ملاحظة فقط: سطر Test Evidence في الكبسولة الحقيقية قُصّ إلى 160 حرفاً بـ `...` كما هو مقصود بالقرار 2.

**تأكيد:** لم ألمس `duet_status.py` ولا `test_duet_status.py` ولا `run_tests.cmd` ولا أياً من ملفات التخطيط الأربعة، ولم أكتب `--out` داخل مجلد المشروع، ولم يُكسر أي اختبار من T1 أو S1/S2.

[EXEC_REPORT S3-T2]
