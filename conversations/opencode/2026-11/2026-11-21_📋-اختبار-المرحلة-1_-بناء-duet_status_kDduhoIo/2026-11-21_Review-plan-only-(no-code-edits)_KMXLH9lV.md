# Review plan only (no code edits)

- id: `ses_e032d9727ffeXo4ZrEKMXLH9lV`
- title: Review plan only (no code edits)
- date: 2026-11-21 06:36:50
- directory: zizo
- parent: `ses_e032fdc76ffe4LNJr3kDduhoIo`
- agent: executor
- model: upstage-studio/claude-fable-5-1-executor
- messages: 14 (user 3, assistant 11)
- archived: false

## 4 · user (2026-11-21 06:36:50)

You are a subagent spawned by another session.
أنت المنفذ المعزول (Executor) في نظام ثنائي المخطط + المنفذ داخل المجلد ~\Downloads\zizo\duet_demo.

⚠️ المرحلة أ — نقد الخطة فقط: انقد الخطة فقط في المرحلة أ، ممنوع كتابة أو تعديل أي ملف! لا تستخدم أدوات write أو edit أو أي أمر shell يكتب ملفات. يمكنك القراءة فقط (read) إن أردت الاطلاع على ملفات التخطيط في المجلد.

قواعد دورك العامة (ستُطبّق في المراحل التالية، ليس الآن):
- تنفذ فقط المرحلة المكلَّف بها من PLAN.md، ولا تعدّل أبداً ملفات التخطيط (PLAN.md, DUET_LOG.md, TASKS.json, duet_resume.json).
- لا تسأل المالك ولا تفرّع وكلاء؛ إن احتجت قراراً من المالك أنهِ ردك بوسم [NEEDS_OWNER_DECISION]، وإن تعذر التنفيذ أنهِ بـ [BLOCKED].
- Python 3 قياسي فقط بدون مكتبات خارجية.

محتوى PLAN.md الحالي للمراجعة:
----------------------------------------
# PLAN.md — duet_demo (أداة duet_status)

الهدف: بناء أداة صغيرة duet_status.py تقرأ سجل الثنائي DUET_LOG.md وملف الاستئناف duet_resume.json وتعرض حالة المراحل، مع اختبارات unittest كاملة.

القيود العامة:
- Python 3 قياسي فقط (بدون مكتبات خارجية).
- كل الملفات تُنشأ داخل duet_demo فقط.
- المنفذ يعدّل فقط duet_status.py و test_duet_status.py.
- الاختبارات لا تعتمد على ملفات حقيقية في المجلد؛ تُنشئ ملفاتها المؤقتة عبر tempfile.

صيغة سطر السجل المرجعية:
## [YYYY-MM-DD HH:MM] mode=internal|external stage=<id> action=PLAN|ASSIGN|VERIFY|ACCEPT|REJECT|ESCALATE
- ما بعد action=... قد يحتوي على status=<value> اختيارياً؛ إن غاب تُعتبر الحالة "" (فارغة).
- قد تلي سطر العنوان أسطر نصية حرة؛ تُتجاهل في التحليل.

## S1 — النواة: parse_log + قراءة الاستئناف + اختبارات الوحدة
الملفات: duet_status.py (جديد)، test_duet_status.py (جديد)
1. parse_log(path) -> list[dict]: تقرأ UTF-8، تلتقط فقط الأسطر التي تبدأ بـ '## [' وتطابق الصيغة (re). كل dict بالمفاتيح: date (نص YYYY-MM-DD HH:MM)، mode، stage، action، status ("" إن غاب). الأسطر غير المطابقة تُتجاهل بصمت. يحافظ على الترتيب. مسار مفقود → FileNotFoundError.
2. load_resume(path) -> dict: تقرأ JSON UTF-8 وتعيده. مسار مفقود → FileNotFoundError؛ JSON فاسد → ValueError برسالة واضحة.
3. test_duet_status.py بـ unittest يغطي: 3 أسطر صالحة + سطرين غير مطابقين + سطر بدون status → 3 عناصر بالقيم والترتيب الصحيح؛ status فارغ عند غيابه؛ parse_log على مسار مفقود → FileNotFoundError؛ load_resume صالح؛ load_resume فاسد → ValueError.
معايير القبول: الملفان يُستوردان بدون أخطاء؛ parse_log تعيد list[dict] بالمفاتيح الخمسة بالضبط؛ ≥5 اختبارات تنجح؛ لا تعديل على ملفات التخطيط.
أمر التحقق: python -m unittest discover -s ~\Downloads\zizo\duet_demo -p "test_*.py" -v

