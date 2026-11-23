# Review plan only (no code edits)

- id: `ses_e02059baaffeHa0M6w0CO0U65F`
- title: Review plan only (no code edits)
- date: 2026-11-21 12:00:07
- directory: D:/SMS/.hRhR_gateway-service
- parent: `ses_e02073e05ffehgYIVxPQ1PPyjI`
- agent: executor
- model: upstage-studio/claude-fable-5-1-executor
- messages: 16 (user 3, assistant 13)
- archived: false

## 4 · user (2026-11-21 12:00:07)

You are a subagent spawned by another session.
أنت وكيل المنفذ (executor) في ثلاثي OpenCode (planner-reviewer + executor + critic). هذه هي **المرحلة A — مراجعة الخطة فقط**.

⛔ قواعد صارمة لهذا الاستدعاء:
- **ممنوع تماماً كتابة أو تعديل أو إنشاء أي ملف** في هذه المرحلة (لا bridge_doctor.py ولا test_bridge_doctor.py ولا أي شيء آخر).
- **ممنوع قراءة أي ملف يطابق `*opencode.json*`** (بنية الملف موثقة كاملة داخل الخطة أدناه).
- ممنوع تشغيل أي أوامر شيل.
- مسموح لك فقط قراءة ملفات مجلد `D:\SMS\.hRhR_gateway-service\tools` (مثل `run_tests.cmd`) لفهم السياق إن احتجت.
- ردّك = نقد مكتوب فقط.

## المطلوب منك
انقد الخطة التالية تقنياً وأجب في نقاط مرقمة مختصرة:
1. هل هناك غموض أو تعارض في مواصفات الدوال (`check_health`, `check_agents_config`, `check_tools`, `format_report`, `main`) يمنعك من التنفيذ الدقيق؟
2. هل قواعد الحوكمة الخمس في `check_agents_config` واضحة وقابلة للتحقق البرمجي بلا تخمين؟ وما تفسيرك لـ "وجود `* * deny`" (action="*", resource="*", effect="deny")؟
3. هل عدد الاختبارات المطلوب (>=10 في T1، >=5 في T2) وطريقة الـ opener الوهمي + tempfile كافية ومنطقية؟ أي ثغرة في اختبار subprocess على منفذ مغلق `127.0.0.1:1`؟
4. هل هناك مخاطر ويندوز (ترميز، مسارات، `reconfigure`) لم تغطّها الخطة؟
5. ما أي تعديلات صغيرة تقترحها على الخطة قبل البدء؟ (اذكرها كاقتراحات فقط، لا تنفذها).

اختم ردك بسطر: `PLAN_REVIEW: OK` إذا كانت الخطة قابلة للتنفيذ كما هي، أو `PLAN_REVIEW: NEEDS_CHANGES` مع تلخيص التغييرات المطلوبة.

---
# PLAN.md (المسودة 1)

**الهدف:** بناء أداة فحص يومية حقيقية `bridge_doctor.py` تفحص صحة الكوبري الصامت (`127.0.0.1:8020/health`)، وحوكمة صلاحيات الوكلاء الثلاثة في `opencode.json`، ووجود أدوات الفحص والتوثيق الأساسية، مع تغطية اختبارية كاملة بـ `unittest`.

**المجلد الهدف:** `D:\SMS\.hRhR_gateway-service\tools`

**القيود العامة:**
- Python 3 قياسي فقط (`stdlib` فقط: `argparse`, `json`, `os`, `sys`, `urllib.request`, `urllib.error`).
- الملفان الجديدان يُنشآن داخل `D:\SMS\.hRhR_gateway-service\tools` فقط: `bridge_doctor.py` و `test_bridge_doctor.py`.
- **ممنوع تماماً** على المنفذ إنشاء أو تعديل `PLAN.md`, `DUET_LOG.md`, `TASKS.json`, `duet_resume.json` أو تعديل `run_tests.cmd` أو ملفات `duet_demo` أو قراءة أي ملف يطابق `*opencode.json*`.
- الاختبارات تستخدم ملفات مؤقتة عبر `tempfile.TemporaryDirectory` وتمرر `opener` وهمي لـ `check_health` — **لا اتصالات شبكة حقيقية ولا قراءة لأي `*opencode.json*`** في `test_bridge_doctor.py` (أسماء ملفات التست المؤقتة تكون مثلاً `sample_agents_cfg.json`).
- **رسائل البرنامج ومخرجاته ASCII/إنجليزية صافية بدون ألوان ANSI** لتجنب `UnicodeEncodeError` على ويندوز، ولا تطبع أي مفاتيح API من ملف الإعداد أبداً.
- التحقق حصراً عبر `tools\run_tests.cmd unit` (بعد T1) و `tools\run_tests.cmd all` (بعد T2).

## المرجع الدقيق لبنية `opencode.json` (للمطابقة بدون قراءة الملف)
- الكائن الجذري يحتوي `"agents"` (`dict`) بالمفاتيح المطلوبة الثلاثة (`REQUIRED_AGENTS = ("planner-reviewer", "executor", "critic")`).
- كل وكيل يحتوي `"permissions"` وهي `list[dict]`، لكل عنصر المفاتيح: `"action"`, `"resource"`, `"effect"` (`"allow"` | `"deny"` | `"ask"`).
- قواعد الحوكمة المطلوب فحصها في `check_agents_config`:
  1. وجود الوكلاء الثلاثة داخل `data["agents"]`.
  2. لكل وكيل من الثلاثة: وجود القاعدة `{"action": "read", "resource": "*opencode.json*", "effect": "deny"}`.
  3. `"planner-reviewer"`: وجود `shell * deny` و `edit * deny`، مع سماح `subagent executor allow` و `subagent critic allow`.
  4. `"executor"`: وجود `subagent * deny` و `question * deny`، ووجود `edit deny` لكل من `*PLAN.md`, `*DUET_LOG.md`, `*TASKS.json`, `*duet_resume.json`.
  5. `"critic"`: وجود `* * deny`، وسماح `read *` و `grep *` و `glob *`، وعدم وجود أي قاعدة `effect == "allow"` على `action` من `("edit", "shell", "subagent", "write")`.

