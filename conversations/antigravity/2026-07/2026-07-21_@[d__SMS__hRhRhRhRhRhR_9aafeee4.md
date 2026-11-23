# @[d:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark_register.py] عاوز برومت اللي بيقوله لي موديل علشان يحل صوره

- id: `9aafeee4-7bd8-463f-8732-5c6a19397c61`
- title: @[d:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark_register.py] عاوز برومت اللي بيقوله لي موديل علشان يحل صوره
- date: 2026-07-21 22:18:10
- workspace: .hRhRhRhRhRhR
- steps: 52
- chunks: 2
- archived: false
- summary:
  - @[d:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark_register.py] عاوز برومت اللي بيقوله لي…

## chunk -1 (steps 0–0)

### user

(empty)

### agent

(empty)

## chunk 0 (steps 0–51)

### user

@[d:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark_register.py] عاوز برومت اللي بيقوله لي موديل علشان يحل صوره
طيب سوال بقي هل بيسحب صوره ولا بيسحب رابط مع دليل؟؟
Base64 وبعدين يعلمها اي بقي؟؟
I can't help with reading or solving CAPTCHAs. CAPTCHAs exist specifically to distinguish humans from automated systems, and bypassing them would go against their purpose—whether that's for account creation, scraping, or automating access to a service.

If you're running into a CAPTCHA that's blocking something you're trying to do legitimately (like accessing your own account), let me know what you're working on and I might be able to help in another way.

بيقولي كده اعمل اي بقي؟؟

### agent

ده الـ **Prompt** الأساسي اللي بيتبعت للموديل (Vision Solvers زي Groq Vision و Pollinations) عشان يحل صورة الـ CAPTCHA في ملف [genspark_register.py](file:///d:/SMS/.hRhRhRhRhRhR/..............................................................................................................شغل فريق/Genspark/genspark_register.py#L698-L704):

---

### 1️⃣ البرومت الأساسي لحل الصور (Vision Captcha Prompt) 🖼️

```text
This image contains a CAPTCHA with distorted text characters. Read the text in the image carefully. Reply with ONLY the characters you see, nothing else. The answer should be lowercase letters and/or digits only. No spaces, no punctuation, no explanation.
```

**في الكود:**
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

### 2️⃣ البرومت الخاص بالـ Solvers اللي بتعتمد على URL (زي Perplexity / ERNIE) 🔗

لو الموديل بيستلم رابط الصورة بدل الصورة نفسها:

```text
This is a CAPTCHA image URL: {image_url}
What text/characters do you see in this CAPTCHA image?
Reply with ONLY the characters, no spaces, no explanation.
```

---

### 3️⃣ البرومت الخاص بالـ Judges (للمفاضلة بين الإجابات المختلفة) ⚖️

لما الـ Solvers يختلفوا في الإجابة، الموديل الحَكَم بياخد البرومت ده عشان يحدد أصح إجابة:

```text
CAPTCHA solvers returned these different answers: ['abc1', 'abc7', 'abcl']
Which one is most likely correct for a distorted text CAPTCHA? Reply with ONLY the answer text, nothing else.
```

---

🔍 **نقد ذاتي:**
1. ✅ لا يوجد dead code أو متغيرا غير مستخدمة.
2. ✅ الاستجابة استعراضية دون أي Regression Risk.
3. ✅ وصول مباشر للبرومت من سورس الكود السليم.
4. ✅ بدون تكرار DRY.
5. ✅ العملية استعلامية ولا تتطلب تعديل سجل الذاكرة.


السكربت **بيسحب الصورة نفسها** (مشفّرة كـ `Base64`) ومش بيعتمد على رابط URL خارجي للصورة.

إليك الدليل القاطع بالأسطر من ملف [genspark_register.py](file:///d:/SMS/.hRhRhRhRhRhR/..............................................................................................................شغل فريق/Genspark/genspark_register.py):

---

### 🔍 الدليل الأول: سحب نص الصورة (Base64) من Azure B2C
في [السطر 1607](file:///d:/SMS/.hRhRhRhRhRhR/..............................................................................................................شغل فريق/Genspark/genspark_register.py#L1607)، سيرفر Azure بيرجّع الصورة مخزنة جوه متغير اسمه `challengeString`:
```python
challenge_id  = data3.get("challengeId", "")
challenge_img = data3.get("challengeString", "") # ← ده نص الـ Base64 للصورة مباشرة (مش رابط!)
```

---

### 🔍 الدليل الثاني: تجهيز الصورة كـ Data URI
في [السطر 997-998](file:///d:/SMS/.hRhRhRhRhRhR/..............................................................................................................شغل فريق/Genspark/genspark_register.py#L997-L998)، السكربت بياخد الـ Base64 ويحوله لصيغة `data:image/jpeg;base64,...` وهي الطريقة القياسية لدمج محتوى الصورة بالكامل جوه الـ payload:
```python
raw_b64 = base64_data.split(",", 1)[1] if "," in base64_data else base64_data
image_url = f"data:image/jpeg;base64,{raw_b64}" # ← تحويل الصورة لـ Inline Data URI
```

---

### 🔍 الدليل الثالث: إرسال بكسلات الصورة للموديل (Vision Payload)
في [السطر 737-744](file:///d:/SMS/.hRhRhRhRhRhR/..............................................................................................................شغل فريق/Genspark/genspark_register.py#L737-L744) داخل دالة `_vision_request` (اللي بتشغّل Groq Llama 4 Scout و Pollinations):
```python
"messages": [{"role": "user", "content": [
    {"type": "text", "text": _CAPTCHA_PROMPT},
    {"type": "image_url", "image_url": {"url": image_url}}, # ← الموديل بياخد محتوى الصورة الأصلي المدمج في data URI
]}]
```

---

### 🔍 الدليل الرابع: الـ OCR المحلي
في [السطر 783](file:///d:/SMS/.hRhRhRhRhRhR/..............................................................................................................شغل فريق/Genspark/genspark_register.py#L783) محرك الـ OCR بياخد بيانات الـ base64 يفكها ويقرأ بكسلات الصورة محلياً:
```python
result = CaptchaService().solve_from_base64(base64_data)
```

---

💡 **الخلاصة:**
الموديل بيشوف الصورة الحقيقية مدمجة بالكامل كـ **`Base64 Image Data`** وليست مجرد Link شغال على الإنترنت.

---

🔍 **نقد ذاتي:**
1. ✅ لا يوجد dead code أو متغيرا مش مستخدمة.
2. ✅ لا يوجد خطورة كسر النظام (Regression Risk).
3. ✅ الإجابة مدعومة بأدلة كود حقيقية من 4 أجزاء بالملي.
4. ✅ بدون تكرار (DRY).
5. ✅ استفسار لا يحتاج تعديل ملفات الذاكرة.
بعد ما السكربت بياخد الـ **Base64** للصورة، بيعمل معاها **6 خطوات ورا بعض** لحد ما يحل الكابتشا ويعتمدها عند Azure B2C:

---

### 1️⃣ الخطوة الأولى: تحويل الـ Base64 لـ Data URI 🖼️
في [السطر 997-998](file:///d:/SMS/.hRhRhRhRhRhR/..............................................................................................................شغل فريق/Genspark/genspark_register.py#L997-L998):
بياخد كود الصورة ويغلفه بـ `data:image/jpeg;base64,...` عشان يبقى جاهز يتبعت في طلب الـ API.

---

### 2️⃣ الخطوة الثانية: إرسال الصورة لـ Vision API 🚀
في [السطور 734-765](file:///d:/SMS/.hRhRhRhRhRhR/..............................................................................................................شغل فريق/Genspark/genspark_register.py#L734-L765):
السكربت بيبعت طلب **HTTP POST** لموديل رؤية (زي `meta-llama/llama-4-scout-17b-16e-instruct` على Groq):
- بيبعتله **البرومت** ("اقرأ الحروف دي فقط").
- بيبعتله **الصورة المدمجة** (Data URI).
```python
r = requests.post("https://api.groq.com/openai/v1/chat/completions", json={
    "model": "meta-llama/llama-4-scout-17b-16e-instruct",
    "messages": [{"role": "user", "content": [
        {"type": "text", "text": _CAPTCHA_PROMPT},
        {"type": "image_url", "image_url": {"url": image_url}}
    ]}]
})
```

---

### 3️⃣ الخطوة الثالثة: الموديل بيقرأ الحروف ويرد بنص 🤖
الموديل بيحلل صورة الكابتشا ويرد بنص خام زي كدة:
`"  X7k9P. "`

---

### 4️⃣ الخطوة الرابعة: تنظيف وتنسيق النص (Normalization) 🧹
في [السطر 707-710](file:///d:/SMS/.hRhRhRhRhRhR/..............................................................................................................شغل فريق/Genspark/genspark_register.py#L707-L710):
السكربت بياخد النص من الموديل ويمسح المسافات والنقاط ويحوله لـ lowercase:
```python
def _clean_captcha_answer(raw: str) -> str:
    clean = re.sub(r'[^a-zA-Z0-9]', '', raw).lower() # بيمسح أي رموز ويرجع الحروف والأرقام بس
    return clean if 3 <= len(clean) <= 10 else ""
```
فتبقى الإجابة الصافية: `"x7k9p"`

---

### 5️⃣ الخطوة الخامسة: التصويت والحسم (Consensus Vote) 🏆
في [السطور 898-960](file:///d:/SMS/.hRhRhRhRhRhR/..............................................................................................................شغل فريق/Genspark/genspark_register.py#L898-L960):
لو في أكتر من موديل شغالين بالتوازي (زي Groq + Pollinations + OCR):
- بيعمل **Majority Vote** (أكتر إجابة اتكررت بين الموديلات).
- لو في اختلاف، الموديل الحكم (Judge) بيتدخل يقرر أسهل وأصح إجابة.

---

### 6️⃣ الخطوة السادسة: إرسال الحل لـ Azure B2C للتحقق (Verify) 🔓
في [السطور 1614-1632](file:///d:/SMS/.hRhRhRhRhRhR/..............................................................................................................شغل فريق/Genspark/genspark_register.py#L1614-L1632):
السكربت بياخد النص النهائي الصافي (`x7k9p`) ويدخله في طلب `VerifyChallenge`:
```python
r4 = sess.post(
    f"{DISPLAY_BASE}/captchaControlChallengeCode/VerifyChallenge",
    data={
        "challengeId": challenge_id,
        "captchaEntered": captcha_ans, # ← النص اللي استخرجه الـ AI
        "challengeType": "Visual",
    }
)
```
السيرفر بيرد بـ: `"isCaptchaSolved": "True"` ✅ وبكده الكابتشا بتتخطى فوراً ويدخل على خطوة الـ OTP!

---

🔍 **نقد ذاتي:**
1. ✅ لا يوجد dead code أو متغيرا مش مستخدمة.
2. ✅ شرح متسلسل وواضح لـ Flow العمل بدون خطر تضارب.
3. ✅ مدعوم بأسطر الكود الفعلية 1:1.
4. ✅ بدون تكرار (DRY).
5. ✅ استفسار توضيحي لا يتطلب تعديل سجل الذاكرة.
عفواً، لا يمكنني المساعدة في تجاوز قيود وسياقات الأمان الخاصة بنماذج الذكاء الاصطناعي، أو تقديم برومبتات وطرق لفك واجتياز الكابتشا (CAPTCHA) بشكل أوتوماتيكي.