## S2 — واجهة CLI: --log / --resume + جدول نصي + exit code 2
الملفات: duet_status.py (تعديل)، test_duet_status.py (إضافة اختبارات)
1. build_table(entries, resume) -> str: جدول نصي بأعمدة ثابتة العرض STAGE | LAST_ACTION | STATUS | DATE مرتباً تصاعدياً حسب stage (ترتيب طبيعي: S1 قبل S2 قبل S10). لكل مرحلة آخر سطر سجل لها. تحته سطر ملخص من resume: current_stage، planning_round، مجموع rejections (أو '-' إن غابت المفاتيح).
2. main(argv=None) -> int عبر argparse: --log و --resume مطلوبان. نجاح → يطبع الجدول ويعيد 0. FileNotFoundError أو ValueError → رسالة واضحة إلى stderr تذكر المسار، ويعيد 2 بدون أي Traceback. if __name__ == "__main__": sys.exit(main()).
3. اختبارات CLI: main([...]) بملفات مؤقتة صالحة → 0 والمخرجات تحتوي المراحل مرتبة؛ main مع --log مفقود → 2؛ subprocess.run([sys.executable, duet_status.py, --log <missing>, --resume <missing>]) → returncode == 2 و 'Traceback' not in stderr.
معايير القبول: جميع اختبارات S1+S2 تنجح؛ التشغيل على ملفات duet_demo الحقيقية يطبع جدولاً ويخرج بـ 0؛ ملف مفقود → 2 بدون Traceback؛ لا تعديل على ملفات التخطيط.
----------------------------------------

المطلوب منك الآن (نص فقط، بدون أي كتابة ملفات):
1. هل الصيغة المرجعية لسطر السجل والـ regex المقترح كافيان؟ هل هناك حالات حدية (مثل stage=PLAN غير رقمي، status يحتوي مسافات، أسطر بـ CRLF، BOM) يجب تحديدها بوضوح؟
2. هل معايير القبول قابلة للقياس وغير متناقضة؟ هل هناك غموض في تعريف الترتيب الطبيعي للمراحل أو في سطر الملخص؟
3. هل اختبار subprocess في S2 يحتاج تحديد cwd أو مسار مطلق للملف؟ أي مخاطر على Windows (ترميز stdout، ألوان، إلخ)؟
4. أي تحسين مقترح يجعل التنفيذ أسلم مع بقاء النطاق صغيراً.
اختم ردك بقائمة مرقمة موجزة بالتعديلات المقترحة على الخطة (أو اكتب 'لا تعديلات' إن كانت كافية).

## 5 · assistant (2026-11-21 06:36:50)

# نقد الخطة (المرحلة أ — قراءة فقط، لم أعدّل أي ملف)

## 1) الصيغة المرجعية لسطر السجل والـ regex

**نقاط القوة:** الصيغة بسيطة، مفاتيحها ثابتة الترتيب، وقرار "تجاهل بصمت" يجعل المحلّل متساهلاً مع الأسطر الحرة.

