# 🧠 المرجع الشامل — منظومة Google One / Gemini AI Hybrid Trial (`repo_echiiiro` + MuMu 15)

> **الغرض من المرجع:** دليل دائم للتعليمات، القواعد، الأوامر، المعمارية، وحلول الأعطال الحقيقية الخاصة بتفعيل وفحص باقات **Google AI Pro (5 TB)** و **Google AI Ultra** على محاكي **MuMu Player 15 (Android 15)** عبر **Frida 16.7.19 + Play Billing v5–v8 (`module.apk`)** بدون لمس أي تطبيقات محلية خبيثة أو تعديل ملفات نظام مقفولة.

---

## 1️⃣ خريطة الملفات والمسارات المعتمدة

- **مسار المشروع الرئيسي:** `D:\SMS\.hRhRhRhRhRhR\repo_echiiiro\`
  - `START.bat` (UTF-8 بدون BOM، أسطر CRLF): قائمة التشغيل السريعة (`1–7`, `M`, `0`).
  - `hybrid-trial.ps1` (UTF-8 بـ BOM): المنسّق الذكي بنظام **Best-First Cascade** وتجاهل متفرعات العائلة (`subs_variant 6mo`). لا يستخدم `param()` تفادياً لتصادم أعلام `--*` مع PowerShell 5.1.
  - `auto-trial.ps1` (UTF-8 بـ BOM): المحرك الموحّد لـ ADB و Frida (أوضاع `--list` / `--activate --allow-checkout` / `--verify` / `--check-adb` / `--clean-cache`).
  - `frida-auto-trial.js` (UTF-8 بدون BOM): سكريبت حقن `BillingClient` داخل عملية `com.google.android.apps.subscriptions.red` عبر `module.apk` وعزل `BootClassLoader`.
  - `prepare-mumu.ps1` (UTF-8 بـ BOM): تجهيز محاكي MuMu (والمحاكي مطفأ تماماً) لتفعيل Root وفك القفل والتمويه كـ `Xiaomi 15 Ultra` (`25010PN30G`).
  - `module.apk`: حزمة Billing المساعدة المرفوعة إلى `/data/local/tmp/module.apk` (يتم التحقق ديناميكياً من بصمة `SHA-256` بين النسخة المحلية والجهاز + فرض `chmod 0444`).
  - `frida-server` + `frida-server.zip`: خادم Frida **v16.7.19** على الجهاز (`/data/local/tmp/frida-server`).
- **ملف الإرشاد العام (خالي من البيانات الخاصة):** `~\.gemini\antigravity\brain\859afe72-1223-4095-9d33-6701c4db8928\TELEGRAM_COMPLETE_GUIDE.md`
- **حزمة الاختبار الشاملة (`11` اختبار PowerShell + `7` اختبارات Node.js):** `~\.gemini\antigravity\brain\859afe72-1223-4095-9d33-6701c4db8928\scratch\test_suite.ps1`

---

## 2️⃣ ترتيب الطابور وقواعد الأهلية والباقات (Business Rules)

### أ. أولوية التفعيل في `hybrid-trial.ps1` (`Build-RankedQueue`):
1. **`g1.play.ai.pro` (`20x`)** — Google AI Ultra 20x (30 TB) إذا وُجد له عرض مجاني فعلي (`phases.size() > 1` مع `phase 0` = مجاني).
2. **`g1.play.20tb` (`5x`)** — Google AI Ultra 5x (20 TB) إذا وُجد له عرض مجاني فعلي.
3. **`g1.2tb.ai.subs_variant` (`pro12`, فقط `months == 12`)** — Google AI Pro (5 TB) لمدة **12 شهراً** (`12months-eft`).
   - **قاعدة Pruning إلزامية:** يتم استبعاد عرض `6months-eft` من نفس عائلة `subs_variant` عمداً لمنع استهلاك الأهلية مرتين (`double-burn`) إذا رُفض التفعيل من جوجل بلاي.
4. **`g1.play.2tb.ai` (`pro`, fallback موثوق)** — Google AI Pro (5 TB) لمدة **3 شهور** (`eft-3mo` أو أطول فترة متاحة).

### ب. قرارات البزنس الصارمة (ممنوعات ومحددات):
- **استبعاد `AI Plus` ومشاركة العائلة نهائياً:** باقات `g1.helium` / `g1.ai.plus` / `g1.play.ai` وخطط `Family Sharing` مستبعدة تماماً من السكريبتات بناءً على طلب المستخدم (الأولوية لحسابات `Pro` / `Ultra` المستقلة بالكوتة الكاملة).
- **حقيقة `Google AI Ultra`:** العروض التجريبية المجانية لـ Ultra (`20x` و `5x`) موقوفة حالياً من خوادم جوجل وتظهر في الفحص بأسعار مدفوعة كاملة (`$99.99` / `$149.99` / `$199.99` بدون فترة مجانية)، لذا يتخطاها السكريبت تلقائياً.
- **الفرق الميداني بين `pro12` و `pro` (3 شهور) وتقنية الدمج بالترتيب (`CHARGE_FULL_PRICE`):**
  - عرض `g1.2tb.ai.subs_variant / 12months-eft` قد يظهر كـ `Free` في فحص `queryProductDetailsAsync` على الحسابات الأمريكية، لكن الفتح المباشر له غالباً يرفضه Play Checkout بعد الضغط برسالة: `"The item you requested is not available for purchase"` (`code=4`) بسبب فحوصات Play Integrity / أهلية جهاز الشريك.
  - عرض `g1.play.2tb.ai / eft-3mo` (3 شهور) مستقر ويعمل بنجاح على MuMu 15 ويتم التحقق منه بنجاح (`ENTITLEMENT_VERIFIED ack=true`).
  - **ثغرة التكديس والتجاوز المثبتة حياً (2026-11-20):** بعد تفعيل `g1.play.2tb.ai / eft-3mo` (`3` شهور)، إرسال `BillingFlowParams$SubscriptionUpdateParams` مع `oldPurchaseToken` و `ReplacementMode.CHARGE_FULL_PRICE (5)` إلى `g1.2tb.ai.subs_variant / 12months-eft` تجاوز الرفض المباشر ودمج الأيام المتبقية (`365 + 89 = 454 يوم`) بـ **`Today: $0.00`** وتم تفعيله وقبوله رسمياً على خوادم Google Play (`ack=true` حتى **`18 Feb 2028`**)!
  - **تحذير خطير حول باقي أوضاع `ReplacementMode`:** وضع `DEFERRED (6)` يحذف العرض المجاني ويحوّله لاشتراك مدفوع `$19.99/mo`؛ وضعا `WITHOUT_PRORATION (3)` و `WITH_TIME_PRORATION (1)` يُرفضان بـ `code=5`؛ ووضع `CHARGE_PRORATED_PRICE (2)` يطلب `$1.33 Today`؛ كما أن محاولة `CHARGE_FULL_PRICE` على `Ultra (20TB)` تطلب دفع **`$99.99 Today` فوراً** لعدم وجود أي مرحلة مجانية لـ Ultra.
- **قاعدة أمان التكديس والتشغيل:** الوضع القياسي في `auto-trial.ps1` يفحص الملكية مسبقاً ويقف بكود `5` (`ITEM_ALREADY_OWNED`) لمنع أخطاء التكديس، وتقنية التبديل (`CHARGE_FULL_PRICE`) تُجرَّب فقط كخطوة واعية بعد `eft-3mo` وبالتحقق البصري من وجود `Today: $0.00`.
- **حقيقة عرض الطلبة (`one.google.com/ai-student`):** داخل مصر يعطي **AI Plus** فقط، أما منحة **AI Pro (12 شهراً)** للطلبة فتتطلب التحقق عبر **SheerID** لحسابات جامعات أمريكية (بريد `.edu` + إثبات قيد جامعي).

---

## 3️⃣ جدول أكواد الخروج في `auto-trial.ps1` وتصرف `hybrid-trial.ps1`

- **`0` (`LIST_COMPLETE` / `TRIAL_ACTIVATED` / `ENTITLEMENT_VERIFIED`):** نجاح كامل. في `--activate` يعرض دليل الحماية بعد الاشتراك.
- **`1` (خطأ قاتل — `BOOTSTRAP_TIMEOUT` / `LAUNCH_ERROR` / `NO_ACTIVITY` / فشل بيئة):** إيقاف فوري لكل الطابور.
- **`2` (العرض غير متاح — `NO_TRIALS` / `SELECT_FAILED` / `ENTITLEMENT_EMPTY` / Billing `code=4`):**
  - مع `--activate` يقوم `auto-trial.ps1` تلقائياً بـ `Reset-PlayTransientUi` (`KEYCODE_BACK` + `am force-stop com.android.vending`).
  - في `hybrid-trial.ps1` ينتقل تلقائياً للخطة التالية خلال `1.5` ثانية.
- **`3` (`USER_CANCELLED` / Billing `code=1`):**
  - `hybrid-trial.ps1` يسأل المستخدم: `Checkout cancelled. Try next fallback tier? [y/N]` قبل التجربة التالية.
- **`4` (`CHECKOUT_TIMEOUT`):**
  - `hybrid-trial.ps1` يشغل `--verify` أولاً للتأكد إذا كان الدفع تم في الخلفية؛ لو ما زال فارغاً يسأل المستخدم `[y/N]` للانتقال للخطة التالية.
- **`5` (`ITEM_ALREADY_OWNED` / Billing `code=7`):**
  - توقف آمن فوري (`hybrid-trial.ps1` يخرج بكود `0`) لأن الحساب مشترك بالفعل.
- **`6` (فشل شبكة / فوترة — `CONNECT_FAILED` / `QUERY_FAILED` / `SETUP_FAILED`):** إيقاف فوري.
- **`7` (`PURCHASE_PENDING` — `PurchaseState=2`):**
  - إيقاف طوارئ فوري (`exit 7`) لمنع إعادة محاولة الشراء وحدوث سحب مزدوج من البطاقة.

---

## 4️⃣ قواعد الحماية المالية وأمان الحساب (Checkout & Post-Activation Checklist)

1. **إذن الدفع الصريح:** أمر `--activate` محظور برمجياً بدون تمرير `--allow-checkout` معه (الوضع الافتراضي `--list` آمن للقراءة فقط).
2. **أثناء شاشة Google Play Checkout:**
   - تأكد بعينك من السطر: `Starting today: 3-month free trial` (أو `12-month free trial`) وتاريخ بداية السحب المستقبلي بوضوح قبل الضغط على `Subscribe`.
   - لا تفعّل أي خيار `backup payment method` ولا تحفظ بطاقة احتياطية.
   - لا تضغط `Back` بعشوائية أثناء معالجة الدفع، وإذا انتهت مهلة السكربت (`120s` افتراضياً أو حسب `--timeout`) ونافذة الدفع ما زالت مفتوحة يمكنك إكمال الضغط على `Subscribe` ثم تشغيل `--verify` للتحقق.
3. **إجباري خلال 72 ساعة (والأفضل بعد 10 ثوانٍ مباشرة من نجاح التفعيل):**
   - افتح تطبيق **Google One** مرة واحدة لتأكيد المزامنة وتحويل `ack=true` (إذا ظهر `ack=false` في اللوج، فتح التطبيق يُنهي الـ Acknowledge).
   - افتح **Play Store -> Payments & subscriptions -> Subscriptions -> Google One -> Cancel subscription** لإيقاف التجديد التلقائي فوراً (الاشتراك والمميزات يستمران حتى آخر يوم في الفترة المجانية دون أي خصم).
   - ادخل على `https://pay.google.com` واحذف وسيلة الدفع إذا لم تعد بحاجة إليها.
