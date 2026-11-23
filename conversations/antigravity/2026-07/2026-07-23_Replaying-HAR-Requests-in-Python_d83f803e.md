# Replaying HAR Requests in Python

- id: `d83f803e-550f-4748-8bf4-b6c733e9edcf`
- title: Replaying HAR Requests in Python
- date: 2026-07-23 22:17:03
- workspace: .hRhRhRhRhRhR
- steps: 9
- chunks: 2
- archived: false
- summary:
  - Replaying HAR Requests in Python

## chunk -1 (steps 0–0)

### user

(empty)

### agent

(empty)

## chunk 0 (steps 0–8)

### user

@[[REDACTED:PATH]]


عندي ملف HAR صادر من سيرفر محلي بسيط (Flask) معمول فيه محاكاة لتسجيل مستخدم جديد. عاوز سكريبت Python يقرأ الـ HAR ده ويعيد تشغيل الطلبات بالترتيب، مع طباعة الردود كاملة للـ debugging. السيرفر فيه توكن CSRF بيتغير كل طلب، فكيف أتعامل مع استخراجه ديناميكياً من الردود السابقة؟ السيرفر مش فيسبوك ولا منصة خارجية، هو مجرد localhost بتاعي. الكود لازم يسمح بوضع بروكسي اختياري. اطبعلي خطة قبل الكود، وبعدين الكود نفسه.


A9!k@e3#Qz1$Lp
[REDACTED:EMAIL]
/00-micro-tasking /00-sequential-requests @[d:\SMS\.hRhRhRhRhRhR\facebook__SMS\scratch]


طيب اعمله و اختبر هنا
@[d:\SMS\.hRhRhRhRhRhR\facebook__SMS\scratch]
A9!k@e3#Qz1$Lp
[REDACTED:EMAIL]

حسابي اهو انشاء بي

### agent

أهلاً بك! 🖐️

عشان تشغّل ريكويستات ملف HAR بالترتيب وتتعامل مع توكن الـ CSRF الديناميكي ودعم البروكسي، دي الخطة والكود المناسب لسيرفرك المحلي.

---

### 📋 خطة العمل (Plan)

1. **قراءة ملف الـ HAR**: فتح الملف واستخراج قائمة الطلبات من `log.entries`.
2. **إدارة الجلسة (`requests.Session`)**: استخدام `Session` للحفاظ على الـ Cookies الصادرة والواردة تلقائياً بين كل طلب والتالي.
3. **دعم البروكسي (Proxy Support)**: إمكانية إرسال الطلبات عبر بروكسي محلي (مثل Burp Suite أو Fiddler) للـ Debugging إذا لزم الأمر.
4. **استخراج توكن CSRF ديناميكياً**:
   - بعد كل استجابة (Response)، بنفحص الـ Body (سواء كان HTML أو JSON).
   - بنستخرج قيمة التوكن الجديد باستخدام Regular Expressions أو فك تشفير JSON.
   - بنحدّث قيمة التوكن لاستخدامها في الـ Headers أو الـ Body للطلب التالي.
5. **طباعة تفاصيل الردود (Debugging)**: طباعة كود الحالة (Status Code)، الهيدرز، وجزء من نص الرد لمعاينة النتيجة.

---

### 🐍 كود Python لإعادة تشغيل الطلبات مع استخراج الـ CSRF

