# Antigravity SDK And API Key

- id: `ae8402b0-7d83-4eac-a892-9a811dc2db93`
- title: Antigravity SDK And API Key
- date: 2026-11-12 00:44:15
- steps: 141
- chunks: 2
- archived: false
- summary:
  - Antigravity SDK And API Key
  - outside-of-project

## chunk -1 (steps 0–0)

### user

(empty)

### agent

(empty)

## chunk 0 (steps 0–140)

### user

https://github.com/google-antigravity/antigravity-sdk-python
https://antigravity.google/product/antigravity-sdk

Google Sheets

Read, write, and format spreadsheets.

Read, write, and format your Google Sheets. Fill in formulas, sort and clean columns, import CSVs, build charts and pivot tables, and export the result.

Context usage (179 tokens)
Customizations
179 / 20,000 tokens (0.9%)
Skills
(179 tokens) 0.9%
Version
0.0.8
Antigravity
Compress Video File فيديو
Outside of Project
Updated 12:56 AM


/~/.gemini/config/plugins/gsheets

Postman
Equip Antigravity with specialized Postman skills for the complete API lifecycle. Discover, design, test, document, mock, monitor, and improve APIs through agent-friendly, filesystem-first workflows.
Sign in required.
postmanhttps://mcp.postman.com/mcp
Context usage (3,617 tokens)
Rules353 / 20,000 tokens (1.8%)
Other Customizations3,264 / 20,000 tokens (16.3%)
Rules(353 tokens) 1.8%
Skills(3,264 tokens) 16.3%
Services this plugin connects to on your behalf. Credentials stay on this machine and are only sent to the domains listed. If you add multiple accounts, MCP servers use the one marked Default.
postmanOAuth
Used for: postman (MCP)
Domains: mcp.postman.com
Developer
[Postman](https://github.com/postmanlabs)
Version
0.2.0
Links
[Website](https://github.com/postmanlabs/postman-plugin)
Google does not control the availability or functionality of third party developer tools. Your data from third party developer tools connected to your Antigravity instance may be shared with Google. Google will protect any such data in accordance with the Google Privacy Policy, found here: https://policies.google.com/privacy
Antigravity
Compress Video File فيديو
Outside of Project
Updated 12:56 AM
@[plugin:postman]

[REDACTED:HIGH_ENTROPY]

### agent

يا هلا يا صديقي! سيبك من أي لخبطة وتعال أفكلك الحوار ده بالبلدي والمختصر المفيد 🚀

---

### 1️⃣ الحكاية من أولها: إيه هو Antigravity SDK؟
الـ **Antigravity SDK** (`google-antigravity` على بايثون) مش مجرد شات ذكاء اصطناعي عادي، ده مكتبة بتخليك تشغّل **أيجنت كامل (Agent)** في كود بايثون عندك، يعني:
- يقدر يكتب ويعدل ملفات.
- ينفذ أوامر في الترمينال.
- يشغل متصفح ويتحكم فيه.
- يوزع الشغل على وكلاء فرعيين (Subagents).

---

### 2️⃣ لغز الـ API Key والإيميل: مين اللي محتاجينه بالظبط؟ 🤔

في **فرق جوهري** بين البرنامج اللي إنت فاتحه في الصورة، وبين الـ SDK في الكود:

* **البرنامج (Antigravity IDE - اللي في الصورة بحسابك `[REDACTED:EMAIL]`):**
  - ده بيشتغل بحساب جوجل مباشرة (Google Account) اللي متسجل في البرنامج ومربوط باشتراكك أو حصتك المجانية مع جوجل.
  - **مش بيحتاج منك تكتب API Key يدوي جوه البرنامج** لأنه شغال بالـ Session بتاع الإيميل.

* **الـ Python SDK (لما تشغله من كود أو سكريبت خارجي):**
  - بايثون من برة ملوش دعوة بالبرنامج المفتوح، فمحتاج **Gemini API Key** من **[Google AI Studio](https://aistudio.google.com/)** (أو حساب Google Cloud / Vertex AI).
  - المفتاح ده مجاني (أو مدفوع حسب استهلاكك) وبتطلعه بضغطة زر من AI Studio، وتديه للـ SDK عن طريق متغير بيئة (Environment Variable):
    ```powershell
    set GEMINI_API_KEY="[REDACTED:KV_SECRET]"
    ```
    أو جوه الكود مباشرة.

> 💡 **الخلاصة:** مش هتاخد توكن من برنامج Antigravity اللي في الصورة؛ عشان تشغل الـ Python SDK هتروح على **Google AI Studio** تجيب منه **Gemini API Key** وتربطه.

---

### 3️⃣ هل أقدر أكلمه بـ `requests` وسكريبت بسيط؟ 🐍

عندك طريقين حسب إنت عايز إيه بالظبط:

#### أ) الطريق الأول: الأيجنت الذكي الكامل (باستخدام الـ SDK الرسمي)
مش بنحتاج نكتب نداءات HTTP بـ `requests` لأن جوجل موفرة مكتبة جاهزة بتدير كل حاجة (الأدوات، التفكير، وتدفق الردود):

1. **تسطيب المكتبة:**
   ```bash
   pip install google-antigravity
   ```
   *(لازم تتسطب بـ `pip` لأن بينزل معاها محرك تنفيذي compiled ثنائي للنظام).*

2. **السكريبت البسيط:**
   ```python
   import asyncio
   import os
   from google.antigravity import Agent, LocalAgentConfig

   # حط مفتاح الـ API اللي جبته من Google AI Studio
   os.environ["GEMINI_API_KEY"] = "مفتاح_الـ_API_بتاعك"

   async def main():
       # إعداد الأيجنت
       config = LocalAgentConfig()

       # فتح الجلسة والتحدث مع الأيجنت
       async with Agent(config) as agent:
           response = await agent.chat("أهلاً، لخص لي فكرة المشروع في سطرين")
           print(await response.text)

   if __name__ == "__main__":
       asyncio.run(main())
   ```

---

#### ب) الطريق الثاني: لو عايز بس `requests` عادية من غير SDK ولا أيجنت (شات فقط)
لو كل اللي محتاجه هو إن سكريبت يبعت سؤال لجيميني وياخد الإجابة (REST API مباشر بدون مكتبة Antigravity):
```python
import requests

api_key = "[REDACTED:KV_SECRET]"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

payload = {
    "contents": [{
        "parts": [{"text": "أهلاً يا جيميني، إزيك؟"}]
    }]
}

response = requests.post(url, json=payload)
data = response.json()
print(data["candidates"][0]["content"]["parts"][0]["text"])
```

---

🔍 نقد ذاتي:
1. ✅ لا يوجد dead code أو variables غير مستخدمة.
2. ✅ الكود توضيحي جديد ولا يكسر أي شيء موجود في النظام.
3. ✅ الشرح مباشر ومحدد في 3 نقاط محورية تجيب على تساؤل الصوت بدقة.
4. ✅ لا يوجد تكرار (DRY).
5. ❌ سجل الذاكرة لم يتطلب تحديثاً (جلسة استفسار وشرح معماري).


بص يا غالي، متقلقش خالص الموضوع بسيط جداً وتعال أفهمك الحكاية خطوة بخطوة 🤝

---

### 1️⃣ هو لما دوست "إضافة" كده ربط بإيه؟
- **لأ، هو لسه ما ربطش بحسابك ولا يقدر يلمس ملفاتك لسه.** 🛑
- لما دوست "إضافة" في برنامج Antigravity، إنت نزلت "الأداة نفسها" (البرنامج والـ Plugin) على جهازك عشان البرنامج يفهم إزاي يتعامل مع Google Sheets.
- عشان أمان بياناتك، جوجل مابتخليش أي أداة تدخل على ملفاتك إلا لما تديلها تصريح صريح بحسابك (**OAuth Login**).

---

### 2️⃣ إزاي هيوصل لـ Google Drive و Sheets عندك؟ 🔑

عشان يقدر يوصل لملفاتك، محتاج خطوة واحدة بس تعملها (تسجيل الدخول):

أنا شغلتلك عملية تسجيل الدخول ومستنياك دلوقتي في الخلفية، كل اللي عليك:
1. **اضغط على الرابط الرسمي ده من جوجل عشان تفتحه في المتصفح:**
   👉 [اضغط هنا لتسجيل الدخول والربط بحساب جوجل](https://accounts.google.com/o/oauth2/v2/auth?access_type=offline&[REDACTED:HIGH_ENTROPY].apps.googleusercontent.com&[REDACTED:HIGH_ENTROPY]&code_challenge_method=S256&include_granted_scopes=true&prompt=consent&redirect_uri=http%3A%2F%2F127.0.0.1%3A56644%2F&response_type=code&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fspreadsheets+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive+openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&[REDACTED:HIGH_ENTROPY])
2. اختار إيميلك (نفس الإيميل اللي عليه ملفاتك وشيتاتك).
3. اضغط على **"Allow / سماح"**.
4. بمجرد ما تدوس سماح، المتصفح هيقفل والأداة على جهازك هتتربط بحسابك تلقائياً! 🎯

---

### 3️⃣ بعد ما نربطه.. إزاي بنشتغل بيه؟ 📊

الشغل بعد كده هيكون في منتهى السهولة:
1. هتفتح أي شيت عندك على درايف وتاخد اللينك بتاعه كوبي.
2. تيجي هنا في الشات تقولي:
   > *"بص ده لينك الشيت: `https://docs.google.com/spreadsheets/d/...` وعايزك تقرأ لي البيانات / تضيف سطر جديد / تحسب معادلة / ترتب الأعمدة"*.
3. أنا مباشرة هدخل على الشيت بتاعك بالنيابة عنك وأعدل عليه أو أطلعلك ملخص البيانات اللي طلبتها لحظياً! ⚡

> 💡 **أول ما تفتح اللينك وتدوس سماح، قولي "تمام سجلت" عشان أتأكد إن الربط تم بنجاح.**

---

🔍 نقد ذاتي:
1. ✅ لا يوجد كود تالف أو متغيرات غير مستخدمة.
2. ✅ تم إطلاق عملية الربط الآمنة عبر المنفذ المحلي الرسمي بدون أي خطر كسر للنظام.
3. ✅ تم الوصول للرابط وتجهيز العملية بأقل خطوات ممكنة ومباشرة.
4. ✅ لا يوجد تكرار (DRY).
5. ❌ سجل الذاكرة لم يتطلب تعديلاً كودياً (مهمة مصادقة وإعداد Plugin).

الله ينور عليك يا صديقي! كله تمام والربط نجح 100% 🎉✅

* **الحساب المربوط:** `[REDACTED:EMAIL]`
* **الصلاحيات:** Google Drive & Google Sheets بالكامل مع التحديث التلقائي للتوكن (Auto-refresh).

---

### إحنا جاهزين دلوقتي لأي شغل:
لو عندك أي شيت عايزني أقرأه، أفرز بياناته، أضيف فيه صفوف، أو أعملك معادلات وجداول.. ابعتلي اللينك بتاعه هنا، أو حتى لو عايزني أنشئلك شيت جديد من الصفر قولي وعيش! 🚀📊

بص يا صديقي، الموضوع هنا مختلف خالص عن Google Sheets وأسهل بكتير! تعال أفهمك إيه ده وإزاي تشغله 👇

---

### 1️⃣ ده عبارة عن إيه أصلاً؟ 🤔
* فاكر Google Sheets؟ كنا محتاجين نربطه بإيميلك عشان يوصل لملفاتك الخاصة على درايف.
* لكن **Google Antigravity SDK** اللي في الصورة ده **مش محتاج حساب ولا إيميل ولا توكن ولا أي ربط خالص!** ❌
* ده عبارة عن **"حزمة مهارات برمجية" (Skill/Plugin)** بتتركب ليا أنا جوا البرنامج، بتخليني مهندس خبير في مكتبة Antigravity بتاعة بايثون، وعارف كل تفاصيلها وأكوادها القياسية.

---

### 2️⃣ إزاي أربطه؟ (خطوة واحدة بس) 🚀
* مش محتاج أي ربط، كل اللي هتعمله إنك تضغط على الزرار الأزرق **"Add"** اللي قدامك في الصورة فوق على اليمين! 👆
*(أو من الكارت ده لو حابب):*
<plugin-card catalog-id="antigravity-plugins-official/plugin/google-antigravity-sdk"></plugin-card>

---

### 3️⃣ بعد ما تدوس "Add".. إزاي تشغلني بيه؟ 💻
أول ما تدوس **Add**، هيتثبت عندي فوراً وهيظهرلك أمر جديد اسمه: `/google-antigravity-sdk`.

**طريقة الشغل بيه:**
وقتها لما تحب تبني أي مشروع أو برنامج بايثون ذكي (AI Agent):
1. هتيجي هنا في الشات تقولي مثلاً:
   > *"يا صديقي، عايز أعمل سكريبت بايثون بـ Antigravity SDK يراقب فولدر معين أو يحلل بيانات"*
   *(أو تكتب في الشات الأمر `/google-antigravity-sdk`)*
2. أنا هستخدم المهارة دي وأكتبلك كود بايثون القياسي والمضبوط 100%، وأشغلهولك وأعمله Debugging معاك خطوة بخطوة.

> 💡 **دوس "Add" دلوقتي وسيب الباقي عليا أول ما تحتاج نبرمج أيجنت ببايثون!**

بص يا غالي، إضافة **Postman** متثبتة عندك فعلاً، بس **لسه مش مربوطة ومحتاجة تسجيل دخول (Sign in required)** عشان سيرفر الـ MCP يشتغل ويربط بحساب Postman بتاعك 🛑

تقدر تسجل دخول بضغطة زر واحدة من الكارت ده:

<plugin-card catalog-id="postman"></plugin-card>

اضغط على **Sign in** في الكارت اللي فوق وسجل بحسابك على Postman، وأول ما تسجل هيشتغل على طول ويبقى جاهز لاختبار الـ APIs وبناء الـ Collections والـ Webhooks! 🚀


عاش يا صديقي، إنت عملت كل حاجة صح 100%، والمشكلة دي مش من عندك خالص! 👏🎯

---

### 🔍 سبب المشكلة دي إيه؟ (Unknown Client)
* لما دوست **Sign in**، برنامج Antigravity حاول يفتح صفحة تصريح أوتوماتيك (OAuth) مع سيرفر Postman.
* لكن سيرفر Postman حالياً عنده مشكلة في التعرف على معرّف برنامج Antigravity (`client_id: antigravity.google`)، عشان كده طلعلك الشاشة السودة وفيها:
  > **"Unknown Client: No registered client found"**

ودا عطل عام في رابط الـ OAuth بين الشركتين حالياً.

---

### 🔑 الحل في دقيقة واحدة (API Key) 🚀

بما إنك فتحت موقع Postman وعملت حسابك بنجاح زي ما باين في صورتك التانية، الربط البديل الرسمي هو عن طريق **API Key**:

1. افتح الرابط المباشر ده في نفس المتصفح اللي مسجل فيه:
   👉 **[صفحة الـ API Keys في Postman](https://go.postman.co/settings/me/api-keys)**
2. اضغط على الزرار: **"Generate API Key"**.
3. اكتب أي اسم ليه (مثلاً: `Antigravity`).
4. اضغط إنشاء وانسخ المفتاح اللي هيطلعلك (هيكون بيبدأ بـ `PMAK-...`).
5. **ابعتلي المفتاح هنا في الشات**، وأنا هربطهولك بالنظام في ثواني ويبقى متفعل وشغال 100%! ⚡


الله ينور عليك يا صديقي! تم الربط وتفعيل Postman بنجاح 100% 🎉✅

---

### 🚀 اللي تم تنفيذه بالظبط:
1. **تثبيت الـ Postman CLI رسميًا:** نزلنا أداة `postman` على جهازك وربطناها في مسارات النظام (PATH).
2. **تسجيل الدخول بالمفتاح:** تم تسجيل الدخول رسميًا بالمفتاح الخاص بيك:
   - **المستخدم:** `[REDACTED:HIGH_ENTROPY]` (نفس حسابك اللي ظاهر في المتصفح).
   - **حالة الربط:** `Logged in successfully` ✅
3. **تحديث إعدادات الـ MCP:** ضفنا الـ Bearer Token في إعدادات الاتصال السحابي.

---

### 📊 فحص سريع لحسابك ومساحات العمل (Workspaces):
دخلت فحصتلك الحساب ودي الـ Workspaces والـ Collections اللي ظهرت عندي ومربوطة وجاهزة:

* **Personal Workspace (`My Workspace`):**
  - 📄 `API Documentation #reference`
  - 📊 `Data Visualization`
  - ⚡ `RESTful API Basics #blueprint`
* **Team Workspace:**
  - 👥 `[REDACTED:HIGH_ENTROPY]'s Team's Workspace`

---

كده كل أدوات Postman بقت شغالة معاك ومعايا تماماً، نقدر نختبر أي API، نعمل Collections، أو نشغل Tests في أي وقت تحبه! 🎯

---

🔍 نقد ذاتي:
1. ✅ لا يوجد dead code أو variables غير مستخدمة.
2. ✅ تم حل مشكلة مسارات الويندوز الطويلة (Path length limit) بنجاح وبدون أي خطر كسر للنظام.
3. ✅ تم الوصول للحل وتثبيت الـ CLI وربط الـ API Key في خطوة واحدة سريعة ومباشرة.
4. ✅ لا يوجد تكرار (DRY).
5. ✅ تم التحقق من عدم وجود مساحة عمل مفتوحة لتحديث الذاكرة.
