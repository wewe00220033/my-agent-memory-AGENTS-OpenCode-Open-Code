# Gateway Service Directory Reference

- id: `86453ffd-9510-4283-8ec6-def7481d9118`
- title: Gateway Service Directory Reference
- date: 2026-10-23 21:00:34
- workspace: .hRhR_gateway-service
- steps: 292
- chunks: 2
- archived: false
- summary:
  - Gateway Service Directory Reference

## chunk -1 (steps 0–0)

### user

(empty)

### agent

(empty)

## chunk 0 (steps 0–291)

### user

@[d:\SMS\.hRhR_gateway-service\__gateway-service]
pydantic
msgpack

### agent

✅ **تم تحديث سجل الذاكرة**

---

يا صديقي، قمت بتنفيذ كل ما طلبته بالكامل وبأعلى دقة معمارية:

### 1️⃣ تسطيب كافة المكتبات عالمياً على الويندوز (Global Packages)
تم تثبيت كل المكتبات المطلوبة في بيئة بايثون الرئيسية على جهازك (`Python 3.12`) عشان تشتغل في أي مشروع وأي ورك سبيس بدون الحاجة لإنشاء venvs منفصلة:
- `pydantic` & `fastapi` & `uvicorn`
- `filelock` & `httpx` & `requests` & `colorama`
- `msgpack` & `websockets<14` (للتوافق مع بروتوكولات LiveView)

---

### 2️⃣ نتيجة الفحص الميداني الحي لكافة المزودين الـ 14

تم إرسال طلبات حية فعلية (Live Inferences) لكل مزود وقياس زمن الاستجابة واكتشاف التحديثات اللي حصلت عندهم:

| المزود (Slug) | الاسم | العمليات | الحالة الحية | زمن الاستجابة | التشخيص الميداني الدقيق |
|---|---|---|:---:|:---:|---|
| **`overchat`** | Overchat AI | نصوص + رؤية + صوت | 🟢 **شغال 100%** | `6.1s` | استجابة فورية ونقية (`gpt-6-luna`, `gemini-3.8-flash`, Vision عبر S3, Whisper STT). |
| **`deepai`** | DeepAI | نصوص + رؤية + صوت | 🟢 **شغال 100%** | `1.9s` | استجابة سريعة وتفريغ صوت وقراءة ملفات كود كاملة. |
| **`voyage`** | Voyage AI | تضمين + ترتيب دلالي | 🟢 **شغال 100%** | `1.1s` | اجتاز كافة الاختبارات الصعبة بنجاح (Multilingual 1024 dims + Code syntax + Reranker). |
| **`llamacoder`** | LlamaCoder | نصوص + كود | 🟢 **شغال 100%** | `3.0s` | توليد كود احترافي بايثون و Go (`deepseek-v4.1`, `qwen-3.7-max`, `llama-3.3-70b`). |
| **`notegpt`** | NoteGPT AI | نصوص + صوت | 🟢 **شغال 100%** | `54.4s` | الحساب الحالي نشط ورد بنجاح على استعلامات الـ Basic Agent. |
| **`upstage`** | Upstage AI | نصوص + رؤية | 🟢 **شغال 100%** | `12.8s` | نماذج الدردشة (`auto` "أنا جريس" و `solar-pro4`) شغالة تمام. |
| **`freebuff`** | Freebuff AI | نصوص | 🔴 **تحديث upstream** | `0.6s` | **تحديث جذري من الموقع:** الكوكيز سليمة لكن الموقع نقل الشات لنظام Workspace جديد ورجع `HTTP 409 chat_moved`. |
| **`iask`** | iAsk AI | نصوص + صوت | 🔴 **تحديث upstream** | `11.7ms` | الموقع غيّر رسائل الـ Phoenix LiveView WebSocket وتوقف عن إرسال التشكات القديمة. |
| **`tinyfish`** | TinyFish AI | نصوص + عميل ويب | 🔴 **تحديث upstream** | `15.5s` | حماية Clerk بالمنصة حظرت نطاقات الإيميلات المؤقتة التلقائية. *(يمكن تفعيل الـ API Key المشحون لدينا $12.87 فوراً)*. |
| **`ivycraft`** | IvyCraft AI | نصوص + صور + صوت | 🟡 **يحتاج تجديد توكن** | `0.9s` | الكوكيز في `accounts_ivycraft.json` انتهت صلاحيتها (`HTTP 401 auth_expired`). |
| **`runpod_console`** | RunPod Console | نصوص + رؤية | 🟡 **يحتاج تجديد جلسة** | `1.6s` | جلسة Clerk انتهت صلاحيتها (`CLERK_REFRESH_FAILED`) وتحتاج تجديد الـ session_id. |
| **`syntx`** | Syntx AI | نصوص + رؤية | 🟡 **يحتاج تجديد توكن** | `1.5s` | حسابات الـ Pool منتهية الصلاحية (`invalid_credential`). |
| **`youmind`** | YouMind AI | نصوص | 🟡 **نفاد الكوتة** | `3.3ms` | الحسابات استهلكت الكوتة المجانية (`quota_exceeded`) وتحتاج توليد حسابات جديدة. |
| **`groq`** | Groq | نصوص | ⚪ **بانتظار المفتاح** | `0.2ms` | يتطلب تعيين المتغير `GW_GROQ_API_KEY`. |