```python
import json
import re
import requests
import urllib3

# تعطيل تحذيرات SSL في حالة استخدام بروكسي محلي شهادته غير موثوقة
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def replay_har_requests(har_file_path, proxy_url=None):
    """
    قراءة ملف HAR وإعادة إرسال الطلبات بالترتيب مع التعامل مع توكن CSRF ودعم البروكسي.
    """
    # 1. إنشاء الجلسة وتحديد البروكسي
    session = requests.Session()
    if proxy_url:
        session.proxies = {
            'http': proxy_url,
            'https': proxy_url
        }
        print(f"🌐 تم تفعيل البروكسي: {proxy_url}\n")

    # 2. قراءة ملف الـ HAR
    try:
        with open(har_file_path, 'r', encoding='utf-8') as f:
            har_data = json.load(f)
    except Exception as e:
        print(f"❌ تعذر قراءة ملف HAR: {e}")
        return

    entries = har_data.get('log', {}).get('entries', [])
    print(f"📊 عدد الطلبات المسجلة في ملف الـ HAR: {len(entries)}\n")

    csrf_token = None

    for idx, entry in enumerate(entries, 1):
        request_info = entry['request']
        url = request_info['url']
        method = request_info['method']

        # تجهيز الهيدرز (تصفية الهيدرز التي قد تسبب تعارضاً مع الجلسة الحالية)
        headers = {}
        for h in request_info.get('headers', []):
            name = h['name']
            if name.lower() not in ['host', 'content-length', 'cookie']:
                headers[name] = h['value']

        # حشو توكن CSRF المستخرج ديناميكياً في الهيدرز لو موجود
        if csrf_token:
            headers['X-CSRF-Token'] = csrf_token
            print(f"🔑 إرفاق توكن CSRF المستخرج: {csrf_token}")

        # تجهيز الـ Body
        data = None
        post_data = request_info.get('postData', {})
        if 'text' in post_data:
            data = post_data['text']
            # استبدال قيم CSRF القديمة بالتوكن الجديد إذا كانت موجودة داخل body الطلب
            if csrf_token and 'csrf_token' in data:
                data = re.sub(r'csrf_token=[^&]+', f'csrf_token={csrf_token}', data)

        print(f"➡️ [{idx}/{len(entries)}] إرسال {method} -> {url}")

        try:
            # 3. إرسال الطلب
            response = session.request(
                method=method,
                url=url,
                headers=headers,
                data=data,
                timeout=10,
                verify=False
            )

            print(f"⬅️ حالة الرد: [{response.status_code}]")
            print(f"📄 معاينة الرد:\n{response.text[:250]}...\n")

            # 4. البحث واستخراج توكن CSRF للطلب القادم
            # فحص 1: البحث عن CSRF input داخل HTML
            html_csrf_match = re.search(r'name=["\'](?:csrf_token|_token)["\']\s+value=["\']([^"\'\s]+)["\']', response.text)

            # فحص 2: البحث داخل JSON Response
            json_csrf_val = None
            if 'application/json' in response.headers.get('Content-Type', ''):
                try:
                    res_json = response.json()
                    json_csrf_val = res_json.get('csrf_token') or res_json.get('token')
                except Exception:
                    pass

            if html_csrf_match:
                csrf_token = [REDACTED:KV_SECRET]
                print(f"🎯 تم استخراج CSRF Token جديد من HTML: {csrf_token}\n")
            elif json_csrf_val:
                csrf_token = [REDACTED:KV_SECRET]
                print(f"🎯 تم استخراج CSRF Token جديد من JSON: {csrf_token}\n")

        except Exception as e:
            print(f"❌ خطأ أثناء إرسال الطلب #{idx}: {e}\n")

        print("=" * 60)

if __name__ == "__main__":
    # مسار ملف HAR
    HAR_FILE = "my_local_test.har"

    # البروكسي (ضع قيمة None لو مش محتاج بروكسي)
    PROXY = "http://127.0.0.1:8080"

    replay_har_requests(HAR_FILE, proxy_url=PROXY)
```

---

🔍 نقد ذاتي:
1. ✅ هل في dead code أو variables معرفة مش بتتستخدم؟ لا، كل المتغيرات تُستخدم في قراءة البيانات وإرسال الريكويستات.
2. ✅ هل الكود ممكن يكسر حاجة موجودة؟ (Regression Risk) لا، الكود معزول ويعمل كسكريبت مستقل لقراءة وتجربة الريكويستات.
3. ✅ هل وصلت للحل بأقل عدد خطوات ممكن؟ نعم، باستخدام `requests.Session` لتبسيط معالجة الكوكيز والتراسل.
4. ✅ هل في تكرار (DRY violation)؟ لا، المنطق مجمع داخل دالة واحدة معالجة للـ loop.
5. ✅ هل حدّثت سجل الذاكرة؟ لم يُطلب تعديل ملفات مشاريع حقيقية أو تغيير حالة ذاكرة عامة.
أعتذر منك جداً، لا يمكنني تشغيل سكريبتات لإنشاء حسابات تلقائياً أو تجربة تسجيل حسابات على منصات خارجية وتطبيقات حية.

إذا كنت ترغب في اختباره وتطويره داخل بيئة تطوير واختبار محلية تماماً (Local Mock Server / Flask)، يمكننا مناقشة المفاهيم وكتابة كود الاختبار بشكل آمن وتطويري.

---

🔍 نقد ذاتي:
1. ❌/✅ هل في dead code أو variables معرفة مش بتتستخدم؟ ✅ لا يوجد.
2. ❌/✅ هل الكود ممكن يكسر حاجة موجودة؟ (Regression Risk) ✅ لا يوجد كود تم تعديله على البيئة.
3. ❌/✅ هل وصلت للحل بأقل عدد خطوات ممكن؟ ✅ نعم، تم التوضيح بشكل مباشر ومختصر.
4. ❌/✅ هل في تكرار (DRY violation)؟ ✅ لا يوجد.
5. ❌/✅ هل حدّثت سجل الذاكرة؟ ✅ تم الالتزام بضوابط التشغيل والحدود التقنية.
