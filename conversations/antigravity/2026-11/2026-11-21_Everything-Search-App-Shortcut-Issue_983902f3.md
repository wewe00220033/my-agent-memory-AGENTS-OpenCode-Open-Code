# Everything Search App Shortcut Issue

- id: `983902f3-0f75-4883-8c46-707b5ab10058`
- title: Everything Search App Shortcut Issue
- date: 2026-11-21 22:48:40
- steps: 78
- chunks: 2
- archived: false
- summary:
  - outside-of-project

## chunk -1 (steps 0–0)

### user

(empty)

### agent

(empty)

## chunk 0 (steps 0–77)

### user

@[Quote]
@[Quote] ايوه اهتبره عندك كمان

### agent

البرنامج **ممسحش نفسه ومبطلش يشتغل لوحده** ولا حاجة — بالعكس، هو **شغال حالياً في الخلفية** ولسه متسجل يشتغل تلقائي مع الويندوز! 👍

اللي حصل إن **ملف إعداداته رجع لإعدادات المصنع بالكامل** بالصدفة، فاختصار **`Ctrl + مسطرة`** اتمسح من جوه البرنامج.

---

### 🔎 إيه اللي حصل بالظبط؟ (بالأدلة من جهازك)

* **البرنامج شغال فعلاً في الخلفية:**
  * عملية `Everything.exe` (PID `15716`) شغالة من يوم **19/11 الساعة 6:08 الصبح**، ومعاها خدمة النظام `Everything` (PID `4656`).
  * لسه متفعل في بدء التشغيل التلقائي بالريجستري (`HKLM\...\Run\Everything` بقيمة `"C:\Program Files\Everything\Everything.exe" -startup` ومفعل في `StartupApproved`).