## S1 — `bridge_doctor.py` + `test_bridge_doctor.py`

### T1 (اختبار النبض) — دوال الفحص الأساسية + `format_report` + اختبارات الوحدة
1. ثابت الوحدة: `REQUIRED_AGENTS = ("planner-reviewer", "executor", "critic")`.
2. `check_health(health_url="http://127.0.0.1:8020/health", timeout=3.0, opener=None) -> dict`:
   - تستخدم `opener(health_url, timeout=timeout)` إن مُرِّرت، وإلا `urllib.request.urlopen`.
   - تقرأ المخرج كـ UTF-8 JSON dict وتتحقق من: `status == "ok"`، `session_configured is True`، `session_valid is True`، و `isinstance(models_count, int) and not isinstance(models_count, bool) and models_count >= 1`.
   - تلتقط `(OSError, ValueError, TypeError)` بوضوح ولا ترفع استثناء؛ تعيد dict بالمفاتيح الأربعة: `{"name": "bridge_health", "ok": bool, "status": "PASS"|"FAIL", "detail": str}`.
3. `check_agents_config(config_path) -> dict`:
   - تقرأ JSON بـ `encoding="utf-8-sig"` وتتحقق من القواعد الخمس المذكورة في قسم المرجع أعلاه.
   - تلتقط `(OSError, ValueError, TypeError)` (ملف مفقود / مجلد / JSON فاسد / غير dict) ولا ترفع استثناء؛ تعيد `{"name": "agents_governance", "ok": bool, "status": "PASS"|"FAIL", "detail": str}` مع ذكر سبب الفشل بوضوح دون طبع أي قيم حساسة.
4. `check_tools(tool_paths=None) -> dict`:
   - إذا `tool_paths is None` تفحص المسارات الثلاثة الافتراضية (`run_tests.cmd`, `duet_status.py`, `make_capsule.py`).
   - تقبل `(label, path)` pairs أو dict وتتحقق أن كل ملف موجود فعلياً وحجمه `> 0` (`os.path.isfile(path) and os.path.getsize(path) > 0`).
   - تعيد `{"name": "tools_suite", "ok": bool, "status": "PASS"|"FAIL", "detail": str}`.
5. `format_report(checks) -> str`:
   - جدول نص خام ASCII بالأعمدة: `CHECK | STATUS | DETAIL` + فاصل + الصفوف + سطر ختامي فارغ ثم سطر إجمالي: `OVERALL: PASS (X/Y checks passed)` أو `OVERALL: FAIL (X/Y checks passed)`.
6. اختبارات T1 في `test_bridge_doctor.py` (`>= 10` اختبارات بـ `tempfile.TemporaryDirectory` + `opener` وهمي):
   - `check_health` نجاح؛ فشل بسبب `session_valid=False` أو `status!="ok"` أو `models_count=0`؛ خطأ شبكة (`OSError`)؛ JSON فاسد.
   - `check_agents_config` نجاح كامل؛ نقص وكيل؛ فقدان حظر `*opencode.json*`؛ وجود `shell allow` في `critic`؛ ملف مفقود / JSON فاسد.
   - `check_tools` نجاح؛ ملف مفقود أو فارغ (0 بايت).
   - `format_report` نجاح كامل وفشل جزئي.

### T2 — واجهة CLI `main` + `--json` + اختبارات CLI و subprocess
1. `_safe_streams()` لـ `sys.stdout` و `sys.stderr` (`reconfigure(errors="replace")` إن توفرت).
2. `main(argv=None) -> int` بـ `argparse` (`prog="bridge_doctor"`):
   - وسائط اختيارية بقيم افتراضية واضحة:
     - `--health-url` (افتراضي `"http://127.0.0.1:8020/health"`)
     - `--config` (افتراضي `os.path.join(os.path.expanduser("~"), ".config", "opencode", "opencode.json")`)
     - `--run-tests` (افتراضي `r"D:\SMS\.hRhR_gateway-service\tools\run_tests.cmd"`)
     - `--duet-status` (افتراضي `r"~\Downloads\zizo\duet_demo\duet_status.py"`)
     - `--make-capsule` (افتراضي `r"~\Downloads\zizo\duet_demo\make_capsule.py"`)
     - `--timeout` (`type=float`, افتراضي `3.0`)
     - `--json` (`action="store_true"`)
   - تشغّل الفحوصات الثلاثة؛ لو `--json` تطبع كائن JSON (`overall`, `passed`, `total`, `checks`)؛ وإلا تطبع `format_report(checks)`.
   - تعيد `0` إذا نجحت كل الفحوصات، و `1` إذا فشل أي فحص.
   - `if __name__ == "__main__": sys.exit(main())`.
3. اختبارات T2 في `test_bridge_doctor.py` (`>= 5` اختبارات):
   - `main` نجاح (`0`)؛ `main` فشل (`1`)؛ `main(["--json", ...])` بمخرجات JSON صالحة؛ اختبار `subprocess` على ملفات مؤقتة ومنفذ مغلق (`127.0.0.1:1`) يعيد `1` بدون `Traceback`.

**بوابة الخروج:** التحقق المستقل عبر `tools\run_tests.cmd all` ثم استدعاء `critic` (`LENS: fish`) -> `[FINAL_APPROVED]`.
---

تذكير أخير: **لا تكتب ولا تعدّل أي ملف الآن. نقد فقط.**

## 5 · assistant (2026-11-21 12:00:07)

سأقرأ `run_tests.cmd` أولاً للتأكد من أن بوابة التحقق في الخطة تكتشف ملف الاختبار الجديد فعلياً، ثم أقدم النقد.

## 15 · assistant (2026-11-21 12:00:24)

قرأت `run_tests.cmd` (31 سطراً). النقد التقني أدناه — بدون أي تعديل ملفات.

