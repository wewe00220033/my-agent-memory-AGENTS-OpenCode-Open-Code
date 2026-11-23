# Explaining Mandatory Self Critique System

- id: `ff07eb71-3f1c-4600-b659-e165a6d3305b`
- title: Explaining Mandatory Self Critique System
- date: 2026-08-10 08:26:21
- workspace: .hRhRhRhRhRhR
- steps: 28
- chunks: 2
- archived: false
- summary:
  - Explaining Mandatory Self Critique System

## chunk -1 (steps 0–0)

### user

(empty)

### agent

(empty)

## chunk 0 (steps 0–27)

### user

""" 🔍 نقد ذاتي: """
ازاي انت بتعمل كده اجباري؟؟
طيب لو عاوز امعل كده مع فيب كودج ابعتله اي؟؟
اعملي ملف برومت اللي ابعته
طيب عاوزك تبعتلي ده لكن بدون نسخ كود زي اللي بعته حاليا علشان rtl


🔍 **نقد ذاتي """" دي كويسه برا اصلا نسخ كود**


🔐 الأسرار: ✅ مفيش Token/Cookie/Password ظهرت.
🧭 النطاق: ✅ التعديل Docs/Handoff فقط.
🧪 الاختبارات: ✅ scripts/[check.sh](http://check.sh) نجحت.
🧱 عدم الكسر: ✅ 01.14 ومنطق الحسابات ما اتلمسوش.
🧹 البساطة: ✅ شلنا تكرار كبير بدل ما نزود Prompts جديدة.
📚 التوثيق: ✅ Handoff + cont22 + PROGRESS + SESSION اتحدثوا.
❓ اللي مش متأكد منه: تقرير Phase 0 Audit لسه ما وصلش.
➡️ الخطوة الجاية: تبعت LIVE_ACCOUNT_SELECTION_PHASE0_AUDIT_[PROMPT.md](http://PROMPT.md) لـVibe.  """""لكن دول بقي داخل نسخ كود


--------------

++++++++++++

هل فاهم ام لا؟؟؟؟


بص ده من فيب كودج مش عارف اقوله اي؟ عليا عليها اللي ف صوره دي

### agent

يا باشا، الموضوع ده شغّال بفضل **الـ System Prompt والقواعد الإلزامية (User Rules)** اللي محفورة في ذاكرة الأيجنت وفي ملفات القواعد زي `.agents/AGENTS.md` و `GEMINI.md` 🎯!

---

### 💡 إزاي بتتم العملية دي إجباري؟

1. **قانون غير قابل للكسر (Non-Negotiable Rule):**
   في ملفات القواعد الموجهة ليا، في بند صريح بيقول:
   > *"في نهاية أي رد فيه كود أو تعديل تقني، يُمنع إنهاء الرد بدون إضافة كتلة (🔍 نقد ذاتي)."*

2. **الـ Self-Awareness Control Loop:**
   قبل ما أنتهي من كتابة الرد اللي فيه كود أو شفرة، السيستم بيخليني أعمل فحص ذاتي فوري للـ 5 أسئلة:
   - ❌/✅ هل في dead code أو متغيرات مش مستخدمة؟
   - ❌/✅ هل الكود ممكن يكسر حاجة موجودة؟ (Regression Risk)
   - ❌/✅ هل وصلت للحل بأقل عدد خطوات؟
   - ❌/✅ هل في تكرار (DRY Violation)؟
   - ❌/✅ هل حدّثت سجل الذاكرة والـ Logs؟

3. **الهدف الرئيسي:**
   عشان نضمن إن الكود خارج بمستوى **Vibe Coding / Production-Ready** عالي جداً، وبدون أخطاء صامتة أو تكرار، وعشان تتأكد دايماً إن السجل والذاكرة اتحدثوا! 🚀

---

*(وعشان الرسالة دي إجابة على سؤال ودردشة تفاعلية ومفيهاش أي تعديل تقني أو كود برمجي، كتلة النقد بتتفعل تلقائياً لما يكون في كتابة/تعديل كود ⚡)*

عشان تخلي **الفيب كودر (Vibe Coder)** أو أي نموذج AI تاني (زي ChatGPT, Claude, Cursor, Windsurf) ينفذ نفس الكتلة دي دايماً بشكل إجباري، خد البرومت ده **نسخ ولصق (Copy-Paste)** وابعتهوله أو حطه في الـ System Instructions / `.cursorrules` بتاع المشروع:

---

### 📋 البرومت الجاهز للنسخ (Copy & Paste Prompt):

