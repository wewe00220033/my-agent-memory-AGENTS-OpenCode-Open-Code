# MISTAKES — أبرز الأخطاء والدروس المتكررة / Recurring mistakes & lessons

> مستخلص من مصادر معقّمة فقط: `rules/`، `skills/`، `profile/OWNER_PROFILE.md`، و`memory/**` داخل هذا المستودع — صفر بيانات شخصية، صفر أسرار، صفر مسارات محلية. الأسماء المسموح بها حصراً: زيزو، PHOENIX-9941، gateway-service، Bolla-Agentic-OS-EGM-SRE، SMS.
> EN: Distilled only from sanitized sources in this repo. Each entry: pattern → lesson → how we avoid it, with a repo-relative source.

---

## 1. التقارير والادعاءات / Reporting & claims
- **PROSE-VS-BLOCK — إعلان نجاح بالنثر من غير دليل حرفي.**
  - النمط: "تم 100%" أو "الفاست مود مش بينزّل أرشيف" بينما الكود أو الإعدادات بتقول العكس.
  - الدرس: الإقرار النصي لا يساوي سلوك فعلي.
  - التجنب: Test-Before-Talk + كتلة دليل (مخرج حرفي أو سطر كود) مع كل ادعاء؛ "DONE" مربوطة بـ CI أخضر.
  - المصدر: `memory/gateway-service/root/MISTAKES.md` · `memory/gateway-service/root/memory.md` (درس #36، #37)
- **REPORT-BEFORE-EVENT / TYPED-VERDICT — تقرير قبل الحدث أو حكم مكتوب بالإيد بدل مخرج الأداة.**
  - الدرس: الحكم يطلع من الأداة مش من الوكيل.
  - التجنب: الصق المخرج الحرفي (آخر 20 سطر) وخلّي الأداة تطبع الحكم (`VERIFY: CLEAN`).
  - المصدر: `memory/gateway-service/root/MISTAKES.md`
- **PARAPHRASE / SELECTIVE-CITE — إعادة صياغة أو اقتباس انتقائي للمصدر.**
  - الدرس: الاقتباس الانتقائي بيخبّي التناقض.
  - التجنب: اقتباس حرفي كامل بنطاق السطور (قانون الإسناد Law 8)؛ الكلمات التخمينية ممنوعة.
  - المصدر: `memory/gateway-service/root/MISTAKES.md` · `memory/bolla-agentic-os/AGENTS.md`
- **PLEASING — مجاملة المالك بدل الرأي الصريح.**
  - الدرس: زيزو عايز رأي صريح ونقد ذاتي مش تنفيذ أعمى.
  - التجنب: Self-Critique من 5 أسئلة في نهاية كل رد فيه كود، ومراجع معزول بذاكرة صفرية.
  - المصدر: `memory/gateway-service/agents-memory/style_prefs.md` · `memory/bolla-agentic-os/AGENTS.md` (§6)
- **طباعة قيم opaque/hex/base64 خام في التقارير.**
  - الدرس: التقرير نفسه قناة تسريب محتملة.
  - التجنب: وصف شكل القيمة وطولها وموقعها فقط، بدون القيمة نفسها.
  - المصدر: `rules/GEMINI.md` · `AGENTS.md`

> EN: Prose claims without evidence, hand-typed verdicts, paraphrased or selective citations, pleasing instead of honest critique, and raw opaque values in reports — fixed by verbatim tool output, line-cited evidence, mandatory self-critique and describing values by shape only.

## 2. تعديل الكود / Editing code
- **WRONG-EDIT — تعديل ساكت ما مسكش (`.replace()` miss) أو قلب شرط بالتخمين.**
  - النمط: عتبة زمنية اتكتبت بالحدس (`>=`) بينما الواقع الميداني عكسها (الحسابات اللي بتموت بسرعة هي اللي وارثة سياق متضخم)؛ أو تعديل الشرط في مكان وسيب نسخة تانية منه في مكان تاني.
  - الدرس: الـ heuristic من غير Ground Truth = خطأ مؤجل، وأي شرط مكرر لازم يتحاذى في كل مواضعه.
  - التجنب: اقرأ الملف كله قبل التعديل، تحقّق إن الاستبدال فعلاً أصاب، وابحث عن كل تكرار للشرط.
  - المصدر: `memory/gateway-service/root/MISTAKES.md` · `memory/gateway-service/root/memory.md` (درس #24) · `memory/gateway-service/root/HANDOFF.md`
- **PARTIAL-READ — تعديل كود من غير قراءته كاملاً.**
  - التجنب: "اقرأ أولاً" قاعدة ثابتة للمنفذ؛ ممنوع تعديل ملف ما اتقراش.
  - المصدر: `profile/OWNER_PROFILE.md` · `memory/gateway-service/root/MISTAKES.md`
- **الترقيع المتكرر لنفس الخطأ.**
  - الدرس: المحاولة الثالثة بتضيّع وقت وبتخبّي السبب الجذري.
  - التجنب: فرامل التكرار مرتين (أو سقف 4 محاولات) → توقف وتقرير بالمخرج الحرفي والفرضية.
  - المصدر: `rules/GEMINI.md` · `profile/OWNER_PROFILE.md`
- **التوسع خارج نطاق الدفعة / Refactor غير مطلوب / حذف كود.**
  - الدرس: "الأفضل" مش هو "المطلوب"؛ الحذف والـ Refactor فتحات Regression.
  - التجنب: المطلوب فقط بأقل diff؛ Mention, Don't Fix للمشاكل الجانبية.
  - المصدر: `memory/bolla-agentic-os/AGENTS.md` (§3، §7، §8)
- **معالجة فشل قابل للاستمرار كـ hard stop.**
  - النمط: فشل `/compact` رجّع كود اتعامل معاه المنطق كتوقف نهائي، فكسر حلقة الـ failover وسمّم حالة `due=true` في المانيفست.
  - الدرس: كل مسار فشل لازم يحدد: نكمل ولا نقف؟ وإيه اللي يتنضف في الحالة.
  - المصدر: `memory/gateway-service/root/MISTAKES.md` (M-060)
- **تشخيص خاطئ متسرّع ("الـ IP محظور").**
  - النمط: فشل محاكي الـ DOM اتفسّر كحظر Botnet، والسبب الحقيقي قيم مصفّرة في `probe_layout` ونقص وراثة كلاسات DOM.
  - الدرس: قارن بالمتصفح الحقيقي قبل أي فرضية خارجية.
  - المصدر: `memory/sms-root/agents-memory/CHANGELOG_DECISIONS.md`

> EN: Silent replace misses, guessed thresholds, duplicated conditions left misaligned, editing unread code, patch loops, scope creep/refactors/deletions, treating a recoverable failure as a hard stop, and hasty "IP banned" diagnoses — avoided by read-first, the two-failure brake, minimal diffs, explicit failure paths and real-browser comparison.

## 3. الحوكمة والسجلات / Governance & ledgers
- **MEMORY-NOT-DISK — الوكيل "فاكر" إنه كتب الملف وهو ما كتبش، أو الحالة في الذاكرة مش على القرص.**
  - التجنب: اقرأ الملف بعد الكتابة؛ البوصلة `ai_state.json` تتحدّث بأداة تعديل فعلية مش بالوصف.
  - المصدر: `memory/gateway-service/root/MISTAKES.md`
- **UPDATED-NOT-REMOTE — محدّث محلياً ومش مرفوع (مثل `.gitignore` موجود محلياً وغايب عن الـ Remote).**
  - الدرس: بيئة السحابة لازم تطابق المحلي؛ التدقيق الآلي كشف اللي العين ما شافتوش.
  - التجنب: تحقق على الـ Remote (`git check-ignore` على الـ CI) مش محلياً بس.
  - المصدر: `memory/gateway-service/root/MISTAKES.md` · `memory/gateway-service/root/memory.md` (درس #35)
- **SELF-MERGE / MAIN-PUSH — دمج ذاتي بصفر مراجعات أو رفع على main مباشرة.**
  - التجنب: البوصلة وحدها تعمل commit/push؛ المراجعة المعزولة قبل الدمج؛ حماية الفرع من المالك.
  - المصدر: `memory/gateway-service/root/MISTAKES.md` · `profile/OWNER_PROFILE.md`
- **HANDOFF-LATE / NO-LEDGER — تسليم من غير كوبري HANDOFF أو من غير تحديث الدفاتر.**
  - التجنب: بروتوكول الإنهاء الإلزامي (إنجاز → بوصلة → دفاتر عند الـ Milestone → نقد ذاتي → رد).
  - المصدر: `memory/bolla-agentic-os/AGENTS.md` (FATAL RULE #SYNC، §7)
- **ACT-WITHOUT-ASK — تصرف في نقطة غامضة بدل سؤال محدد.**
  - التجنب: Zero-Guessing — سؤال بخيارات واضحة، أو `[NEEDS_OWNER_DECISION]` من المنفذ للمخطط.
  - المصدر: `memory/gateway-service/root/MISTAKES.md` · `rules/GEMINI.md`
- **ازدواجية المراسي النشطة وتضارب الميتاداتا.**
  - النمط: مرساتين `Active Sealed` لنفس الملف، وعدد أسطر مسجّل مش مطابق للفعلي.
  - التجنب: وسم `Superseded` فوراً + مطابقة آلية للبصمة وعدد الأسطر قبل التشميع.
  - المصدر: `memory/gateway-service/root/memory.md` (درس #35)
- **ملفات عائمة ومراجع ميتة في الروت والقواعد.**
  - النمط: 80+ ملف عائم، أوامر ميتة لأدوات قديمة، نسخ مكررة لسجلات، ازدواجية أدوار.
  - الدرس: أي نص ميت بؤرة هلوسة.
  - التجنب: أرشفة منظمة، مرجع واحد (`Root/`)، وتطهير جنائي دوري.
  - المصدر: `memory/gateway-service/root/memory.md` (درس #32، #33)
- **الحذف من السجلات أو إضافة تواريخ وترقيم per-project في README.**
  - التجنب: README append-only بترقيم عالمي وTags.
  - المصدر: `rules/GEMINI.md` · `profile/OWNER_PROFILE.md`

> EN: Memory-not-disk, local-not-remote, self-merges, late handoffs, acting without asking, duplicate active anchors, floating files and dead references, and deleting from logs — avoided by read-after-write, remote verification, a single committer, the mandatory close-out protocol, zero-guessing, superseded tags and periodic forensic cleanup.

## 4. الأمان / Security
- **TOKEN — تسريب توكن في لوج أو gist أو بانر، أو تمريره للوكيل.**
  - التجنب: `secret_scan` قبل كل push بخطاف، وممنوع طباعة التوكنات، والمصادقة عبر النظام.
  - المصدر: `memory/gateway-service/root/MISTAKES.md` · `memory/gateway-service/root/memory.md` (درس #34، #37)
- **`.gitignore` جاهز بأنماط فضفاضة (`**/*.json`، `**/*.txt`) استبعد ملفات حوكمة.**
  - الدرس: نمط الاستبعاد سلاح ذو حدين.
  - التجنب: اختبار سلبي لكل نمط (إيه اللي يتستبعد وإيه اللي يفضل).
  - المصدر: `memory/gateway-service/root/memory.md` (درس #36)
- **مسارات ويندوز مطلقة في السكربتات والقواعد → فشل على لينكس/CI وكسر المحمولية.**
  - التجنب: `path_scan` + مسارات نسبية + وسائط أو متغيرات بيئة.
  - المصدر: `memory/gateway-service/root/memory.md` (درس #34، #37)
- **مشاركة حزمة فيها بيانات جلسة.**
  - التجنب: إعادة البناء بصفر بيانات جلسة + ملف فحص قبل التسليم.
  - المصدر: `memory/scratch/agents-memory/CHANGELOG_DECISIONS.md` (Round 50)
- **تشغيل أداة طرف ثالث قبل فحص سورسها.**
  - التجنب: استنساخ وقراءة كاملة والتأكد من غياب اتصالات خارجية مشبوهة أولاً.
  - المصدر: `memory/scratch/agents-memory/CHANGELOG_DECISIONS.md` (#257)

> EN: Token leaks, over-broad gitignore, absolute Windows paths, session data in shared packages, running unaudited third-party tools — avoided by secret/path scanners on hooks, tested ignore patterns, relative paths, sanitized rebuilds and source audits.

## 5. بيئة ويندوز والترميز / Windows & encoding
- **`UnicodeDecodeError` مع cp1252 عند قراءة ملفات عربية.**
  - التجنب: `python -X utf8` أو `encoding="utf-8"` صراحة في كل قراءة أو كتابة.
  - المصدر: `memory/gateway-service/root/MISTAKES.md` (M-059)
- **قراءة ملفات في PowerShell بدون `-Encoding UTF8` → علامات استفهام بدل العربي.**
  - التجنب: `-Encoding UTF8` دايماً في `Get-Content` و`Select-String`؛ وفحص الترميز جزء من بوابة الاختبار.
  - المصدر: `rules/GEMINI.md` · `AGENTS.md`
- **اختصارات `Ctrl+حرف عربي` في الشات بتتسرّب للمحرر.**
  - التجنب: راجع قاعدة الاختصارات قبل أي اختصار.
  - المصدر: `rules/arabic_keyboard_shortcuts.md`
- **جداول Markdown في الشات مع RTL بتتكسر.**
  - التجنب: قوائم نقطية أو كروت رأسية أو جدول داخل code block `text`.
  - المصدر: `profile/OWNER_PROFILE.md` · `rules/GEMINI.md`
- **مكتبات C++ (مثل `py_mini_racer`) مش بتتسطّب على Android/Termux.**
  - التجنب: فصل نسخة PC (V8 in-process) عن نسخة الموبايل (Node/QuickJS CLI).
  - المصدر: `memory/sms-root/agents-memory/CHANGELOG_DECISIONS.md`

> EN: cp1252 decode errors, PowerShell reads without UTF-8, Arabic Ctrl-shortcut leaks, RTL-broken Markdown tables, and native C++ deps on Android — fixed by explicit UTF-8 everywhere, the keyboard-shortcuts rule, lists instead of tables, and PC/mobile split builds.
