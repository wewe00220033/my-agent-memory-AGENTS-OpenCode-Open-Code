# DECISIONS — أبرز القرارات الهندسية والأمنية والإدارية / Key engineering, security & management decisions

> مستخلص من مصادر معقّمة فقط: `rules/`، `skills/`، `profile/OWNER_PROFILE.md`، وذاكرة المشاريع المنشورة تحت `memory/**` داخل هذا المستودع — صفر بيانات شخصية، صفر أسرار، صفر مسارات محلية. الأسماء المسموح بها حصراً: زيزو، PHOENIX-9941، gateway-service، Bolla-Agentic-OS-EGM-SRE، SMS.
> EN: Distilled only from the sanitized sources in this repo (`rules/`, `skills/`, `profile/`, `memory/**`). Zero PII, zero secrets, zero local paths. Each decision cites its source as a repo-relative path.

---

## 1. الأمان والتعقيم / Security & sanitization
- **الأسرار في `.env` أو متغيرات البيئة بس** — ممنوع في الكود، ممنوع في البانرات والتيرمينال والـ artifacts والكوميتات. `.env` و`*.env` و`keys.txt` و`*.key` مستبعدة صراحة في `.gitignore`.
  - المصدر: `memory/gateway-service/agents-memory/decisions_log.md` · `memory/gateway-service/root/memory.md` (درس #34)
- **Zero Leak Invariant:** ماسحات regex + مراسي تشفيرية SHA-256 قبل أي رفع لمستودع عام؛ التوكنات والإيميلات وأرقام التليفونات ممنوعة من الدخول للـ Git.
  - المصدر: `memory/bolla-agentic-os/agents-memory/CHANGELOG_DECISIONS.md` (#003) · `memory/bolla-agentic-os/root/memory.md`
- **بوابة حوكمة آلية محمولة** (`.governance/`): `secret_scan` + `path_scan` + `verify_sync` + مسبار سلوكي، مربوطة بخطافات `pre-commit`/`pre-push` وبـ GitHub Actions كجهاز ثانٍ مستقل. التعليمات النصية تُقرأ بانتقائية؛ الفحص الآلي هو الضمان الوحيد.
  - المصدر: `memory/gateway-service/root/memory.md` (درس #37)
- **لا مسارات ويندوز مطلقة في القواعد أو السكربتات** — مسارات نسبية محمولة فقط، والوسائط أو متغيرات البيئة للمسارات الخاصة بالجهاز.
  - المصدر: `memory/gateway-service/root/memory.md` (درس #34، #37)
- **`.gitignore` بأنماط دقيقة لا فضفاضة:** كل نمط يُختبر مرتين (إيه اللي بيستبعده وإيه اللي بيسيبه)؛ ملفات الحوكمة لازم تطلع `NOT_IGNORED` والأسرار `IGNORED`.
  - المصدر: `memory/gateway-service/root/memory.md` (درس #36)
- **الوكيل ما يشوفش التوكن أصلاً:** الاعتماد على مصادقة النظام (مثل `gh auth login`) بدل تمرير توكنات للوكيل.
  - المصدر: `memory/gateway-service/root/memory.md` (درس #37)
- **الحزم المنقولة لغيرك تتعقّم أولاً:** أي ZIP أو حزمة تشغيل تُعاد بناؤها بصفر بيانات جلسة قبل المشاركة، مع ملف فحص `verify`.
  - المصدر: `memory/scratch/agents-memory/CHANGELOG_DECISIONS.md` (Round 49–50)
- **فحص السورس قبل تشغيل أي أداة خارجية:** استنساخ محلي وقراءة السكربتات بالكامل والتأكد من عدم وجود اتصالات خارجية مشبوهة قبل أي تشغيل.
  - المصدر: `memory/scratch/agents-memory/CHANGELOG_DECISIONS.md` (#257)

> EN: Secrets only in env; regex + SHA-256 anchors as a zero-leak invariant; portable automated governance gate (hooks + CI); no absolute Windows paths; tight `.gitignore` patterns tested both ways; agents never see tokens; packages sanitized before sharing; audit third-party source before running it.

## 2. حوكمة الوكلاء والدفعات / Agent governance & batching
- **فصل الأدوار بلا تداخل:** المالك يقرر · البوصلة (Antigravity) وحدها تعمل commit/push · المخطط يخطط ويراجع بلا كود · المنفذ ينفّذ دفعته فقط في عزلة · الناقد بذاكرة صفرية. "اتنين يعدّلوا نفس الملف في نفس الوقت" = الجريمة الكبرى.
  - المصدر: `profile/OWNER_PROFILE.md` · `memory/gateway-service/agents-memory/AGENT_RULES.md`
- **نقطة تلاقي واحدة بين الوكلاء** (`SYNC_DESK.md` / `AGENT_SYNC.md`): المهام بحالات `[OPEN] → [WIP] → [DONE]`، والملفات المقفولة `🔒 LOCKED` ما تتلمسش حتى لو الوكيل متأكد.
  - المصدر: `memory/gateway-service/agents-memory/AGENT_RULES.md` · `memory/gateway-service/agents-memory/AGENT_SYNC.md`
- **تصنيف المخاطر T0/T1/T2:** 🟢 T0 وثائقي · 🟡 T1 جراحي ≤ 10 أسطر مع مرساة وSHA-256 · 🔴 T2 معماري/شبكي/ملف جديد = وثيقة مواصفات + محاكي جاف + موافقة GO صريحة · ☠️ المساس بالأمان أو حذف بيانات = توقف واستشارة زيزو.
  - المصدر: `memory/bolla-agentic-os/AGENTS.md` (§4) · `rules/dastoor_bolla_architect_sre.md`
- **EGM (الفيل والسمكة الذهبية):** الفيل يخطط ويكتب المواصفة ولا يكتب كود في وضع `[PLANNING]`؛ في T2 يُطلق مراجعين معزولين بذاكرة صفرية يراجعوا بلا مجاملة قبل بوابة GO، ثم فحص انحراف Spec-to-Code قبل الـ commit.
  - المصدر: `memory/bolla-agentic-os/AGENTS.md` (EGM Lifecycle) · `rules/egm_protocol.md` · `skills/egm-review/SKILL.md`
- **الدفعات تتدرج:** نبض (تاسك واحد) → 25% → 50% بسقف 5؛ المهام الحساسة 🔴 مفردة مع dry-run وتقرير قبل أي كتابة.
  - المصدر: `profile/OWNER_PROFILE.md`
- **فرامل التكرار مرتين:** نفس الفشل مرتين (أو 4 محاولات) → توقف + مخرج حرفي + ما تغيّر بين المحاولتين + فرضية السبب الجذري. لا ترقيع ثالث.
  - المصدر: `profile/OWNER_PROFILE.md` · `rules/GEMINI.md`
- **Mention, Don't Fix:** أي مشكلة جانبية خارج النطاق تُسجَّل في الذاكرة وتُذكر، ولا تُعدَّل تلقائياً.
  - المصدر: `memory/bolla-agentic-os/AGENTS.md` (§8)
- **قانون الإسناد الحرفي بالسطور (Law 8):** لا ادعاء فني ولا تعديل كود بدون كتلة دليل من HAR حي أو كود المرساة أو مسبار حي أو التوثيق الرسمي؛ الكلمات التخمينية ("غالباً"، "المفروض"، "Probably") = رفض تلقائي.
  - المصدر: `memory/bolla-agentic-os/AGENTS.md` (Verbatim Ground-Truth Citation Law)
- **التطوير التتابعي بترقيم صارم:** `01_x.py` للخطوة الجديدة، `01.02_x.py` لتصحيح نفس الخطوة، `03_sandbox_*.py` للتجارب، مع commit فوري بعد كل خطوة ناجحة.
  - المصدر: `memory/bolla-agentic-os/AGENTS.md` (Sequential Requests v2.0)

> EN: Five non-overlapping roles; one sync desk with OPEN/WIP/DONE and locked files; T0/T1/T2 risk tiers; EGM spec-first review with zero-memory reviewers and a drift check; batches 1 → 25% → 50%; two-identical-failures brake; mention-don't-fix; verbatim line-cited evidence law; strictly versioned sequential scripts.

## 3. بوابات الاختبار والتحقق / Test & verification gates
- **البوابة الواحدة قبل أي تسليم:** `run_tests.cmd all` = 100% + `VERIFY: CLEAN`. "DONE" ما تتقالش إلا لما الـ CI يخضّر على جهاز مستقل.
  - المصدر: `profile/OWNER_PROFILE.md` · `memory/gateway-service/root/memory.md` (درس #37)
- **Test-Before-Talk بمسبار سلوكي:** ما ينفعش إقرار Markdown بإن السكربت اتصلح؛ لازم مسبار آلي معزول يجرّب الحالات الحدية بالأرقام.
  - المصدر: `memory/gateway-service/root/memory.md` (درس #36)
- **مطابقة HAR بالسطور 100%:** مسارات الـ API والـ Headers والـ Payload والـ Response تتطابق مع الكتلة المرجعية قبل اعتماد أي ريكويست.
  - المصدر: `memory/bolla-agentic-os/AGENTS.md` (Sequential Requests)
- **اختبارات التكافؤ بايت-بايت** عند إعادة بناء أجزاء من ملف ضخم، وحزمة اختبارات شاملة (1000+) تمر بالكامل قبل تشميع المرساة.
  - المصدر: `memory/gateway-service/root/HANDOFF.md`
- **المقارنة مع المتصفح الحقيقي هي الـ Ground Truth** لأي محاكاة بروتوكول (تحديات JSA/DOM): لما الـ mock يفشل، قارن بـ dump من Chrome حقيقي قبل ما تفترض "IP محظور".
  - المصدر: `memory/sms-root/agents-memory/CHANGELOG_DECISIONS.md`
- **المقارنات الحية رأس برأس تُوثَّق كاملة** (المهام، الردود، الحكم) في ملف handoff مستقل قبل اتخاذ قرار اختيار مزوّد.
  - المصدر: `memory/sms-root/handoff.md`
- **بطاقة جودة التخطيط ≥ 8/10** + موافقة GO صريحة قبل لمس أي ملف تشغيلي.
  - المصدر: `memory/gateway-service/root/memory.md` (درس #31) · `skills/02-planning-system/SKILL.md`

> EN: One mandatory gate (all tests + VERIFY: CLEAN, CI green on an independent machine); behavioral probes instead of prose claims; 100% HAR parity; byte-parity rebuild tests; real-browser dumps as ground truth for protocol mocks; documented head-to-head benchmarks; planning quality card ≥ 8/10 + explicit GO.

## 4. أسلوب الكود / Code style
- **Python 3.10+ وstdlib أولاً** — صفر اعتماديات pip في أدوات الحوكمة (تم التحقق على Windows / Python 3.12).
  - المصدر: `memory/gateway-service/agents-memory/style_prefs.md` · `memory/bolla-agentic-os/agents-memory/CHANGELOG_DECISIONS.md` (#005)
- **`curl_cffi` بدل `requests`** (بصمة TLS تعدّي Cloudflare)؛ Playwright بس لما السيرفر يربط التوكن بجلسة متصفح؛ الهدف الدائم Zero-Browser.
  - المصدر: `memory/gateway-service/agents-memory/decisions_log.md` · `memory/sms-root/agents-memory/CHANGELOG_DECISIONS.md`
- **النقر عبر CDP `Runtime.evaluate` + `userGesture`** مش `execute_script` (React بيشتغل في الـ main world).
  - المصدر: `memory/gateway-service/agents-memory/decisions_log.md`
- **JSON atomic** (`.tmp` → `replace`) لأي تخزين حالة؛ مفيش `input()` في production؛ مفيش hardcoded values.
  - المصدر: `memory/gateway-service/agents-memory/decisions_log.md` · `memory/gateway-service/agents-memory/style_prefs.md`
- **DRY عبر مكتبة `shared/`** (`step()`, `ok()`, `fail()`) بدل copy-paste؛ `LOOP_MODE` هو الوضع الافتراضي للإنتاج.
  - المصدر: `memory/gateway-service/agents-memory/decisions_log.md`
- **قراءة وكتابة الملفات بـ UTF-8 صراحة** (`-X utf8` أو `encoding="utf-8"`) على ويندوز.
  - المصدر: `memory/gateway-service/root/MISTAKES.md` (MEMORY-NOT-DISK)
- **تعديل جراحي فقط:** الدالة المستهدفة بس؛ كود "مش منسق" لكنه شغال يتساب زي ما هو — الحماية من الـ Regression أولى من التجميل. ممنوع TODO أو Placeholder.
  - المصدر: `memory/bolla-agentic-os/AGENTS.md` (§5، §7، §8)
- **Non-Goals صريحة** لكل مشروع (مثلاً: لا واجهة ويب، لا database — JSON كافي، لا تعقيد زيادة).
  - المصدر: `memory/gateway-service/agents-memory/PROJECT_VISION.md`
- **colorama + fallback + تعليقات عربية**، وبانرات بداية/نجاح في التيرمينال.
  - المصدر: `memory/gateway-service/agents-memory/style_prefs.md`

> EN: Python stdlib first; curl_cffi over requests; browser only when unavoidable; CDP userGesture clicks; atomic JSON; no input()/hardcoding; shared DRY helpers; explicit UTF-8 on Windows; surgical edits only; explicit non-goals.

## 5. بنية الذاكرة والسجلات / Memory & ledger structure
- **النواة الموحدة في `Root/`:** `ai_state.json` (بوصلة فورية بعد كل خطوة) + `PROGRESS.md` + `tasks.md` + `memory.md` + `ANCHORS.md` + `HANDOFF.md` + `keys.txt` (محلي ومستبعد من Git). "Lean Sync": البوصلة فورياً، والدفاتر عند الـ Milestones.
  - المصدر: `memory/bolla-agentic-os/AGENTS.md` (FATAL RULE #SYNC) · `memory/gateway-service/root/memory.md` (درس #35)
- **`.agents/memory/` كذاكرة عامة عبر المشاريع:** `CHANGELOG_DECISIONS.md` (قرارات/مشاكل محلولة/دروس) + `decisions_log.md` + `style_prefs.md` + `LOG.md` + `SYNC_DESK.md`.
  - المصدر: `memory/gateway-service/agents-memory/AGENT_RULES.md` · `memory/gateway-service/agents-memory/decisions_log.md`
- **سجل المراسي وثيقة تشفيرية رسمية:** مرساة واحدة نشطة لكل ملف، أي مرساة مستبدلة تُوسم `Superseded` فوراً، وعدد الأسطر والبصمة يتطابقوا آلياً قبل التشميع.
  - المصدر: `memory/gateway-service/root/memory.md` (درس #35)
- **`README.md` سجل حي append-only** بترقيم مشاكل عالمي وTags، بلا تواريخ وبلا حذف.
  - المصدر: `profile/OWNER_PROFILE.md` · `rules/GEMINI.md`
- **`HANDOFF.md` كوبري الاستئناف** في نهاية كل مرحلة: الحالة الراهنة، ما تم تسليمه، خطة الاستئناف خطوة بخطوة، وخطة التراجع.
  - المصدر: `memory/gateway-service/root/HANDOFF.md` · `memory/bolla-agentic-os/root/HANDOFF.md`
- **سجل الأخطاء مصنّف بالفئة والحالة** (`CAUGHT` / `OPEN` / `OWNER`)، يُولَّد آلياً من دفتر كامل بالأدلة.
  - المصدر: `memory/gateway-service/root/MISTAKES.md`
- **سجل الفويسات الحي (`VOICE_LOG.md`) كمرساة Ground Truth** بتفريغ حرفي للتوجيهات الصوتية.
  - المصدر: `memory/gateway-service/root/memory.md` (درس #25)
- **نظافة الروت شرط مسبق:** الملفات العائمة والمراجع الميتة تُؤرشف في `_archive/`؛ الروت يقتصر على الأساسي — المساحة النظيفة تحمي من الهلوسة.
  - المصدر: `memory/gateway-service/root/memory.md` (درس #32، #33)
- **ذاكرة الـ AI المنشورة (هذا المستودع):** تصدير معقّم لكل مشروع تحت `memory/<project>/`، مانيفست خارج الشجرة المنشورة، ومراجعة بشرية (المخطط) لإصابات الإنتروبيا قبل أي تنقيح إضافي.
  - المصدر: `AGENTS.md` · `memory/INDEX.md`

> EN: Unified `Root/` core (state compass + ledgers + anchors + handoff), cross-project `.agents/memory/`, single active anchor per file, append-only README, handoff bridges per phase, class/status-coded mistakes ledger, voice ledger as ground truth, clean root as a precondition, and this repo's sanitized per-project export.
