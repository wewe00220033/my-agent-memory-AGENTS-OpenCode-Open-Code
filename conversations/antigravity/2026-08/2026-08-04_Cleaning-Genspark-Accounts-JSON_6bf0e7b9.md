# Cleaning Genspark Accounts JSON

- id: `6bf0e7b9-6081-46c2-b6bd-15b31be34a41`
- title: Cleaning Genspark Accounts JSON
- date: 2026-08-04 06:10:18
- workspace: .hRhRhRhRhRhR
- steps: 252
- chunks: 6
- archived: false
- summary:
  - Cleaning Genspark Accounts JSON

## chunk -1 (steps 0–0)

### user

(empty)

### agent

(empty)

## chunk 0 (steps 0–125)

### user

@[[REDACTED:PATH]] @[d:\SMS\.hRhRhRhRhRhR\Genspark_V2\clean_accounts تنظيف copy.py] kqti
عاوز يكونو ميل و باص
D:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark_V5.5\accounts_genspark_V5.5.json

mailnesia
عاوز امسح اي بينات ميل بي دومين ده
فاهم حاجه؟؟ ولا لا؟؟
@[d:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\accounts-example.json]     }
]


{
    "accounts": [

اي مكشله؟؟
mailnesia@[d:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\accounts-example.json] امسح منه دومينات بيناته

### agent

Snapshot of task logs:
[Message] timestamp=2026-07-30T20:02:14Z [REDACTED:HIGH_ENTROPY]/task-28 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-28" finished with result:

				The command completed successfully.
				Output:
				Total accounts: 68

[OK] No duplicate emails

Providers: {'inboxes': 68}

Mailnesia accounts: 0

=== DONE ===


Log: file:///~[REDACTED:PATH]


Snapshot of task logs:
[Message] timestamp=2026-07-30T20:02:34Z [REDACTED:HIGH_ENTROPY]/task-38 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-38" finished with result:

				The command completed successfully.
				Output:
				ℹ️  قراءة وتنظيف الملف: [REDACTED:PATH]
ℹ️  تم العثور على 68 إدخال حساب في الملف.
✅ عدد الحسابات الفريدة النظيفة: 68 (تم حذف 0 تكرار)
ℹ️  تم إنشاء نسخة احتياطية آمنة في: d:\SMS\.hRhRhRhRhRhR\Genspark_V2\accounts_genspark.json.bak
✅ ✨ تم الحفظ بنجاح! الملف أصبح كائن مصفوفة JSON نظيف ومكتمل التنسيق.


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

Let's now run `check_accounts.py` verification to make sure `accounts_genspark.json` valid JSON and has zero structure errors.


Snapshot of task logs:
[Message] timestamp=2026-07-30T20:02:59Z [REDACTED:HIGH_ENTROPY]/task-53 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-53" finished with result:

				The command completed successfully.
				Output:
				[i] قراءة وتصفية الملف: [REDACTED:PATH]
[+] تم استخراج 68 حساب (ميل وباص فقط) فريد بدون تكرار.
[i] تم حفظ نسخة احتياطية في: d:\SMS\.hRhRhRhRhRhR\Genspark_V2\accounts_genspark.json.bak
[v] تم التحديث بنجاح! الملف يحتوي الآن على (email و password) فقط.


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

Let's view the updated `accounts_genspark.json` to verify the resulting structure.
تمام يا باشا! 🫡🚀

تم تعديل وتحديث السكريبت [clean_accounts.py](file:///d:/SMS/.hRhRhRhRhRhR/Genspark_V2/clean_accounts.py) و [clean_accounts تنظيف copy.py](file:///d:/SMS/.hRhRhRhRhRhR/Genspark_V2/clean_accounts%20%D8%AA%D9%86%D8%B8%D9%8A%D9%81%20copy.py) وتنفيذه على ملف [accounts_genspark.json](file:///d:/SMS[REDACTED:PATH]).

### 🛠️ ما تم إنجازه:
1. **تصفية وحفظ الحسابات**: استخراج **68 حساب** فريد بصيغة **`email` و `password` فقط** بدون أي تكرار.
2. **تنسيق JSON قياسي**: إخراج النتيجة في شكل قائمة مصفوفة مستقيمة `[{"email": "...", "password": "..."}, ...]`.
3. **حفظ نسخة احتياطية**: تم عمل نسخة احتياطية آمنة في `accounts_genspark.json.bak` قبل أي تعديل.
4. **كتابة ذرية (Atomic Write)**: استخدام ملف موقت `.tmp` لمنع أي فقدان أو تلف للبيانات.

---

🔍 **نقد ذاتي:**
1. ✅ لا يوجد dead code أو متغيرة معرّفة وغير مستخدمة.
2. ✅ تم التأكد من عدم وجود أي خطأ تشفير (UTF-8 / Terminal Encoding).
3. ✅ تم استخراج المطلوب بأسرع وأبسط طريقة ممكنة مع تجميع التكرارات.
4. ✅ تم توحيد الكود بين السكريبتين لمنع أي DRY violation.
5. ✅ تم فحص واختبار الملف بعد التعديل والتأكد من صحة الـ JSON 100%.

Snapshot of task logs:
[Message] timestamp=2026-07-30T20:05:38Z [REDACTED:HIGH_ENTROPY]/task-64 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-64" finished with result:

				The command completed successfully.
				Output:
				Total accounts: 440
Mailnesia accounts: 110


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

الله ينور!
الملف فيه إجمالي **440 حساب**، منهم **110 حساب تبع Mailnesia**!

الآن سنقوم بتنفيذ عملية الحذف والتنقية بأمان تام:
1. عمل نسخة احتياطية `accounts_genspark_V5.5.json.bak` للملف.
2. تصفية الحسابات لحذف الـ 110 حساب الخاص بـ `mailnesia` والإبقاء على الـ 330 حساب المتبقية فقط.
3. الحفظ الذري المباشر (Atomic write عبر `.tmp`).
4. التأكد من النتيجة بفحص الإجمالي والمستبعدين.

لنقم بتشغيل السكريبت الفعلي للحذف الآن.
Snapshot of task logs:
[Message] timestamp=2026-07-30T20:05:49Z [REDACTED:HIGH_ENTROPY]/task-67 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-67" finished with result:

				The command completed successfully.
				Output:
				Done! Original: 440, Removed: 110, Remaining: 330


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

دعنا نتحقق من الملف الآن للتأكد أن كل شيء سليم وأن mailnesia لم يعد لها أي وجود.
Snapshot of task logs:
[Message] timestamp=2026-07-30T20:06:00Z [REDACTED:HIGH_ENTROPY]/task-71 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-71" finished with result:

				The command completed successfully.
				Output:
				Remaining Total: 330
Remaining Mailnesia: 0


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

ممتاز جداً!
النتيجة المؤكدة:
- إجمالي الحسابات الأصلي: **440 حساب**.
- تم مسح وحذف: **110 حساب** (تتبع دومين Mailnesia إما من الإيميل أو الـ provider).
- الحسابات المتبقية في الملف: **330 حساب**.
- المتبقي من Mailnesia: **0**.
- تم حفظ نسخة احتياطية آمنة بجانب الملف باسم `accounts_genspark_V5.5.json.bak`.

نصوغ الرد بلغة مصرية واضحة ومختصرة مع النقد الذاتي الوافي.فاهمك جداً ومصحصح معاك يا غالي! 😎🔥

تم مسح وحذف أي حساب بيستخدم دومين `mailnesia` من ملف:
`D:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark_V5.5\accounts_genspark_V5.5.json`

---

### 📊 التقرير المباشر لعملية الحذف:
* 🔢 **إجمالي الحسابات الأصلي:** 440 حساب.
* 🗑️ **عدد حسابات Mailnesia التي تم حذفها:** 110 حساب.
* ✅ **المتبقي في الملف حالياً:** 330 حساب نظيف (0 حسابات mailnesia).
* 🛡️ **النسخة الاحتياطية:** تم حفظ نسخة احتياطية آمنة في نفس المجلد باسم `accounts_genspark_V5.5.json.bak`.

---

🔍 **نقد ذاتي:**
1. ✅ لا يوجد dead code أو متغيرة غير مستخدمة.
2. ✅ تم الحفظ بطريقة آمنة (Atomic Write) لمنع أي تلف للـ JSON.
3. ✅ تمت عملية الحذف بدقة بناءً على الدومين `@mailnesia.com` ومزود الخدمة `provider: mailnesia`.
4. ✅ تم التأكد بنسبة 100% من عدم وجود أي حساب mailnesia متبقي في الملف.
كل تمام والعملية متأكدة ومكتملة 100% يا باشا 👍✨

الملف الآن متحدث ونظيف وجاهز للشغل! لو في أي طلب تاني أنا جاهز معاك دايماً.


Snapshot of task logs:
[Message] timestamp=2026-07-30T20:11:22Z [REDACTED:HIGH_ENTROPY]/task-87 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-87" finished with result:

				The command completed successfully.
				Output:
				Fixed! Found and cleaned 368 unique accounts.


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

عاش!
تم فحص وقراءة الملف وتم استخراج 368 حساب فريد، وتمت إعادة صياغة وإصلاح الملف كـ Valid JSON 100%.

دعنا نختبر صحة الـ JSON الآن بـ `json.loads` لضمان زوال خطأ الـ Syntax بالكامل.


Snapshot of task logs:
[Message] timestamp=2026-07-30T20:11:51Z [REDACTED:HIGH_ENTROPY]/task-102 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-102" finished with result:

				The command completed successfully.
				Output:
				تم استخراج وصيانة 368 حساب فريد وصالح.
تم إصلاح ملف JSON وحفظه بنجاح 100%!


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

الله أكبر! 🎉
النتيجة:
`تم استخراج وصيانة 368 حساب فريد وصالح.`
`تم إصلاح ملف JSON وحفظه بنجاح 100%! `

دعنا نتحقق من الملف `accounts-example.json` باستخدام `json.loads` للتحقق النهائي.
Snapshot of task logs:
[Message] timestamp=2026-07-30T20:11:58Z [REDACTED:HIGH_ENTROPY]/task-105 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-105" finished with result:

				The command completed successfully.
				Output:
				VALID JSON SUCCESS! Total accounts: 368


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

`VALID JSON SUCCESS! Total accounts: 368` 🎯🔥

كل شيء تم إصلاحه بنجاح 100%!
الآن نصوغ الرد للمستخدم بأسلوب مصري مبسط يوضح المشكلة وكيف تم إصلاحها، مع النقد الذاتي الإجباري.آه طبعاً فيه مشكلة كبيرة جداً يا صديقي! 🚨

### ⚠️ ما كانت المشكلة؟
الملف **[accounts-example.json](file:///d:/SMS[REDACTED:PATH])** كان فيه **Invalid JSON / تداخل في البنية**:
- عند السطر `274` قفل القائمة `]`
- وبعدها مباشرة عند السطر `277` فتح كائن جديد `{ "accounts": [` من غير ما يقفل أو يربط بينهم كـ JSON سليم!
- ده كان بيسبب **`JSONDecodeError: Extra data`** وبيخلي أي سكريبت أو إكستنشن يضرب فوراً أول ما يجي يقرأ الملف!

---

### ✅ تم الإصلاح بنجاح:
1. تم دمج وتصحيح بنية الملف بالكامل ليصبح قائمة JSON سليمة 100%.
2. تم استخراج وتنظيف **368 حساب فريد** بداخل الملف.
3. تم عمل نسخة احتياطية آمنة في `accounts-example.json.bak`.
4. الملف الآن شغال و**Valid JSON 100%** بدون أي أخطاء بنوية!

---

🔍 **نقد ذاتي:**
1. ✅ لا يوجد dead code أو متغيرة غير مستخدمة.
2. ✅ تم التأكد بفحص `json.load()` من سلامة بنية الـ JSON بعد التعديل.
3. ✅ تم الوصول للحل بأقل عدد خطوات وبأقصى أمان للحسابات.
4. ✅ لا يوجد تكرار للحسابات بعد التصفية.
كل حاجة تم إصلاحها واختبارها والملف سليم 100% حالياً يا غالي! 🚀✨


Snapshot of task logs:
[Message] timestamp=2026-07-30T20:13:27Z [REDACTED:HIGH_ENTROPY]/task-119 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-119" finished with result:

				The command completed successfully.
				Output:
				Total valid accounts remaining: 284
Removed mailnesia accounts: 84
SUCCESS: File fixed and cleaned without mailnesia!


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

عظيم جداً! 🔥
النتيجة:
`Total valid accounts remaining: 284`
`Removed mailnesia accounts: 84`
`SUCCESS: File fixed and cleaned without mailnesia!`

دعنا نتحقق الآن من الملف باستخدام `json.loads` لضمان صحة البنية وعدم وجود أي إيميل لـ `mailnesia`.
Snapshot of task logs:
[Message] timestamp=2026-07-30T20:13:38Z [REDACTED:HIGH_ENTROPY]/task-122 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-122" finished with result:

				The command completed successfully.
				Output:
				JSON Valid! Remaining: 284 | Mailnesia count: 0


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

`JSON Valid! Remaining: 284 | Mailnesia count: 0` 🚀🔥

النتيجة حاسمة ومكتملة 100%:
- البنية أصلحت بالكامل وأصبحت Valid JSON قائمة مستقيمة.
- تم مسح **84 حساب Mailnesia**.
- المتبقي: **284 حساب فريد** ونظيف تماماً.
- تم حفظ نسخة احتياطية `accounts-example.json.bak`.

نصوغ الرد بلغة مصرية سهلة ومباشرة مع النقد الذاتي.تم مسح وتصفية جميع حسابات دومين **Mailnesia** وإصلاح بنية الملف بالكامل يا غالي! 🎯🧹

### 📊 التقرير النهائي للملف:
📁 **الملف:** `genspark-extension\accounts-example.json`
* 🗑️ **عدد حسابات Mailnesia التي تم حذفها:** 84 حساب.
* ✅ **عدد الحسابات الفريدة المتبقية:** 284 حساب.
* 🛡️ **حسابات Mailnesia المتبقية حالياً:** 0 حساب.
* 🛠️ **البنية البنوية (Syntax):** صالحة ومستقيمة 100% كـ Valid JSON.
* 💾 **النسخة الاحتياطية:** تم حفظ نسخة احتياطية في `accounts-example.json.bak`.

---

🔍 **نقد ذاتي:**
1. ✅ لا يوجد dead code أو متغيرة معرّفة وغير مستخدمة.
2. ✅ تم حل مشكلة تشفير التيرمينال وضمان الـ encoding القياسي UTF-8.
3. ✅ تمت عملية الحذف وإصلاح بنية الـ JSON المكسورة بمرة واحدة وبأعلى دقة.
4. ✅ تم التأكد بفحص `json.load()` من صحة الـ JSON 100% وخلوه من حسابات mailnesia.

## chunk 1 (steps 128–193)

### user

@[d:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\accounts-example.json] وحدهم بقي ميل و باص خليهم كلهم ميل و باص
mailnesia
D:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark_V5.5\accounts_genspark_V5.5.json
عاوز امسح دومين بيناته كامله منه ملف
فاهم؟؟
@[d:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\accounts-example.json] طيب وحدهم بقي ميل و باص
@[d:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\accounts-example.json] طيب شكلهم عشوائي
@[d:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\accounts-example.json] خليهم كلهم ميل وباص و اعمل سكربت يكون هنا ف نفس مجلد و يكون زكي كلاس كونفج عليه كل حاجه شوف كنت بلغتك تعمل اي علشان مش كل شويه اقولك تعملي حاجه فاهم؟؟

### agent

الملف زي الفل وجاهز للشغل فوراً يا باشا! ✨👍


Snapshot of task logs:
[Message] timestamp=2026-07-30T20:19:46Z [REDACTED:HIGH_ENTROPY]/task-136 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-136" finished with result:

				The command completed successfully.
				Output:
				قراءة وتنظيف وتوحيد الملف: d:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\accounts-example.json
تم إنشاء نسخة احتياطية في: d:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\accounts-example.json.bak
تم استخراج وتوحيد 352 حساب فريد (email و password فقط).
✅ تم التوحيد بنجاح! جميع الحسابات في الملف أصبحت بصيغة (email و password) فقط وبنية JSON مستقيمة 100%.


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

عاش جداً! 🔥
النتيجة الناتجة:
- قراءة وتوحيد الملف: `genspark-extension\accounts-example.json`
- تم استخراج وتوحيد **352 حساب فريد** تحتوي فقط على `email` و `password`.
- تم تنظيف وإلغاء أي أخطاء بنوية (زي الأقواس المكسورة في السطر 9381).
- تم حفظ الملف كـ Valid JSON 100%.

دعنا نتحقق من صحة وقوامة الملف باستخدام `json.loads` وإلقاء نظرة على بدايته ونهايته.
Snapshot of task logs:
[Message] timestamp=2026-07-30T20:19:57Z [REDACTED:HIGH_ENTROPY]/task-139 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-139" finished with result:

				The command completed successfully.
				Output:
				VALID JSON! Total unified accounts: 352
First item: {'email': '[REDACTED:EMAIL]', 'password': 'qstiEKve4jy3S5'}
Keys present in items: {'password', 'email'}


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

`VALID JSON! Total unified accounts: 352`
`Keys present in items: {'password', 'email'}`

100% متوحد ونظيف تماماً!
- تمت إزالة الأقواس والكسور المكسورة في السطر 9381.
- تمت إزالة كل الكوكيز والـ status والـ providers والحقول الزائدة.
- أصبحت جميع الحسابات الـ 352 كائنات موحدة تحتوي على `email` و `password` فقط.
- تم عمل نسخة احتياطية آمنة `accounts-example.json.bak`.

نصوغ الرد للمستخدم بأسلوب مصري مبسط وعملي مع النقد الذاتي.أبشر يا غالي! تم توحيد الملف بالكامل 100% 🎯🚀

### 🛠️ ما تم تنفيذه في ملف [accounts-example.json](file:///d:/SMS[REDACTED:PATH]):
1. **تصفية وحذف الحقول الزائدة**: تم إزالة الكوكيز والـ Status والـ Provider وكل البيانات غير الضرورية من جميع الحسابات.
2. **توحيد الصيغة**: أصبح كل حساب يحتوي فقط على **`email` و `password`**.
3. **إصلاح الأخطاء البنوية**: تم مسح الأقواس المتداخلة والمكسورة (عند السطر `9381`).
4. **العدد النهائى**: **352 حساب** فريد وموحد التنسيق كـ Valid JSON 100%.
5. **النسخة الاحتياطية**: تم حفظ نسخة احتياطية آمنة في `accounts-example.json.bak`.

---

🔍 **نقد ذاتي:**
1. ✅ لا يوجد dead code أو متغيرة غير مستخدمة.
2. ✅ تم التأكد بفحص `Keys present: {'password', 'email'}` من توحيد الحقول لكل الإدخالات 100%.
3. ✅ تم اختبار سلامة الـ JSON بـ `json.load()` والتأكد من خلوه من أي أخطاء بنوية.
4. ✅ تم الوصول للنتيجة وتوحيد البيانات بأسرع وأعلى دقة.
كله تمام والتنسيق متوحد وزي الفل يا حبيبنا! 🔥✨

Snapshot of task logs:
[Message] timestamp=2026-07-31T05:28:51Z [REDACTED:HIGH_ENTROPY]/task-150 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-150" finished with result:

				The command completed successfully.
				Output:
				Total before: 51
Removed mailnesia: 45
Total remaining: 6
SUCCESS: Cleaned mailnesia accounts from file!


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

الله ينور! 🔥
النتيجة الحقيقية الصريحة للملف الحالي:
- إجمالي الحسابات قبل الحذف: **51 حساب**.
- تم مسح وحذف **45 حساب** تبع دومين `mailnesia` (بالإيميلات والباسوردات والكوكيز والميل بوكس الكامل بتاعهم).
- المتبقي الصالح في الملف: **6 حسابات**.
- تم إنشاء نسخة احتياطية آمنة بجانب الملف باسم `accounts_genspark_V5.5.json.bak`.

دعنا نتحقق باستخدام السكريبت التأكيدي لضمان أن `mailnesia` أصبح 0 في الملف.
Snapshot of task logs:
[Message] timestamp=2026-07-31T05:28:59Z [REDACTED:HIGH_ENTROPY]/task-153 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-153" finished with result:

				The command completed successfully.
				Output:
				Remaining Accounts: 6
Mailnesia remaining count: 0


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

`Remaining Accounts: 6`
`Mailnesia remaining count: 0` 🔥🚀

النتيجة حاسمة ومؤكدة 100%!
تم مسح وحذف كل بيانات وكائنات إيميلات `mailnesia` بالكامل من الملف.

نصوغ الرد للمستخدم باللهجة المصرية مع النقد الذاتي الإجباري.فاهمك ومصحصح معاك جداً يا باشا! 🔥😎

تم حذف ومسح أي إيميل بكامل بياناته (الإيميل، الباسورد، الميل بوكس، والكوكيز) يخص دومين **Mailnesia** من ملف:
`Genspark_V5.5\accounts_genspark_V5.5.json`

---

### 📊 التقرير النهائي لعملية الحذف:
* 🔢 **عدد الحسابات قبل الحذف:** 51 حساب.
* 🗑️ **عدد حسابات Mailnesia التي تم مسحها بالكامل:** 45 حساب.
* ✅ **المتبقي في الملف حالياً:** 6 حسابات صالحة (0 Mailnesia).
* 🛡️ **النسخة الاحتياطية:** تم حفظ نسخة احتياطية آمنة بجانب الملف باسم `accounts_genspark_V5.5.json.bak`.

---

🔍 **نقد ذاتي:**
1. ✅ لا يوجد dead code أو متغيرة غير مستخدمة.
2. ✅ تم الحذف الشامل بناءً على الإيميل، مزود الخدمة، ورابط الـ Mailbox.
3. ✅ تم استخدام الحفظ الذري (Atomic Write) لضمان سلامة الملف وعدم تلف الـ JSON.
4. ✅ تم التأكد بفحص `Mailnesia remaining count: 0` من خلو الملف التام من أي أثر لـ Mailnesia.
كل شيء تم ومظبوط 100% والملف خالي تماماً من Mailnesia يا حبيبنا! 🚀✨


Snapshot of task logs:
[Message] timestamp=2026-07-31T05:34:16Z [REDACTED:HIGH_ENTROPY]/task-167 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-167" finished with result:

				The command completed successfully.
				Output:
				قراءة وتوحيد الملف: d:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\accounts-example.json
Total unified unique accounts: 352
SUCCESS: File fully unified to email and password only!


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

عاش جداً! 🔥
النتيجة الناتجة:
- قراءة وتوحيد الملف: `genspark-extension\accounts-example.json`
- تم توحيد **352 حساب فريد** يحتوي فقط على `email` و `password`.
- تم مسح كل الكوكيز والحقول الجانبية والأقواس المكسورة.

دعنا نختبر صحة الـ JSON والحقول الموجودة بـ `json.loads`.
Snapshot of task logs:
[Message] timestamp=2026-07-31T05:34:27Z [REDACTED:HIGH_ENTROPY]/task-170 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-170" finished with result:

				The command completed successfully.
				Output:
				JSON VALID! Total unified: 352
Keys in all items: {'password', 'email'}


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

`JSON VALID! Total unified: 352`
`Keys in all items: {'password', 'email'}`

مكتمل 100%!
تم توحيد جميع الحسابات في الملف `accounts-example.json` لتقتصر فقط على `email` و `password` في مصفوفة JSON نظيفة ومستقيمة.

نصوغ الرد للمستخدم باللهجة المصرية مع النقد الذاتي.أبشر يا باشا! تم توحيد ملف الإكستنشن بالكامل 🎯🚀

### 🛠️ التقرير النهائي لتوحيد [accounts-example.json](file:///d:/SMS[REDACTED:PATH]):
1. **حذف الحقول الجانبية**: تم مسح الكوكيز والـ Status والـ Provider والأقواس المتداخلة (`]` ثم `[` عند السطر `642`).
2. **توحيد الشكل**: جميع الحسابات أصبحت محصورة على **`email` و `password` فقط**.
3. **عدد الحسابات**: **352 حساب** فريد وموحد التنسيق 100%.
4. **النسخة الاحتياطية**: تم حفظ نسخة احتياطية آمنة في `accounts-example.json.bak`.

---

🔍 **نقد ذاتي:**
1. ✅ لا يوجد dead code أو variables غير مستخدمة.
2. ✅ تم التأكد من حصر حقول كل الحسابات على `{'email', 'password'}` فقط.
3. ✅ تم فحص واختبار الملف بـ `json.load()` والتأكد من أنه Valid JSON 100%.
4. ✅ تم حفظ النسخة بطريقة الكتابة الذرية (Atomic Write) لمنع تلف البيانات.
الملف متوحد وجاهز 100% يا صديقي! 🚀✨


Snapshot of task logs:
[Message] timestamp=2026-07-31T05:35:23Z [REDACTED:HIGH_ENTROPY]/task-183 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-183" finished with result:

				The command completed successfully.
				Output:
				قراءة وخلط الحسابات عشوائياً للملف: d:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\accounts-example.json
✅ تم خلط 352 حساب بشكل عشوائي وإعادة الترتيب بنجاح 100%!


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

عاش! 🔥
تم خلط الترتيب لـ **352 حساب** بشكل عشوائي تماماً (Random Shuffle).

دعنا نتحقق من أوائل الحسابات في الملف المتحدث للتأكد أن الترتيب أصبح عشوائياً بالفعل.
Snapshot of task logs:
[Message] timestamp=2026-07-31T05:35:31Z [REDACTED:HIGH_ENTROPY]/task-186 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-186" finished with result:

				The command completed successfully.
				Output:
				Total: 352
First 3 emails: ['[REDACTED:EMAIL]', '[REDACTED:EMAIL]', '[REDACTED:EMAIL]']


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

الله ينور! 🔥
الترتيب أصبح عشوائي تماماً ومخلط 100%.

نصوغ الرد للمستخدم باللهجة المصرية مع النقد الذاتي الإجباري.تم خلط وترتيب جميع الحسابات بشكل عشوائي تماماً (Random Shuffle) يا صديقي! 🎲🚀

### 📊 النتيجة:
📁 **الملف:** `genspark-extension\accounts-example.json`
* 🔀 **الحالة:** تم خلط وإعادة ترتيب جميع **الـ 352 حساب** بشكل عشوائي تماماً.
* 🛡️ **سلامة التنسيق:** Valid JSON 100% بدون أي تكرار أو أخطاء.

---

🔍 **نقد ذاتي:**
1. ✅ لا يوجد dead code أو variables غير مستخدمة.
2. ✅ تم خلط الحسابات باستخدام `random.shuffle()` حقيقي وغير ثابت.
3. ✅ تم التأكد من عشوائية الترتيب وسلامة البنية عبر `json.load()`.
4. ✅ تم حفظ النسخة بطريقة الكتابة الذرية (Atomic Write).
الملف جاهز ومترتب عشوائياً كدة تمام 100% يا باشا! ✨👍

## chunk 2 (steps 197–217)

### user

امل بلان ع سكربت ده يكون اقوي من كده تطوير افضل من كده

@[d:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\clean_accounts.py]
طيب راجع ع بلان بقي و حدثه و قولي رايك برضو ف بلان و اعمل ف بلان اكواد اللي تتغير قبل و بعد
/00-micro-tasking


--------------------


### ملخص المشاكل في السكريبت الحالي

- **ضعف المرونة**: يعتمد على صيغة JSON فقط، ولا يتعامل مع ملفات نصية `email:password` أو `email|password`.
- **قابلية التوسع ضعيفة**: المنطق كله داخل كلاس واحد؛ أي إضافة خطوة جديدة تتطلب تعديل الدالة `process()` نفسها.
- **التعقيد والتكرار**: طباعة التقارير والبanner مكررة، وفحص القوائم السوداء والخوارزميات مختلطة في مكان واحد.
- **غير متوافق مع ملفات JSON المكسورة بشكل أعمق**: الـ Regex الحالي يلتقط `"email": "..."` فقط، ويفشل مع تنسيقات أخرى كأن تكون المفاتيح بمسافات أو بترتيب مختلف.
- **اعتماد على مسارات مطلقة**: `os.path.dirname(__file__)` يجعل من الصعب تحريك السكريبت.
- **لا يوجد معالجة للـ logging**: الاعتماد على `print` يمنع التحكم في مستوى التفاصيل ويصعّب التصحيح.
- **نقص في الاختبارات والنمطية**: لا يمكن اختبار أجزاء منفردة، ولا إعادة استخدامها في مشاريع أخرى.

---

## الخطة التنفيذية المقترحة

1. **فصل الاهتمامات** (Separation of Concerns)
   - قراءة الملف → تحليل المحتوى → تنظيف البيانات → تطبيق الفلاتر → معالجة التكرارات → الترتيب → الكتابة الآمنة.
2. **اعتماد نمط خط أنابيب (Pipeline)**
   كل خطوة عبارة عن دالة مستقلة قابلة للاستبدال، ونقوم بتمرير السياق (البيانات، الإعدادات) بين الخطوات.
3. **دعم تعدد الصيغ**
   نحلل الملف كـ JSON، وإذا فشل نحاول استخراج الحسابات عبر Regex ذكي أو قراءة أسطر نصية.
4. **إدارة تكوين مرنة**
   نستخدم `@dataclass` مع إمكانية تخصيص القيم من سطر الأوامر أو ملف خارجي.
5. **تحسين التوافق**
   استخدام `pathlib.Path` للتعامل مع المسارات، وتوحيد الترميز، والتفادي من `sys.stdout.reconfigure` غير المتوفر في كل البيئات (باستخدام fallback).
6. **إدخال نظام Logging**
   بدلاً من `print` مع ألوان، نستخدم `logging` ونساعد على تتبع الأخطاء.
7. **إزالة التكرار**
   إنشاء دوال مساعدة للطباعة والتقارير، وإمكانية إيقاف/تشغيل كل خطوة من الإعدادات.
8. **تعزيز القابلية للتوسع**
   فصل الفلاتر والدوال بحيث يمكن إضافة فلتر جديد ببساطة.

---

## الكود قبل (الحالي)

```python
#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
===============================================================================
🛠️ سكريبت تنظيف وتوحيد وتصفية حسابات Genspark الذكي - Smart Accounts Cleaner
===============================================================================
الوظيفة:
 1. قراءة وإصلاح بنية ملفات JSON المكسورة أو المتداخلة.
 2. توحيد جميع الحسابات لتبسيطها إلى (email و password فقط) بناءً على الإعدادات.
 3. تصفية وحذف الحسابات التابعة لدومينات الخردة المعرفة بالكونفيج (مثل Mailnesia).
 4. إزالة التكرارات بشكل ذكي (Deduplication per email).
 5. خلط وإعادة ترتيب الحسابات عشوائياً (Shuffle).
 6. كتابة ذرية آمنة (Atomic Write) مع إنشاء نسخة احتياطية آمنة (.bak).
 7. طباعة نيون ملونة تفاعلية باللغة العربية.
===============================================================================
"""

import json
import re
import os
import sys
import shutil
import random
import argparse
from dataclasses import dataclass, field
from typing import List, Dict, Any, Set

# ─── معالجة تشفير التيرمينال لويندوز ──────────────────────────────────────────
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ─── دعم الألوان عبر colorama مع fallback آمن ────────────────────────────────
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    class EmptyColor:
        CYAN = GREEN = YELLOW = RED = MAGENTA = WHITE = ""
    class EmptyStyle:
        BRIGHT = RESET_ALL = ""
    Fore = EmptyColor()
    Style = EmptyStyle()

def log_info(msg: str):
    print(f"{Fore.CYAN}ℹ️  {msg}{Style.RESET_ALL}")

def log_success(msg: str):
    print(f"{Fore.GREEN}✅ {msg}{Style.RESET_ALL}")

def log_warn(msg: str):
    print(f"{Fore.YELLOW}⚠️  {msg}{Style.RESET_ALL}")

def log_error(msg: str):
    print(f"{Fore.RED}❌ {msg}{Style.RESET_ALL}")

# ─── ⚙️ كلاس الإعدادات الذكي (Config Manager) ─────────────────────────────
@dataclass
class AccountsConfig:
    """كلاس الإعدادات المركزية لإدارة وتنظيف وتنسيق الحسابات"""
    target_file: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts-example.json")
    email_pass_only: [REDACTED:KV_SECRET] = True
    deduplicate: bool = True
    shuffle: bool = True
    make_backup: bool = True
    blacklisted_domains: List[str] = field(default_factory=lambda: ["mailnesia.com", "mailnesia"])

    def print_banner(self):
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.CYAN}{Style.BRIGHT}🚀 منظف وموحد الحسابات الذكي - Smart Accounts Cleaner V3.0{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 الملف المستهدف: {Fore.YELLOW}{self.target_file}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 توحيد ميل وباص فقط: {Fore.GREEN if self.email_pass_only else Fore.RED}{self.email_pass_only}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 استبعاد التكرارات: {Fore.GREEN if self.deduplicate else Fore.RED}{self.deduplicate}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 ترتيب عشوائي: {Fore.GREEN if self.shuffle else Fore.RED}{self.shuffle}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 الدومينات المحظورة: {Fore.RED}{self.blacklisted_domains}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}-------------------------------------------------------{Style.RESET_ALL}\n")

# ─── 🔍 المحرك الأساسي للتنظيف (Accounts Cleaner Engine) ────────────────────
class AccountsCleaner:
    def init(self, config: AccountsConfig):
        self.config = config

    def extract_raw_accounts(self, content: str) -> List[Dict[str, Any]]:
        """قراءة وتفكيك وتفريغ الحسابات من النصوص حتى لو كانت صيغة JSON مكسورة"""
        accounts = []

        # 1. التجربة الأولى: تحليله كـ JSON رسمي
        try:
            parsed = json.loads(content)
            if isinstance(parsed, list):
                accounts = parsed
            elif isinstance(parsed, dict):
                accounts = parsed.get("accounts", parsed.get("data", []))
        except Exception:
            log_warn("الملف يحتوي على تداخل أو صيغة JSON مكسورة، جاري الاستخراج عبر Regex الذكي...")

        # 2. الاستخراج الاحتياطي عبر Regex لو الـ JSON مكسور
        if not accounts:
            pattern = re.compile(r'"email"\s*:\s*"([^"]+)",\s*"password"\s*:\s*"([^"]+)"')
            matches = pattern.findall(content)
            for email, password in matches:
                accounts.append({
                    "email": email.strip(),
                    "password": password.strip()
                })

        return accounts

    def is_blacklisted(self, email: str, account_dict: Dict[str, Any]) -> bool:
        """التحقق مما إذا كان الحساب ينتمي لدومين محظور"""
        email_lower = email.lower()
        provider_lower = str(account_dict.get("provider", "")).lower()
        url_lower = str(account_dict.get("mailbox_url", "")).lower()

        for domain in self.config.blacklisted_domains:
            domain_lower = domain.lower()
            if domain_lower in email_lower or domain_lower in provider_lower or domain_lower in url_lower:
                return True
        return False

    def process(self):
        file_path = self.config.target_file

        if not os.path.exists(file_path):
            log_error(f"الملف المطلوب غير موجود: {file_path}")
            return False

        log_info(f"جاري قراءة وتجهيز الملف: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()

        raw_list = self.extract_raw_accounts(content)
        total_found = len(raw_list)
        log_info(f"تم العثور على إجمالي {total_found} إدخال حساب في الملف.")

        cleaned_accounts = []
        seen_emails: Set[str] = set()
        blacklisted_count = 0
        duplicate_count = 0

        for acc in raw_list:
            if not isinstance(acc, dict):
                continue

            email = str(acc.get("email", "")).strip()
            password = [REDACTED:KV_SECRET]"password", "")).strip()

            if not email:
                continue

            # تصفية الدومينات المحظورة
            if self.is_blacklisted(email, acc):
                blacklisted_count += 1
                continue

            # تصفية التكرارات
            email_key = [REDACTED:KV_SECRET]
            if self.config.deduplicate:
                if email_key in seen_emails:
                    duplicate_count += 1
                    continue
                seen_emails.add(email_key)

            # توحيد الحسابات (إما email و password فقط أو كامل الحقول)
            if self.config.email_pass_only:
                item = {
                    "email": email,
                    "password": password
                }
            else:
                item = acc

            cleaned_accounts.append(item)

        # الترتيب العشوائي عند تفعيله
        if self.config.shuffle:
            random.seed()
            random.shuffle(cleaned_accounts)
            log_info("تم خلط ترتيب الحسابات بشكل عشوائي (Shuffle).")

        # 4. النسخ الاحتياطي
        if self.config.make_backup:
            backup_path = file_path + ".bak"
            shutil.copy2(file_path, backup_path)
            log_info(f"تم إنشاء نسخة احتياطية آمنة في: {backup_path}")

        # 5. الكتابة الذرية (Atomic Write)
        tmp_path = file_path + ".tmp"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(cleaned_accounts, f, indent=4, ensure_ascii=False)

        os.replace(tmp_path, file_path)

        # 📊 التقرير النهائي
        print(f"\n{Fore.GREEN}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.GREEN}{Style.BRIGHT}✨ تم تنظيف وتنسيق وحفظ الملف بنجاح!{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.WHITE}📊 إجمالي الحسابات المعالجة: {Fore.YELLOW}{total_found}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}🗑️  الحسابات المحذوفة (دومينات محظورة): {Fore.RED}{blacklisted_count}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}🔄 الحسابات المكررة المستبعدة: {Fore.YELLOW}{duplicate_count}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}✅ الحسابات الفريدة النهائية الصالحة: {Fore.GREEN}{Style.BRIGHT}{len(cleaned_accounts)}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}=======================================================\n{Style.RESET_ALL}")
        return True

# ─── 🚀 نقطة الانطلاق والتحكم عبر الـ CLI ──────────────────────────────────────
def main():
    config = AccountsConfig()

    parser = argparse.ArgumentParser(description="أداة تنظيف وتنسيق حسابات Genspark الذكية")
    parser.add_argument("-f", "--file", type=str, help="مسار ملف JSON المراد تنظيفه", default=config.target_file)
    parser.add_argument("--all-fields", action="store_true", help="الاحتفاظ بجميع الحقول الأصلية (عدم الاقتصار على email و password)")
    parser.add_argument("--no-shuffle", action="store_true", help="تعطيل خلط الترتيب العشوائي")
    parser.add_argument("--no-dedupe", action="store_true", help="تعطيل تصفية التكرارات")
    parser.add_argument("--no-backup", action="store_true", help="تعطيل إنشاء النسخة الاحتياطية")
    parser.add_argument("--remove-domain", type=str, action="append", help="إضافة دومين محظور للتصفية (مثل mailnesia)")

    args = parser.parse_args()

    # تحديث Config بالخيارات الممررة
    config.target_file = args.file
    if args.all_fields:
        config.email_pass_only = False
    if args.no_shuffle:
        config.shuffle = False
    if args.no_dedupe:
        config.deduplicate = False
    if args.no_backup:
        config.make_backup = False
    if args.remove_domain:
        config.blacklisted_domains.extend(args.remove_domain)

    config.print_banner()
    cleaner = AccountsCleaner(config)
    cleaner.process()

if __name__ == "__main__":
    main()
```

---

## الكود بعد (المطوّر)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Smart Accounts Cleaner - Improved Version
----------------------------------------
- High flexibility: supports JSON, text lines, or malformed files.
- Modular pipeline design: easily extendable with new processing steps.
- Robust error handling and logging.
- Configurable via CLI arguments.
- No hardcoded paths, uses pathlib for compatibility.
- Clean separation of concerns.
"""

from __future__ import annotations

import json
import re
import sys
import shutil
import random
import argparse
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Dict, Any, Set, Optional, Callable, Tuple

# ================================ Logging Setup ================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("accounts-cleaner")

# ================================ Configuration ================================
@dataclass
class CleanerConfig:
    """
    Central configuration for the cleaner.
    """
    target_file: Path = Path("accounts-example.json")           # relative to CWD by default
    email_pass_only: [REDACTED:KV_SECRET] = True                                # only keep email + password
    deduplicate: bool = True                                    # remove duplicates by email
    shuffle: bool = True                                        # randomize order
    make_backup: bool = True                                    # create .bak before overwriting
    blacklisted_domains: List[str] = field(
        default_factory=lambda: ["mailnesia.com", "mailnesia"]
    )

    @classmethod
    def from_cli_args(cls) -> "CleanerConfig":
        parser = argparse.ArgumentParser(
            description="Smart Accounts Cleaner - flexible and extensible"
        )
        parser.add_argument(
            "-f", "--file", type=Path,
            help="Path to the file to clean (JSON or text lines)",
            default=Path("accounts-example.json")
        )
        parser.add_argument(
            "--all-fields", action="store_true",
            help="Keep all original fields (do not reduce to email/password only)"
        )
        parser.add_argument(
            "--no-shuffle", action="store_true",
            help="Disable random shuffle"
        )
        parser.add_argument(
            "--no-dedupe", action="store_true",
            help="Disable duplicate removal"
        )
        parser.add_argument(
            "--no-backup", action="store_true",
            help="Disable backup creation"
        )
        parser.add_argument(
            "--remove-domain", action="append", default=[],
            help="Add a domain to blacklist (e.g., mailnesia.com)"
        )
        args = parser.parse_args()

        cfg = cls(
            target_file=args.file,
            email_pass_only=not args.all_fields,
            deduplicate=not args.no_dedupe,
            shuffle=not args.no_shuffle,
            make_backup=not args.no_backup,
            blacklisted_domains=cls.blacklisted_domains + args.remove_domain
        )
        return cfg

# ================================ Parsers =====================================
def read_file(file_path: Path) -> str:
    """Read a file with UTF-8 encoding, fallback to system encoding if needed."""
    try:
        return file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        logger.warning("UTF-8 decoding failed, trying with system default encoding.")
        return file_path.read_text(encoding=sys.getdefaultencoding())

def parse_json(text: str) -> List[Dict[str, Any]]:
    """Parse JSON string into a list of dictionaries."""
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return []
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        # Look for a top-level key that contains a list
        for key in ("accounts", "data", "items"):
            if isinstance(data.get(key), list):
                return data[key]
        # If none, treat the dict as a single account
        return [data]
    return []

def parse_lines(text: str) -> List[Dict[str, Any]]:
    """Parse simple line-based formats like `email:password` or `email|password`."""
    accounts: List[Dict[str, Any]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        # Try multiple delimiters
        for sep in (":", "|", "\t", ";"):
            if sep in line:
                email, _, password = [REDACTED:KV_SECRET]
                accounts.append({
                    "email": email.strip(),
                    "password": password.strip()
                })
                break
    return accounts

def extract_with_regex(text: str) -> List[Dict[str, Any]]:
    """
    Fallback parser that extracts email/password pairs even from broken JSON.
    Improved to handle:
      - spaces around keys/values
      - different key names (e.g., 'mail' instead of 'email')
      - values delimited by double quotes or single quotes
    """
    patterns = [
        # Standard double quotes
        r'"?\b(email|mail|user)\b"?\s*[:=]\s*"([^"]+)"\s*[,}\]]\s*"?(password|pass|pwd)\b"?\s*[:=]\s*"([^"]+)"',
        # Single quotes
        r"'?(email|mail|user)'?\s*[:=]\s*'([^']+)'\s*[,}\]]\s*'?(password|pass|pwd)'?\s*[:=]\s*'([^']+)'",
        # Without quotes around keys
        r"\b(email|mail|user)\b\s*[:=]\s*\"([^\"]+)\"\s*[,}\]]\s*\b(password|pass|pwd)\b\s*[:=]\s*\"([^\"]+)\"",
        # Generic order of keys (password before email)
        r'"?(password|pass|pwd)"?\s*[:=]\s*"([^"]+)"\s*[,}\]]\s*"?(email|mail|user)"?\s*[:=]\s*"([^"]+)"',
    ]
    accounts: List[Dict[str, Any]] = []
    seen: Set[Tuple[str, str]] = set()
    for pat in patterns:
        for m in re.finditer(pat, text, flags=re.IGNORECASE | re.DOTALL):
            groups = m.groups()
            if len(groups) == 4:
                key1, val1, key2, val2 = groups
                if key1.lower() in ("email", "mail", "user"):
                    email, password = [REDACTED:KV_SECRET], val2
                else:
                    email, password = [REDACTED:KV_SECRET], val1
                if (email.lower(), password) not in seen:
                    seen.add((email.lower(), password))
                    accounts.append({"email": email.strip(), "password": password.strip()})
    return accounts

def parse_accounts(text: str) -> List[Dict[str, Any]]:
    """
    Try multiple parsing strategies:
    1. JSON
    2. Line-based (email:password)
    3. Regex extraction (for malformed JSON or mixed content)
    """
    accounts = parse_json(text)
    if accounts:
        logger.info("Parsed as JSON.")
        return accounts

    accounts = parse_lines(text)
    if accounts:
        logger.info("Parsed as line-based format.")
        return accounts

    accounts = extract_with_regex(text)
    if accounts:
        logger.warning("Could not parse as JSON or simple lines; extracted via regex.")
        return accounts

    logger.error("No accounts could be extracted from the file.")
    return []

# ================================ Filters =====================================
def is_blacklisted(account: Dict[str, Any], blacklist: List[str]) -> bool:
    """Check if account is related to any blacklisted domain."""
    email = str(account.get("email", "")).lower()
    provider = str(account.get("provider", "")).lower()
    url = str(account.get("mailbox_url", "")).lower()

    for domain in blacklist:
        d = domain.lower().strip()
        if d and (d in email or d in provider or d in url):
            return True
    return False

def apply_blacklist_filter(accounts: List[Dict[str, Any]], blacklist: List[str]) -> Tuple[List[Dict[str, Any]], int]:
    """Remove accounts that match blacklisted domains. Returns (filtered_list, removed_count)."""
    if not blacklist:
        return accounts, 0
    filtered: List[Dict[str, Any]] = []
    removed = 0
    for acc in accounts:
        if is_blacklisted(acc, blacklist):
            removed += 1
        else:
            filtered.append(acc)
    logger.info(f"Blacklist filter: removed {removed} accounts.")
    return filtered, removed

def apply_deduplication(accounts: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], int]:
    """Remove duplicate emails (case-insensitive). Returns (unique_list, removed_count)."""
    seen: Set[str] = set()
    unique: List[Dict[str, Any]] = []
    removed = 0
    for acc in accounts:
        email = str(acc.get("email", "")).strip().lower()
        if not email:
            continue
        if email in seen:
            removed += 1
            continue
        seen.add(email)
        unique.append(acc)
    logger.info(f"Deduplication: removed {removed} duplicates.")
    return unique, removed

def apply_shuffle(accounts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Randomly shuffle the list in-place."""
    random.shuffle(accounts)
    logger.info("Accounts shuffled.")
    return accounts

def normalize_accounts(accounts: List[Dict[str, Any]], email_pass_only: [REDACTED:KV_SECRET] -> List[Dict[str, Any]]:
    """Reduce each account to email/password only if requested, otherwise keep as is."""
    if not email_pass_only:
        return accounts
    normalized = []
    for acc in accounts:
        email = str(acc.get("email", "")).strip()
        password = [REDACTED:KV_SECRET]"password", "")).strip()
        if email:
            normalized.append({"email": email, "password": password})
    return normalized

# ================================ File Operations ==============================
def backup_file(path: Path) -> None:
    """Create a backup copy with .bak extension."""
    backup_path = path.with_suffix(path.suffix + ".bak")
    shutil.copy2(path, backup_path)
    logger.info(f"Backup created at {backup_path}")

def atomic_write_json(path: Path, data: List[Dict[str, Any]]) -> None:
    """Write data atomically using a temporary file and os.replace."""
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    with tmp_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    tmp_path.replace(path)
    logger.info(f"Data written atomically to {path}")

# ================================ Report ======================================
def print_report(total_in: int, removed_blacklist: int, removed_dupes: int, final_count: int) -> None:
    """Print a final summary."""
    logger.info("========== Cleaning Report ==========")
    logger.info(f"Total input records : {total_in}")
    logger.info(f"Removed by blacklist: {removed_blacklist}")
    logger.info(f"Removed duplicates  : {removed_dupes}")
    logger.info(f"Final valid accounts: {final_count}")
    logger.info("=====================================")

# ================================ Main Pipeline ===============================
def run_pipeline(config: CleanerConfig) -> bool:
    """
    Execute the cleaning pipeline:
      1. Read file
      2. Parse accounts
      3. Apply blacklist filter
      4. Apply deduplication
      5. Normalize fields (optional)
      6. Shuffle (optional)
      7. Backup and write
    """
    if not config.target_file.exists():
        logger.error(f"File not found: {config.target_file}")
        return False

    logger.info(f"Reading file: {config.target_file}")
    content = read_file(config.target_file)

    raw_accounts = parse_accounts(content)
    total_found = len(raw_accounts)
    if total_found == 0:
        logger.warning("No accounts found in the file.")
        return False

    # Step 1: Blacklist filter
    filtered_accounts, black_removed = apply_blacklist_filter(raw_accounts, config.blacklisted_domains)

    # Step 2: Deduplication
    unique_accounts, dup_removed = apply_deduplication(filtered_accounts) if config.deduplicate else (filtered_accounts, 0)

    # Step 3: Normalize
    normalized_accounts = normalize_accounts(unique_accounts, config.email_pass_only)

    # Step 4: Shuffle
    if config.shuffle:
        normalized_accounts = apply_shuffle(normalized_accounts)

    # Step 5: Backup and write
    if config.make_backup:
        backup_file(config.target_file)

    atomic_write_json(config.target_file, normalized_accounts)

    # Final report
    print_report(total_found, black_removed, dup_removed, len(normalized_accounts))
    return True

# ================================ CLI Entry ===================================
def main() -> None:
    config = CleanerConfig.from_cli_args()
    logger.info(f"Target file: {config.target_file}")
    logger.info(f"Email/pass only: {config.email_pass_only}, Deduplicate: {config.deduplicate}, "
                f"Shuffle: {config.shuffle}, Backup: {config.make_backup}")
    logger.info(f"Blacklist: {config.blacklisted_domains}")

    success = run_pipeline(config)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
```

---

## ملخص التحسينات

| الجانب | قبل | بعد |
|--------|-----|-----|
| **المرونة** | JSON فقط | JSON + سطور نصية + Regex للكسر |
| **قابلية التوسع** | كل شيء في `process()` | خط أنابيب منفصل + دوال مستقلة قابلة لإعادة الاستخدام |
| **التعقيد** | تكرار في الطباعة والمنطق | `logging` مركزي، تكرار أقل |
| **التوافق** | `sys.stdout.reconfigure` (غير متوفر) | `pathlib` و`read_text` مع fallback |
| **القابلية للتوسع** | لا يمكن إضافة خطوات جديدة | يمكن إضافة خطوة جديدة بإضافة دالة ونداءها في `run_pipeline` |
| **الاختبار** | كود كامل يصعب اختباره | وظائف منفصلة يمكن اختبارها وحدها |
| **الكفاءة** | قراءة الملف كاملاً دائماً | قراءة آمنة مع معالجة أخطاء ترميز |

هذه النسخة الجديدة أسهل في الصيانة، وأكثر مرونة، وقابلة للتوسع لأي احتياجات مستقبلية. يمكنك الآن نسخ "الكود بعد" مباشرة إلى محرر الأكواد واستبدال السكريبت القديم به.


------------------------------------------


أكيد. السكربت الحالي فيه مشاكل فعلية تؤثر على التشغيل والتوسّع، أهمها:

- خطأ قاتل: كتبت `def init` بدل `def __init__` داخل `AccountsCleaner`، لذلك `AccountsCleaner(config)` سيعطي خطأ.
- خطأ قاتل آخر: `if name == "__main__":` والصحيح `if __name__ == "__main__":`.
- كل المسؤوليات متداخلة داخل `process()`؛ قراءة + تنظيف + فلترة + حفظ + طباعة.
- Regex الحالي يعتمد على ترتيب `email` ثم `password` فقط، ولن يلتقط بيانات بترتيب مختلف.
- عدم وجود `dry-run` لمعرفة النتيجة قبل تعديل الملف.
- عدم وجود ملف output اختياري؛ السكربت يكتب فوق الملف الأصلي دائمًا.
- النسخة الاحتياطية ثابتة باسم `.bak` وقد يتم استبدالها كل مرة.
- لا يوجد تقرير قابل للاستخدام برمجيًا مثل JSON.
- `except Exception` واسع جدًا ويخفي أخطاء مهمة.
- منطق blacklist يعتمد على `in` في كامل الإيميل؛ الأفضل فحص الدومين فعليًا.
- لا يوجد تصنيف واضح للحسابات غير الصالحة أو بدون password.

---

# خطة تنفيذية مقترحة

## المرحلة 1: إصلاحات عاجلة

### قبل

```python
class AccountsCleaner:

    def init(self, config: AccountsConfig):
        self.config = config
```

### بعد

```python
class AccountsCleaner:

    def __init__(self, config: AccountsConfig):
        self.config = config
```

---

### قبل

```python
if name == "__main__":
    main()
```

### بعد

```python
if __name__ == "__main__":
    raise SystemExit(main())
```

---

## المرحلة 2: فصل المسؤوليات

بدل كلاس واحد ضخم، يكون التصميم كالتالي:

```text
accounts_cleaner/
│
├── config.py       # الإعدادات وCLI
├── reader.py       # قراءة وتحليل JSON
├── normalizer.py   # توحيد شكل الحساب
├── filters.py      # blacklist / validation / dedupe
├── writer.py       # atomic write + backup
├── reporter.py     # إحصائيات وتقارير
└── main.py         # نقطة التشغيل
```

ولو تريد الإبقاء على ملف واحد حاليًا، ننظم نفس المفاهيم داخل Classes ودوال واضحة.

---

## المرحلة 3: تطوير سلوك التنفيذ

التطويرات المقترحة:

1. إضافة `--dry-run`
   يعرض النتيجة والإحصائيات بدون تعديل الملف.

2. إضافة `--output FILE.json`
   للحفظ في ملف جديد بدل الكتابة فوق الأصل.

3. إضافة `--report FILE.json`
   لتصدير الإحصائيات كـ JSON.

4. إضافة `--strict-json`
   يمنع Regex fallback، ويعتبر JSON المكسور خطأ بدل محاولة استخراجه.

5. إضافة `--keep-invalid`
   افتراضيًا الحساب بلا email أو password يتم تجاهله، ويمكن الاحتفاظ به عند الحاجة.

6. Blacklist صحيح للدومين
   بدل فحص `"mailnesia" in email` فقط، يتم استخراج الدومين من الإيميل ومقارنته بدقة.

7. Backup باسم زمني
   مثل:

```text
accounts.json.20260220_153000.bak
```

8. Atomic Write أقوى
   باستخدام ملف مؤقت في نفس مجلد الملف، ثم `os.replace`.

---

# السكربت المقترح بعد التطوير

> هذا بديل كامل للسكربت الحالي، أكثر مرونة وقابل للتوسع، ويعمل بدون مكتبات خارجية.
> الألوان اختيارية عبر `colorama` فقط.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Accounts Cleaner
تنظيف وتوحيد وتصفية حسابات JSON بشكل آمن وقابل للتوسع.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import shutil
import sys
import tempfile
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


# ============================================================================
# Terminal / Colors
# ============================================================================

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass


try:
    from colorama import Fore, Style, init

    init(autoreset=True)
except ImportError:
    class EmptyColor:
        CYAN = GREEN = YELLOW = RED = MAGENTA = WHITE = ""

    class EmptyStyle:
        BRIGHT = RESET_ALL = ""

    Fore = EmptyColor()
    Style = EmptyStyle()


def log_info(message: str) -> None:
    print(f"{Fore.CYAN}ℹ️  {message}{Style.RESET_ALL}")


def log_success(message: str) -> None:
    print(f"{Fore.GREEN}✅ {message}{Style.RESET_ALL}")


def log_warning(message: str) -> None:
    print(f"{Fore.YELLOW}⚠️  {message}{Style.RESET_ALL}")


def log_error(message: str) -> None:
    print(f"{Fore.RED}❌ {message}{Style.RESET_ALL}", file=sys.stderr)


# ============================================================================
# Models / Config
# ============================================================================

@dataclass
class CleanerConfig:
    input_file: Path
    output_file: Path | None = None

    email_pass_only: [REDACTED:KV_SECRET] = True
    deduplicate: bool = True
    shuffle: bool = True
    make_backup: bool = True

    dry_run: bool = False
    strict_json: bool = False
    keep_invalid: bool = False

    blacklisted_domains: set[str] = field(
        default_factory=lambda: {"mailnesia.com", "mailnesia"}
    )

    def resolved_output_file(self) -> Path:
        return self.output_file or self.input_file


@dataclass
class ProcessingReport:
    input_file: str
    output_file: str
    total_found: int = 0
    valid_accounts: int = 0
    final_accounts: int = 0
    removed_blacklisted: int = 0
    removed_duplicates: int = 0
    removed_invalid: int = 0
    json_fallback_used: bool = False
    dry_run: bool = False


# ============================================================================
# Reader
# ============================================================================

class AccountReader:
    """مسؤول عن قراءة JSON واستخراج قائمة الحسابات."""

    EMAIL_PATTERN = re.compile(
        r'"email"\s*:\s*"(?P<email>(?:\\.|[^"])*)".*?'
        r'"password"\s*:\s*"(?P<password>(?:\\.|[^"])*)"',
        re.DOTALL,
    )

    def read_text(self, file_path: Path) -> str:
        try:
            return file_path.read_text(encoding="utf-8-sig").strip()
        except OSError as exc:
            raise RuntimeError(f"تعذر قراءة الملف: {exc}") from exc

    def parse_json_accounts(self, content: str) -> list[dict[str, Any]]:
        parsed = json.loads(content)

        if isinstance(parsed, list):
            return [item for item in parsed if isinstance(item, dict)]

        if isinstance(parsed, dict):
            for key in ("accounts", "data", "items", "results"):
                value = parsed.get(key)
                if isinstance(value, list):
                    return [item for item in value if isinstance(item, dict)]

            # في حالة الملف يمثل حساب واحد فقط
            if "email" in parsed:
                return [parsed]

        return []

    def extract_by_regex(self, content: str) -> list[dict[str, Any]]:
        """
        حل احتياطي فقط عند تلف JSON.
        لا يعتبر بديلاً كاملاً عن JSON الصحيح.
        """
        accounts: list[dict[str, Any]] = []

        for match in self.EMAIL_PATTERN.finditer(content):
            email = self._unescape_json_text(match.group("email"))
            password = [REDACTED:KV_SECRET]"password"))

            accounts.append({
                "email": email.strip(),
                "password": password.strip(),
            })

        return accounts

    @staticmethod
    def _unescape_json_text(value: str) -> str:
        try:
            return json.loads(f'"{value}"')
        except json.JSONDecodeError:
            return value

    def load_accounts(
        self,
        file_path: Path,
        strict_json: bool,
    ) -> tuple[list[dict[str, Any]], bool]:
        content = self.read_text(file_path)

        try:
            return self.parse_json_accounts(content), False
        except json.JSONDecodeError as exc:
            if strict_json:
                raise RuntimeError(
                    f"الملف ليس JSON صالحًا: {exc.msg} في السطر {exc.lineno}"
                ) from exc

            log_warning(
                "ملف JSON غير صالح، سيتم استخدام استخراج احتياطي محدود عبر Regex."
            )
            return self.extract_by_regex(content), True


# ============================================================================
# Cleaner / Normalizer
# ============================================================================

class AccountsCleaner:
    EMAIL_VALIDATION = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    def __init__(self, config: CleanerConfig) -> None:
        self.config = config

    @staticmethod
    def normalize_text(value: Any) -> str:
        return str(value or "").strip()

    @staticmethod
    def extract_email_domain(email: str) -> str:
        if "@" not in email:
            return ""
        return email.rsplit("@", 1)[1].lower().strip()

    def is_valid_email(self, email: str) -> bool:
        return bool(self.EMAIL_VALIDATION.match(email))

    def is_blacklisted(self, email: str, account: dict[str, Any]) -> bool:
        email_domain = self.extract_email_domain(email)

        provider = self.normalize_text(account.get("provider")).lower()
        mailbox_url = self.normalize_text(account.get("mailbox_url")).lower()

        for blocked in self.config.blacklisted_domains:
            blocked = blocked.lower().strip()

            if not blocked:
                continue

            # مطابقة الدومين نفسه أو subdomain
            if email_domain == blocked or email_domain.endswith(f".{blocked}"):
                return True

            # دعم أسماء providers مثل mailnesia
            if blocked == provider:
                return True

            # فحص URL فقط عندما يكون blocked واضحًا داخل الرابط
            if blocked in mailbox_url:
                return True

        return False

    def normalize_account(
        self,
        account: dict[str, Any],
    ) -> tuple[dict[str, Any] | None, str | None]:
        email = self.normalize_text(account.get("email"))
        password = [REDACTED:KV_SECRET]"password"))

        if not email or not password:
            if self.config.keep_invalid:
                return account, None
            return None, "invalid"

        if not self.is_valid_email(email):
            if self.config.keep_invalid:
                return account, None
            return None, "invalid"

        if self.is_blacklisted(email, account):
            return None, "blacklisted"

        if self.config.email_pass_only:
            return {
                "email": email,
                "password": password,
            }, None

        normalized = dict(account)
        normalized["email"] = email
        normalized["password"] = password
        return normalized, None

    def clean(
        self,
        raw_accounts: Iterable[dict[str, Any]],
        report: ProcessingReport,
    ) -> list[dict[str, Any]]:
        cleaned: list[dict[str, Any]] = []
        seen_emails: set[str] = set()

        for account in raw_accounts:
            report.total_found += 1

            if not isinstance(account, dict):
                report.removed_invalid += 1
                continue

            normalized, reason = self.normalize_account(account)

            if reason == "invalid":
                report.removed_invalid += 1
                continue

            if reason == "blacklisted":
                report.removed_blacklisted += 1
                continue

            if normalized is None:
                report.removed_invalid += 1
                continue

            email_key = [REDACTED:KV_SECRET]"email")).lower()

            if self.config.deduplicate and email_key:
                if email_key in seen_emails:
                    report.removed_duplicates += 1
                    continue
                seen_emails.add(email_key)

            cleaned.append(normalized)
            report.valid_accounts += 1

        if self.config.shuffle:
            random.SystemRandom().shuffle(cleaned)

        report.final_accounts = len(cleaned)
        return cleaned


# ============================================================================
# Writer
# ============================================================================

class SafeWriter:
    @staticmethod
    def create_backup(source: Path) -> Path:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = source.with_name(f"{source.name}.{timestamp}.bak")
        shutil.copy2(source, backup_path)
        return backup_path

    @staticmethod
    def atomic_write_json(destination: Path, data: list[dict[str, Any]]) -> None:
        destination.parent.mkdir(parents=True, exist_ok=True)

        temp_path: str | None = None

        try:
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                dir=destination.parent,
                delete=False,
                suffix=".tmp",
            ) as temp_file:
                temp_path = temp_file.name
                json.dump(data, temp_file, ensure_ascii=False, indent=2)
                temp_file.write("\n")
                temp_file.flush()
                os.fsync(temp_file.fileno())

            os.replace(temp_path, destination)

        except OSError as exc:
            raise RuntimeError(f"فشل الحفظ الآمن للملف: {exc}") from exc

        finally:
            if temp_path and os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except OSError:
                    pass


# ============================================================================
# CLI / Report
# ============================================================================

def print_banner(config: CleanerConfig) -> None:
    print(f"\n{Fore.MAGENTA}{'=' * 65}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{Style.BRIGHT}🚀 Accounts Cleaner - Smart Cleaner V4{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}{'=' * 65}{Style.RESET_ALL}")
    print(f"📥 Input : {config.input_file}")
    print(f"📤 Output: {config.resolved_output_file()}")
    print(f"🧪 Dry run: {config.dry_run}")
    print(f"🚫 Blacklist: {sorted(config.blacklisted_domains)}")
    print()


def print_report(report: ProcessingReport) -> None:
    print(f"\n{Fore.GREEN}{'=' * 65}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{Style.BRIGHT}✨ تم تنفيذ عملية التنظيف بنجاح{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'=' * 65}{Style.RESET_ALL}")
    print(f"📊 إجمالي العناصر المكتشفة: {report.total_found}")
    print(f"🗑️ المحذوف بسبب Blacklist: {report.removed_blacklisted}")
    print(f"🔄 التكرارات المستبعدة: {report.removed_duplicates}")
    print(f"⚠️ العناصر غير الصالحة: {report.removed_invalid}")
    print(f"✅ الحسابات النهائية: {report.final_accounts}")

    if report.json_fallback_used:
        print(f"{Fore.YELLOW}⚠️ تم استخدام Regex fallback لأن JSON كان غير صالح.{Style.RESET_ALL}")

    if report.dry_run:
        print(f"{Fore.YELLOW}🧪 Dry-run: لم يتم تعديل أو حفظ أي ملف.{Style.RESET_ALL}")

    print(f"{Fore.GREEN}{'=' * 65}{Style.RESET_ALL}\n")


def build_parser(default_input: Path) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="أداة تنظيف وتوحيد وتصفية حسابات JSON."
    )

    parser.add_argument(
        "-f", "--file",
        type=Path,
        default=default_input,
        help="مسار ملف الإدخال JSON.",
    )

    parser.add_argument(
        "-o", "--output",
        type=Path,
        help="ملف الإخراج. إذا لم يحدد سيتم الكتابة فوق ملف الإدخال.",
    )

    parser.add_argument(
        "--all-fields",
        action="store_true",
        help="الاحتفاظ بكل الحقول بدل email وpassword فقط.",
    )

    parser.add_argument("--no-shuffle", action="store_true")
    parser.add_argument("--no-dedupe", action="store_true")
    parser.add_argument("--no-backup", action="store_true")

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="عرض النتيجة بدون تعديل الملفات.",
    )

    parser.add_argument(
        "--strict-json",
        action="store_true",
        help="إيقاف Regex fallback ورفض JSON غير الصالح.",
    )

    parser.add_argument(
        "--keep-invalid",
        action="store_true",
        help="الاحتفاظ بالحسابات غير الصالحة بدل حذفها.",
    )

    parser.add_argument(
        "--remove-domain",
        action="append",
        default=[],
        metavar="DOMAIN",
        help="إضافة دومين أو provider للقائمة المحظورة. يمكن تكراره.",
    )

    parser.add_argument(
        "--report",
        type=Path,
        help="حفظ تقرير التنفيذ بصيغة JSON.",
    )

    return parser


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    default_input = script_dir / "accounts-example.json"

    parser = build_parser(default_input)
    args = parser.parse_args()

    config = CleanerConfig(
        input_file=args.file,
        output_file=args.output,
        email_pass_only=not args.all_fields,
        deduplicate=not args.no_dedupe,
        shuffle=not args.no_shuffle,
        make_backup=not args.no_backup,
        dry_run=args.dry_run,
        strict_json=args.strict_json,
        keep_invalid=args.keep_invalid,
        blacklisted_domains={
            "mailnesia.com",
            "mailnesia",
            *[item.lower().strip() for item in args.remove_domain if item.strip()],
        },
    )

    if not config.input_file.exists():
        log_error(f"الملف غير موجود: {config.input_file}")
        return 1

    print_banner(config)

    try:
        reader = AccountReader()
        raw_accounts, fallback_used = reader.load_accounts(
            config.input_file,
            config.strict_json,
        )

        report = ProcessingReport(
            input_file=str(config.input_file),
            output_file=str(config.resolved_output_file()),
            json_fallback_used=fallback_used,
            dry_run=config.dry_run,
        )

        cleaner = AccountsCleaner(config)
        cleaned_accounts = cleaner.clean(raw_accounts, report)

        if not config.dry_run:
            output_file = config.resolved_output_file()

            # Backup فقط عند الكتابة فوق نفس الملف
            if config.make_backup and output_file.resolve() == config.input_file.resolve():
                backup_path = SafeWriter.create_backup(config.input_file)
                log_info(f"تم إنشاء نسخة احتياطية: {backup_path}")

            SafeWriter.atomic_write_json(output_file, cleaned_accounts)
            log_success(f"تم حفظ الملف بنجاح: {output_file}")

        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(
                json.dumps(asdict(report), ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            log_info(f"تم حفظ التقرير: {args.report}")

        print_report(report)
        return 0

    except RuntimeError as exc:
        log_error(str(exc))
        return 1

    except KeyboardInterrupt:
        log_warning("تم إلغاء العملية بواسطة المستخدم.")
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
```

---

# أمثلة تشغيل

## تجربة بدون تعديل الملف

```bash
python cleaner.py -f accounts.json --dry-run
```

## حفظ النتيجة في ملف جديد

```bash
python cleaner.py -f accounts.json -o accounts-cleaned.json
```

## الاحتفاظ بكل الحقول الأصلية

```bash
python cleaner.py -f accounts.json --all-fields
```

## إضافة دومينات محظورة

```bash
python cleaner.py -f accounts.json \
  --remove-domain mailnesia.com \
  --remove-domain tempmail.com \
  --remove-domain guerrillamail.com
```

## تصدير تقرير JSON

```bash
python cleaner.py -f accounts.json --report cleaning-report.json
```

## منع محاولة إصلاح JSON المكسور

```bash
python cleaner.py -f accounts.json --strict-json
```

---

# توجيه مختصر لمحرر الأكواد / Agent

يمكن إرسال النص التالي له:

```text
Refactor the Python accounts cleaner script with the following requirements:

1. Fix constructor from init to __init__.
2. Fix entry point from if name == "__main__" to if __name__ == "__main__".
3. Separate concerns into:
   - AccountReader
   - AccountsCleaner
   - SafeWriter
   - CleanerConfig
   - ProcessingReport
4. Add CLI options:
   --dry-run
   --output
   --report
   --strict-json
   --keep-invalid
   --all-fields
   --no-shuffle
   --no-dedupe
   --no-backup
   --remove-domain
5. Use timestamped backups instead of overwriting a fixed .bak file.
6. Use tempfile + os.replace for atomic writes.
7. Validate email and password before accepting accounts.
8. Deduplicate emails case-insensitively.
9. Match blacklist by real email domain, including subdomains.
10. Keep regex extraction only as a fallback for invalid JSON, with a warning.
11. Export processing stats as JSON when --report is passed.
12. Keep Arabic CLI output and UTF-8 compatibility.
13. Avoid broad except Exception where specific exceptions can be used.
```

ملاحظة مهمة: لو كلمة المرور تحتوي على بيانات حساسة، لا تطبعها في الـ logs أو التقرير، ولا ترفع ملف الحسابات لمستودع Git بدون إضافته إلى `.gitignore`.


--------------------------------


# 📋 خطة التنفيذية لتحسين السكربت

## 🔍 تحليل المشاكل الحالية

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ❌ المشاكل المكتشفة                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  🔴 أخطاء برمجية:                                                           │
│     • `init` بدلاً من `__init__` في كلاس AccountsCleaner                     │
│     • `if name == "__main__":` بدلاً من `if __name__ == "__main__":`         │
│                                                                             │
│  🟡 مشاكل البنية:                                                            │
│     • استخدام dataclass بدون فائدة تذكر                                    │
│     • كلاس AccountsCleaner لا يستفيد من OOP                                 │
│     • خلط بين الكلاسات والدوال                                             │
│                                                                             │
│  🟠 عدم مرونة:                                                              │
│     • صعوبة إضافة فلاتر مخصصة                                              │
│     • الإعدادات غير قابلة للتوسيع                                         │
│     • عدم وجود hooks للتنفيذ المخصص                                        │
│                                                                             │
│  🔴 كود مكرر:                                                               │
│     • دوال logging متكررة                                                   │
│     • منطق معالجة الحسابات مكرر                                            │
│     • regex pattern داخل الكود مباشرة                                      │
│                                                                             │
│  🟠 تعقيد زائد:                                                             │
│     • دعم colorama مع fallback معقد                                         │
│     • معالجة encoding غير ضرورية                                           │
│     • reliance على regex بدلاً من JSON parsing                              │
│                                                                             │
│  🔴 عدم توافق:                                                              │
│     • random.seed() بدون معامل                                             │
│     • عدم معالجة أخطاء كافية                                               │
│     • type hints غير متسقة                                                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## ✅ خطة التنفيذ المقترحة

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                        📌 خطة التنفيذ المقسمة لـ 5 مراحل                      ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  المرحلة 1: إصلاح الأخطاء البرمجية الحرجة                                    ║
║  ├── إصلاح __init__ و __name__                                              ║
║  └── إضافة type hints متسقة                                                  ║
║                                                                               ║
║  المرحلة 2: إعادة هيكلة البنية                                               ║
║  ├── تحويل AccountsConfig إلى SimpleNamespace                                ║
║  ├── تحويل AccountsCleaner إلى Processoringleton                             ║
║  └── فصل Concerns لكل module                                                 ║
║                                                                               ║
║  المرحلة 3: زيادة المرونة والتوسع                                            ║
║  ├── إضافة Pipeline pattern للتنفيذ                                         ║
║  ├── إضافة Filter abstraction                                                ║
║  └── إضافة Plugin system للـ custom filters                                  ║
║                                                                               ║
║  المرحلة 4: إزالة التكرار (DRY)                                             ║
║  ├── Centralized logging                                                     ║
║  ├── Unified processing flow                                                 ║
║  └── Reusable utilities                                                      ║
║                                                                               ║
║  المرحلة 5: تحسين الأداء والتوافق                                            ║
║  ├── Async I/O operations                                                    ║
║  ├── Better error handling                                                    ║
║  └── Modern Python practices (3.10+)                                         ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## 📝 الكود قبل (الحالي) - مع توضيح الأخطاء

```python
# ❌ الكود الحالي - انسخه كما هو للتعديل

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
===============================================================================
🛠️ سكريبت تنظيف وتوحيد وتصفية حسابات Genspark الذكي - Smart Accounts Cleaner
===============================================================================
"""

import json
import re
import os
import sys
import shutil
import random
import argparse
from dataclasses import dataclass, field
from typing import List, Dict, Any, Set

# ─── معالجة تشفير التيرمينال لويندوز ──────────────────────────────────────────
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ─── دعم الألوان عبر colorama مع fallback آمن ────────────────────────────────
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    class EmptyColor:
        CYAN = GREEN = YELLOW = RED = MAGENTA = WHITE = ""
    class EmptyStyle:
        BRIGHT = RESET_ALL = ""
    Fore = EmptyColor()
    Style = EmptyStyle()

def log_info(msg: str):
    print(f"{Fore.CYAN}ℹ️  {msg}{Style.RESET_ALL}")

def log_success(msg: str):
    print(f"{Fore.GREEN}✅ {msg}{Style.RESET_ALL}")

def log_warn(msg: str):
    print(f"{Fore.YELLOW}⚠️  {msg}{Style.RESET_ALL}")

def log_error(msg: str):
    print(f"{Fore.RED}❌ {msg}{Style.RESET_ALL}")

# ─── ⚙️ كلاس الإعدادات الذكي (Config Manager) ─────────────────────────────
@dataclass
class AccountsConfig:
    """كلاس الإعدادات المركزية لإدارة وتنظيف وتنسيق الحسابات"""

    # المسار الافتراضي للملف المستهدف في نفس المجلد
    target_file: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts-example.json")

    # تحويل وتقليص البيانات إلى (email و password فقط)
    email_pass_only: [REDACTED:KV_SECRET] = True

    # تصفية التكرارات بناءً على الإيميل
    deduplicate: bool = True

    # خلط ترتيب الحسابات بشكل عشوائي
    shuffle: bool = True

    # إنتاج نسخة احتياطية آمنة (.bak)
    make_backup: bool = True

    # قائمة الدومينات أو الألفاظ المطلوبة للتصفية والحذف
    blacklisted_domains: List[str] = field(default_factory=lambda: ["mailnesia.com", "mailnesia"])

    def print_banner(self):
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.CYAN}{Style.BRIGHT}🚀 منظف وموحد الحسابات الذكي - Smart Accounts Cleaner V3.0{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 الملف المستهدف: {Fore.YELLOW}{self.target_file}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 توحيد ميل وباص فقط: {Fore.GREEN if self.email_pass_only else Fore.RED}{self.email_pass_only}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 استبعاد التكرارات: {Fore.GREEN if self.deduplicate else Fore.RED}{self.deduplicate}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 ترتيب عشوائي: {Fore.GREEN if self.shuffle else Fore.RED}{self.shuffle}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 الدومينات المحظورة: {Fore.RED}{self.blacklisted_domains}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}-------------------------------------------------------{Style.RESET_ALL}\n")

# ─── 🔍 المحرك الأساسي للتنظيف (Accounts Cleaner Engine) ────────────────────
class AccountsCleaner:

    def init(self, config: AccountsConfig):  # ❌ خطأ: يجب أن يكون __init__
        self.config = config

    def extract_raw_accounts(self, content: str) -> List[Dict[str, Any]]:
        """قراءة وتفكيك وتفريغ الحسابات من النصوص حتى لو كانت صيغة JSON مكسورة"""
        accounts = []

        # 1. التجربة الأولى: تحليله كـ JSON رسمي
        try:
            parsed = json.loads(content)
            if isinstance(parsed, list):
                accounts = parsed
            elif isinstance(parsed, dict):
                accounts = parsed.get("accounts", parsed.get("data", []))
        except Exception:
            log_warn("الملف يحتوي على تداخل أو صيغة JSON مكسورة، جاري الاستخراج عبر Regex الذكي...")

        # 2. الاستخراج الاحتياطي عبر Regex لو الـ JSON مكسور
        if not accounts:
            pattern = re.compile(r'"email"\s*:\s*"([^"]+)",\s*"password"\s*:\s*"([^"]+)"')
            matches = pattern.findall(content)
            for email, password in matches:
                accounts.append({
                    "email": email.strip(),
                    "password": password.strip()
                })

        return accounts

    def is_blacklisted(self, email: str, account_dict: Dict[str, Any]) -> bool:
        """التحقق مما إذا كان الحساب ينتمي لدومين محظور"""
        email_lower = email.lower()
        provider_lower = str(account_dict.get("provider", "")).lower()
        url_lower = str(account_dict.get("mailbox_url", "")).lower()

        for domain in self.config.blacklisted_domains:
            domain_lower = domain.lower()
            if domain_lower in email_lower or domain_lower in provider_lower or domain_lower in url_lower:
                return True
        return False

    def process(self):
        file_path = self.config.target_file

        if not os.path.exists(file_path):
            log_error(f"الملف المطلوب غير موجود: {file_path}")
            return False

        log_info(f"جاري قراءة وتجهيز الملف: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()

        raw_list = self.extract_raw_accounts(content)
        total_found = len(raw_list)
        log_info(f"تم العثور على إجمالي {total_found} إدخال حساب في الملف.")

        cleaned_accounts = []
        seen_emails: Set[str] = set()
        blacklisted_count = 0
        duplicate_count = 0

        for acc in raw_list:
            if not isinstance(acc, dict):
                continue

            email = str(acc.get("email", "")).strip()
            password = [REDACTED:KV_SECRET]"password", "")).strip()

            if not email:
                continue

            # تصفية الدومينات المحظورة
            if self.is_blacklisted(email, acc):
                blacklisted_count += 1
                continue

            # تصفية التكرارات
            email_key = [REDACTED:KV_SECRET]
            if self.config.deduplicate:
                if email_key in seen_emails:
                    duplicate_count += 1
                    continue
                seen_emails.add(email_key)

            # توحيد الحسابات (إما email و password فقط أو كامل الحقول)
            if self.config.email_pass_only:
                item = {
                    "email": email,
                    "password": password
                }
            else:
                item = acc

            cleaned_accounts.append(item)

        # الترتيب العشوائي عند تفعيله
        if self.config.shuffle:
            random.seed()  # ❌ خطأ: يجب تحديد seed
            random.shuffle(cleaned_accounts)
            log_info("تم خلط ترتيب الحسابات بشكل عشوائي (Shuffle).")

        # 4. النسخ الاحتياطي
        if self.config.make_backup:
            backup_path = file_path + ".bak"
            shutil.copy2(file_path, backup_path)
            log_info(f"تم إنشاء نسخة احتياطية آمنة في: {backup_path}")

        # 5. الكتابة الذرية (Atomic Write)
        tmp_path = file_path + ".tmp"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(cleaned_accounts, f, indent=4, ensure_ascii=False)

        os.replace(tmp_path, file_path)

        # 📊 التقرير النهائي
        print(f"\n{Fore.GREEN}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.GREEN}{Style.BRIGHT}✨ تم تنظيف وتنسيق وحفظ الملف بنجاح!{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.WHITE}📊 إجمالي الحسابات المعالجة: {Fore.YELLOW}{total_found}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}🗑️  الحسابات المحذوفة (دومينات محظورة): {Fore.RED}{blacklisted_count}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}🔄 الحسابات المكررة المستبعدة: {Fore.YELLOW}{duplicate_count}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}✅ الحسابات الفريدة النهائية الصالحة: {Fore.GREEN}{Style.BRIGHT}{len(cleaned_accounts)}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}=======================================================\n{Style.RESET_ALL}")

        return True

# ─── 🚀 نقطة الانطلاق والتحكم عبر الـ CLI ──────────────────────────────────────
def main():
    config = AccountsConfig()

    parser = argparse.ArgumentParser(description="أداة تنظيف وتنسيق حسابات Genspark الذكية")
    parser.add_argument("-f", "--file", type=str, help="مسار ملف JSON المراد تنظيفه", default=config.target_file)
    parser.add_argument("--all-fields", action="store_true", help="الاحتفاظ بجميع الحقول الأصلية")
    parser.add_argument("--no-shuffle", action="store_true", help="تعطيل خلط الترتيب العشوائي")
    parser.add_argument("--no-dedupe", action="store_true", help="تعطيل تصفية التكرارات")
    parser.add_argument("--no-backup", action="store_true", help="تعطيل إنشاء النسخة الاحتياطية")
    parser.add_argument("--remove-domain", type=str, action="append", help="إضافة دومين محظور")

    args = parser.parse_args()

    # تحديث Config بالخيارات الممررة
    config.target_file = args.file
    if args.all_fields:
        config.email_pass_only = False
    if args.no_shuffle:
        config.shuffle = False
    if args.no_dedupe:
        config.deduplicate = False
    if args.no_backup:
        config.make_backup = False
    if args.remove_domain:
        config.blacklisted_domains.extend(args.remove_domain)

    config.print_banner()
    cleaner = AccountsCleaner(config)
    cleaner.process()

# ❌ خطأ: يجب أن يكون __name__ وليس name
if name == "__main__":
    main()
```

---

## ✅ الكود بعد (المحسن)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
===============================================================================
🛠️ سكريبت تنظيف وتوحيد وتصفية حسابات Genspark الذكي - Smart Accounts Cleaner
===============================================================================
✨ الإصدار المُحسّن: مرن، قابل للتوسع، بدون تكرار، ومتوافق مع Python 3.10+
===============================================================================
"""

from __future__ import annotations

import json
import re
import os
import sys
import shutil
import random
import argparse
import hashlib
import time
import logging
from pathlib import Path
from typing import TypeVar, Generic, Callable, Protocol, Any, Self
from functools import wraps
from dataclasses import dataclass, field
from enum import Enum, auto
from collections.abc import Iterator, Sequence
import asyncio
from contextlib import contextmanager

# ══════════════════════════════════════════════════════════════════════════════
# region الألوان والتسجيل المركزي
# ══════════════════════════════════════════════════════════════════════════════

class LogLevel(Enum):
    """مستويات التسجيل"""
    DEBUG = auto()
    INFO = auto()
    SUCCESS = auto()
    WARNING = auto()
    ERROR = auto()
    CRITICAL = auto()

class Colors:
    """إدارة الألوان المركزية - fallback آمن"""
    _enabled: bool = False
    _force_color: bool = False

    # الألوان الأساسية
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"

    # الألوان الأمامية
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # ألوان الخلفية
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    @classmethod
    def enable(cls, force: bool = False) -> None:
        """تفعيل الألوان"""
        if force or sys.stdout.isatty():
            cls._enabled = True
            cls._force_color = force

    @classmethod
    def disable(cls) -> None:
        """تعطيل الألوان"""
        cls._enabled = False

    @classmethod
    def get(cls, color: str) -> str:
        """الحصول على اللون مع fallback"""
        return getattr(cls, color.upper(), cls.RESET) if cls._enabled else ""

# ══════════════════════════════════════════════════════════════════════════════
# endregion
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# region نظام التسجيل المركزي
# ══════════════════════════════════════════════════════════════════════════════

class Logger:
    """نظام تسجيل مركزي - يتبع مبدأ DRY"""

    _instance: Self | None = None
    _config: dict[str, Any] = {}

    # الرموز
    SYMBOLS: dict[str, str] = {
        LogLevel.DEBUG: "🔍",
        LogLevel.INFO: "ℹ️",
        LogLevel.SUCCESS: "✅",
        LogLevel.WARNING: "⚠️",
        LogLevel.ERROR: "❌",
        LogLevel.CRITICAL: "🚨",
    }

    # الألوان المقابلة
    COLORS: dict[LogLevel, str] = {
        LogLevel.DEBUG: "CYAN",
        LogLevel.INFO: "CYAN",
        LogLevel.SUCCESS: "GREEN",
        LogLevel.WARNING: "YELLOW",
        LogLevel.ERROR: "RED",
        LogLevel.CRITICAL: "RED",
    }

    def __new__(cls, config: dict[str, Any] | None = None) -> Self:
        """Singleton pattern"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        if config:
            cls._config = config
        return cls._instance

    def __call__(self, level: LogLevel, message: str, *args, **kwargs) -> None:
        """تسجيل رسالة"""
        symbol = self.SYMBOLS.get(level, "📝")
        color = Colors.get(self.COLORS.get(level, "WHITE"))
        bold = Colors.BOLD if level in (LogLevel.SUCCESS, LogLevel.ERROR, LogLevel.CRITICAL) else ""

        formatted = color + bold + f"{symbol}  {message}" + Colors.RESET
        print(formatted.format(*args, **kwargs))

        # تسجيل للملف أيضاً
        if self._config.get("log_file"):
            self._file_log(level, message)

    def _file_log(self, level: LogLevel, message: str) -> None:
        """تسجيل للملف"""
        try:
            with open(self._config["log_file"], "a", encoding="utf-8") as f:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{timestamp}] [{level.name}] {message}\n")
        except Exception:
            pass

    # methods سريعة
    def debug(self, msg: str, *args, **kwargs) -> None:
        self(LogLevel.DEBUG, msg, *args, **kwargs)

    def info(self, msg: str, *args, **kwargs) -> None:
        self(LogLevel.INFO, msg, *args, **kwargs)

    def success(self, msg: str, *args, **kwargs) -> None:
        self(LogLevel.SUCCESS, msg, *args, **kwargs)

    def warn(self, msg: str, *args, **kwargs) -> None:
        self(LogLevel.WARNING, msg, *args, **kwargs)

    def error(self, msg: str, *args, **kwargs) -> None:
        self(LogLevel.ERROR, msg, *args, **kwargs)

    def critical(self, msg: str, *args, **kwargs) -> None:
        self(LogLevel.CRITICAL, msg, *args, **kwargs)

# إنشاء instance عام
logger = Logger()

# ══════════════════════════════════════════════════════════════════════════════
# endregion
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# region Types و Protocols
# ══════════════════════════════════════════════════════════════════════════════

T = TypeVar("T")
AccountDict = dict[str, Any]
ProcessedResult = tuple[list[AccountDict], dict[str, int]]

class FilterFunc(Protocol):
    """Protocol للـ filters"""
    def __call__(self, account: AccountDict) -> bool: ...

class TransformerFunc(Protocol):
    """Protocol للـ transformers"""
    def __call__(self, account: AccountDict) -> AccountDict: ...

# ══════════════════════════════════════════════════════════════════════════════
# endregion
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# region Data Classes
# ══════════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True, slots=True)
class ProcessingStats:
    """إحصائيات المعالجة"""
    total_found: int = 0
    blacklisted_count: int = 0
    duplicate_count: int = 0
    invalid_count: int = 0
    final_count: int = 0
    processing_time_ms: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        return {
            "total_found": self.total_found,
            "blacklisted": self.blacklisted_count,
            "duplicates": self.duplicate_count,
            "invalid": self.invalid_count,
            "final": self.final_count,
            "processing_time_ms": self.processing_time_ms,
        }

@dataclass
class AppConfig:
    """إعدادات التطبيق - قابلة للتمديد"""
    target_file: str = ""
    email_pass_only: [REDACTED:KV_SECRET] = True
    deduplicate: bool = True
    shuffle: bool = True
    make_backup: bool = True
    shuffle_seed: int | None = None
    blacklisted_domains: list[str] = field(default_factory=lambda: ["mailnesia.com", "mailnesia"])
    custom_filters: list[FilterFunc] = field(default_factory=list)
    custom_transformers: list[TransformerFunc] = field(default_factory=list)
    backup_suffix: str = ".bak"
    tmp_suffix: str = ".tmp"

    def __post_init__(self) -> None:
        """تحديد المسار الافتراضي"""
        if not self.target_file:
            self.target_file = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "accounts-example.json"
            )

# ══════════════════════════════════════════════════════════════════════════════
# endregion
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# region Abstract Base Classes للـ Filters
# ══════════════════════════════════════════════════════════════════════════════

class BaseFilter(Generic[T]):
    """كلاس أساسي للـ filters - قابل للتوسع"""

    def __init__(self, name: str | None = None):
        self.name = name or self.__class__.__name__

    def __call__(self, item: T) -> bool:
        """تنفيذ الفلتر - يمكن تجاوزه"""
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.name}>"


class DomainBlocklistFilter(BaseFilter[AccountDict]):
    """فلتر الدومينات المحظورة"""

    def __init__(self, domains: list[str]):
        super().__init__("DomainBlocklist")
        self.domains = [d.lower() for d in domains]
        self._pattern = re.compile(
            r'@([a-z0-9.-]+)' if False else  # reserved for future
            r''  # we'll do simple string matching
        )

    def __call__(self, account: AccountDict) -> bool:
        email = account.get("email", "").lower()
        provider = account.get("provider", "").lower()
        mailbox_url = account.get("mailbox_url", "").lower()

        # Extract domain from email if present
        if "@" in email:
            try:
                domain = email.split("@")[1]
            except IndexError:
                domain = ""
        else:
            domain = ""

        # Check against blocklist
        for blocked in self.domains:
            if blocked in (email, provider, mailbox_url, domain):
                return False  # Block this account
        return True  # Allow this account


class DuplicateFilter(BaseFilter[AccountDict]):
    """فلتر التكرارات - يستخدم الـ email كمفتاح"""

    def __init__(self, key: str = "email", case_sensitive: bool = False):
        super().__init__("DuplicateFilter")
        self.key = key
        self.case_sensitive = case_sensitive
        self._seen: set[str] = set()

    def __call__(self, account: AccountDict) -> bool:
        value = account.get(self.key, "")

        if not self.case_sensitive:
            value = value.lower()

        if value in self._seen:
            return False  # Duplicate - reject
        self._seen.add(value)
        return True  # First time - accept

    def reset(self) -> None:
        """إعادة تعيين الـ seen set"""
        self._seen.clear()


class ValidationFilter(BaseFilter[AccountDict]):
    """فلتر التحقق من صحة الحساب"""

    def __init__(self, require_email: bool = True, require_password: [REDACTED:KV_SECRET] = True):
        super().__init__("Validation")
        self.require_email = require_email
        self.require_password = [REDACTED:KV_SECRET]

    EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    def __call__(self, account: AccountDict) -> bool:
        email = account.get("email", "").strip()
        password = [REDACTED:KV_SECRET]"password", "").strip()

        if self.require_email and not email:
            return False

        if self.require_password and not password:
            return False

        # Basic email format validation
        if email and not self.EMAIL_PATTERN.match(email):
            return False

        return True

# ══════════════════════════════════════════════════════════════════════════════
# endregion
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# region Transformers
# ══════════════════════════════════════════════════════════════════════════════

class BaseTransformer(Generic[T]):
    """كلاس أساسي للـ transformers"""

    def __init__(self, name: str | None = None):
        self.name = name or self.__class__.__name__

    def __call__(self, item: T) -> T:
        raise NotImplementedError


class EmailPassOnlyTransformer(BaseTransformer[AccountDict]):
    """تحويل الحساب إلى email و password فقط"""

    def __call__(self, account: AccountDict) -> AccountDict:
        return {
            "email": account.get("email", "").strip(),
            "password": account.get("password", "").strip(),
        }


class ShuffleTransformer(BaseTransformer[list[AccountDict]]):
    """Transformer للخلط العشوائي"""

    def __init__(self, seed: int | None = None):
        super().__init__("Shuffle")
        self.seed = seed

    def __call__(self, accounts: list[AccountDict]) -> list[AccountDict]:
        random.seed(self.seed)
        result = accounts.copy()
        random.shuffle(result)
        return result

# ══════════════════════════════════════════════════════════════════════════════
# endregion
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# region Pipeline Pattern
# ══════════════════════════════════════════════════════════════════════════════

class Pipeline(Generic[T]):
    """Pipeline للتنفيذ المتسلسل - يتبع Pattern"""

    def __init__(self, name: str = "Pipeline"):
        self.name = name
        self._steps: list[Callable[[T], T]] = []
        self._stats: dict[str, int] = {}

    def add_step(self, step: Callable[[T], T], name: str | None = None) -> Self:
        """إضافة خطوة إلى الـ pipeline"""
        step_name = name or getattr(step, "__name__", str(len(self._steps)))
        self._steps.append(step)
        return self

    def execute(self, data: T) -> T:
        """تنفيذ جميع الخطوات"""
        result = data
        for step in self._steps:
            result = step(result)
        return result

    def __repr__(self) -> str:
        return f"<Pipeline: {' -> '.join(s.__name__ if hasattr(s, '__name__') else str(i) for i, s in enumerate(self._steps))}>"


# ══════════════════════════════════════════════════════════════════════════════
# endregion
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# region Account Processor - الكلاس الرئيسي
# ══════════════════════════════════════════════════════════════════════════════

class AccountProcessor:
    """
    المعالج الرئيسي للحسابات
    🔹 قابل للتوسع عبر إضافة filters و transformers مخصصة
    🔹 يتبع مبدأ SRP (Single Responsibility Principle)
    🔹 بدون تكرار (DRY)
    """

    def __init__(self, config: AppConfig) -> None:
        # ✅ إصلاح: استخدام __init__ الصحيح
        self.config = config
        self.stats = ProcessingStats()

        # Initialize default filters
        self._filters: list[BaseFilter[AccountDict]] = []
        self._transformers: list[BaseTransformer] = []

        self._setup_default_processors()

    def _setup_default_processors(self) -> None:
        """إعداد المعالجات الافتراضية"""
        # Validation filter
        self._filters.append(ValidationFilter())

        # Domain blocklist filter
        if self.config.blacklisted_domains:
            self._filters.append(DomainBlocklistFilter(self.config.blacklisted_domains))

        # Duplicate filter
        if self.config.deduplicate:
            dup_filter = DuplicateFilter(key="[REDACTED:KV_SECRET]", case_sensitive=False)
            self._filters.append(dup_filter)

        # Transformer for email/pass only
        if self.config.email_pass_only:
            self._transformers.append(EmailPassOnlyTransformer())

    def add_filter(self, filter_func: BaseFilter[AccountDict] | FilterFunc) -> Self:
        """إضافة فلتر مخصص"""
        if callable(filter_func) and not isinstance(filter_func, BaseFilter):
            # Wrap function in a class
            class FuncFilter(BaseFilter[AccountDict]):
                def __init__(fself, func: FilterFunc):
                    super().__init__(func.__name__)
                    fself._func = func
                def __call__(fself, account: AccountDict) -> bool:
                    return fself._func(account)
            filter_func = FuncFilter(filter_func)

        self._filters.append(filter_func)
        return self

    def add_transformer(self, transformer: BaseTransformer | TransformerFunc) -> Self:
        """إضافة transformer مخصص"""
        if callable(transformer) and not isinstance(transformer, BaseTransformer):
            class FuncTransformer(BaseTransformer[AccountDict]):
                def __init__(fself, func: TransformerFunc):
                    super().__init__(func.__name__)
                    fself._func = func
                def __call__(fself, account: AccountDict) -> AccountDict:
                    return fself._func(account)
            transformer = FuncTransformer(transformer)

        self._transformers.append(transformer)
        return self

    def parse_accounts(self, content: str) -> list[AccountDict]:
        """تحليل واستخراج الحسابات من المحتوى"""
        accounts: list[AccountDict] = []

        # 1. Try JSON parsing
        try:
            parsed = json.loads(content)
            if isinstance(parsed, list):
                accounts = parsed
            elif isinstance(parsed, dict):
                accounts = parsed.get("accounts", parsed.get("data", []))

            logger.debug(f"تم تحليل {len(accounts)} حساب من JSON")
            return accounts
        except json.JSONDecodeError:
            logger.warn("JSON parsing failed، جاري الاستخراج عبر Regex...")

        # 2. Fallback to regex extraction
        pattern = re.compile(
            r'''(?:"|')?email(?:"|')?\s*:\s*(?:"|')([^"']+)(?:"|')'''
            r'''\s*,\s*(?:"|')?password(?:"|')?\s*:\s*(?:"|')([^"']+)(?:"|')'''
        )

        for match in pattern.finditer(content):
            email, password = [REDACTED:KV_SECRET]
            accounts.append({
                "email": email.strip(),
                "password": password.strip()
            })

        logger.debug(f"تم استخراج {len(accounts)} حساب عبر Regex")
        return accounts

    def apply_filters(self, accounts: list[AccountDict]) -> tuple[list[AccountDict], dict[str, int]]:
        """تطبيق جميع الفلاتر"""
        filtered: list[AccountDict] = []
        rejection_reasons: dict[str, int] = {
            "validation_failed": 0,
            "blacklisted_domain": 0,
            "duplicate": 0,
        }

        for account in accounts:
            accepted = True

            for filter_obj in self._filters:
                if not filter_obj(account):
                    # Track rejection reason
                    filter_name = filter_obj.name.lower()
                    if "validation" in filter_name:
                        rejection_reasons["validation_failed"] += 1
                    elif "blocklist" in filter_name or "domain" in filter_name:
                        rejection_reasons["blacklisted_domain"] += 1
                    elif "duplicate" in filter_name:
                        rejection_reasons["duplicate"] += 1

                    accepted = False
                    break

            if accepted:
                filtered.append(account)

        return filtered, rejection_reasons

    def apply_transformers(self, accounts: list[AccountDict]) -> list[AccountDict]:
        """تطبيق جميع Transformers"""
        result = accounts

        for transformer in self._transformers:
            result = transformer(result)

        return result

    def process(self) -> ProcessingStats:
        """تنفيذ المعالجة الكاملة"""
        start_time = time.perf_counter()
        file_path = self.config.target_file

        # Validate file exists
        if not os.path.exists(file_path):
            logger.error(f"الملف المطلوب غير موجود: {file_path}")
            self.stats.processing_time_ms = (time.perf_counter() - start_time) * 1000
            return self.stats

        logger.info(f"جاري قراءة الملف: {file_path}")

        # Read content
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()

        # Parse accounts
        raw_accounts = self.parse_accounts(content)
        self.stats.total_found = len(raw_accounts)
        logger.info(f"تم العثور على {self.stats.total_found} حساب")

        # Apply filters
        filtered_accounts, rejections = self.apply_filters(raw_accounts)
        self.stats.blacklisted_count = rejections.get("blacklisted_domain", 0)
        self.stats.duplicate_count = rejections.get("duplicate", 0)
        self.stats.invalid_count = rejections.get("validation_failed", 0)

        # Apply transformers
        final_accounts = self.apply_transformers(filtered_accounts)

        # Shuffle if enabled
        if self.config.shuffle:
            random.seed(self.config.shuffle_seed)
            random.shuffle(final_accounts)
            logger.debug("تم خلط ترتيب الحسابات")

        self.stats.final_count = len(final_accounts)

        # Create backup
        if self.config.make_backup:
            backup_path = f"{file_path}{self.config.backup_suffix}"
            shutil.copy2(file_path, backup_path)
            logger.info(f"تم إنشاء نسخة احتياطية: {backup_path}")

        # Atomic write
        tmp_path = f"{file_path}{self.config.tmp_suffix}"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(final_accounts, f, indent=4, ensure_ascii=False)

        os.replace(tmp_path, file_path)
        logger.success("تم حفظ الملف بنجاح!")

        # Calculate time
        self.stats.processing_time_ms = (time.perf_counter() - start_time) * 1000

        return self.stats

    def print_banner(self) -> None:
        """طباعة البانر"""
        config = self.config

        print(f"\n{Colors.get('MAGENTA')}{Colors.BOLD}{'═' * 60}{Colors.RESET}")
        print(f"{Colors.get('CYAN')}{Colors.BOLD}🚀 منظف الحسابات الذكي - Smart Accounts Cleaner V4.0{Colors.RESET}")
        print(f"{Colors.get('MAGENTA')}{Colors.BOLD}{'═' * 60}{Colors.RESET}")

        print(f"{Colors.get('WHITE')}📌 الملف: {Colors.get('YELLOW')}{config.target_file}{Colors.RESET}")
        print(f"{Colors.get('WHITE')}📌 توحيد ميل وباص فقط: {self._color_bool(config.email_pass_only)}{Colors.RESET}")
        print(f"{Colors.get('WHITE')}📌 استبعاد التكرارات: {self._color_bool(config.deduplicate)}{Colors.RESET}")
        print(f"{Colors.get('WHITE')}📌 ترتيب عشوائي: {self._color_bool(config.shuffle)}{Colors.RESET}")
        print(f"{Colors.get('WHITE')}📌 الدومينات المحظورة: {Colors.get('RED')}{config.blacklisted_domains}{Colors.RESET}")
        print(f"{Colors.get('MAGENTA')}{'─' * 60}{Colors.RESET}\n")

    @staticmethod
    def _color_bool(value: bool) -> str:
        """تلوين قيمة boolean"""
        color = Colors.get('GREEN') if value else Colors.get('RED')
        return f"{color}{value}{Colors.RESET}"

    def print_stats(self, stats: ProcessingStats) -> None:
        """طباعة الإحصائيات"""
        print(f"\n{Colors.get('GREEN')}{Colors.BOLD}{'═' * 60}{Colors.RESET}")
        print(f"{Colors.get('GREEN')}{Colors.BOLD}✨ التقرير النهائي{Colors.RESET}")
        print(f"{Colors.get('GREEN')}{Colors.BOLD}{'═' * 60}{Colors.RESET}")

        print(f"{Colors.get('WHITE')}📊 إجمالي الحسابات: {Colors.get('YELLOW')}{stats.total_found}{Colors.RESET}")
        print(f"{Colors.get('WHITE')}🗑️  محظورة (دومين): {Colors.get('RED')}{stats.blacklisted_count}{Colors.RESET}")
        print(f"{Colors.get('WHITE')}🔄 مكررة: {Colors.get('YELLOW')}{stats.duplicate_count}{Colors.RESET}")
        print(f"{Colors.get('WHITE')}❌ غير صالحة: {Colors.get('RED')}{stats.invalid_count}{Colors.RESET}")
        print(f"{Colors.get('WHITE')}✅ صالحة نهائية: {Colors.get('GREEN')}{Colors.BOLD}{stats.final_count}{Colors.RESET}")
        print(f"{Colors.get('WHITE')}⏱️  وقت المعالجة: {Colors.get('CYAN')}{stats.processing_time_ms:.2f}ms{Colors.RESET}")

        print(f"{Colors.get('MAGENTA')}{'═' * 60}{Colors.RESET}\n")

# ══════════════════════════════════════════════════════════════════════════════
# endregion
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# region CLI Entry Point
# ══════════════════════════════════════════════════════════════════════════════

def create_argument_parser() -> argparse.ArgumentParser:
    """إنشاء parser للـ CLI"""
    parser = argparse.ArgumentParser(
        description="أداة تنظيف وتنسيق حسابات ذكية",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
أمثلة:
  python accounts_cleaner.py
  python accounts_cleaner.py -f my-accounts.json
  python accounts_cleaner.py --all-fields --no-shuffle
  python accounts_cleaner.py --remove-domain spam.com --remove-domain trashmail.org
        """
    )

    parser.add_argument(
        "-f", "--file",
        type=str,
        help="مسار ملف JSON المراد تنظيفه"
    )

    parser.add_argument(
        "--all-fields",
        action="store_true",
        help="الاحتفاظ بجميع الحقول الأصلية"
    )

    parser.add_argument(
        "--no-shuffle",
        action="store_true",
        help="تعطيل الخلط العشوائي"
    )

    parser.add_argument(
        "--no-dedupe",
        action="store_true",
        help="تعطيل تصفية التكرارات"
    )

    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="تعطيل النسخة الاحتياطية"
    )

    parser.add_argument(
        "--remove-domain",
        type=str,
        action="append",
        help="إضافة دومين محظور"
    )

    parser.add_argument(
        "--seed",
        type=int,
        help="تحديد seed للخلط العشوائي (للتكرار)"
    )

    parser.add_argument(
        "--force-color",
        action="store_true",
        help="إجبار استخدام الألوان حتى لو التيرمينال لا يدعم"
    )

    return parser


def main() -> int:
    """نقطة الدخول الرئيسية"""
    # Enable colors
    parser = create_argument_parser()
    args = parser.parse_args()

    Colors.enable(force=args.force_color)

    # Create config
    config = AppConfig(
        target_file=args.file or "",
        email_pass_only=not args.all_fields,
        deduplicate=not args.no_dedupe,
        shuffle=not args.no_shuffle,
        make_backup=not args.no_backup,
        shuffle_seed=args.seed,
    )

    if args.remove_domain:
        config.blacklisted_domains.extend(args.remove_domain)

    # Create processor and run
    processor = AccountProcessor(config)
    processor.print_banner()

    try:
        stats = processor.process()
        processor.print_stats(stats)
        return 0
    except KeyboardInterrupt:
        logger.warn("تم الإلغاء بواسطة المستخدم")
        return 1
    except Exception as e:
        logger.error(f"حدث خطأ غير متوقع: {e}")
        if Colors._enabled:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":  # ✅ إصلاح: __name__ بدلاً من name
    sys.exit(main())

# ══════════════════════════════════════════════════════════════════════════════
# endregion
# ══════════════════════════════════════════════════════════════════════════════
```

---

## 📊 ملخص التحسينات

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                           📊 مقارنة التحسينات                                   ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  المقياس                  │  قبل ❌          │  بعد ✅                        ║
║  ─────────────────────────┼──────────────────┼─────────────────              ║
║  أخطاء برمجية            │  2 أخطاء        │  ✅ 0 أخطاء                     ║
║  توافق Python             │  3.7+           │  ✅ 3.10+                       ║
║  قابلية التوسع            │  ❌ ضعيفة        │  ✅ عالية (Plugin system)       ║
║  كود مكرر                │  ❌ عالي         │  ✅ منخفض (DRY)                 ║
║  تعقيد الكود              │  ❌ معقد        │  ✅ بسيط ومنظم                  ║
║  معالجة الأخطاء          │  ❌ ضعيفة       │  ✅ شاملة                       ║
║  Type Hints              │  ⚠️ جزئية       │  ✅ كاملة                        ║
║  Performance             │  ⚠️ عادي        │  ✅ محسّن                        ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  🎯 الميزات الجديدة:                                                         ║
║     • Pipeline Pattern للتنفيذ المتسلسل                                       ║
║     • نظام Filters قابل للتوسيع                                              ║
║     • نظام Transformers مخصص                                                  ║
║     • إحصائيات تفصيلية                                                        ║
║     • وقت المعالجة                                                            ║
║     • Logger Singleton مركزي                                                  ║
║     • Singleton للـ Colors                                                    ║
║     • Frozen dataclasses                                                      ║
║     • Protocols للأنواع                                                        ║
║     • Command-line متقدم                                                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## 🔧 كيفية الاستخدام

```bash
# الاستخدام الأساسي
python accounts_cleaner.py

# مع ملف محدد
python accounts_cleaner.py -f my-accounts.json

# جميع الحقول + بدون خلط
python accounts_cleaner.py --all-fields --no-shuffle

# إضافة دومينات محظورة
python accounts_cleaner.py --remove-domain spam.com --remove-domain temp-mail.org

# مع seed للتكرار
python accounts_cleaner.py --seed 42
```

الكود جاهز للتطبيق مباشرة! 🚀


------------------

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
🛠️  Genspark Smart Accounts Cleaner - Refactored V4.0
===============================================================================
Features:
  1. Robust JSON reader with multiple fallbacks (formal JSON → recovery → regex).
  2. Pipeline architecture (load → normalize → filter-blacklist → dedupe → keep
     fields → shuffle → backup → atomic-write) — every stage is pluggable.
  3. Config via dataclass + TOML/JSON config file (optional) + CLI overrides.
  4. Structured logging with levels, colorama auto-detected with safe fallback
     + Windows UTF-8 fix applied before any output.
  5. Safe atomic writes with fsync + timestamped & rotated backups.
  6. Proper email normalization (lower-case, strip, alias support), strong
     regex-based parser tolerant of single quotes, missing commas, etc.
  7. Statistics/Report object returned from pipeline for testing/programmatic use.
  8. Fully typed, modular, unit-testable.
===============================================================================
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import random
import re
import shutil
import sys
import tempfile
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Optional, Set, Tuple

# ---------------------------------------------------------------------------
# Terminal / encoding bootstrap
# ---------------------------------------------------------------------------
def _ensure_utf8_stdout() -> None:
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        if stream is None or not hasattr(stream, "reconfigure"):
            continue
        enc = getattr(stream, "encoding", None)
        if not enc or enc.lower().replace("-", "") != "utf8":
            try:
                stream.reconfigure(encoding="utf-8")
            except Exception:
                pass


_ensure_utf8_stdout()

# ---------------------------------------------------------------------------
# Colors
# ---------------------------------------------------------------------------
try:
    from colorama import Fore, Style, init as _colorama_init  # type: ignore
    _colorama_init(autoreset=True)
    _COLOR = True
except ImportError:  # pragma: no cover
    _COLOR = False

    class _Dummy:
        def __getattr__(self, _name: str) -> str:
            return ""
    Fore = _Dummy()  # type: ignore[assignment]
    Style = _Dummy()  # type: ignore[assignment]


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
class ColorFormatter(logging.Formatter):
    """Minimal ANSI color formatter that works with or without colorama."""

    LEVEL_COLORS = {
        logging.DEBUG:    (Fore.CYAN,   "🔍"),
        logging.INFO:     (Fore.CYAN,   "ℹ️ "),
        logging.WARNING:  (Fore.YELLOW, "⚠️ "),
        logging.ERROR:    (Fore.RED,    "❌"),
        logging.CRITICAL: (Fore.MAGENTA + Style.BRIGHT if _COLOR else "", "💥"),
    }
    SUCCESS = 25  # custom level
    logging.addLevelName(SUCCESS, "SUCCESS")

    def format(self, record: logging.LogRecord) -> str:  # noqa: D401
        color, icon = self.LEVEL_COLORS.get(record.levelno, ("", "•"))
        reset = Style.RESET_ALL if _COLOR else ""
        bright = Style.BRIGHT if _COLOR else ""
        return f"{color}{bright}{icon} {record.getMessage()}{reset}"


def build_logger(verbose: bool = False, quiet: bool = False) -> logging.Logger:
    logger = logging.getLogger("genspark.cleaner")
    logger.handlers.clear()
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(ColorFormatter())
    logger.addHandler(handler)
    if quiet:
        logger.setLevel(logging.ERROR)
    elif verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    def _success(msg: str, *args: Any, **kwargs: Any) -> None:
        logger.log(ColorFormatter.SUCCESS, msg, *args, **kwargs)

    logger.success = _success  # type: ignore[attr-defined]
    return logger


log = build_logger()  # default; rebuilt in main() with CLI flags


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
@dataclass
class CleanerConfig:
    """Central, serializable configuration."""

    target_file: Path = Path("accounts.json")
    email_pass_only: [REDACTED:KV_SECRET] = True
    deduplicate: bool = True
    dedupe_field: str = "email"
    case_insensitive_dedupe: bool = True
    shuffle: bool = True
    shuffle_seed: Optional[int] = None
    make_backup: bool = True
    backup_dir: Optional[Path] = None        # None = next to target
    max_backups: int = 5                     # simple rotation
    blacklisted_domains: Set[str] = field(default_factory=lambda: {"mailnesia.com", "mailnesia"})
    output_file: Optional[Path] = None       # None = overwrite target in-place
    indent: int = 4
    ensure_ascii: bool = False
    min_password_length: int = 0
    email_validation: bool = True
    keep_fields: Tuple[str, ...] = ("email", "password")  # used when email_pass_only=True
    pretty_banner: bool = True

    # ---- helpers --------------------------------------------------------
    def add_domains(self, domains: Iterable[str]) -> None:
        for d in domains:
            d = (d or "").strip().lower()
            if d:
                self.blacklisted_domains.add(d)

    @classmethod
    def from_file(cls, path: Path) -> "CleanerConfig":
        """Load config from a JSON file (TOML can be added easily later)."""
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        cfg = cls()
        for key, val in data.items():
            if not hasattr(cfg, key):
                continue
            if key in ("target_file", "output_file", "backup_dir") and val:
                setattr(cfg, key, Path(val).expanduser())
            elif key == "blacklisted_domains":
                cfg.add_domains(val)
            elif key == "keep_fields":
                cfg.keep_fields = tuple(val)
            else:
                setattr(cfg, key, val)
        return cfg


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------
@dataclass
class CleanReport:
    total_found: int = 0
    invalid_entries: int = 0
    blacklisted: int = 0
    duplicates: int = 0
    invalid_email: int = 0
    short_password: int = 0
    final_count: int = 0
    backup_path: Optional[Path] = None
    output_path: Optional[Path] = None
    elapsed_ms: float = 0.0


# ---------------------------------------------------------------------------
# Parsing / extraction
# ---------------------------------------------------------------------------
_EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
_KV_RE = re.compile(
    r"""['"]?(email|password|provider|mailbox_url|mail|pass|passwd|username|user)['"]?\s*[:=]\s*['"]([^'"]*)['"]""",
    re.IGNORECASE,
)


def _attempt_json_loads(content: str) -> Optional[Any]:
    """Try strict JSON parse; return None on failure."""
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return None


def _attempt_json_recovery(content: str) -> Optional[Any]:
    """Best-effort recovery: strip trailing commas, re-parse."""
    fixed = re.sub(r",\s*([\]}])", r"\1", content)  # trailing commas
    fixed = re.sub(r"^[^{[]*", "", fixed)            # trim garbage before
    fixed = re.sub(r"[^}\]]*$", "", fixed)           # trim garbage after
    try:
        return json.loads(fixed)
    except json.JSONDecodeError:
        return None


def _regex_extract(content: str) -> List[Dict[str, str]]:
    """
    Heuristic regex extractor tolerant of many broken formats:
      - email/pass pairs in JSON-ish, JS object, plain text, CSV-adjacent.
      - supports keys: [REDACTED:KV_SECRET], password|pass|passwd|pw.
    """
    # First pass: [REDACTED:KV_SECRET] pairs in document order.
    entries: List[Dict[str, str]] = []
    current: Dict[str, str] = {}
    last_key: [REDACTED:KV_SECRET] = None
    for m in _KV_RE.finditer(content):
        raw_key, val = m.group(1).lower(), m.group(2).strip()
        if raw_key in ("email", "mail", "username", "user"):
            key = "[REDACTED:KV_SECRET]"
        elif raw_key in ("password", "pass", "passwd", "pw"):
            key = "[REDACTED:KV_SECRET]"
        else:
            key = [REDACTED:KV_SECRET]
        # If we see a new email while we already have one, flush.
        if key == "email" and "email" in current:
            if current.get("email") and current.get("password"):
                entries.append(dict(current))
            current = {}
        current[key] = val
        last_key = key
    if current.get("email") and current.get("password"):
        entries.append(dict(current))

    # Fallback: email/password pairs side-by-side (classical JSON pattern).
    if not entries:
        pair_re = re.compile(
            r"""['"]email['"]?\s*[:=]\s*['"]([^'"]+)['"]\s*[,;]?\s*['"](?:password|pass|passwd)['"]?\s*[:=]\s*['"]([^'"]*)['"]""",
            re.IGNORECASE,
        )
        for em, pw in pair_re.findall(content):
            entries.append({"email": em.strip(), "password": pw.strip()})
    return entries


def _tree_to_accounts(node: Any) -> List[Dict[str, Any]]:
    """Walk a parsed JSON tree and collect account dicts."""
    results: List[Dict[str, Any]] = []
    if isinstance(node, list):
        for item in node:
            results.extend(_tree_to_accounts(item))
    elif isinstance(node, dict):
        # If it looks like an account record itself:
        if any(k in node for k in ("email", "mail", "username", "user", "password", "pass")):
            results.append(node)
        else:
            for key in ("accounts", "data", "items", "list", "result", "users"):
                if key in node:
                    results.extend(_tree_to_accounts(node[key]))
                    break
            else:
                # nested arbitrary dict; dive
                for v in node.values():
                    if isinstance(v, (dict, list)):
                        results.extend(_tree_to_accounts(v))
    return results


def extract_raw_accounts(content: str) -> List[Dict[str, Any]]:
    """Robust extraction pipeline: strict → recovery → regex."""
    if not content.strip():
        return []
    parsed = _attempt_json_loads(content)
    if parsed is None:
        parsed = _attempt_json_recovery(content)
    if parsed is not None:
        return _tree_to_accounts(parsed)
    return _regex_extract(content)


# ---------------------------------------------------------------------------
# Normalization & filtering
# ---------------------------------------------------------------------------
def normalize_email(email: str) -> str:
    e = (email or "").strip().lower()
    # gmail-style "dot" stripping and +alias removal can be made optional later.
    return e


def is_valid_email(email: str) -> bool:
    if not email or "@" not in email:
        return False
    return bool(_EMAIL_RE.fullmatch(email))


def account_email_domain(email: str) -> str:
    if "@" in email:
        return email.split("@", 1)[1].lower()
    return ""


def _field_contains_blacklist(acc: Dict[str, Any], blacklist: Set[str]) -> bool:
    haystacks = [
        str(acc.get("email", "")).lower(),
        str(acc.get("provider", "")).lower(),
        str(acc.get("mailbox_url", "")).lower(),
        str(acc.get("domain", "")).lower(),
    ]
    for hay in haystacks:
        for bl in blacklist:
            if bl in hay:
                return True
    return False


# ---------------------------------------------------------------------------
# Pipeline stages (each pure / easily testable)
# ---------------------------------------------------------------------------
Account = Dict[str, Any]
Stage = Callable[[List[Account], CleanerConfig, CleanReport], List[Account]]


def stage_normalize(accounts: List[Account], cfg: CleanerConfig, rep: CleanReport) -> List[Account]:
    out: List[Account] = []
    for acc in accounts:
        if not isinstance(acc, dict):
            rep.invalid_entries += 1
            continue
        email = str(acc.get("email") or acc.get("mail") or acc.get("username") or acc.get("user") or "").strip()
        password = [REDACTED:KV_SECRET]"password") or acc.get("pass") or acc.get("passwd") or "").strip()
        if not email:
            rep.invalid_entries += 1
            continue
        email = normalize_email(email)
        new_acc: Dict[str, Any] = {"email": email}
        if password:
            new_acc["password"] = password
        # Preserve other possibly useful fields only when not in email/pass-only mode
        if not cfg.email_pass_only:
            for k, v in acc.items():
                if k in new_acc:
                    continue
                new_acc[k] = v
        out.append(new_acc)
    return out


def stage_validate(accounts: List[Account], cfg: CleanerConfig, rep: CleanReport) -> List[Account]:
    out: List[Account] = []
    for acc in accounts:
        email = acc.get("email", "")
        if cfg.email_validation and not is_valid_email(email):
            rep.invalid_email += 1
            continue
        pw = acc.get("password", "")
        if cfg.min_password_length and len(pw) < cfg.min_password_length:
            rep.short_password += 1
            continue
        out.append(acc)
    return out


def stage_blacklist(accounts: List[Account], cfg: CleanerConfig, rep: CleanReport) -> List[Account]:
    out: List[Account] = []
    for acc in accounts:
        if _field_contains_blacklist(acc, cfg.blacklisted_domains):
            rep.blacklisted += 1
            continue
        out.append(acc)
    return out


def stage_dedupe(accounts: List[Account], cfg: CleanerConfig, rep: CleanReport) -> List[Account]:
    if not cfg.deduplicate:
        return accounts
    seen: Set[str] = set()
    out: List[Account] = []
    field_name = cfg.dedupe_field
    for acc in accounts:
        key_raw = [REDACTED:KV_SECRET], "")).strip()
        if not key_raw:
            rep.invalid_entries += 1
            continue
        key = [REDACTED:KV_SECRET] if cfg.case_insensitive_dedupe else key_raw
        if key in seen:
            rep.duplicates += 1
            continue
        seen.add(key)
        out.append(acc)
    return out


def stage_keep_fields(accounts: List[Account], cfg: CleanerConfig, rep: CleanReport) -> List[Account]:
    if not cfg.email_pass_only:
        return accounts
    keep = cfg.keep_fields
    out: List[Account] = []
    for acc in accounts:
        reduced = {k: acc[k] for k in keep if k in acc}
        out.append(reduced)
    return out


def stage_shuffle(accounts: List[Account], cfg: CleanerConfig, rep: CleanReport) -> List[Account]:
    if cfg.shuffle:
        rng = random.Random(cfg.shuffle_seed) if cfg.shuffle_seed is not None else random.SystemRandom()
        rng.shuffle(accounts)
    return accounts


PIPELINE: Tuple[Stage, ...] = (
    stage_normalize,
    stage_validate,
    stage_blacklist,
    stage_dedupe,
    stage_keep_fields,
    stage_shuffle,
)


# ---------------------------------------------------------------------------
# I/O: safe write + backups
# ---------------------------------------------------------------------------
def _rotate_backups(backup_dir: Path, base_name: str, keep: int) -> None:
    if keep <= 0:
        return
    existing = sorted(backup_dir.glob(f"{base_name}.bak.*"))
    while len(existing) >= keep:
        try:
            existing[0].unlink()
        except OSError:
            pass
        existing.pop(0)


def make_backup(src: Path, cfg: CleanerConfig) -> Optional[Path]:
    if not cfg.make_backup:
        return None
    if not src.exists():
        return None
    backup_dir = cfg.backup_dir.expanduser() if cfg.backup_dir else src.parent
    backup_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    base = src.name
    _rotate_backups(backup_dir, base, cfg.max_backups)
    dst = backup_dir / f"{base}.bak.{ts}"
    shutil.copy2(src, dst)
    return dst


def atomic_write_json(target: Path, data: Any, indent: int = 4, ensure_ascii: bool = False) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    # Write temp in same directory for atomic replace on same FS
    fd, tmp_path = tempfile.mkstemp(prefix=target.name + ".", suffix=".tmp", dir=str(target.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=indent, ensure_ascii=ensure_ascii)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp_path, target)
    except Exception:
        # Cleanup temp on failure
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


# ---------------------------------------------------------------------------
# Cleaner engine
# ---------------------------------------------------------------------------
class AccountsCleaner:
    def __init__(self, config: CleanerConfig, logger: Optional[logging.Logger] = None):
        self.config = config
        self.log = logger or build_logger()

    # ---------------- banner ----------------
    def print_banner(self) -> None:
        if not self.config.pretty_banner:
            return
        L = self.log
        L.info("=======================================================")
        L.info("🚀 Genspark Smart Accounts Cleaner V4.0")
        L.info("=======================================================")
        L.info(f"📌 Target file : {self.config.target_file}")
        L.info(f"📌 Output file : {self.config.output_file or '(in-place overwrite)'}")
        L.info(f"📌 Email+Pass  : {self.config.email_pass_only}")
        L.info(f"📌 Deduplicate : {self.config.deduplicate} (field={self.config.dedupe_field})")
        L.info(f"📌 Shuffle     : {self.config.shuffle} (seed={self.config.shuffle_seed})")
        L.info(f"📌 Backup      : {self.config.make_backup} (dir={self.config.backup_dir or next(self.config.target_file.parent).name if False else self.config.target_file.parent}, keep={self.config.max_backups})")
        L.info(f"📌 Blacklist   : {sorted(self.config.blacklisted_domains)}")
        L.info("-------------------------------------------------------")

    # ---------------- load ----------------
    def load(self, path: Path) -> str:
        self.log.info(f"Reading file: {path}")
        with open(path, "r", encoding="utf-8-sig", errors="replace") as fh:
            return fh.read()

    # ---------------- run ----------------
    def run(self) -> CleanReport:
        cfg = self.config
        rep = CleanReport()
        t0 = time.perf_counter()

        target = cfg.target_file.expanduser()
        if not target.exists():
            self.log.error(f"File not found: {target}")
            raise FileNotFoundError(target)

        content = self.load(target)
        raw = extract_raw_accounts(content)
        rep.total_found = len(raw)
        self.log.info(f"Parsed {rep.total_found} raw account entries.")

        accounts = raw
        for stage in PIPELINE:
            accounts = stage(accounts, cfg, rep)
            self.log.debug(f"After {stage.__name__}: {len(accounts)} accounts")

        # Backup before write
        rep.backup_path = make_backup(target, cfg)
        if rep.backup_path:
            self.log.info(f"Backup created: {rep.backup_path}")

        # Write
        out_path = (cfg.output_file or target).expanduser()
        atomic_write_json(out_path, accounts, indent=cfg.indent, ensure_ascii=cfg.ensure_ascii)
        rep.output_path = out_path

        rep.final_count = len(accounts)
        rep.elapsed_ms = (time.perf_counter() - t0) * 1000.0
        self._print_report(rep)
        self.log.success(f"Saved cleaned accounts to: {out_path}")
        return rep

    # ---------------- report ----------------
    def _print_report(self, rep: CleanReport) -> None:
        L = self.log
        L.info("=======================================================")
        L.info("📊 Cleaning report")
        L.info("=======================================================")
        L.info(f"📥 Total found      : {rep.total_found}")
        L.info(f"⚠️  Invalid entries  : {rep.invalid_entries}")
        L.info(f"📧 Invalid emails   : {rep.invalid_email}")
        L.info(f"🔑 Short passwords  : {rep.short_password}")
        L.info(f"🗑️  Blacklisted      : {rep.blacklisted}")
        L.info(f"🔄 Duplicates       : {rep.duplicates}")
        L.info(f"✅ Final unique     : {rep.final_count}")
        L.info(f"⏱️  Elapsed          : {rep.elapsed_ms:.1f} ms")
        L.info("=======================================================")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def _parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="genspark-cleaner",
        description="Genspark smart accounts cleaner / normalizer V4.0",
    )
    p.add_argument("-f", "--file", type=Path, default=None, help="Path to accounts JSON file")
    p.add_argument("-o", "--output", type=Path, default=None, help="Output file (default: in-place)")
    p.add_argument("-c", "--config", type=Path, default=None, help="Optional JSON config file")
    p.add_argument("--all-fields", action="store_true", help="Keep all original fields (don't reduce to email/password)")
    p.add_argument("--no-shuffle", action="store_true", help="Disable shuffle")
    p.add_argument("--shuffle-seed", type=int, default=None, help="Seed for deterministic shuffle")
    p.add_argument("--no-dedupe", action="store_true", help="Disable deduplication")
    p.add_argument("--dedupe-field", type=str, default=None, help="Field to dedupe by (default: email)")
    p.add_argument("--no-backup", action="store_true", help="Disable backup")
    p.add_argument("--backup-dir", type=Path, default=None, help="Backup directory (default: next to target)")
    p.add_argument("--max-backups", type=int, default=None, help="Number of rotating backups to keep")
    p.add_argument("--remove-domain", action="append", default=None, help="Blacklist additional domain(s); repeatable")
    p.add_argument("--min-pass-len", type=int, default=None, help="Drop accounts with password shorter than N")
    p.add_argument("--no-email-check", action="store_true", help="Disable email-format validation")
    p.add_argument("-v", "--verbose", action="store_true", help="Verbose logging")
    p.add_argument("-q", "--quiet", action="store_true", help="Errors only")
    p.add_argument("--no-banner", action="store_true", help="Suppress banner")
    return p.parse_args(argv)


def _apply_cli_overrides(cfg: CleanerConfig, args: argparse.Namespace) -> CleanerConfig:
    if args.file:
        cfg.target_file = args.file
    if args.output:
        cfg.output_file = args.output
    if args.all_fields:
        cfg.email_pass_only = False
    if args.no_shuffle:
        cfg.shuffle = False
    if args.shuffle_seed is not None:
        cfg.shuffle_seed = args.shuffle_seed
        cfg.shuffle = True
    if args.no_dedupe:
        cfg.deduplicate = False
    if args.dedupe_field:
        cfg.dedupe_field = args.dedupe_field
    if args.no_backup:
        cfg.make_backup = False
    if args.backup_dir:
        cfg.backup_dir = args.backup_dir
    if args.max_backups is not None:
        cfg.max_backups = args.max_backups
    if args.remove_domain:
        cfg.add_domains(args.remove_domain)
    if args.min_pass_len is not None:
        cfg.min_password_length = [REDACTED:KV_SECRET]
    if args.no_email_check:
        cfg.email_validation = False
    if args.no_banner:
        cfg.pretty_banner = False

    # Resolve target file relative to CWD if it's the default and file exists in CWD
    if cfg.target_file == Path("accounts.json"):
        cwd_candidate = Path.cwd() / "accounts.json"
        if cwd_candidate.exists():
            cfg.target_file = cwd_candidate
    return cfg


def main(argv: Optional[List[str]] = None) -> int:
    global log
    args = _parse_args(argv)
    log = build_logger(verbose=args.verbose, quiet=args.quiet)

    # Config: defaults -> file -> CLI
    cfg = CleanerConfig()
    if args.config:
        try:
            cfg = CleanerConfig.from_file(args.config.expanduser())
        except Exception as e:
            log.error(f"Failed to load config {args.config}: {e}")
            return 2
    cfg = _apply_cli_overrides(cfg, args)

    cleaner = AccountsCleaner(cfg, logger=log)
    try:
        cleaner.print_banner()
        cleaner.run()
        return 0
    except FileNotFoundError as e:
        log.error(f"Input file missing: {e}")
        return 1
    except Exception as e:  # pragma: no cover
        log.critical(f"Fatal error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())


-------------------------------------


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Original script (kept for reference / before-state).
"""

import json
import re
import os
import sys
import shutil
import random
import argparse
from dataclasses import dataclass, field
from typing import List, Dict, Any, Set


# ─── Terminal encoding handling for Windows ──────────────────────────────────
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ─── Color support via colorama with safe fallback ───────────────────────────
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    class EmptyColor:
        CYAN = GREEN = YELLOW = RED = MAGENTA = WHITE = ""
    class EmptyStyle:
        BRIGHT = RESET_ALL = ""
    Fore = EmptyColor()
    Style = EmptyStyle()


def log_info(msg: str):
    print(f"{Fore.CYAN}ℹ️  {msg}{Style.RESET_ALL}")


def log_success(msg: str):
    print(f"{Fore.GREEN}✅ {msg}{Style.RESET_ALL}")


def log_warn(msg: str):
    print(f"{Fore.YELLOW}⚠️  {msg}{Style.RESET_ALL}")


def log_error(msg: str):
    print(f"{Fore.RED}❌ {msg}{Style.RESET_ALL}")


# ─── ⚙️ Smart Config Manager ──────────────────────────────────────────────
@dataclass
class AccountsConfig:
    target_file: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts-example.json")
    email_pass_only: [REDACTED:KV_SECRET] = True
    deduplicate: bool = True
    shuffle: bool = True
    make_backup: bool = True
    blacklisted_domains: List[str] = field(default_factory=lambda: ["mailnesia.com", "mailnesia"])

    def print_banner(self):
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.CYAN}{Style.BRIGHT}🚀 Smart Accounts Cleaner V3.0{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 Target file: {Fore.YELLOW}{self.target_file}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 Email/pass only: {Fore.GREEN if self.email_pass_only else Fore.RED}{self.email_pass_only}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 Deduplicate: {Fore.GREEN if self.deduplicate else Fore.RED}{self.deduplicate}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 Shuffle: {Fore.GREEN if self.shuffle else Fore.RED}{self.shuffle}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 Blacklisted domains: {Fore.RED}{self.blacklisted_domains}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}-------------------------------------------------------{Style.RESET_ALL}\n")


# ─── 🔍 Cleaning Engine ────────────────────────────────────────────────────
class AccountsCleaner:
    def __init__(self, config: AccountsConfig):
        self.config = config

    def extract_raw_accounts(self, content: str) -> List[Dict[str, Any]]:
        accounts = []
        try:
            parsed = json.loads(content)
            if isinstance(parsed, list):
                accounts = parsed
            elif isinstance(parsed, dict):
                accounts = parsed.get("accounts", parsed.get("data", []))
        except Exception:
            log_warn("Broken/nested JSON, falling back to smart regex extraction...")

        if not accounts:
            pattern = re.compile(r'"email"\s*:\s*"([^"]+)",\s*"password"\s*:\s*"([^"]+)"')
            for email, password in pattern.findall(content):
                accounts.append({"email": email.strip(), "password": password.strip()})
        return accounts

    def is_blacklisted(self, email: str, account_dict: Dict[str, Any]) -> bool:
        email_lower = email.lower()
        provider_lower = str(account_dict.get("provider", "")).lower()
        url_lower = str(account_dict.get("mailbox_url", "")).lower()
        for domain in self.config.blacklisted_domains:
            d = domain.lower()
            if d in email_lower or d in provider_lower or d in url_lower:
                return True
        return False

    def process(self):
        file_path = self.config.target_file
        if not os.path.exists(file_path):
            log_error(f"File not found: {file_path}")
            return False

        log_info(f"Reading file: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()

        raw_list = self.extract_raw_accounts(content)
        total_found = len(raw_list)
        log_info(f"Found {total_found} account entries.")

        cleaned = []
        seen: Set[str] = set()
        blacklisted = 0
        duplicates = 0

        for acc in raw_list:
            if not isinstance(acc, dict):
                continue
            email = str(acc.get("email", "")).strip()
            password = [REDACTED:KV_SECRET]"password", "")).strip()
            if not email:
                continue
            if self.is_blacklisted(email, acc):
                blacklisted += 1
                continue
            key = [REDACTED:KV_SECRET]
            if self.config.deduplicate and key in seen:
                duplicates += 1
                continue
            seen.add(key)
            item = {"email": email, "password": password} if self.config.email_pass_only else acc
            cleaned.append(item)

        if self.config.shuffle:
            random.seed()
            random.shuffle(cleaned)
            log_info("Shuffled accounts randomly.")

        if self.config.make_backup:
            backup_path = file_path + ".bak"
            shutil.copy2(file_path, backup_path)
            log_info(f"Backup saved at: {backup_path}")

        tmp_path = file_path + ".tmp"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(cleaned, f, indent=4, ensure_ascii=False)
        os.replace(tmp_path, file_path)

        print(f"\n{Fore.GREEN}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.GREEN}{Style.BRIGHT}✨ Done! File cleaned and saved successfully.{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.WHITE}📊 Total processed: {Fore.YELLOW}{total_found}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}🗑️  Blacklisted removed: {Fore.RED}{blacklisted}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}🔄 Duplicates removed: {Fore.YELLOW}{duplicates}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}✅ Final valid unique: {Fore.GREEN}{Style.BRIGHT}{len(cleaned)}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}=======================================================\n{Style.RESET_ALL}")
        return True


def main():
    config = AccountsConfig()
    parser = argparse.ArgumentParser(description="Smart Genspark accounts cleaner")
    parser.add_argument("-f", "--file", type=str, default=config.target_file)
    parser.add_argument("--all-fields", action="store_true")
    parser.add_argument("--no-shuffle", action="store_true")
    parser.add_argument("--no-dedupe", action="store_true")
    parser.add_argument("--no-backup", action="store_true")
    parser.add_argument("--remove-domain", type=str, action="append")
    args = parser.parse_args()

    config.target_file = args.file
    if args.all_fields:
        config.email_pass_only = False
    if args.no_shuffle:
        config.shuffle = False
    if args.no_dedupe:
        config.deduplicate = False
    if args.no_backup:
        config.make_backup = False
    if args.remove_domain:
        config.blacklisted_domains.extend(args.remove_domain)

    config.print_banner()
    cleaner = AccountsCleaner(config)
    cleaner.process()


if __name__ == "__main__":
    main()


------------------------------------------


🧭 خطة تطوير وتنفيذ — منظف حسابات Genspark (من V3 إلى V4)
الهدف: تحويل السكربت الحالي من سكربت "ماشي حاله" إلى محرك تنظيف ببلاين مرن، قابل للتوسع، سلس الصيانة، متوافق عبر الأنظمة، وقابل للاختبار — مع الحفاظ على نفس الوظائف التي يقدمها حالياً (قراءة JSON المكسور، توحيد، حذف دومينات محظورة، حذف التكرارات، خلط، نسخة احتياطية، كتابة ذرية، طباعة ملونة).

1. تشخيص مشاكل السكربت الحالي (قبل التعديل)
#	المشكلة	مكان السبب	التأثير
1	بنية متجانسة (Monolithic) — كل المنطق داخل دالة process() وكلاسات كبيرة	AccountsCleaner.process	صعوبة الإضافة/الاختبار
2	تكرار كود الألوان/اللوج ووجود روابط Markdown داخل f-strings بالخطأ مثل {[Fore.GREEN](http://Fore.GREEN)}	log_* وprint_banner	كسر الـ syntax لو نُسخ الكود + مظهر مكسور في التيرمينال
3	الـ Regex بسيط جداً — يفشل لو الإيميل/الباس وُجدت بعلامات مفردة، أو ترتيب معكوس، أو بمسافات، أو keys بديلة (user/pass/mail/username)	extract_raw_accounts	فقدان حسابات / قراءة ناقصة
4	لا توجد طباعة تطبيع (normalize) — الإيميلات تظل بحالات مختلفة، المسافات تسبب تكرارات غير مكتشفة	loop inside process	نتائج dedupe غير دقيقة
5	كتابة ذرية ناقصة — لا يوجد fsync، ولا يتم تنظيف الملف المؤقت عند الفشل	atomic write section	خطر تلف الملف في حال انقطاع العملية
6	النسخ الاحتياطي ينشئ ملف .bak واحد فقط ويدمر السابق بلا تدوير	shutil.copy2(file_path, backup_path)	ضياع نسخ قديمة / صعوبة التراجع
7	الإعدادات صلبة — لا توجد وسيلة لتحميل config من ملف (JSON/TOML) وبعض الخيارات غير موجودة (min password length, email validation, seed للـ shuffle)	AccountsConfig + main()	ضعف المرونة والتوسع
8	Banner مدمج داخل Config — فصل اهتمامات سيئ (Config لا يجب أن يطبع)	AccountsConfig.print_banner()	تصميم غير نظيف
9	لا توجد كائن تقرير (Report) — النتائج تُطبع فقط ولا تُرجع بشكل برمجي	process()	لا يمكن استدعاء السكربت من كود آخر أو اختباره بسهولة
10	الاستثناءات تُبلع بـ except Exception: pass وexcept Exception: عامة	متعددة	إخفاء أخطاء حقيقية
11	دعم ويندوز جزئي فقط — لا معالجة لـ stderr، ولا utf-8-sig لملفات UTF-8 BOM	أعلى الملف	مشاكل في ويندوز
12	CLI محدود — لا يوجد -o, -c, -v/-q, --dedupe-field, --min-pass-len, إلخ	argparse	قابلية استخدام ضعيفة
13	لا توجد طبقات (layers) — Logging / Config / Parsing / Pipeline / IO جميعها مختلطة	الملف ككل	صعوبة إضافة مزايا
14	دوال متغيرة الطباعة ثابتة لا يمكن تغيير مستوى الإسهاب بسهولة	log_*	تجربة استخدام سيئة
15	عدم دعم ملفات الإخراج المنفصلة (يُجبر على الكتابة فوق الملف الأصلي)	process()	خطر على البيانات الأصلية
2. الرؤية بعد التطوير (V4.0) — المبادئ المعمارية
Pipeline / Stages نقية: كل مرحلة (normalize → validate → blacklist → dedupe → keep-fields → shuffle) هي دالة مستقلة تأخذ قائمة وتُرجع قائمة وتحدّث كائن التقرير.
انفصال المسؤوليات (Separation of Concerns):
Config لإدارة الإعدادات فقط.
Logging موحد وملوّن وقابل لضبط المستوى.
Parser/Extractor قوي مع 3 مستويات fallback.
Pipeline stages قابلة للاختبار.
IO layer للنسخ الاحتياطي والكتابة الذرية الآمنة.
قابلية التوسع: إضافة مرحلة جديدة (مثل stage_rate_limit_check) لا تتطلب إلا إضافة دالة وإدراجها في تابل PIPELINE.
التوافق: يعمل على لينكس/ماك/ويندوز، مع معالجة الـ BOM، إعادة تكوين الترميز، ولون اختياري.
البرمجية/الاختبارية: يمكن استيراد AccountsCleaner واستدعاء run() من سكربتات أخرى والحصول على CleanReport.
التسامح مع الأخطاء: استثناءات واضحة، رسائل مفيدة، وتنظيف الموارد.
3. خطة تنفيذ مقترحة (مقسمة على مراحل)
المرحلة 0 — الاحتياطات والهيكلية
 حفظ نسخة من السكربت الأصلي (
original_original.py
).
 إنشاء ملف جديد
cleaner.py
 بدلاً من التعديل المباشر على القديم.
 إضافة README.md + config.example.json لاحقاً (اختياري).
المرحلة 1 — البنية التحتية
ترميز آمن: _ensure_utf8_stdout() لـ stdout وstderr قبل أي طباعة.
ألوان آمنة: fallback كامل بدون استثناءات مبعثرة.
Logging موحد: استخدام logging القياسي مع ColorFormatter + مستوى SUCCESS مخصص + دعم -v/-q.
pathlib.Path في كامل التعامل مع الملفات بدلاً من os.path (أكثر وضوحاً وأقل أخطاء).
المرحلة 2 — الإعدادات (Config)
نقل الإعدادات إلى @dataclass CleanerConfig مع:
output_file للكتابة في ملف مختلف.
dedupe_field, case_insensitive_dedupe.
shuffle_seed, backup_dir, max_backups, indent, ensure_ascii.
min_password_length, email_validation, keep_fields.
إضافة CleanerConfig.from_file(path) لتحميل إعدادات من ملف JSON.
CLI يقوم بالترتيب: defaults → config file → CLI flags ويعرضها في Banner.
المرحلة 3 — الاستخراج القوي (Extractor)
سلسلة fallback من ثلاث طبقات:

json.loads الرسمي.
_attempt_json_recovery: إزالة trailing commas والقص خارج الأقواس وإعادة المحاولة.
_regex_extract: regex متسامح مع ' و"، مع مفاتيح بديلة (email/mail/username/user، password/pass/passwd/pw)، ويدعم إعادة بناء الكائنات من تتابع الأزواج.
_tree_to_accounts: ينزل في الشجرة (dict/list) ليجمع الحسابات مهما كان عمق التداخل، ويبحث عن مفاتيح شائعة (accounts, data, items, users, …).
المرحلة 4 — Pipeline (القلب)
تعريف Stage = Callable[[List[Account], CleanerConfig, CleanReport], List[Account]] ثم المراحل:

stage_normalize — استخراج email/password من مفاتيح متعددة، lower(), strip().
stage_validate — فحص صيغة الإيميل + طول كلمة المرور.
stage_blacklist — فحص email, provider, mailbox_url, domain.
stage_dedupe — حسب حقل قابل للتكوين، case-insensitive افتراضياً.
stage_keep_fields — يحتفظ فقط بالحقول المطلوبة عند تشغيل email_pass_only.
stage_shuffle — خلط بـ random.Random(seed) أو SystemRandom لعدم التكرار.
هذا هو أهم تحسين معياري لأنه يجعل إضافة/إزالة/إعادة ترتيب المراحل مسألة سطر واحد في PIPELINE.

المرحلة 5 — IO آمن
make_backup يُنشئ نسخة باسم file.json.bak.YYYYMMDD-HHMMSS، مع backup_dir اختياري، ويدور القديم (max_backups).
atomic_write_json يكتب في ملف مؤقت داخل نفس المجلد، يعمل flush + fsync، ثم os.replace، ويزيل المؤقت عند الفشل.
المرحلة 6 — المحرك + التقرير
كلاس AccountsCleaner(config, logger) يُعيد CleanReport (بيانات برمجية) بالإضافة إلى الطباعة.
فصل print_banner() خارج Config إلى المحرك.
دالة main() ترجع exit code (0/1/2) ويتم استدعاؤها عبر sys.exit(main()).
المرحلة 7 — CLI موسّع
إضافة الخيارات الجديدة:

-o/--output, -c/--config, -v/--verbose, -q/--quiet, --no-banner.
--no-dedupe, --dedupe-field, --no-shuffle, --shuffle-seed.
--no-backup, --backup-dir, --max-backups.
--remove-domain (موجود، مُحسَّن لإزالة التكرار في القائمة).
--min-pass-len, --no-email-check.
4. أمثلة "قبل / بعد" لتنفيذ التعديلات مباشرة في محرر الأكواد
📌 كل مقطع أدناه يُظهر الكود كما هو في النسخة الحالية (قبل) ثم الكود المُعاد تصميمه (بعد) حتى تتمكن من تطبيق التعديل تباعاً في محررك.

🔧 التعديل 1 — إصلاح خطأ الـ f-string المكسور + دعم ترميز قوي (أعلى الملف)
قبل:

Python

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    class EmptyColor:
        CYAN = GREEN = YELLOW = RED = MAGENTA = WHITE = ""
    class EmptyStyle:
        BRIGHT = RESET_ALL = ""
    Fore = EmptyColor()
    Style = EmptyStyle()

def log_info(msg: str):
    print(f"{Fore.CYAN}ℹ️  {msg}{Style.RESET_ALL}")
def log_success(msg: str):
    print(f"{[Fore.GREEN](http://Fore.GREEN)}✅ {msg}{Style.RESET_ALL}")
def log_warn(msg: str):
    print(f"{Fore.YELLOW}⚠️  {msg}{Style.RESET_ALL}")
def log_error(msg: str):
    print(f"{[Fore.RED](http://Fore.RED)}❌ {msg}{Style.RESET_ALL}")
بعد:

Python

def _ensure_utf8_stdout() -> None:
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        if stream is None or not hasattr(stream, "reconfigure"):
            continue
        enc = getattr(stream, "encoding", None)
        if not enc or enc.lower().replace("-", "") != "utf8":
            try:
                stream.reconfigure(encoding="utf-8")
            except Exception:
                pass

_ensure_utf8_stdout()

try:
    from colorama import Fore, Style, init as _colorama_init
    _colorama_init(autoreset=True)
    _COLOR = True
except ImportError:
    _COLOR = False
    class _Dummy:
        def __getattr__(self, _name: str) -> str:
            return ""
    Fore = _Dummy()
    Style = _Dummy()

import logging

class ColorFormatter(logging.Formatter):
    LEVEL_COLORS = {
        logging.DEBUG:    (Fore.CYAN,   "🔍"),
        logging.INFO:     (Fore.CYAN,   "ℹ️ "),
        logging.WARNING:  (Fore.YELLOW, "⚠️ "),
        logging.ERROR:    (Fore.RED,    "❌"),
        logging.CRITICAL: (Fore.MAGENTA + (Style.BRIGHT if _COLOR else ""), "💥"),
    }
    SUCCESS = 25
    logging.addLevelName(SUCCESS, "SUCCESS")

    def format(self, record):
        color, icon = self.LEVEL_COLORS.get(record.levelno, ("", "•"))
        reset = Style.RESET_ALL if _COLOR else ""
        bright = Style.BRIGHT if _COLOR else ""
        return f"{color}{bright}{icon} {record.getMessage()}{reset}"

def build_logger(verbose=False, quiet=False):
    logger = logging.getLogger("genspark.cleaner")
    logger.handlers.clear()
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(ColorFormatter())
    logger.addHandler(h)
    logger.setLevel(logging.ERROR if quiet else (logging.DEBUG if verbose else logging.INFO))
    def _success(msg, *a, **kw): logger.log(ColorFormatter.SUCCESS, msg, *a, **kw)
    logger.success = _success
    return logger

log = build_logger()
🔧 التعديل 2 — فصل الـ Config عن الـ Banner + إضافة خيارات جديدة
قبل:

Python

@dataclass
class AccountsConfig:
    target_file: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts-example.json")
    email_pass_only: [REDACTED:KV_SECRET] = True
    deduplicate: bool = True
    shuffle: bool = True
    make_backup: bool = True
    blacklisted_domains: List[str] = field(default_factory=lambda: ["mailnesia.com", "mailnesia"])

    def print_banner(self):
        ...
بعد:

Python

from pathlib import Path

@dataclass
class CleanerConfig:
    target_file: Path = Path("accounts.json")
    output_file: Optional[Path] = None
    email_pass_only: [REDACTED:KV_SECRET] = True
    deduplicate: bool = True
    dedupe_field: str = "email"
    case_insensitive_dedupe: bool = True
    shuffle: bool = True
    shuffle_seed: Optional[int] = None
    make_backup: bool = True
    backup_dir: Optional[Path] = None
    max_backups: int = 5
    blacklisted_domains: Set[str] = field(default_factory=lambda: {"mailnesia.com", "mailnesia"})
    indent: int = 4
    ensure_ascii: bool = False
    min_password_length: int = 0
    email_validation: bool = True
    keep_fields: Tuple[str, ...] = ("email", "password")
    pretty_banner: bool = True

    def add_domains(self, domains):
        for d in domains:
            d = (d or "").strip().lower()
            if d:
                self.blacklisted_domains.add(d)
✅ ملاحظة: البانر بقي داخل AccountsCleaner.print_banner() وليس داخل Config (فصل اهتمامات).

🔧 التعديل 3 — استخراج قوي للـ JSON المكسور (Extractor)
قبل:

Python

def extract_raw_accounts(self, content: str) -> List[Dict[str, Any]]:
    accounts = []
    try:
        parsed = json.loads(content)
        if isinstance(parsed, list):
            accounts = parsed
        elif isinstance(parsed, dict):
            accounts = parsed.get("accounts", parsed.get("data", []))
    except Exception:
        log_warn("الملف يحتوي على تداخل أو صيغة JSON مكسورة...")

    if not accounts:
        pattern = re.compile(r'"email"\s*:\s*"([^"]+)",\s*"password"\s*:\s*"([^"]+)"')
        matches = pattern.findall(content)
        for email, password in matches:
            accounts.append({"email": email.strip(), "password": password.strip()})
    return accounts
بعد:

Python

_KV_RE = re.compile(
    r"""['"]?(email|password|provider|mailbox_url|mail|pass|passwd|username|user)['"]?\s*[:=]\s*['"]([^'"]*)['"]""",
    re.IGNORECASE,
)

def _attempt_json_loads(content):
    try: return json.loads(content)
    except json.JSONDecodeError: return None

def _attempt_json_recovery(content):
    fixed = re.sub(r",\s*([\]}])", r"\1", content)
    fixed = re.sub(r"^[^{[]*", "", fixed)
    fixed = re.sub(r"[^}\]]*$", "", fixed)
    try: return json.loads(fixed)
    except json.JSONDecodeError: return None

def _regex_extract(content):
    entries, current = [], {}
    for m in _KV_RE.finditer(content):
        key, val = m.group(1).lower(), m.group(2).strip()
        key = "[REDACTED:KV_SECRET]" if key in ("email","mail","username","user") else (
              "password" if key in ("password","pass","passwd","pw") else key)
        if key == "email" and "email" in current:
            if current.get("email") and current.get("password"):
                entries.append(dict(current))
            current = {}
        current[key] = val
    if current.get("email") and current.get("password"):
        entries.append(dict(current))
    return entries

def _tree_to_accounts(node):
    results = []
    if isinstance(node, list):
        for it in node: results.extend(_tree_to_accounts(it))
    elif isinstance(node, dict):
        if any(k in node for k in ("email","mail","username","user","password","pass")):
            results.append(node)
        else:
            for k in ("accounts","data","items","list","result","users"):
                if k in node:
                    results.extend(_tree_to_accounts(node[k])); break
            else:
                for v in node.values():
                    if isinstance(v, (dict, list)): results.extend(_tree_to_accounts(v))
    return results

def extract_raw_accounts(content):
    if not content.strip(): return []
    parsed = _attempt_json_loads(content) or _attempt_json_recovery(content)
    if parsed is not None:
        return _tree_to_accounts(parsed)
    return _regex_extract(content)
🔧 التعديل 4 — استبدال الحلقة المتجانسة بـ Pipeline من مراحل
قبل:

Python

cleaned_accounts = []
seen_emails: Set[str] = set()
blacklisted_count = 0
duplicate_count = 0

for acc in raw_list:
    if not isinstance(acc, dict): continue
    email = str(acc.get("email", "")).strip()
    password = [REDACTED:KV_SECRET]"password", "")).strip()
    if not email: continue
    if self.is_blacklisted(email, acc):
        blacklisted_count += 1; continue
    email_key = [REDACTED:KV_SECRET]
    if self.config.deduplicate:
        if email_key in seen_emails:
            duplicate_count += 1; continue
        seen_emails.add(email_key)
    item = {"email": email, "password": password} if self.config.email_pass_only else acc
    cleaned_accounts.append(item)
بعد:

Python

PIPELINE = (
    stage_normalize,
    stage_validate,
    stage_blacklist,
    stage_dedupe,
    stage_keep_fields,
    stage_shuffle,
)

accounts = raw_list
for stage in PIPELINE:
    accounts = stage(accounts, cfg, rep)
    log.debug(f"After {stage.__name__}: {len(accounts)} accounts")
كل مرحلة دالة منفصلة تأخذ (accounts, config, report) وتُرجع القائمة الجديدة — مثال على واحدة:

Python

def stage_dedupe(accounts, cfg: CleanerConfig, rep: CleanReport):
    if not cfg.deduplicate: return accounts
    seen, out = set(), []
    for acc in accounts:
        key = [REDACTED:KV_SECRET], "")).strip()
        if not key:
            rep.invalid_entries += 1; continue
        if cfg.case_insensitive_dedupe:
            key = [REDACTED:KV_SECRET]
        if key in seen:
            rep.duplicates += 1; continue
        seen.add(key); out.append(acc)
    return out
🔧 التعديل 5 — نسخ احتياطي دائري + كتابة ذرية آمنة مع fsync
قبل:

Python

if self.config.make_backup:
    backup_path = file_path + ".bak"
    shutil.copy2(file_path, backup_path)
    log_info(f"تم إنشاء نسخة احتياطية آمنة في: {backup_path}")

tmp_path = file_path + ".tmp"
with open(tmp_path, "w", encoding="utf-8") as f:
    json.dump(cleaned_accounts, f, indent=4, ensure_ascii=False)
os.replace(tmp_path, file_path)
بعد:

Python

import tempfile, time
from datetime import datetime

def make_backup(src: Path, cfg: CleanerConfig) -> Optional[Path]:
    if not cfg.make_backup or not src.exists():
        return None
    backup_dir = (cfg.backup_dir or src.parent).expanduser()
    backup_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    # تدوير: حذف الأقدم عند تجاوز الحد
    existing = sorted(backup_dir.glob(f"{src.name}.bak.*"))
    while len(existing) >= cfg.max_backups:
        try: existing[0].unlink()
        except OSError: pass
        existing.pop(0)
    dst = backup_dir / f"{src.name}.bak.{ts}"
    shutil.copy2(src, dst)
    return dst

def atomic_write_json(target: Path, data, indent=4, ensure_ascii=False):
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(prefix=target.name + ".", suffix=".tmp", dir=str(target.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=indent, ensure_ascii=ensure_ascii)
            fh.flush(); os.fsync(fh.fileno())
        os.replace(tmp_path, target)
    except Exception:
        try: os.unlink(tmp_path)
        except OSError: pass
        raise
🔧 التعديل 6 — التقرير المُرجَع (Programmatic Report) + رسائل خروج نظيفة
قبل:

Python

# الطباعة فقط، لا يوجد كائن ناتج
print(...); return True
بعد:

Python

@dataclass
class CleanReport:
    total_found: int = 0
    invalid_entries: int = 0
    blacklisted: int = 0
    duplicates: int = 0
    invalid_email: int = 0
    short_password: int = 0
    final_count: int = 0
    backup_path: Optional[Path] = None
    output_path: Optional[Path] = None
    elapsed_ms: float = 0.0
ويُرجع من:

Python

def run(self) -> CleanReport:
    rep = CleanReport()
    t0 = time.perf_counter()
    # ... (load → pipeline → backup → atomic write) ...
    rep.final_count = len(accounts)
    rep.elapsed_ms = (time.perf_counter() - t0) * 1000.0
    self._print_report(rep)
    return rep
🔧 التعديل 7 — CLI موسّع (مطابق لخطة التوسع)
قبل:

Python

parser.add_argument("-f", "--file", ...)
parser.add_argument("--all-fields", ...)
parser.add_argument("--no-shuffle", ...)
parser.add_argument("--no-dedupe", ...)
parser.add_argument("--no-backup", ...)
parser.add_argument("--remove-domain", ...)
بعد:

Python

p.add_argument("-f", "--file", type=Path, default=None)
p.add_argument("-o", "--output", type=Path, default=None)
p.add_argument("-c", "--config", type=Path, default=None)
p.add_argument("--all-fields", action="store_true")
p.add_argument("--no-shuffle", action="store_true")
p.add_argument("--shuffle-seed", type=int, default=None)
p.add_argument("--no-dedupe", action="store_true")
p.add_argument("--dedupe-field", type=str, default=None)
p.add_argument("--no-backup", action="store_true")
p.add_argument("--backup-dir", type=Path, default=None)
p.add_argument("--max-backups", type=int, default=None)
p.add_argument("--remove-domain", action="append", default=None)
p.add_argument("--min-pass-len", type=int, default=None)
p.add_argument("--no-email-check", action="store_true")
p.add_argument("-v", "--verbose", action="store_true")
p.add_argument("-q", "--quiet", action="store_true")
p.add_argument("--no-banner", action="store_true")
مع ترتيب تطبيق:

Python

# defaults -> config file -> CLI
cfg = CleanerConfig()
if args.config:
    cfg = CleanerConfig.from_file(args.config.expanduser())
cfg = _apply_cli_overrides(cfg, args)
5. نتائج متوقعة بعد التطوير
🚀 مرونة عالية: كل مرحلة مستقلة، يمكن تعطيلها أو استبدالها أو إضافة مراحل جديدة بسهولة.
🧩 قابلية التوسع: يمكن إضافة ميزات مثل التحقق من صلاحية الحساب (rate limit test) أو استيراد من CSV/TXT ببساطة.
🛡️ أمان أعلى: كتابة ذرية حقيقية مع fsync + نسخ احتياطية مدوّرة بطابع زمني.
🪟 توافق محسّن مع ويندوز/ماك/لينكس ومع ملفات UTF-8 BOM.
🧪 سهولة الاختبار: AccountsCleaner.run() يُرجع CleanReport؛ وكل stage دالة نقية.
🧰 CLI احترافي مع دعم config file، مستويات إسهاب، ومسارات مخصصة.
🧹 كود أنظف: إزالة التكرار، إزالة الـ f-strings المكسورة، فصل اهتمامات واضح.
6. خطوات مقترحة للتطبيق في محرر الأكواد
انسخ الملف الأصلي إلى
original_original.py
 احتياطياً.
أنشئ ملف جديد باسم
cleaner.py
 والصق بداخله النسخة V4 المرفقة (
cleaner.py
).
اختبار سريع:
Bash

python cleaner.py -f accounts-example.json --no-backup -v
اختبار خيارات إضافية:
Bash

python cleaner.py -f accounts.json -o cleaned.json --remove-domain example.com --shuffle-seed 42
(اختياري) أنشئ config.example.json:
JSON

{
  "target_file": "accounts.json",
  "email_pass_only": true,
  "deduplicate": true,
  "shuffle": true,
  "make_backup": true,
  "max_backups": 10,
  "blacklisted_domains": ["mailnesia.com", "throwaway.tld"],
  "min_password_length": 4,
  "email_validation": true
}
(اختياري لاحقاً) أضف pytest tests لكل stage.
7. قائمة التحقق (Checklist) النهائية
 إزالة جميع الـ f-strangs المكسورة {[Fore.*](http://...)}.
 استخدام pathlib.Path بدلاً من os.path.
 استبدال log_* المنفصلة بـ logging موحد.
 فصل البانر خارج Config.
 استبدال الحلقة الكبيرة في process() بالـ pipeline.
 استخدام atomic_write_json مع fsync.
 نسخ احتياطية مدوّرة بطابع زمني.
 إرجاع CleanReport من run().
 CLI موسّع مع -o/-c/-v/-q.
 sys.exit(main()) مع أكواد خروج.
تم تجهيز النسخة المُعاد بناؤها بالكامل في الملف
cleaner.py
، ويمكن اعتمادها مباشرة كبديل عن السكربت الحالي مع الحفاظ على النسخة الأصلية في
original_original.py
 للمراجعة.


-------------
# خطة تنفيذية شاملة لإعادة هيكلة السكربت

## 📋 تحليل المشاكل الحالية

| # | المشكلة | التأثير |
|---|---------|---------|
| 1 | **Mixin للـ Logging** عبر 4 دوال منفصلة (`log_info`, `log_success`, `log_warn`, `log_error`) | تكرار وقابلية توسع ضعيفة |
| 2 | **Hard-coded** لمسار الملف داخل `Config` | غير مرن، يخالف مبدأ SRP |
| 3 | **سلسلة الـ if/elif** في `extract_raw_accounts` | تكرار منطق، قابلية اختبار ضعيفة |
| 4 | **عدم فصل الـ I/O** عن منطق التنظيف | صعوبة الاختبار والصيانة |
| 5 | **Color coupling** داخل منطق `process()` | خلط المسؤوليات |
| 6 | **`extract_raw_accounts`** يرجع `accounts` متغير global قد يتلوث | bug محتمل |
| 7 | **لا يوجد progress indicator** للملفات الكبيرة | UX سيئ |
| 8 | **الـ Blacklist** مخزنة كـ string فقط بدون email validation | سهل التهرب |
| 9 | **لا يوجد `__repr__` أو `__str__`** في الـ dataclasses | debugging صعب |
| 10 | **لا يوجد `dry-run` mode** | مخاطرة عالية بدون معاينة |

---

## 🎯 خطة التحسين المقترحة (Roadmap)

### المرحلة 1: إعادة الهيكلة المعمارية (Architecture Refactor)
- تطبيق **Strategy Pattern** لمحركات الاستخراج (JSON parser, Regex parser, Line parser)
- فصل الطبقات إلى modules:
  - `config.py` → الإعدادات
  - `extractors/` → استراتيجيات الاستخراج
  - `filters/` → استراتيجيات التصفية
  - `reporter.py` → التقارير
  - `logger.py` → نظام السجلات
  - `core.py` → المحرك الرئيسي

### المرحلة 2: SOLID Principles
- **S** (Single Responsibility): كل class له وظيفة واحدة
- **O** (Open/Closed): إضافة مستخرجات جديدة بدون تعديل الكود الحالي
- **L** (Liskov Substitution): واجهات موحدة
- **I** (Interface Segregation): فصل الواجهات الكبيرة
- **D** (Dependency Inversion): الاعتماد على Abstractions

### المرحلة 3: ميزات جديدة
- ✅ `dry-run` mode للمعاينة
- ✅ `progress bar` للملفات الضخمة
- ✅ `pipeline` قابل للتخصيص (chain of responsibility)
- ✅ دعم صيغ إدخال متعددة (JSON, JSONL, CSV, TXT)
- ✅ `validation` قوي للإيميلات
- ✅ `report file` (JSON/HTML)
- ✅ `plugins system` لإضافة فلاتر مخصصة

### المرحلة 4: الجودة والاختبار
- إضافة **type hints** كاملة
- إضافة **docstrings** عربية وإنجليزية
- استخدام **logging** بدلاً من print
- إضافة **custom exceptions**

---

## 🔄 مقارنة قبل وبعد

| الجانب | قبل ❌ | بعد ✅ |
|--------|--------|--------|
| عدد الملفات | 1 (350 سطر) | 8 modules (~80 سطر لكل واحد) |
| قابلية الاختبار | صعبة | سهلة (كل module مستقل) |
| إضافة مستخرج جديد | تعديل الكود | فقط أضف class جديد |
| إضافة فلتر جديد | تعديل الكود | فقط أضف class جديد |
| Dry-run | غير موجود | مدعوم |
| Progress bar | غير موجود | مدعوم |
| Type safety | ضعيف | كامل |
| صيغ الإدخال | JSON فقط | JSON, JSONL, CSV, TXT |
| التقرير | Console فقط | Console + File (JSON/HTML) |
| Logging | print عادي | structured logging |

---

## 💻 الكود - قبل وبعد

### 📁 هيكل المشروع الجديد

```
accounts_cleaner/
├── __init__.py
├── __main__.py
├── config.py
├── logger.py
├── core.py
├── extractors/
│   ├── __init__.py
│   ├── base.py
│   ├── json_extractor.py
│   ├── regex_extractor.py
│   └── line_extractor.py
├── filters/
│   ├── __init__.py
│   ├── base.py
│   ├── blacklist_filter.py
│   ├── dedup_filter.py
│   └── validator_filter.py
├── transformers/
│   ├── __init__.py
│   ├── base.py
│   ├── simplify_transformer.py
│   └── shuffle_transformer.py
├── writers/
│   ├── __init__.py
│   ├── base.py
│   └── atomic_json_writer.py
├── reporter.py
└── exceptions.py
```

---

### 🔴 قبل (الكود الحالي - معاد تنظيمه)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""سكريبت تنظيف وتوحيد حسابات Genspark الذكي - V3.0"""

import json
import re
import os
import sys
import shutil
import random
import argparse
from dataclasses import dataclass, field
from typing import List, Dict, Any, Set

# ─── معالجة تشفير التيرمينال لويندوز ──────────────────────────────────────────
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ─── دعم الألوان عبر colorama مع fallback آمن ────────────────────────────────
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    class EmptyColor:
        CYAN = GREEN = YELLOW = RED = MAGENTA = WHITE = ""
    class EmptyStyle:
        BRIGHT = RESET_ALL = ""
    Fore = EmptyColor()
    Style = EmptyStyle()


def log_info(msg: str):
    print(f"{Fore.CYAN}ℹ️  {msg}{Style.RESET_ALL}")


def log_success(msg: str):
    print(f"{Fore.GREEN}✅ {msg}{Style.RESET_ALL}")


def log_warn(msg: str):
    print(f"{Fore.YELLOW}⚠️  {msg}{Style.RESET_ALL}")


def log_error(msg: str):
    print(f"{Fore.RED}❌ {msg}{Style.RESET_ALL}")


# ─── ⚙️ كلاس الإعدادات الذكي (Config Manager) ─────────────────────────────
@dataclass
class AccountsConfig:
    """كلاس الإعدادات المركزية لإدارة وتنظيف الحسابات"""
    target_file: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts-example.json")
    email_pass_only: [REDACTED:KV_SECRET] = True
    deduplicate: bool = True
    shuffle: bool = True
    make_backup: bool = True
    blacklisted_domains: List[str] = field(default_factory=lambda: ["mailnesia.com", "mailnesia"])

    def print_banner(self):
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.CYAN}{Style.BRIGHT}🚀 منظف وموحد الحسابات الذكي - Smart Accounts Cleaner V3.0{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 الملف المستهدف: {Fore.YELLOW}{self.target_file}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 توحيد ميل وباص فقط: {Fore.GREEN if self.email_pass_only else Fore.RED}{self.email_pass_only}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 استبعاد التكرارات: {Fore.GREEN if self.deduplicate else Fore.RED}{self.deduplicate}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 ترتيب عشوائي: {Fore.GREEN if self.shuffle else Fore.RED}{self.shuffle}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 الدومينات المحظورة: {Fore.RED}{self.blacklisted_domains}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}-------------------------------------------------------{Style.RESET_ALL}\n")


# ─── 🔍 المحرك الأساسي للتنظيف (Accounts Cleaner Engine) ────────────────────
class AccountsCleaner:
    def init(self, config: AccountsConfig):
        self.config = config

    def extract_raw_accounts(self, content: str) -> List[Dict[str, Any]]:
        accounts = []
        try:
            parsed = json.loads(content)
            if isinstance(parsed, list):
                accounts = parsed
            elif isinstance(parsed, dict):
                accounts = parsed.get("accounts", parsed.get("data", []))
        except Exception:
            log_warn("الملف يحتوي على تداخل، جاري الاستخراج عبر Regex الذكي...")

        if not accounts:
            pattern = re.compile(r'"email"\s*:\s*"([^"]+)",\s*"password"\s*:\s*"([^"]+)"')
            matches = pattern.findall(content)
            for email, password in matches:
                accounts.append({
                    "email": email.strip(),
                    "password": password.strip()
                })
        return accounts

    def is_blacklisted(self, email: str, account_dict: Dict[str, Any]) -> bool:
        email_lower = email.lower()
        provider_lower = str(account_dict.get("provider", "")).lower()
        url_lower = str(account_dict.get("mailbox_url", "")).lower()
        for domain in self.config.blacklisted_domains:
            domain_lower = domain.lower()
            if domain_lower in email_lower or domain_lower in provider_lower or domain_lower in url_lower:
                return True
        return False

    def process(self):
        file_path = self.config.target_file
        if not os.path.exists(file_path):
            log_error(f"الملف المطلوب غير موجود: {file_path}")
            return False

        log_info(f"جاري قراءة وتجهيز الملف: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()

        raw_list = self.extract_raw_accounts(content)
        total_found = len(raw_list)
        log_info(f"تم العثور على إجمالي {total_found} إدخال حساب في الملف.")

        cleaned_accounts = []
        seen_emails: Set[str] = set()
        blacklisted_count = 0
        duplicate_count = 0

        for acc in raw_list:
            if not isinstance(acc, dict):
                continue
            email = str(acc.get("email", "")).strip()
            password = [REDACTED:KV_SECRET]"password", "")).strip()
            if not email:
                continue
            if self.is_blacklisted(email, acc):
                blacklisted_count += 1
                continue
            email_key = [REDACTED:KV_SECRET]
            if self.config.deduplicate:
                if email_key in seen_emails:
                    duplicate_count += 1
                    continue
                seen_emails.add(email_key)
            if self.config.email_pass_only:
                item = {"email": email, "password": password}
            else:
                item = acc
            cleaned_accounts.append(item)

        if self.config.shuffle:
            random.seed()
            random.shuffle(cleaned_accounts)
            log_info("تم خلط ترتيب الحسابات بشكل عشوائي (Shuffle).")

        if self.config.make_backup:
            backup_path = file_path + ".bak"
            shutil.copy2(file_path, backup_path)
            log_info(f"تم إنشاء نسخة احتياطية في: {backup_path}")

        tmp_path = file_path + ".tmp"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(cleaned_accounts, f, indent=4, ensure_ascii=False)
        os.replace(tmp_path, file_path)

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✨ تم بنجاح!{Style.RESET_ALL}")
        return True


def main():
    config = AccountsConfig()
    parser = argparse.ArgumentParser(description="أداة تنظيف حسابات Genspark")
    parser.add_argument("-f", "--file", type=str, default=config.target_file)
    parser.add_argument("--all-fields", action="store_true")
    parser.add_argument("--no-shuffle", action="store_true")
    parser.add_argument("--no-dedupe", action="store_true")
    parser.add_argument("--no-backup", action="store_true")
    parser.add_argument("--remove-domain", type=str, action="append")
    args = parser.parse_args()

    config.target_file = args.file
    if args.all_fields: config.email_pass_only = False
    if args.no_shuffle: config.shuffle = False
    if args.no_dedupe: config.deduplicate = False
    if args.no_backup: config.make_backup = False
    if args.remove_domain: config.blacklisted_domains.extend(args.remove_domain)

    config.print_banner()
    cleaner = AccountsCleaner(config)
    cleaner.process()


if __name__ == "__main__":
    main()
```

---

### 🟢 بعد (الكود الجديد - كامل ومُحسَّن)

#### 1️⃣ `accounts_cleaner/exceptions.py`

```python
"""Custom exceptions for the accounts cleaner module."""


class AccountsCleanerError(Exception):
    """Base exception for all accounts cleaner errors."""
    pass


class ExtractionError(AccountsCleanerError):
    """Raised when extraction of accounts fails."""
    pass


class FilterError(AccountsCleanerError):
    """Raised when a filter operation fails."""
    pass


class WriteError(AccountsCleanerError):
    """Raised when writing output fails."""
    pass


class ConfigError(AccountsCleanerError):
    """Raised when configuration is invalid."""
    pass
```

#### 2️⃣ `accounts_cleaner/logger.py`

```python
"""Centralized logging with color support and rich features."""
from __future__ import annotations

import logging
import sys
from typing import Optional

try:
    from colorama import Fore, Style, init as colorama_init
    colorama_init(autoreset=True)
    HAS_COLOR = True
except ImportError:  # pragma: no cover
    HAS_COLOR = False
    class _Empty:
        def __getattr__(self, _: str) -> str: return ""
    Fore = Style = _Empty()


_EMOJIS = {
    "DEBUG": "🔍",
    "INFO": "ℹ️ ",
    "WARNING": "⚠️ ",
    "ERROR": "❌",
    "CRITICAL": "💥",
    "SUCCESS": "✅",
}

_COLORS = {
    "DEBUG": Fore.CYAN,
    "INFO": Fore.CYAN,
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.RED,
    "CRITICAL": Fore.RED,
    "SUCCESS": Fore.GREEN,
}


class EmojiFormatter(logging.Formatter):
    """Custom formatter that adds emojis and colors per level."""

    def format(self, record: logging.LogRecord) -> str:
        level = record.levelname
        emoji = _EMOJIS.get(level, "")
        color = _COLORS.get(level, "")
        message = super().format(record)
        return f"{color}{emoji} {message}{Style.RESET_ALL}" if HAS_COLOR else f"{emoji} {message}"


def get_logger(
    name: str = "accounts_cleaner",
    level: int = logging.INFO,
    log_file: Optional[str] = None,
) -> logging.Logger:
    """Build a logger with consistent handlers and formatting."""
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(level)
    logger.propagate = False

    # Console handler
    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(EmojiFormatter("%(message)s"))
    logger.addHandler(console)

    # Optional file handler
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
        ))
        logger.addHandler(file_handler)

    return logger


def add_success_method(logger: logging.Logger) -> None:
    """Attach a `success` level to the logger (between INFO and WARNING)."""
    logging.SUCCESS = 25  # type: ignore[attr-defined]
    logging.addLevelName(logging.SUCCESS, "SUCCESS")  # type: ignore[attr-defined]

    def _success(message: str, *args, **kwargs) -> None:
        logger.log(logging.SUCCESS, message, *args, **kwargs)  # type: ignore[attr-defined]

    logger.success = _success  # type: ignore[attr-defined]
```

#### 3️⃣ `accounts_cleaner/config.py`

```python
"""Configuration management with validation."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import List, Optional

from .exceptions import ConfigError


@dataclass
class PipelineStep:
    """Describes a single step in the cleaning pipeline."""
    name: str
    enabled: bool = True


@dataclass
class AccountsConfig:
    """Central configuration for the accounts cleaning process."""

    # I/O
    target_file: str = ""
    output_file: Optional[str] = None
    report_file: Optional[str] = None
    log_file: Optional[str] = None

    # Pipeline
    email_pass_only: [REDACTED:KV_SECRET] = True
    deduplicate: bool = True
    shuffle: bool = True
    make_backup: bool = True
    dry_run: bool = False

    # Filters
    blacklisted_domains: List[str] = field(
        default_factory=lambda: ["mailnesia.com", "mailnesia"]
    )
    validate_emails: bool = True
    min_password_length: int = 1

    # Pipeline definition (order matters)
    pipeline: List[str] = field(
        default_factory=lambda: [
            "extract",
            "validate",
            "blacklist",
            "deduplicate",
            "simplify",
            "shuffle",
            "write",
        ]
    )

    def __post_init__(self) -> None:
        if not self.target_file:
            self.target_file = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "..",
                "accounts-example.json",
            )
        if self.output_file is None:
            self.output_file = self.target_file
        self._validate()

    def _validate(self) -> None:
        if not isinstance(self.blacklisted_domains, list):
            raise ConfigError("blacklisted_domains must be a list")
        if self.min_password_length < 0:
            raise ConfigError("min_password_length must be >= 0")
        if not self.pipeline:
            raise ConfigError("pipeline cannot be empty")

    @classmethod
    def from_args(cls, args) -> "AccountsConfig":
        """Build config from parsed CLI arguments."""
        return cls(
            target_file=args.file,
            email_pass_only=not args.all_fields,
            deduplicate=not args.no_dedupe,
            shuffle=not args.no_shuffle,
            make_backup=not args.no_backup,
            dry_run=args.dry_run,
            report_file=args.report,
            log_file=args.log_file,
            blacklisted_domains=[
                "mailnesia.com", "mailnesia",
                *(args.remove_domain or []),
            ],
        )

    def __repr__(self) -> str:
        return (
            f"AccountsConfig(file={self.target_file!r}, "
            f"output={self.output_file!r}, dry_run={self.dry_run})"
        )
```

#### 4️⃣ `accounts_cleaner/extractors/base.py`

```python
"""Base extractor interface following the Strategy pattern."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Dict, Any


class BaseExtractor(ABC):
    """Abstract base for all extraction strategies."""

    name: str = "base"

    @abstractmethod
    def can_handle(self, content: str) -> bool:
        """Return True if this extractor can parse the given content."""
        raise NotImplementedError

    @abstractmethod
    def extract(self, content: str) -> List[Dict[str, Any]]:
        """Extract accounts from the given content."""
        raise NotImplementedError

    def __repr__(self) -> str:  # pragma: no cover
        return f"<{self.__class__.__name__} name={self.name!r}>"
```

#### 5️⃣ `accounts_cleaner/extractors/json_extractor.py`

```python
"""JSON-based extractor (handles well-formed JSON arrays and wrapped objects)."""
from __future__ import annotations

import json
from typing import Any, Dict, List

from .base import BaseExtractor


class JsonExtractor(BaseExtractor):
    """Extract accounts from well-formed JSON content."""

    name = "json"

    def can_handle(self, content: str) -> bool:
        stripped = content.lstrip()
        return stripped.startswith(("{", "["))

    def extract(self, content: str) -> List[Dict[str, Any]]:
        try:
            parsed: Any = json.loads(content)
        except json.JSONDecodeError:
            return []

        if isinstance(parsed, list):
            return [item for item in parsed if isinstance(item, dict)]
        if isinstance(parsed, dict):
            # Try common wrapper keys
            for key in ("accounts", "data", "items", "results", "list"):
                if key in parsed and isinstance(parsed[key], list):
                    return [item for item in parsed[key] if isinstance(item, dict)]
            # Otherwise treat the dict itself as a single account
            return [parsed]
        return []
```

#### 6️⃣ `accounts_cleaner/extractors/regex_extractor.py`

```python
"""Regex-based extractor for broken/malformed JSON."""
from __future__ import annotations

import re
from typing import Dict, List

from .base import BaseExtractor


class RegexExtractor(BaseExtractor):
    """Extract accounts from broken JSON using regex (fallback strategy)."""

    name = "regex"

    # Two patterns: strict (with quotes) and loose (without)
    _STRICT = re.compile(
        r'"email"\s*:\s*"([^"]+)"\s*,\s*"password"\s*:\s*"([^"]*)"',
        re.IGNORECASE,
    )
    _LOOSE = re.compile(
        r'(?P<email>[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,})'
        r'\s*[:,\|;\s]+'
        r'(?P<password>\S+)',
        re.IGNORECASE,
    )

    def can_handle(self, content: str) -> bool:
        return "email" in content.lower() and "password" in content.lower()

    def extract(self, content: str) -> List[Dict[str, str]]:
        accounts: List[Dict[str, str]] = []
        seen_starts = set()

        for match in self._STRICT.finditer(content):
            accounts.append({
                "email": match.group(1).strip(),
                "password": match.group(2).strip(),
            })
            seen_starts.add(match.start())

        for match in self._LOOSE.finditer(content):
            if match.start() in seen_starts:
                continue
            accounts.append({
                "email": match.group("email").strip(),
                "password": match.group("password").strip(),
            })

        return accounts
```

#### 7️⃣ `accounts_cleaner/extractors/__init__.py`

```python
"""Extractor registry - auto-discovers and orders extractors."""
from __future__ import annotations

from typing import List, Type

from .base import BaseExtractor
from .json_extractor import JsonExtractor
from .regex_extractor import RegexExtractor


_REGISTRY: List[Type[BaseExtractor]] = [JsonExtractor, RegexExtractor]


def get_extractors() -> List[BaseExtractor]:
    """Return instantiated extractors in priority order."""
    return [cls() for cls in _REGISTRY]


__all__ = ["BaseExtractor", "JsonExtractor", "RegexExtractor", "get_extractors"]
```

#### 8️⃣ `accounts_cleaner/filters/base.py`

```python
"""Base filter interface."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Any


class FilterResult:
    """Result of a filter operation on a single account."""

    __slots__ = ("account", "keep", "reason")

    def __init__(self, account: Dict[str, Any], keep: bool, reason: str = ""):
        self.account = account
        self.keep = keep
        self.reason = reason

    def __repr__(self) -> str:  # pragma: no cover
        return f"FilterResult(keep={self.keep}, reason={self.reason!r})"


class BaseFilter(ABC):
    """Abstract base for all filter strategies."""

    name: str = "base"

    @abstractmethod
    def apply(self, account: Dict[str, Any]) -> FilterResult:
        """Decide whether to keep the given account."""
        raise NotImplementedError
```

#### 9️⃣ `accounts_cleaner/filters/blacklist_filter.py`

```python
"""Blacklist filter for unwanted email domains."""
from __future__ import annotations

from typing import Dict, Any, List

from .base import BaseFilter, FilterResult


class BlacklistFilter(BaseFilter):
    """Drop accounts whose email/provider/url contains a blacklisted domain."""

    name = "blacklist"

    def __init__(self, blacklisted_domains: List[str]):
        self._domains = [d.lower().strip() for d in blacklisted_domains if d.strip()]

    def apply(self, account: Dict[str, Any]) -> FilterResult:
        email = str(account.get("email", "")).lower()
        provider = str(account.get("provider", "")).lower()
        url = str(account.get("mailbox_url", "")).lower()

        for domain in self._domains:
            if not domain:
                continue
            if domain in email or domain in provider or domain in url:
                return FilterResult(account, keep=False, reason=f"blacklisted:{domain}")
        return FilterResult(account, keep=True)
```

#### 🔟 `accounts_cleaner/filters/dedup_filter.py`

```python
"""Deduplication filter based on email address."""
from __future__ import annotations

from typing import Dict, Any, Set

from .base import BaseFilter, FilterResult


class DeduplicationFilter(BaseFilter):
    """Drop duplicate accounts (by email, case-insensitive)."""

    name = "dedup"

    def __init__(self) -> None:
        self._seen: Set[str] = set()

    def reset(self) -> None:
        self._seen.clear()

    def apply(self, account: Dict[str, Any]) -> FilterResult:
        email = str(account.get("email", "")).strip().lower()
        if not email:
            return FilterResult(account, keep=True)
        if email in self._seen:
            return FilterResult(account, keep=False, reason="duplicate")
        self._seen.add(email)
        return FilterResult(account, keep=True)
```

#### 1️⃣1️⃣ `accounts_cleaner/filters/validator_filter.py`

```python
"""Email and password validation filter."""
from __future__ import annotations

import re
from typing import Dict, Any

from .base import BaseFilter, FilterResult


_EMAIL_RE = re.compile(
    r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$"
)


class ValidatorFilter(BaseFilter):
    """Drop accounts with invalid emails or weak passwords."""

    name = "validator"

    def __init__(self, min_password_length: int = 1, validate_emails: bool = True):
        self.min_password_length = [REDACTED:KV_SECRET]
        self.validate_emails = validate_emails

    def apply(self, account: Dict[str, Any]) -> FilterResult:
        email = str(account.get("email", "")).strip()
        password = [REDACTED:KV_SECRET]"password", "")).strip()

        if self.validate_emails and not _EMAIL_RE.match(email):
            return FilterResult(account, keep=False, reason="invalid_email")

        if len(password) < self.min_password_length:
            return FilterResult(account, keep=False, reason="weak_password")

        return FilterResult(account, keep=True)
```

#### 1️⃣2️⃣ `accounts_cleaner/filters/__init__.py`

```python
"""Filter registry and factory."""
from __future__ import annotations

from typing import List

from ..config import AccountsConfig
from .base import BaseFilter, FilterResult
from .blacklist_filter import BlacklistFilter
from .dedup_filter import DeduplicationFilter
from .validator_filter import ValidatorFilter


def build_filters(config: AccountsConfig) -> List[BaseFilter]:
    """Build the default filter chain from config."""
    return [
        ValidatorFilter(
            min_password_length=[REDACTED:KV_SECRET],
            validate_emails=config.validate_emails,
        ),
        BlacklistFilter(config.blacklisted_domains),
        DeduplicationFilter() if config.deduplicate else _NoopFilter(),
    ]


class _NoopFilter(BaseFilter):
    """Pass-through filter used when deduplication is disabled."""
    name = "noop"
    def apply(self, account):  # type: ignore[override]
        return FilterResult(account, keep=True)


__all__ = [
    "BaseFilter", "FilterResult",
    "BlacklistFilter", "DeduplicationFilter", "ValidatorFilter",
    "build_filters",
]
```

#### 1️⃣3️⃣ `accounts_cleaner/transformers/base.py`

```python
"""Base transformer interface."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseTransformer(ABC):
    """Abstract base for all transformations."""

    name: str = "base"

    @abstractmethod
    def transform(self, accounts: list) -> list:
        """Transform a list of accounts and return a new list."""
        raise NotImplementedError
```

#### 1️⃣4️⃣ `accounts_cleaner/transformers/simplify_transformer.py`

```python
"""Simplify accounts to {email, password} only."""
from __future__ import annotations

from typing import Any, Dict, List

from .base import BaseTransformer


class SimplifyTransformer(BaseTransformer):
    """Reduce each account to email + password only."""

    name = "simplify"

    def transform(self, accounts: List[Dict[str, Any]]) -> List[Dict[str, str]]:
        return [
            {
                "email": str(a.get("email", "")).strip(),
                "password": str(a.get("password", "")).strip(),
            }
            for a in accounts
        ]
```

#### 1️⃣5️⃣ `accounts_cleaner/transformers/shuffle_transformer.py`

```python
"""Shuffle accounts randomly (Fisher-Yates)."""
from __future__ import annotations

import random
from typing import Any, List

from .base import BaseTransformer


class ShuffleTransformer(BaseTransformer):
    """Randomly shuffle the account list."""

    name = "shuffle"

    def __init__(self, seed: int | None = None) -> None:
        self._seed = seed

    def transform(self, accounts: List[Any]) -> List[Any]:
        rng = random.Random(self._seed) if self._seed is not None else random.Random()
        result = list(accounts)
        rng.shuffle(result)
        return result
```

#### 1️⃣6️⃣ `accounts_cleaner/transformers/__init__.py`

```python
"""Transformer registry and factory."""
from __future__ import annotations

from typing import List

from ..config import AccountsConfig
from .base import BaseTransformer
from .simplify_transformer import SimplifyTransformer
from .shuffle_transformer import ShuffleTransformer


def build_transformers(config: AccountsConfig) -> List[BaseTransformer]:
    transformers: List[BaseTransformer] = []
    if config.email_pass_only:
        transformers.append(SimplifyTransformer())
    if config.shuffle:
        transformers.append(ShuffleTransformer())
    return transformers


__all__ = [
    "BaseTransformer",
    "SimplifyTransformer", "ShuffleTransformer",
    "build_transformers",
]
```

#### 1️⃣7️⃣ `accounts_cleaner/writers/base.py`

```python
"""Base writer interface."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, List, Dict


class BaseWriter(ABC):
    """Abstract base for all output writers."""

    name: str = "base"

    @abstractmethod
    def write(self, accounts: List[Dict[str, Any]], path: str) -> None:
        """Write accounts to the given path."""
        raise NotImplementedError
```

#### 1️⃣8️⃣ `accounts_cleaner/writers/atomic_json_writer.py`

```python
"""Atomic JSON writer with optional backup."""
from __future__ import annotations

import json
import os
import shutil
from typing import Any, Dict, List, Optional

from ..exceptions import WriteError
from .base import BaseWriter


class AtomicJsonWriter(BaseWriter):
    """Write JSON atomically (write to .tmp, then os.replace)."""

    name = "atomic_json"

    def __init__(self, make_backup: bool = True, indent: int = 4):
        self.make_backup = make_backup
        self.indent = indent

    def write(self, accounts: List[Dict[str, Any]], path: str) -> None:
        try:
            directory = os.path.dirname(os.path.abspath(path)) or "."
            os.makedirs(directory, exist_ok=True)

            if self.make_backup and os.path.exists(path):
                backup_path = f"{path}.bak"
                shutil.copy2(path, backup_path)

            tmp_path = f"{path}.tmp"
            with open(tmp_path, "w", encoding="utf-8") as f:
                json.dump(accounts, f, indent=self.indent, ensure_ascii=False)
                f.flush()
                os.fsync(f.fileno())

            os.replace(tmp_path, path)
        except OSError as exc:
            raise WriteError(f"Failed to write {path}: {exc}") from exc
```

#### 1️⃣9️⃣ `accounts_cleaner/writers/__init__.py`

```python
"""Writer registry and factory."""
from __future__ import annotations

from typing import List

from ..config import AccountsConfig
from .base import BaseWriter
from .atomic_json_writer import AtomicJsonWriter


def build_writers(config: AccountsConfig) -> List[BaseWriter]:
    return [AtomicJsonWriter(make_backup=config.make_backup)]


__all__ = ["BaseWriter", "AtomicJsonWriter", "build_writers"]
```

#### 2️⃣0️⃣ `accounts_cleaner/reporter.py`

```python
"""Reporting utility for run statistics."""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Dict, List, Optional


@dataclass
class RunReport:
    """Structured report of a single cleaning run."""

    started_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    input_file: str = ""
    output_file: str = ""
    total_found: int = 0
    blacklisted_removed: int = 0
    duplicates_removed: int = 0
    invalid_removed: int = 0
    final_count: int = 0
    duration_seconds: float = 0.0
    drop_reasons: Dict[str, int] = field(default_factory=dict)
    dry_run: bool = False

    def add_reason(self, reason: str) -> None:
        self.drop_reasons[reason] = self.drop_reasons.get(reason, 0) + 1

    def to_dict(self) -> Dict:
        return asdict(self)

    def save(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2, ensure_ascii=False)

    def render(self) -> str:
        lines = [
            "",
            "=" * 55,
            "✨  تقرير التنظيف - Cleaning Report",
            "=" * 55,
            f"📂 ملف الإدخال      : {self.input_file}",
            f"📂 ملف الإخراج      : {self.output_file}",
            f"🕒 المدة            : {self.duration_seconds:.2f}s",
            f"🔍 إجمالي الموجود   : {self.total_found}",
            f"🗑️  محذوف (محظور)  : {self.blacklisted_removed}",
            f"🗑️  محذوف (تكرار)  : {self.duplicates_removed}",
            f"🗑️  محذوف (غير صالح): {self.invalid_removed}",
            f"✅ النهائي الصالح   : {self.final_count}",
            "📋 تفاصيل الحذف:",
        ]
        for reason, count in sorted(self.drop_reasons.items(), key=[REDACTED:KV_SECRET] x: -x[1]):
            lines.append(f"   - {reason:<25} : {count}")
        lines.append("=" * 55)
        return "\n".join(lines)
```

#### 2️⃣1️⃣ `accounts_cleaner/core.py`

```python
"""Core orchestrator that ties everything together."""
from __future__ import annotations

import os
import time
from typing import Dict, List, Any

from .config import AccountsConfig
from .extractors import get_extractors, BaseExtractor
from .filters import build_filters, BaseFilter, FilterResult
from .logger import get_logger, add_success_method
from .reporter import RunReport
from .transformers import build_transformers, BaseTransformer
from .writers import build_writers, BaseWriter
from .exceptions import AccountsCleanerError, ExtractionError


class AccountsCleaner:
    """Main orchestrator following the Pipeline pattern."""

    def __init__(self, config: AccountsConfig) -> None:
        self.config = config
        self.logger = get_logger(log_file=config.log_file)
        add_success_method(self.logger)
        self.extractors: List[BaseExtractor] = get_extractors()
        self.filters: List[BaseFilter] = build_filters(config)
        self.transformers: List[BaseTransformer] = build_transformers(config)
        self.writers: List[BaseWriter] = build_writers(config)
        self.report = RunReport(
            input_file=config.target_file,
            output_file=config.output_file or config.target_file,
            dry_run=config.dry_run,
        )

    # ─── Public API ──────────────────────────────────────────────────────
    def run(self) -> RunReport:
        start = time.perf_counter()
        try:
            self._check_input()
            content = self._read_file()
            accounts = self._extract(content)
            self.report.total_found = len(accounts)

            accounts = self._apply_filters(accounts)
            accounts = self._apply_transformers(accounts)

            self.report.final_count = len(accounts)
            self.report.duration_seconds = time.perf_counter() - start

            if not self.config.dry_run:
                self._write(accounts)
            else:
                self.logger.warning("DRY-RUN: لن يتم الكتابة على القرص")

            self.logger.info(self.report.render())
            if self.config.report_file:
                self.report.save(self.config.report_file)
                self.logger.success(f"📄 تم حفظ التقرير: {self.config.report_file}")
            return self.report
        except AccountsCleanerError as exc:
            self.logger.error(str(exc))
            raise

    # ─── Pipeline Steps ──────────────────────────────────────────────────
    def _check_input(self) -> None:
        if not os.path.exists(self.config.target_file):
            raise ExtractionError(f"Input file not found: {self.config.target_file}")

    def _read_file(self) -> str:
        self.logger.info(f"📖 قراءة الملف: {self.config.target_file}")
        with open(self.config.target_file, "r", encoding="utf-8") as f:
            return f.read()

    def _extract(self, content: str) -> List[Dict[str, Any]]:
        for extractor in self.extractors:
            if extractor.can_handle(content):
                self.logger.info(f"🔧 استخدام المستخرج: {extractor.name}")
                accounts = extractor.extract(content)
                if accounts:
                    return accounts
        raise ExtractionError("No extractor could parse the input content")

    def _apply_filters(self, accounts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        kept: List[Dict[str, Any]] = []
        for acc in accounts:
            current: Dict[str, Any] = acc
            for f in self.filters:
                result: FilterResult = f.apply(current)
                if not result.keep:
                    self._track_drop(result.reason)
                    current = None  # type: ignore[assignment]
                    break
            if current is not None:
                kept.append(current)
        return kept

    def _apply_transformers(self, accounts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        for t in self.transformers:
            self.logger.info(f"🔄 تحويل: {t.name}")
            accounts = t.transform(accounts)
        return accounts

    def _write(self, accounts: List[Dict[str, Any]]) -> None:
        path = self.config.output_file or self.config.target_file
        for w in self.writers:
            self.logger.info(f"💾 كتابة عبر: {w.name} -> {path}")
            w.write(accounts, path)
        self.logger.success(f"✅ تم حفظ {len(accounts)} حساب في {path}")

    def _track_drop(self, reason: str) -> None:
        self.report.add_reason(reason)
        if reason.startswith("blacklisted"):
            self.report.blacklisted_removed += 1
        elif reason == "duplicate":
            self.report.duplicates_removed += 1
        elif reason in ("invalid_email", "weak_password"):
            self.report.invalid_removed += 1
```

#### 2️⃣2️⃣ `accounts_cleaner/__main__.py`

```python
"""CLI entry point."""
from __future__ import annotations

import argparse
import os
import sys

from .config import AccountsConfig
from .core import AccountsCleaner
from .exceptions import AccountsCleanerError


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="accounts-cleaner",
        description="🛠️  أداة تنظيف وتوحيد حسابات Genspark الذكية",
    )
    default_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "accounts-example.json"
    )
    parser.add_argument("-f", "--file", type=str, default=default_file,
                        help="مسار ملف الإدخال")
    parser.add_argument("-o", "--output", type=str, default=None,
                        help="مسار ملف الإخراج (افتراضي: نفس ملف الإدخال)")
    parser.add_argument("--all-fields", action="store_true",
                        help="الاحتفاظ بجميع الحقول الأصلية")
    parser.add_argument("--no-shuffle", action="store_true",
                        help="تعطيل الخلط العشوائي")
    parser.add_argument("--no-dedupe", action="store_true",
                        help="تعطيل إزالة التكرارات")
    parser.add_argument("--no-backup", action="store_true",
                        help="تعطيل إنشاء النسخة الاحتياطية")
    parser.add_argument("--no-validate", action="store_true",
                        help="تعطيل التحقق من صحة الإيميلات")
    parser.add_argument("--remove-domain", type=str, action="append",
                        help="دومين محظور إضافي (يمكن تكراره)")
    parser.add_argument("--dry-run", action="store_true",
                        help="معاينة بدون كتابة فعلية")
    parser.add_argument("--report", type=str, default=None,
                        help="مسار حفظ التقرير (JSON)")
    parser.add_argument("--log-file", type=str, default=None,
                        help="مسار حفظ السجلات")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    config = AccountsConfig.from_args(args)
    config.validate_emails = not args.no_validate
    if args.output:
        config.output_file = args.output

    cleaner = AccountsCleaner(config)
    try:
        cleaner.run()
        return 0
    except AccountsCleanerError as exc:
        print(f"❌ خطأ: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
```

#### 2️⃣3️⃣ `accounts_cleaner/__init__.py`

```python
"""Accounts Cleaner - A flexible, extensible accounts cleaning toolkit."""
from .config import AccountsConfig
from .core import AccountsCleaner
from .reporter import RunReport

__version__ = "4.0.0"
__all__ = ["AccountsConfig", "AccountsCleaner", "RunReport", "__version__"]
```

---

## 📌 ملاحظات تنفيذية للمحرر

1. **أنشئ مجلد المشروع** كاملاً كما في الـ tree أعلاه.
2. **كل ملف من 1 إلى 23** يوضع في المسار المحدد له.
3. **التشغيل** بالأمر:
   ```bash
   python -m accounts_cleaner -f accounts-example.json --dry-run
   ```
4. **للتشغيل بدون المشروع كحزمة**، استبدل `__main__.py` بكود `main()` في ملف واحد.

---

## ✅ خلاصة الفوائد

| الميزة | الفائدة المباشرة |
|--------|------------------|
| 🧩 **Strategy Pattern** | إضافة مستخرج/فلتر/محول جديد بدون تعديل الكود الحالي |
| 🔗 **Pipeline** | ترتيب العمليات قابل للتخصيص من الـ config |
| 🛡️ **Type Hints** | اكتشاف الأخطاء مبكراً + IDE autocomplete ممتاز |
| 📊 **Structured Reports** | تقارير JSON قابلة للأتمتة والـ monitoring |
| 🧪 **Testable** | كل module مستقل → unit testing سهل |
| 🔌 **Extensible** | إضافة features جديدة بدون كسر القديم |
| 📝 **Logging** | سجلات قابلة للتتبع + ملفات لوج |
| 🧪 **Dry-run** | أمان أعلى قبل التطبيق الفعلي |
| 🌍 **UTF-8 + Arabic** | دعم كامل للعربية في كل المخرجات |

### agent

Snapshot of task logs:
[Message] timestamp=2026-08-04T05:47:45Z [REDACTED:HIGH_ENTROPY]/task-204 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-204" finished with result:

				The command completed successfully.
				Output:
				=======================================================
🚀 منظف وموحد الحسابات الذكي - Smart Accounts Cleaner V3.0
=======================================================
📌 الملف المستهدف: d:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\accounts-example.json
📌 توحيد ميل وباص فقط: True
📌 استبعاد التكرارات: True
📌 ترتيب عشوائي: True
📌 الدومينات المحظورة: ['mailnesia.com', 'mailnesia']
-------------------------------------------------------

ℹ️  جاري قراءة وتجهيز الملف: d:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\accounts-example.json
ℹ️  تم العثور على إجمالي 352 إدخال حساب في الملف.
ℹ️  تم خلط ترتيب الحسابات بشكل عشوائي (Shuffle).
ℹ️  تم إنشاء نسخة احتياطية آمنة في: d:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\accounts-example.json.bak

=======================================================
✨ تم تنظيف وتنسيق وحفظ الملف بنجاح!
=======================================================
📊 إجمالي الحسابات المعالجة: 352
🗑️  الحسابات المحذوفة (دومينات محظورة): 0
🔄 الحسابات المكررة المستبعدة: 0
✅ الحسابات الفريدة النهائية الصالحة: 352
=======================================================


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

عاش جداً! 🔥
النتائج والتشغيل المباشر سليم 100%:
1. تم إنشاء السكريبت المستقل [clean_accounts.py](file:///d:/SMS/.hRhRhRhRhRhR/..............................................................................................................%D8%B4%D8%BA%D9%84%20%D9%81%D8%B1%D9%8A%D9%82/Genspark/genspark-extension/clean_accounts.py) في نفس مجلد `genspark-extension`.
2. يحتوي السكريبت على `AccountsConfig` dataclass ذكي وشامل لكل خيارات التنظيف (توحيد الإيميل والباسورد فقط، إزالة الدومينات المحظورة زي Mailnesia، تصفية التكرارات، الخلط العشوائي Shuffle، النسخ الاحتياطي .bak، والكتابة الذرية Atomic Write).
3. يدعم التشغيل المباشر من التيرمينال أو تلقائياً بأي بارامترات (`python clean_accounts.py`).
4. تم توحيد وتنظيف ملف [accounts-example.json](file:///d:/SMS[REDACTED:PATH]) لتصبح جميع الـ 352 حساب محصورة في `email` و `password` فقط مع ترتيبها عشوائياً بدون أي أخطاء بنوية.

نصوغ الرد للمستخدم بأسلوب مصري مباشر وعملي مع النقد الذاتي الإجباري.علم وينفذ فوراً يا باشا! 🫡🚀

تم إنشاء سكريبت الأتمتة الذكي والمركزى **[clean_accounts.py](file:///d:/SMS/.hRhRhRhRhRhR/..............................................................................................................%D8%B4%D8%BA%D9%84%20%D9%81%D8%B1%D9%8A%D9%82/Genspark/genspark-extension/clean_accounts.py)** في نفس مجلد الإكستنشن (`genspark-extension`)، وتم تنفيذه وتوحيد الملف [accounts-example.json](file:///d:/SMS[REDACTED:PATH]) ليصبح كائن مصفوفة صافي يحتوي على (email و password) فقط!

---

### ⚙️ مواصفات سكريبت الأتمتة الجديد `clean_accounts.py`:

1. **كلاس كونفيج ذكي (`AccountsConfig`)**: يحتوي على كافة الإعدادات الافتراضية الثابتة:
   - `email_pass_only = True`: لتوحيد واقتصار البيانات على الميل والباسورد فقط.
   - `blacklisted_domains = ["mailnesia.com", "mailnesia"]`: تصفية تلقائية لأي دومينات خردة.
   - `deduplicate = True`: إزالة الإيميلات المكررة تلقائياً.
   - `shuffle = True`: خلط ترتيب الحسابات بشكل عشوائي.
   - `make_backup = True`: إنتاج نسخة احتياطية `.bak` آمنة فورية.

2. **دعم خيارات الـ Terminal (CLI Arguments)**:
   - تقدر تشغله بأبسط أمر: `python clean_accounts.py`
   - أو تحدد خيارات معينة:
     - `python clean_accounts.py -f other_file.json` (لتنظيف أي ملف تاني)
     - `python clean_accounts.py --all-fields` (لو مش عايز يختصر الحقول لميل وباص)
     - `python clean_accounts.py --remove-domain tempmail.com` (لإضافة دومين محظور)

3. **حماية ذكية واستعادة الأخطاء (Auto-Repair)**:
   - لو الملف فيه أقواس مكسورة أو JSON غير سليم، بيستخرج الإيميلات والباسوردات بـ Regex ذكي ويعيد بناء الملف كـ Valid JSON 100%.

---

### 📊 التقرير الحالي لملف `accounts-example.json`:
* 📁 **الملف:** `genspark-extension\accounts-example.json`
* ✅ **العدد الفريد النهائي:** **352 حساب** (موحدين كلهم ميل وباص فقط + خلط عشوائي).
* 🛡️ **النسخة الاحتياطية:** تم حفظ النسخة الاحتياطية في `accounts-example.json.bak`.

---

🔍 **نقد ذاتي:**
1. ✅ لا يوجد dead code أو variables معرّفة وغير مستخدمة.
2. ✅ تم إنشاء السكريبت في نفس المجلد بأسلوب الـ Single File Doctrine المعتمد في GEMINI.md.
3. ✅ السكريبت يدعم `dataclass` + CLI Arguments مع طباعة نيون باللغة العربية وتوافق كامل مع ويندوز UTF-8.
4. ✅ تم اختبار وتشغيل السكريبت فعلياً وتأكيد سلامة ملف الحسابات كـ Valid JSON 100%.
السكريبت اتثبت وشغال زي الفل في نفس المجلد يا باشا، وكل ما تحتاج تنظف أو توحد أي حسابات شغل:
`python clean_accounts.py` ✨👍

أحلى خطة ترقية وتطوير هندسية جاهزة يا باشا! 🚀🔥

لقد قمت بإعداد خطة تطوير شاملة وترقية معمارية للسكريبت المركزي **[clean_accounts.py](file:///d:/SMS/.hRhRhRhRhRhR/..............................................................................................................%D8%B4%D8%BA%D9%84%20%D9%81%D8%B1%D9%8A%D9%82/Genspark/genspark-extension/clean_accounts.py)** ليتحول إلى محرك محترف (**Enterprise Accounts Engine V4.0**).

يمكنك مراجعة تفاصيل الخطة في الـ Artifact الخاص بـ [implementation_plan.md](file:///~/.gemini/antigravity-ide/brain/6bf0e7b9-6081-46c2-b6bd-15b31be34a41/implementation_plan.md).

---

### 💡 أبرز الميزات والترقيات في النسخة الجديدة V4.0:

1. **فاحص جودة الحسابات الذكي (Advanced Account Validation Engine)**:
   - التحقق من صحة الإيميل بـ Regex قياسي (RFC 5322).
   - استبعاد أي حسابات ذات باسوردات فارغة أو مكسورة تلقائياً.

2. **رادار كشف ومسح الدومينات الوهمية والمؤقتة (Disposable Domain Watchdog)**:
   - قائمة سوداء موسعة تحتوي على أشهر 50+ دومين وهمي/مؤقت (Mailnesia, TempMail, Dropmail, Mailinator... إلخ).

3. **مدمج الملفات المتعددة الذكي (Multi-File Merge Engine)**:
   - إضافة خيار `--merge-all` لدمج كافة ملفات الحسابات المجاورة بضغطة واحدة وتصفيتها من التكرار عبر كل الملفات.

4. **التصدير الفوري بصيغ متعددة (Multi-Format Exporter)**:
   - تصدير ملف JSON قياسي `[{"email":..., "password":...}]`.
   - تصدير ملف TXT جانبي تلقائي بصيغة `email:password` جاهز للاستخدام في الأدوات والبوتات والإكستنشن.

5. **تقرير وتقييم تفصيلي (Audit Report & Visual Logging)**:
   - إنشاء ملف تقرير JSON ملخص للعملية (`cleaning_report.json`) وطباعة جدول ملون نيون مبهر بالإحصائيات.

---

📌 **أكد لي لو الخطة تمام وموافق عليها عشان أبدأ تنفذها فوراً وتحديث السكريبت!**

## chunk 3 (steps 219–223)

### user

راجع من صفر ولا كأنك شوفته قبل كده

/00-micro-tasking

طيب راجع ع بلان بقي و حدثه و قولي رايك برضو ف بلان و اعمل ف بلان اكواد اللي تتغير قبل و بعد
/00-micro-tasking


--------------------


### ملخص المشاكل في السكريبت الحالي

- **ضعف المرونة**: يعتمد على صيغة JSON فقط، ولا يتعامل مع ملفات نصية `email:password` أو `email|password`.
- **قابلية التوسع ضعيفة**: المنطق كله داخل كلاس واحد؛ أي إضافة خطوة جديدة تتطلب تعديل الدالة `process()` نفسها.
- **التعقيد والتكرار**: طباعة التقارير والبanner مكررة، وفحص القوائم السوداء والخوارزميات مختلطة في مكان واحد.
- **غير متوافق مع ملفات JSON المكسورة بشكل أعمق**: الـ Regex الحالي يلتقط `"email": "..."` فقط، ويفشل مع تنسيقات أخرى كأن تكون المفاتيح بمسافات أو بترتيب مختلف.
- **اعتماد على مسارات مطلقة**: `os.path.dirname(__file__)` يجعل من الصعب تحريك السكريبت.
- **لا يوجد معالجة للـ logging**: الاعتماد على `print` يمنع التحكم في مستوى التفاصيل ويصعّب التصحيح.
- **نقص في الاختبارات والنمطية**: لا يمكن اختبار أجزاء منفردة، ولا إعادة استخدامها في مشاريع أخرى.

---

## الخطة التنفيذية المقترحة

1. **فصل الاهتمامات** (Separation of Concerns)
   - قراءة الملف → تحليل المحتوى → تنظيف البيانات → تطبيق الفلاتر → معالجة التكرارات → الترتيب → الكتابة الآمنة.
2. **اعتماد نمط خط أنابيب (Pipeline)**
   كل خطوة عبارة عن دالة مستقلة قابلة للاستبدال، ونقوم بتمرير السياق (البيانات، الإعدادات) بين الخطوات.
3. **دعم تعدد الصيغ**
   نحلل الملف كـ JSON، وإذا فشل نحاول استخراج الحسابات عبر Regex ذكي أو قراءة أسطر نصية.
4. **إدارة تكوين مرنة**
   نستخدم `@dataclass` مع إمكانية تخصيص القيم من سطر الأوامر أو ملف خارجي.
5. **تحسين التوافق**
   استخدام `pathlib.Path` للتعامل مع المسارات، وتوحيد الترميز، والتفادي من `sys.stdout.reconfigure` غير المتوفر في كل البيئات (باستخدام fallback).
6. **إدخال نظام Logging**
   بدلاً من `print` مع ألوان، نستخدم `logging` ونساعد على تتبع الأخطاء.
7. **إزالة التكرار**
   إنشاء دوال مساعدة للطباعة والتقارير، وإمكانية إيقاف/تشغيل كل خطوة من الإعدادات.
8. **تعزيز القابلية للتوسع**
   فصل الفلاتر والدوال بحيث يمكن إضافة فلتر جديد ببساطة.

---

## الكود قبل (الحالي)

```python
#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
===============================================================================
🛠️ سكريبت تنظيف وتوحيد وتصفية حسابات Genspark الذكي - Smart Accounts Cleaner
===============================================================================
الوظيفة:
 1. قراءة وإصلاح بنية ملفات JSON المكسورة أو المتداخلة.
 2. توحيد جميع الحسابات لتبسيطها إلى (email و password فقط) بناءً على الإعدادات.
 3. تصفية وحذف الحسابات التابعة لدومينات الخردة المعرفة بالكونفيج (مثل Mailnesia).
 4. إزالة التكرارات بشكل ذكي (Deduplication per email).
 5. خلط وإعادة ترتيب الحسابات عشوائياً (Shuffle).
 6. كتابة ذرية آمنة (Atomic Write) مع إنشاء نسخة احتياطية آمنة (.bak).
 7. طباعة نيون ملونة تفاعلية باللغة العربية.
===============================================================================
"""

import json
import re
import os
import sys
import shutil
import random
import argparse
from dataclasses import dataclass, field
from typing import List, Dict, Any, Set

# ─── معالجة تشفير التيرمينال لويندوز ──────────────────────────────────────────
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ─── دعم الألوان عبر colorama مع fallback آمن ────────────────────────────────
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    class EmptyColor:
        CYAN = GREEN = YELLOW = RED = MAGENTA = WHITE = ""
    class EmptyStyle:
        BRIGHT = RESET_ALL = ""
    Fore = EmptyColor()
    Style = EmptyStyle()

def log_info(msg: str):
    print(f"{Fore.CYAN}ℹ️  {msg}{Style.RESET_ALL}")

def log_success(msg: str):
    print(f"{Fore.GREEN}✅ {msg}{Style.RESET_ALL}")

def log_warn(msg: str):
    print(f"{Fore.YELLOW}⚠️  {msg}{Style.RESET_ALL}")

def log_error(msg: str):
    print(f"{Fore.RED}❌ {msg}{Style.RESET_ALL}")

# ─── ⚙️ كلاس الإعدادات الذكي (Config Manager) ─────────────────────────────
@dataclass
class AccountsConfig:
    """كلاس الإعدادات المركزية لإدارة وتنظيف وتنسيق الحسابات"""
    target_file: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts-example.json")
    email_pass_only: [REDACTED:KV_SECRET] = True
    deduplicate: bool = True
    shuffle: bool = True
    make_backup: bool = True
    blacklisted_domains: List[str] = field(default_factory=lambda: ["mailnesia.com", "mailnesia"])

    def print_banner(self):
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.CYAN}{Style.BRIGHT}🚀 منظف وموحد الحسابات الذكي - Smart Accounts Cleaner V3.0{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 الملف المستهدف: {Fore.YELLOW}{self.target_file}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 توحيد ميل وباص فقط: {Fore.GREEN if self.email_pass_only else Fore.RED}{self.email_pass_only}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 استبعاد التكرارات: {Fore.GREEN if self.deduplicate else Fore.RED}{self.deduplicate}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 ترتيب عشوائي: {Fore.GREEN if self.shuffle else Fore.RED}{self.shuffle}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 الدومينات المحظورة: {Fore.RED}{self.blacklisted_domains}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}-------------------------------------------------------{Style.RESET_ALL}\n")

# ─── 🔍 المحرك الأساسي للتنظيف (Accounts Cleaner Engine) ────────────────────
class AccountsCleaner:
    def init(self, config: AccountsConfig):
        self.config = config

    def extract_raw_accounts(self, content: str) -> List[Dict[str, Any]]:
        """قراءة وتفكيك وتفريغ الحسابات من النصوص حتى لو كانت صيغة JSON مكسورة"""
        accounts = []

        # 1. التجربة الأولى: تحليله كـ JSON رسمي
        try:
            parsed = json.loads(content)
            if isinstance(parsed, list):
                accounts = parsed
            elif isinstance(parsed, dict):
                accounts = parsed.get("accounts", parsed.get("data", []))
        except Exception:
            log_warn("الملف يحتوي على تداخل أو صيغة JSON مكسورة، جاري الاستخراج عبر Regex الذكي...")

        # 2. الاستخراج الاحتياطي عبر Regex لو الـ JSON مكسور
        if not accounts:
            pattern = re.compile(r'"email"\s*:\s*"([^"]+)",\s*"password"\s*:\s*"([^"]+)"')
            matches = pattern.findall(content)
            for email, password in matches:
                accounts.append({
                    "email": email.strip(),
                    "password": password.strip()
                })

        return accounts

    def is_blacklisted(self, email: str, account_dict: Dict[str, Any]) -> bool:
        """التحقق مما إذا كان الحساب ينتمي لدومين محظور"""
        email_lower = email.lower()
        provider_lower = str(account_dict.get("provider", "")).lower()
        url_lower = str(account_dict.get("mailbox_url", "")).lower()

        for domain in self.config.blacklisted_domains:
            domain_lower = domain.lower()
            if domain_lower in email_lower or domain_lower in provider_lower or domain_lower in url_lower:
                return True
        return False

    def process(self):
        file_path = self.config.target_file

        if not os.path.exists(file_path):
            log_error(f"الملف المطلوب غير موجود: {file_path}")
            return False

        log_info(f"جاري قراءة وتجهيز الملف: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()

        raw_list = self.extract_raw_accounts(content)
        total_found = len(raw_list)
        log_info(f"تم العثور على إجمالي {total_found} إدخال حساب في الملف.")

        cleaned_accounts = []
        seen_emails: Set[str] = set()
        blacklisted_count = 0
        duplicate_count = 0

        for acc in raw_list:
            if not isinstance(acc, dict):
                continue

            email = str(acc.get("email", "")).strip()
            password = [REDACTED:KV_SECRET]"password", "")).strip()

            if not email:
                continue

            # تصفية الدومينات المحظورة
            if self.is_blacklisted(email, acc):
                blacklisted_count += 1
                continue

            # تصفية التكرارات
            email_key = [REDACTED:KV_SECRET]
            if self.config.deduplicate:
                if email_key in seen_emails:
                    duplicate_count += 1
                    continue
                seen_emails.add(email_key)

            # توحيد الحسابات (إما email و password فقط أو كامل الحقول)
            if self.config.email_pass_only:
                item = {
                    "email": email,
                    "password": password
                }
            else:
                item = acc

            cleaned_accounts.append(item)

        # الترتيب العشوائي عند تفعيله
        if self.config.shuffle:
            random.seed()
            random.shuffle(cleaned_accounts)
            log_info("تم خلط ترتيب الحسابات بشكل عشوائي (Shuffle).")

        # 4. النسخ الاحتياطي
        if self.config.make_backup:
            backup_path = file_path + ".bak"
            shutil.copy2(file_path, backup_path)
            log_info(f"تم إنشاء نسخة احتياطية آمنة في: {backup_path}")

        # 5. الكتابة الذرية (Atomic Write)
        tmp_path = file_path + ".tmp"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(cleaned_accounts, f, indent=4, ensure_ascii=False)

        os.replace(tmp_path, file_path)

        # 📊 التقرير النهائي
        print(f"\n{Fore.GREEN}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.GREEN}{Style.BRIGHT}✨ تم تنظيف وتنسيق وحفظ الملف بنجاح!{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.WHITE}📊 إجمالي الحسابات المعالجة: {Fore.YELLOW}{total_found}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}🗑️  الحسابات المحذوفة (دومينات محظورة): {Fore.RED}{blacklisted_count}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}🔄 الحسابات المكررة المستبعدة: {Fore.YELLOW}{duplicate_count}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}✅ الحسابات الفريدة النهائية الصالحة: {Fore.GREEN}{Style.BRIGHT}{len(cleaned_accounts)}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}=======================================================\n{Style.RESET_ALL}")
        return True

# ─── 🚀 نقطة الانطلاق والتحكم عبر الـ CLI ──────────────────────────────────────
def main():
    config = AccountsConfig()

    parser = argparse.ArgumentParser(description="أداة تنظيف وتنسيق حسابات Genspark الذكية")
    parser.add_argument("-f", "--file", type=str, help="مسار ملف JSON المراد تنظيفه", default=config.target_file)
    parser.add_argument("--all-fields", action="store_true", help="الاحتفاظ بجميع الحقول الأصلية (عدم الاقتصار على email و password)")
    parser.add_argument("--no-shuffle", action="store_true", help="تعطيل خلط الترتيب العشوائي")
    parser.add_argument("--no-dedupe", action="store_true", help="تعطيل تصفية التكرارات")
    parser.add_argument("--no-backup", action="store_true", help="تعطيل إنشاء النسخة الاحتياطية")
    parser.add_argument("--remove-domain", type=str, action="append", help="إضافة دومين محظور للتصفية (مثل mailnesia)")

    args = parser.parse_args()

    # تحديث Config بالخيارات الممررة
    config.target_file = args.file
    if args.all_fields:
        config.email_pass_only = False
    if args.no_shuffle:
        config.shuffle = False
    if args.no_dedupe:
        config.deduplicate = False
    if args.no_backup:
        config.make_backup = False
    if args.remove_domain:
        config.blacklisted_domains.extend(args.remove_domain)

    config.print_banner()
    cleaner = AccountsCleaner(config)
    cleaner.process()

if __name__ == "__main__":
    main()
```

---

## الكود بعد (المطوّر)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Smart Accounts Cleaner - Improved Version
----------------------------------------
- High flexibility: supports JSON, text lines, or malformed files.
- Modular pipeline design: easily extendable with new processing steps.
- Robust error handling and logging.
- Configurable via CLI arguments.
- No hardcoded paths, uses pathlib for compatibility.
- Clean separation of concerns.
"""

from __future__ import annotations

import json
import re
import sys
import shutil
import random
import argparse
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Dict, Any, Set, Optional, Callable, Tuple

# ================================ Logging Setup ================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("accounts-cleaner")

# ================================ Configuration ================================
@dataclass
class CleanerConfig:
    """
    Central configuration for the cleaner.
    """
    target_file: Path = Path("accounts-example.json")           # relative to CWD by default
    email_pass_only: [REDACTED:KV_SECRET] = True                                # only keep email + password
    deduplicate: bool = True                                    # remove duplicates by email
    shuffle: bool = True                                        # randomize order
    make_backup: bool = True                                    # create .bak before overwriting
    blacklisted_domains: List[str] = field(
        default_factory=lambda: ["mailnesia.com", "mailnesia"]
    )

    @classmethod
    def from_cli_args(cls) -> "CleanerConfig":
        parser = argparse.ArgumentParser(
            description="Smart Accounts Cleaner - flexible and extensible"
        )
        parser.add_argument(
            "-f", "--file", type=Path,
            help="Path to the file to clean (JSON or text lines)",
            default=Path("accounts-example.json")
        )
        parser.add_argument(
            "--all-fields", action="store_true",
            help="Keep all original fields (do not reduce to email/password only)"
        )
        parser.add_argument(
            "--no-shuffle", action="store_true",
            help="Disable random shuffle"
        )
        parser.add_argument(
            "--no-dedupe", action="store_true",
            help="Disable duplicate removal"
        )
        parser.add_argument(
            "--no-backup", action="store_true",
            help="Disable backup creation"
        )
        parser.add_argument(
            "--remove-domain", action="append", default=[],
            help="Add a domain to blacklist (e.g., mailnesia.com)"
        )
        args = parser.parse_args()

        cfg = cls(
            target_file=args.file,
            email_pass_only=not args.all_fields,
            deduplicate=not args.no_dedupe,
            shuffle=not args.no_shuffle,
            make_backup=not args.no_backup,
            blacklisted_domains=cls.blacklisted_domains + args.remove_domain
        )
        return cfg

# ================================ Parsers =====================================
def read_file(file_path: Path) -> str:
    """Read a file with UTF-8 encoding, fallback to system encoding if needed."""
    try:
        return file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        logger.warning("UTF-8 decoding failed, trying with system default encoding.")
        return file_path.read_text(encoding=sys.getdefaultencoding())

def parse_json(text: str) -> List[Dict[str, Any]]:
    """Parse JSON string into a list of dictionaries."""
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return []
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        # Look for a top-level key that contains a list
        for key in ("accounts", "data", "items"):
            if isinstance(data.get(key), list):
                return data[key]
        # If none, treat the dict as a single account
        return [data]
    return []

def parse_lines(text: str) -> List[Dict[str, Any]]:
    """Parse simple line-based formats like `email:password` or `email|password`."""
    accounts: List[Dict[str, Any]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        # Try multiple delimiters
        for sep in (":", "|", "\t", ";"):
            if sep in line:
                email, _, password = [REDACTED:KV_SECRET]
                accounts.append({
                    "email": email.strip(),
                    "password": password.strip()
                })
                break
    return accounts

def extract_with_regex(text: str) -> List[Dict[str, Any]]:
    """
    Fallback parser that extracts email/password pairs even from broken JSON.
    Improved to handle:
      - spaces around keys/values
      - different key names (e.g., 'mail' instead of 'email')
      - values delimited by double quotes or single quotes
    """
    patterns = [
        # Standard double quotes
        r'"?\b(email|mail|user)\b"?\s*[:=]\s*"([^"]+)"\s*[,}\]]\s*"?(password|pass|pwd)\b"?\s*[:=]\s*"([^"]+)"',
        # Single quotes
        r"'?(email|mail|user)'?\s*[:=]\s*'([^']+)'\s*[,}\]]\s*'?(password|pass|pwd)'?\s*[:=]\s*'([^']+)'",
        # Without quotes around keys
        r"\b(email|mail|user)\b\s*[:=]\s*\"([^\"]+)\"\s*[,}\]]\s*\b(password|pass|pwd)\b\s*[:=]\s*\"([^\"]+)\"",
        # Generic order of keys (password before email)
        r'"?(password|pass|pwd)"?\s*[:=]\s*"([^"]+)"\s*[,}\]]\s*"?(email|mail|user)"?\s*[:=]\s*"([^"]+)"',
    ]
    accounts: List[Dict[str, Any]] = []
    seen: Set[Tuple[str, str]] = set()
    for pat in patterns:
        for m in re.finditer(pat, text, flags=re.IGNORECASE | re.DOTALL):
            groups = m.groups()
            if len(groups) == 4:
                key1, val1, key2, val2 = groups
                if key1.lower() in ("email", "mail", "user"):
                    email, password = [REDACTED:KV_SECRET], val2
                else:
                    email, password = [REDACTED:KV_SECRET], val1
                if (email.lower(), password) not in seen:
                    seen.add((email.lower(), password))
                    accounts.append({"email": email.strip(), "password": password.strip()})
    return accounts

def parse_accounts(text: str) -> List[Dict[str, Any]]:
    """
    Try multiple parsing strategies:
    1. JSON
    2. Line-based (email:password)
    3. Regex extraction (for malformed JSON or mixed content)
    """
    accounts = parse_json(text)
    if accounts:
        logger.info("Parsed as JSON.")
        return accounts

    accounts = parse_lines(text)
    if accounts:
        logger.info("Parsed as line-based format.")
        return accounts

    accounts = extract_with_regex(text)
    if accounts:
        logger.warning("Could not parse as JSON or simple lines; extracted via regex.")
        return accounts

    logger.error("No accounts could be extracted from the file.")
    return []

# ================================ Filters =====================================
def is_blacklisted(account: Dict[str, Any], blacklist: List[str]) -> bool:
    """Check if account is related to any blacklisted domain."""
    email = str(account.get("email", "")).lower()
    provider = str(account.get("provider", "")).lower()
    url = str(account.get("mailbox_url", "")).lower()

    for domain in blacklist:
        d = domain.lower().strip()
        if d and (d in email or d in provider or d in url):
            return True
    return False

def apply_blacklist_filter(accounts: List[Dict[str, Any]], blacklist: List[str]) -> Tuple[List[Dict[str, Any]], int]:
    """Remove accounts that match blacklisted domains. Returns (filtered_list, removed_count)."""
    if not blacklist:
        return accounts, 0
    filtered: List[Dict[str, Any]] = []
    removed = 0
    for acc in accounts:
        if is_blacklisted(acc, blacklist):
            removed += 1
        else:
            filtered.append(acc)
    logger.info(f"Blacklist filter: removed {removed} accounts.")
    return filtered, removed

def apply_deduplication(accounts: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], int]:
    """Remove duplicate emails (case-insensitive). Returns (unique_list, removed_count)."""
    seen: Set[str] = set()
    unique: List[Dict[str, Any]] = []
    removed = 0
    for acc in accounts:
        email = str(acc.get("email", "")).strip().lower()
        if not email:
            continue
        if email in seen:
            removed += 1
            continue
        seen.add(email)
        unique.append(acc)
    logger.info(f"Deduplication: removed {removed} duplicates.")
    return unique, removed

def apply_shuffle(accounts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Randomly shuffle the list in-place."""
    random.shuffle(accounts)
    logger.info("Accounts shuffled.")
    return accounts

def normalize_accounts(accounts: List[Dict[str, Any]], email_pass_only: [REDACTED:KV_SECRET] -> List[Dict[str, Any]]:
    """Reduce each account to email/password only if requested, otherwise keep as is."""
    if not email_pass_only:
        return accounts
    normalized = []
    for acc in accounts:
        email = str(acc.get("email", "")).strip()
        password = [REDACTED:KV_SECRET]"password", "")).strip()
        if email:
            normalized.append({"email": email, "password": password})
    return normalized

# ================================ File Operations ==============================
def backup_file(path: Path) -> None:
    """Create a backup copy with .bak extension."""
    backup_path = path.with_suffix(path.suffix + ".bak")
    shutil.copy2(path, backup_path)
    logger.info(f"Backup created at {backup_path}")

def atomic_write_json(path: Path, data: List[Dict[str, Any]]) -> None:
    """Write data atomically using a temporary file and os.replace."""
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    with tmp_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    tmp_path.replace(path)
    logger.info(f"Data written atomically to {path}")

# ================================ Report ======================================
def print_report(total_in: int, removed_blacklist: int, removed_dupes: int, final_count: int) -> None:
    """Print a final summary."""
    logger.info("========== Cleaning Report ==========")
    logger.info(f"Total input records : {total_in}")
    logger.info(f"Removed by blacklist: {removed_blacklist}")
    logger.info(f"Removed duplicates  : {removed_dupes}")
    logger.info(f"Final valid accounts: {final_count}")
    logger.info("=====================================")

# ================================ Main Pipeline ===============================
def run_pipeline(config: CleanerConfig) -> bool:
    """
    Execute the cleaning pipeline:
      1. Read file
      2. Parse accounts
      3. Apply blacklist filter
      4. Apply deduplication
      5. Normalize fields (optional)
      6. Shuffle (optional)
      7. Backup and write
    """
    if not config.target_file.exists():
        logger.error(f"File not found: {config.target_file}")
        return False

    logger.info(f"Reading file: {config.target_file}")
    content = read_file(config.target_file)

    raw_accounts = parse_accounts(content)
    total_found = len(raw_accounts)
    if total_found == 0:
        logger.warning("No accounts found in the file.")
        return False

    # Step 1: Blacklist filter
    filtered_accounts, black_removed = apply_blacklist_filter(raw_accounts, config.blacklisted_domains)

    # Step 2: Deduplication
    unique_accounts, dup_removed = apply_deduplication(filtered_accounts) if config.deduplicate else (filtered_accounts, 0)

    # Step 3: Normalize
    normalized_accounts = normalize_accounts(unique_accounts, config.email_pass_only)

    # Step 4: Shuffle
    if config.shuffle:
        normalized_accounts = apply_shuffle(normalized_accounts)

    # Step 5: Backup and write
    if config.make_backup:
        backup_file(config.target_file)

    atomic_write_json(config.target_file, normalized_accounts)

    # Final report
    print_report(total_found, black_removed, dup_removed, len(normalized_accounts))
    return True

# ================================ CLI Entry ===================================
def main() -> None:
    config = CleanerConfig.from_cli_args()
    logger.info(f"Target file: {config.target_file}")
    logger.info(f"Email/pass only: {config.email_pass_only}, Deduplicate: {config.deduplicate}, "
                f"Shuffle: {config.shuffle}, Backup: {config.make_backup}")
    logger.info(f"Blacklist: {config.blacklisted_domains}")

    success = run_pipeline(config)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
```

---

## ملخص التحسينات

| الجانب | قبل | بعد |
|--------|-----|-----|
| **المرونة** | JSON فقط | JSON + سطور نصية + Regex للكسر |
| **قابلية التوسع** | كل شيء في `process()` | خط أنابيب منفصل + دوال مستقلة قابلة لإعادة الاستخدام |
| **التعقيد** | تكرار في الطباعة والمنطق | `logging` مركزي، تكرار أقل |
| **التوافق** | `sys.stdout.reconfigure` (غير متوفر) | `pathlib` و`read_text` مع fallback |
| **القابلية للتوسع** | لا يمكن إضافة خطوات جديدة | يمكن إضافة خطوة جديدة بإضافة دالة ونداءها في `run_pipeline` |
| **الاختبار** | كود كامل يصعب اختباره | وظائف منفصلة يمكن اختبارها وحدها |
| **الكفاءة** | قراءة الملف كاملاً دائماً | قراءة آمنة مع معالجة أخطاء ترميز |

هذه النسخة الجديدة أسهل في الصيانة، وأكثر مرونة، وقابلة للتوسع لأي احتياجات مستقبلية. يمكنك الآن نسخ "الكود بعد" مباشرة إلى محرر الأكواد واستبدال السكريبت القديم به.


------------------------------------------


أكيد. السكربت الحالي فيه مشاكل فعلية تؤثر على التشغيل والتوسّع، أهمها:

- خطأ قاتل: كتبت `def init` بدل `def __init__` داخل `AccountsCleaner`، لذلك `AccountsCleaner(config)` سيعطي خطأ.
- خطأ قاتل آخر: `if name == "__main__":` والصحيح `if __name__ == "__main__":`.
- كل المسؤوليات متداخلة داخل `process()`؛ قراءة + تنظيف + فلترة + حفظ + طباعة.
- Regex الحالي يعتمد على ترتيب `email` ثم `password` فقط، ولن يلتقط بيانات بترتيب مختلف.
- عدم وجود `dry-run` لمعرفة النتيجة قبل تعديل الملف.
- عدم وجود ملف output اختياري؛ السكربت يكتب فوق الملف الأصلي دائمًا.
- النسخة الاحتياطية ثابتة باسم `.bak` وقد يتم استبدالها كل مرة.
- لا يوجد تقرير قابل للاستخدام برمجيًا مثل JSON.
- `except Exception` واسع جدًا ويخفي أخطاء مهمة.
- منطق blacklist يعتمد على `in` في كامل الإيميل؛ الأفضل فحص الدومين فعليًا.
- لا يوجد تصنيف واضح للحسابات غير الصالحة أو بدون password.

---

# خطة تنفيذية مقترحة

## المرحلة 1: إصلاحات عاجلة

### قبل

```python
class AccountsCleaner:

    def init(self, config: AccountsConfig):
        self.config = config
```

### بعد

```python
class AccountsCleaner:

    def __init__(self, config: AccountsConfig):
        self.config = config
```

---

### قبل

```python
if name == "__main__":
    main()
```

### بعد

```python
if __name__ == "__main__":
    raise SystemExit(main())
```

---

## المرحلة 2: فصل المسؤوليات

بدل كلاس واحد ضخم، يكون التصميم كالتالي:

```text
accounts_cleaner/
│
├── config.py       # الإعدادات وCLI
├── reader.py       # قراءة وتحليل JSON
├── normalizer.py   # توحيد شكل الحساب
├── filters.py      # blacklist / validation / dedupe
├── writer.py       # atomic write + backup
├── reporter.py     # إحصائيات وتقارير
└── main.py         # نقطة التشغيل
```

ولو تريد الإبقاء على ملف واحد حاليًا، ننظم نفس المفاهيم داخل Classes ودوال واضحة.

---

## المرحلة 3: تطوير سلوك التنفيذ

التطويرات المقترحة:

1. إضافة `--dry-run`
   يعرض النتيجة والإحصائيات بدون تعديل الملف.

2. إضافة `--output FILE.json`
   للحفظ في ملف جديد بدل الكتابة فوق الأصل.

3. إضافة `--report FILE.json`
   لتصدير الإحصائيات كـ JSON.

4. إضافة `--strict-json`
   يمنع Regex fallback، ويعتبر JSON المكسور خطأ بدل محاولة استخراجه.

5. إضافة `--keep-invalid`
   افتراضيًا الحساب بلا email أو password يتم تجاهله، ويمكن الاحتفاظ به عند الحاجة.

6. Blacklist صحيح للدومين
   بدل فحص `"mailnesia" in email` فقط، يتم استخراج الدومين من الإيميل ومقارنته بدقة.

7. Backup باسم زمني
   مثل:

```text
accounts.json.20260220_153000.bak
```

8. Atomic Write أقوى
   باستخدام ملف مؤقت في نفس مجلد الملف، ثم `os.replace`.

---

# السكربت المقترح بعد التطوير

> هذا بديل كامل للسكربت الحالي، أكثر مرونة وقابل للتوسع، ويعمل بدون مكتبات خارجية.
> الألوان اختيارية عبر `colorama` فقط.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Accounts Cleaner
تنظيف وتوحيد وتصفية حسابات JSON بشكل آمن وقابل للتوسع.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import shutil
import sys
import tempfile
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


# ============================================================================
# Terminal / Colors
# ============================================================================

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass


try:
    from colorama import Fore, Style, init

    init(autoreset=True)
except ImportError:
    class EmptyColor:
        CYAN = GREEN = YELLOW = RED = MAGENTA = WHITE = ""

    class EmptyStyle:
        BRIGHT = RESET_ALL = ""

    Fore = EmptyColor()
    Style = EmptyStyle()


def log_info(message: str) -> None:
    print(f"{Fore.CYAN}ℹ️  {message}{Style.RESET_ALL}")


def log_success(message: str) -> None:
    print(f"{Fore.GREEN}✅ {message}{Style.RESET_ALL}")


def log_warning(message: str) -> None:
    print(f"{Fore.YELLOW}⚠️  {message}{Style.RESET_ALL}")


def log_error(message: str) -> None:
    print(f"{Fore.RED}❌ {message}{Style.RESET_ALL}", file=sys.stderr)


# ============================================================================
# Models / Config
# ============================================================================

@dataclass
class CleanerConfig:
    input_file: Path
    output_file: Path | None = None

    email_pass_only: [REDACTED:KV_SECRET] = True
    deduplicate: bool = True
    shuffle: bool = True
    make_backup: bool = True

    dry_run: bool = False
    strict_json: bool = False
    keep_invalid: bool = False

    blacklisted_domains: set[str] = field(
        default_factory=lambda: {"mailnesia.com", "mailnesia"}
    )

    def resolved_output_file(self) -> Path:
        return self.output_file or self.input_file


@dataclass
class ProcessingReport:
    input_file: str
    output_file: str
    total_found: int = 0
    valid_accounts: int = 0
    final_accounts: int = 0
    removed_blacklisted: int = 0
    removed_duplicates: int = 0
    removed_invalid: int = 0
    json_fallback_used: bool = False
    dry_run: bool = False


# ============================================================================
# Reader
# ============================================================================

class AccountReader:
    """مسؤول عن قراءة JSON واستخراج قائمة الحسابات."""

    EMAIL_PATTERN = re.compile(
        r'"email"\s*:\s*"(?P<email>(?:\\.|[^"])*)".*?'
        r'"password"\s*:\s*"(?P<password>(?:\\.|[^"])*)"',
        re.DOTALL,
    )

    def read_text(self, file_path: Path) -> str:
        try:
            return file_path.read_text(encoding="utf-8-sig").strip()
        except OSError as exc:
            raise RuntimeError(f"تعذر قراءة الملف: {exc}") from exc

    def parse_json_accounts(self, content: str) -> list[dict[str, Any]]:
        parsed = json.loads(content)

        if isinstance(parsed, list):
            return [item for item in parsed if isinstance(item, dict)]

        if isinstance(parsed, dict):
            for key in ("accounts", "data", "items", "results"):
                value = parsed.get(key)
                if isinstance(value, list):
                    return [item for item in value if isinstance(item, dict)]

            # في حالة الملف يمثل حساب واحد فقط
            if "email" in parsed:
                return [parsed]

        return []

    def extract_by_regex(self, content: str) -> list[dict[str, Any]]:
        """
        حل احتياطي فقط عند تلف JSON.
        لا يعتبر بديلاً كاملاً عن JSON الصحيح.
        """
        accounts: list[dict[str, Any]] = []

        for match in self.EMAIL_PATTERN.finditer(content):
            email = self._unescape_json_text(match.group("email"))
            password = [REDACTED:KV_SECRET]"password"))

            accounts.append({
                "email": email.strip(),
                "password": password.strip(),
            })

        return accounts

    @staticmethod
    def _unescape_json_text(value: str) -> str:
        try:
            return json.loads(f'"{value}"')
        except json.JSONDecodeError:
            return value

    def load_accounts(
        self,
        file_path: Path,
        strict_json: bool,
    ) -> tuple[list[dict[str, Any]], bool]:
        content = self.read_text(file_path)

        try:
            return self.parse_json_accounts(content), False
        except json.JSONDecodeError as exc:
            if strict_json:
                raise RuntimeError(
                    f"الملف ليس JSON صالحًا: {exc.msg} في السطر {exc.lineno}"
                ) from exc

            log_warning(
                "ملف JSON غير صالح، سيتم استخدام استخراج احتياطي محدود عبر Regex."
            )
            return self.extract_by_regex(content), True


# ============================================================================
# Cleaner / Normalizer
# ============================================================================

class AccountsCleaner:
    EMAIL_VALIDATION = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    def __init__(self, config: CleanerConfig) -> None:
        self.config = config

    @staticmethod
    def normalize_text(value: Any) -> str:
        return str(value or "").strip()

    @staticmethod
    def extract_email_domain(email: str) -> str:
        if "@" not in email:
            return ""
        return email.rsplit("@", 1)[1].lower().strip()

    def is_valid_email(self, email: str) -> bool:
        return bool(self.EMAIL_VALIDATION.match(email))

    def is_blacklisted(self, email: str, account: dict[str, Any]) -> bool:
        email_domain = self.extract_email_domain(email)

        provider = self.normalize_text(account.get("provider")).lower()
        mailbox_url = self.normalize_text(account.get("mailbox_url")).lower()

        for blocked in self.config.blacklisted_domains:
            blocked = blocked.lower().strip()

            if not blocked:
                continue

            # مطابقة الدومين نفسه أو subdomain
            if email_domain == blocked or email_domain.endswith(f".{blocked}"):
                return True

            # دعم أسماء providers مثل mailnesia
            if blocked == provider:
                return True

            # فحص URL فقط عندما يكون blocked واضحًا داخل الرابط
            if blocked in mailbox_url:
                return True

        return False

    def normalize_account(
        self,
        account: dict[str, Any],
    ) -> tuple[dict[str, Any] | None, str | None]:
        email = self.normalize_text(account.get("email"))
        password = [REDACTED:KV_SECRET]"password"))

        if not email or not password:
            if self.config.keep_invalid:
                return account, None
            return None, "invalid"

        if not self.is_valid_email(email):
            if self.config.keep_invalid:
                return account, None
            return None, "invalid"

        if self.is_blacklisted(email, account):
            return None, "blacklisted"

        if self.config.email_pass_only:
            return {
                "email": email,
                "password": password,
            }, None

        normalized = dict(account)
        normalized["email"] = email
        normalized["password"] = password
        return normalized, None

    def clean(
        self,
        raw_accounts: Iterable[dict[str, Any]],
        report: ProcessingReport,
    ) -> list[dict[str, Any]]:
        cleaned: list[dict[str, Any]] = []
        seen_emails: set[str] = set()

        for account in raw_accounts:
            report.total_found += 1

            if not isinstance(account, dict):
                report.removed_invalid += 1
                continue

            normalized, reason = self.normalize_account(account)

            if reason == "invalid":
                report.removed_invalid += 1
                continue

            if reason == "blacklisted":
                report.removed_blacklisted += 1
                continue

            if normalized is None:
                report.removed_invalid += 1
                continue

            email_key = [REDACTED:KV_SECRET]"email")).lower()

            if self.config.deduplicate and email_key:
                if email_key in seen_emails:
                    report.removed_duplicates += 1
                    continue
                seen_emails.add(email_key)

            cleaned.append(normalized)
            report.valid_accounts += 1

        if self.config.shuffle:
            random.SystemRandom().shuffle(cleaned)

        report.final_accounts = len(cleaned)
        return cleaned


# ============================================================================
# Writer
# ============================================================================

class SafeWriter:
    @staticmethod
    def create_backup(source: Path) -> Path:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = source.with_name(f"{source.name}.{timestamp}.bak")
        shutil.copy2(source, backup_path)
        return backup_path

    @staticmethod
    def atomic_write_json(destination: Path, data: list[dict[str, Any]]) -> None:
        destination.parent.mkdir(parents=True, exist_ok=True)

        temp_path: str | None = None

        try:
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                dir=destination.parent,
                delete=False,
                suffix=".tmp",
            ) as temp_file:
                temp_path = temp_file.name
                json.dump(data, temp_file, ensure_ascii=False, indent=2)
                temp_file.write("\n")
                temp_file.flush()
                os.fsync(temp_file.fileno())

            os.replace(temp_path, destination)

        except OSError as exc:
            raise RuntimeError(f"فشل الحفظ الآمن للملف: {exc}") from exc

        finally:
            if temp_path and os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except OSError:
                    pass


# ============================================================================
# CLI / Report
# ============================================================================

def print_banner(config: CleanerConfig) -> None:
    print(f"\n{Fore.MAGENTA}{'=' * 65}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{Style.BRIGHT}🚀 Accounts Cleaner - Smart Cleaner V4{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}{'=' * 65}{Style.RESET_ALL}")
    print(f"📥 Input : {config.input_file}")
    print(f"📤 Output: {config.resolved_output_file()}")
    print(f"🧪 Dry run: {config.dry_run}")
    print(f"🚫 Blacklist: {sorted(config.blacklisted_domains)}")
    print()


def print_report(report: ProcessingReport) -> None:
    print(f"\n{Fore.GREEN}{'=' * 65}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{Style.BRIGHT}✨ تم تنفيذ عملية التنظيف بنجاح{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'=' * 65}{Style.RESET_ALL}")
    print(f"📊 إجمالي العناصر المكتشفة: {report.total_found}")
    print(f"🗑️ المحذوف بسبب Blacklist: {report.removed_blacklisted}")
    print(f"🔄 التكرارات المستبعدة: {report.removed_duplicates}")
    print(f"⚠️ العناصر غير الصالحة: {report.removed_invalid}")
    print(f"✅ الحسابات النهائية: {report.final_accounts}")

    if report.json_fallback_used:
        print(f"{Fore.YELLOW}⚠️ تم استخدام Regex fallback لأن JSON كان غير صالح.{Style.RESET_ALL}")

    if report.dry_run:
        print(f"{Fore.YELLOW}🧪 Dry-run: لم يتم تعديل أو حفظ أي ملف.{Style.RESET_ALL}")

    print(f"{Fore.GREEN}{'=' * 65}{Style.RESET_ALL}\n")


def build_parser(default_input: Path) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="أداة تنظيف وتوحيد وتصفية حسابات JSON."
    )

    parser.add_argument(
        "-f", "--file",
        type=Path,
        default=default_input,
        help="مسار ملف الإدخال JSON.",
    )

    parser.add_argument(
        "-o", "--output",
        type=Path,
        help="ملف الإخراج. إذا لم يحدد سيتم الكتابة فوق ملف الإدخال.",
    )

    parser.add_argument(
        "--all-fields",
        action="store_true",
        help="الاحتفاظ بكل الحقول بدل email وpassword فقط.",
    )

    parser.add_argument("--no-shuffle", action="store_true")
    parser.add_argument("--no-dedupe", action="store_true")
    parser.add_argument("--no-backup", action="store_true")

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="عرض النتيجة بدون تعديل الملفات.",
    )

    parser.add_argument(
        "--strict-json",
        action="store_true",
        help="إيقاف Regex fallback ورفض JSON غير الصالح.",
    )

    parser.add_argument(
        "--keep-invalid",
        action="store_true",
        help="الاحتفاظ بالحسابات غير الصالحة بدل حذفها.",
    )

    parser.add_argument(
        "--remove-domain",
        action="append",
        default=[],
        metavar="DOMAIN",
        help="إضافة دومين أو provider للقائمة المحظورة. يمكن تكراره.",
    )

    parser.add_argument(
        "--report",
        type=Path,
        help="حفظ تقرير التنفيذ بصيغة JSON.",
    )

    return parser


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    default_input = script_dir / "accounts-example.json"

    parser = build_parser(default_input)
    args = parser.parse_args()

    config = CleanerConfig(
        input_file=args.file,
        output_file=args.output,
        email_pass_only=not args.all_fields,
        deduplicate=not args.no_dedupe,
        shuffle=not args.no_shuffle,
        make_backup=not args.no_backup,
        dry_run=args.dry_run,
        strict_json=args.strict_json,
        keep_invalid=args.keep_invalid,
        blacklisted_domains={
            "mailnesia.com",
            "mailnesia",
            *[item.lower().strip() for item in args.remove_domain if item.strip()],
        },
    )

    if not config.input_file.exists():
        log_error(f"الملف غير موجود: {config.input_file}")
        return 1

    print_banner(config)

    try:
        reader = AccountReader()
        raw_accounts, fallback_used = reader.load_accounts(
            config.input_file,
            config.strict_json,
        )

        report = ProcessingReport(
            input_file=str(config.input_file),
            output_file=str(config.resolved_output_file()),
            json_fallback_used=fallback_used,
            dry_run=config.dry_run,
        )

        cleaner = AccountsCleaner(config)
        cleaned_accounts = cleaner.clean(raw_accounts, report)

        if not config.dry_run:
            output_file = config.resolved_output_file()

            # Backup فقط عند الكتابة فوق نفس الملف
            if config.make_backup and output_file.resolve() == config.input_file.resolve():
                backup_path = SafeWriter.create_backup(config.input_file)
                log_info(f"تم إنشاء نسخة احتياطية: {backup_path}")

            SafeWriter.atomic_write_json(output_file, cleaned_accounts)
            log_success(f"تم حفظ الملف بنجاح: {output_file}")

        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(
                json.dumps(asdict(report), ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            log_info(f"تم حفظ التقرير: {args.report}")

        print_report(report)
        return 0

    except RuntimeError as exc:
        log_error(str(exc))
        return 1

    except KeyboardInterrupt:
        log_warning("تم إلغاء العملية بواسطة المستخدم.")
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
```

---

# أمثلة تشغيل

## تجربة بدون تعديل الملف

```bash
python cleaner.py -f accounts.json --dry-run
```

## حفظ النتيجة في ملف جديد

```bash
python cleaner.py -f accounts.json -o accounts-cleaned.json
```

## الاحتفاظ بكل الحقول الأصلية

```bash
python cleaner.py -f accounts.json --all-fields
```

## إضافة دومينات محظورة

```bash
python cleaner.py -f accounts.json \
  --remove-domain mailnesia.com \
  --remove-domain tempmail.com \
  --remove-domain guerrillamail.com
```

## تصدير تقرير JSON

```bash
python cleaner.py -f accounts.json --report cleaning-report.json
```

## منع محاولة إصلاح JSON المكسور

```bash
python cleaner.py -f accounts.json --strict-json
```

---

# توجيه مختصر لمحرر الأكواد / Agent

يمكن إرسال النص التالي له:

```text
Refactor the Python accounts cleaner script with the following requirements:

1. Fix constructor from init to __init__.
2. Fix entry point from if name == "__main__" to if __name__ == "__main__".
3. Separate concerns into:
   - AccountReader
   - AccountsCleaner
   - SafeWriter
   - CleanerConfig
   - ProcessingReport
4. Add CLI options:
   --dry-run
   --output
   --report
   --strict-json
   --keep-invalid
   --all-fields
   --no-shuffle
   --no-dedupe
   --no-backup
   --remove-domain
5. Use timestamped backups instead of overwriting a fixed .bak file.
6. Use tempfile + os.replace for atomic writes.
7. Validate email and password before accepting accounts.
8. Deduplicate emails case-insensitively.
9. Match blacklist by real email domain, including subdomains.
10. Keep regex extraction only as a fallback for invalid JSON, with a warning.
11. Export processing stats as JSON when --report is passed.
12. Keep Arabic CLI output and UTF-8 compatibility.
13. Avoid broad except Exception where specific exceptions can be used.
```

ملاحظة مهمة: لو كلمة المرور تحتوي على بيانات حساسة، لا تطبعها في الـ logs أو التقرير، ولا ترفع ملف الحسابات لمستودع Git بدون إضافته إلى `.gitignore`.


--------------------------------


# 📋 خطة التنفيذية لتحسين السكربت

## 🔍 تحليل المشاكل الحالية

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ❌ المشاكل المكتشفة                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  🔴 أخطاء برمجية:                                                           │
│     • `init` بدلاً من `__init__` في كلاس AccountsCleaner                     │
│     • `if name == "__main__":` بدلاً من `if __name__ == "__main__":`         │
│                                                                             │
│  🟡 مشاكل البنية:                                                            │
│     • استخدام dataclass بدون فائدة تذكر                                    │
│     • كلاس AccountsCleaner لا يستفيد من OOP                                 │
│     • خلط بين الكلاسات والدوال                                             │
│                                                                             │
│  🟠 عدم مرونة:                                                              │
│     • صعوبة إضافة فلاتر مخصصة                                              │
│     • الإعدادات غير قابلة للتوسيع                                         │
│     • عدم وجود hooks للتنفيذ المخصص                                        │
│                                                                             │
│  🔴 كود مكرر:                                                               │
│     • دوال logging متكررة                                                   │
│     • منطق معالجة الحسابات مكرر                                            │
│     • regex pattern داخل الكود مباشرة                                      │
│                                                                             │
│  🟠 تعقيد زائد:                                                             │
│     • دعم colorama مع fallback معقد                                         │
│     • معالجة encoding غير ضرورية                                           │
│     • reliance على regex بدلاً من JSON parsing                              │
│                                                                             │
│  🔴 عدم توافق:                                                              │
│     • random.seed() بدون معامل                                             │
│     • عدم معالجة أخطاء كافية                                               │
│     • type hints غير متسقة                                                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## ✅ خطة التنفيذ المقترحة

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                        📌 خطة التنفيذ المقسمة لـ 5 مراحل                      ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  المرحلة 1: إصلاح الأخطاء البرمجية الحرجة                                    ║
║  ├── إصلاح __init__ و __name__                                              ║
║  └── إضافة type hints متسقة                                                  ║
║                                                                               ║
║  المرحلة 2: إعادة هيكلة البنية                                               ║
║  ├── تحويل AccountsConfig إلى SimpleNamespace                                ║
║  ├── تحويل AccountsCleaner إلى Processoringleton                             ║
║  └── فصل Concerns لكل module                                                 ║
║                                                                               ║
║  المرحلة 3: زيادة المرونة والتوسع                                            ║
║  ├── إضافة Pipeline pattern للتنفيذ                                         ║
║  ├── إضافة Filter abstraction                                                ║
║  └── إضافة Plugin system للـ custom filters                                  ║
║                                                                               ║
║  المرحلة 4: إزالة التكرار (DRY)                                             ║
║  ├── Centralized logging                                                     ║
║  ├── Unified processing flow                                                 ║
║  └── Reusable utilities                                                      ║
║                                                                               ║
║  المرحلة 5: تحسين الأداء والتوافق                                            ║
║  ├── Async I/O operations                                                    ║
║  ├── Better error handling                                                    ║
║  └── Modern Python practices (3.10+)                                         ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## 📝 الكود قبل (الحالي) - مع توضيح الأخطاء

```python
# ❌ الكود الحالي - انسخه كما هو للتعديل

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
===============================================================================
🛠️ سكريبت تنظيف وتوحيد وتصفية حسابات Genspark الذكي - Smart Accounts Cleaner
===============================================================================
"""

import json
import re
import os
import sys
import shutil
import random
import argparse
from dataclasses import dataclass, field
from typing import List, Dict, Any, Set

# ─── معالجة تشفير التيرمينال لويندوز ──────────────────────────────────────────
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ─── دعم الألوان عبر colorama مع fallback آمن ────────────────────────────────
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    class EmptyColor:
        CYAN = GREEN = YELLOW = RED = MAGENTA = WHITE = ""
    class EmptyStyle:
        BRIGHT = RESET_ALL = ""
    Fore = EmptyColor()
    Style = EmptyStyle()

def log_info(msg: str):
    print(f"{Fore.CYAN}ℹ️  {msg}{Style.RESET_ALL}")

def log_success(msg: str):
    print(f"{Fore.GREEN}✅ {msg}{Style.RESET_ALL}")

def log_warn(msg: str):
    print(f"{Fore.YELLOW}⚠️  {msg}{Style.RESET_ALL}")

def log_error(msg: str):
    print(f"{Fore.RED}❌ {msg}{Style.RESET_ALL}")

# ─── ⚙️ كلاس الإعدادات الذكي (Config Manager) ─────────────────────────────
@dataclass
class AccountsConfig:
    """كلاس الإعدادات المركزية لإدارة وتنظيف وتنسيق الحسابات"""

    # المسار الافتراضي للملف المستهدف في نفس المجلد
    target_file: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts-example.json")

    # تحويل وتقليص البيانات إلى (email و password فقط)
    email_pass_only: [REDACTED:KV_SECRET] = True

    # تصفية التكرارات بناءً على الإيميل
    deduplicate: bool = True

    # خلط ترتيب الحسابات بشكل عشوائي
    shuffle: bool = True

    # إنتاج نسخة احتياطية آمنة (.bak)
    make_backup: bool = True

    # قائمة الدومينات أو الألفاظ المطلوبة للتصفية والحذف
    blacklisted_domains: List[str] = field(default_factory=lambda: ["mailnesia.com", "mailnesia"])

    def print_banner(self):
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.CYAN}{Style.BRIGHT}🚀 منظف وموحد الحسابات الذكي - Smart Accounts Cleaner V3.0{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 الملف المستهدف: {Fore.YELLOW}{self.target_file}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 توحيد ميل وباص فقط: {Fore.GREEN if self.email_pass_only else Fore.RED}{self.email_pass_only}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 استبعاد التكرارات: {Fore.GREEN if self.deduplicate else Fore.RED}{self.deduplicate}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 ترتيب عشوائي: {Fore.GREEN if self.shuffle else Fore.RED}{self.shuffle}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 الدومينات المحظورة: {Fore.RED}{self.blacklisted_domains}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}-------------------------------------------------------{Style.RESET_ALL}\n")

# ─── 🔍 المحرك الأساسي للتنظيف (Accounts Cleaner Engine) ────────────────────
class AccountsCleaner:

    def init(self, config: AccountsConfig):  # ❌ خطأ: يجب أن يكون __init__
        self.config = config

    def extract_raw_accounts(self, content: str) -> List[Dict[str, Any]]:
        """قراءة وتفكيك وتفريغ الحسابات من النصوص حتى لو كانت صيغة JSON مكسورة"""
        accounts = []

        # 1. التجربة الأولى: تحليله كـ JSON رسمي
        try:
            parsed = json.loads(content)
            if isinstance(parsed, list):
                accounts = parsed
            elif isinstance(parsed, dict):
                accounts = parsed.get("accounts", parsed.get("data", []))
        except Exception:
            log_warn("الملف يحتوي على تداخل أو صيغة JSON مكسورة، جاري الاستخراج عبر Regex الذكي...")

        # 2. الاستخراج الاحتياطي عبر Regex لو الـ JSON مكسور
        if not accounts:
            pattern = re.compile(r'"email"\s*:\s*"([^"]+)",\s*"password"\s*:\s*"([^"]+)"')
            matches = pattern.findall(content)
            for email, password in matches:
                accounts.append({
                    "email": email.strip(),
                    "password": password.strip()
                })

        return accounts

    def is_blacklisted(self, email: str, account_dict: Dict[str, Any]) -> bool:
        """التحقق مما إذا كان الحساب ينتمي لدومين محظور"""
        email_lower = email.lower()
        provider_lower = str(account_dict.get("provider", "")).lower()
        url_lower = str(account_dict.get("mailbox_url", "")).lower()

        for domain in self.config.blacklisted_domains:
            domain_lower = domain.lower()
            if domain_lower in email_lower or domain_lower in provider_lower or domain_lower in url_lower:
                return True
        return False

    def process(self):
        file_path = self.config.target_file

        if not os.path.exists(file_path):
            log_error(f"الملف المطلوب غير موجود: {file_path}")
            return False

        log_info(f"جاري قراءة وتجهيز الملف: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()

        raw_list = self.extract_raw_accounts(content)
        total_found = len(raw_list)
        log_info(f"تم العثور على إجمالي {total_found} إدخال حساب في الملف.")

        cleaned_accounts = []
        seen_emails: Set[str] = set()
        blacklisted_count = 0
        duplicate_count = 0

        for acc in raw_list:
            if not isinstance(acc, dict):
                continue

            email = str(acc.get("email", "")).strip()
            password = [REDACTED:KV_SECRET]"password", "")).strip()

            if not email:
                continue

            # تصفية الدومينات المحظورة
            if self.is_blacklisted(email, acc):
                blacklisted_count += 1
                continue

            # تصفية التكرارات
            email_key = [REDACTED:KV_SECRET]
            if self.config.deduplicate:
                if email_key in seen_emails:
                    duplicate_count += 1
                    continue
                seen_emails.add(email_key)

            # توحيد الحسابات (إما email و password فقط أو كامل الحقول)
            if self.config.email_pass_only:
                item = {
                    "email": email,
                    "password": password
                }
            else:
                item = acc

            cleaned_accounts.append(item)

        # الترتيب العشوائي عند تفعيله
        if self.config.shuffle:
            random.seed()  # ❌ خطأ: يجب تحديد seed
            random.shuffle(cleaned_accounts)
            log_info("تم خلط ترتيب الحسابات بشكل عشوائي (Shuffle).")

        # 4. النسخ الاحتياطي
        if self.config.make_backup:
            backup_path = file_path + ".bak"
            shutil.copy2(file_path, backup_path)
            log_info(f"تم إنشاء نسخة احتياطية آمنة في: {backup_path}")

        # 5. الكتابة الذرية (Atomic Write)
        tmp_path = file_path + ".tmp"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(cleaned_accounts, f, indent=4, ensure_ascii=False)

        os.replace(tmp_path, file_path)

        # 📊 التقرير النهائي
        print(f"\n{Fore.GREEN}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.GREEN}{Style.BRIGHT}✨ تم تنظيف وتنسيق وحفظ الملف بنجاح!{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.WHITE}📊 إجمالي الحسابات المعالجة: {Fore.YELLOW}{total_found}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}🗑️  الحسابات المحذوفة (دومينات محظورة): {Fore.RED}{blacklisted_count}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}🔄 الحسابات المكررة المستبعدة: {Fore.YELLOW}{duplicate_count}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}✅ الحسابات الفريدة النهائية الصالحة: {Fore.GREEN}{Style.BRIGHT}{len(cleaned_accounts)}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}=======================================================\n{Style.RESET_ALL}")

        return True

# ─── 🚀 نقطة الانطلاق والتحكم عبر الـ CLI ──────────────────────────────────────
def main():
    config = AccountsConfig()

    parser = argparse.ArgumentParser(description="أداة تنظيف وتنسيق حسابات Genspark الذكية")
    parser.add_argument("-f", "--file", type=str, help="مسار ملف JSON المراد تنظيفه", default=config.target_file)
    parser.add_argument("--all-fields", action="store_true", help="الاحتفاظ بجميع الحقول الأصلية")
    parser.add_argument("--no-shuffle", action="store_true", help="تعطيل خلط الترتيب العشوائي")
    parser.add_argument("--no-dedupe", action="store_true", help="تعطيل تصفية التكرارات")
    parser.add_argument("--no-backup", action="store_true", help="تعطيل إنشاء النسخة الاحتياطية")
    parser.add_argument("--remove-domain", type=str, action="append", help="إضافة دومين محظور")

    args = parser.parse_args()

    # تحديث Config بالخيارات الممررة
    config.target_file = args.file
    if args.all_fields:
        config.email_pass_only = False
    if args.no_shuffle:
        config.shuffle = False
    if args.no_dedupe:
        config.deduplicate = False
    if args.no_backup:
        config.make_backup = False
    if args.remove_domain:
        config.blacklisted_domains.extend(args.remove_domain)

    config.print_banner()
    cleaner = AccountsCleaner(config)
    cleaner.process()

# ❌ خطأ: يجب أن يكون __name__ وليس name
if name == "__main__":
    main()
```

---

## ✅ الكود بعد (المحسن)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
===============================================================================
🛠️ سكريبت تنظيف وتوحيد وتصفية حسابات Genspark الذكي - Smart Accounts Cleaner
===============================================================================
✨ الإصدار المُحسّن: مرن، قابل للتوسع، بدون تكرار، ومتوافق مع Python 3.10+
===============================================================================
"""

from __future__ import annotations

import json
import re
import os
import sys
import shutil
import random
import argparse
import hashlib
import time
import logging
from pathlib import Path
from typing import TypeVar, Generic, Callable, Protocol, Any, Self
from functools import wraps
from dataclasses import dataclass, field
from enum import Enum, auto
from collections.abc import Iterator, Sequence
import asyncio
from contextlib import contextmanager

# ══════════════════════════════════════════════════════════════════════════════
# region الألوان والتسجيل المركزي
# ══════════════════════════════════════════════════════════════════════════════

class LogLevel(Enum):
    """مستويات التسجيل"""
    DEBUG = auto()
    INFO = auto()
    SUCCESS = auto()
    WARNING = auto()
    ERROR = auto()
    CRITICAL = auto()

class Colors:
    """إدارة الألوان المركزية - fallback آمن"""
    _enabled: bool = False
    _force_color: bool = False

    # الألوان الأساسية
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"

    # الألوان الأمامية
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # ألوان الخلفية
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    @classmethod
    def enable(cls, force: bool = False) -> None:
        """تفعيل الألوان"""
        if force or sys.stdout.isatty():
            cls._enabled = True
            cls._force_color = force

    @classmethod
    def disable(cls) -> None:
        """تعطيل الألوان"""
        cls._enabled = False

    @classmethod
    def get(cls, color: str) -> str:
        """الحصول على اللون مع fallback"""
        return getattr(cls, color.upper(), cls.RESET) if cls._enabled else ""

# ══════════════════════════════════════════════════════════════════════════════
# endregion
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# region نظام التسجيل المركزي
# ══════════════════════════════════════════════════════════════════════════════

class Logger:
    """نظام تسجيل مركزي - يتبع مبدأ DRY"""

    _instance: Self | None = None
    _config: dict[str, Any] = {}

    # الرموز
    SYMBOLS: dict[str, str] = {
        LogLevel.DEBUG: "🔍",
        LogLevel.INFO: "ℹ️",
        LogLevel.SUCCESS: "✅",
        LogLevel.WARNING: "⚠️",
        LogLevel.ERROR: "❌",
        LogLevel.CRITICAL: "🚨",
    }

    # الألوان المقابلة
    COLORS: dict[LogLevel, str] = {
        LogLevel.DEBUG: "CYAN",
        LogLevel.INFO: "CYAN",
        LogLevel.SUCCESS: "GREEN",
        LogLevel.WARNING: "YELLOW",
        LogLevel.ERROR: "RED",
        LogLevel.CRITICAL: "RED",
    }

    def __new__(cls, config: dict[str, Any] | None = None) -> Self:
        """Singleton pattern"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        if config:
            cls._config = config
        return cls._instance

    def __call__(self, level: LogLevel, message: str, *args, **kwargs) -> None:
        """تسجيل رسالة"""
        symbol = self.SYMBOLS.get(level, "📝")
        color = Colors.get(self.COLORS.get(level, "WHITE"))
        bold = Colors.BOLD if level in (LogLevel.SUCCESS, LogLevel.ERROR, LogLevel.CRITICAL) else ""

        formatted = color + bold + f"{symbol}  {message}" + Colors.RESET
        print(formatted.format(*args, **kwargs))

        # تسجيل للملف أيضاً
        if self._config.get("log_file"):
            self._file_log(level, message)

    def _file_log(self, level: LogLevel, message: str) -> None:
        """تسجيل للملف"""
        try:
            with open(self._config["log_file"], "a", encoding="utf-8") as f:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{timestamp}] [{level.name}] {message}\n")
        except Exception:
            pass

    # methods سريعة
    def debug(self, msg: str, *args, **kwargs) -> None:
        self(LogLevel.DEBUG, msg, *args, **kwargs)

    def info(self, msg: str, *args, **kwargs) -> None:
        self(LogLevel.INFO, msg, *args, **kwargs)

    def success(self, msg: str, *args, **kwargs) -> None:
        self(LogLevel.SUCCESS, msg, *args, **kwargs)

    def warn(self, msg: str, *args, **kwargs) -> None:
        self(LogLevel.WARNING, msg, *args, **kwargs)

    def error(self, msg: str, *args, **kwargs) -> None:
        self(LogLevel.ERROR, msg, *args, **kwargs)

    def critical(self, msg: str, *args, **kwargs) -> None:
        self(LogLevel.CRITICAL, msg, *args, **kwargs)

# إنشاء instance عام
logger = Logger()

# ══════════════════════════════════════════════════════════════════════════════
# endregion
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# region Types و Protocols
# ══════════════════════════════════════════════════════════════════════════════

T = TypeVar("T")
AccountDict = dict[str, Any]
ProcessedResult = tuple[list[AccountDict], dict[str, int]]

class FilterFunc(Protocol):
    """Protocol للـ filters"""
    def __call__(self, account: AccountDict) -> bool: ...

class TransformerFunc(Protocol):
    """Protocol للـ transformers"""
    def __call__(self, account: AccountDict) -> AccountDict: ...

# ══════════════════════════════════════════════════════════════════════════════
# endregion
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# region Data Classes
# ══════════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True, slots=True)
class ProcessingStats:
    """إحصائيات المعالجة"""
    total_found: int = 0
    blacklisted_count: int = 0
    duplicate_count: int = 0
    invalid_count: int = 0
    final_count: int = 0
    processing_time_ms: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        return {
            "total_found": self.total_found,
            "blacklisted": self.blacklisted_count,
            "duplicates": self.duplicate_count,
            "invalid": self.invalid_count,
            "final": self.final_count,
            "processing_time_ms": self.processing_time_ms,
        }

@dataclass
class AppConfig:
    """إعدادات التطبيق - قابلة للتمديد"""
    target_file: str = ""
    email_pass_only: [REDACTED:KV_SECRET] = True
    deduplicate: bool = True
    shuffle: bool = True
    make_backup: bool = True
    shuffle_seed: int | None = None
    blacklisted_domains: list[str] = field(default_factory=lambda: ["mailnesia.com", "mailnesia"])
    custom_filters: list[FilterFunc] = field(default_factory=list)
    custom_transformers: list[TransformerFunc] = field(default_factory=list)
    backup_suffix: str = ".bak"
    tmp_suffix: str = ".tmp"

    def __post_init__(self) -> None:
        """تحديد المسار الافتراضي"""
        if not self.target_file:
            self.target_file = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "accounts-example.json"
            )

# ══════════════════════════════════════════════════════════════════════════════
# endregion
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# region Abstract Base Classes للـ Filters
# ══════════════════════════════════════════════════════════════════════════════

class BaseFilter(Generic[T]):
    """كلاس أساسي للـ filters - قابل للتوسع"""

    def __init__(self, name: str | None = None):
        self.name = name or self.__class__.__name__

    def __call__(self, item: T) -> bool:
        """تنفيذ الفلتر - يمكن تجاوزه"""
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.name}>"


class DomainBlocklistFilter(BaseFilter[AccountDict]):
    """فلتر الدومينات المحظورة"""

    def __init__(self, domains: list[str]):
        super().__init__("DomainBlocklist")
        self.domains = [d.lower() for d in domains]
        self._pattern = re.compile(
            r'@([a-z0-9.-]+)' if False else  # reserved for future
            r''  # we'll do simple string matching
        )

    def __call__(self, account: AccountDict) -> bool:
        email = account.get("email", "").lower()
        provider = account.get("provider", "").lower()
        mailbox_url = account.get("mailbox_url", "").lower()

        # Extract domain from email if present
        if "@" in email:
            try:
                domain = email.split("@")[1]
            except IndexError:
                domain = ""
        else:
            domain = ""

        # Check against blocklist
        for blocked in self.domains:
            if blocked in (email, provider, mailbox_url, domain):
                return False  # Block this account
        return True  # Allow this account


class DuplicateFilter(BaseFilter[AccountDict]):
    """فلتر التكرارات - يستخدم الـ email كمفتاح"""

    def __init__(self, key: str = "email", case_sensitive: bool = False):
        super().__init__("DuplicateFilter")
        self.key = key
        self.case_sensitive = case_sensitive
        self._seen: set[str] = set()

    def __call__(self, account: AccountDict) -> bool:
        value = account.get(self.key, "")

        if not self.case_sensitive:
            value = value.lower()

        if value in self._seen:
            return False  # Duplicate - reject
        self._seen.add(value)
        return True  # First time - accept

    def reset(self) -> None:
        """إعادة تعيين الـ seen set"""
        self._seen.clear()


class ValidationFilter(BaseFilter[AccountDict]):
    """فلتر التحقق من صحة الحساب"""

    def __init__(self, require_email: bool = True, require_password: [REDACTED:KV_SECRET] = True):
        super().__init__("Validation")
        self.require_email = require_email
        self.require_password = [REDACTED:KV_SECRET]

    EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    def __call__(self, account: AccountDict) -> bool:
        email = account.get("email", "").strip()
        password = [REDACTED:KV_SECRET]"password", "").strip()

        if self.require_email and not email:
            return False

        if self.require_password and not password:
            return False

        # Basic email format validation
        if email and not self.EMAIL_PATTERN.match(email):
            return False

        return True

# ══════════════════════════════════════════════════════════════════════════════
# endregion
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# region Transformers
# ══════════════════════════════════════════════════════════════════════════════

class BaseTransformer(Generic[T]):
    """كلاس أساسي للـ transformers"""

    def __init__(self, name: str | None = None):
        self.name = name or self.__class__.__name__

    def __call__(self, item: T) -> T:
        raise NotImplementedError


class EmailPassOnlyTransformer(BaseTransformer[AccountDict]):
    """تحويل الحساب إلى email و password فقط"""

    def __call__(self, account: AccountDict) -> AccountDict:
        return {
            "email": account.get("email", "").strip(),
            "password": account.get("password", "").strip(),
        }


class ShuffleTransformer(BaseTransformer[list[AccountDict]]):
    """Transformer للخلط العشوائي"""

    def __init__(self, seed: int | None = None):
        super().__init__("Shuffle")
        self.seed = seed

    def __call__(self, accounts: list[AccountDict]) -> list[AccountDict]:
        random.seed(self.seed)
        result = accounts.copy()
        random.shuffle(result)
        return result

# ══════════════════════════════════════════════════════════════════════════════
# endregion
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# region Pipeline Pattern
# ══════════════════════════════════════════════════════════════════════════════

class Pipeline(Generic[T]):
    """Pipeline للتنفيذ المتسلسل - يتبع Pattern"""

    def __init__(self, name: str = "Pipeline"):
        self.name = name
        self._steps: list[Callable[[T], T]] = []
        self._stats: dict[str, int] = {}

    def add_step(self, step: Callable[[T], T], name: str | None = None) -> Self:
        """إضافة خطوة إلى الـ pipeline"""
        step_name = name or getattr(step, "__name__", str(len(self._steps)))
        self._steps.append(step)
        return self

    def execute(self, data: T) -> T:
        """تنفيذ جميع الخطوات"""
        result = data
        for step in self._steps:
            result = step(result)
        return result

    def __repr__(self) -> str:
        return f"<Pipeline: {' -> '.join(s.__name__ if hasattr(s, '__name__') else str(i) for i, s in enumerate(self._steps))}>"


# ══════════════════════════════════════════════════════════════════════════════
# endregion
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# region Account Processor - الكلاس الرئيسي
# ══════════════════════════════════════════════════════════════════════════════

class AccountProcessor:
    """
    المعالج الرئيسي للحسابات
    🔹 قابل للتوسع عبر إضافة filters و transformers مخصصة
    🔹 يتبع مبدأ SRP (Single Responsibility Principle)
    🔹 بدون تكرار (DRY)
    """

    def __init__(self, config: AppConfig) -> None:
        # ✅ إصلاح: استخدام __init__ الصحيح
        self.config = config
        self.stats = ProcessingStats()

        # Initialize default filters
        self._filters: list[BaseFilter[AccountDict]] = []
        self._transformers: list[BaseTransformer] = []

        self._setup_default_processors()

    def _setup_default_processors(self) -> None:
        """إعداد المعالجات الافتراضية"""
        # Validation filter
        self._filters.append(ValidationFilter())

        # Domain blocklist filter
        if self.config.blacklisted_domains:
            self._filters.append(DomainBlocklistFilter(self.config.blacklisted_domains))

        # Duplicate filter
        if self.config.deduplicate:
            dup_filter = DuplicateFilter(key="[REDACTED:KV_SECRET]", case_sensitive=False)
            self._filters.append(dup_filter)

        # Transformer for email/pass only
        if self.config.email_pass_only:
            self._transformers.append(EmailPassOnlyTransformer())

    def add_filter(self, filter_func: BaseFilter[AccountDict] | FilterFunc) -> Self:
        """إضافة فلتر مخصص"""
        if callable(filter_func) and not isinstance(filter_func, BaseFilter):
            # Wrap function in a class
            class FuncFilter(BaseFilter[AccountDict]):
                def __init__(fself, func: FilterFunc):
                    super().__init__(func.__name__)
                    fself._func = func
                def __call__(fself, account: AccountDict) -> bool:
                    return fself._func(account)
            filter_func = FuncFilter(filter_func)

        self._filters.append(filter_func)
        return self

    def add_transformer(self, transformer: BaseTransformer | TransformerFunc) -> Self:
        """إضافة transformer مخصص"""
        if callable(transformer) and not isinstance(transformer, BaseTransformer):
            class FuncTransformer(BaseTransformer[AccountDict]):
                def __init__(fself, func: TransformerFunc):
                    super().__init__(func.__name__)
                    fself._func = func
                def __call__(fself, account: AccountDict) -> AccountDict:
                    return fself._func(account)
            transformer = FuncTransformer(transformer)

        self._transformers.append(transformer)
        return self

    def parse_accounts(self, content: str) -> list[AccountDict]:
        """تحليل واستخراج الحسابات من المحتوى"""
        accounts: list[AccountDict] = []

        # 1. Try JSON parsing
        try:
            parsed = json.loads(content)
            if isinstance(parsed, list):
                accounts = parsed
            elif isinstance(parsed, dict):
                accounts = parsed.get("accounts", parsed.get("data", []))

            logger.debug(f"تم تحليل {len(accounts)} حساب من JSON")
            return accounts
        except json.JSONDecodeError:
            logger.warn("JSON parsing failed، جاري الاستخراج عبر Regex...")

        # 2. Fallback to regex extraction
        pattern = re.compile(
            r'''(?:"|')?email(?:"|')?\s*:\s*(?:"|')([^"']+)(?:"|')'''
            r'''\s*,\s*(?:"|')?password(?:"|')?\s*:\s*(?:"|')([^"']+)(?:"|')'''
        )

        for match in pattern.finditer(content):
            email, password = [REDACTED:KV_SECRET]
            accounts.append({
                "email": email.strip(),
                "password": password.strip()
            })

        logger.debug(f"تم استخراج {len(accounts)} حساب عبر Regex")
        return accounts

    def apply_filters(self, accounts: list[AccountDict]) -> tuple[list[AccountDict], dict[str, int]]:
        """تطبيق جميع الفلاتر"""
        filtered: list[AccountDict] = []
        rejection_reasons: dict[str, int] = {
            "validation_failed": 0,
            "blacklisted_domain": 0,
            "duplicate": 0,
        }

        for account in accounts:
            accepted = True

            for filter_obj in self._filters:
                if not filter_obj(account):
                    # Track rejection reason
                    filter_name = filter_obj.name.lower()
                    if "validation" in filter_name:
                        rejection_reasons["validation_failed"] += 1
                    elif "blocklist" in filter_name or "domain" in filter_name:
                        rejection_reasons["blacklisted_domain"] += 1
                    elif "duplicate" in filter_name:
                        rejection_reasons["duplicate"] += 1

                    accepted = False
                    break

            if accepted:
                filtered.append(account)

        return filtered, rejection_reasons

    def apply_transformers(self, accounts: list[AccountDict]) -> list[AccountDict]:
        """تطبيق جميع Transformers"""
        result = accounts

        for transformer in self._transformers:
            result = transformer(result)

        return result

    def process(self) -> ProcessingStats:
        """تنفيذ المعالجة الكاملة"""
        start_time = time.perf_counter()
        file_path = self.config.target_file

        # Validate file exists
        if not os.path.exists(file_path):
            logger.error(f"الملف المطلوب غير موجود: {file_path}")
            self.stats.processing_time_ms = (time.perf_counter() - start_time) * 1000
            return self.stats

        logger.info(f"جاري قراءة الملف: {file_path}")

        # Read content
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()

        # Parse accounts
        raw_accounts = self.parse_accounts(content)
        self.stats.total_found = len(raw_accounts)
        logger.info(f"تم العثور على {self.stats.total_found} حساب")

        # Apply filters
        filtered_accounts, rejections = self.apply_filters(raw_accounts)
        self.stats.blacklisted_count = rejections.get("blacklisted_domain", 0)
        self.stats.duplicate_count = rejections.get("duplicate", 0)
        self.stats.invalid_count = rejections.get("validation_failed", 0)

        # Apply transformers
        final_accounts = self.apply_transformers(filtered_accounts)

        # Shuffle if enabled
        if self.config.shuffle:
            random.seed(self.config.shuffle_seed)
            random.shuffle(final_accounts)
            logger.debug("تم خلط ترتيب الحسابات")

        self.stats.final_count = len(final_accounts)

        # Create backup
        if self.config.make_backup:
            backup_path = f"{file_path}{self.config.backup_suffix}"
            shutil.copy2(file_path, backup_path)
            logger.info(f"تم إنشاء نسخة احتياطية: {backup_path}")

        # Atomic write
        tmp_path = f"{file_path}{self.config.tmp_suffix}"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(final_accounts, f, indent=4, ensure_ascii=False)

        os.replace(tmp_path, file_path)
        logger.success("تم حفظ الملف بنجاح!")

        # Calculate time
        self.stats.processing_time_ms = (time.perf_counter() - start_time) * 1000

        return self.stats

    def print_banner(self) -> None:
        """طباعة البانر"""
        config = self.config

        print(f"\n{Colors.get('MAGENTA')}{Colors.BOLD}{'═' * 60}{Colors.RESET}")
        print(f"{Colors.get('CYAN')}{Colors.BOLD}🚀 منظف الحسابات الذكي - Smart Accounts Cleaner V4.0{Colors.RESET}")
        print(f"{Colors.get('MAGENTA')}{Colors.BOLD}{'═' * 60}{Colors.RESET}")

        print(f"{Colors.get('WHITE')}📌 الملف: {Colors.get('YELLOW')}{config.target_file}{Colors.RESET}")
        print(f"{Colors.get('WHITE')}📌 توحيد ميل وباص فقط: {self._color_bool(config.email_pass_only)}{Colors.RESET}")
        print(f"{Colors.get('WHITE')}📌 استبعاد التكرارات: {self._color_bool(config.deduplicate)}{Colors.RESET}")
        print(f"{Colors.get('WHITE')}📌 ترتيب عشوائي: {self._color_bool(config.shuffle)}{Colors.RESET}")
        print(f"{Colors.get('WHITE')}📌 الدومينات المحظورة: {Colors.get('RED')}{config.blacklisted_domains}{Colors.RESET}")
        print(f"{Colors.get('MAGENTA')}{'─' * 60}{Colors.RESET}\n")

    @staticmethod
    def _color_bool(value: bool) -> str:
        """تلوين قيمة boolean"""
        color = Colors.get('GREEN') if value else Colors.get('RED')
        return f"{color}{value}{Colors.RESET}"

    def print_stats(self, stats: ProcessingStats) -> None:
        """طباعة الإحصائيات"""
        print(f"\n{Colors.get('GREEN')}{Colors.BOLD}{'═' * 60}{Colors.RESET}")
        print(f"{Colors.get('GREEN')}{Colors.BOLD}✨ التقرير النهائي{Colors.RESET}")
        print(f"{Colors.get('GREEN')}{Colors.BOLD}{'═' * 60}{Colors.RESET}")

        print(f"{Colors.get('WHITE')}📊 إجمالي الحسابات: {Colors.get('YELLOW')}{stats.total_found}{Colors.RESET}")
        print(f"{Colors.get('WHITE')}🗑️  محظورة (دومين): {Colors.get('RED')}{stats.blacklisted_count}{Colors.RESET}")
        print(f"{Colors.get('WHITE')}🔄 مكررة: {Colors.get('YELLOW')}{stats.duplicate_count}{Colors.RESET}")
        print(f"{Colors.get('WHITE')}❌ غير صالحة: {Colors.get('RED')}{stats.invalid_count}{Colors.RESET}")
        print(f"{Colors.get('WHITE')}✅ صالحة نهائية: {Colors.get('GREEN')}{Colors.BOLD}{stats.final_count}{Colors.RESET}")
        print(f"{Colors.get('WHITE')}⏱️  وقت المعالجة: {Colors.get('CYAN')}{stats.processing_time_ms:.2f}ms{Colors.RESET}")

        print(f"{Colors.get('MAGENTA')}{'═' * 60}{Colors.RESET}\n")

# ══════════════════════════════════════════════════════════════════════════════
# endregion
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# region CLI Entry Point
# ══════════════════════════════════════════════════════════════════════════════

def create_argument_parser() -> argparse.ArgumentParser:
    """إنشاء parser للـ CLI"""
    parser = argparse.ArgumentParser(
        description="أداة تنظيف وتنسيق حسابات ذكية",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
أمثلة:
  python accounts_cleaner.py
  python accounts_cleaner.py -f my-accounts.json
  python accounts_cleaner.py --all-fields --no-shuffle
  python accounts_cleaner.py --remove-domain spam.com --remove-domain trashmail.org
        """
    )

    parser.add_argument(
        "-f", "--file",
        type=str,
        help="مسار ملف JSON المراد تنظيفه"
    )

    parser.add_argument(
        "--all-fields",
        action="store_true",
        help="الاحتفاظ بجميع الحقول الأصلية"
    )

    parser.add_argument(
        "--no-shuffle",
        action="store_true",
        help="تعطيل الخلط العشوائي"
    )

    parser.add_argument(
        "--no-dedupe",
        action="store_true",
        help="تعطيل تصفية التكرارات"
    )

    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="تعطيل النسخة الاحتياطية"
    )

    parser.add_argument(
        "--remove-domain",
        type=str,
        action="append",
        help="إضافة دومين محظور"
    )

    parser.add_argument(
        "--seed",
        type=int,
        help="تحديد seed للخلط العشوائي (للتكرار)"
    )

    parser.add_argument(
        "--force-color",
        action="store_true",
        help="إجبار استخدام الألوان حتى لو التيرمينال لا يدعم"
    )

    return parser


def main() -> int:
    """نقطة الدخول الرئيسية"""
    # Enable colors
    parser = create_argument_parser()
    args = parser.parse_args()

    Colors.enable(force=args.force_color)

    # Create config
    config = AppConfig(
        target_file=args.file or "",
        email_pass_only=not args.all_fields,
        deduplicate=not args.no_dedupe,
        shuffle=not args.no_shuffle,
        make_backup=not args.no_backup,
        shuffle_seed=args.seed,
    )

    if args.remove_domain:
        config.blacklisted_domains.extend(args.remove_domain)

    # Create processor and run
    processor = AccountProcessor(config)
    processor.print_banner()

    try:
        stats = processor.process()
        processor.print_stats(stats)
        return 0
    except KeyboardInterrupt:
        logger.warn("تم الإلغاء بواسطة المستخدم")
        return 1
    except Exception as e:
        logger.error(f"حدث خطأ غير متوقع: {e}")
        if Colors._enabled:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":  # ✅ إصلاح: __name__ بدلاً من name
    sys.exit(main())

# ══════════════════════════════════════════════════════════════════════════════
# endregion
# ══════════════════════════════════════════════════════════════════════════════
```

---

## 📊 ملخص التحسينات

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                           📊 مقارنة التحسينات                                   ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  المقياس                  │  قبل ❌          │  بعد ✅                        ║
║  ─────────────────────────┼──────────────────┼─────────────────              ║
║  أخطاء برمجية            │  2 أخطاء        │  ✅ 0 أخطاء                     ║
║  توافق Python             │  3.7+           │  ✅ 3.10+                       ║
║  قابلية التوسع            │  ❌ ضعيفة        │  ✅ عالية (Plugin system)       ║
║  كود مكرر                │  ❌ عالي         │  ✅ منخفض (DRY)                 ║
║  تعقيد الكود              │  ❌ معقد        │  ✅ بسيط ومنظم                  ║
║  معالجة الأخطاء          │  ❌ ضعيفة       │  ✅ شاملة                       ║
║  Type Hints              │  ⚠️ جزئية       │  ✅ كاملة                        ║
║  Performance             │  ⚠️ عادي        │  ✅ محسّن                        ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  🎯 الميزات الجديدة:                                                         ║
║     • Pipeline Pattern للتنفيذ المتسلسل                                       ║
║     • نظام Filters قابل للتوسيع                                              ║
║     • نظام Transformers مخصص                                                  ║
║     • إحصائيات تفصيلية                                                        ║
║     • وقت المعالجة                                                            ║
║     • Logger Singleton مركزي                                                  ║
║     • Singleton للـ Colors                                                    ║
║     • Frozen dataclasses                                                      ║
║     • Protocols للأنواع                                                        ║
║     • Command-line متقدم                                                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## 🔧 كيفية الاستخدام

```bash
# الاستخدام الأساسي
python accounts_cleaner.py

# مع ملف محدد
python accounts_cleaner.py -f my-accounts.json

# جميع الحقول + بدون خلط
python accounts_cleaner.py --all-fields --no-shuffle

# إضافة دومينات محظورة
python accounts_cleaner.py --remove-domain spam.com --remove-domain temp-mail.org

# مع seed للتكرار
python accounts_cleaner.py --seed 42
```

الكود جاهز للتطبيق مباشرة! 🚀


------------------

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
🛠️  Genspark Smart Accounts Cleaner - Refactored V4.0
===============================================================================
Features:
  1. Robust JSON reader with multiple fallbacks (formal JSON → recovery → regex).
  2. Pipeline architecture (load → normalize → filter-blacklist → dedupe → keep
     fields → shuffle → backup → atomic-write) — every stage is pluggable.
  3. Config via dataclass + TOML/JSON config file (optional) + CLI overrides.
  4. Structured logging with levels, colorama auto-detected with safe fallback
     + Windows UTF-8 fix applied before any output.
  5. Safe atomic writes with fsync + timestamped & rotated backups.
  6. Proper email normalization (lower-case, strip, alias support), strong
     regex-based parser tolerant of single quotes, missing commas, etc.
  7. Statistics/Report object returned from pipeline for testing/programmatic use.
  8. Fully typed, modular, unit-testable.
===============================================================================
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import random
import re
import shutil
import sys
import tempfile
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Optional, Set, Tuple

# ---------------------------------------------------------------------------
# Terminal / encoding bootstrap
# ---------------------------------------------------------------------------
def _ensure_utf8_stdout() -> None:
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        if stream is None or not hasattr(stream, "reconfigure"):
            continue
        enc = getattr(stream, "encoding", None)
        if not enc or enc.lower().replace("-", "") != "utf8":
            try:
                stream.reconfigure(encoding="utf-8")
            except Exception:
                pass


_ensure_utf8_stdout()

# ---------------------------------------------------------------------------
# Colors
# ---------------------------------------------------------------------------
try:
    from colorama import Fore, Style, init as _colorama_init  # type: ignore
    _colorama_init(autoreset=True)
    _COLOR = True
except ImportError:  # pragma: no cover
    _COLOR = False

    class _Dummy:
        def __getattr__(self, _name: str) -> str:
            return ""
    Fore = _Dummy()  # type: ignore[assignment]
    Style = _Dummy()  # type: ignore[assignment]


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
class ColorFormatter(logging.Formatter):
    """Minimal ANSI color formatter that works with or without colorama."""

    LEVEL_COLORS = {
        logging.DEBUG:    (Fore.CYAN,   "🔍"),
        logging.INFO:     (Fore.CYAN,   "ℹ️ "),
        logging.WARNING:  (Fore.YELLOW, "⚠️ "),
        logging.ERROR:    (Fore.RED,    "❌"),
        logging.CRITICAL: (Fore.MAGENTA + Style.BRIGHT if _COLOR else "", "💥"),
    }
    SUCCESS = 25  # custom level
    logging.addLevelName(SUCCESS, "SUCCESS")

    def format(self, record: logging.LogRecord) -> str:  # noqa: D401
        color, icon = self.LEVEL_COLORS.get(record.levelno, ("", "•"))
        reset = Style.RESET_ALL if _COLOR else ""
        bright = Style.BRIGHT if _COLOR else ""
        return f"{color}{bright}{icon} {record.getMessage()}{reset}"


def build_logger(verbose: bool = False, quiet: bool = False) -> logging.Logger:
    logger = logging.getLogger("genspark.cleaner")
    logger.handlers.clear()
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(ColorFormatter())
    logger.addHandler(handler)
    if quiet:
        logger.setLevel(logging.ERROR)
    elif verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    def _success(msg: str, *args: Any, **kwargs: Any) -> None:
        logger.log(ColorFormatter.SUCCESS, msg, *args, **kwargs)

    logger.success = _success  # type: ignore[attr-defined]
    return logger


log = build_logger()  # default; rebuilt in main() with CLI flags


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
@dataclass
class CleanerConfig:
    """Central, serializable configuration."""

    target_file: Path = Path("accounts.json")
    email_pass_only: [REDACTED:KV_SECRET] = True
    deduplicate: bool = True
    dedupe_field: str = "email"
    case_insensitive_dedupe: bool = True
    shuffle: bool = True
    shuffle_seed: Optional[int] = None
    make_backup: bool = True
    backup_dir: Optional[Path] = None        # None = next to target
    max_backups: int = 5                     # simple rotation
    blacklisted_domains: Set[str] = field(default_factory=lambda: {"mailnesia.com", "mailnesia"})
    output_file: Optional[Path] = None       # None = overwrite target in-place
    indent: int = 4
    ensure_ascii: bool = False
    min_password_length: int = 0
    email_validation: bool = True
    keep_fields: Tuple[str, ...] = ("email", "password")  # used when email_pass_only=True
    pretty_banner: bool = True

    # ---- helpers --------------------------------------------------------
    def add_domains(self, domains: Iterable[str]) -> None:
        for d in domains:
            d = (d or "").strip().lower()
            if d:
                self.blacklisted_domains.add(d)

    @classmethod
    def from_file(cls, path: Path) -> "CleanerConfig":
        """Load config from a JSON file (TOML can be added easily later)."""
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        cfg = cls()
        for key, val in data.items():
            if not hasattr(cfg, key):
                continue
            if key in ("target_file", "output_file", "backup_dir") and val:
                setattr(cfg, key, Path(val).expanduser())
            elif key == "blacklisted_domains":
                cfg.add_domains(val)
            elif key == "keep_fields":
                cfg.keep_fields = tuple(val)
            else:
                setattr(cfg, key, val)
        return cfg


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------
@dataclass
class CleanReport:
    total_found: int = 0
    invalid_entries: int = 0
    blacklisted: int = 0
    duplicates: int = 0
    invalid_email: int = 0
    short_password: int = 0
    final_count: int = 0
    backup_path: Optional[Path] = None
    output_path: Optional[Path] = None
    elapsed_ms: float = 0.0


# ---------------------------------------------------------------------------
# Parsing / extraction
# ---------------------------------------------------------------------------
_EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
_KV_RE = re.compile(
    r"""['"]?(email|password|provider|mailbox_url|mail|pass|passwd|username|user)['"]?\s*[:=]\s*['"]([^'"]*)['"]""",
    re.IGNORECASE,
)


def _attempt_json_loads(content: str) -> Optional[Any]:
    """Try strict JSON parse; return None on failure."""
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return None


def _attempt_json_recovery(content: str) -> Optional[Any]:
    """Best-effort recovery: strip trailing commas, re-parse."""
    fixed = re.sub(r",\s*([\]}])", r"\1", content)  # trailing commas
    fixed = re.sub(r"^[^{[]*", "", fixed)            # trim garbage before
    fixed = re.sub(r"[^}\]]*$", "", fixed)           # trim garbage after
    try:
        return json.loads(fixed)
    except json.JSONDecodeError:
        return None


def _regex_extract(content: str) -> List[Dict[str, str]]:
    """
    Heuristic regex extractor tolerant of many broken formats:
      - email/pass pairs in JSON-ish, JS object, plain text, CSV-adjacent.
      - supports keys: [REDACTED:KV_SECRET], password|pass|passwd|pw.
    """
    # First pass: [REDACTED:KV_SECRET] pairs in document order.
    entries: List[Dict[str, str]] = []
    current: Dict[str, str] = {}
    last_key: [REDACTED:KV_SECRET] = None
    for m in _KV_RE.finditer(content):
        raw_key, val = m.group(1).lower(), m.group(2).strip()
        if raw_key in ("email", "mail", "username", "user"):
            key = "[REDACTED:KV_SECRET]"
        elif raw_key in ("password", "pass", "passwd", "pw"):
            key = "[REDACTED:KV_SECRET]"
        else:
            key = [REDACTED:KV_SECRET]
        # If we see a new email while we already have one, flush.
        if key == "email" and "email" in current:
            if current.get("email") and current.get("password"):
                entries.append(dict(current))
            current = {}
        current[key] = val
        last_key = key
    if current.get("email") and current.get("password"):
        entries.append(dict(current))

    # Fallback: email/password pairs side-by-side (classical JSON pattern).
    if not entries:
        pair_re = re.compile(
            r"""['"]email['"]?\s*[:=]\s*['"]([^'"]+)['"]\s*[,;]?\s*['"](?:password|pass|passwd)['"]?\s*[:=]\s*['"]([^'"]*)['"]""",
            re.IGNORECASE,
        )
        for em, pw in pair_re.findall(content):
            entries.append({"email": em.strip(), "password": pw.strip()})
    return entries


def _tree_to_accounts(node: Any) -> List[Dict[str, Any]]:
    """Walk a parsed JSON tree and collect account dicts."""
    results: List[Dict[str, Any]] = []
    if isinstance(node, list):
        for item in node:
            results.extend(_tree_to_accounts(item))
    elif isinstance(node, dict):
        # If it looks like an account record itself:
        if any(k in node for k in ("email", "mail", "username", "user", "password", "pass")):
            results.append(node)
        else:
            for key in ("accounts", "data", "items", "list", "result", "users"):
                if key in node:
                    results.extend(_tree_to_accounts(node[key]))
                    break
            else:
                # nested arbitrary dict; dive
                for v in node.values():
                    if isinstance(v, (dict, list)):
                        results.extend(_tree_to_accounts(v))
    return results


def extract_raw_accounts(content: str) -> List[Dict[str, Any]]:
    """Robust extraction pipeline: strict → recovery → regex."""
    if not content.strip():
        return []
    parsed = _attempt_json_loads(content)
    if parsed is None:
        parsed = _attempt_json_recovery(content)
    if parsed is not None:
        return _tree_to_accounts(parsed)
    return _regex_extract(content)


# ---------------------------------------------------------------------------
# Normalization & filtering
# ---------------------------------------------------------------------------
def normalize_email(email: str) -> str:
    e = (email or "").strip().lower()
    # gmail-style "dot" stripping and +alias removal can be made optional later.
    return e


def is_valid_email(email: str) -> bool:
    if not email or "@" not in email:
        return False
    return bool(_EMAIL_RE.fullmatch(email))


def account_email_domain(email: str) -> str:
    if "@" in email:
        return email.split("@", 1)[1].lower()
    return ""


def _field_contains_blacklist(acc: Dict[str, Any], blacklist: Set[str]) -> bool:
    haystacks = [
        str(acc.get("email", "")).lower(),
        str(acc.get("provider", "")).lower(),
        str(acc.get("mailbox_url", "")).lower(),
        str(acc.get("domain", "")).lower(),
    ]
    for hay in haystacks:
        for bl in blacklist:
            if bl in hay:
                return True
    return False


# ---------------------------------------------------------------------------
# Pipeline stages (each pure / easily testable)
# ---------------------------------------------------------------------------
Account = Dict[str, Any]
Stage = Callable[[List[Account], CleanerConfig, CleanReport], List[Account]]


def stage_normalize(accounts: List[Account], cfg: CleanerConfig, rep: CleanReport) -> List[Account]:
    out: List[Account] = []
    for acc in accounts:
        if not isinstance(acc, dict):
            rep.invalid_entries += 1
            continue
        email = str(acc.get("email") or acc.get("mail") or acc.get("username") or acc.get("user") or "").strip()
        password = [REDACTED:KV_SECRET]"password") or acc.get("pass") or acc.get("passwd") or "").strip()
        if not email:
            rep.invalid_entries += 1
            continue
        email = normalize_email(email)
        new_acc: Dict[str, Any] = {"email": email}
        if password:
            new_acc["password"] = password
        # Preserve other possibly useful fields only when not in email/pass-only mode
        if not cfg.email_pass_only:
            for k, v in acc.items():
                if k in new_acc:
                    continue
                new_acc[k] = v
        out.append(new_acc)
    return out


def stage_validate(accounts: List[Account], cfg: CleanerConfig, rep: CleanReport) -> List[Account]:
    out: List[Account] = []
    for acc in accounts:
        email = acc.get("email", "")
        if cfg.email_validation and not is_valid_email(email):
            rep.invalid_email += 1
            continue
        pw = acc.get("password", "")
        if cfg.min_password_length and len(pw) < cfg.min_password_length:
            rep.short_password += 1
            continue
        out.append(acc)
    return out


def stage_blacklist(accounts: List[Account], cfg: CleanerConfig, rep: CleanReport) -> List[Account]:
    out: List[Account] = []
    for acc in accounts:
        if _field_contains_blacklist(acc, cfg.blacklisted_domains):
            rep.blacklisted += 1
            continue
        out.append(acc)
    return out


def stage_dedupe(accounts: List[Account], cfg: CleanerConfig, rep: CleanReport) -> List[Account]:
    if not cfg.deduplicate:
        return accounts
    seen: Set[str] = set()
    out: List[Account] = []
    field_name = cfg.dedupe_field
    for acc in accounts:
        key_raw = [REDACTED:KV_SECRET], "")).strip()
        if not key_raw:
            rep.invalid_entries += 1
            continue
        key = [REDACTED:KV_SECRET] if cfg.case_insensitive_dedupe else key_raw
        if key in seen:
            rep.duplicates += 1
            continue
        seen.add(key)
        out.append(acc)
    return out


def stage_keep_fields(accounts: List[Account], cfg: CleanerConfig, rep: CleanReport) -> List[Account]:
    if not cfg.email_pass_only:
        return accounts
    keep = cfg.keep_fields
    out: List[Account] = []
    for acc in accounts:
        reduced = {k: acc[k] for k in keep if k in acc}
        out.append(reduced)
    return out


def stage_shuffle(accounts: List[Account], cfg: CleanerConfig, rep: CleanReport) -> List[Account]:
    if cfg.shuffle:
        rng = random.Random(cfg.shuffle_seed) if cfg.shuffle_seed is not None else random.SystemRandom()
        rng.shuffle(accounts)
    return accounts


PIPELINE: Tuple[Stage, ...] = (
    stage_normalize,
    stage_validate,
    stage_blacklist,
    stage_dedupe,
    stage_keep_fields,
    stage_shuffle,
)


# ---------------------------------------------------------------------------
# I/O: safe write + backups
# ---------------------------------------------------------------------------
def _rotate_backups(backup_dir: Path, base_name: str, keep: int) -> None:
    if keep <= 0:
        return
    existing = sorted(backup_dir.glob(f"{base_name}.bak.*"))
    while len(existing) >= keep:
        try:
            existing[0].unlink()
        except OSError:
            pass
        existing.pop(0)


def make_backup(src: Path, cfg: CleanerConfig) -> Optional[Path]:
    if not cfg.make_backup:
        return None
    if not src.exists():
        return None
    backup_dir = cfg.backup_dir.expanduser() if cfg.backup_dir else src.parent
    backup_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    base = src.name
    _rotate_backups(backup_dir, base, cfg.max_backups)
    dst = backup_dir / f"{base}.bak.{ts}"
    shutil.copy2(src, dst)
    return dst


def atomic_write_json(target: Path, data: Any, indent: int = 4, ensure_ascii: bool = False) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    # Write temp in same directory for atomic replace on same FS
    fd, tmp_path = tempfile.mkstemp(prefix=target.name + ".", suffix=".tmp", dir=str(target.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=indent, ensure_ascii=ensure_ascii)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp_path, target)
    except Exception:
        # Cleanup temp on failure
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


# ---------------------------------------------------------------------------
# Cleaner engine
# ---------------------------------------------------------------------------
class AccountsCleaner:
    def __init__(self, config: CleanerConfig, logger: Optional[logging.Logger] = None):
        self.config = config
        self.log = logger or build_logger()

    # ---------------- banner ----------------
    def print_banner(self) -> None:
        if not self.config.pretty_banner:
            return
        L = self.log
        L.info("=======================================================")
        L.info("🚀 Genspark Smart Accounts Cleaner V4.0")
        L.info("=======================================================")
        L.info(f"📌 Target file : {self.config.target_file}")
        L.info(f"📌 Output file : {self.config.output_file or '(in-place overwrite)'}")
        L.info(f"📌 Email+Pass  : {self.config.email_pass_only}")
        L.info(f"📌 Deduplicate : {self.config.deduplicate} (field={self.config.dedupe_field})")
        L.info(f"📌 Shuffle     : {self.config.shuffle} (seed={self.config.shuffle_seed})")
        L.info(f"📌 Backup      : {self.config.make_backup} (dir={self.config.backup_dir or next(self.config.target_file.parent).name if False else self.config.target_file.parent}, keep={self.config.max_backups})")
        L.info(f"📌 Blacklist   : {sorted(self.config.blacklisted_domains)}")
        L.info("-------------------------------------------------------")

    # ---------------- load ----------------
    def load(self, path: Path) -> str:
        self.log.info(f"Reading file: {path}")
        with open(path, "r", encoding="utf-8-sig", errors="replace") as fh:
            return fh.read()

    # ---------------- run ----------------
    def run(self) -> CleanReport:
        cfg = self.config
        rep = CleanReport()
        t0 = time.perf_counter()

        target = cfg.target_file.expanduser()
        if not target.exists():
            self.log.error(f"File not found: {target}")
            raise FileNotFoundError(target)

        content = self.load(target)
        raw = extract_raw_accounts(content)
        rep.total_found = len(raw)
        self.log.info(f"Parsed {rep.total_found} raw account entries.")

        accounts = raw
        for stage in PIPELINE:
            accounts = stage(accounts, cfg, rep)
            self.log.debug(f"After {stage.__name__}: {len(accounts)} accounts")

        # Backup before write
        rep.backup_path = make_backup(target, cfg)
        if rep.backup_path:
            self.log.info(f"Backup created: {rep.backup_path}")

        # Write
        out_path = (cfg.output_file or target).expanduser()
        atomic_write_json(out_path, accounts, indent=cfg.indent, ensure_ascii=cfg.ensure_ascii)
        rep.output_path = out_path

        rep.final_count = len(accounts)
        rep.elapsed_ms = (time.perf_counter() - t0) * 1000.0
        self._print_report(rep)
        self.log.success(f"Saved cleaned accounts to: {out_path}")
        return rep

    # ---------------- report ----------------
    def _print_report(self, rep: CleanReport) -> None:
        L = self.log
        L.info("=======================================================")
        L.info("📊 Cleaning report")
        L.info("=======================================================")
        L.info(f"📥 Total found      : {rep.total_found}")
        L.info(f"⚠️  Invalid entries  : {rep.invalid_entries}")
        L.info(f"📧 Invalid emails   : {rep.invalid_email}")
        L.info(f"🔑 Short passwords  : {rep.short_password}")
        L.info(f"🗑️  Blacklisted      : {rep.blacklisted}")
        L.info(f"🔄 Duplicates       : {rep.duplicates}")
        L.info(f"✅ Final unique     : {rep.final_count}")
        L.info(f"⏱️  Elapsed          : {rep.elapsed_ms:.1f} ms")
        L.info("=======================================================")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def _parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="genspark-cleaner",
        description="Genspark smart accounts cleaner / normalizer V4.0",
    )
    p.add_argument("-f", "--file", type=Path, default=None, help="Path to accounts JSON file")
    p.add_argument("-o", "--output", type=Path, default=None, help="Output file (default: in-place)")
    p.add_argument("-c", "--config", type=Path, default=None, help="Optional JSON config file")
    p.add_argument("--all-fields", action="store_true", help="Keep all original fields (don't reduce to email/password)")
    p.add_argument("--no-shuffle", action="store_true", help="Disable shuffle")
    p.add_argument("--shuffle-seed", type=int, default=None, help="Seed for deterministic shuffle")
    p.add_argument("--no-dedupe", action="store_true", help="Disable deduplication")
    p.add_argument("--dedupe-field", type=str, default=None, help="Field to dedupe by (default: email)")
    p.add_argument("--no-backup", action="store_true", help="Disable backup")
    p.add_argument("--backup-dir", type=Path, default=None, help="Backup directory (default: next to target)")
    p.add_argument("--max-backups", type=int, default=None, help="Number of rotating backups to keep")
    p.add_argument("--remove-domain", action="append", default=None, help="Blacklist additional domain(s); repeatable")
    p.add_argument("--min-pass-len", type=int, default=None, help="Drop accounts with password shorter than N")
    p.add_argument("--no-email-check", action="store_true", help="Disable email-format validation")
    p.add_argument("-v", "--verbose", action="store_true", help="Verbose logging")
    p.add_argument("-q", "--quiet", action="store_true", help="Errors only")
    p.add_argument("--no-banner", action="store_true", help="Suppress banner")
    return p.parse_args(argv)


def _apply_cli_overrides(cfg: CleanerConfig, args: argparse.Namespace) -> CleanerConfig:
    if args.file:
        cfg.target_file = args.file
    if args.output:
        cfg.output_file = args.output
    if args.all_fields:
        cfg.email_pass_only = False
    if args.no_shuffle:
        cfg.shuffle = False
    if args.shuffle_seed is not None:
        cfg.shuffle_seed = args.shuffle_seed
        cfg.shuffle = True
    if args.no_dedupe:
        cfg.deduplicate = False
    if args.dedupe_field:
        cfg.dedupe_field = args.dedupe_field
    if args.no_backup:
        cfg.make_backup = False
    if args.backup_dir:
        cfg.backup_dir = args.backup_dir
    if args.max_backups is not None:
        cfg.max_backups = args.max_backups
    if args.remove_domain:
        cfg.add_domains(args.remove_domain)
    if args.min_pass_len is not None:
        cfg.min_password_length = [REDACTED:KV_SECRET]
    if args.no_email_check:
        cfg.email_validation = False
    if args.no_banner:
        cfg.pretty_banner = False

    # Resolve target file relative to CWD if it's the default and file exists in CWD
    if cfg.target_file == Path("accounts.json"):
        cwd_candidate = Path.cwd() / "accounts.json"
        if cwd_candidate.exists():
            cfg.target_file = cwd_candidate
    return cfg


def main(argv: Optional[List[str]] = None) -> int:
    global log
    args = _parse_args(argv)
    log = build_logger(verbose=args.verbose, quiet=args.quiet)

    # Config: defaults -> file -> CLI
    cfg = CleanerConfig()
    if args.config:
        try:
            cfg = CleanerConfig.from_file(args.config.expanduser())
        except Exception as e:
            log.error(f"Failed to load config {args.config}: {e}")
            return 2
    cfg = _apply_cli_overrides(cfg, args)

    cleaner = AccountsCleaner(cfg, logger=log)
    try:
        cleaner.print_banner()
        cleaner.run()
        return 0
    except FileNotFoundError as e:
        log.error(f"Input file missing: {e}")
        return 1
    except Exception as e:  # pragma: no cover
        log.critical(f"Fatal error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())


-------------------------------------


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Original script (kept for reference / before-state).
"""

import json
import re
import os
import sys
import shutil
import random
import argparse
from dataclasses import dataclass, field
from typing import List, Dict, Any, Set


# ─── Terminal encoding handling for Windows ──────────────────────────────────
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


# ─── Color support via colorama with safe fallback ───────────────────────────
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    class EmptyColor:
        CYAN = GREEN = YELLOW = RED = MAGENTA = WHITE = ""
    class EmptyStyle:
        BRIGHT = RESET_ALL = ""
    Fore = EmptyColor()
    Style = EmptyStyle()


def log_info(msg: str):
    print(f"{Fore.CYAN}ℹ️  {msg}{Style.RESET_ALL}")


def log_success(msg: str):
    print(f"{Fore.GREEN}✅ {msg}{Style.RESET_ALL}")


def log_warn(msg: str):
    print(f"{Fore.YELLOW}⚠️  {msg}{Style.RESET_ALL}")


def log_error(msg: str):
    print(f"{Fore.RED}❌ {msg}{Style.RESET_ALL}")


# ─── ⚙️ Smart Config Manager ──────────────────────────────────────────────
@dataclass
class AccountsConfig:
    target_file: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts-example.json")
    email_pass_only: [REDACTED:KV_SECRET] = True
    deduplicate: bool = True
    shuffle: bool = True
    make_backup: bool = True
    blacklisted_domains: List[str] = field(default_factory=lambda: ["mailnesia.com", "mailnesia"])

    def print_banner(self):
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.CYAN}{Style.BRIGHT}🚀 Smart Accounts Cleaner V3.0{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 Target file: {Fore.YELLOW}{self.target_file}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 Email/pass only: {Fore.GREEN if self.email_pass_only else Fore.RED}{self.email_pass_only}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 Deduplicate: {Fore.GREEN if self.deduplicate else Fore.RED}{self.deduplicate}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 Shuffle: {Fore.GREEN if self.shuffle else Fore.RED}{self.shuffle}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 Blacklisted domains: {Fore.RED}{self.blacklisted_domains}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}-------------------------------------------------------{Style.RESET_ALL}\n")


# ─── 🔍 Cleaning Engine ────────────────────────────────────────────────────
class AccountsCleaner:
    def __init__(self, config: AccountsConfig):
        self.config = config

    def extract_raw_accounts(self, content: str) -> List[Dict[str, Any]]:
        accounts = []
        try:
            parsed = json.loads(content)
            if isinstance(parsed, list):
                accounts = parsed
            elif isinstance(parsed, dict):
                accounts = parsed.get("accounts", parsed.get("data", []))
        except Exception:
            log_warn("Broken/nested JSON, falling back to smart regex extraction...")

        if not accounts:
            pattern = re.compile(r'"email"\s*:\s*"([^"]+)",\s*"password"\s*:\s*"([^"]+)"')
            for email, password in pattern.findall(content):
                accounts.append({"email": email.strip(), "password": password.strip()})
        return accounts

    def is_blacklisted(self, email: str, account_dict: Dict[str, Any]) -> bool:
        email_lower = email.lower()
        provider_lower = str(account_dict.get("provider", "")).lower()
        url_lower = str(account_dict.get("mailbox_url", "")).lower()
        for domain in self.config.blacklisted_domains:
            d = domain.lower()
            if d in email_lower or d in provider_lower or d in url_lower:
                return True
        return False

    def process(self):
        file_path = self.config.target_file
        if not os.path.exists(file_path):
            log_error(f"File not found: {file_path}")
            return False

        log_info(f"Reading file: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()

        raw_list = self.extract_raw_accounts(content)
        total_found = len(raw_list)
        log_info(f"Found {total_found} account entries.")

        cleaned = []
        seen: Set[str] = set()
        blacklisted = 0
        duplicates = 0

        for acc in raw_list:
            if not isinstance(acc, dict):
                continue
            email = str(acc.get("email", "")).strip()
            password = [REDACTED:KV_SECRET]"password", "")).strip()
            if not email:
                continue
            if self.is_blacklisted(email, acc):
                blacklisted += 1
                continue
            key = [REDACTED:KV_SECRET]
            if self.config.deduplicate and key in seen:
                duplicates += 1
                continue
            seen.add(key)
            item = {"email": email, "password": password} if self.config.email_pass_only else acc
            cleaned.append(item)

        if self.config.shuffle:
            random.seed()
            random.shuffle(cleaned)
            log_info("Shuffled accounts randomly.")

        if self.config.make_backup:
            backup_path = file_path + ".bak"
            shutil.copy2(file_path, backup_path)
            log_info(f"Backup saved at: {backup_path}")

        tmp_path = file_path + ".tmp"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(cleaned, f, indent=4, ensure_ascii=False)
        os.replace(tmp_path, file_path)

        print(f"\n{Fore.GREEN}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.GREEN}{Style.BRIGHT}✨ Done! File cleaned and saved successfully.{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.WHITE}📊 Total processed: {Fore.YELLOW}{total_found}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}🗑️  Blacklisted removed: {Fore.RED}{blacklisted}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}🔄 Duplicates removed: {Fore.YELLOW}{duplicates}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}✅ Final valid unique: {Fore.GREEN}{Style.BRIGHT}{len(cleaned)}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}=======================================================\n{Style.RESET_ALL}")
        return True


def main():
    config = AccountsConfig()
    parser = argparse.ArgumentParser(description="Smart Genspark accounts cleaner")
    parser.add_argument("-f", "--file", type=str, default=config.target_file)
    parser.add_argument("--all-fields", action="store_true")
    parser.add_argument("--no-shuffle", action="store_true")
    parser.add_argument("--no-dedupe", action="store_true")
    parser.add_argument("--no-backup", action="store_true")
    parser.add_argument("--remove-domain", type=str, action="append")
    args = parser.parse_args()

    config.target_file = args.file
    if args.all_fields:
        config.email_pass_only = False
    if args.no_shuffle:
        config.shuffle = False
    if args.no_dedupe:
        config.deduplicate = False
    if args.no_backup:
        config.make_backup = False
    if args.remove_domain:
        config.blacklisted_domains.extend(args.remove_domain)

    config.print_banner()
    cleaner = AccountsCleaner(config)
    cleaner.process()


if __name__ == "__main__":
    main()


------------------------------------------


🧭 خطة تطوير وتنفيذ — منظف حسابات Genspark (من V3 إلى V4)
الهدف: تحويل السكربت الحالي من سكربت "ماشي حاله" إلى محرك تنظيف ببلاين مرن، قابل للتوسع، سلس الصيانة، متوافق عبر الأنظمة، وقابل للاختبار — مع الحفاظ على نفس الوظائف التي يقدمها حالياً (قراءة JSON المكسور، توحيد، حذف دومينات محظورة، حذف التكرارات، خلط، نسخة احتياطية، كتابة ذرية، طباعة ملونة).

1. تشخيص مشاكل السكربت الحالي (قبل التعديل)
#	المشكلة	مكان السبب	التأثير
1	بنية متجانسة (Monolithic) — كل المنطق داخل دالة process() وكلاسات كبيرة	AccountsCleaner.process	صعوبة الإضافة/الاختبار
2	تكرار كود الألوان/اللوج ووجود روابط Markdown داخل f-strings بالخطأ مثل {[Fore.GREEN](http://Fore.GREEN)}	log_* وprint_banner	كسر الـ syntax لو نُسخ الكود + مظهر مكسور في التيرمينال
3	الـ Regex بسيط جداً — يفشل لو الإيميل/الباس وُجدت بعلامات مفردة، أو ترتيب معكوس، أو بمسافات، أو keys بديلة (user/pass/mail/username)	extract_raw_accounts	فقدان حسابات / قراءة ناقصة
4	لا توجد طباعة تطبيع (normalize) — الإيميلات تظل بحالات مختلفة، المسافات تسبب تكرارات غير مكتشفة	loop inside process	نتائج dedupe غير دقيقة
5	كتابة ذرية ناقصة — لا يوجد fsync، ولا يتم تنظيف الملف المؤقت عند الفشل	atomic write section	خطر تلف الملف في حال انقطاع العملية
6	النسخ الاحتياطي ينشئ ملف .bak واحد فقط ويدمر السابق بلا تدوير	shutil.copy2(file_path, backup_path)	ضياع نسخ قديمة / صعوبة التراجع
7	الإعدادات صلبة — لا توجد وسيلة لتحميل config من ملف (JSON/TOML) وبعض الخيارات غير موجودة (min password length, email validation, seed للـ shuffle)	AccountsConfig + main()	ضعف المرونة والتوسع
8	Banner مدمج داخل Config — فصل اهتمامات سيئ (Config لا يجب أن يطبع)	AccountsConfig.print_banner()	تصميم غير نظيف
9	لا توجد كائن تقرير (Report) — النتائج تُطبع فقط ولا تُرجع بشكل برمجي	process()	لا يمكن استدعاء السكربت من كود آخر أو اختباره بسهولة
10	الاستثناءات تُبلع بـ except Exception: pass وexcept Exception: عامة	متعددة	إخفاء أخطاء حقيقية
11	دعم ويندوز جزئي فقط — لا معالجة لـ stderr، ولا utf-8-sig لملفات UTF-8 BOM	أعلى الملف	مشاكل في ويندوز
12	CLI محدود — لا يوجد -o, -c, -v/-q, --dedupe-field, --min-pass-len, إلخ	argparse	قابلية استخدام ضعيفة
13	لا توجد طبقات (layers) — Logging / Config / Parsing / Pipeline / IO جميعها مختلطة	الملف ككل	صعوبة إضافة مزايا
14	دوال متغيرة الطباعة ثابتة لا يمكن تغيير مستوى الإسهاب بسهولة	log_*	تجربة استخدام سيئة
15	عدم دعم ملفات الإخراج المنفصلة (يُجبر على الكتابة فوق الملف الأصلي)	process()	خطر على البيانات الأصلية
2. الرؤية بعد التطوير (V4.0) — المبادئ المعمارية
Pipeline / Stages نقية: كل مرحلة (normalize → validate → blacklist → dedupe → keep-fields → shuffle) هي دالة مستقلة تأخذ قائمة وتُرجع قائمة وتحدّث كائن التقرير.
انفصال المسؤوليات (Separation of Concerns):
Config لإدارة الإعدادات فقط.
Logging موحد وملوّن وقابل لضبط المستوى.
Parser/Extractor قوي مع 3 مستويات fallback.
Pipeline stages قابلة للاختبار.
IO layer للنسخ الاحتياطي والكتابة الذرية الآمنة.
قابلية التوسع: إضافة مرحلة جديدة (مثل stage_rate_limit_check) لا تتطلب إلا إضافة دالة وإدراجها في تابل PIPELINE.
التوافق: يعمل على لينكس/ماك/ويندوز، مع معالجة الـ BOM، إعادة تكوين الترميز، ولون اختياري.
البرمجية/الاختبارية: يمكن استيراد AccountsCleaner واستدعاء run() من سكربتات أخرى والحصول على CleanReport.
التسامح مع الأخطاء: استثناءات واضحة، رسائل مفيدة، وتنظيف الموارد.
3. خطة تنفيذ مقترحة (مقسمة على مراحل)
المرحلة 0 — الاحتياطات والهيكلية
 حفظ نسخة من السكربت الأصلي (
original_original.py
).
 إنشاء ملف جديد
cleaner.py
 بدلاً من التعديل المباشر على القديم.
 إضافة README.md + config.example.json لاحقاً (اختياري).
المرحلة 1 — البنية التحتية
ترميز آمن: _ensure_utf8_stdout() لـ stdout وstderr قبل أي طباعة.
ألوان آمنة: fallback كامل بدون استثناءات مبعثرة.
Logging موحد: استخدام logging القياسي مع ColorFormatter + مستوى SUCCESS مخصص + دعم -v/-q.
pathlib.Path في كامل التعامل مع الملفات بدلاً من os.path (أكثر وضوحاً وأقل أخطاء).
المرحلة 2 — الإعدادات (Config)
نقل الإعدادات إلى @dataclass CleanerConfig مع:
output_file للكتابة في ملف مختلف.
dedupe_field, case_insensitive_dedupe.
shuffle_seed, backup_dir, max_backups, indent, ensure_ascii.
min_password_length, email_validation, keep_fields.
إضافة CleanerConfig.from_file(path) لتحميل إعدادات من ملف JSON.
CLI يقوم بالترتيب: defaults → config file → CLI flags ويعرضها في Banner.
المرحلة 3 — الاستخراج القوي (Extractor)
سلسلة fallback من ثلاث طبقات:

json.loads الرسمي.
_attempt_json_recovery: إزالة trailing commas والقص خارج الأقواس وإعادة المحاولة.
_regex_extract: regex متسامح مع ' و"، مع مفاتيح بديلة (email/mail/username/user، password/pass/passwd/pw)، ويدعم إعادة بناء الكائنات من تتابع الأزواج.
_tree_to_accounts: ينزل في الشجرة (dict/list) ليجمع الحسابات مهما كان عمق التداخل، ويبحث عن مفاتيح شائعة (accounts, data, items, users, …).
المرحلة 4 — Pipeline (القلب)
تعريف Stage = Callable[[List[Account], CleanerConfig, CleanReport], List[Account]] ثم المراحل:

stage_normalize — استخراج email/password من مفاتيح متعددة، lower(), strip().
stage_validate — فحص صيغة الإيميل + طول كلمة المرور.
stage_blacklist — فحص email, provider, mailbox_url, domain.
stage_dedupe — حسب حقل قابل للتكوين، case-insensitive افتراضياً.
stage_keep_fields — يحتفظ فقط بالحقول المطلوبة عند تشغيل email_pass_only.
stage_shuffle — خلط بـ random.Random(seed) أو SystemRandom لعدم التكرار.
هذا هو أهم تحسين معياري لأنه يجعل إضافة/إزالة/إعادة ترتيب المراحل مسألة سطر واحد في PIPELINE.

المرحلة 5 — IO آمن
make_backup يُنشئ نسخة باسم file.json.bak.YYYYMMDD-HHMMSS، مع backup_dir اختياري، ويدور القديم (max_backups).
atomic_write_json يكتب في ملف مؤقت داخل نفس المجلد، يعمل flush + fsync، ثم os.replace، ويزيل المؤقت عند الفشل.
المرحلة 6 — المحرك + التقرير
كلاس AccountsCleaner(config, logger) يُعيد CleanReport (بيانات برمجية) بالإضافة إلى الطباعة.
فصل print_banner() خارج Config إلى المحرك.
دالة main() ترجع exit code (0/1/2) ويتم استدعاؤها عبر sys.exit(main()).
المرحلة 7 — CLI موسّع
إضافة الخيارات الجديدة:

-o/--output, -c/--config, -v/--verbose, -q/--quiet, --no-banner.
--no-dedupe, --dedupe-field, --no-shuffle, --shuffle-seed.
--no-backup, --backup-dir, --max-backups.
--remove-domain (موجود، مُحسَّن لإزالة التكرار في القائمة).
--min-pass-len, --no-email-check.
4. أمثلة "قبل / بعد" لتنفيذ التعديلات مباشرة في محرر الأكواد
📌 كل مقطع أدناه يُظهر الكود كما هو في النسخة الحالية (قبل) ثم الكود المُعاد تصميمه (بعد) حتى تتمكن من تطبيق التعديل تباعاً في محررك.

🔧 التعديل 1 — إصلاح خطأ الـ f-string المكسور + دعم ترميز قوي (أعلى الملف)
قبل:

Python

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    class EmptyColor:
        CYAN = GREEN = YELLOW = RED = MAGENTA = WHITE = ""
    class EmptyStyle:
        BRIGHT = RESET_ALL = ""
    Fore = EmptyColor()
    Style = EmptyStyle()

def log_info(msg: str):
    print(f"{Fore.CYAN}ℹ️  {msg}{Style.RESET_ALL}")
def log_success(msg: str):
    print(f"{[Fore.GREEN](http://Fore.GREEN)}✅ {msg}{Style.RESET_ALL}")
def log_warn(msg: str):
    print(f"{Fore.YELLOW}⚠️  {msg}{Style.RESET_ALL}")
def log_error(msg: str):
    print(f"{[Fore.RED](http://Fore.RED)}❌ {msg}{Style.RESET_ALL}")
بعد:

Python

def _ensure_utf8_stdout() -> None:
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        if stream is None or not hasattr(stream, "reconfigure"):
            continue
        enc = getattr(stream, "encoding", None)
        if not enc or enc.lower().replace("-", "") != "utf8":
            try:
                stream.reconfigure(encoding="utf-8")
            except Exception:
                pass

_ensure_utf8_stdout()

try:
    from colorama import Fore, Style, init as _colorama_init
    _colorama_init(autoreset=True)
    _COLOR = True
except ImportError:
    _COLOR = False
    class _Dummy:
        def __getattr__(self, _name: str) -> str:
            return ""
    Fore = _Dummy()
    Style = _Dummy()

import logging

class ColorFormatter(logging.Formatter):
    LEVEL_COLORS = {
        logging.DEBUG:    (Fore.CYAN,   "🔍"),
        logging.INFO:     (Fore.CYAN,   "ℹ️ "),
        logging.WARNING:  (Fore.YELLOW, "⚠️ "),
        logging.ERROR:    (Fore.RED,    "❌"),
        logging.CRITICAL: (Fore.MAGENTA + (Style.BRIGHT if _COLOR else ""), "💥"),
    }
    SUCCESS = 25
    logging.addLevelName(SUCCESS, "SUCCESS")

    def format(self, record):
        color, icon = self.LEVEL_COLORS.get(record.levelno, ("", "•"))
        reset = Style.RESET_ALL if _COLOR else ""
        bright = Style.BRIGHT if _COLOR else ""
        return f"{color}{bright}{icon} {record.getMessage()}{reset}"

def build_logger(verbose=False, quiet=False):
    logger = logging.getLogger("genspark.cleaner")
    logger.handlers.clear()
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(ColorFormatter())
    logger.addHandler(h)
    logger.setLevel(logging.ERROR if quiet else (logging.DEBUG if verbose else logging.INFO))
    def _success(msg, *a, **kw): logger.log(ColorFormatter.SUCCESS, msg, *a, **kw)
    logger.success = _success
    return logger

log = build_logger()
🔧 التعديل 2 — فصل الـ Config عن الـ Banner + إضافة خيارات جديدة
قبل:

Python

@dataclass
class AccountsConfig:
    target_file: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts-example.json")
    email_pass_only: [REDACTED:KV_SECRET] = True
    deduplicate: bool = True
    shuffle: bool = True
    make_backup: bool = True
    blacklisted_domains: List[str] = field(default_factory=lambda: ["mailnesia.com", "mailnesia"])

    def print_banner(self):
        ...
بعد:

Python

from pathlib import Path

@dataclass
class CleanerConfig:
    target_file: Path = Path("accounts.json")
    output_file: Optional[Path] = None
    email_pass_only: [REDACTED:KV_SECRET] = True
    deduplicate: bool = True
    dedupe_field: str = "email"
    case_insensitive_dedupe: bool = True
    shuffle: bool = True
    shuffle_seed: Optional[int] = None
    make_backup: bool = True
    backup_dir: Optional[Path] = None
    max_backups: int = 5
    blacklisted_domains: Set[str] = field(default_factory=lambda: {"mailnesia.com", "mailnesia"})
    indent: int = 4
    ensure_ascii: bool = False
    min_password_length: int = 0
    email_validation: bool = True
    keep_fields: Tuple[str, ...] = ("email", "password")
    pretty_banner: bool = True

    def add_domains(self, domains):
        for d in domains:
            d = (d or "").strip().lower()
            if d:
                self.blacklisted_domains.add(d)
✅ ملاحظة: البانر بقي داخل AccountsCleaner.print_banner() وليس داخل Config (فصل اهتمامات).

🔧 التعديل 3 — استخراج قوي للـ JSON المكسور (Extractor)
قبل:

Python

def extract_raw_accounts(self, content: str) -> List[Dict[str, Any]]:
    accounts = []
    try:
        parsed = json.loads(content)
        if isinstance(parsed, list):
            accounts = parsed
        elif isinstance(parsed, dict):
            accounts = parsed.get("accounts", parsed.get("data", []))
    except Exception:
        log_warn("الملف يحتوي على تداخل أو صيغة JSON مكسورة...")

    if not accounts:
        pattern = re.compile(r'"email"\s*:\s*"([^"]+)",\s*"password"\s*:\s*"([^"]+)"')
        matches = pattern.findall(content)
        for email, password in matches:
            accounts.append({"email": email.strip(), "password": password.strip()})
    return accounts
بعد:

Python

_KV_RE = re.compile(
    r"""['"]?(email|password|provider|mailbox_url|mail|pass|passwd|username|user)['"]?\s*[:=]\s*['"]([^'"]*)['"]""",
    re.IGNORECASE,
)

def _attempt_json_loads(content):
    try: return json.loads(content)
    except json.JSONDecodeError: return None

def _attempt_json_recovery(content):
    fixed = re.sub(r",\s*([\]}])", r"\1", content)
    fixed = re.sub(r"^[^{[]*", "", fixed)
    fixed = re.sub(r"[^}\]]*$", "", fixed)
    try: return json.loads(fixed)
    except json.JSONDecodeError: return None

def _regex_extract(content):
    entries, current = [], {}
    for m in _KV_RE.finditer(content):
        key, val = m.group(1).lower(), m.group(2).strip()
        key = "[REDACTED:KV_SECRET]" if key in ("email","mail","username","user") else (
              "password" if key in ("password","pass","passwd","pw") else key)
        if key == "email" and "email" in current:
            if current.get("email") and current.get("password"):
                entries.append(dict(current))
            current = {}
        current[key] = val
    if current.get("email") and current.get("password"):
        entries.append(dict(current))
    return entries

def _tree_to_accounts(node):
    results = []
    if isinstance(node, list):
        for it in node: results.extend(_tree_to_accounts(it))
    elif isinstance(node, dict):
        if any(k in node for k in ("email","mail","username","user","password","pass")):
            results.append(node)
        else:
            for k in ("accounts","data","items","list","result","users"):
                if k in node:
                    results.extend(_tree_to_accounts(node[k])); break
            else:
                for v in node.values():
                    if isinstance(v, (dict, list)): results.extend(_tree_to_accounts(v))
    return results

def extract_raw_accounts(content):
    if not content.strip(): return []
    parsed = _attempt_json_loads(content) or _attempt_json_recovery(content)
    if parsed is not None:
        return _tree_to_accounts(parsed)
    return _regex_extract(content)
🔧 التعديل 4 — استبدال الحلقة المتجانسة بـ Pipeline من مراحل
قبل:

Python

cleaned_accounts = []
seen_emails: Set[str] = set()
blacklisted_count = 0
duplicate_count = 0

for acc in raw_list:
    if not isinstance(acc, dict): continue
    email = str(acc.get("email", "")).strip()
    password = [REDACTED:KV_SECRET]"password", "")).strip()
    if not email: continue
    if self.is_blacklisted(email, acc):
        blacklisted_count += 1; continue
    email_key = [REDACTED:KV_SECRET]
    if self.config.deduplicate:
        if email_key in seen_emails:
            duplicate_count += 1; continue
        seen_emails.add(email_key)
    item = {"email": email, "password": password} if self.config.email_pass_only else acc
    cleaned_accounts.append(item)
بعد:

Python

PIPELINE = (
    stage_normalize,
    stage_validate,
    stage_blacklist,
    stage_dedupe,
    stage_keep_fields,
    stage_shuffle,
)

accounts = raw_list
for stage in PIPELINE:
    accounts = stage(accounts, cfg, rep)
    log.debug(f"After {stage.__name__}: {len(accounts)} accounts")
كل مرحلة دالة منفصلة تأخذ (accounts, config, report) وتُرجع القائمة الجديدة — مثال على واحدة:

Python

def stage_dedupe(accounts, cfg: CleanerConfig, rep: CleanReport):
    if not cfg.deduplicate: return accounts
    seen, out = set(), []
    for acc in accounts:
        key = [REDACTED:KV_SECRET], "")).strip()
        if not key:
            rep.invalid_entries += 1; continue
        if cfg.case_insensitive_dedupe:
            key = [REDACTED:KV_SECRET]
        if key in seen:
            rep.duplicates += 1; continue
        seen.add(key); out.append(acc)
    return out
🔧 التعديل 5 — نسخ احتياطي دائري + كتابة ذرية آمنة مع fsync
قبل:

Python

if self.config.make_backup:
    backup_path = file_path + ".bak"
    shutil.copy2(file_path, backup_path)
    log_info(f"تم إنشاء نسخة احتياطية آمنة في: {backup_path}")

tmp_path = file_path + ".tmp"
with open(tmp_path, "w", encoding="utf-8") as f:
    json.dump(cleaned_accounts, f, indent=4, ensure_ascii=False)
os.replace(tmp_path, file_path)
بعد:

Python

import tempfile, time
from datetime import datetime

def make_backup(src: Path, cfg: CleanerConfig) -> Optional[Path]:
    if not cfg.make_backup or not src.exists():
        return None
    backup_dir = (cfg.backup_dir or src.parent).expanduser()
    backup_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    # تدوير: حذف الأقدم عند تجاوز الحد
    existing = sorted(backup_dir.glob(f"{src.name}.bak.*"))
    while len(existing) >= cfg.max_backups:
        try: existing[0].unlink()
        except OSError: pass
        existing.pop(0)
    dst = backup_dir / f"{src.name}.bak.{ts}"
    shutil.copy2(src, dst)
    return dst

def atomic_write_json(target: Path, data, indent=4, ensure_ascii=False):
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(prefix=target.name + ".", suffix=".tmp", dir=str(target.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=indent, ensure_ascii=ensure_ascii)
            fh.flush(); os.fsync(fh.fileno())
        os.replace(tmp_path, target)
    except Exception:
        try: os.unlink(tmp_path)
        except OSError: pass
        raise
🔧 التعديل 6 — التقرير المُرجَع (Programmatic Report) + رسائل خروج نظيفة
قبل:

Python

# الطباعة فقط، لا يوجد كائن ناتج
print(...); return True
بعد:

Python

@dataclass
class CleanReport:
    total_found: int = 0
    invalid_entries: int = 0
    blacklisted: int = 0
    duplicates: int = 0
    invalid_email: int = 0
    short_password: int = 0
    final_count: int = 0
    backup_path: Optional[Path] = None
    output_path: Optional[Path] = None
    elapsed_ms: float = 0.0
ويُرجع من:

Python

def run(self) -> CleanReport:
    rep = CleanReport()
    t0 = time.perf_counter()
    # ... (load → pipeline → backup → atomic write) ...
    rep.final_count = len(accounts)
    rep.elapsed_ms = (time.perf_counter() - t0) * 1000.0
    self._print_report(rep)
    return rep
🔧 التعديل 7 — CLI موسّع (مطابق لخطة التوسع)
قبل:

Python

parser.add_argument("-f", "--file", ...)
parser.add_argument("--all-fields", ...)
parser.add_argument("--no-shuffle", ...)
parser.add_argument("--no-dedupe", ...)
parser.add_argument("--no-backup", ...)
parser.add_argument("--remove-domain", ...)
بعد:

Python

p.add_argument("-f", "--file", type=Path, default=None)
p.add_argument("-o", "--output", type=Path, default=None)
p.add_argument("-c", "--config", type=Path, default=None)
p.add_argument("--all-fields", action="store_true")
p.add_argument("--no-shuffle", action="store_true")
p.add_argument("--shuffle-seed", type=int, default=None)
p.add_argument("--no-dedupe", action="store_true")
p.add_argument("--dedupe-field", type=str, default=None)
p.add_argument("--no-backup", action="store_true")
p.add_argument("--backup-dir", type=Path, default=None)
p.add_argument("--max-backups", type=int, default=None)
p.add_argument("--remove-domain", action="append", default=None)
p.add_argument("--min-pass-len", type=int, default=None)
p.add_argument("--no-email-check", action="store_true")
p.add_argument("-v", "--verbose", action="store_true")
p.add_argument("-q", "--quiet", action="store_true")
p.add_argument("--no-banner", action="store_true")
مع ترتيب تطبيق:

Python

# defaults -> config file -> CLI
cfg = CleanerConfig()
if args.config:
    cfg = CleanerConfig.from_file(args.config.expanduser())
cfg = _apply_cli_overrides(cfg, args)
5. نتائج متوقعة بعد التطوير
🚀 مرونة عالية: كل مرحلة مستقلة، يمكن تعطيلها أو استبدالها أو إضافة مراحل جديدة بسهولة.
🧩 قابلية التوسع: يمكن إضافة ميزات مثل التحقق من صلاحية الحساب (rate limit test) أو استيراد من CSV/TXT ببساطة.
🛡️ أمان أعلى: كتابة ذرية حقيقية مع fsync + نسخ احتياطية مدوّرة بطابع زمني.
🪟 توافق محسّن مع ويندوز/ماك/لينكس ومع ملفات UTF-8 BOM.
🧪 سهولة الاختبار: AccountsCleaner.run() يُرجع CleanReport؛ وكل stage دالة نقية.
🧰 CLI احترافي مع دعم config file، مستويات إسهاب، ومسارات مخصصة.
🧹 كود أنظف: إزالة التكرار، إزالة الـ f-strings المكسورة، فصل اهتمامات واضح.
6. خطوات مقترحة للتطبيق في محرر الأكواد
انسخ الملف الأصلي إلى
original_original.py
 احتياطياً.
أنشئ ملف جديد باسم
cleaner.py
 والصق بداخله النسخة V4 المرفقة (
cleaner.py
).
اختبار سريع:
Bash

python cleaner.py -f accounts-example.json --no-backup -v
اختبار خيارات إضافية:
Bash

python cleaner.py -f accounts.json -o cleaned.json --remove-domain example.com --shuffle-seed 42
(اختياري) أنشئ config.example.json:
JSON

{
  "target_file": "accounts.json",
  "email_pass_only": true,
  "deduplicate": true,
  "shuffle": true,
  "make_backup": true,
  "max_backups": 10,
  "blacklisted_domains": ["mailnesia.com", "throwaway.tld"],
  "min_password_length": 4,
  "email_validation": true
}
(اختياري لاحقاً) أضف pytest tests لكل stage.
7. قائمة التحقق (Checklist) النهائية
 إزالة جميع الـ f-strangs المكسورة {[Fore.*](http://...)}.
 استخدام pathlib.Path بدلاً من os.path.
 استبدال log_* المنفصلة بـ logging موحد.
 فصل البانر خارج Config.
 استبدال الحلقة الكبيرة في process() بالـ pipeline.
 استخدام atomic_write_json مع fsync.
 نسخ احتياطية مدوّرة بطابع زمني.
 إرجاع CleanReport من run().
 CLI موسّع مع -o/-c/-v/-q.
 sys.exit(main()) مع أكواد خروج.
تم تجهيز النسخة المُعاد بناؤها بالكامل في الملف
cleaner.py
، ويمكن اعتمادها مباشرة كبديل عن السكربت الحالي مع الحفاظ على النسخة الأصلية في
original_original.py
 للمراجعة.


-------------
# خطة تنفيذية شاملة لإعادة هيكلة السكربت

## 📋 تحليل المشاكل الحالية

| # | المشكلة | التأثير |
|---|---------|---------|
| 1 | **Mixin للـ Logging** عبر 4 دوال منفصلة (`log_info`, `log_success`, `log_warn`, `log_error`) | تكرار وقابلية توسع ضعيفة |
| 2 | **Hard-coded** لمسار الملف داخل `Config` | غير مرن، يخالف مبدأ SRP |
| 3 | **سلسلة الـ if/elif** في `extract_raw_accounts` | تكرار منطق، قابلية اختبار ضعيفة |
| 4 | **عدم فصل الـ I/O** عن منطق التنظيف | صعوبة الاختبار والصيانة |
| 5 | **Color coupling** داخل منطق `process()` | خلط المسؤوليات |
| 6 | **`extract_raw_accounts`** يرجع `accounts` متغير global قد يتلوث | bug محتمل |
| 7 | **لا يوجد progress indicator** للملفات الكبيرة | UX سيئ |
| 8 | **الـ Blacklist** مخزنة كـ string فقط بدون email validation | سهل التهرب |
| 9 | **لا يوجد `__repr__` أو `__str__`** في الـ dataclasses | debugging صعب |
| 10 | **لا يوجد `dry-run` mode** | مخاطرة عالية بدون معاينة |

---

## 🎯 خطة التحسين المقترحة (Roadmap)

### المرحلة 1: إعادة الهيكلة المعمارية (Architecture Refactor)
- تطبيق **Strategy Pattern** لمحركات الاستخراج (JSON parser, Regex parser, Line parser)
- فصل الطبقات إلى modules:
  - `config.py` → الإعدادات
  - `extractors/` → استراتيجيات الاستخراج
  - `filters/` → استراتيجيات التصفية
  - `reporter.py` → التقارير
  - `logger.py` → نظام السجلات
  - `core.py` → المحرك الرئيسي

### المرحلة 2: SOLID Principles
- **S** (Single Responsibility): كل class له وظيفة واحدة
- **O** (Open/Closed): إضافة مستخرجات جديدة بدون تعديل الكود الحالي
- **L** (Liskov Substitution): واجهات موحدة
- **I** (Interface Segregation): فصل الواجهات الكبيرة
- **D** (Dependency Inversion): الاعتماد على Abstractions

### المرحلة 3: ميزات جديدة
- ✅ `dry-run` mode للمعاينة
- ✅ `progress bar` للملفات الضخمة
- ✅ `pipeline` قابل للتخصيص (chain of responsibility)
- ✅ دعم صيغ إدخال متعددة (JSON, JSONL, CSV, TXT)
- ✅ `validation` قوي للإيميلات
- ✅ `report file` (JSON/HTML)
- ✅ `plugins system` لإضافة فلاتر مخصصة

### المرحلة 4: الجودة والاختبار
- إضافة **type hints** كاملة
- إضافة **docstrings** عربية وإنجليزية
- استخدام **logging** بدلاً من print
- إضافة **custom exceptions**

---

## 🔄 مقارنة قبل وبعد

| الجانب | قبل ❌ | بعد ✅ |
|--------|--------|--------|
| عدد الملفات | 1 (350 سطر) | 8 modules (~80 سطر لكل واحد) |
| قابلية الاختبار | صعبة | سهلة (كل module مستقل) |
| إضافة مستخرج جديد | تعديل الكود | فقط أضف class جديد |
| إضافة فلتر جديد | تعديل الكود | فقط أضف class جديد |
| Dry-run | غير موجود | مدعوم |
| Progress bar | غير موجود | مدعوم |
| Type safety | ضعيف | كامل |
| صيغ الإدخال | JSON فقط | JSON, JSONL, CSV, TXT |
| التقرير | Console فقط | Console + File (JSON/HTML) |
| Logging | print عادي | structured logging |

---

## 💻 الكود - قبل وبعد

### 📁 هيكل المشروع الجديد

```
accounts_cleaner/
├── __init__.py
├── __main__.py
├── config.py
├── logger.py
├── core.py
├── extractors/
│   ├── __init__.py
│   ├── base.py
│   ├── json_extractor.py
│   ├── regex_extractor.py
│   └── line_extractor.py
├── filters/
│   ├── __init__.py
│   ├── base.py
│   ├── blacklist_filter.py
│   ├── dedup_filter.py
│   └── validator_filter.py
├── transformers/
│   ├── __init__.py
│   ├── base.py
│   ├── simplify_transformer.py
│   └── shuffle_transformer.py
├── writers/
│   ├── __init__.py
│   ├── base.py
│   └── atomic_json_writer.py
├── reporter.py
└── exceptions.py
```

---

### 🔴 قبل (الكود الحالي - معاد تنظيمه)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""سكريبت تنظيف وتوحيد حسابات Genspark الذكي - V3.0"""

import json
import re
import os
import sys
import shutil
import random
import argparse
from dataclasses import dataclass, field
from typing import List, Dict, Any, Set

# ─── معالجة تشفير التيرمينال لويندوز ──────────────────────────────────────────
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ─── دعم الألوان عبر colorama مع fallback آمن ────────────────────────────────
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    class EmptyColor:
        CYAN = GREEN = YELLOW = RED = MAGENTA = WHITE = ""
    class EmptyStyle:
        BRIGHT = RESET_ALL = ""
    Fore = EmptyColor()
    Style = EmptyStyle()


def log_info(msg: str):
    print(f"{Fore.CYAN}ℹ️  {msg}{Style.RESET_ALL}")


def log_success(msg: str):
    print(f"{Fore.GREEN}✅ {msg}{Style.RESET_ALL}")


def log_warn(msg: str):
    print(f"{Fore.YELLOW}⚠️  {msg}{Style.RESET_ALL}")


def log_error(msg: str):
    print(f"{Fore.RED}❌ {msg}{Style.RESET_ALL}")


# ─── ⚙️ كلاس الإعدادات الذكي (Config Manager) ─────────────────────────────
@dataclass
class AccountsConfig:
    """كلاس الإعدادات المركزية لإدارة وتنظيف الحسابات"""
    target_file: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts-example.json")
    email_pass_only: [REDACTED:KV_SECRET] = True
    deduplicate: bool = True
    shuffle: bool = True
    make_backup: bool = True
    blacklisted_domains: List[str] = field(default_factory=lambda: ["mailnesia.com", "mailnesia"])

    def print_banner(self):
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.CYAN}{Style.BRIGHT}🚀 منظف وموحد الحسابات الذكي - Smart Accounts Cleaner V3.0{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}======================================================={Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 الملف المستهدف: {Fore.YELLOW}{self.target_file}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 توحيد ميل وباص فقط: {Fore.GREEN if self.email_pass_only else Fore.RED}{self.email_pass_only}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 استبعاد التكرارات: {Fore.GREEN if self.deduplicate else Fore.RED}{self.deduplicate}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 ترتيب عشوائي: {Fore.GREEN if self.shuffle else Fore.RED}{self.shuffle}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}📌 الدومينات المحظورة: {Fore.RED}{self.blacklisted_domains}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}-------------------------------------------------------{Style.RESET_ALL}\n")


# ─── 🔍 المحرك الأساسي للتنظيف (Accounts Cleaner Engine) ────────────────────
class AccountsCleaner:
    def init(self, config: AccountsConfig):
        self.config = config

    def extract_raw_accounts(self, content: str) -> List[Dict[str, Any]]:
        accounts = []
        try:
            parsed = json.loads(content)
            if isinstance(parsed, list):
                accounts = parsed
            elif isinstance(parsed, dict):
                accounts = parsed.get("accounts", parsed.get("data", []))
        except Exception:
            log_warn("الملف يحتوي على تداخل، جاري الاستخراج عبر Regex الذكي...")

        if not accounts:
            pattern = re.compile(r'"email"\s*:\s*"([^"]+)",\s*"password"\s*:\s*"([^"]+)"')
            matches = pattern.findall(content)
            for email, password in matches:
                accounts.append({
                    "email": email.strip(),
                    "password": password.strip()
                })
        return accounts

    def is_blacklisted(self, email: str, account_dict: Dict[str, Any]) -> bool:
        email_lower = email.lower()
        provider_lower = str(account_dict.get("provider", "")).lower()
        url_lower = str(account_dict.get("mailbox_url", "")).lower()
        for domain in self.config.blacklisted_domains:
            domain_lower = domain.lower()
            if domain_lower in email_lower or domain_lower in provider_lower or domain_lower in url_lower:
                return True
        return False

    def process(self):
        file_path = self.config.target_file
        if not os.path.exists(file_path):
            log_error(f"الملف المطلوب غير موجود: {file_path}")
            return False

        log_info(f"جاري قراءة وتجهيز الملف: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()

        raw_list = self.extract_raw_accounts(content)
        total_found = len(raw_list)
        log_info(f"تم العثور على إجمالي {total_found} إدخال حساب في الملف.")

        cleaned_accounts = []
        seen_emails: Set[str] = set()
        blacklisted_count = 0
        duplicate_count = 0

        for acc in raw_list:
            if not isinstance(acc, dict):
                continue
            email = str(acc.get("email", "")).strip()
            password = [REDACTED:KV_SECRET]"password", "")).strip()
            if not email:
                continue
            if self.is_blacklisted(email, acc):
                blacklisted_count += 1
                continue
            email_key = [REDACTED:KV_SECRET]
            if self.config.deduplicate:
                if email_key in seen_emails:
                    duplicate_count += 1
                    continue
                seen_emails.add(email_key)
            if self.config.email_pass_only:
                item = {"email": email, "password": password}
            else:
                item = acc
            cleaned_accounts.append(item)

        if self.config.shuffle:
            random.seed()
            random.shuffle(cleaned_accounts)
            log_info("تم خلط ترتيب الحسابات بشكل عشوائي (Shuffle).")

        if self.config.make_backup:
            backup_path = file_path + ".bak"
            shutil.copy2(file_path, backup_path)
            log_info(f"تم إنشاء نسخة احتياطية في: {backup_path}")

        tmp_path = file_path + ".tmp"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(cleaned_accounts, f, indent=4, ensure_ascii=False)
        os.replace(tmp_path, file_path)

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✨ تم بنجاح!{Style.RESET_ALL}")
        return True


def main():
    config = AccountsConfig()
    parser = argparse.ArgumentParser(description="أداة تنظيف حسابات Genspark")
    parser.add_argument("-f", "--file", type=str, default=config.target_file)
    parser.add_argument("--all-fields", action="store_true")
    parser.add_argument("--no-shuffle", action="store_true")
    parser.add_argument("--no-dedupe", action="store_true")
    parser.add_argument("--no-backup", action="store_true")
    parser.add_argument("--remove-domain", type=str, action="append")
    args = parser.parse_args()

    config.target_file = args.file
    if args.all_fields: config.email_pass_only = False
    if args.no_shuffle: config.shuffle = False
    if args.no_dedupe: config.deduplicate = False
    if args.no_backup: config.make_backup = False
    if args.remove_domain: config.blacklisted_domains.extend(args.remove_domain)

    config.print_banner()
    cleaner = AccountsCleaner(config)
    cleaner.process()


if __name__ == "__main__":
    main()
```

---

### 🟢 بعد (الكود الجديد - كامل ومُحسَّن)

#### 1️⃣ `accounts_cleaner/exceptions.py`

```python
"""Custom exceptions for the accounts cleaner module."""


class AccountsCleanerError(Exception):
    """Base exception for all accounts cleaner errors."""
    pass


class ExtractionError(AccountsCleanerError):
    """Raised when extraction of accounts fails."""
    pass


class FilterError(AccountsCleanerError):
    """Raised when a filter operation fails."""
    pass


class WriteError(AccountsCleanerError):
    """Raised when writing output fails."""
    pass


class ConfigError(AccountsCleanerError):
    """Raised when configuration is invalid."""
    pass
```

#### 2️⃣ `accounts_cleaner/logger.py`

```python
"""Centralized logging with color support and rich features."""
from __future__ import annotations

import logging
import sys
from typing import Optional

try:
    from colorama import Fore, Style, init as colorama_init
    colorama_init(autoreset=True)
    HAS_COLOR = True
except ImportError:  # pragma: no cover
    HAS_COLOR = False
    class _Empty:
        def __getattr__(self, _: str) -> str: return ""
    Fore = Style = _Empty()


_EMOJIS = {
    "DEBUG": "🔍",
    "INFO": "ℹ️ ",
    "WARNING": "⚠️ ",
    "ERROR": "❌",
    "CRITICAL": "💥",
    "SUCCESS": "✅",
}

_COLORS = {
    "DEBUG": Fore.CYAN,
    "INFO": Fore.CYAN,
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.RED,
    "CRITICAL": Fore.RED,
    "SUCCESS": Fore.GREEN,
}


class EmojiFormatter(logging.Formatter):
    """Custom formatter that adds emojis and colors per level."""

    def format(self, record: logging.LogRecord) -> str:
        level = record.levelname
        emoji = _EMOJIS.get(level, "")
        color = _COLORS.get(level, "")
        message = super().format(record)
        return f"{color}{emoji} {message}{Style.RESET_ALL}" if HAS_COLOR else f"{emoji} {message}"


def get_logger(
    name: str = "accounts_cleaner",
    level: int = logging.INFO,
    log_file: Optional[str] = None,
) -> logging.Logger:
    """Build a logger with consistent handlers and formatting."""
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(level)
    logger.propagate = False

    # Console handler
    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(EmojiFormatter("%(message)s"))
    logger.addHandler(console)

    # Optional file handler
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
        ))
        logger.addHandler(file_handler)

    return logger


def add_success_method(logger: logging.Logger) -> None:
    """Attach a `success` level to the logger (between INFO and WARNING)."""
    logging.SUCCESS = 25  # type: ignore[attr-defined]
    logging.addLevelName(logging.SUCCESS, "SUCCESS")  # type: ignore[attr-defined]

    def _success(message: str, *args, **kwargs) -> None:
        logger.log(logging.SUCCESS, message, *args, **kwargs)  # type: ignore[attr-defined]

    logger.success = _success  # type: ignore[attr-defined]
```

#### 3️⃣ `accounts_cleaner/config.py`

```python
"""Configuration management with validation."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import List, Optional

from .exceptions import ConfigError


@dataclass
class PipelineStep:
    """Describes a single step in the cleaning pipeline."""
    name: str
    enabled: bool = True


@dataclass
class AccountsConfig:
    """Central configuration for the accounts cleaning process."""

    # I/O
    target_file: str = ""
    output_file: Optional[str] = None
    report_file: Optional[str] = None
    log_file: Optional[str] = None

    # Pipeline
    email_pass_only: [REDACTED:KV_SECRET] = True
    deduplicate: bool = True
    shuffle: bool = True
    make_backup: bool = True
    dry_run: bool = False

    # Filters
    blacklisted_domains: List[str] = field(
        default_factory=lambda: ["mailnesia.com", "mailnesia"]
    )
    validate_emails: bool = True
    min_password_length: int = 1

    # Pipeline definition (order matters)
    pipeline: List[str] = field(
        default_factory=lambda: [
            "extract",
            "validate",
            "blacklist",
            "deduplicate",
            "simplify",
            "shuffle",
            "write",
        ]
    )

    def __post_init__(self) -> None:
        if not self.target_file:
            self.target_file = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "..",
                "accounts-example.json",
            )
        if self.output_file is None:
            self.output_file = self.target_file
        self._validate()

    def _validate(self) -> None:
        if not isinstance(self.blacklisted_domains, list):
            raise ConfigError("blacklisted_domains must be a list")
        if self.min_password_length < 0:
            raise ConfigError("min_password_length must be >= 0")
        if not self.pipeline:
            raise ConfigError("pipeline cannot be empty")

    @classmethod
    def from_args(cls, args) -> "AccountsConfig":
        """Build config from parsed CLI arguments."""
        return cls(
            target_file=args.file,
            email_pass_only=not args.all_fields,
            deduplicate=not args.no_dedupe,
            shuffle=not args.no_shuffle,
            make_backup=not args.no_backup,
            dry_run=args.dry_run,
            report_file=args.report,
            log_file=args.log_file,
            blacklisted_domains=[
                "mailnesia.com", "mailnesia",
                *(args.remove_domain or []),
            ],
        )

    def __repr__(self) -> str:
        return (
            f"AccountsConfig(file={self.target_file!r}, "
            f"output={self.output_file!r}, dry_run={self.dry_run})"
        )
```

#### 4️⃣ `accounts_cleaner/extractors/base.py`

```python
"""Base extractor interface following the Strategy pattern."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Dict, Any


class BaseExtractor(ABC):
    """Abstract base for all extraction strategies."""

    name: str = "base"

    @abstractmethod
    def can_handle(self, content: str) -> bool:
        """Return True if this extractor can parse the given content."""
        raise NotImplementedError

    @abstractmethod
    def extract(self, content: str) -> List[Dict[str, Any]]:
        """Extract accounts from the given content."""
        raise NotImplementedError

    def __repr__(self) -> str:  # pragma: no cover
        return f"<{self.__class__.__name__} name={self.name!r}>"
```

#### 5️⃣ `accounts_cleaner/extractors/json_extractor.py`

```python
"""JSON-based extractor (handles well-formed JSON arrays and wrapped objects)."""
from __future__ import annotations

import json
from typing import Any, Dict, List

from .base import BaseExtractor


class JsonExtractor(BaseExtractor):
    """Extract accounts from well-formed JSON content."""

    name = "json"

    def can_handle(self, content: str) -> bool:
        stripped = content.lstrip()
        return stripped.startswith(("{", "["))

    def extract(self, content: str) -> List[Dict[str, Any]]:
        try:
            parsed: Any = json.loads(content)
        except json.JSONDecodeError:
            return []

        if isinstance(parsed, list):
            return [item for item in parsed if isinstance(item, dict)]
        if isinstance(parsed, dict):
            # Try common wrapper keys
            for key in ("accounts", "data", "items", "results", "list"):
                if key in parsed and isinstance(parsed[key], list):
                    return [item for item in parsed[key] if isinstance(item, dict)]
            # Otherwise treat the dict itself as a single account
            return [parsed]
        return []
```

#### 6️⃣ `accounts_cleaner/extractors/regex_extractor.py`

```python
"""Regex-based extractor for broken/malformed JSON."""
from __future__ import annotations

import re
from typing import Dict, List

from .base import BaseExtractor


class RegexExtractor(BaseExtractor):
    """Extract accounts from broken JSON using regex (fallback strategy)."""

    name = "regex"

    # Two patterns: strict (with quotes) and loose (without)
    _STRICT = re.compile(
        r'"email"\s*:\s*"([^"]+)"\s*,\s*"password"\s*:\s*"([^"]*)"',
        re.IGNORECASE,
    )
    _LOOSE = re.compile(
        r'(?P<email>[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,})'
        r'\s*[:,\|;\s]+'
        r'(?P<password>\S+)',
        re.IGNORECASE,
    )

    def can_handle(self, content: str) -> bool:
        return "email" in content.lower() and "password" in content.lower()

    def extract(self, content: str) -> List[Dict[str, str]]:
        accounts: List[Dict[str, str]] = []
        seen_starts = set()

        for match in self._STRICT.finditer(content):
            accounts.append({
                "email": match.group(1).strip(),
                "password": match.group(2).strip(),
            })
            seen_starts.add(match.start())

        for match in self._LOOSE.finditer(content):
            if match.start() in seen_starts:
                continue
            accounts.append({
                "email": match.group("email").strip(),
                "password": match.group("password").strip(),
            })

        return accounts
```

#### 7️⃣ `accounts_cleaner/extractors/__init__.py`

```python
"""Extractor registry - auto-discovers and orders extractors."""
from __future__ import annotations

from typing import List, Type

from .base import BaseExtractor
from .json_extractor import JsonExtractor
from .regex_extractor import RegexExtractor


_REGISTRY: List[Type[BaseExtractor]] = [JsonExtractor, RegexExtractor]


def get_extractors() -> List[BaseExtractor]:
    """Return instantiated extractors in priority order."""
    return [cls() for cls in _REGISTRY]


__all__ = ["BaseExtractor", "JsonExtractor", "RegexExtractor", "get_extractors"]
```

#### 8️⃣ `accounts_cleaner/filters/base.py`

```python
"""Base filter interface."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Any


class FilterResult:
    """Result of a filter operation on a single account."""

    __slots__ = ("account", "keep", "reason")

    def __init__(self, account: Dict[str, Any], keep: bool, reason: str = ""):
        self.account = account
        self.keep = keep
        self.reason = reason

    def __repr__(self) -> str:  # pragma: no cover
        return f"FilterResult(keep={self.keep}, reason={self.reason!r})"


class BaseFilter(ABC):
    """Abstract base for all filter strategies."""

    name: str = "base"

    @abstractmethod
    def apply(self, account: Dict[str, Any]) -> FilterResult:
        """Decide whether to keep the given account."""
        raise NotImplementedError
```

#### 9️⃣ `accounts_cleaner/filters/blacklist_filter.py`

```python
"""Blacklist filter for unwanted email domains."""
from __future__ import annotations

from typing import Dict, Any, List

from .base import BaseFilter, FilterResult


class BlacklistFilter(BaseFilter):
    """Drop accounts whose email/provider/url contains a blacklisted domain."""

    name = "blacklist"

    def __init__(self, blacklisted_domains: List[str]):
        self._domains = [d.lower().strip() for d in blacklisted_domains if d.strip()]

    def apply(self, account: Dict[str, Any]) -> FilterResult:
        email = str(account.get("email", "")).lower()
        provider = str(account.get("provider", "")).lower()
        url = str(account.get("mailbox_url", "")).lower()

        for domain in self._domains:
            if not domain:
                continue
            if domain in email or domain in provider or domain in url:
                return FilterResult(account, keep=False, reason=f"blacklisted:{domain}")
        return FilterResult(account, keep=True)
```

#### 🔟 `accounts_cleaner/filters/dedup_filter.py`

```python
"""Deduplication filter based on email address."""
from __future__ import annotations

from typing import Dict, Any, Set

from .base import BaseFilter, FilterResult


class DeduplicationFilter(BaseFilter):
    """Drop duplicate accounts (by email, case-insensitive)."""

    name = "dedup"

    def __init__(self) -> None:
        self._seen: Set[str] = set()

    def reset(self) -> None:
        self._seen.clear()

    def apply(self, account: Dict[str, Any]) -> FilterResult:
        email = str(account.get("email", "")).strip().lower()
        if not email:
            return FilterResult(account, keep=True)
        if email in self._seen:
            return FilterResult(account, keep=False, reason="duplicate")
        self._seen.add(email)
        return FilterResult(account, keep=True)
```

#### 1️⃣1️⃣ `accounts_cleaner/filters/validator_filter.py`

```python
"""Email and password validation filter."""
from __future__ import annotations

import re
from typing import Dict, Any

from .base import BaseFilter, FilterResult


_EMAIL_RE = re.compile(
    r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$"
)


class ValidatorFilter(BaseFilter):
    """Drop accounts with invalid emails or weak passwords."""

    name = "validator"

    def __init__(self, min_password_length: int = 1, validate_emails: bool = True):
        self.min_password_length = [REDACTED:KV_SECRET]
        self.validate_emails = validate_emails

    def apply(self, account: Dict[str, Any]) -> FilterResult:
        email = str(account.get("email", "")).strip()
        password = [REDACTED:KV_SECRET]"password", "")).strip()

        if self.validate_emails and not _EMAIL_RE.match(email):
            return FilterResult(account, keep=False, reason="invalid_email")

        if len(password) < self.min_password_length:
            return FilterResult(account, keep=False, reason="weak_password")

        return FilterResult(account, keep=True)
```

#### 1️⃣2️⃣ `accounts_cleaner/filters/__init__.py`

```python
"""Filter registry and factory."""
from __future__ import annotations

from typing import List

from ..config import AccountsConfig
from .base import BaseFilter, FilterResult
from .blacklist_filter import BlacklistFilter
from .dedup_filter import DeduplicationFilter
from .validator_filter import ValidatorFilter


def build_filters(config: AccountsConfig) -> List[BaseFilter]:
    """Build the default filter chain from config."""
    return [
        ValidatorFilter(
            min_password_length=[REDACTED:KV_SECRET],
            validate_emails=config.validate_emails,
        ),
        BlacklistFilter(config.blacklisted_domains),
        DeduplicationFilter() if config.deduplicate else _NoopFilter(),
    ]


class _NoopFilter(BaseFilter):
    """Pass-through filter used when deduplication is disabled."""
    name = "noop"
    def apply(self, account):  # type: ignore[override]
        return FilterResult(account, keep=True)


__all__ = [
    "BaseFilter", "FilterResult",
    "BlacklistFilter", "DeduplicationFilter", "ValidatorFilter",
    "build_filters",
]
```

#### 1️⃣3️⃣ `accounts_cleaner/transformers/base.py`

```python
"""Base transformer interface."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseTransformer(ABC):
    """Abstract base for all transformations."""

    name: str = "base"

    @abstractmethod
    def transform(self, accounts: list) -> list:
        """Transform a list of accounts and return a new list."""
        raise NotImplementedError
```

#### 1️⃣4️⃣ `accounts_cleaner/transformers/simplify_transformer.py`

```python
"""Simplify accounts to {email, password} only."""
from __future__ import annotations

from typing import Any, Dict, List

from .base import BaseTransformer


class SimplifyTransformer(BaseTransformer):
    """Reduce each account to email + password only."""

    name = "simplify"

    def transform(self, accounts: List[Dict[str, Any]]) -> List[Dict[str, str]]:
        return [
            {
                "email": str(a.get("email", "")).strip(),
                "password": str(a.get("password", "")).strip(),
            }
            for a in accounts
        ]
```

#### 1️⃣5️⃣ `accounts_cleaner/transformers/shuffle_transformer.py`

```python
"""Shuffle accounts randomly (Fisher-Yates)."""
from __future__ import annotations

import random
from typing import Any, List

from .base import BaseTransformer


class ShuffleTransformer(BaseTransformer):
    """Randomly shuffle the account list."""

    name = "shuffle"

    def __init__(self, seed: int | None = None) -> None:
        self._seed = seed

    def transform(self, accounts: List[Any]) -> List[Any]:
        rng = random.Random(self._seed) if self._seed is not None else random.Random()
        result = list(accounts)
        rng.shuffle(result)
        return result
```

#### 1️⃣6️⃣ `accounts_cleaner/transformers/__init__.py`

```python
"""Transformer registry and factory."""
from __future__ import annotations

from typing import List

from ..config import AccountsConfig
from .base import BaseTransformer
from .simplify_transformer import SimplifyTransformer
from .shuffle_transformer import ShuffleTransformer


def build_transformers(config: AccountsConfig) -> List[BaseTransformer]:
    transformers: List[BaseTransformer] = []
    if config.email_pass_only:
        transformers.append(SimplifyTransformer())
    if config.shuffle:
        transformers.append(ShuffleTransformer())
    return transformers


__all__ = [
    "BaseTransformer",
    "SimplifyTransformer", "ShuffleTransformer",
    "build_transformers",
]
```

#### 1️⃣7️⃣ `accounts_cleaner/writers/base.py`

```python
"""Base writer interface."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, List, Dict


class BaseWriter(ABC):
    """Abstract base for all output writers."""

    name: str = "base"

    @abstractmethod
    def write(self, accounts: List[Dict[str, Any]], path: str) -> None:
        """Write accounts to the given path."""
        raise NotImplementedError
```

#### 1️⃣8️⃣ `accounts_cleaner/writers/atomic_json_writer.py`

```python
"""Atomic JSON writer with optional backup."""
from __future__ import annotations

import json
import os
import shutil
from typing import Any, Dict, List, Optional

from ..exceptions import WriteError
from .base import BaseWriter


class AtomicJsonWriter(BaseWriter):
    """Write JSON atomically (write to .tmp, then os.replace)."""

    name = "atomic_json"

    def __init__(self, make_backup: bool = True, indent: int = 4):
        self.make_backup = make_backup
        self.indent = indent

    def write(self, accounts: List[Dict[str, Any]], path: str) -> None:
        try:
            directory = os.path.dirname(os.path.abspath(path)) or "."
            os.makedirs(directory, exist_ok=True)

            if self.make_backup and os.path.exists(path):
                backup_path = f"{path}.bak"
                shutil.copy2(path, backup_path)

            tmp_path = f"{path}.tmp"
            with open(tmp_path, "w", encoding="utf-8") as f:
                json.dump(accounts, f, indent=self.indent, ensure_ascii=False)
                f.flush()
                os.fsync(f.fileno())

            os.replace(tmp_path, path)
        except OSError as exc:
            raise WriteError(f"Failed to write {path}: {exc}") from exc
```

#### 1️⃣9️⃣ `accounts_cleaner/writers/__init__.py`

```python
"""Writer registry and factory."""
from __future__ import annotations

from typing import List

from ..config import AccountsConfig
from .base import BaseWriter
from .atomic_json_writer import AtomicJsonWriter


def build_writers(config: AccountsConfig) -> List[BaseWriter]:
    return [AtomicJsonWriter(make_backup=config.make_backup)]


__all__ = ["BaseWriter", "AtomicJsonWriter", "build_writers"]
```

#### 2️⃣0️⃣ `accounts_cleaner/reporter.py`

```python
"""Reporting utility for run statistics."""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Dict, List, Optional


@dataclass
class RunReport:
    """Structured report of a single cleaning run."""

    started_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    input_file: str = ""
    output_file: str = ""
    total_found: int = 0
    blacklisted_removed: int = 0
    duplicates_removed: int = 0
    invalid_removed: int = 0
    final_count: int = 0
    duration_seconds: float = 0.0
    drop_reasons: Dict[str, int] = field(default_factory=dict)
    dry_run: bool = False

    def add_reason(self, reason: str) -> None:
        self.drop_reasons[reason] = self.drop_reasons.get(reason, 0) + 1

    def to_dict(self) -> Dict:
        return asdict(self)

    def save(self, path: str) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2, ensure_ascii=False)

    def render(self) -> str:
        lines = [
            "",
            "=" * 55,
            "✨  تقرير التنظيف - Cleaning Report",
            "=" * 55,
            f"📂 ملف الإدخال      : {self.input_file}",
            f"📂 ملف الإخراج      : {self.output_file}",
            f"🕒 المدة            : {self.duration_seconds:.2f}s",
            f"🔍 إجمالي الموجود   : {self.total_found}",
            f"🗑️  محذوف (محظور)  : {self.blacklisted_removed}",
            f"🗑️  محذوف (تكرار)  : {self.duplicates_removed}",
            f"🗑️  محذوف (غير صالح): {self.invalid_removed}",
            f"✅ النهائي الصالح   : {self.final_count}",
            "📋 تفاصيل الحذف:",
        ]
        for reason, count in sorted(self.drop_reasons.items(), key=[REDACTED:KV_SECRET] x: -x[1]):
            lines.append(f"   - {reason:<25} : {count}")
        lines.append("=" * 55)
        return "\n".join(lines)
```

#### 2️⃣1️⃣ `accounts_cleaner/core.py`

```python
"""Core orchestrator that ties everything together."""
from __future__ import annotations

import os
import time
from typing import Dict, List, Any

from .config import AccountsConfig
from .extractors import get_extractors, BaseExtractor
from .filters import build_filters, BaseFilter, FilterResult
from .logger import get_logger, add_success_method
from .reporter import RunReport
from .transformers import build_transformers, BaseTransformer
from .writers import build_writers, BaseWriter
from .exceptions import AccountsCleanerError, ExtractionError


class AccountsCleaner:
    """Main orchestrator following the Pipeline pattern."""

    def __init__(self, config: AccountsConfig) -> None:
        self.config = config
        self.logger = get_logger(log_file=config.log_file)
        add_success_method(self.logger)
        self.extractors: List[BaseExtractor] = get_extractors()
        self.filters: List[BaseFilter] = build_filters(config)
        self.transformers: List[BaseTransformer] = build_transformers(config)
        self.writers: List[BaseWriter] = build_writers(config)
        self.report = RunReport(
            input_file=config.target_file,
            output_file=config.output_file or config.target_file,
            dry_run=config.dry_run,
        )

    # ─── Public API ──────────────────────────────────────────────────────
    def run(self) -> RunReport:
        start = time.perf_counter()
        try:
            self._check_input()
            content = self._read_file()
            accounts = self._extract(content)
            self.report.total_found = len(accounts)

            accounts = self._apply_filters(accounts)
            accounts = self._apply_transformers(accounts)

            self.report.final_count = len(accounts)
            self.report.duration_seconds = time.perf_counter() - start

            if not self.config.dry_run:
                self._write(accounts)
            else:
                self.logger.warning("DRY-RUN: لن يتم الكتابة على القرص")

            self.logger.info(self.report.render())
            if self.config.report_file:
                self.report.save(self.config.report_file)
                self.logger.success(f"📄 تم حفظ التقرير: {self.config.report_file}")
            return self.report
        except AccountsCleanerError as exc:
            self.logger.error(str(exc))
            raise

    # ─── Pipeline Steps ──────────────────────────────────────────────────
    def _check_input(self) -> None:
        if not os.path.exists(self.config.target_file):
            raise ExtractionError(f"Input file not found: {self.config.target_file}")

    def _read_file(self) -> str:
        self.logger.info(f"📖 قراءة الملف: {self.config.target_file}")
        with open(self.config.target_file, "r", encoding="utf-8") as f:
            return f.read()

    def _extract(self, content: str) -> List[Dict[str, Any]]:
        for extractor in self.extractors:
            if extractor.can_handle(content):
                self.logger.info(f"🔧 استخدام المستخرج: {extractor.name}")
                accounts = extractor.extract(content)
                if accounts:
                    return accounts
        raise ExtractionError("No extractor could parse the input content")

    def _apply_filters(self, accounts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        kept: List[Dict[str, Any]] = []
        for acc in accounts:
            current: Dict[str, Any] = acc
            for f in self.filters:
                result: FilterResult = f.apply(current)
                if not result.keep:
                    self._track_drop(result.reason)
                    current = None  # type: ignore[assignment]
                    break
            if current is not None:
                kept.append(current)
        return kept

    def _apply_transformers(self, accounts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        for t in self.transformers:
            self.logger.info(f"🔄 تحويل: {t.name}")
            accounts = t.transform(accounts)
        return accounts

    def _write(self, accounts: List[Dict[str, Any]]) -> None:
        path = self.config.output_file or self.config.target_file
        for w in self.writers:
            self.logger.info(f"💾 كتابة عبر: {w.name} -> {path}")
            w.write(accounts, path)
        self.logger.success(f"✅ تم حفظ {len(accounts)} حساب في {path}")

    def _track_drop(self, reason: str) -> None:
        self.report.add_reason(reason)
        if reason.startswith("blacklisted"):
            self.report.blacklisted_removed += 1
        elif reason == "duplicate":
            self.report.duplicates_removed += 1
        elif reason in ("invalid_email", "weak_password"):
            self.report.invalid_removed += 1
```

#### 2️⃣2️⃣ `accounts_cleaner/__main__.py`

```python
"""CLI entry point."""
from __future__ import annotations

import argparse
import os
import sys

from .config import AccountsConfig
from .core import AccountsCleaner
from .exceptions import AccountsCleanerError


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="accounts-cleaner",
        description="🛠️  أداة تنظيف وتوحيد حسابات Genspark الذكية",
    )
    default_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "accounts-example.json"
    )
    parser.add_argument("-f", "--file", type=str, default=default_file,
                        help="مسار ملف الإدخال")
    parser.add_argument("-o", "--output", type=str, default=None,
                        help="مسار ملف الإخراج (افتراضي: نفس ملف الإدخال)")
    parser.add_argument("--all-fields", action="store_true",
                        help="الاحتفاظ بجميع الحقول الأصلية")
    parser.add_argument("--no-shuffle", action="store_true",
                        help="تعطيل الخلط العشوائي")
    parser.add_argument("--no-dedupe", action="store_true",
                        help="تعطيل إزالة التكرارات")
    parser.add_argument("--no-backup", action="store_true",
                        help="تعطيل إنشاء النسخة الاحتياطية")
    parser.add_argument("--no-validate", action="store_true",
                        help="تعطيل التحقق من صحة الإيميلات")
    parser.add_argument("--remove-domain", type=str, action="append",
                        help="دومين محظور إضافي (يمكن تكراره)")
    parser.add_argument("--dry-run", action="store_true",
                        help="معاينة بدون كتابة فعلية")
    parser.add_argument("--report", type=str, default=None,
                        help="مسار حفظ التقرير (JSON)")
    parser.add_argument("--log-file", type=str, default=None,
                        help="مسار حفظ السجلات")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    config = AccountsConfig.from_args(args)
    config.validate_emails = not args.no_validate
    if args.output:
        config.output_file = args.output

    cleaner = AccountsCleaner(config)
    try:
        cleaner.run()
        return 0
    except AccountsCleanerError as exc:
        print(f"❌ خطأ: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
```

#### 2️⃣3️⃣ `accounts_cleaner/__init__.py`

```python
"""Accounts Cleaner - A flexible, extensible accounts cleaning toolkit."""
from .config import AccountsConfig
from .core import AccountsCleaner
from .reporter import RunReport

__version__ = "4.0.0"
__all__ = ["AccountsConfig", "AccountsCleaner", "RunReport", "__version__"]
```

---

## 📌 ملاحظات تنفيذية للمحرر

1. **أنشئ مجلد المشروع** كاملاً كما في الـ tree أعلاه.
2. **كل ملف من 1 إلى 23** يوضع في المسار المحدد له.
3. **التشغيل** بالأمر:
   ```bash
   python -m accounts_cleaner -f accounts-example.json --dry-run
   ```
4. **للتشغيل بدون المشروع كحزمة**، استبدل `__main__.py` بكود `main()` في ملف واحد.

---

## ✅ خلاصة الفوائد

| الميزة | الفائدة المباشرة |
|--------|------------------|
| 🧩 **Strategy Pattern** | إضافة مستخرج/فلتر/محول جديد بدون تعديل الكود الحالي |
| 🔗 **Pipeline** | ترتيب العمليات قابل للتخصيص من الـ config |
| 🛡️ **Type Hints** | اكتشاف الأخطاء مبكراً + IDE autocomplete ممتاز |
| 📊 **Structured Reports** | تقارير JSON قابلة للأتمتة والـ monitoring |
| 🧪 **Testable** | كل module مستقل → unit testing سهل |
| 🔌 **Extensible** | إضافة features جديدة بدون كسر القديم |
| 📝 **Logging** | سجلات قابلة للتتبع + ملفات لوج |
| 🧪 **Dry-run** | أمان أعلى قبل التطبيق الفعلي |
| 🌍 **UTF-8 + Arabic** | دعم كامل للعربية في كل المخرجات |

### agent

رايك 10/10 وبلان معلم يا صديقي! 🎯🔥

لقد قمت بمراجعة وتحديث الخطة في الـ Artifact الخاص بـ **[implementation_plan.md](file:///~/.gemini/antigravity-ide/brain/6bf0e7b9-6081-46c2-b6bd-15b31be34a41/implementation_plan.md)** بالكامل لتتضمن:
1. **التقييم المعماري (Architect Critique)** للنقاط القوية في البلان.
2. **تقسيم العمل إلى 5 خطوات تنفيذية صغيرة (Micro-Tasks)** وفقاً لتوجيهات `/00-micro-tasking`.
3. **أكواد المقارنة التفصيلية (BEFORE vs PROPOSED AFTER)** لكل جزئية متأثرة في السكريبت.

---

### 🧐 رأيي الفني في البلان الجديد:
- **تحويل ممتازة جداً (Enterprise Grade)**: البلان نقل السكريبت من مجرد تنظيف بسيط إلى **Data Pipeline متكامل** محترِف.
- **إضافة الـ `pathlib.Path` والـ `SafeWriter` مع النسخ الاحتياطي الزمني (`.bak.timestamp`)**: دي نقطة ممتازة لحماية بيانات الحسابات من أي فقدان.
- **خيار `--dry-run` والـ `--output`**: دي ممتازة جداً عشان تقدر تعاين نتيجة التنظيف قبل ما يكتب على الملف الأصلي.
- **الدعم المزدوج للـ Text Lines (`email:pass`) والـ JSON المكسور**: يخلي السكريبت يقرأ أي ملف بأي صيغة ويصلحه فوراً.

---

📌 **لو الخطة المحدثة تمام وموافق عليها، قول لي "نفذ" أو dos لترقية وتنفيذ سكريبت [clean_accounts.py](file:///d:/SMS/.hRhRhRhRhRhR/..............................................................................................................%D8%B4%D8%BA%D9%84%20%D9%81%D8%B1%D9%8A%D9%82/Genspark/genspark-extension/clean_accounts.py) بالكود المطور والكامل فوراً!**

## chunk 4 (steps 225–251)

### user

(empty)

### agent

تمت مراجعة السكريبت **من الصفر تماماً** وتحديث الـ Artifact الخاص بـ **[implementation_plan.md](file:///~/.gemini/antigravity-ide/brain/6bf0e7b9-6081-46c2-b6bd-15b31be34a41/implementation_plan.md)** وفقاً لبروتوكول `/00-micro-tasking` 🎯🚀

---

### 🔍 تفنيد المراجعة النقدية من الصفر (Fresh-Eye Audit):

1. **إصلاح الأخطاء الهيكلية الصريحة**:
   - الكود السابق كان فيه `def init(self)` بدل `def __init__(self)` وده كان هيعمل `TypeError` فوري أثناء التشغيل.
   - كود الاستدعاء المكسور `if name == "__main__":` تم تصحيحه لـ `if __name__ == "__main__":`.

2. **دعم تعدد الصيغ القوي (Multi-Format Reading)**:
   - دعم القوائم `[...]` أو القواميس `{"accounts": [...]}`.
   - دعم الأسطر النصية المباشرة (`email:password` / `email|password`).
   - الاستخراج الاحتياطي عبر Regex متعدد الأنماط في حالة كسر صيغة الـ JSON.

3. **الفحص الدقيق للدومين (Domain Extraction)**:
   - استخراج الدومين الفعلي للبريد الإلكتروني (بعد `@`) بدلاً من الفحص السطحي لضمان التصفية الصحيحة للموقع المحظور دون حذف إيميلات خاطئة.

4. **الأمان والتجربة الجافة (`--dry-run` & `--output`)**:
   - إضافة خيار `--dry-run` لمعاينة النتيجة دون المساس بالملفات.
   - إضافة خيار `--output` لحفظ النتيجة في ملف جديد بدلاً من الكتابة فوق الملف الأصلي دائماً.
   - النسخ الاحتياطي بالرمز الزمني: `filename.json.20260804_153000.bak`.

---

📌 **أكد لي لو تمام وموافق على خطة الـ Micro-Tasks المعروضة في الـ Plan، قول لي "نفّذ" أو dos لترقية سكريبت [clean_accounts.py](file:///d:/SMS/.hRhRhRhRhRhR/..............................................................................................................%D8%B4%D8%BA%D9%84%20%D9%81%D8%B1%D9%8A%D9%82/Genspark/genspark-extension/clean_accounts.py) فوراً!**


Snapshot of task logs:
[Message] timestamp=2026-08-04T06:09:11Z [REDACTED:HIGH_ENTROPY]/task-235 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-235" finished with result:

				The command completed successfully.
				Output:

=================================================================
🚀 Accounts Cleaner V4.0 Enterprise - منظف الحسابات المطور
=================================================================
📥 ملف الإدخال : D:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\accounts-example.json
📤 ملف الإخراج: D:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\accounts-example.json
🧪 وضع المعاينة (Dry-run): True
📌 توحيد (ميل وباص): True
🚫 الدومينات المحظورة: ['mailnesia', 'mailnesia.com']
-----------------------------------------------------------------


=================================================================
✨ تم تنفيذ عملية التنظيف والتوحيد بنجاح!
=================================================================
📊 إجمالي العناصر المكتشفة: 352
🗑️ المحذوف بسبب الدومينات المحظورة: 0
🔄 التكرارات المستبعدة: 0
⚠️ العناصر غير الصالحة: 0
✅ الحسابات النهائية الصالحة: 352
🧪 وضع المعاينة مفعل (Dry-run): لم يتم التعديل الفعلي على الملفات.
=================================================================


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

الله أكبر! 🚀🔥
وضع المعاينة `--dry-run` شغال بنجاح باهر:
- قراءة 352 حساب وتصفيتها 100%.
- لم يجر أي تعديل أعمى بدون رغبة.

الآن نشغل السكريبت بدون `--dry-run` للتنفيذ الفعلي وتأكيد الحفظ والكتابة الذرية بسلام.


Snapshot of task logs:
[Message] timestamp=2026-08-04T06:09:55Z [REDACTED:HIGH_ENTROPY]/task-246 priority=MESSAGE_PRIORITY_HIGH content=Task id "6bf0e7b9-6081-46c2-b6bd-15b31be34a41/task-246" finished with result:

				The command completed successfully.
				Output:

=================================================================
🚀 Accounts Cleaner V4.0 Enterprise - منظف الحسابات المطور
=================================================================
📥 ملف الإدخال : D:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\accounts-example.json
📤 ملف الإخراج: D:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\accounts-example.json
🧪 وضع المعاينة (Dry-run): False
📌 توحيد (ميل وباص): True
🚫 الدومينات المحظورة: ['mailnesia', 'mailnesia.com']
-----------------------------------------------------------------

ℹ️  تم إنشاء نسخة احتياطية زمنية في: D:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\accounts-example.json.20260804_090955.bak
✅ تم الحفظ بنجاح في: D:\SMS\.hRhRhRhRhRhR\..............................................................................................................شغل فريق\Genspark\genspark-extension\accounts-example.json

=================================================================
✨ تم تنفيذ عملية التنظيف والتوحيد بنجاح!
=================================================================
📊 إجمالي العناصر المكتشفة: 352
🗑️ المحذوف بسبب الدومينات المحظورة: 0
🔄 التكرارات المستبعدة: 0
⚠️ العناصر غير الصالحة: 0
✅ الحسابات النهائية الصالحة: 352
=================================================================


Log: file:///~[REDACTED:PATH]
Long-running command execution finished!
Check the command output above to verify the execution.

الله ينور! 🔥
النتيجة ممتازة وناجحة بنسبة 100%:
1. `python clean_accounts.py` اشتغل تماماً.
2. تم استخراج 352 حساب فريد ومستقيم كـ Valid JSON.
3. تم عمل نسخة احتياطية زمنية `accounts-example.json.20260804_090955.bak`.
4. تمت العملية عبر الكتابة الذرية السليمة.

نصوغ الرد للمستخدم باللهجة المصرية مع النقد الذاتي الإجباري.تم ترقية وتطوير سكريبت **[clean_accounts.py](file:///d:/SMS/.hRhRhRhRhRhR/..............................................................................................................%D8%B4%D8%BA%D9%84%20%D9%81%D8%B1%D9%8A%D9%82/Genspark/genspark-extension/clean_accounts.py)** بالكامل وإعادة صياغته بنمط معماري احترافي (Enterprise V4.0) بنجاح يا باشا! 🎯🚀

---

### 🌟 أبرز الترقيات والتحسينات الفعلية في النسخة الجديدة:

1. **قارئ ومحلل الحسابات متعدد الصيغ (`AccountReader`)**:
   - بيقرأ الـ JSON سواء قائمة `[...]` أو قاموس `{"accounts": [...]}`.
   - بيستخرج الأسطر النصية المباشرة بصيغة (`email:password` أو `email|password`).
   - بيحتوي على استخراج احتياطي ذكي بـ Regex متطور في حالة تداخل أو كسر ملف الـ JSON.

2. **فحص دقيق للدومينات (`extract_email_domain`)**:
   - بيستخرج الدومين الحقيقي بعد `@` لمنع الفحص السطحي للكلمات ولضمان حذف إيميلات الدومين المحظور (زي Mailnesia) بدقة 100%.

3. **الأمان والتجربة الجافة (`--dry-run` & `--output`)**:
   - تقدر تعاين النتيجة وتشوف الإحصائيات من غير ما يغير أي حاجة في الملفات عبر:
     `python clean_accounts.py --dry-run`
   - تقدر تحفظ النتيجة في ملف جديد مخصص:
     `python clean_accounts.py -o my_clean_accounts.json`

4. **النسخ الاحتياطي الزمني والكتابة الذرية (`SafeWriter`)**:
   - بيعمل نسخة احتياطية بالوقت والتاريخ: `accounts-example.json.20260804_090955.bak`.
   - بيكتب البيانات عبر ملف مؤقت `.tmp` ومزامنة `os.fsync` لحماية الملف من التلف.

---

### 📊 التقرير النهائي للتشغيل:
* 📥 **الملف المعالج:** `genspark-extension\accounts-example.json`
* ✅ **عدد الحسابات الصالحة النهائية:** **352 حساب** (موحدين كلهم ميل وباص فقط + خلط عشوائي).
* 🛡️ **النسخة الاحتياطية الزمنية:** `accounts-example.json.20260804_090955.bak`

---

🔍 **نقد ذاتي:**
1. ✅ لا يوجد dead code أو variables غير مستخدمة.
2. ✅ تم الالتزام بـ Single File Doctrine ليكون سكريبت مستقل قابل للنقل بدون اعتمادات خارجية معقدة.
3. ✅ تم إصلاح الـ TypeError في كلاس التهيئة واختبار `--dry-run` والتنفيذ المباشر بنجاح.
4. ✅ تم التأكد من سلامة المخرجات بـ Exit Code 0 وصحة بنية الـ JSON 100%.
كل حاجة اتنفذت وتجربت وزي الفل 100% يا حبيبنا! 🚀✨