## ملاحظة حرجة أولاً (بوابة التحقق نفسها)
- `run_tests.cmd` السطور 13–16 و22–25 و26–29: `exit /b %ERRORLEVEL%` موجود **داخل بلوك أقواس**، و`%ERRORLEVEL%` في cmd يُوسَّع وقت تحليل البلوك لا وقت التنفيذ. النتيجة:
  - وضع `unit`: لو فشل `test_bridge_doctor.py`، السطر 15 يعيد قيمة الـ errorlevel القديمة (0 من السطر 11) ⇒ **الفشل يُبلَّغ كنجاح (exit 0)**.
  - وضع `all`: `if errorlevel 1` (سطر 24) يُقيَّم ديناميكياً فيكتشف الفشل، لكنه ينفذ `exit /b 0` بالقيمة المتجمدة ⇒ نفس المشكلة.
  - المنفذ ممنوع من تعديل `run_tests.cmd`. لذلك يجب أن يَعتمد الحكم في T1/T2 على **نص المخرج** (`OK` / `FAILED (failures=..)`) لا على كود الخروج، وأن يُبلَّغ المخطط بهذا العيب ليقرر إصلاحه (استخدام `setlocal EnableDelayedExpansion` + `!ERRORLEVEL!`، أو إخراج `exit` خارج الأقواس).
- الاكتشاف نفسه سليم: `unittest discover -s "%~dp0." -p "test_*.py"` يُدرج مجلد `tools` في `sys.path` فيعمل `import bridge_doctor` بلا `__init__.py`.
- السطر 11 يشغّل `fable_eval_lab\test_bridge_v4_unit.py` أولاً؛ لو فشل هو، اختباراتنا لا تُشغَّل أصلاً (اعتماد خارجي يجب الانتباه له عند قراءة المخرج).

## 1) غموض/تعارض في مواصفات الدوال
1. **حقن الـ opener في `main` غير محدد:** اختبار "`main` نجاح (0)" يتطلب نجاح `check_health` بلا شبكة حقيقية، لكن توقيع `main(argv=None)` لا يوفر منفذاً لذلك. يلزم إما `main(argv=None, opener=None)` أو تعليمة صريحة باستخدام `unittest.mock.patch("bridge_doctor.urllib.request.urlopen")`. **هذا يمنع التنفيذ الدقيق لـ T2 كما هي.**
2. **عقد كائن الاستجابة في `check_health`:** غير محدد هل الـ opener يعيد كائناً يدعم `with` أم فقط `.read()`. أقترح تثبيت: "يعيد كائناً له `.read() -> bytes`؛ يُغلق عبر `.close()` إن وُجد"، والاختبار يعيد `io.BytesIO`.
3. **JSON صالح لكنه ليس dict** (مثلاً قائمة): `data.get(...)` يرفع `AttributeError` الذي **ليس** ضمن `(OSError, ValueError, TypeError)`. يلزم فحص `isinstance(data, dict)` صريح قبل الوصول، أو إضافة `AttributeError`/`KeyError` للالتقاط. ينطبق أيضاً على `check_agents_config` (`data["agents"]` ليس dict، `permissions` ليست list، عنصر ليس dict).
4. **`check_tools`:** عبارة "تقبل pairs أو dict" مع غياب تسميات الافتراضيات؛ والمسارات الافتراضية الثلاثة مذكورة فقط في قسم T2 (CLI) لا في T1. أقترح ثوابت على مستوى الوحدة (`DEFAULT_RUN_TESTS`, `DEFAULT_DUET_STATUS`, `DEFAULT_MAKE_CAPSULE`) وتسميات ثابتة (`run_tests`, `duet_status`, `make_capsule`) وقبول نوع واحد فقط (قائمة أزواج) لتبسيط الاختبار.
5. **`format_report`:** عرض الأعمدة (ثابت/ديناميكي)، رمز الفاصل، وهل يُقص `DETAIL` الطويل — كلها غير محددة، فتصبح أي تأكيدات تنسيقية في الاختبارات تحكّمية. أقترح: عرض ديناميكي = أطول قيمة، فاصل من `-` بطول الجدول، بلا قص.
6. **`--json`:** نوع `overall` (`"PASS"/"FAIL"` أم bool) غير محدد. أقترح نصاً `"PASS"/"FAIL"` لمطابقة التقرير النصي.
7. **`detail` في `check_agents_config`:** أول قاعدة فاشلة أم كل القواعد؟ أقترح تجميع كل الانتهاكات مفصولة بـ `; ` (أنفع للتشخيص اليومي).

## 2) وضوح قواعد الحوكمة الخمس
- قابلة للتحقق برمجياً بشرط تثبيت دلالة واحدة: **مطابقة نصية تامة (case-sensitive) لثلاثية `(action, resource, effect)`** مع تجاهل أي مفاتيح إضافية في العنصر. يجب النص على ذلك لأن أي اختلاف حرفي في الملف الحقيقي (مثلاً `**/opencode.json*` بدل `*opencode.json*`) سيُسقط الفحص دون أن نستطيع التأكد لأننا ممنوعون من قراءة الملف — المخطط هو الضامن لصحة النصوص الحرفية.
- تفسيري لـ `* * deny` عند `critic`: قاعدة **المنع الافتراضي الشامل** (`action="*"`, `resource="*"`, `effect="deny"`) تمنع كل أداة على كل مورد، ثم تُستثنى صراحةً بقواعد `read * allow` و`grep * allow` و`glob * allow`. الفاحص يتحقق من **وجود** هذه العناصر فقط ولا يحاكي ترتيب/أسبقية القواعد في OpenCode — ينبغي التصريح بذلك في الخطة حتى لا يُفهم الفحص على أنه تحقق دلالي كامل.
- ثغرات دلالية (كاقتراحات لا أكثر): قاعدة 5 لا تمنع `question`/`webfetch` allow للـ critic؛ قاعدة 4 تمنع `edit` على ملفات القيادة لكن لا تذكر `write` (التفاف محتمل). قاعدة 3 `edit * deny` للـ planner يبدو متعارضاً مع كون الـ planner مالك `PLAN.md` — إن كان الملف الحقيقي يضيف `write`/`edit` خاصاً بعدها، فالفحص الحالي سيمرّ لأنه يفحص الوجود فقط؛ لا مشكلة تنفيذية لكنها نقطة توضيح.
- عنصر `permissions` مشوّه (ناقص مفاتيح): هل يُعدّ فشلاً أم يُتجاهل؟ يلزم قرار (أقترح: فشل مع ذكر رقم الوكيل والفهرس فقط دون قيم).