4. **تنقيح اللوجات (PII Redaction):** `auto-trial.ps1` يفلتر `PURCHASE:`, `purchaseToken`, `orderId`, و `GPA.*` قبل الطباعة أو الكتابة في ملف اللوج (`autotrial-*.log`).

---

## 5️⃣ اشتراطات البيئة على Windows + MuMu Player 15 (Android 15)

- **تهيئة MuMu 15 وهو مطفأ تماماً:**
  - شغّل `.\prepare-mumu.ps1 -VmIndex 0` (أو `--no-spoof` للحفاظ على هوية Samsung) والمحاكي مغلق كلياً (`is_process_started == false && is_android_started == false`).
  - يقوم تلقائياً بتفعيل `root_permission=true` (ويترك `system_disk_readonly` على وضعه الآمن لأن تغييره لـ `false` عبر CLI على Android 15 يسبّب `VERR_FILE_NOT_FOUND` لفقدان `system-diff.vdi`، بينما `/data/local/tmp/` على `data.vdi` قابل للكتابة أصلاً).
- **تطابق إصدار Frida الصارم (لا تستخدم Frida 17!):**
  - الخادم داخل المحاكي: `frida-server 16.7.19`.
  - العميل على ويندوز: `pip install "frida==16.7.19" "frida-tools<14.0.0"`.
  - أي تعارض في الـ Major Version (مثل Frida 17) يسبب `Failed to attach: unable to communicate with remote frida-server`.