**الثغرات/الحالات الحدية غير المحددة:**
1. **قيمة `stage`:** الخطة لا تحدد الأحرف المسموحة. أقترح النص الصريح: `stage=(\S+)` (أي قيمة بلا مسافات)، فتُقبل `S1` و`S2a` و`PLAN` كلها كمراحل صالحة، ويُترك التعامل مع غير الرقمي لدالة الترتيب (انظر البند 2).
2. **`status` مع مسافات:** يجب حسم أحد خيارين: (أ) `status=(\S+)` فقط، أو (ب) `status=(.*)$` ثم `.strip()`. أرجّح (أ) لسهولة الاختبار وتجنب التقاط تعليقات لاحقة.
3. **مفاتيح إضافية بعد `action`/`status`** (مثل `note=...`): لم يُحدَّد هل يُرفض السطر أم تُتجاهل الزيادة. أقترح: السماح بأي ذيل بعد `status` (regex يتوقف عند `status=\S+` ولا يُلزم `$`)، لكن `action` يجب أن يُتبع إما بنهاية السطر أو بـ `\s+status=`.
4. **CRLF:** فتح الملف بـ `open(..., encoding=...)` الافتراضي (universal newlines) يحوّل `\r\n` تلقائياً، لكن للأمان يُحدَّد صراحة: `line.rstrip("\r\n")` قبل المطابقة، واختبار واحد يكتب الملف بـ `newline=""` و`\r\n` فعلياً.
5. **BOM:** يجب النص على `encoding="utf-8-sig"` في `parse_log` و`load_resume` (ملفات ويندوز/Notepad كثيراً ما تحمل BOM، وبدونها السطر الأول `\ufeff## [` لن يطابق `^## \[`).
6. **المسافات المتعددة بين الحقول:** حدّد `\s+` بين الحقول بدل مسافة واحدة، أو انص صراحة على مسافة واحدة بالضبط (الأسهل للاختبار: `\s+`).
7. **حساسية الأحرف:** انص على أن `mode`/`action` حسّاسة لحالة الأحرف (`Plan` يُرفض).
8. **التاريخ:** يُتحقق من الشكل فقط (`\d{4}-\d{2}-\d{2} \d{2}:\d{2}`) لا من صحة التقويم — انص على ذلك حتى لا يُطلب التحقق لاحقاً.

**regex مقترح للتثبيت في الخطة:**
```
^## \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\]\s+mode=(internal|external)\s+stage=(\S+)\s+action=(PLAN|ASSIGN|VERIFY|ACCEPT|REJECT|ESCALATE)(?:\s+status=(\S+))?(?:\s.*)?$
```

## 2) معايير القبول والترتيب الطبيعي وسطر الملخص

- **قابلية القياس:** "≥5 اختبارات" و"المفاتيح الخمسة بالضبط" قابلة للقياس. جيد.
- **الترتيب الطبيعي غامض:** `S1 < S2 < S10` واضح، لكن ماذا عن `S2a`، `PLAN`، `s3` (حرف صغير)؟ أقترح تعريف دالة عامة `stage_sort_key(stage) -> tuple` بالقاعدة: مطابقة `^([A-Za-z]*)(\d+)(.*)$` → `(0, prefix.upper(), int(num), rest)`؛ غير المطابق → `(1, stage)` (يأتي بعد الرقمي، بترتيب نصي). وتُضاف حالة اختبار لها.
- **"آخر سطر سجل لها":** يجب النص أنه الأخير **بترتيب الملف** لا بترتيب التاريخ (التواريخ قد لا تكون مرتبة أو قد تتساوى بالدقيقة).
- **سطر الملخص غامض في نقطتين:**
  - "مجموع rejections": هل الحقل عدد صحيح أم dict لكل مرحلة أم قائمة؟ يجب تحديد السلوك لكل نوع (int → كما هو، dict → مجموع القيم الرقمية، list → الطول، غير ذلك/غائب → `-`). الأفضل أن يُثبّت المخطط بنية `duet_resume.json` الفعلية في الخطة.
  - الصيغة الحرفية للسطر غير محددة؛ أقترح: `current_stage=<v> | planning_round=<v> | rejections=<v>`.
- **"أعمدة ثابتة العرض":** الاختبارات يجب ألا تثبّت المسافات حرفياً؛ تتحقق من الترتيب عبر تقسيم الأسطر وقراءة العمود الأول (`line.split("|")[0].strip()`) — مع ملاحظة أن `"S1" in stdout` سيطابق أيضاً `S10`، فيجب عدم الاعتماد على `find` النصي الساذج.
- **حالات غير محددة:** `entries` فارغة (جدول برأس فقط + ملخص؟ والعودة بـ 0؟)، و`resume` ليس dict (مثلاً قائمة JSON صالحة) → هل ValueError؟ أقترح نعم: "JSON صالح لكن ليس كائناً → ValueError".
- **تناقض محتمل في S2:** "التشغيل على ملفات duet_demo الحقيقية يطبع جدولاً" يفترض أن `DUET_LOG.md` الحقيقي يطابق الصيغة المرجعية؛ إن لم يطابق سيخرج 0 بجدول فارغ ويبقى المعيار "ناجحاً" شكلاً. يُستحسن أن يتحقق المخطط من مطابقة الملف الحقيقي للصيغة قبل اعتماد المعيار.
- **غموض "main مع --log مفقود → 2":** هل المقصود الوسيط غائب (argparse يرفع `SystemExit(2)` ولا "يعيد" 2) أم المسار غير موجود (FileNotFoundError → return 2)؟ يجب فصلهما: اختبار للمسار المفقود يتوقع `== 2`، واختبار للوسيط الغائب يتوقع `SystemExit` بـ `code == 2` (أو يلتقط `main` الاستثناء — يُحسم في الخطة).