## 3) كفاية الاختبارات وثغرة `127.0.0.1:1`
- الأعداد (≥10 / ≥5) ومنهج `tempfile.TemporaryDirectory` + opener وهمي مناسبة ومنطقية ومحققة للعزل.
- اختبار subprocess: يجب أن يمرر **كل** المسارات صراحةً (`--config` لملف مؤقت باسم `sample_agents_cfg.json`، و`--run-tests/--duet-status/--make-capsule` لملفات مؤقتة) حتى لا يعتمد الاختبار على الملفات الحقيقية ولا يقرأ `opencode.json` الحقيقي بالافتراضي.
- المنفذ 1: على ويندوز غالباً `ConnectionRefusedError` فوري (RST)، لكن جدار الحماية قد يُسقط الحزمة بصمت فينتظر حتى `--timeout`؛ لذلك يجب تمرير `--timeout 1` (أو أقل) وضبط `subprocess.run(..., timeout=30)`. بديل أكثر حتمية: فتح `socket` على `("127.0.0.1", 0)` لأخذ منفذ حر ثم إغلاقه واستخدامه (ضمان رفض الاتصال).
- التأكيد: `returncode == 1` و`"Traceback" not in stderr`، مع `text=True, encoding="utf-8", errors="replace"` و`sys.executable`.
- اختبارات `main` يجب أن تلتقط `stdout` عبر `contextlib.redirect_stdout(io.StringIO())`؛ وهذا يفرض أن `_safe_streams` يحرس بـ `hasattr(stream, "reconfigure")` لأن `StringIO` لا يملكه.

## 4) مخاطر ويندوز غير المغطاة
1. عيب كود الخروج في `run_tests.cmd` (أعلاه) — أخطر نقطة.
2. `reconfigure` على `StringIO` (أعلاه)؛ أيضاً لا تستدعِ `_safe_streams` إلا داخل `main`/`__main__` مع الحارس.
3. `TemporaryDirectory` على ويندوز يفشل في التنظيف لو بقي ملف مفتوحاً — كل القراءات/الكتابات عبر `with open(...)`.
4. سلاسل `help` في argparse: أي `%` حرفي يجب مضاعفته `%%` وإلا `ValueError` عند `--help`.
5. `os.path.expanduser("~")` يعتمد على `USERPROFILE` — سليم، لكن مسار الإعداد الافتراضي سيكون مختلفاً إن شُغّل بحساب آخر (لا مشكلة، فقط للعلم).
6. السرية: قراءة `data["agents"]` فقط وعدم طباعة أي قيمة من بقية الجذر؛ رسائل `json.JSONDecodeError` تحوي الموضع فقط لا المحتوى — آمنة.
7. `urllib.error.URLError`/`HTTPError` كلاهما `OSError`، و`JSONDecodeError`/`UnicodeDecodeError` كلاهما `ValueError` — تغطية الالتقاط صحيحة.

## 5) تعديلات صغيرة مقترحة (بدون تنفيذ)
1. إضافة `opener=None` إلى توقيع `main` (أو تصريح باستخدام `mock.patch`).
2. تثبيت عقد كائن الاستجابة (`.read()` + `.close()` اختياري) وفحص `isinstance(..., dict)` صريح في الدالتين.
3. نقل المسارات الافتراضية الثلاثة إلى ثوابت وحدة + تسميات ثابتة، وتضييق `check_tools` لقائمة أزواج.
4. تثبيت مواصفة `format_report` (عرض ديناميكي، فاصل `-`، بلا قص) ونوع `overall` في `--json`.
5. اختبار subprocess بمنفذ حر مغلق ديناميكياً أو `--timeout 1` مع كل المسارات مؤقتة.
6. تجميع كل انتهاكات الحوكمة في `detail`، وتحديد تعامل العناصر المشوهة.
7. تبليغ المخطط بعيب `%ERRORLEVEL%` في `run_tests.cmd` واعتماد نص المخرج كمعيار قبول حتى إصلاحه (خارج نطاقي).

`PLAN_REVIEW: NEEDS_CHANGES` — التغييرات الملزمة: (1) منفذ حقن opener في `main`، (2) فحص `isinstance(dict)` صريح/توسيع الالتقاط، (3) تثبيت مواصفة `format_report` و`--json.overall`، (4) اختبار subprocess بمسارات مؤقتة كاملة + timeout قصير، (5) اعتماد نص مخرج `unittest` لا كود خروج `run_tests.cmd` حتى يُصلَح عيب التوسيع المبكر.

[EXECUTOR_FEEDBACK]

## 24 · user (2026-11-21 12:05:49)

تم اعتماد الخطة (المسودة 2) بعد دمج تغييراتك الخمسة الملزمة كلها. الآن **المرحلة B — نفّذ T1 فقط** (اختبار النبض). لا تنفذ أي شيء من T2 الآن (لا `main`، لا `_safe_streams`، لا argparse، لا اختبارات CLI/subprocess).

⛔ القيود الصارمة:
- تعدّل/تنشئ **فقط**: `D:\SMS\.hRhR_gateway-service\tools\bridge_doctor.py` و `D:\SMS\.hRhR_gateway-service\tools\test_bridge_doctor.py`.
- ممنوع لمس `PLAN.md`, `DUET_LOG.md`, `TASKS.json`, `duet_resume.json`, `run_tests.cmd`, أو أي ملف `duet_demo`.
- **ممنوع قراءة أي ملف يطابق `*opencode.json*`** (لك وللاختبارات). ملفات التست المؤقتة بأسماء مثل `sample_agents_cfg.json`.
- لا اتصالات شبكة حقيقية في الاختبارات؛ لا ألوان ANSI؛ مخرجات ASCII/إنجليزية صافية؛ لا طباعة أي قيم من خارج `data["agents"]`.
- كل قراءة/كتابة عبر `with open(...)`.
- stdlib فقط. التحقق النهائي سيجريه المخطط عبر `run_tests.cmd unit`؛ يمكنك تشغيل اختباراتك محلياً بـ `python -m unittest test_bridge_doctor -v` من داخل مجلد tools إن سمحت صلاحياتك، ومعيار القبول = نص المخرج (`Ran N tests` + `OK`) لا كود الخروج.

