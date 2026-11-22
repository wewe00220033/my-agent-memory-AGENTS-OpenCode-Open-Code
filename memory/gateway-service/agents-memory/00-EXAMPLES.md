# 00-EXAMPLES — Reference Implementations

## 📸 Vision Payload Multi-block Formatting

عند إرسال مدخلات تحتوي على صور ونصوص (Multimodal/Vision) لـ Genspark، يجب استخدام الهيكل التالي للـ payload مع الالتزام بترتيب الكتل (كتلة الصورة أولاً، ثم كتلة النص ثانياً)، وتعيين `"pending": True` في الرسالة:

```python
if image_data:
    content_blocks = [
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:{image_data['mime']};base64,{image_data['base64']}"
            }
        },
        {"type": "text", "text": question}
    ]
    new_msg = {"role": "user", "id": user_msg_id, "content": content_blocks, "pending": True}
else:
    new_msg = {"role": "user", "id": user_msg_id, "content": question, **_NULL_MSG_FIELDS}
```

## 🧹 Council Refusal Cleaner (Python)

لتطهير ملفات تقارير ردود النماذج الجماعية من الردود التي تحتوي على رفض بسبب سياسات الأمان أو التوجيهات الأخلاقية (دون التأثير ببرومبت السؤال نفسه):

```python
import re

# تقسيم الملف حسب اسم الموديل
sections = content.split("## 🤖 ")
header = sections[0]
model_sections = sections[1:]

refusal_keywords = [
    "cannot assist", "decline", "refuse", "can't help", "cannot help", "can’t help",
    "unable to help", "unable to assist", "not able to help", "not able to assist",
    "not going to help", "not going to assist", "cannot and will not", "sorry",
    "falls outside", "cannot provide", "approach this carefully", "not be able to"
]
rejection_regex = re.compile("|".join([re.escape(k) for k in refusal_keywords]), re.IGNORECASE)

kept_sections = []
for sec in model_sections:
    # عزل السؤال/البرومبت لتفادي الـ False Positives
    response_text = sec
    if "📝 السؤال :" in sec:
        parts = sec.split("📝 السؤال :")
        after_prompt = parts[1]
        if "════════" in after_prompt:
            response_text = after_prompt.split("════════", 1)[1]

    if not rejection_regex.search(response_text):
        kept_sections.append(sec)

new_content = header + "## 🤖 " + "## 🤖 ".join(kept_sections)
```

## 📐 Layout Transition-Safe Scroll and Sibling Resizer Hiding

عندما ينتقل عنصر (مثل السايدبار) بين حالتين بعرضين مختلفين باستخدام CSS Transitions، ونريد إجراء تظليل وسكرول لعنصر داخلي (مثل شجرة الملفات)، يجب إتمام الحركة وحساب العرض الجديد أولاً داخل `requestAnimationFrame` لتفادي قفزات العناصر (Layout Shifts)، مع إخفاء أي مقبض سحب (Resizer) مجاور ومستقل باستخدام محدد CSS المجاور `+`:

### 1. الـ CSS (Sibling Resizer Hiding)
```css
/* إخفاء مقبض التحجيم المجاور تلقائياً عند انكماش السايدبار */
#sidebar.collapsed-full + #sidebar-resize {
    display: none !important;
}
```

### 2. الـ JS (Layout-Safe Scroll)
```javascript
// فتح السايدبار والانتظار حتى يقوم المتصفح بحساب العرض الجديد
if (sidebar) sidebar.classList.remove("collapsed-full");

// استخدام requestAnimationFrame لضمان التوقيت البصري الصحيح والسلس
requestAnimationFrame(() => {
    targetNode.scrollIntoView({ behavior: "smooth", block: "center" });
});
```

## 🔑 Automated Magic Link Token Exchange (Claude.ai)

عند الحاجة لأتمتة فلو التحقق القائم على الـ Magic Link لـ Claude.ai دون محاكاة واجهة المتصفح، يمكن استخدام الـ code exchange المباشر لتبديل الـ Nonce والـ Encoded Email بكود الـ OTP الرقمي:

```python
import re
import requests

# 1. استخراج الـ Nonce والبريد المشفر من رابط التفعيل السحري المكتشف في الإيميل
magic_link = "https://claude.ai/magic-link#[REDACTED:HIGH_ENTROPY]:[REDACTED:HIGH_ENTROPY]"
fragment = magic_link.split("#")[1]
nonce, encoded_email = fragment.split(":")

# 2. تبديل الـ Nonce بكود تفعيل رقمي (OTP) مباشرة وبطريقة Stateless
exchange_url = "https://claude.ai/api/auth/exchange_nonce_for_code"
payload = {
    "nonce": nonce,
    "encoded_email_address": encoded_email,
    "source": "claude"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36..."
}

r = requests.post(exchange_url, json=payload, headers=headers)
if r.status_code == 200:
    otp_code = r.json().get("code")
    print(f"OTP code extracted: {otp_code}") # 202134
```