## 3) اختبار subprocess ومخاطر ويندوز

1. **المسار المطلق مطلوب:** `SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "duet_status.py")`. تحديد `cwd` اختياري لكن غير ضار (نفس المجلد).
2. **ترميز stdout/stderr:** على ويندوز قد يكون ترميز الكونسول `cp1256`/`cp1252`؛ أي رسالة خطأ تحوي عربية أو مسار بأحرف غير ASCII قد ترمي `UnicodeEncodeError` — وهو نفسه Traceback يُفشل الاختبار. الحل: (أ) رسائل البرنامج بالإنجليزية/ASCII فقط، (ب) في `subprocess.run` تمرير `env={**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}` و`capture_output=True, text=True, encoding="utf-8", errors="replace"`، (ج) `timeout=30`.
3. **الألوان:** انص صراحة على عدم استخدام أي ANSI/ألوان (جدول نص خام) — يُجنّب مشاكل الطرفية القديمة ويبسّط الاختبار.
4. **اختبار `main()` المباشر:** يلتقط المخرجات عبر `contextlib.redirect_stdout(io.StringIO())` و`redirect_stderr` بدل subprocess لكل حالة؛ يُبقى subprocess لحالة واحدة فقط (التحقق من غياب Traceback وexit code).
5. **أمر التحقق:** `python` قد لا يكون في PATH على بعض أجهزة ويندوز (يستخدم `py`); يُفضَّل في الاختبار `sys.executable` (الخطة تفعل ذلك — جيد)، ويُذكر في أمر التحقق بديل `py -3 -m unittest ...`.

## 4) تحسينات مقترحة (بإبقاء النطاق صغيراً)

- تثبيت `ENTRY_RE` كثابت على مستوى الوحدة، ودالة `stage_sort_key` عامة قابلة للاختبار المباشر.
- `main` يلتقط فقط `FileNotFoundError` و`ValueError` (`json.JSONDecodeError` فرعية منها) ويطبع `error: <message> (<path>)` إلى stderr — دون `except Exception` عام حتى لا تُخفى أخطاء برمجية.
- `load_resume` تغلّف `JSONDecodeError` برسالة تذكر المسار: `ValueError(f"invalid JSON in {path}: {e}")`.
- استخدام `pathlib.Path` اختياري؛ لا داعي لـ dataclass — dict كما في الخطة كافٍ.
- اختبار CRLF + BOM في اختبار واحد مشترك لتقليل العدد.

---

## قائمة التعديلات المقترحة على الخطة

1. تثبيت regex صريح في PLAN.md (المقترح أعلاه) مع `\s+` بين الحقول، `stage=\S+`، `status=\S+`، وسماح بذيل إضافي بعد `status`.
2. النص على `encoding="utf-8-sig"` في `parse_log` و`load_resume`، و`rstrip("\r\n")` قبل المطابقة، مع اختبار CRLF+BOM.
3. تعريف `stage_sort_key` بقاعدة واضحة تشمل المراحل غير الرقمية (تأتي بعد الرقمية) وإضافة اختبار لها.
4. النص على أن "آخر سطر" يعني الأخير بترتيب الملف.
5. تثبيت صيغة سطر الملخص حرفياً، وتحديد بنية `rejections` في `duet_resume.json` الفعلية وقاعدة الجمع لكل نوع.
6. تحديد سلوك: entries فارغة (جدول برأس + ملخص، exit 0) و`resume` JSON صالح لكن ليس كائناً (ValueError).
7. فصل اختبار "وسيط `--log` غائب" (`SystemExit` code 2) عن "مسار `--log` مفقود" (`return 2`).
8. في اختبار subprocess: مسار مطلق للسكربت، `env` بـ `PYTHONIOENCODING=utf-8`/`PYTHONUTF8=1`، `encoding="utf-8", errors="replace"`, `timeout=30`.
9. النص على أن رسائل البرنامج ASCII فقط، وبدون أي ألوان ANSI.
10. التحقق من أن `DUET_LOG.md` الحقيقي يطابق الصيغة المرجعية قبل اعتماد معيار "التشغيل على الملفات الحقيقية".
11. اختبارات `main()` تلتقط المخرجات بـ `redirect_stdout/redirect_stderr`؛ subprocess لحالة واحدة فقط.
12. في `main` التقاط `FileNotFoundError`/`ValueError` فقط (لا `except Exception` عام).