## مواصفة T1 (من PLAN.md المسودة 2)

### ثوابت الوحدة في `bridge_doctor.py`
- `REQUIRED_AGENTS = ("planner-reviewer", "executor", "critic")`
- `DEFAULT_HEALTH_URL = "http://127.0.0.1:8020/health"`
- `DEFAULT_CONFIG = os.path.join(os.path.expanduser("~"), ".config", "opencode", "opencode.json")`
- `DEFAULT_RUN_TESTS = r"D:\SMS\.hRhR_gateway-service\tools\run_tests.cmd"`
- `DEFAULT_DUET_STATUS = r"~\Downloads\zizo\duet_demo\duet_status.py"`
- `DEFAULT_MAKE_CAPSULE = r"~\Downloads\zizo\duet_demo\make_capsule.py"`
- `DEFAULT_TOOL_PATHS = (("run_tests", DEFAULT_RUN_TESTS), ("duet_status", DEFAULT_DUET_STATUS), ("make_capsule", DEFAULT_MAKE_CAPSULE))`
- `CATCH = (OSError, ValueError, TypeError, AttributeError, KeyError)` — تُلتقط في الفحوصات الثلاثة ولا تُرفع أبداً.

### 1) `check_health(health_url=DEFAULT_HEALTH_URL, timeout=3.0, opener=None) -> dict`
- تستخدم `opener(health_url, timeout=timeout)` إن مُرِّرت، وإلا `urllib.request.urlopen`.
- عقد كائن الاستجابة: له `.read() -> bytes`؛ يُغلق عبر `.close()` إن وُجد (الاختبارات تعيد `io.BytesIO`).
- فك UTF-8 ثم `json.loads`؛ فحص `isinstance(data, dict)` صريح قبل أي وصول؛ التحقق من: `status == "ok"`, `session_configured is True`, `session_valid is True`, `isinstance(models_count, int) and not isinstance(models_count, bool) and models_count >= 1`.
- تلتقط `CATCH`؛ تعيد `{"name": "bridge_health", "ok": bool, "status": "PASS"|"FAIL", "detail": str}`.

### 2) `check_agents_config(config_path) -> dict`
- تقرأ JSON بـ `encoding="utf-8-sig"` عبر `with open`؛ تفحص صراحةً `isinstance(data, dict)`، `isinstance(data.get("agents"), dict)`، `isinstance(permissions, list)`، وكل عنصر `dict` بالمفاتيح الثلاثة `action/resource/effect` (وإلا انتهاك `malformed` يُذكر باسم الوكيل ورقم الفهرس فقط، دون قيم).
- دلالة المطابقة: مطابقة نصية تامة حساسة لحالة الأحرف للثلاثية `(action, resource, effect)` مع تجاهل أي مفاتيح إضافية. الفحص وجودي فقط.
- القواعد الخمس:
  1. وجود الوكلاء الثلاثة داخل `data["agents"]`.
  2. لكل وكيل من الثلاثة: وجود `{"action": "read", "resource": "*opencode.json*", "effect": "deny"}`.
  3. `planner-reviewer`: وجود `shell * deny` و `edit * deny`، و `subagent executor allow` و `subagent critic allow`.
  4. `executor`: وجود `subagent * deny` و `question * deny`، و `edit <res> deny` لكل من `*PLAN.md`, `*DUET_LOG.md`, `*TASKS.json`, `*duet_resume.json`.
  5. `critic`: وجود `* * deny`، وسماح `read * allow`, `grep * allow`, `glob * allow`، وعدم وجود أي قاعدة `effect == "allow"` على `action` من `("edit", "shell", "subagent", "write")`.
- `detail` عند الفشل = تجميع **كل** الانتهاكات مفصولة بـ `"; "`.
- تلتقط `CATCH` (ملف مفقود / مجلد / JSON فاسد / غير dict)؛ تعيد `{"name": "agents_governance", "ok": bool, "status": "PASS"|"FAIL", "detail": str}` دون طبع أي قيم حساسة.

### 3) `check_tools(tool_paths=None) -> dict`
- إذا `None` تستخدم `DEFAULT_TOOL_PATHS`؛ تقبل قائمة/صفاً من أزواج `(label, path)` (و`dict` يُحوَّل عبر `.items()`).
- كل ملف: `os.path.isfile(path) and os.path.getsize(path) > 0`.
- `detail`: `missing_or_empty: <labels>` أو `all N tools present`.
- تعيد `{"name": "tools_suite", "ok": bool, "status": "PASS"|"FAIL", "detail": str}`.

### 4) `format_report(checks) -> str`
- جدول ASCII بالأعمدة `CHECK | STATUS | DETAIL`؛ عرض كل عمود ديناميكي = أطول قيمة (مع العنوان)؛ فاصل من `-` بطول سطر العنوان؛ بلا قص لـ DETAIL.
- ثم سطر فارغ ثم `OVERALL: PASS (X/Y checks passed)` أو `OVERALL: FAIL (X/Y checks passed)`.

### 5) اختبارات T1 في `test_bridge_doctor.py` (>= 10، `unittest` + `tempfile.TemporaryDirectory` + opener وهمي يعيد `io.BytesIO`)
- `check_health`: نجاح؛ فشل `session_valid=False`؛ فشل `status!="ok"`؛ فشل `models_count=0`؛ خطأ شبكة (`OSError`)؛ JSON فاسد؛ JSON صالح لكنه قائمة.
- `check_agents_config`: نجاح كامل؛ نقص وكيل؛ فقدان حظر `*opencode.json*`؛ `shell allow` في `critic`؛ ملف مفقود؛ JSON فاسد؛ عنصر permissions مشوّه؛ تجميع أكثر من انتهاك في `detail`.
- `check_tools`: نجاح؛ ملف مفقود أو فارغ (0 بايت).
- `format_report`: نجاح كامل وفشل جزئي (تأكيد على `OVERALL:` ووجود الأعمدة الثلاثة فقط، بلا تأكيدات عرض حرفية).