- **حماية Android 14/15 W^X لـ `DexClassLoader`:**
  - أندرويد 15 يرفض تحميل أي `.apk` قابل للكتابة عبر `DexClassLoader` بـ `SecurityException`.
  - `auto-trial.ps1` يفحص `SHA-256` لـ `module.apk` ويرفعه عند الاختلاف ثم يفرض `chmod 0444 /data/local/tmp/module.apk` تلقائياً.

---

## 6️⃣ دليل تشخيص وحل الأعطال الميدانية المثبتة (8 Bugs Solved)

1. **تعليق `adb start-server` للأبد في PowerShell:**
   - **السبب:** `Start-Process -Wait` ينتظر شجرة العمليات بما فيها `adb fork-server` الخلفية.
   - **الحل:** `Start-AdbDaemon` يستخدم `[System.Diagnostics.Process]::Start($psi)` مع `WaitForExit(8000)` بدون انتظار الشجرة.
2. **توهم وجود عدة أجهزة على محاكي MuMu 15 واحد (`more than one device`):**
   - **السبب:** محاكي MuMu 15 واحد يستجيب على 3 بورتات (`16384`, `7555`, `5555`) إضافة إلى `emulator-5554`.
   - **الحل:** `Find-ConnectedDevices` يقرأ `/proc/sys/kernel/random/boot_id` لإزالة البورتات المكررة لنفس النواة، ولا يسقط إلى `adb devices` إلا إذا كانت قائمة TCP فارغة (`$found.Count -eq 0`).
