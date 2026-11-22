# 📐 خطة التطوير المعمارية لـ NoteGPT (v3.0 Production Blueprint)
## Multi-Turn Session Memory · Camera-Roll Sandbox Exporter · Gateway Service Onboarding

> **تاريخ التوثيق:** 2026-09-25
> **المرجع الحاكم:** [دستور بولا الهندسي v1.2](file:///d:/SMS/.hRhRhRhRhRhR/.agents/rules/00-bolla-constitution.md) + [AGENTS.md v2.6](file:///d:/SMS/.hRhRhRhRhRhR/.agents/AGENTS.md) + [سير عمل التخطيط /00-planning](file:///d:/SMS/.hRhRhRhRhRhR/.agents/workflows/00-planning.md)
> **الحالة:** 🟢 جاهزة للتنفيذ التتابعي المعتمد

---

## 🎯 1. الأهداف والنطاق (Goals & Non-Goals)

### ✅ الأهداف المعتمدة (Goals):
1. **المرحلة 1 — الذاكرة المتصلة متعددة الجولات (Multi-Turn Chat Memory):**
   - قراءة وحفظ معرف الجلسة في ملف `active_session.txt` داخل مجلد `01_notegpt_pure_v01`.
   - إذا كان الملف يحتوي على `conversation_id`، يستمر الأيجنت في نفس المحادثة على ساندبوكس ديتونا السحابي محتفظاً بالذاكرة والسياق.
   - إذا تم مسح الملف أو تفريغه، يبدأ شات جديد كلياً من الصفر (`🆕 بدء محادثة جديدة`).
2. **المرحلة 2 — نظام تصدير الملفات وسجل الكاميرات (FIFO Camera-Roll Project Manager):**
   - اعتراض مخرجات الأيجنت (CDN / tool_call_result / Markdown code blocks) وتنزيلها محلياً في مجلد `agent_output/{timestamp}_{clean_title}/`.
   - تطبيق خوارزمية تدوير سجل الكاميرات FIFO للحفاظ على آخر 10 مشاريع فقط وحذف الأقدم تلقائياً لمنع امتلاء القرص.
3. **المرحلة 3 — دمج NoteGPT كـ Provider رسمي في بوابة الجيتواي (`__gateway-service`):**
   - بناء حزمة `__gateway-service/providers/notegpt/` بالطبقات الثلاث القياسية (`_core.py`, `adapter.py`, `definition.py`, `models_metadata.json`).
   - ربط الموديلين المعتمدين (`kimi-k3` كافتراضي و `deepseek-v4-flash`).
   - اجتياز اختبارات العزل الهيرميتك بنسبة 100% بدون أي متصفح (Pure Requests).

### ⛔ ما هو خارج النطاق حالياً (Non-Goals):
- إنشاء حسابات جديدة لـ NoteGPT (بناءً على توجيه المستخدم: "سيبك منه").
- نقل المجلد من `بعدين` إلى `شغال` (بناءً على توجيه المستخدم: "أنا هنقله بعدين").

---

## 📜 2. أدلة الإسناد المرجعي الصريحة (Verbatim Ground-Truth Citations)

### أ. الدليل المرجعي لإدارة الجلسة (`active_session.txt`):
- **المصدر المعتمد:** [`01.06_notegpt_agent_mode.py`](file:///d:/SMS/.hRhRhRhRhRhR/.AAA_GGG_iii_VIBE_CODING/بعدين/NOT_EGPT/01.06_notegpt_agent_mode.py#L356-L384)
- **النطاق بالسطور:** L356-L384 و L1243-L1259
- **الاقتباس الحرفي:**
  ```python
  def load_active_session() -> str:
      """قراءة معرف الجلسة الحالي للاستمرار في نفس المحادثة بضغطة زر Run (Multi-Turn Session)"""
      session_file = pathlib.Path(Config.ACTIVE_SESSION_FILE)
      if session_file.exists():
          try:
              with open(session_file, "r", encoding="utf-8") as f:
                  cid = f.read().strip()
                  if cid and len(cid) >= 16:
                      return cid
          except Exception:
              pass
      return create_and_save_new_session()
  ```

### ب. الدليل المرجعي لسجل الكاميرات وتصدير ملفات الساندبوكس (FIFO 10 Buffer):
- **المصدر المعتمد:** [`01.06_notegpt_agent_mode.py`](file:///d:/SMS/.hRhRhRhRhRhR/.AAA_GGG_iii_VIBE_CODING/بعدين/NOT_EGPT/01.06_notegpt_agent_mode.py#L916-L1008)
- **النطاق بالسطور:** L916-L933 و L935-L1008
- **الاقتباس الحرفي:**
  ```python
  def manage_saved_projects_buffer(output_base_dir: pathlib.Path, max_projects: int = Config.MAX_SAVED_PROJECTS):
      """تدوير المجلدات للحفاظ على آخر 10 مشاريع فقط (نظام مسح الأقدم FIFO)"""
      subdirs = [d for d in output_base_dir.iterdir() if d.is_dir()]
      if len(subdirs) > max_projects:
          subdirs.sort(key=[REDACTED:KV_SECRET] x: x.stat().st_mtime)
          dirs_to_delete = subdirs[:len(subdirs) - max_projects]
          for d in dirs_to_delete:
              shutil.rmtree(d, ignore_errors=True)
          print(f"\n[تدوير السجل الذكي - FIFO]: تم تنظيف {len(dirs_to_delete)} مجلد قديم للحفاظ على آخر {max_projects} مشاريع فقط (نظام سجل الكاميرات).")
  ```

### ج. الدليل المرجعي لدستور إضافة مزودي الجيتواي:
- **المصدر المعتمد:** [`.agents/workflows/00-gateway-provider-onboarding.md`](file:///d:/SMS/.hRhRhRhRhRhR/.agents/workflows/00-gateway-provider-onboarding.md)
- **الاشتراطات:** معمارية الطبقات الثلاث، الـ 7 Invariants، وقانون الصفر متصفح بنسبة 100%.

---

## ⚖️ 3. مصفوفة تصنيف المخاطر والبوابات (Risk Classification & Gates)

| المرحلة | التعديل المستهدف | التصنيف | الإجراء الوقائي الدستوري |
|---|---|:---:|---|
| **المرحلة 1** | دمج إدارة الجلسات `active_session.txt` في `main.py` | 🟡 T1 | حفظ مرساة `.anchor` + حساب SHA-256 + فحص التراجع |
| **المرحلة 2** | دمج مستخرج الملفات وتدوير الكاميرات FIFO في `main.py` | 🟡 T1 | عزل دالة `extract_and_save_sandbox_files` واختبارها محلياً |
| **المرحلة 3** | إنشاء وتدشين مزود `notegpt` داخل `__gateway-service` | 🔴 T2 | بناء طبقات Core / Adapter / Definition واختبارات Hermetic معزولة |

---

## 🛠️ 4. خطوات التنفيذ التتابعي الصارم (Step-by-Step Execution Plan)

### 🔹 الخطوة 1: تجهيز وتثبيت الذاكرة متعددة الجولات (Multi-Turn Chat) في `main.py`:
1. إضافة متغير `ACTIVE_SESSION_FILE = BASE_DIR / "active_session.txt"` وثوابت الإعدادات.
2. دمج دوال `load_active_session()` و `save_active_session()` و `create_and_save_new_session()`.
3. التحقق من حالة الجلسة قبل إرسال السؤال:
   - طباعة بانر نيون: `🆕 [بدء شات جديد]: تم اكتشاف مسح ملف الجلسة...`
   - أو `🔄 [استمرار في نفس الشات]: جاري مواصلة المحادثة السابقة (Session: xxxx)...`
4. تمرير `conversation_id` المحفوظ لـ `ask_notegpt_agent`.

### 🔹 الخطوة 2: دمج نظام استخراج ملفات الساندبوكس وتدوير الكاميرات (FIFO 10):
1. دمج دالة `manage_saved_projects_buffer(output_base, max_projects=10)`.
2. دمج دالة `extract_and_save_sandbox_files(reasoning, answer, prompt)` لالتقاط:
   - روابط CDN `cdn.ng-resource.com` وتنزيلها بـ `requests.get`.
   - كائنات `tool_call_result` التي تحتوي على `file_path` و `content`.
   - كتل الأكواد المعنونة في الماركداون.
3. استدعاء الدالة فور اكتمال الإجابة وحفظ الملفات في `agent_output/{timestamp}_{clean_title}`.
4. طباعة ملخص الملفات المحفوظة بدقة وأحجامها.

### 🔹 الخطوة 3: التحقق والاختبار الحي المزدوج:
1. **اختبار 1:** إرسال سؤال يطلب كتابة ملف كود (مثال: سكربت بايثون معنون) والتأكد من تنزيله في `agent_output/`.
2. **اختبار 2:** إرسال سؤال استكمالي على نفس الجلسة بدون مسح `active_session.txt` والتأكد من تذكر الموديل للسؤال السابق.
3. **اختبار 3:** تفريغ ملف `active_session.txt` والتأكد من توليد جلسة جديدة كلياً وبدء شات جديد.
4. **اختبار 4:** التأكد من تدوير مجلدات `agent_output` وحذف ما يزيد عن 10 بنظام الكاميرات.

### 🔹 الخطوة 4: تدشين NoteGPT كـ Provider في بوابة الجيتواي (`__gateway-service`):
1. إنشاء مجلد `__gateway-service/providers/notegpt/`.
2. بناء `models_metadata.json` متضمناً `kimi-k3` و `deepseek-v4-flash`.
3. بناء `_core.py` مستدعياً `notegpt_signer.py` و `node_wasm_signer.js` بدون متصفح.
4. بناء `adapter.py` لترجمة العقود واستخراج الرد الصافي النظيف.
5. بناء `definition.py` مع حصر القدرات (`generate_text`, `chat`).
6. كتابة حزمة اختبارات `tests/providers/test_notegpt.py` واجتيازها بنجاح 100%.
7. تسجيل المزود في `__gateway-service/app.py`.

---

## 🛡️ 5. خطة التراجع السريع وحماية السلامة (Pre-mortem & Rollback)
- ملف `main.py` محمي بمرساة مشمعة بـ SHA-256 في `Root/ANCHORS.md`:
  - المرساة: `anchor_notegpt_main_kimi_default_v1`
  - الهاش: `8bfbc4cb0678c43f8c375598889ddb7a9c3203e90757e49ffe6ac7c1a7a96930`
- عند حدوث أي خطأ غير متوقع، يتم التراجع الفوري لنفس المرساة واستعادة الحالة المستقرة في ثانية واحدة.