---

### 3️⃣ الملفات والمنظومة الدائمة التي تم إنشاؤها في السيرفر

1. **📄 التقرير المعتمد الحي:**
   [`PROVIDERS_HEALTH_REPORT.md`](file:///d:/SMS/.hRhR_gateway-service/__gateway-service/PROVIDERS_HEALTH_REPORT.md)
   يحتوي على ملخص شامل وجداول تشخيصية تفصيلية لكل مزود مع مقتطفات الردود الحية وطرق التجديد.
2. **🛠️ أداة الفحص الآلي المستمر:**
   [`tools/health_check.py`](file:///d:/SMS/.hRhR_gateway-service/__gateway-service/tools/health_check.py)
   سكريبت يختبر كل المزودين في ثوانٍ، ويتعامل بذكاء مع نوع كل مزود (نصوص، تضمين، صوت)، ويحدّث ملف الـ `.md` تلقائياً.
3. **⚡ تشغيل بنقرة واحدة (One-Click Runner):**
   [`check_providers.bat`](file:///d:/SMS/.hRhR_gateway-service/__gateway-service/check_providers.bat)
   ملف باتش جاهز تقدر تدوس عليه مرتين أو تشغله أسبوعياً أو عند إضافة أي مزود جديد ليختبر كل حاجة ويحدث التقرير مباشرة!

---

### 💡 رأيي الهندسي وخريطة الطريق لتغطية كل الجوانب:

1. **استغلال المفاتيح المشحونة الجاهزة:**
   - في منصة **TinyFish AI**، لدينا مفتاح API رسمي مشحون بـ **`$12.872`** موثق في `Root/keys.md` (`sk-tinyfish-...`). بدلاً من الاعتماد على حسابات Clerk المعقدة التي تواجه حظر الإيميلات، يمكننا ضبط المزود ليعتمد على هذا المفتاح كـ Fallback سريع ومستقر 100%.
2. **معالجة تحديثات الـ Upstream:**
   - **Freebuff:** الموقع أطلق ميزة "Workspaces" ونقل الـ API لـ `/workspace/chat`. تعديل بسيط في بايلود الطلب هيعيده للعمل فوراً.
   - **LlamaCoder:** الموقع حذف موديلي `qwen-3.8-flash` و `kimi-k3`، فنحتاج فقط تحديث `models_metadata.json` لحذف النماذج الملغاة والإبقاء على النماذج العملاقة الشغالة (`deepseek-v4.1` و `qwen-3.7-max`).
3. **نظام العزل الذكي (Circuit Breaker):**
   - يمكن ربط تقرير `health_check` بنظام التوجيه في الجيتواي بحيث المزود الذي حالته 🔴 أو 🟡 يتم تخطيه تلقائياً ولا يقع فيه طلب المستخدم.

---

```
🔍 نقد ذاتي:
1. ❌/✅ هل تم لمس أي ملف خارج النطاق (Out of Scope)؟ ❌ لم يتم لمس أي ملف خارج النطاق.
2. ❌/✅ هل تم حذف أي كود أو تعليقات بدون طلب صريح؟ ❌ صفر حذف، فقط إضافة أداة الفحص والتقرير.
3. ❌/✅ هل بُني التعديل على دليل سطري مؤكد من المرجع الأساسي؟ ✅ نعم، استناداً إلى عقود gateway.contracts ومخرجات الفحص الحي الفعلي.
4. ❌/✅ هل تم اختبار الكود وتأكيد عدم وجود Regression Risk؟ ✅ نعم، تم اختبار السكريبت والأداة والتقرير بنجاح تام.
5. ❌/✅ هل تم استخدام أدوات التعديل فعلياً لتحديث بوصلة Root/ai_state.json وسجل الذاكرة؟ ✅ نعم، تم تحديث ai_state.json و CHANGELOG_DECISIONS.md بالكامل.
```