3. **تجمد `am start` خلف نافذة Play المتبقية (`SheetUiBuilderHostActivity`) عند `--verify`:**
   - **السبب:** نافذة Play Checkout المعلقة فوق Task تطبيق Google One تمنع `am start` العادي وتخرج بـ `Warning: Activity not started` مع `pidof` فارغ.
   - **الحل:** `Get-GoogleOnePid` يستخدم `am start --activity-clear-task -n $activity`، وإذا ظهر التحذير يرسل `input keyevent 4` (`Back`) ويعيد الإطلاق ثم يمسح `pidof` بمرونة حتى 8 محاولات.
4. **تجمد `--verify` صامتاً بعد `BillingClient connected` عند وجود اشتراك فعّال:**
   - **السبب:** Google One يحتوي داخل `base.apk!classes2.dex` على نسخة مضغوطة بـ R8 من `Purchase` تفتقد `getPurchaseToken()`، وبسبب تفويض `context.getClassLoader()` (Parent-First) ينهار `BillingClientImpl` في `module.apk` بصمت بـ `NoSuchMethodError` داخل `FutureTask`.
   - **الحل المعماري الجذري:** تمرير `context.getClassLoader().getParent()` (`BootClassLoader`) إلى `DexClassLoader` في `frida-auto-trial.js` مع تنفيذ الاستعلام من `QRClass` عبر `postMain(..., 0)`.
