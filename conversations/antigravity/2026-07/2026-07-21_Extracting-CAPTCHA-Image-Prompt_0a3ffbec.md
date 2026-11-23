# Extracting CAPTCHA Image Prompt

- id: `0a3ffbec-e43e-4e71-b594-90dc43434f77`
- title: Extracting CAPTCHA Image Prompt
- date: 2026-07-21 22:29:38
- workspace: .hRhRhRhRhRhR
- steps: 27
- chunks: 2
- archived: false
- summary:
  - Extracting CAPTCHA Image Prompt

## chunk -1 (steps 0–0)

### user

(empty)

### agent

(empty)

## chunk 0 (steps 0–26)

### user

@[d:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark_register.py] عاوز برومت اللي بيقوله لي موديل علشان يحل صوره
طيب سوالبقي هي صوره ولا رابط وكمان بي اني موديل؟

### agent

في ملف [genspark_register.py](file:///d:/SMS/.hRhRhRhRhRhR/..............................................................................................................شغل%20فريق/Genspark/genspark_register.py) فيه 3 برومبتات (Prompts) بيستخدموا لحل وتحديد كود الـ CAPTCHA/الصورة:

---

### 1️⃣ البرومبت الرئيسي موديلات الـ Vision (زي Groq Llama 4 Scout و Pollinations):
ده البرومبت الأساسي اللي بيتبعت مع صورة الـ CAPTCHA للموديل:

```python
_CAPTCHA_PROMPT = (
    "This image contains a CAPTCHA with distorted text characters. "
    "Read the text in the image carefully. "
    "Reply with ONLY the characters you see, nothing else. "
    "The answer should be lowercase letters and/or digits only. "
    "No spaces, no punctuation, no explanation."
)
```

---

### 2️⃣ برومبت موديلات الـ URL/Text (زي Perplexity و ERNIE):
ده البرومبت اللي بيتبعت لما يكون الموديل بياخد رابط الصورة `image_url` مباشرة:

```python
prompt = (
    f"This is a CAPTCHA image URL: {image_url}\n"
    "What text/characters do you see in this CAPTCHA image?\n"
    "Reply with ONLY the characters, no spaces, no explanation."
)
```

---

### 3️⃣ برومبت الحكم (Judge Prompt):
ده البرومبت اللي بيتبعت للموديل لو الموديلات اختلفوا في الإجابة عشان يختار أصح إجابة بينهم:

```python
judge_prompt = (
    f"CAPTCHA solvers returned these different answers: {valid}\n"
    f"Which one is most likely correct for a distorted text CAPTCHA? "
    f"Reply with ONLY the answer text, nothing else."
)
```

---

🔍 نقد ذاتي:
1. ✅ لا يوجد dead code أو متغيّرات غير مستخدمة (استفسار فقط).
2. ✅ لا يوجد خطر كسر كود (Regression Risk) لعدم إجراء أي تعديلات على الملفات.
3. ✅ تم الوصول للإجابة وتحديد البرومبتات بدقة في خطوة واحدة.
4. ✅ عدم وجود تكرار DRY.
5. ✅ تمت مراجعة الملف المعني وتحديد النصوص بالظبط.

إليك الإجابة بالتفصيل من واقع كود السكربت في [genspark_register.py](file:///d:/SMS/.hRhRhRhRhRhR/..............................................................................................................شغل%20فريق/Genspark/genspark_register.py):

---

### 1️⃣ هل هي صورة ولا رابط؟ 🖼️🔗

**هي بتتحول لـ الاثنين معاً (Data URL):**
* السيرفر بيبعت الـ CAPTCHA في الأول على هيئة **Base64** (نص كود مشفر للصورة).
* السكربت بياخد النص ده ويحوله لـ **Data URL** بصيغة JPEG:
  ```python
  image_url = f"data:image/jpeg;base64,{raw_b64}"
  ```
* الموديلات اللي بتدعم الرؤية (Vision Models) بتعامل الـ Data URL ده **كصورة حقيقية مباشرة** (`{"type": "image_url", "image_url": {"url": image_url}}`).

---

### 2️⃣ بأني موديل بيتم الحل؟ 🤖

السكربت فيه **نظام ذكي موزع (Multi-Solver Consensus)**، وبيعتمد على الموديلات التالية:

#### 🟢 الموديل الأساسي (الأسرع والأول افتراضياً):
* **Groq Llama 4 Scout** (`meta-llama/llama-4-scout-17b-16e-instruct`)
  * **السبب:** أسرع موديل رؤية (بياخد حوالي **0.7 ثانية** بس!).
  * بياخد keys من ملف `accounts_Groq.json` وبيحل الصورة فوراً.

#### 🔵 موديلات رؤية تانية (Vision Fallbacks):
* **Pollinations OpenAI / Claude** (`gen.pollinations.ai`)
* **z.ai OCR** (خدمة OCR محلية كخيار احتياطي).

#### 🔮 موديلات التقييم والحكم (Judges):
لو الموديلات اختلفوا في الإجابة، السكربت بيشغل نظام **الـ Judges** للترجيح بالأغلبية:
* **Perplexity Pool:** بيسأل **7 موديلات مختلفة بالتوازي** من Perplexity ويحصل تصويت بالأغلبية (Majority Vote).
* **Groq Judge:** بيقيم الأجوبة ويرجح الأصح.

---

🔍 نقد ذاتي:
1. ✅ لا يوجد dead code أو متغيّرات معلّقة.
2. ✅ لا يوجد خطر تكسير، إجابة توضيحية مباشرة ودقيقة بناءً على قراءة الكود.
3. ✅ تم الوصول للشرح بأقل عدد خطوات وتوضيح الـ Data URL والـ Models بالظبط.
4. ✅ عدم وجود تكرار DRY.
5. ✅ التزم بالقواعد وتنسيق الرد باللغة المصرية والـ Emojis.