## التقرير المطلوب عند الانتهاء
1. قائمة الملفات التي أنشأتها/عدّلتها (مساراتها فقط).
2. قائمة أسماء الاختبارات المضافة وعددها.
3. إن شغّلت الاختبارات محلياً: نص المخرج الحرفي (`Ran N tests` / `OK` أو الفشل).
4. أي انحراف عن المواصفة مع السبب.
إذا تكرر نفس الفشل مرتين دون حل، توقف وأعد `[توقف - تكرار مرتين]` مع وصف الافتراض الذي تشك فيه.

## 25 · assistant (2026-11-21 12:05:49)

بدء المرحلة B — T1. سأفحص أولاً هل الملفان موجودان مسبقاً في مجلد `tools` قبل الكتابة.

## 35 · assistant (2026-11-21 12:06:03)

الملفان غير موجودين — سأنشئ `bridge_doctor.py` أولاً وفق مواصفة T1 (الثوابت + الفحوصات الثلاثة + `format_report`، بلا أي شيء من T2).

## 45 · assistant (2026-11-21 12:07:51)

تم إنشاء `bridge_doctor.py`. الآن أنشئ `test_bridge_doctor.py` بـ 19 اختباراً (opener وهمي يعيد `io.BytesIO` + ملفات مؤقتة باسم `sample_agents_cfg.json`، بلا شبكة وبلا قراءة أي `opencode.json`).

## 55 · assistant (2026-11-21 12:09:02)

تم إنشاء ملف الاختبارات. الآن أشغّل الاختبارات محلياً من داخل مجلد `tools` للتحقق من نص المخرج (`Ran N tests` + `OK`).

## 65 · assistant (2026-11-21 12:09:18)

الاختبارات نجحت: `Ran 23 tests` + `OK`. ملاحظة: `Exit code: 1` و`NativeCommandError` في المخرج هما أثر جانبي لإعادة توجيه `2>&1` في PowerShell (unittest يكتب تقريره على stderr) وليس فشلاً — معيار القبول المتفق عليه هو نص المخرج، وهو `OK`.

## تقرير تسليم T1

**1) الملفات المنشأة (لم يُلمس أي ملف آخر):**
- `D:\SMS\.hRhR_gateway-service\tools\bridge_doctor.py` — الثوابت (`REQUIRED_AGENTS`, `DEFAULT_*`, `DEFAULT_TOOL_PATHS`, `CATCH`) + `check_health` + `check_agents_config` + `check_tools` + `format_report`. لا `main`/`_safe_streams`/argparse (T2 لم يُنفَّذ).
- `D:\SMS\.hRhR_gateway-service\tools\test_bridge_doctor.py` — ملف جديد (تصريح: إنشاء ملف اختبار جديد، بلا حذف/تخطي/إضعاف لأي اختبار قائم).

**2) الاختبارات المضافة — 23 اختباراً (المطلوب ≥10):**
- `CheckHealthTests` (8): `test_health_success`, `test_health_fail_session_valid_false`, `test_health_fail_status_not_ok`, `test_health_fail_models_count_zero`, `test_health_fail_models_count_bool_rejected`, `test_health_network_error_is_caught`, `test_health_invalid_json`, `test_health_json_list_not_dict`.
- `CheckAgentsConfigTests` (11): `test_config_full_success`, `test_config_utf8_bom_accepted`, `test_config_missing_agent`, `test_config_missing_opencode_deny`, `test_config_critic_shell_allow_rejected`, `test_config_file_missing`, `test_config_invalid_json`, `test_config_root_not_dict`, `test_config_malformed_permission_entry`, `test_config_multiple_violations_aggregated`, `test_config_does_not_leak_secret_values`.
- `CheckToolsTests` (2): `test_tools_success`, `test_tools_missing_or_empty`.
- `FormatReportTests` (2): `test_report_all_pass`, `test_report_partial_fail`.
- كل fixtures الإعداد تُكتب في `tempfile.TemporaryDirectory` باسم `sample_agents_cfg.json`؛ الـ opener الوهمي يعيد `io.BytesIO`؛ لا شبكة ولا قراءة لأي `*opencode.json*`.

**3) أمر التحقق والمخرج الحرفي (آخر سطور):**
```
& "C:\Python315\python.exe" -m unittest test_bridge_doctor -v 2>&1   (workdir: tools)
...
test_health_network_error_is_caught (test_bridge_doctor.CheckHealthTests.test_health_network_error_is_caught) ... ok
test_health_success (test_bridge_doctor.CheckHealthTests.test_health_success) ... ok
test_tools_missing_or_empty (test_bridge_doctor.CheckToolsTests.test_tools_missing_or_empty) ... ok
test_tools_success (test_bridge_doctor.CheckToolsTests.test_tools_success) ... ok
test_report_all_pass (test_bridge_doctor.FormatReportTests.test_report_all_pass) ... ok
test_report_partial_fail (test_bridge_doctor.FormatReportTests.test_report_partial_fail) ... ok
----------------------------------------------------------------------
Ran 23 tests in 0.059s
OK
```

**4) انحرافات/قرارات صغيرة خارج نص المواصفة (للعلم):**
- `format_report([])` يعيد `OVERALL: FAIL (0/0 checks passed)` — المواصفة لم تحدد الحالة الفارغة؛ اخترت FAIL لأن "لا فحوصات" لا يعني صحة.
- `check_health`: لو أعاد `.read()` شيئاً غير `bytes` يُحوَّل بـ `str()` بدل الرفع (توسعة دفاعية فقط).
- كل `detail` يمر عبر `_ascii()` (أي حرف غير ASCII يصبح `?`) ضماناً لقيد "ASCII صافٍ"؛ رسائل الاستثناء تُدرج بصيغة `ExceptionType: message` فقط.
- أضفت 4 اختبارات زائدة عن القائمة (bool لـ `models_count`، BOM، جذر غير dict، عدم تسريب قيمة سرية من خارج `data["agents"]`) — إضافات لا استبدال.
- تذكير بما رُفع سابقاً: `run_tests.cmd` السطر 15/24 يستخدم `%ERRORLEVEL%` داخل أقواس، فكود خروجه غير موثوق؛ الاعتماد على نص `OK`/`FAILED` عند التحقق عبر `run_tests.cmd unit` (خارج نطاقي تعديله).

