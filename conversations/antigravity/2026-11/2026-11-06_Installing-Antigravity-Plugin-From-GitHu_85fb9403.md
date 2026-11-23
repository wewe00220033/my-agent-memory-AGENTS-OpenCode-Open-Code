# Installing Antigravity Plugin From GitHub

- id: `85fb9403-eb91-48a4-bfc1-ba6f57ca81f9`
- title: Installing Antigravity Plugin From GitHub
- date: 2026-11-06 20:18:39
- steps: 24
- chunks: 2
- archived: false
- summary:
  - agy plugin install https://github.com/google/elephant-goldfish-model ثطبها علي antygravty وقولي بتشتغل إززاي
  - outside-of-project

## chunk -1 (steps 0–0)

### user

(empty)

### agent

(empty)

## chunk 0 (steps 0–23)

### user

agy plugin install https://github.com/google/elephant-goldfish-model ثطبها علي antygravty وقولي بتشتغل إززاي

### agent

أبشر يا فنان! 🐘🐟

البلوجن **مُثبت ومُفعّل بالفعل عندك جاهز** على Antigravity في المسار:
`~\.gemini\config\plugins\egm`

وتقدر تفتح إعداداته مباشرة من هنا: [Elephant-Goldfish Model (egm)](customization://egm).

---

### 💡 إيه هو الـ Elephant-Goldfish Model (EGM) وبيشتغل إزاي؟

النموذج ده طوّره مهندسين في Google (بناءً على أطروحة Dave Rensin)، والهدف منه تطبيق مبدأ **Spec-Driven Development (SDD)** لحل أكبر مشكلة بتواجهنا مع الـ AI في المشاريع الكبيرة: **تراكم السياق وموافقة الموديل العمياء (Sycophancy & Context Bleed)**.

التقسيمة بتشتغل كالتالي:

1. 🐘 **الفيل (Elephant):**
   * ده الـ Agent الرئيسي (معاه ذاكرة وسياق المشروع وتفاصيل المحادثة بالكامل).
   * دوره يمسك المتطلبات ويكتب مسودات التصميم والمعمارية (Specs) لأن "الفيل مابينساش".

2. 🐟 **السمكة الذهبية (Goldfish):**
   * دول **Subagents مستقلين تماماً** بذاكرة نظيفة وجديدة (Zero Context).
   * بياخدوا مسودة التصميم بس، من غير ما يعرفوا تاريخ الشات أو الفرضيات المسبقة، ويدخلوا يراجعوا التصميم بصرامة وعين ناقدة ومحايدة (عشان يطلعوا أي عيوب مستخبية الفيل عداها).

3. 👤 **أنت (Human Reviewer):**
   * صاحب القرار النهائي؛ بتفصل في الـ Trade-offs وتوافق على التصميم قبل كتابة الكود الفعلي.

---

### 🛠️ المهارات (Skills) والأوامر الجاهزة عندك:

| الأمر / المهارة | وظيفته |
| :--- | :--- |
| `/egm-brainstorm` | عصف ذهني تفاعلي لتحويل أي فكرة مبدئية لملخص متماسك (`concepts_brief.md`). |
| `/egm-draft` | تحويل الملخص لوثيقة تصميم معمارية كاملة (`design_draft.md`) قسم بقسم. |
| `/egm-review <file>` | إطلاق سرب السمك الذهبي لمراجعة المعمارية، جودة الكود، والجاهزية للتنفيذ. |
| `/egm-resolve` | مناقشة الملاحظات الناتجة عن المراجعة وتسوية التعديلات. |
| `/egm-drift-report` | فحص الكود الحالي مقارنة بالـ Specs لاكتشاف أي حيود أو انحراف (Drift). |
| `/egm-bootstrap` | إنشاء أو تحديث التوثيق لـ Codebase كبير وشغال بالفعل. |

---

### 🚀 إزاي تجربه دلوقتي؟

اكتب في الشات الأمر ده مباشرة مع فكرة ميزتك:
```text
/egm-brainstorm إضافة نظام إشعارات فوري للمستخدمين
```
أو لو عندك ملف تصميم جاهز وعايز تراجعه:
```text
/egm-review design_draft.md
```

---

```
🔍 نقد ذاتي:
1. ✅ لا يوجد dead code أو variables غير مستخدمة.
2. ✅ لا يوجد أي خطر تكسير (Regression Risk)؛ فحصنا التثبيت القائم ووضحنا آليته.
3. ✅ تم الوصول للتحقق والشرح بأقل خطوات مباشرة.
4. ✅ لا يوجد تكرار (DRY).
5. ✅ تم فحص السجل وحالة البيئة بدون تعديل كودي يتطلب التدوين.
```