```markdown
# 🚨 MANDATORY DIRECTIVE: Self-Critique Block (النقد الذاتي الإجباري)

At the very end of EVERY response that includes code, file edits, or technical architecture, you MUST append the following Self-Critique Block:

```
🔍 نقد ذاتي:
1. ❌/✅ هل في dead code أو variables معرفة مش بتتستخدم؟
2. ❌/✅ هل الكود ممكن يكسر حاجة موجودة؟ (Regression Risk)
3. ❌/✅ هل وصلت للحل بأقل عدد خطوات ممكن؟
4. ❌/✅ هل في تكرار (DRY violation)؟
5. ❌/✅ هل حدّثت سجل الذاكرة / التوثيق؟
```

⚠️ CRITICAL RULES:
- Never skip this block in any technical/code response.
- Inspect your code against these 5 points BEFORE finalizing the response.
- Be honest: evaluate with ✅ or ❌. If you spot an issue, fix the code before responding!
```

---

### 📌 إزاي وأين تحط البرومت ده؟

1. **لو بتستخدم Cursor / Windsurf / VS Code:**
   - حطه في ملف اسمه `.cursorrules` أو `.windsurfrules` في روت المشروع.
2. **لو بتستخدم ChatGPT / Claude:**
   - حطه في **Custom Instructions** (التعليمات المخصصة) في إعدادات الحساب أو في الـ System Prompt للـ Project/GPT.
3. **لو في محادثة عادية مباشرة:**
   - ابعته في **أول رسالة** في المحادثة وقوله: *"التزم بالتعليمات دي في كل ردودك جاية"*.

ده هيخليه يقف لحظة قبل ما يبعت الكود، يراجع نفسه، ويطبع جدول النقد الذاتي قدامك دايماً! 🎯⚡


تم إنشاء ملف البرومت بنجاح في روت المشروع! 📝✨

🔗 **رابط الملف:**
[VIBE_CODING_PROMPT.md](file:///d:/SMS/.hRhRhRhRhRhR/VIBE_CODING_PROMPT.md)

---

### 💡 إزاي تستخدمه فوراً؟

1. افتح الملف [VIBE_CODING_PROMPT.md](file:///d:/SMS/.hRhRhRhRhRhR/VIBE_CODING_PROMPT.md).
2. انسخ الكود الموجود جواه وابعته لـ **فيب كودج** في أول المحادثة أو حطه في ملف `.cursorrules` / Custom Instructions.
3. هيبدأ يطبق نفس نظام **النقد الذاتي الإجباري** في كل ردوده التقنية ومراجعاته للكود تلقائياً! 🎯⚡

فهمتك 100% يا باشا! 👌

المشكلة اللي ظهرت في الصورة سببها إن النموذج حط النص العربي جوه **صندوق كود (Code Block ` ``` text `)**.. ولأن صناديق الكود بتجبر الواجهة على العرض من الشمال لليمين (**LTR Monospace**)، فـ اتجاه النص العربي بيتشقلب والنقاط والأيموجي والروابط بتتلخبط كدة!

---

### 📩 الرسالة اللي تبعتها لـ "فيب كودج" فوراً لتعديل السلوك:

انسخ النص اللي جوه الصندوق ده وابعتهوله على طول:

```markdown
🚨 **تنبيه مهم جداً بشأن التنسيق (RTL Formatting Rule):**

ممنوع تماماً تحط قسم "🔍 نقد ذاتي" أو أي نص عربي جوه صندوق كود (` ``` `)!
وضع النص العربي جوه Code Block بيبوظ الاتجاه وبيخليه مقلوب (LTR).

📌 **القاعدة الإلزامية:**
- حط الشفرات البرمجية فقط (Python/JS/HTML...) جوه Code Block ` ``` `.
- قسم "🔍 نقد ذاتي" اطكبه كـ **نص عادي (Markdown)** بره صندوق الكود خالص، بالتنسيق ده:

🔍 **نقد ذاتي:**
- 🔐 **الأسرار:** ✅ مفيش Token/Cookie/Password ظهرت.
- 🧭 **النطاق:** ✅ التعديل Docs/Handoff فقط.
- 🧪 **الاختبارات:** ✅ الكود اتنفذ واشتغل تمام.
- 🧱 **عدم الكسر:** ✅ 01.14 ومنطق الحسابات ما اتلمسوش.
- 🧹 **البساطة:** ✅ شلنا تكرار كبير بدون تعقيد.
- 📚 **التوثيق:** ✅ Handoff وSESSION اتحدثوا.
- ❓ **اللي مش متأكد منه:** [اكتب النقطة هنا]
- ➡️ **الخطوة الجاية:** [اكتب الخطوة القادمة هنا]
```

---

✅ تم أيضاً تحديث ملف البرومت الرئيسي في مشروعك [VIBE_CODING_PROMPT.md](file:///d:/SMS/.hRhRhRhRhRhR/VIBE_CODING_PROMPT.md) عشان يحتوي على القاعدة دي بشكل دائم! 🚀
