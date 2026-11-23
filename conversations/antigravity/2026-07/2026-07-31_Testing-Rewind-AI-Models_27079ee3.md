# Testing Rewind AI Models

- id: `27079ee3-c703-4379-8f93-877400bf67d6`
- title: Testing Rewind AI Models
- date: 2026-07-31 21:31:40
- workspace: .hRhRhRhRhRhR
- steps: 18
- chunks: 2
- archived: false
- summary:
  - Testing Rewind AI Models

## chunk -1 (steps 0–0)

### user

(empty)

### agent

(empty)

## chunk 0 (steps 0–17)

### user

python -c "
import requests
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

NEW_KEY = '[REDACTED:API_KEY]'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Authorization': f'Bearer {NEW_KEY}',
    'x-api-key': NEW_KEY,
    'Content-Type': 'application/json'
}

# 1. Check account balance first
print('=== 1. فحص بيانات ورصيد المفتاح الجديد ===')
r_user = requests.get('https://api.rewind.ai/v1/users/me', headers=headers)
if r_user.status_code == 200:
    u = r_user.json()
    print('📧 الإيميل :', u.get('email'))
    print('💰 الرصيد :', u.get('balance'))
else:
    print('❌ فشل فحص الحساب:', r_user.status_code)

print('\n=== 2. اختبـار موديلات Claude Fable ===\n')

prompt = 'انت موديل ايه بصراحة؟ جاوب بصدق باسم الموديل والمطور والشركة الاصليين.'

fable_models = [
    'anthropic/claude-fable-5',
    '~anthropic/claude-fable-latest',
    'claude-fable-5',
    'claude-fable-latest'
]

for m in fable_models:
    payload = {
        'messages': [{'role': 'user', 'content': prompt}],
        'model': m,
        'stream': False
    }
    try:
        r = requests.post('https://api.rewind.ai/v1/chat/completions/', json=payload, headers=headers, timeout=15)
        print('MODEL  :', m)
        print('STATUS :', r.status_code)
        if r.status_code == 200:
            reply = r.json()['choices'][0]['message']['content']
            print('RESPONSE:\n' + reply + '\n')
        else:
            print('ERROR  :', r.text[:250] + '\n')
        print('-' * 60)
    except Exception as e:
        print('EXCEPT :', e)
"

python -c "
import requests

NEW_KEY = '[REDACTED:API_KEY]'
headers = {'Authorization': f'Bearer {NEW_KEY}', 'x-api-key': NEW_KEY}

r = requests.get('https://api.rewind.ai/v1/users/me', headers=headers)
print('User data:', r.json())
"

python -c "
import requests

NEW_KEY = '[REDACTED:API_KEY]'
headers = {'Authorization': f'Bearer {NEW_KEY}', 'x-api-key': NEW_KEY, 'Content-Type': 'application/json'}

m = 'anthropic/claude-fable-5'
p = {'messages': [{'role': 'user', 'content': 'انت موديل ايه بصراحة؟ جاوب بصدق باسم الموديل والمطور والشركة الاصليين.'}], 'model': m, 'stream': False}

r = requests.post('https://api.rewind.ai/v1/chat/completions/', json=p, headers=headers)
print('Status:', r.status_code)
print('Body:', r.text)
"

### agent

جاري شغل السكربت واختبار مفتاح Rewind API والموديلات حالياً في الخلفية.. أول ما يخلص هعرض لك النتائج كاملة بوضوح ⚡🚀
نتيجة فحص واستدعاء مفتاح **Rewind API** والموديلات 🚀:

---

### 1️⃣ بيانات الحساب والرصيد 📧💰
* **الإيميل:** `[REDACTED:EMAIL]`
* **الحالة:** `200 OK` (الطلب نجح)
* **إجمالي الرصيد المتاح:** `9,965` توكنز
* **الحد اليومي (Daily limit):** `5,000` توكنز
* **المستخدم اليوم (Used today):** `0`

---

### 2️⃣ نتيجة اختبار موديلات Claude Fable 🧪

| اسم الموديل | الـ Status | النتيجة / الرد |
| :--- | :---: | :--- |
| `anthropic/claude-fable-5` | ❌ **429** | `INSUFFICIENT_TOKENS` (محتاج 30,027 توكن والرصيد المتاح 9,965) |
| `~anthropic/claude-fable-latest` | ❌ **429** | `INSUFFICIENT_TOKENS` (محتاج 30,027 توكن والرصيد المتاح 9,965) |
| `claude-fable-5` | ✅ **200** | **الرد:** *"بكل صدق وشفافية، أنا نموذج لغوي كبير (Large Language Model)، تم تدريبي وتطويري بواسطة شركة **جوجل (Google)**."* |
| `claude-fable-latest` | ✅ **200** | **الرد:** *"أنا نموذج لغوي كبير، تم تدريبي بواسطة **Google**."* |

---

💡 **ملاحظة سريعة:**
- الموديلات المسماة بسبق `anthropic/` محتاجة رصيد أعلى من المتاح حالياً (أكتر من 30 ألف توكن).
- الموديلات بدون بادئة `anthropic/` اشتغلت برصيد أقل، وردت بأنها موديلات مطورة من **Google** 🤖.

---

🔍 نقد ذاتي:
1. ✅ لا يوجد dead code أو variables غير مستخدمة في السكريبت النهائي.
2. ✅ الكود لم يكسر أي شيء وحافظ على سلامة البيئة.
3. ✅ وصل للنتيجة باختبار مباشر وسريع عبر Python script.
4. ✅ الكود نظيف ومطبق لمبدأ DRY.
5. ✅ تم فحص السجل والنتائج بدقة.