[STAGE T1 DONE]

## 74 · user (2026-11-21 12:12:21)

تم اعتماد T1 بالتحقق المستقل (`run_tests.cmd unit` -> `Ran 25 tests OK` + `Ran 23 tests OK`). الآن **نفّذ T2 فقط** وفق PLAN.md (المسودة 2). لا تغيّر سلوك دوال T1 المعتمدة إلا إن لزم إصلاح ضروري موثق.

⛔ القيود الصارمة (كما في T1):
- تعدّل **فقط**: `D:\SMS\.hRhR_gateway-service\tools\bridge_doctor.py` و `D:\SMS\.hRhR_gateway-service\tools\test_bridge_doctor.py`.
- ممنوع لمس `PLAN.md`, `DUET_LOG.md`, `TASKS.json`, `duet_resume.json`, `run_tests.cmd`, أو أي ملف `duet_demo`.
- **ممنوع قراءة أي ملف يطابق `*opencode.json*`** (لك وللاختبارات). الاختبارات تمرر `--config` لملف مؤقت باسم `sample_agents_cfg.json` **صراحةً دائماً** حتى لا يُستخدم `DEFAULT_CONFIG` الحقيقي.
- لا اتصالات شبكة حقيقية في اختبارات `main` (استخدم حقن `opener`)؛ اختبار subprocess الوحيد يتصل بمنفذ محلي حر مغلق فقط.
- لا ألوان ANSI؛ مخرجات ASCII/إنجليزية صافية؛ سلاسل `help` في argparse بلا أي `%` حرفي؛ `with open` دائماً؛ stdlib فقط.
- لا تحذف/تُضعف أي اختبار من اختبارات T1 الـ 23.

## مواصفة T2

### 1) `_safe_streams()`
- لـ `sys.stdout` و `sys.stderr`: تستدعي `stream.reconfigure(errors="replace")` **فقط إذا `hasattr(stream, "reconfigure")`** (لأن `io.StringIO` لا يملكه)؛ تلتقط أي استثناء داخلياً ولا ترفع؛ تُستدعى داخل `main` فقط.

### 2) `main(argv=None, opener=None) -> int`
- `argparse.ArgumentParser(prog="bridge_doctor")` بالوسائط:
  - `--health-url` (افتراضي `DEFAULT_HEALTH_URL`)
  - `--config` (افتراضي `DEFAULT_CONFIG`)
  - `--run-tests` (افتراضي `DEFAULT_RUN_TESTS`)
  - `--duet-status` (افتراضي `DEFAULT_DUET_STATUS`)
  - `--make-capsule` (افتراضي `DEFAULT_MAKE_CAPSULE`)
  - `--timeout` (`type=float`, افتراضي `3.0`)
  - `--json` (`action="store_true"`)
- `opener` يُمرَّر كما هو إلى `check_health(health_url, timeout=..., opener=opener)`.
- تشغّل الفحوصات الثلاثة بالترتيب: `check_health`, `check_agents_config(config)`, `check_tools([("run_tests", run_tests), ("duet_status", duet_status), ("make_capsule", make_capsule)])`.
- لو `--json`: تطبع `json.dumps({"overall": "PASS"|"FAIL", "passed": int, "total": int, "checks": [قائمة dicts الفحوصات]}, indent=2)`؛ وإلا تطبع `format_report(checks)`.
- تعيد `0` إذا نجحت كل الفحوصات، و`1` إذا فشل أي فحص. لا `Traceback` في أي حالة.
- `if __name__ == "__main__": sys.exit(main())`.
- أضف `import argparse` و `import sys` (و`io` إن لزم) لمستوى الوحدة.

### 3) اختبارات T2 في `test_bridge_doctor.py` (>= 5 اختبارات جديدة، صنف مثل `MainCliTests`)
- كل اختبار ينشئ `TemporaryDirectory` ويكتب `sample_agents_cfg.json` + 3 ملفات أدوات غير فارغة، ويمرر `--config/--run-tests/--duet-status/--make-capsule` صراحةً.
- `main` نجاح: `opener` وهمي بحمولة صحيحة + إعداد صالح + أدوات موجودة -> يعيد `0`، والتقاط stdout عبر `contextlib.redirect_stdout(io.StringIO())` والتأكد من `OVERALL: PASS (3/3 checks passed)`.
- `main` فشل: (مثلاً `opener` يرفع `OSError`) -> يعيد `1` و`OVERALL: FAIL`.
- `main(["--json", ...])`: `json.loads(stdout)` صالح، يحوي المفاتيح `overall/passed/total/checks`، `overall` نص `"PASS"` أو `"FAIL"`، `total == 3`، و`checks` قائمة بطول 3.
- `--json` في حالة فشل: `overall == "FAIL"` و`passed < total`.
- اختبار subprocess: احصل على منفذ حر عبر `socket.socket()` + `bind(("127.0.0.1", 0))` + `getsockname()[1]` ثم أغلق الـ socket؛ شغّل `subprocess.run([sys.executable, <مسار bridge_doctor.py>, "--health-url", f"http://127.0.0.1:{port}/health", "--timeout", "1", "--config", ..., "--run-tests", ..., "--duet-status", ..., "--make-capsule", ...], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30)` وأكّد `returncode == 1` و`"Traceback" not in stderr` و`"OVERALL: FAIL" in stdout`.
- اختبار `_safe_streams` لا يرفع عند `sys.stdout` مُستبدل بـ `io.StringIO` (ضمن أحد اختبارات main أو اختبار مستقل).

## التقرير المطلوب عند الانتهاء
1. الملفات المعدّلة (مساراتها فقط).
2. أسماء اختبارات T2 المضافة وعددها، وإجمالي الاختبارات في الملف.
3. نص المخرج الحرفي لتشغيلك المحلي (`Ran N tests` / `OK`).
4. أي انحراف عن المواصفة مع السبب.
إذا تكرر نفس الفشل مرتين دون حل، توقف وأعد `[توقف - تكرار مرتين]` مع وصف الافتراض الذي تشك فيه. اختم بـ `[STAGE T2 DONE]`.

