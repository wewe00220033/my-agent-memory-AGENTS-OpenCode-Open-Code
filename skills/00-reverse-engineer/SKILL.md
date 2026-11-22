---
name: 00-reverse-engineer
description: بروتوكول الهندسة العكسية الذاتية للمزودين واكتشاف الـ APIs وفحص الرصيد وبناء مصانع الحسابات (Zero Browser + Pure Requests)
---

# 🕵️‍♂️ بروتوكول الهندسة العكسية للمزودين — Vibe Coding Provider Reverse-Engineering
## Workflow: 00-reverse-engineer

> **يُفعّل تلقائياً بـ `/00-reverse-engineer` أو عند فحص أي رابط مزود ذكاء اصطناعي جديد**
> **الهدف:** تفكيك المنصة، استخراج المعمارية والـ APIs، كشف الرصيد المجاني، اختبار التسجيل بالإيميل المؤقت (Zero Browser)، وبناء ملفات الربط والعميل ومصنع الحسابات وتوثيق الـ README.

---

## 🎯 القواعد الذهبية الإلزامية (Non-Negotiable Core Laws):
1. **قانون الزيرو متصفح (Zero-Browser Law):** الاعتماد 100% على الـ Pure HTTP Requests لفحص الـ Chunks والباندلز والتسجيل والشات بدون فتح أي متصفح.
2. **قانون الاستباقية الآلية:** عدم التوقف بعد كل خطوة، العمل في حلقة تنفيذية متصلة (Autonomous Loop) لإنهاء الفحص والبناء والتوثيق.
3. **قانون التوثيق وسجل الذاكرة:** إنشاء ملف `README.md` شامل في مجلد المزود وتحديث سجل القرارات `.agents/memory/CHANGELOG_DECISIONS.md`.

---

## 🔄 مسار خطوات البروتوكول (The 5-Step Pipeline):

### [Step 1/5] — كشف المعمارية والباندل (Architecture & Chunks Analysis)
```
1. سحب الصفحة الرئيسية واستخراج روابط ملفات الجافاسكريبت والـ Manifests.
2. فحص محتوى الـ Chunks لاستخراج:
   - مسارات الـ API الداخلية والخارجية (/api/, /v1/, /public/).
   - نظام المصادقة: Clerk, Supabase, Firebase, WorkOS, NextAuth, Custom JWT.
   - بوابات الحماية والكابتشا: Turnstile, hCaptcha, reCaptcha, Verisoul.
```

### [Step 2/5] — فحص الرصيد المجاني والنماذج (Quotas & Models Discovery)
```
1. البحث في كود الواجهة عن:
   - رصيد الترحيب (Welcome Bonus).
   - رصيد التجديد اليومي (Daily Drip Allowance).
   - التوكنات المجانية وشروط الدفع المسبق (Prepaid vs Free Tier).
2. استخراج قائمة النماذج المتاحة، أحجام السياق (Context Window)، ودعم الصور (Vision).
```

### [Step 3/5] — اختبار التسجيل البرمجي بالإيميلات المؤقتة (Live Tempmail Test)
```
1. تجربة استدعاء مسار التسجيل برمجياً باستخدام المزودين المحليين:
   - __دومينات مؤقته/providers/ (emailnator.py, tempmail_club.py, tempnet.py).
   - أو مزود عام (mail.tm / 1secmail) كبديل تلقائي.
2. تصنيف الموقع بدقة:
   - Pure Requests 100%: تسجيل وشات مباشر بدون متصفح.
   - Hybrid: يتطلب جلسة/كابتشا لمرة واحدة ثم يعمل بيور ريكوست.
   - Browser Only: معتمد على متصفح بالكامل.
3. حفظ بيانات الحساب التجريبي النشط والتوكن في accounts_{provider}.json.
```

### [Step 4/5] — بناء أدوات الربط والعميل (Tooling & SDK Generation)
```
إنشاء مجلد مخصص للمزود يضم:
├── 01_{provider}_chat.py          # عميل محادثة متوافق مع معيار OpenAI / Anthropic
├── 02_{provider}_auth_factory.py  # مصنع الحسابات وتوليد الـ API Keys
├── accounts_{provider}.json       # الحسابات النشطة والتوكنات
└── README.md                      # التوثيق الشامل وجدول الـ Endpoints
```

### [Step 5/5] — التوثيق وسجل الذاكرة (Master Index & Memory Logging)
```
1. تحديث جدول المقارنة العام في README.md للمشروع.
2. تسجيل النتيجة والدروس المستفادة تلقائياً في .agents/memory/CHANGELOG_DECISIONS.md.
3. إنهاء الرد بالعامية المصرية مع كتلة النقد الذاتي 🔍 نقد ذاتي.
```

---

## 💻 طريقة الاستدعاء:
```text
/00-reverse-engineer https://example-ai.com/
```