5. **إنهاء `frida -q -t 0` خلال صفر ثانية في `frida-tools < 14`:**
   - **السبب:** `-t 0` يعني مهلة صفرية فينفصل السكربت قبل ردود `BillingClient`.
   - **الحل:** التشغيل بـ `-q -t inf` وتصريف `StandardOutput`/`StandardError` عبر `ReadToEndAsync()` مع مؤقت ثنائي المرحلة (`<=30s` للتحضير و `--timeout` للدفع) وبوابة عزل `[<RUN_ID>]` في `logcat`.
6. **انهيار مصفوفة العنصر الواحد في PowerShell 5.1 (`$arr.Count -eq $null`):**
   - **السبب:** PowerShell 5.1 يفك المصفوفة ذات العنصر الواحد تلقائياً عند إرجاعها من الدوال (واستخدام `, @(...)` مع `@(Func)` يسبب تغليفاً مزدوجاً `Object[][]`).
   - **الحل:** إرجاع `@($list.ToArray())` من الدالة والتغليف مرة واحدة `@(Func ...)` عند جهة الاستدعاء فقط.
7. **تصادم `param()` في PowerShell 5.1 مع أعلام `--list` / `--allow-checkout`:**
   - **السبب:** محلل `param()` يفسر `--*` على نحو خاطئ ويفجر `ParameterBindingException`.
   - **الحل:** الاستغناء عن `param()` تماماً وتحليل `$args` بحلقة `while ($i -lt $args.Count)`.
8. **خطأ `Startup failed (VERR_FILE_NOT_FOUND)` بعد `prepare-mumu.ps1` على MuMu 15 الجديد:**
   - **السبب:** فرض `--key system_disk_readonly --value false` عبر CLI يجعل `.nemu` يبحث عن `system-diff.vdi` غير الموجود على جهاز Android 15 جديد؛ بينما `frida-server` و `module.apk` يعملان في `/data/local/tmp/` على `data.vdi` القابل للكتابة بالفعل.
   - **الحل:** الاقتصار على `root_permission=true` وترك `system_disk_readonly` كما هو (`true` افتراضياً)، وعند عودة `id -u` كـ `2000` يقوم `auto-trial.ps1` تلقائياً بترقية `adbd` عبر `adb root` (`UID=0`).
9. **فشل `Get-GoogleOnePid` في استدعاءين متتاليين سريعين (`--list` ثم `--verify`) على Android 15:**
   - **السبب:** إعادة تشغيل Google One فور `am force-stop` قد تتسابق مع تفكيك العملية السابقة فلا تعيد `pidof` نتيجة قبل انتهاء المسح.
   - **الحل:** زيادة انتظار ما بعد `am force-stop` في `Get-GoogleOnePid` إلى `1200ms` وتوسيع المسح إلى `10` محاولات مع إعادة إطلاق `--activity-clear-task` عند المحاولتين `3` و`6`.

---

## 7️⃣ أوامر التشغيل والتحقق السريعة (Cheat Sheet) & قائمة `START.bat`

* خيارات `START.bat`: `[1]` تلقائي `15` شهراً (`--stack-15m`) | `[2]` فحص فقط (`--dry-run`) | `[3]` التدرج الكلاسيكي (`Ultra -> Pro 12m -> Pro 3m`) | `[4]` ترقية فورية (`--replace-mode CHARGE_FULL_PRICE`) | `[5]` مباشر `eft-3mo` | `[6]` التحقق (`--verify`) | `[7]` مسح الكاش (`--clean-cache`) | `[8]` فحص `ADB` | `[M]` تجهيز MuMu (Xiaomi) | `[N]` تجهيز MuMu (Samsung) | `[0]` خروج.