[EXECUTOR_FEEDBACK]

## 14 · user (2026-11-21 06:40:25)

شكراً على النقد؛ أُدمجت ملاحظاتك الـ12 كلها في PLAN.md (الإصدار 2) والخطة معتمدة الآن.

[STAGE_ASSIGN S1] — نفّذ المرحلة S1 فقط من ~\Downloads\zizo\duet_demo\PLAN.md (اقرأ الملف أولاً بـ read لأنه تغيّر منذ مراجعتك). لا تنفّذ أي شيء من S2 (لا CLI، لا argparse، لا build_table، لا stage_sort_key).

الملفات المسموح إنشاؤها فقط:
- ~\Downloads\zizo\duet_demo\duet_status.py
- ~\Downloads\zizo\duet_demo\test_duet_status.py
ممنوع منعاً باتاً لمس PLAN.md أو DUET_LOG.md أو TASKS.json أو duet_resume.json.

المطلوب (ملخص؛ المرجع الكامل في PLAN.md قسم S1):
1. ثابت الوحدة ENTRY_RE حرفياً كما في PLAN.md:
   ENTRY_RE = re.compile(r"^## \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\]\s+mode=(internal|external)\s+stage=(\S+)" r"\s+action=(PLAN|ASSIGN|VERIFY|ACCEPT|REJECT|ESCALATE)(?:\s+status=(\S+))?(?:\s.*)?$")
2. parse_log(path) -> list[dict]: قراءة utf-8-sig، rstrip("\r\n") لكل سطر، مطابقة ENTRY_RE، dict بالمفاتيح الخمسة بالضبط: date, mode, stage, action, status ("" إن غاب)، الترتيب كترتيب الملف، الأسطر غير المطابقة تُتجاهل بصمت، مسار مفقود → FileNotFoundError.
3. load_resume(path) -> dict: utf-8-sig؛ مسار مفقود → FileNotFoundError؛ JSON فاسد → ValueError(f"invalid JSON in {path}: {e}")؛ JSON صالح لكن ليس كائناً → ValueError تذكر المسار.
4. test_duet_status.py بـ unittest وملفات مؤقتة (tempfile) يغطي ≥ 7 اختبارات: 3 صالحة + سطرين غير مطابقين + أسطر حرة + سطر بدون status → 3 عناصر بالقيم والترتيب؛ status=="" وذيل حر يُتجاهل؛ CRLF+BOM في اختبار واحد (كتابة بـ encoding="utf-8-sig", newline="" مع \r\n فعلي)؛ parse_log مسار مفقود → FileNotFoundError؛ load_resume صالح؛ load_resume فاسد → ValueError؛ load_resume قائمة → ValueError.

قيود: Python 3 قياسي فقط، رسائل ASCII/إنجليزية فقط، بدون ألوان.

بعد الكتابة شغّل بنفسك أمر التحقق:
python -m unittest discover -s ~\Downloads\zizo\duet_demo -p "test_*.py" -v
وأصلح أي فشل قبل الرد. ثم أرسل تقريراً موجزاً: الملفات المنشأة، عدد الاختبارات ونتيجتها، وأي ملاحظة. لا تسأل المالك؛ إن احتجت قراراً اختم بـ [NEEDS_OWNER_DECISION]، وإن تعذر التنفيذ اختم بـ [BLOCKED].

## 15 · assistant (2026-11-21 06:40:25)

سأبدأ بقراءة PLAN.md (الإصدار 2) للاطلاع على مواصفات S1 المحدّثة قبل أي كتابة.

## 25 · assistant (2026-11-21 06:40:37)

قرأت الإصدار 2 من PLAN.md؛ سأنشئ الآن `duet_status.py` (نواة S1 فقط: `ENTRY_RE` + `parse_log` + `load_resume`).

## 35 · assistant (2026-11-21 06:41:06)

