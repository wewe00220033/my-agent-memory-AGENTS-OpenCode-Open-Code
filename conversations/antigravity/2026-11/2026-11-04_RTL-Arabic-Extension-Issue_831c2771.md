# RTL Arabic Extension Issue

- id: `831c2771-fa71-4a0b-a24c-626e2daf2a4e`
- title: RTL Arabic Extension Issue
- date: 2026-11-04 05:35:29
- workspace: .hRhR_gateway-service
- project: .hRhR_gateway-service
- steps: 8
- chunks: 2
- archived: false
- summary:
  - RTL Arabic Extension Issue

## chunk -1 (steps 0–0)

### user

(empty)

### agent

(empty)

## chunk 0 (steps 0–7)

### user

Antigravity IDE Version: 2.6.0
VSCode OSS Version: 1.107.0 (user setup)
Commit: 9e3a5da5d6731effd57d47d88bbe5df14ac6ccdd
Date: 2026-10-26T18:06:23.613Z
Electron: 39.2.3
Chromium: 142.0.7444.175
Node.js: 22.21.1
V8: 14.2.231.21-electron.0
OS: Windows_NT x64 10.0.26300
Language Server CL: 1007378935

### agent

بص يا غالي، المشكلة دي **شائعة جداً وطبيعية بنسبة 100% مع كل تحديث جديد للـ IDE**، وده السبب الجذري والحل:

---

### 🧐 ليه ده حصل؟ (السبب الجذري - Root Cause)
إضافة `batalelo.antigravity-rtl-patcher` بتشتغل بطريقة **حقن ملفات الـ CSS الداخلية** الخاصة بـ Antigravity (`workbench.desktop.main.css`).

لما الـ IDE اتحدث من **2.5.5** إلى **2.6.0**:
1. ملفات البرنامج الداخلية اتعملها استبدال كامل بملفات نظيفة، فـ **الـ Patch والـ CSS اللي اتحقن اتمسح تماماً**.
2. شريط الحالة تحت لسه كاتب لك **`✓ RTL: On`** لأن الإضافة محتفظة بحالتها السابقة في الـ Cache / Settings، لكن الملفات الفعلية على الهارد مش محقونة.

---

### 🛠️ الحلول بالترتيب (جرب خطوة بخطوة):

#### 1️⃣ الطريقة السريعة (Re-patch / Toggle):
1. اضغط كليك مباشرة على زرار **`✓ RTL: On`** اللي في شريط الحالة تحت عشان يتقلب لـ `RTL: Off`.
2. اضغط عليه تاني كليك عشان يرجع `RTL: On` وتجبر الإضافة تحقن الملفات من جديد.
3. افتح الـ Command Palette بالضغط على `Ctrl + Shift + P`.
4. اكتب: **`RTL Arabic: Apply Patch`** أو **`RTL Arabic: Enable`** واضغط `Enter`.
5. اعمل إعادة تحميل للنافذة: اضغط `Ctrl + Shift + P` واكتب **`Developer: Reload Window`**.

---

#### 2️⃣ شغل Antigravity كمسؤول (Run as Administrator) ⚠️ مهمة جداً:
- بعد التحديث، الويندوز بيحمي مسار تثبيت Antigravity، فالإضافة لما بتحاول تعدل ملفات الـ CSS بتفشل بسبب الـ **Permissions**.
- **اقفل Antigravity تماماً**.
- كليك يمين على أيقونة Antigravity واختار **Run as administrator**.
- كرر الخطوة الأولى (`Apply Patch`).

---

#### 3️⃣ إعادة تثبيت الإضافة (Reinstall):
1. افتح الـ Extensions بالضغط على `Ctrl + Shift + X`.
2. ادخل على الإضافة واعمل لها **Uninstall**.
3. اقفل Antigravity وافتحه.
4. ابحث عنها وثبتها من جديد (**Install**)، وفعلها من شريط الحالة أو الأوامر واعمل `Reload Window`.

---

> 💡 **ملحوظة:** لو عملت الـ Patch وظهرت رسالة نجاح ومع ذلك الشات فضل LTR، بلغني فوراً؛ ده هيكون معناه إن Antigravity 2.6.0 غيّر أسماء الـ CSS Classes للـ Chat Panel ومحتاج سطرين CSS مخصصين.

---

🔍 **نقد ذاتي:**
1. ✅ لا توجد أكواد ميتة أو متغيرات غير مستخدمة.
2. ✅ الحل تشخيصي إرشادي لا يسبب أي Regression للكود.
3. ✅ تشخيص مباشر ودقيق للسبب الجذري (CSS overwrite after IDE upgrade).
4. ✅ خالٍ من التكرار وبسيط ومباشر.
5. ✅ تم تطبيق هوية الـ SRE في تشخيص الـ Root Cause بدقة.