```powershell
# الانتقال لمجلد المشروع
cd "D:\SMS\.hRhRhRhRhRhR\repo_echiiiro"

# 1. تجهيز محاكي MuMu #0 (وهو مطفأ تماماً؛ أضف --no-spoof للإبقاء على هوية Samsung)
.\prepare-mumu.ps1 -VmIndex 0 --no-spoof

# 2. فحص اتصال ADB وإزالة تكرار البورتات
.\auto-trial.ps1 --check-adb

# 3. فحص العروض المؤهلة على الحساب الحالي بدون فتح شاشة دفع
.\hybrid-trial.ps1 --dry-run

# 4. الدمج الآلي الكامل لوصفة الـ 15 شهراً (يفحص حالة الحساب ثم eft-3mo -> CHARGE_FULL_PRICE -> 12months-eft)
.\hybrid-trial.ps1 --allow-checkout --stack-15m --timeout 180

# 5. التشغيل بالتدرج الكلاسيكي (Ultra -> Pro 12m -> skip 6m -> Pro 3m)
.\hybrid-trial.ps1 --allow-checkout --timeout 180

# 6. ترقية حساب يحمل 3 شهور (g1.play.2tb.ai) إلى 12 شهراً مباشرة عبر CHARGE_FULL_PRICE
.\auto-trial.ps1 --activate --allow-checkout --product pro12 --dur 12mo --offer-id 12months-eft --replace-mode CHARGE_FULL_PRICE

# 7. فتح خطة Pro 3-Month مباشرة
.\auto-trial.ps1 --activate --allow-checkout --product pro --dur 3mo --offer-id eft-3mo

# 8. التحقق من اشتراك الحساب الحالي وحفظ النتيجة كـ JSON
.\auto-trial.ps1 --verify --out-json .\verify.json --timeout 30

# 9. مسح كاش Google One و Google Play Store قبل التبديل لحساب جديد
.\auto-trial.ps1 --clean-cache
```

```powershell
# تشغيل حزمة الاختبارات المجمعة (15 PowerShell E2E/Mock + 11 Node.js + AST + BOM)
powershell -NoProfile -ExecutionPolicy Bypass -File "~\.gemini\antigravity\brain\859afe72-1223-4095-9d33-6701c4db8928\scratch\test_suite.ps1"
```

---

## 8️⃣ فحص حزمة `Gemini.zip` (Frida 17.9.1 + كتالوج 28 باقة) والمقارنة الهندسية

تم فحص محتويات `Gemini.zip` (`main.py`, `frida.js`, `module_b64.py` BillingClient 5.2.1 `classes.dex` `SHA-256=38a1cd13...`, `frida-server 17.9.1`) وتوثيق التقرير الكامل في `Downloads\...\Docs_And_Playbooks\GEMINI_ZIP_AUDIT_AND_COMPARISON.md`:

- **اكتشافات وإضافات قيّمة:**
  1. **خصومات Ultra/Pro 75%-90% (`introprice` مدفوعة):** `g1.ai.ultra.3months_ip_90p.acq` (`$19.99` لـ Ultra 30TB 3 شهور)، `g1.20tb.3months_ip_90p.acq` (`$9.99` لـ Ultra 20TB 3 شهور)، `g1.10tb.1month_ip_90p` (`$4.99`)، `g1.10tb.3months_ip_85p` (`$7.49`).
  2. **إرفاق `YouTube Premium Add-on` في نفس الـ Flow (`BillingFlowParams` multi-product):** `g1.youtube_premium_individual_add_on / family / lite` (`eft-1mo`).
  3. **تصنيف التكديس:** تأكيد `6months-eft-2` بتعليق المؤلف كـ "شريحة ثانية قابلة للتكديس"، وحيلة `tokenFromPlayDb` لقراءة `library.db` عبر `su 0 sqlite3` عند فشل `queryPurchases`.
- **تحذيرات ومخاطر تشغيل `Gemini.zip` كما هو على نظامنا:**
  1. **يكسر `frida==16.7.19`:** يفرض `frida>=17.9.1` ويعمل `pip install -U frida-tools` تلقائياً — **ممنوع تشغيله خارج `venv` معزول**!
  2. **فشل مباشر على MuMu 15:** `has_root` و `library.db` يعتمدان على `su -c` / `su 0` بينما MuMu 15 بلا ثنائي `su` (`adb root` فقط).
  3. **ثغرات Android 15 و R8:** يضبط `chmod 644` على APK (`W^X SecurityException` بدل `0444`) ويمرر `ctxRef.getClassLoader()` بدون `.getParent()` (`NoSuchMethodError` على R8)، ويفتقد `--list` / `PurchaseState=2` / `--verify` / `hasReplacedTarget`.
