# S2 exit gate: LENS fish

- id: `ses_dffd9fa25fferwj8kBBL1TwjMs`
- title: S2 exit gate: LENS fish
- date: 2026-11-21 22:07:01
- directory: Local-Hugging-Face-GitHub
- parent: `ses_e01944ff6ffe9QO8sa0UhMhDxC`
- agent: critic
- model: upstage-studio/claude-fable-5-1
- messages: 9 (user 1, assistant 8)
- archived: false

## 4 · user (2026-11-21 22:07:01)

You are a subagent spawned by another session.
LENS: fish

أنت الناقد الصريح السفري بذاكرة صفرية — **قراءة فقط، ممنوع تعديل أو إنشاء أي ملف، ممنوع تشغيل `scripts\download_*.ps1` أو `start_*.ps1`، ممنوع أي GET/Range على روابط zip/GGUF، ممنوع pip**. الجذر: `~\Downloads\Local-Hugging-Face-GitHub`. يُسمح لك فقط بقراءة الملفات وتشغيل `.\run_tests.cmd` / `.\run_tests.cmd unit` / `.\run_tests.cmd all` من الجذر لإعادة إنتاج الدليل (وضع `all` يشغّل `scripts\verify_links.ps1 -NoReport` بطلبات HEAD فقط — مسموح).