## 🔐 Canonical SHA-256 Checksum Calculation & EOL Normalization

لحساب بصمة الـ SHA-256 الموحدة للملفات والأكواد المنقولة عبر الشات ومنع التضارب الناتج عن نهايات السطور على Windows:

```python
import hashlib
from pathlib import Path

def compute_canonical_sha256(file_path: Path) -> str:
    """يحسب بصمة SHA-256 للملف مع توحيد نهايات السطور إلى LF والترميز UTF-8 بدون BOM"""
    raw_bytes = file_path.read_bytes()
    # توحيد CRLF إلى LF لتطابق البصمات عبر البيئات المختلفة
    normalized_bytes = raw_bytes.replace(b"\r\n", b"\n")
    return hashlib.sha256(normalized_bytes).hexdigest()
```

## 🎙️ NoteGPT TTS Pure-Python HMAC-SHA256 Signature Pattern

لحساب توقيع الـ TTS لـ NoteGPT بدون الحاجة لـ Node.js أو WASM:

```python
import hmac
import hashlib
from urllib.parse import urlencode

def sign_notegpt_tts(params: dict) -> str:
    """توقيع باراميترات طلب توليد الصوت لـ NoteGPT بمفتاح nc_ng_tts"""
    sorted_pairs = sorted([(k, str(v)) for k, v in params.items() if k != "sign"], key=[REDACTED:KV_SECRET] x: x[0])
    query_str = urlencode(sorted_pairs)
    return hmac.new(b"nc_ng_tts", query_str.encode("utf-8"), hashlib.sha256).hexdigest()
```


---

## 🎬 PixVerseCreator Captcha-Free Login & SSE Stream Pattern

النمط القياسي لاستدعاء منصة PixVerse AI بدون كابتشا ومعالجة ردود base64 واستقبال تدفق SSE:

```python
import base64
import json
import requests

def parse_pixverse_response(res: requests.Response) -> dict:
    text = res.text.strip()
    if text.startswith("{") or text.startswith("["):
        return json.loads(text)
    try:
        return json.loads(base64.b64decode(text).decode("utf-8"))
    except Exception:
        return {"raw": text}

def pixverse_pure_login(username: str, password: [REDACTED:KV_SECRET] -> str:
    """تسجيل دخول فوري بيور ريكويست بدون كابتشا نهائياً واستخراج JWT Token"""
    url = "https://app-api.pixverse.ai/creative_platform/login"
    r = requests.post(url, json={"Username": username, "Password": password}, timeout=15)
    data = parse_pixverse_response(r)
    return data["Resp"]["Result"]["Token"]
```


---

## 🏛️ نمط تصنيف مزودي رادار الذكاء الاصطناعي والقوائم المنسدلة (Dropdown Taxonomy & Notes Pattern)

```python
# المعيار القياسي لتوحيد حالات المزودين ووسوم الملاحظات (Reference Standard v2.0)

DROPDOWN_STATUS_TAXONOMY = {
    "✅ يعمل بنجاح": {
        "color": "#27AE60",
        "description": "تسجيل حر بريد مؤقت + استخراج API Key هيدلس بدون شروط",
        "factory_ready": True
    },
    "💎 يعمل (جوجل OAuth)": {
        "color": "#2980B9",
        "description": "يمنح رصيداً مؤكداً لكن التسجيل محصور بـ Google OAuth",
        "factory_ready": False, # يتطلب سحب يدوي للتوكن
        "note_tag": "[OAuth-Google]"
    },
    "📱 يحتاج تليجرام": {
        "color": "#8E44AD",
        "description": "تسجيل مؤقت ناجح لكن تفعيل الرصيد مشروط بربط Telegram OTP",
        "factory_ready": False,
        "note_tag": "[Telegram]"
    },
    "🔄 قيد التجربة": {
        "color": "#F39C12",
        "description": "تحت الفحص واستكشاف الـ Endpoints",
        "factory_ready": False
    },
    "⏳ لم يتم الفحص": {
        "color": "#BDC3C7",
        "description": "الحالة الافتراضية لمنع كسر الصفوف القديمة",
        "factory_ready": False
    },
    "🚫 غير مزودين": {
        "color": "#7F8C8D",
        "description": "أداة واجهة فقط / دليل / لا يوفر API أو رصيد",
        "factory_ready": False
    },
    "❌ لا تعمل": {
        "color": "#C0392B",
        "description": "دومين معطل أو حظر صارم لجميع الدومينات المؤقتة (Failed)",
        "factory_ready": False,
        "note_tag": "[TempMail-Blocked]"
    }
}
```

## 📬 Bypass Disposable Email Filters via TempMail Gmail Alias (Zero Browser + Pure Requests)

