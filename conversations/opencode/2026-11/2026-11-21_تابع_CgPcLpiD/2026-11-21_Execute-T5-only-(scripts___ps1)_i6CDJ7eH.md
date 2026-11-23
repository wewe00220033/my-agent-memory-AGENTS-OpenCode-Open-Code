# Execute T5 only (scripts/*.ps1)

- id: `ses_e006254f4ffeFiMQ79i6CDJ7eH`
- title: Execute T5 only (scripts/*.ps1)
- date: 2026-11-21 19:38:05
- directory: D:/SMS/.hRhR_gateway-service/scratch/sandbox_resume_test
- parent: `ses_e00664212ffeeT17lpCgPcLpiD`
- agent: executor
- model: upstage-studio/claude-fable-5-1-executor
- messages: 23 (user 3, assistant 20)
- archived: false

## 4 · user (2026-11-21 19:38:05)

You are a subagent spawned by another session.
أنت المنفذ (Executor) في مشروع `Local-Hugging-Face-GitHub` — تنفذ الدفعة المطلوبة فقط، لا تسأل المالك، لا تفرّع وكلاء. جلسة جديدة بعد انقطاع أثناء الدفعة B2.

## المسار
`D:\SMS\.hRhR_gateway-service\scratch\sandbox_resume_test`

## حالة القرص المتحقق منها (لا تلمسها)
- T1 `run_tests.cmd` مقبول.
- T2 `.gitignore` مكتوب وسليم.
- T4 `test_contract.py` مكتوب وسليم.
- **T5 (`scripts\*.ps1`) غير موجود إطلاقاً** → هذا هو المطلوب الوحيد الآن.

## T5 — إنشاء 4 سكريبتات داخل مجلد جديد `scripts\` (تُكتب ولا تُشغَّل إطلاقاً)
اقرأ `README.md` أولاً (الأقسام 3-أ، 4-أ، 4-ج) لنقل الأوامر الأصلية منها.

**قواعد مشتركة لكل سكريبت:**
- الترميز UTF-8 (بدون BOM/UTF-16؛ لا تستخدم `Out-File` الافتراضية في PowerShell 5).
- **السطر الأول حرفياً:** `# WARNING: do not run before S2 (links/versions not verified yet)`
- **بدون** أي حارس `exit 1` (قرار المالك D3) — التعليق التحذيري فقط.
- ممنوع تنفيذ أي `Invoke-WebRequest` / تنزيل / فك ضغط / `pip install` / تشغيل سيرفر أثناء العمل.

**1) `scripts\download_engine.ps1`:** أوامر القسم 3-أ من README مع وسم الإصدار في **متغير واحد أعلى الملف** `$LlamaTag = "b12606"` يُستخدم في بناء الرابط واسم ملف الـ zip (`llama-$LlamaTag-bin-win-cpu-x64.zip`).

**2) `scripts\download_model.ps1`:** `param()` فيه معامل `-Model` بـ `[ValidateSet('LFM2.5-1.2B','granite')]` والافتراضي `'LFM2.5-1.2B'` (قرار D1 — خياران فقط، بدون MiniCPM) + hashtable ربط: الاسم → URL + اسم الملف:
- `LFM2.5-1.2B` → مستودع `LiquidAI/LFM2.5-1.2B-Instruct-GGUF`، ملف `LFM2.5-1.2B-Instruct-Q4_K_M.gguf`
- `granite` → مستودع `ibm-granite/granite-4.0-h-350m-GGUF`، ملف `granite-4.0-h-350m-Q4_K_M.gguf`

**3) `scripts\start_llama_server.ps1`:**
- **لا مسار ثابت للتنفيذي:** `Get-ChildItem -Path (Join-Path $PSScriptRoot '..\engine\llama-cpp') -Filter llama-server.exe -Recurse -File | Select-Object -First 1`؛ إن لم يُعثر عليه → `Write-Error` برسالة واضحة والخروج.
- مسار الموديل الافتراضي: `..\models\LFM2.5-1.2B-Instruct-Q4_K_M.gguf` نسبةً لـ `$PSScriptRoot`.
- أعلام القسم 4-أ كما هي: `--host 127.0.0.1 --port 8080 --ctx-size 4096 -ctk q8_0 -ctv q8_0 --jinja --threads 4`.
- تعليق حرفي: `# NOTE: -ctv q8_0 (quantized V cache) requires Flash Attention to be enabled (not disabled) in llama.cpp; verify in S2 and add -fa only if the server rejects it. Do NOT add -fa here.`
- **لا تضف `-fa`.**

**4) `scripts\start_litellm.ps1`:** أمر القسم 4-ج من README مشيراً إلى `litellm_config.yaml` كنص فقط (مسار نسبي من `$PSScriptRoot\..`).

## محظورات صارمة
- لا تعدّل: `README.md`، `وكيل-الثاني.txt`، `run_tests.cmd`، `.gitignore`، `test_contract.py`، `PLAN.md`، `TASKS.json`، `DUET_LOG.md`، `duet_resume.json`.
- لا تنشئ `litellm_config.yaml` (هذا T3 في دفعة لاحقة).
- لا تنشئ أي ملف غير الأربعة المذكورة.
- إذا احتاج `run_tests.cmd` تصحيحاً: **أبلغ التغيير الحرفي دون تنفيذه** (مسار T1.x).

## التحقق المطلوب بعد الكتابة
شغّل `.\run_tests.cmd unit` من مجلد المشروع. **المتوقع:** فقط C2, C11, C12 = FAIL (+ P2 SKIP لأن PyYAML غير مثبت)، كل الباقي PASS، سطر `RESULT`، exit 1. أي FAIL آخر = أبلغه حرفياً.

## صيغة التقرير
`EXEC_DONE T5` + قائمة الملفات الأربعة المنشأة مع حجم كل ملف + السطر الأول من كل سكريبت + مخرج `run_tests.cmd unit` كاملاً. إذا فشل نفس الفحص مرتين أبلغ `[توقف - تكرار مرتين]` مع السبب.

## 5 · assistant (2026-11-21 19:38:05)

سأبدأ بقراءة `README.md` وفحص حالة المجلد قبل كتابة سكريبتات T5.

## 15 · assistant (2026-11-21 19:38:18)

قرأت README. الآن أفحص `run_tests.cmd` لمعرفة الفحوصات (C1–C12) التي ستتحقق من محتوى السكريبتات قبل الكتابة.

## 25 · assistant (2026-11-21 19:38:34)

قرأت `run_tests.cmd`: الفحوصات C4–C7 تتحقق فقط من وجود الملفات الأربعة، وC2/C11/C12 ستفشل لأن `litellm_config.yaml` خارج النطاق (T3). أبدأ بكتابة السكريبت الأول `download_engine.ps1` بترميز UTF-8 عبر أداة `write` (بدون `Out-File`).

## 35 · assistant (2026-11-21 19:39:03)

تم إنشاء السكريبت الأول. أكتب الآن الثلاثة المتبقية (`download_model.ps1`، `start_llama_server.ps1`، `start_litellm.ps1`) تباعاً.

## 45 · assistant (2026-11-21 19:39:20)

تم إنشاء السكريبت الثاني. أكتب الآن `start_llama_server.ps1` بالبحث الديناميكي عن `llama-server.exe` وبدون `-fa`.

## 55 · assistant (2026-11-21 19:39:38)

تم إنشاء السكريبت الثالث. أكتب الآن الأخير `start_litellm.ps1` بأمر القسم 4-ج مع الإشارة إلى `litellm_config.yaml` كنص فقط.

## 65 · assistant (2026-11-21 19:39:51)

تم إنشاء السكريبتات الأربعة. الآن أتحقق من الحجم والترميز (UTF-8 بدون BOM) والسطر الأول لكل ملف، ثم أشغّل `run_tests.cmd unit`.

## 75 · assistant (2026-11-21 19:40:05)

الترميز سليم (UTF-8 بدون BOM) والسطر الأول مطابق في الملفات الأربعة. أشغّل الآن `run_tests.cmd unit` للتحقق النهائي.

## 85 · assistant (2026-11-21 19:40:17)

النتيجة مطابقة تماماً للمتوقع: فقط C2, C11, C12 = FAIL (ملف `litellm_config.yaml` خارج النطاق — T3)، P2 SKIP، كل الباقي PASS، سطر `RESULT` موجود، exit 1. لا حاجة لأي تعديل على `run_tests.cmd`.

---

# EXEC_DONE T5

## الملفات المنشأة (4 فقط — داخل `scripts\` جديد)

| الملف | الحجم | الترميز | السطر الأول |
|---|---|---|---|
| `scripts\download_engine.ps1` | 1144 بايت | UTF-8 بدون BOM | `# WARNING: do not run before S2 (links/versions not verified yet)` |
| `scripts\download_model.ps1` | 1198 بايت | UTF-8 بدون BOM | `# WARNING: do not run before S2 (links/versions not verified yet)` |
| `scripts\start_llama_server.ps1` | 1416 بايت | UTF-8 بدون BOM | `# WARNING: do not run before S2 (links/versions not verified yet)` |
| `scripts\start_litellm.ps1` | 604 بايت | UTF-8 بدون BOM | `# WARNING: do not run before S2 (links/versions not verified yet)` |

## ملخص المحتوى الفعلي (Actual Diff Summary)
1. **`download_engine.ps1`:** أوامر README 3-أ (السطور 46، 49، 52) مع `$LlamaTag = "b12606"` كمتغير وحيد أعلى الملف يُبنى منه الرابط `https://github.com/ggml-org/llama.cpp/releases/download/$LlamaTag/llama-$LlamaTag-bin-win-cpu-x64.zip`. لا حارس `exit 1` (D3).
2. **`download_model.ps1`:** `param()` مع `[ValidateSet('LFM2.5-1.2B','granite')]` والافتراضي `'LFM2.5-1.2B'` (D1 — بدون MiniCPM) + hashtable `$ModelMap` يربط الاسم → Repo + File حسب README 3-ب (السطور 59، 62).
3. **`start_llama_server.ps1`:** بحث ديناميكي `Get-ChildItem ... -Filter llama-server.exe -Recurse -File | Select-Object -First 1`، `Write-Error` + `return` عند عدم العثور عليه (وعند غياب الموديل)، مسار الموديل الافتراضي `..\models\LFM2.5-1.2B-Instruct-Q4_K_M.gguf` نسبةً لـ `$PSScriptRoot`، أعلام README 4-أ (السطور 78–83) حرفياً، التعليق الحرفي حول `-ctv q8_0`/Flash Attention مدرج، **بدون `-fa`**.
4. **`start_litellm.ps1`:** أمرا README 4-ج (السطور 118–119) مع `$ConfigPath = Join-Path $PSScriptRoot '..' \ litellm_config.yaml` كإشارة نصية فقط (الملف نفسه لم يُنشأ — T3).

## الالتزام بالمحظورات
- لم يُشغَّل أي سكريبت، ولا `Invoke-WebRequest` / تنزيل / `pip install` / سيرفر.
- لم يُعدَّل أي من: `README.md`، `وكيل-الثاني.txt`، `run_tests.cmd`، `.gitignore`، `test_contract.py`، `PLAN.md`، `TASKS.json`، `DUET_LOG.md`، `duet_resume.json`.
- لم يُنشأ `litellm_config.yaml` ولا أي ملف خامس.
- لا تعديل في أي ملف اختبار.
- `run_tests.cmd` لا يحتاج تصحيحاً (لا مسار T1.x).

## أمر التحقق والمخرج الحرفي الكامل
`cmd /c "run_tests.cmd unit"` من `D:\SMS\.hRhR_gateway-service\scratch\sandbox_resume_test`:
```
[PASS] C1 file .gitignore
[FAIL] C2 file litellm_config.yaml
[PASS] C3 file test_contract.py
[PASS] C4 file scripts\download_engine.ps1
[PASS] C5 file scripts\download_model.ps1
[PASS] C6 file scripts\start_llama_server.ps1
[PASS] C7 file scripts\start_litellm.ps1
[PASS] C8 .gitignore contains engine/
[PASS] C9 .gitignore contains models/
[PASS] C10 .gitignore contains *.gguf
[FAIL] C11 litellm_config.yaml contains model_name: agent-slot
[FAIL] C12 litellm_config.yaml contains api_base: http://127.0.0.1:8080/v1
[PASS] C13 dir engine absent
[PASS] C14 dir models absent
[PASS] P1 py_compile test_contract.py
[SKIP] P2 yaml parse litellm_config.yaml (PyYAML not installed)
RESULT passed=12 failed=3 skipped=1
EXIT_CODE=1
```
**التقييم:** مطابق 100% للمتوقع — الـ FAIL الثلاثة (C2/C11/C12) كلها بسبب غياب `litellm_config.yaml` المؤجل لـ T3؛ لا يوجد أي FAIL آخر. تم التحقق من أول مرة (لا تكرار).

[STAGE T5 DONE]

## 94 · user (2026-11-21 19:44:19)

B2 (T2+T4+T5) قُبلت بعد التحقق المستقل — شكراً. الآن الدفعة B3 = **T3 فقط** (منطقة حمراء: ملف إعدادات). لا تلمس أي ملف آخر.

## المسار
`D:\SMS\.hRhR_gateway-service\scratch\sandbox_resume_test`

## T3 — إنشاء `litellm_config.yaml` في جذر المشروع (ملف واحد فقط)
1. اقرأ `README.md` القسم **4-ب** أولاً وانقل محتواه **حرفياً كما هو** (بلوك `agent-slot` الفعّال + بلوك المستقبل معلّقاً، بلا أي تغيير داخل البلوكات — لا إعادة ترتيب، لا تعديل مسافات بادئة، لا إضافة/حذف مفاتيح).
2. قرار المالك D2: `api_key: "[REDACTED:KV_SECRET]"` **حرفي** كما في README (لا `os.environ/` ولا متغير بيئة).
3. يُسمح فقط بإضافة سطور تعليق `#` في **أعلى الملف** (قبل أي مفتاح YAML) تذكر: الموديل الأساسي `LFM2.5-1.2B-Instruct-Q4_K_M` والاحتياطي `granite-4.0-h-350m-Q4_K_M`، وأن الملف مطابق للقسم 4-ب من README.
4. الترميز UTF-8 بدون BOM (لا `Out-File` الافتراضية في PowerShell 5).
5. يجب أن يحتوي الملف حرفياً على `model_name: agent-slot` و `api_base: http://127.0.0.1:8080/v1` (فحوص C11/C12 تعتمد `findstr /L /C:` بالمطابقة الحرفية — تأكد من المسافات والاقتباسات كما في README).

## محظورات صارمة
- لا تعدّل: `README.md`، `وكيل-الثاني.txt`، `run_tests.cmd`، `.gitignore`، `test_contract.py`، `scripts\*.ps1`، `PLAN.md`، `TASKS.json`، `DUET_LOG.md`، `duet_resume.json`.
- لا تنشئ أي ملف غير `litellm_config.yaml`.
- ممنوع `pip install` / تشغيل `litellm` / أي تنزيل.
- إذا احتاج `run_tests.cmd` تصحيحاً: أبلغ التغيير الحرفي **دون تنفيذه** (مسار T1.x).

## التحقق المطلوب بعد الكتابة
شغّل `.\run_tests.cmd unit`. **المتوقع:** `RESULT passed=15 failed=0 skipped=1` (P2 SKIP لأن PyYAML غير مثبت)، exit 0. أي FAIL = أبلغه حرفياً.

## صيغة التقرير
`EXEC_DONE T3` + حجم الملف + أرقام سطور README المنقولة (من–إلى) + سطور التعليق المضافة أعلى الملف حرفياً + تأكيد أن ما بعد التعليقات مطابق حرفياً للقسم 4-ب + مخرج `run_tests.cmd unit` كاملاً مع EXIT_CODE. إذا فشل نفس الفحص مرتين أبلغ `[توقف - تكرار مرتين]` مع السبب.

## 95 · assistant (2026-11-21 19:44:19)

سأبدأ الدفعة B3 بكتابة `litellm_config.yaml` ناقلاً القسم 4-ب (README سطور 93–112) حرفياً مع تعليقات أعلى الملف فقط، بترميز UTF-8 بدون BOM عبر أداة `write`.

## 105 · assistant (2026-11-21 19:44:42)

تم إنشاء الملف. أتحقق الآن من الترميز والحجم ومطابقة ما بعد التعليقات حرفياً للسطور 93–112 من README، ثم أشغّل `run_tests.cmd unit`.

## 115 · assistant (2026-11-21 19:45:03)

النتيجة مطابقة تماماً للمتوقع: `RESULT passed=15 failed=0 skipped=1`، exit 0، الترميز UTF-8 بدون BOM، وما بعد التعليقات مطابق حرفياً للقسم 4-ب.

---

# EXEC_DONE T3

## الملف المنشأ (واحد فقط — في جذر المشروع)
| الملف | الحجم | الترميز |
|---|---|---|
| `litellm_config.yaml` | 1314 بايت | UTF-8 بدون BOM |

## أرقام سطور README المنقولة
- **من السطر 93 إلى السطر 112** (القسم 4-ب — بلوك `agent-slot` الفعّال + بلوك المستقبل معلّقاً)، 20 سطراً.
- التحقق الآلي: `Compare-Object` بين `README.md[93..112]` وجسم الملف بعد التعليقات → **`VERBATIM_MATCH`** (BODY_LINES=20 / REF_LINES=20، لا فروق).

## سطور التعليق المضافة أعلى الملف (حرفياً — 5 سطور قبل أي مفتاح YAML)
```
# litellm_config.yaml - LiteLLM Proxy config (identical to README.md section 4-b)
# Primary local model : LFM2.5-1.2B-Instruct-Q4_K_M (LiquidAI/LFM2.5-1.2B-Instruct-GGUF)
# Fallback local model: granite-4.0-h-350m-Q4_K_M (ibm-granite/granite-4.0-h-350m-GGUF)
# Decision D2: api_key is the literal placeholder value from README (no environment variable).
# Everything below this comment header is copied verbatim from README.md section 4-b.
```

## تأكيد المطابقة الحرفية
- ما بعد سطور التعليق الخمسة مطابق **حرفياً** للقسم 4-ب (README 93–112): لا إعادة ترتيب، لا تعديل مسافات بادئة، لا إضافة/حذف مفاتيح.
- D2 ملتزم: `api_key: "[REDACTED:KV_SECRET]"` حرفي (لا `os.environ/`).
- يحتوي حرفياً على `model_name: agent-slot` و `api_base: http://127.0.0.1:8080/v1` (C11/C12 PASS).

## الالتزام بالمحظورات
- لم يُعدَّل أي من: `README.md`، `وكيل-الثاني.txt`، `run_tests.cmd`، `.gitignore`، `test_contract.py`، `scripts\*.ps1`، `PLAN.md`، `TASKS.json`، `DUET_LOG.md`، `duet_resume.json`.
- لم يُنشأ أي ملف غير `litellm_config.yaml`.
- لا `pip install` / لا تشغيل `litellm` / لا تنزيل.
- لا تعديل في أي ملف اختبار؛ `run_tests.cmd` لا يحتاج تصحيحاً (لا مسار T1.x).

## أمر التحقق والمخرج الحرفي الكامل
`cmd /c "run_tests.cmd unit"` من `D:\SMS\.hRhR_gateway-service\scratch\sandbox_resume_test`:
```
[PASS] C1 file .gitignore
[PASS] C2 file litellm_config.yaml
[PASS] C3 file test_contract.py
[PASS] C4 file scripts\download_engine.ps1
[PASS] C5 file scripts\download_model.ps1
[PASS] C6 file scripts\start_llama_server.ps1
[PASS] C7 file scripts\start_litellm.ps1
[PASS] C8 .gitignore contains engine/
[PASS] C9 .gitignore contains models/
[PASS] C10 .gitignore contains *.gguf
[PASS] C11 litellm_config.yaml contains model_name: agent-slot
[PASS] C12 litellm_config.yaml contains api_base: http://127.0.0.1:8080/v1
[PASS] C13 dir engine absent
[PASS] C14 dir models absent
[PASS] P1 py_compile test_contract.py
[SKIP] P2 yaml parse litellm_config.yaml (PyYAML not installed)
RESULT passed=15 failed=0 skipped=1
EXIT_CODE=0
```
**التقييم:** مطابق 100% للمتوقع — صفر FAIL، P2 SKIP فقط (PyYAML غير مثبت)، exit 0. تم التحقق من أول مرة (لا تكرار).

[STAGE T3 DONE]

## 124 · user (2026-11-21 19:47:54)

B3 (T3) قُبلت بعد التحقق المستقل (الجسم مطابق حرفياً لـ README س93–112). الآن الدفعة B4 = **T6 فقط** — آخر دفعة في S1 — منطقة حمراء (ملفان مشتركان مع المالك). لا تلمس أي ملف آخر.

## المسار
`D:\SMS\.hRhR_gateway-service\scratch\sandbox_resume_test`

## الخطوة 0 الإلزامية (قبل أي تعديل)
انسخ `README.md` إلى `%TEMP%\opencode\README.before.md` (أي `~\AppData\Local\Temp\opencode\README.before.md`) كلقطة قبلية. أبلغ المسار الكامل وحجم اللقطة في التقرير.

## T6-أ — `README.md`: تعديل محصور في قسم "السجل الحي" (من السطر 169 فصاعداً فقط)
**ممنوع تماماً** تغيير أي حرف في السطور 1–168 (الأقسام 1–5). اقرأ القسم أولاً ثم عدّل **فقط**:
1. سطر "الإصدار الحالي" → `v0.2 (Scaffolding — no download)`.
2. سطر "الحالة" → جملة واحدة: الأسكلة جاهزة (غلاف فحص + إعدادات + سكريبتات غير منفذة)، التحميل والتشغيل مؤجلان إلى S2/S3.
3. سطر إنجاز **واحد** جديد في "سجل الإنجازات" (بتاريخ 2026-11-21): إنشاء الأسكلة بدون تحميل — `run_tests.cmd` يمر بـ `passed=15 failed=0 skipped=1`.
4. إضافة الملفات الجديدة إلى قائمة "الملفات الجديدة": `run_tests.cmd`, `.gitignore`, `litellm_config.yaml`, `test_contract.py`, `scripts/download_engine.ps1`, `scripts/download_model.ps1`, `scripts/start_llama_server.ps1`, `scripts/start_litellm.ps1`, `PLAN.md`, `TASKS.json`, `DUET_LOG.md`, `duet_resume.json` — **بدون** `وكيل-الثاني.txt` إطلاقاً.
- جدولا "سجل المشاكل" و"دروس مستفادة" **لا يُمسّان**.
- حافظ على نفس الترميز (UTF-8) ونفس نمط نهايات الأسطر الموجود في الملف (لا تحوّل LF↔CRLF).

## T6-ب — `.agents/memory/CHANGELOG_DECISIONS.md`: إلحاق قسم جديد في نهاية الملف
اقرأ الملف أولاً وقلّد **حرفياً** بنية الأقسام الموجودة (عنوان `##` + البنود الأربعة بنفس صياغتها وترتيبها): **المشكلة / الهدف**، **الملفات المُضافة**، **الدرس المستفاد**، **المخاطر المحتملة (Risks)**. المحتوى:
- **المشكلة / الهدف:** تحويل README من دليل ورقي إلى أسكلة قابلة للتحقق بدون أي تحميل أو تشغيل (قرار المالك: أسكلة بدون تحميل). قرار الموديل: أساسي `LFM2.5-1.2B-Instruct-Q4_K_M` (LiquidAI) / احتياطي `granite-4.0-h-350m-Q4_K_M` (ibm-granite) — أسماء فقط. قرارات المالك: D1 = `-Model` خياران فقط (LFM2.5-1.2B افتراضي + granite، بدون MiniCPM)؛ D2 = `api_key` حرفي `sk-local-placeholder`؛ D3 = بدون حارس `exit 1` (تعليق تحذيري فقط).
- **الملفات المُضافة:** نفس قائمة T6-أ (بدون `وكيل-الثاني.txt`).
- **الدرس المستفاد:** (منسوبة صراحةً إلى "مراجعة الوكيل الثاني — تحقق خارجي لم يُعَد في هذه الجلسة"): روابط `llama-b12606-bin-win-cpu-x64.zip` وملفات GGUF الثلاثة متاحة (استجابة `302 Found`) وأحجامها مطابقة للـ README؛ `chat_template.jinja`/`tokenizer_config.json` موجودة في المستودعات الأساسية للنماذج لا في جذر مستودعات `*-GGUF`؛ `v1.0.0 = latest` بلا أصول ويندوز؛ `-ctv q8_0` يشترط عدم تعطيل Flash Attention في llama.cpp؛ مسار `llama-server.exe` بعد فك الضغط قد يكون داخل مجلد فرعي (عولج بالبحث المتكرر في `start_llama_server.ps1`). إضافة: PyYAML غير مثبت على هذا الجهاز → P2 يبقى SKIP بلا `pip install`.
- **المخاطر المحتملة (Risks):** الروابط لم تُنزَّل ولم تُفحص بنية الـ zip (S2/S3)؛ `-fa` غير مضاف وقد يرفض السيرفر `-ctv q8_0` (يُحسم في S2)؛ السكريبتات لم تُنفَّذ قط؛ `api_key` حرفي يجب استبداله بمتغير بيئة عند الإنتاج.

## محظورات صارمة
- لا تعدّل: `وكيل-الثاني.txt`، `run_tests.cmd`، `.gitignore`، `litellm_config.yaml`، `test_contract.py`، `scripts\*.ps1`، `PLAN.md`، `TASKS.json`، `DUET_LOG.md`، `duet_resume.json`.
- لا تنشئ أي ملف جديد داخل المشروع (اللقطة القبلية في `%TEMP%` فقط).
- لا تنفيذ لأي سكريبت / لا `pip install` / لا تنزيل.

## التحقق المطلوب بعد الكتابة
1. قارن السطور 1–168 بين `README.before.md` و`README.md` (مثلاً `Compare-Object` على `Get-Content`[0..167]) وأبلغ النتيجة حرفياً (المتوقع: لا فروق).
2. شغّل `.\run_tests.cmd unit` → المتوقع `RESULT passed=15 failed=0 skipped=1`، exit 0.

## صيغة التقرير
`EXEC_DONE T6` + مسار وحجم اللقطة القبلية + نتيجة مقارنة س1–168 حرفياً + الأسطر المعدلة/المضافة في README (رقم السطر + النص الجديد) + القسم المُلحق في CHANGELOG حرفياً كاملاً + مخرج `run_tests.cmd unit` كاملاً مع EXIT_CODE. إذا فشل نفس الفحص مرتين أبلغ `[توقف - تكرار مرتين]` مع السبب.

## 125 · assistant (2026-11-21 19:47:54)

سأبدأ الدفعة B4 بالخطوة 0: أخذ اللقطة القبلية لـ `README.md` في `%TEMP%\opencode` والتحقق من حجمها، مع فحص نمط نهايات الأسطر والترميز الحالي للملف قبل أي تعديل.

## 135 · assistant (2026-11-21 19:48:23)

اللقطة القبلية مأخوذة (9223 بايت، README بترميز UTF-8 بدون BOM ونهايات LF فقط). الآن أقرأ `CHANGELOG_DECISIONS.md` لتقليد بنية أقسامه حرفياً قبل أي تعديل.

## 145 · assistant (2026-11-21 19:48:36)

قرأت `CHANGELOG_DECISIONS.md` (بنية: عنوان `##` + 4 بنود). أبدأ T6-أ بتعديل سطرَي "الإصدار الحالي" و"الحالة" (172–173) فقط عبر `edit` (يحافظ على LF والترميز).

## 155 · assistant (2026-11-21 19:49:02)

تم تعديل سطرَي الإصدار والحالة. الآن أضيف سطر الإنجاز الجديد في "سجل الإنجازات" بعد السطر 177 الأصلي (بدون المساس بالسطرين الموجودين).

## 165 · assistant (2026-11-21 19:49:21)

تم إضافة سطر الإنجاز وقائمة الملفات الجديدة في README. أنتقل الآن إلى T6-ب: إلحاق القسم الجديد في نهاية `CHANGELOG_DECISIONS.md` بنفس بنية الأقسام الموجودة (عنوان `##` + البنود الأربعة)، عبر `edit` للحفاظ على LF والترميز.

## 175 · assistant (2026-11-21 19:49:47)

تم إلحاق القسم في CHANGELOG. الآن التحقق النهائي: مقارنة السطور 1–168 بين اللقطة القبلية وREADME، فحص الترميز/نهايات الأسطر بعد التعديل، عرض القسم المُلحق والسطور المعدلة، ثم تشغيل `run_tests.cmd unit`.

## 185 · assistant (2026-11-21 19:50:10)

التحقق نجح بالكامل (س1–168 بلا فروق، `passed=15 failed=0 skipped=1`، exit 0). أقرأ الآن ملف الذيل المؤقت لأبلّغ أرقام السطور المعدلة/المضافة في README بدقة (لأن الكونسول يعرض العربية كـ `?`).

## 195 · assistant (2026-11-21 19:50:27)

التحقق اكتمل بالكامل: السطور 1–168 بلا فروق، الترميز ونهايات الأسطر محفوظة (UTF-8 بدون BOM، LF فقط)، والفحوص `passed=15 failed=0 skipped=1` بـ exit 0.

---

# EXEC_DONE T6

## الخطوة 0 — اللقطة القبلية
- **المسار:** `~\AppData\Local\Temp\opencode\README.before.md`
- **الحجم:** 9223 بايت (مطابق لحجم `README.md` الأصلي قبل التعديل: 9223 بايت، 190 سطراً، UTF-8 بدون BOM، LF فقط).

## نتيجة مقارنة السطور 1–168 (حرفياً)
```
BEFORE_LINES=190 AFTER_LINES=203
LINES_1_168: NO_DIFFERENCES
```
(`Compare-Object -SyncWindow 0` على `[0..167]` من اللقطة القبلية مقابل الملف الحالي → **لا فروق**.)

## T6-أ — الأسطر المعدلة/المضافة في `README.md` (الحالة بعد التعديل: 10281 بايت، 203 سطر، UTF-8 بدون BOM، CRLF=0 / LF=203)

**أسطر معدلة (2):**
- **172:** `* **الإصدار الحالي:** v0.2 (Scaffolding — no download)`
- **173:** `* **الحالة:** الأسكلة جاهزة (غلاف فحص + إعدادات + سكريبتات غير منفذة)، التحميل والتشغيل مؤجلان إلى S2/S3.`

**سطر إنجاز مضاف (1):**
- **178:** `* (2026-11-21) إنشاء الأسكلة بدون تحميل — `run_tests.cmd` يمر بـ `passed=15 failed=0 skipped=1`.`

**أسطر مضافة في "الملفات الجديدة" (12 — بعد سطر `README.md` الأصلي الذي صار 181):**
- **182:** `* `run_tests.cmd` — غلاف الفحوص الثابتة والبايثونية (S1).`
- **183:** `* `.gitignore` — استبعاد `engine/` و `models/` و `*.gguf`.`
- **184:** `* `litellm_config.yaml` — إعدادات `LiteLLM Proxy` (مطابق للقسم 4-ب).`
- **185:** `* `test_contract.py` — اختبار العقد وتمرير الأدوات.`
- **186:** `* `scripts/download_engine.ps1` — تحميل `llama.cpp` (غير منفذ).`
- **187:** `* `scripts/download_model.ps1` — تحميل الموديل GGUF (غير منفذ).`
- **188:** `* `scripts/start_llama_server.ps1` — تشغيل `llama-server.exe` (غير منفذ).`
- **189:** `* `scripts/start_litellm.ps1` — تشغيل `LiteLLM Proxy` (غير منفذ).`
- **190:** `* `PLAN.md` — خطة المراحل S1/S2/S3.`
- **191:** `* `TASKS.json` — سجل المهام.`
- **192:** `* `DUET_LOG.md` — سجل الحوار بين المخطط والمنفذ.`
- **193:** `* `duet_resume.json` — نقطة الاستئناف.`

**لم يُمسّ:** `وكيل-الثاني.txt` غير مذكور إطلاقاً؛ جدولا "سجل المشاكل" (195–198) و"دروس مستفادة" (200–202) بلا أي تغيير (انتقلا فقط بالإزاحة من 182/187 إلى 195/200).

## T6-ب — القسم المُلحق في `.agents/memory/CHANGELOG_DECISIONS.md` (حرفياً كاملاً)
(الملف بعد التعديل: 3719 بايت، 14 سطراً، UTF-8 بدون BOM، LF فقط — أُلحق بعد السطر 7 الأصلي بسطر فارغ فاصل، بنفس بنية القسم الموجود: عنوان `##` + البنود الأربعة بنفس الصياغة والترتيب.)

```
## تحويل `README.md` إلى أسكلة قابلة للتحقق بدون تحميل (S1 — v0.2 Scaffolding)
- **المشكلة / الهدف:** تحويل README من دليل ورقي إلى أسكلة قابلة للتحقق بدون أي تحميل أو تشغيل (قرار المالك: أسكلة بدون تحميل). قرار الموديل: أساسي `LFM2.5-1.2B-Instruct-Q4_K_M` (LiquidAI) / احتياطي `granite-4.0-h-350m-Q4_K_M` (ibm-granite) — أسماء فقط. قرارات المالك: D1 = `-Model` خياران فقط (LFM2.5-1.2B افتراضي + granite، بدون MiniCPM)؛ D2 = `api_key` حرفي `sk-local-placeholder`؛ D3 = بدون حارس `exit 1` (تعليق تحذيري فقط).
- **الملفات المُضافة:** `run_tests.cmd`، `.gitignore`، `litellm_config.yaml`، `test_contract.py`، `scripts/download_engine.ps1`، `scripts/download_model.ps1`، `scripts/start_llama_server.ps1`، `scripts/start_litellm.ps1`، `PLAN.md`، `TASKS.json`، `DUET_LOG.md`، `duet_resume.json`.
- **الدرس المستفاد:** (منسوبة إلى مراجعة الوكيل الثاني — تحقق خارجي لم يُعَد في هذه الجلسة) روابط `llama-b12606-bin-win-cpu-x64.zip` وملفات GGUF الثلاثة متاحة (استجابة `302 Found`) وأحجامها مطابقة للـ README؛ `chat_template.jinja`/`tokenizer_config.json` موجودة في المستودعات الأساسية للنماذج لا في جذر مستودعات `*-GGUF`؛ `v1.0.0 = latest` بلا أصول ويندوز؛ `-ctv q8_0` يشترط عدم تعطيل Flash Attention في llama.cpp؛ مسار `llama-server.exe` بعد فك الضغط قد يكون داخل مجلد فرعي (عولج بالبحث المتكرر في `start_llama_server.ps1`). إضافة: PyYAML غير مثبت على هذا الجهاز → P2 يبقى SKIP بلا `pip install`.
- **المخاطر المحتملة (Risks):** الروابط لم تُنزَّل ولم تُفحص بنية الـ zip (S2/S3)؛ `-fa` غير مضاف وقد يرفض السيرفر `-ctv q8_0` (يُحسم في S2)؛ السكريبتات لم تُنفَّذ قط؛ `api_key` حرفي يجب استبداله بمتغير بيئة عند الإنتاج.
```

## الالتزام بالمحظورات
- الملفان المعدلان فقط: `README.md` (من السطر 169 فصاعداً حصراً) و `.agents/memory/CHANGELOG_DECISIONS.md` (إلحاق في النهاية).
- لم يُعدَّل أي من: `وكيل-الثاني.txt`، `run_tests.cmd`، `.gitignore`، `litellm_config.yaml`، `test_contract.py`، `scripts\*.ps1`، `PLAN.md`، `TASKS.json`، `DUET_LOG.md`، `duet_resume.json`.
- لم يُنشأ أي ملف جديد داخل المشروع. **إفصاح:** أُنشئ ملف مساعد مؤقت خارج المشروع في `%TEMP%\opencode\README.tail.txt` (ذيل README بالترميز الصحيح لقراءة أرقام السطور لأن كونسول PowerShell يعرض العربية كـ `?`) — يمكن حذفه بأمان.
- لا تنفيذ لأي سكريبت / لا `pip install` / لا تنزيل. لا تعديل في أي ملف اختبار.

## أمر التحقق والمخرج الحرفي الكامل
`cmd /c "run_tests.cmd unit"` من `D:\SMS\.hRhR_gateway-service\scratch\sandbox_resume_test`:
```
[PASS] C1 file .gitignore
[PASS] C2 file litellm_config.yaml
[PASS] C3 file test_contract.py
[PASS] C4 file scripts\download_engine.ps1
[PASS] C5 file scripts\download_model.ps1
[PASS] C6 file scripts\start_llama_server.ps1
[PASS] C7 file scripts\start_litellm.ps1
[PASS] C8 .gitignore contains engine/
[PASS] C9 .gitignore contains models/
[PASS] C10 .gitignore contains *.gguf
[PASS] C11 litellm_config.yaml contains model_name: agent-slot
[PASS] C12 litellm_config.yaml contains api_base: http://127.0.0.1:8080/v1
[PASS] C13 dir engine absent
[PASS] C14 dir models absent
[PASS] P1 py_compile test_contract.py
[SKIP] P2 yaml parse litellm_config.yaml (PyYAML not installed)
RESULT passed=15 failed=0 skipped=1
EXIT_CODE=0
```
**التقييم:** مطابق 100% للمتوقع — صفر FAIL، P2 SKIP فقط، exit 0. تم التحقق من أول مرة (لا تكرار).

[STAGE T6 DONE]