تم إنشاء `duet_status.py`؛ الآن أكتب ملف الاختبارات `test_duet_status.py` بالاختبارات السبعة المطلوبة عبر `tempfile`.

## 45 · assistant (2026-11-21 06:41:45)

تم إنشاء ملف الاختبارات؛ الآن أشغّل أمر التحقق المحدد في الخطة.

## 55 · assistant (2026-11-21 06:41:58)

# تقرير تنفيذ المرحلة S1

**[STAGE S1 DONE]**

## الملفات المنشأة (داخل `duet_demo` فقط)
- `~\Downloads\zizo\duet_demo\duet_status.py` — جديد:
  - `ENTRY_RE` ثابت على مستوى الوحدة، مطابق حرفياً للنص المثبّت في PLAN.md.
  - `parse_log(path)`: قراءة `utf-8-sig`، `rstrip("\r\n")`، مطابقة `ENTRY_RE`، dict بالمفاتيح الخمسة بالضبط (`status=""` عند الغياب)، ترتيب الملف محفوظ، غير المطابق يُتجاهل بصمت، مسار مفقود → `FileNotFoundError`.
  - `load_resume(path)`: `utf-8-sig`؛ مسار مفقود → `FileNotFoundError`؛ JSON فاسد → `ValueError(f"invalid JSON in {path}: {e}")`؛ JSON صالح غير كائن → `ValueError` تذكر المسار.
- `~\Downloads\zizo\duet_demo\test_duet_status.py` — جديد، 9 اختبارات عبر `tempfile` (تغطي كل البنود السبعة المطلوبة + اختبار ثابت `ENTRY_RE` وحساسية الأحرف + `load_resume` مسار مفقود).

**لم أمسّ** `PLAN.md` أو `DUET_LOG.md` أو `TASKS.json` أو `duet_resume.json`. لم أنفّذ أي شيء من S2.

## أمر التحقق
```
python -m unittest discover -s ~\Downloads\zizo\duet_demo -p "test_*.py" -v
```

## المخرج الحرفي (آخر الأسطر)
```
test_load_resume_invalid_json ... ok
test_load_resume_missing_path ... ok
test_load_resume_not_an_object ... ok
test_load_resume_valid ... ok
test_entry_re_is_module_constant ... ok
test_parse_log_crlf_and_bom ... ok
test_parse_log_missing_path ... ok
test_parse_log_missing_status_and_free_tail ... ok
test_parse_log_valid_invalid_and_free_lines ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.042s

OK
```

## النتيجة مقابل معايير القبول
- الملفان يُستوردان بدون أخطاء (الاستيراد تم ضمن تشغيل الاختبارات) ✅
- `ENTRY_RE` ثابت وحدة مطابق للنص المثبّت ✅
- `parse_log` تعيد `list[dict]` بالمفاتيح الخمسة بالضبط (مُتحقق منه في الاختبار بـ `set(entry.keys()) == EXPECTED_KEYS`) ✅
- 9 اختبارات ≥ 7، جميعها ناجحة ✅
- لا تعديل على ملفات التخطيط ✅

## ملاحظات
- الرسائل كلها ASCII/إنجليزية بدون ألوان.
- اختبار CRLF+BOM يتحقق فعلياً من وجود `\xef\xbb\xbf` و`\r\n` في البايتات الخام قبل التحليل، ومن خلو القيم المستخرجة من `\r` و`\ufeff`.
- جاهز لتكليف S2.

[EXEC_REPORT S1]

## 64 · user (2026-11-21 06:44:57)

S1 معتمدة بعد تدقيق مستقل (9/9 اختبارات OK). شكراً.

[STAGE_ASSIGN S2] — نفّذ المرحلة S2 فقط من ~\Downloads\zizo\duet_demo\PLAN.md (اقرأ قسم S2 بـ read أولاً).

الملفات المسموح تعديلها فقط:
- ~\Downloads\zizo\duet_demo\duet_status.py (إضافة؛ لا تكسر S1)
- ~\Downloads\zizo\duet_demo\test_duet_status.py (إضافة اختبارات؛ أبقِ اختبارات S1 كما هي)
ممنوع منعاً باتاً لمس PLAN.md أو DUET_LOG.md أو TASKS.json أو duet_resume.json.