## 75 · assistant (2026-11-21 12:12:21)

بدء T2. سأعدّل `bridge_doctor.py` أولاً: إضافة `argparse`/`sys` إلى الاستيرادات وتحديث docstring الوحدة.

## 85 · assistant (2026-11-21 12:12:53)

تم تعديل الاستيرادات. الآن أضيف `_safe_streams` و`main` وكتلة `__main__` في نهاية `bridge_doctor.py` بعد `format_report`.

## 95 · assistant (2026-11-21 12:13:24)

تمت إضافة `main`/`_safe_streams`. الآن أضيف استيرادات T2 (`contextlib`, `socket`, `subprocess`, `sys`) إلى ملف الاختبارات.

## 105 · assistant (2026-11-21 12:13:38)

تمت إضافة الاستيرادات. الآن أضيف صنف `MainCliTests` (6 اختبارات: نجاح/فشل، `--json` نجاح/فشل، subprocess على منفذ حر مغلق، `_safe_streams` مع `StringIO`) قبل كتلة `__main__`.

## 115 · assistant (2026-11-21 12:14:14)

تمت إضافة `MainCliTests`. الآن أشغّل الاختبارات محلياً (الملف كاملاً: T1 + T2) للتحقق من نص المخرج.

## 125 · assistant (2026-11-21 12:14:28)

الاختبارات نجحت: `Ran 29 tests` + `OK` (23 من T1 + 6 من T2). `Exit code: 1` و`NativeCommandError` هما الأثر الجانبي المعروف لـ `2>&1` في PowerShell (unittest يكتب على stderr) — معيار القبول هو نص المخرج.

## تقرير تسليم T2

**1) الملفات المعدّلة (لم يُلمس أي ملف آخر):**
- `D:\SMS\.hRhR_gateway-service\tools\bridge_doctor.py` — إضافة `import argparse`/`import sys`، تحديث docstring الوحدة، وإضافة قسم CLI في النهاية: `_safe_streams()` (حارس `hasattr(stream, "reconfigure")` + التقاط أي استثناء)، `_build_parser()` (الوسائط السبعة بالقيم الافتراضية من الثوابت، سلاسل `help` بلا `%` حرفي)، `main(argv=None, opener=None)`، وكتلة `if __name__ == "__main__": sys.exit(main())`. دوال T1 لم تتغير.
- `D:\SMS\.hRhR_gateway-service\tools\test_bridge_doctor.py` — تصريح تعديل ملف اختبار: إضافة استيرادات (`contextlib`, `socket`, `subprocess`, `sys`)، مساعدين `_cli_fixture` و`_free_closed_port`، وصنف `MainCliTests`. لم يُحذف/يُخطَّ/يُضعَف أي من اختبارات T1 الـ 23.

**2) اختبارات T2 المضافة — 6 (المطلوب ≥5)؛ إجمالي الملف = 29:**
- `test_safe_streams_with_stringio_does_not_raise`
- `test_main_success_returns_zero` (يعيد 0 + `OVERALL: PASS (3/3 checks passed)` + ASCII صافٍ)
- `test_main_failure_returns_one` (opener يرفع `OSError` → 1 + `OVERALL: FAIL (2/3 checks passed)`)
- `test_main_json_output_success` (`json.loads` صالح، المفاتيح الأربعة، `total==3`، `checks` بطول 3 بالترتيب المتفق)
- `test_main_json_output_failure` (`overall=="FAIL"`, `passed < total`)
- `test_subprocess_closed_port_returns_one_without_traceback` (منفذ حر مغلق عبر `bind(("127.0.0.1", 0))`، `--timeout 1`، كل المسارات مؤقتة، `returncode==1`، لا `Traceback`، `OVERALL: FAIL` في stdout)
- كل اختبار يمرر `--config` لملف `sample_agents_cfg.json` مؤقت + 3 أدوات مؤقتة صراحةً؛ لا استخدام لـ `DEFAULT_CONFIG` الحقيقي.

**3) أمر التحقق والمخرج الحرفي (آخر سطور):**
```
& "C:\Python315\python.exe" -m unittest test_bridge_doctor -v 2>&1 | Out-String   (workdir: tools)
...
test_main_failure_returns_one (test_bridge_doctor.MainCliTests.test_main_failure_returns_one) ... ok
test_main_json_output_failure (test_bridge_doctor.MainCliTests.test_main_json_output_failure) ... ok
test_main_json_output_success (test_bridge_doctor.MainCliTests.test_main_json_output_success) ... ok
test_main_success_returns_zero (test_bridge_doctor.MainCliTests.test_main_success_returns_zero) ... ok
test_safe_streams_with_stringio_does_not_raise
(test_bridge_doctor.MainCliTests.test_safe_streams_with_stringio_does_not_raise) ... ok
test_subprocess_closed_port_returns_one_without_traceback
(test_bridge_doctor.MainCliTests.test_subprocess_closed_port_returns_one_without_traceback) ... ok
----------------------------------------------------------------------
Ran 29 tests in 1.114s
OK
```

**4) انحرافات/قرارات صغيرة (للعلم):**
- فصلت بناء الـ parser في دالة مساعدة `_build_parser()` (داخلية) لتبسيط `main` — لا تغيير في السلوك أو الواجهة المطلوبة.
- `_safe_streams` تلتقط `Exception` عاماً (لا `BaseException`) حتى لا تبتلع `KeyboardInterrupt`.
- الاختبار الناجح لـ `main` يمرر `--health-url http://127.0.0.1:1/health --timeout 0.5` ليؤكد أن القيم تصل للـ opener المحقون؛ لا اتصال حقيقي يحدث.
- تذكير قائم من T1: كود خروج `run_tests.cmd` غير موثوق (`%ERRORLEVEL%` داخل أقواس) — اعتماد نص `OK` عند التحقق عبر `run_tests.cmd all` (خارج نطاقي).

[STAGE T2 DONE]