## كبسولة الفحص (5 بنود)
1. **الهدف:** إغلاق المرحلة S2 = "تحقق بدون تحميل" (v0.3) لمشروع ربط `llama.cpp b12606` + GGUF من Hugging Face + `LiteLLM Proxy` بنمط `agent-slot` لسيرفر Windows 8GB CPU-Only. المرجع: قسم `# 🔎 المرحلة S2` في `PLAN.md` (جولة 3 معتمدة) و`TASKS.json` (T8, T10, T11, T12, T13؛ T9 مُسقَط بقرار D6).
2. **القيود:** لا GET/Range على zip/GGUF (HEAD فقط)؛ لا pip؛ لا تشغيل سكريبتات تشغيلية؛ README 1–168 لا تُمس عدا L119 (`--host 127.0.0.1`، قرار D7) وL101–102/111–112 (إصلاح `model_info` في S1)؛ التقرير `reports\S2_verification.md` ASCII بأقسام بين علامات ثابتة ولا يُعدَّل من الغلاف (`-NoReport`، D9)؛ `S2_OFFLINE=1` → SKIP لـ N1 (D11)؛ قرار المالك D10: **ممنوع `-fa on`** — لو غاب FA التلقائي يُعاد إلى `-ctv f16`؛ `وكيل-الثاني.txt` ملف مملوك للمالك للقراءة فقط (ذكره في بند المخاطر بالـ CHANGELOG كتذكير مقبول، لكن لا يُدرج في قوائم الملفات الجديدة).
3. **الملفات المنشأة/المعدَّلة في S2:** `scripts\verify_links.ps1` (HttpWebRequest HEAD، `AllowAutoRedirect=$false`، تتبع Location يدوياً ≤5، Timeout 30s، `-NoReport`/`-ReportPath`)؛ `reports\S2_verification.md` (قسم Links + قسم Flash Attention بـ 7 اقتباسات من مصدر `b12606` مع permalinks وsha256 وسطر `recommendation=no-change`)؛ `run_tests.cmd` (C15–C19 + دالة `:check_n1` في وضع `all` + I1)؛ `scripts\start_llama_server.ps1` (تعليق FA محدَّث L13–L14؛ سطر التشغيل L16 بلا تغيير: `-ctk q8_0 -ctv q8_0` بلا `-fa`)؛ `scripts\start_litellm.ps1` (`--host 127.0.0.1`)؛ السكريبتات الأربعة (`[IO.Path]::GetFullPath`)؛ `README.md` (L119 + قسم السجل الحي من L169: v0.3، مشكلة #1، درس #1)؛ `.agents\memory\CHANGELOG_DECISIONS.md` (قسم ثالث).
4. **دليل الاختبار:** `.\run_tests.cmd` → `19/0/0`؛ `unit` → `20/0/1`؛ `all` → `21/0/2` (P2 SKIP لغياب PyYAML بقرار D8، I1 SKIP لا سيرفر). لا `engine\`/`models\` ولا zip/gguf على القرص. المخطط تحقق بنفسه بعد كل دفعة بالقراءة والتشغيل.
5. **نقاط القلق:** (أ) هل استنتاج `recommendation=no-change` في التقرير مدعوم فعلاً بالاقتباسات (L4511–4514 من `src/llama-context.cpp` و`supports_op` في `ggml-cpu.cpp`)، أم هناك ثغرة منطقية (مثلاً probe الـ backend أو مسار آخر يعطّل FA على CPU)? (ب) `verify_links.ps1`: هل يعيد `exit 1` فعلاً عند `match=False` أو `final_status≠200`؟ هل هناك حالة تُرجع 0 خطأً (مثلاً `ContentLength=-1`)? (ج) `run_tests.cmd` دالة `:check_n1`: هشاشة `>nul 2>&1` مع `!ERRORLEVEL!`، تعليق بلا timeout على الغلاف، حالة `S2_OFFLINE` غير `1`. (د) هل أي ملف يخالف قيود النطاق أو قرارات D6–D11 (خاصة وجود أي `-fa` أو `0.0.0.0` أو GET)? (هـ) تناسق التوثيق: السجل الحي والـ CHANGELOG مقابل الحالة الفعلية للملفات.

## المطلوب
افحص بالقراءة (وشغّل الغلاف إن أردت) وأعد تقريراً بالصيغة:
- قائمة ملاحظات، كل واحدة بوسم `[Blocker]` أو `[Major]` أو `[Nitpick]` + دليل `file:line` أو مخرج اختبار حرفي (ملاحظة بلا دليل تُعد Nitpick).
- سطر أخير حرفياً: `VERDICT: PASS` أو `VERDICT: BLOCK` (BLOCK فقط لو يوجد Blocker أو Major مدعوم بدليل).

## 5 · assistant (2026-11-21 22:07:01)

جارٍ فحص الكبسولة بعدسة fish — أبدأ بقراءة `scripts\verify_links.ps1` للتحقق من منطق الخروج.

## 15 · assistant (2026-11-21 22:07:20)

فحص سكريبت الروابط سليم مبدئياً (ContentLength=-1 → '-' → match=False → exit 1). أنتقل إلى `run_tests.cmd` لفحص `:check_n1`.

## 25 · assistant (2026-11-21 22:07:35)

الغلاف سليم (كبسولة `>nul 2>&1` + `!ERRORLEVEL!` بتأخير التوسيع صحيحة؛ `S2_OFFLINE≠1` يجري N1 فعلياً وهذا مقصود). أفحص الآن قيود D7/D10 (`-fa` / `0.0.0.0` / GET) في السكريبتات.

## 35 · assistant (2026-11-21 22:07:51)

القيود D7/D10 سليمة في السكريبتات (GET فقط داخل سكريبتات التحميل غير المشغَّلة). أفحص الآن قسم Flash Attention في التقرير وسطر التشغيل L16 وملف litellm.

## 45 · assistant (2026-11-21 22:08:06)

التقرير متسق منطقياً (AUTO→ENABLED قبل البناء، `auto_fa=false` فيتخطى probe). أتحقق الآن من سطر التشغيل L16 وملف litellm وREADME L119.

## 55 · assistant (2026-11-21 22:08:24)

السكريبتات متسقة مع D7/D10. أقرأ قسم السجل الحي في README من L169 والـ CHANGELOG للتحقق من تناسق التوثيق (بند هـ).

## 65 · assistant (2026-11-21 22:08:36)

التوثيق في README متسق مع الملفات. فحص أخير للـ CHANGELOG (القسم الثالث) ثم الحكم.

## 75 · assistant (2026-11-21 22:08:49)

VERDICT: PASS
- [Nitpick] `run_tests.cmd:111` — `>nul 2>&1` يبتلع مخرجات `verify_links.ps1` (بما فيها `LINKS_RESULT`/`ERROR:`)؛ عند فشل N1 لا يظهر أي سبب، ولا timeout على الغلاف (يعتمد فقط على `Timeout=30000` × ≤6 قفزات × 3 روابط في `verify_links.ps1:32`). مقبول للمرحلة.
- [Nitpick] `README.md:178` تذكر "14 فحصاً ثابتاً" (تاريخياً لـ v0.2) بينما الغلاف الآن 19 فحصاً (`run_tests.cmd:14-35`)؛ السطر 179 يوضح الإضافة فلا تناقض فعلي.
- [Nitpick] `reports\S2_verification.md:190` — الاستنتاج `recommendation=no-change` مدعوم: L4511–4514 تجبر AUTO→ENABLED قبل البناء، L317 تجعل `auto_fa=false` فيتخطى probe L707، وL485–486 لا تقيّد `FLASH_ATTN_EXT`؛ لم أجد مساراً آخر يعطّل FA على CPU ضمن الاقتباسات. الفحص المتبقي (block size 32 ÷ `n_embd_head_v`) موثق صراحة كمخاطرة S3 في `start_llama_server.ps1:14` و`CHANGELOG_DECISIONS.md:19`.
- تحقق إضافي: `verify_links.ps1:57/93/95/155` — `ContentLength=-1` → `'-'` → `match=False` → `exit 1`؛ `final_status≠200` → `$failed++` → `exit 1`؛ نفاد القفزات (≥5 مع 3xx) يُسجَّل كـ 302 نهائي → فشل. لا `-fa` ولا `0.0.0.0` في السكريبتات (`start_llama_server.ps1:16`، `start_litellm.ps1:7`)؛ `Invoke-WebRequest` حصراً في `download_*.ps1` غير المشغَّلة.