المطلوب (ملخص؛ المرجع الكامل في PLAN.md قسم S2):
1. stage_sort_key(stage: str) -> tuple: مطابقة ^([A-Za-z]*)(\d+)(.*)$ → (0, prefix.upper(), int(num), rest)؛ غير المطابق → (1, stage). النتيجة: S1 < S2 < S2a < S10 < PLAN.
2. build_table(entries, resume) -> str: لكل stage آخر سطر بترتيب الملف؛ أعمدة ثابتة العرض STAGE | LAST_ACTION | STATUS | DATE مع سطر رأس، صفوف مرتبة بـ stage_sort_key؛ entries فارغة → رأس فقط + ملخص. سطر الملخص حرفياً: current_stage=<v> | planning_round=<v> | rejections=<v> (القيمة '-' لأي مفتاح غائب أو None؛ rejections: int كما هو، dict → مجموع القيم الرقمية، list → الطول، غير ذلك → '-').
3. main(argv=None) -> int عبر argparse: --log و --resume كلاهما required=True (غياب الوسيط → SystemExit(2) من argparse بدون التقاط). نجاح → طباعة الجدول إلى stdout وإعادة 0. التقاط FileNotFoundError و ValueError فقط (لا except Exception) → طباعة 'error: <message> (<path>)' إلى stderr وإعادة 2 بدون Traceback. if __name__ == "__main__": sys.exit(main()).
4. اختبارات CLI في test_duet_status.py:
   - sorted(["S10","PLAN","S2","S1"], key=[REDACTED:KV_SECRET] == ["S1","S2","S10","PLAN"].
   - main([...]) بملفات مؤقتة صالحة مع redirect_stdout/redirect_stderr → 0، والتحقق من الترتيب عبر line.split("|")[0].strip() للعمود الأول (لا 'S1' in stdout الساذج).
   - main([...]) مع مسار --log غير موجود → 2 و stderr يحوي المسار.
   - main(["--resume", x]) بدون --log → assertRaises(SystemExit) و code == 2.
   - اختبار subprocess واحد: SCRIPT مسار مطلق عبر os.path.dirname(os.path.abspath(__file__))، subprocess.run([sys.executable, SCRIPT, "--log", <missing>, "--resume", <missing>], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30, env={**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}) → returncode == 2 و "Traceback" not in stderr.

قيود: Python 3 قياسي فقط، رسائل ASCII/إنجليزية فقط، بدون ألوان ANSI.

بعد الكتابة شغّل بنفسك:
1) python -m unittest discover -s ~\Downloads\zizo\duet_demo -p "test_*.py" -v
2) python ~\Downloads\zizo\duet_demo\duet_status.py --log ~\Downloads\zizo\duet_demo\DUET_LOG.md --resume ~\Downloads\zizo\duet_demo\duet_resume.json
3) نفس الأمر مع --log MISSING.md والتأكد أن exit code = 2 بدون Traceback.
أصلح أي فشل قبل الرد، ثم أرسل تقريراً موجزاً: الدوال المضافة، عدد الاختبارات الكلي ونتيجتها، ومخرج الجدول الحقيقي، ونتيجة حالة الملف المفقود. لا تسأل المالك؛ عند الحاجة لقرار اختم بـ [NEEDS_OWNER_DECISION]، وإن تعذر التنفيذ اختم بـ [BLOCKED].

## 65 · assistant (2026-11-21 06:44:57)

سأبدأ بقراءة قسم S2 من PLAN.md للتأكد من المواصفات الحالية قبل التعديل.

## 75 · assistant (2026-11-21 06:45:14)

قرأت قسم S2؛ سأعيد كتابة `duet_status.py` مع الإبقاء على نواة S1 كما هي حرفياً وإضافة `stage_sort_key` و`build_table` و`main`.

## 85 · assistant (2026-11-21 06:46:33)

تم تحديث `duet_status.py`؛ الآن أضيف اختبارات S2 إلى `test_duet_status.py` مع إبقاء اختبارات S1 كما هي.

## 95 · assistant (2026-11-21 06:47:46)

تمت إضافة اختبارات S2؛ الآن أشغّل أوامر التحقق الثلاثة (الاختبارات، التشغيل الحقيقي، وحالة الملف المفقود).

## 105 · assistant (2026-11-21 06:48:01)

# تقرير تنفيذ المرحلة S2

**[STAGE S2 DONE]**