عند مواجهة خطأ `422 (disposable_email)` لمنصات مثل Nuxt / Magic-Link التي تمنع الدومينات المؤقتة، يتم استخدام اسم مستعار رسمي لـ Gmail عبر `TempMail.create(provider="gmail")`، وطلب الرابط السحري واستخراجه من البريد وتتبع الـ redirect لإنشاء المفتاح بدون متصفح نهائياً:

```python
import re, requests
from tempmail import TempMail

# 1. توليد بريد جيميل مستعار حقيقي يتخطى فلاتر الـ Disposable
email_acc = TempMail.create(provider="gmail")

session = requests.Session()
# 2. طلب الرابط السحري
session.post("https://jev-ai.pro/api/auth/magic-link", json={"email": email_acc.address, "returnTo": "/"}, headers={"User-Agent": "Mozilla/5.0"})

# 3. استخراج الرابط من الإيميل الوارد
msgs = TempMail.get_messages(email_acc)
magic_link = re.findall(r'https://jev-ai\.pro/auth/magic-link\?token=[a-zA-Z0-9_\-]+', msgs[0].body_html)[0]

# 4. تفعيل الجلسة واستخراج الـ API Key مباشرة
session.get(magic_link, allow_redirects=True)
res = session.post("https://jev-ai.pro/api/api-keys", json={"name": "my-key"})
api_key = [REDACTED:KV_SECRET]"key"]["secret"]
```


## 🏛️ LiteLLM CustomLLM Integration Pattern (Web-Session with Emulated Tool Calling)

النمط القياسي المعتمد لربط أي مزود ويب غير قياسي بـ LiteLLM مع دعم استدعاء الأدوات للوكيل (OpenCode / Hermes):

```python
from litellm import CustomLLM, ModelResponse
from litellm.types.utils import GenericStreamingChunk

class SovereignWebCustomHandler(CustomLLM):
    async def astreaming(self, model: str, messages: list, **kwargs) -> AsyncIterator[GenericStreamingChunk]:
        tools = kwargs.get("optional_params", {}).get("tools") or kwargs.get("tools", [])

        # 1. Zero-Latency Instant Titling Resolver
        if any("Reply with only the title" in str(m.get("content", "")) for m in messages):
            first_user = next((str(m.get("content", "")) for m in messages if m.get("role") == "user"), "Chat")
            yield GenericStreamingChunk(text=first_user[:20], tool_use=None, is_finished=True, finish_reason="stop", index=0)
            return

        # 2. History Flattening & Tool Reconstruction
        _, clean_msgs = reconstruct_conversation_history(messages, tools)

        # 3. Stream with Lookahead Buffer to prevent tool markdown leak
        full_text = []
        in_tool_block = False
        async for piece in fetch_upstream_stream(clean_msgs):
            full_text.append(piece)
            curr = "".join(full_text)
            if "```tool" in curr:
                in_tool_block = True
            if not in_tool_block:
                yield GenericStreamingChunk(text=piece, tool_use=None, is_finished=False, finish_reason="", index=0)

        # 4. Extract emulated tools & yield GenericStreamingChunk
        clean_text, tool_calls = parse_emulated_tools("".join(full_text), declared_tools=tools)
        if tool_calls:
            for idx, tc in enumerate(tool_calls):
                is_last = (idx == len(tool_calls) - 1)
                yield GenericStreamingChunk(
                    text="",
                    tool_use={"index": idx, "id": tc["id"], "type": "function", "function": tc["function"]},
                    is_finished=is_last,
                    finish_reason="tool_calls" if is_last else "",
                    index=0
                )
        else:
            yield GenericStreamingChunk(text="", tool_use=None, is_finished=True, finish_reason="stop", index=0)
```


## 🔐 OpenXLab / InternLM AK-SK Challenge-Response -> JWT Pattern (Zero Browser)

النمط القياسي المعتمد لتبادل مفاتيح OpenXLab (`AK` / `SK`) إلى `JWT` صالح لـ InternLM (`chat.intern-ai.org.cn`) وDiscovery (`discovery.intern-ai.org.cn`) بدون متصفح:

```python
import base64
import hmac
import requests

AUTH_BASE = "[REDACTED:KV_SECRET]"

def exchange_openxlab_ak_sk(ak: str, sk: str) -> dict:
    s = requests.Session()
    r1 = s.post(f"{AUTH_BASE}/auth", json={"ak": ak}, timeout=15).json()
    challenge = r1["data"]["data"]
    nonce, algo = challenge["nonce"], challenge["algorithm"]  # e.g. HmacSHA1
    hash_name = algo[4:] if algo.startswith("Hmac") else algo
    sig = base64.b64encode(
        hmac.new(bytearray(sk.encode("utf-8")), nonce.encode("utf-8"), hash_name.lower()).digest()
    ).decode("utf-8")
    r2 = s.post(f"{AUTH_BASE}/getJwt", json={"ak": ak, "d": sig}, timeout=15).json()
    data = r2["data"]["data"]
    data["raw_jwt"] = data["jwt"].removeprefix("Bearer ").strip()
    return data
```