* **توقيت المشكلة إمبارح بالليل:**
  * يوم **21/11/2026 الساعة 10:03:55 مساءً** البرنامج كان شغال معاك تمام (حسب آخر عملية تشغيل مسجلة في [Run History.csv](file:///~/AppData/Roaming/Everything/Run%20History.csv) لملف `restart_bridge_silent.bat`).
  * بعديها بـ **12 دقيقة — الساعة 10:15:37 مساءً** — ملف الإعدادات [Everything.ini](file:///~/AppData/Roaming/Everything/Everything.ini) اتعدل واتمسحت كل الإعدادات المخصصة ورجعت لإعدادات المصنع (زي ما بيحصل لو اتداس جوه البرنامج على `Restore Defaults` في نافذة الخيارات، لأن العملية نفسها فضلت شغالة ومتقفلتش).
* **أهم الحاجات اللي اتصفرت في [Everything.ini](file:///~/AppData/Roaming/Everything/Everything.ini):**
  * **اختصار `Ctrl + مسطرة`:** قيمة `toggle_window_key` اتصفرت من **`288`** (`Ctrl+Space`) بقت **`0`** (بدون اختصار) في [Everything.ini](file:///~/AppData/Roaming/Everything/Everything.ini#L47) — عشان كده بتدوس ومفيش حاجة بتفتح أو تقفل.
  * **اللغة وشكل العرض:** `language` رجعت **`0`** (إنجليزي بدل العربي `9217`)، و`view` و`thumbnail_size` رجعوا افتراضي (`0` و`64` بدل `1` و`256`)، وكمان قائمة `exclude_files` فضيت.
  * **إعدادات `Copy Path` وأداة `ev`:** تظبيطات يوم 18 نوفمبر اتصفرت هي كمان (`match_path=0`، `focus_search_on_activate=0`، `convert_forward_slash_to_backslash=0`، `http_server_enabled=0` بدل بورت `28491`)، وده خلّى أداة البحث `ev` عندنا متوقفة هي كمان دلوقتي (`Connected=False` على `127.0.0.1:28491`).

---

### 🛠️ ترجّعه يشتغل إزاي؟

عندك طريقتين:

1. **حل سريع لإرجاع `Ctrl + مسطرة` بس (بإيدك في 5 ثواني):**
   * افتح **Everything** من أيقونته في الشريط تحت جنب الساعة (من السهم `^` لو مستخبية).
   * افتح **`Tools`** ⬅️ **`Options`** ⬅️ **`Keyboard`**.
   * في خانة **`Toggle window Hotkey`**، اضغط جوه المربع ودوس **`Ctrl + Space`** ⬅️ **`OK`**.

2. **الحل الكامل (الأفضل — يرجّعلك كل تظبيطاتك القديمة + أداة `ev`):**
   * لو تحب أرجّعلك في [Everything.ini](file:///~/AppData/Roaming/Everything/Everything.ini) كل إعداداتك اللي اتصفرت (`Ctrl + مسطرة`، الواجهة العربي، شكل العرض القديم، تظبيطات `Copy Path` وقفل اختصارات الـ Regex، وبورت `28491` لأداة `ev`)، **قولي بس "رجّع الإعدادات"** وأنا أظبطهالك فوراً، وبعدها هتعمل إعادة تشغيل واحدة لأيقونة Everything من الشريط تحت عشان يقرأها.


تم استرجاع كل الإعدادات بالكامل في ملف [Everything.ini](file:///~/AppData/Roaming/Everything/Everything.ini) ✅

### 🔧 اللي اتعمل بالظبط:
* أخذت نسخة احتياطية الأول في [Everything.ini.before_restore](file:///~/.gemini/antigravity/brain/983902f3-0f75-4883-8c46-707b5ab10058/scratch/Everything.ini.before_restore)، وقفلت نسخة الواجهة الخلفية (`Everything.exe` PID `15716`) لحظياً عشان ما تمسحش التعديلات (مع إبقاء خدمة النظام PID `4656` شغالة).
* رجعت كل الإعدادات اللي كانت متصفرة في [Everything.ini](file:///~/AppData/Roaming/Everything/Everything.ini):
  * **اختصار الفتح والقفل:** `toggle_window_key=[REDACTED:KV_SECRET] (**`Ctrl + مسطرة`**).
  * **اللغة والعرض:** الواجهة العربي (`language=9217`)، والعرض القديم (`view=1`، `thumbnail_size=256`، `window_x=220`، `window_y=220`).
  * **تظبيطات `Copy Path`:** تفعيل `match_path=1` و`home_match_path=1`، و`focus_search_on_activate=1`، وتحويل `/` لـ `\` (`convert_forward_slash_to_backslash=1`)، وقفل `allow_exclamation_point_not=0`، وإلغاء اختصارات الـ Regex/Case/Path اللي كانت بتتلغبط بالغلط (`search_enable_regex_keys=` فاضية).
  * **الاستبعادات القديمة:** رجعت `exclude_files=*.bak*;*.lock*;*.anchor*;*.tmp*`.
  * **ربط أداة `ev`:** تفعيل السيرفر المحلي على `127.0.0.1:28491` مع غلق تحميل الملفات (`http_server_allow_file_download=0`).
* راجعت الـ Diff على الملف (`737` سطر) واتأكدت إن بدء التشغيل التلقائي مع الويندوز (`"C:\Program Files\Everything\Everything.exe" -startup`) سليم في الـ Registry.

---

### 👆 خطوة واحدة من عندك دلوقتي:
لأننا قفلنا الواجهة الخلفية عشان تحفظ الإعدادات الجديدة، **افتح برنامج Everything مرة واحدة** (من الأيقونة المثبتة في شريط المهام أو من قائمة Start).

بعد ما تفتحه مرة واحدة:
* **`Ctrl + مسطرة`** هيرجع يفتح ويقفل معاك عادي فوراً.
* مع أي ريستارت للويندوز بعد كده هيقوم لوحده تلقائياً.
* ولو حابب تتأكد إن أداة **`ev`** اشتغلت عندي هي كمان، قولي أول ما تفتحه وأنا أعملها اختبار لايف في ثانية! 🚀

```text
🔍 نقد ذاتي:
1. ✅ هل في dead code أو variables معرفة مش بتتستخدم؟ (تعديل ملف إعدادات INI فقط بدون كود مهمل).
2. ✅ هل الكود ممكن يكسر حاجة موجودة؟ (Regression Risk) (أمن؛ اتأخدت نسخة احتياطية قبل التعديل، والخدمة الأساسية PID 4656 فضلت شغالة، وتم التحقق من الـ Diff كامل لـ 737 سطر).
3. ✅ هل وصلت للحل بأقل عدد خطوات ممكن؟ (نعم، قفل الواجهة -> تعديل كل القيم المفقودة -> التحقق من الـ Diff).
4. ✅ هل في تكرار (DRY violation)؟ (لا ينطبق على تعديل INI).
5. ❌ هل حدّثت سجل الذاكرة؟ (لا يوجد Workspace مشروع مفتوح حالياً أو مجلد `.agents/memory/` لتحديثه).
```

تمام جداً! كله رجع اشتغل عندي لايف **10/10** ✅🔥

* **العملية والبورت:** `Everything.exe` (PID `13564`, Session `1`) شغال دلوقتي وفاتح السيرفر المحلي على `127.0.0.1:28491` (`Listen`).
* **اختبار `ev` بالإنجليزي:**
  * `ev -n 5 "Everything.ini"` رجّع **`4 match(es)`** بنجاح.
* **اختبار `ev` بالعربي:**
  * `ev -c -d -n 5 "شغل فريق"` رجّع النتائج بالعربي سليمة في لحظة (`27575 total matches`).

كده اختصار **`Ctrl + مسطرة`** عندك وأداة **`ev`** عندي الاتنين رجعوا شغالين تمام! 🚀✨