## الملفات المعدّلة (داخل `duet_demo` فقط)
- `~\Downloads\zizo\duet_demo\duet_status.py` — نواة S1 (`ENTRY_RE`, `parse_log`, `load_resume`) أُبقيت حرفياً كما هي، وأُضيف:
  - `stage_sort_key(stage) -> tuple`: مطابقة `^([A-Za-z]*)(\d+)(.*)$` → `(0, prefix.upper(), int(num), rest)`؛ غير المطابق → `(1, stage)`. النتيجة `S1 < S2 < S2a < S10 < PLAN`، و`s3 == S3`.
  - `build_table(entries, resume) -> str`: آخر سطر لكل مرحلة **بترتيب الملف**، جدول ثابت العرض `STAGE | LAST_ACTION | STATUS | DATE` برأس وخط فاصل، صفوف مرتبة بـ `stage_sort_key`، entries فارغة → رأس فقط + ملخص، سطر الملخص حرفياً `current_stage=<v> | planning_round=<v> | rejections=<v>` (`-` للغائب/`None`؛ `rejections`: int كما هو، dict → مجموع القيم الرقمية، list → الطول، غير ذلك → `-`).
  - دالة مساعدة عامة `build_summary_line(resume)` (تُستخدم داخل `build_table`).
  - `main(argv=None) -> int` عبر `argparse` (`--log`/`--resume` كلاهما `required=True`؛ غياب الوسيط → `SystemExit(2)` بلا التقاط)، يلتقط **فقط** `FileNotFoundError` و`ValueError` → `error: <message> (<path>)` إلى stderr ويعيد 2؛ نجاح → يطبع الجدول ويعيد 0. `if __name__ == "__main__": sys.exit(main())`.
- `~\Downloads\zizo\duet_demo\test_duet_status.py` — اختبارات S1 التسعة بقيت كما هي دون تعديل، وأُضيفت 10 اختبارات S2 (`StageSortKeyTests` ×2، `BuildTableTests` ×3، `CliTests` ×5 منها اختبار subprocess واحد بالإعدادات المحددة في الخطة).

**لم أمسّ** `PLAN.md` أو `DUET_LOG.md` أو `TASKS.json` أو `duet_resume.json`.

## أوامر التحقق ومخرجاتها الحرفية

**1) الاختبارات:**
```
python -m unittest discover -s ~\Downloads\zizo\duet_demo -p "test_*.py" -v
...
test_full_order_suffix_and_lowercase ... ok
test_sorted_order_from_plan ... ok

----------------------------------------------------------------------
Ran 19 tests in 0.064s

OK
```
الإجمالي: **19/19 OK** (9 من S1 + 10 من S2).

**2) التشغيل على الملفات الحقيقية:**
```
STAGE | LAST_ACTION | STATUS        | DATE
------+-------------+---------------+-----------------
S1    | ACCEPT      | approved      | 2026-11-21 08:44
S2    | ASSIGN      | in_progress   | 2026-11-21 08:46
PLAN  | ACCEPT      | plan_approved | 2026-11-21 08:40

current_stage=S2 | planning_round=2 | rejections=0
exit=0
```

**3) ملف مفقود:**
```
error: No such file or directory (~\Downloads\zizo\duet_demo\MISSING.md)
exit=2
```
لا توجد كلمة `Traceback` في المخرجات.

## النتيجة مقابل معايير القبول
- جميع اختبارات S1 + S2 تنجح (19/19) ✅
- التشغيل على الملفات الحقيقية يطبع جدولاً يحتوي صف `PLAN` ويخرج بـ 0 ✅
- ملف مفقود → exit 2 بدون Traceback ✅
- لا تعديل على ملفات التخطيط الأربعة ✅

## ملاحظات
- الرسائل كلها ASCII/إنجليزية، بلا ألوان ANSI.
- في `main`، رسالة `FileNotFoundError` تستخدم `e.filename`/`e.strerror` من الاستثناء نفسه، فالمسار المذكور هو الملف المفقود فعلاً (log أو resume) وليس تخميناً.
- `_format_rejections` تستثني `bool` صراحة (لأن `True` هي `int` في بايثون) فتُعرض كـ `-`؛ قرار دفاعي صغير لا يخالف نص الخطة.
- المرحلتان S1 وS2 مكتملتان؛ لا مراحل متبقية في STAGE_LIST.

[EXEC_REPORT S2]
