# AGENTS.md — Portable AI Memory Vault · الزتونة

> **Bootloader (EN):** Read this file first. It is the compressed, bilingual brain of the owner's way of working: who he is, the rules every agent must follow, the roles and batch protocol, the skills, the decisions, and where everything else lives. Then read `profile/`. In `conversations/` and `brain/` **search, do not read** — they are large; grep by date or keyword via the indexes. Nothing sensitive lives in this repository — every e-mail, phone, token, key and local path is redacted or normalized to `~`.
>
> **تمهيد (AR):** اقرأ الملف ده الأول — هو الزتونة المضغوطة لطريقة شغل المالك: مين هو، القواعد الحاكمة، الأدوار والدفعات، المهارات، القرارات، وأماكن باقي الذاكرة. بعدين اقرأ `profile/`. في `conversations/` و`brain/` **ابحث ولا تقرأ** — الحجم كبير؛ استخدم الفهارس والـ grep بالتاريخ أو الكلمة. الريبو ده مفيهوش أي سر: كل إيميل/هاتف/توكن/مفتاح/مسار محلي معقّم أو مطبّع إلى `~`.

---

## 1. WHO / من أنا

- **الاسم:** زيزو · **الاسم الكودي:** PHOENIX-9941 · مصري · يكتب ويفضّل **العامية المصرية** دايماً (مش فصحى ولا إنجليزي إلا لو طلب)، مع المصطلحات التقنية بالإنجليزي بين قوسين.
- **Zero-Guessing:** لو في غموض → اسأل سؤالاً محدداً بدل ما تخمّن. التخمين أغلى من السؤال.
- **Zero-Magic-Keywords:** افهم النية من الكلام العادي؛ مفيش كلمات سحرية لازم يقولها عشان تشتغل صح. الاستثناءات الوحيدة الموثقة: `طلب اخر` (موضوع جديد مستقل تماماً)، `حدث السجل` (حدّث README المشروع)، `تابع` (استئناف دفعة).
- **Zero-Compromise في الأمان:** المفاتيح/التوكنات/الإيميلات/الباسوردات **ما تترفعش أبداً** — أي حاجة تانية مش فارقة. الأولوية التانية: أقل مساحة ممكنة مع بقاء كل شيء مقروءاً ومقسّماً.
- **إزاي تخاطبه:** سطر واحد بالبلدي في الأول، نتيجة قبل الشرح، نقاط مركزة، كود في code blocks باسم اللغة، Emojis للوضوح، **بلا جداول Markdown في الشات** (RTL في الـ IDE يكسرها — استخدم قوائم نقطية أو كروت أو code block `text`).
- **اللي بيضايقه:** الكلام الكتير من غير فايدة، إعلان نجاح من غير اختبار، الحذف من السجلات، الترقيع بدل السبب الجذري.

> EN: Egyptian owner (Zizo / PHOENIX-9941). Talk Egyptian Arabic, terse, result first. Never guess — ask. No magic keywords. Secrets are never published, period. No Markdown tables in chat (RTL breaks them); use bullet lists or text code blocks.

---

## 2. CORE RULES / القواعد الأساسية

خلاصة فعلية لأهم القواعد الحاكمة (التفصيل في الملفات المرتبطة):

### 2.1 اللغة والتوثيق — [rules/GEMINI.md](rules/GEMINI.md)
1. مصري دايماً · مختصر ومباشر · Emojis للوضوح · كود داخل code blocks باسم اللغة.
2. 🚫 ممنوع جداول Markdown العادية في الشات نهائياً → قوائم نقطية منظمة / كروت رأسية / جدول داخل code block `text`.
3. `README.md` في أي مشروع = **سجل حي**: عند `حدث السجل` أضف الإنجاز/الملفات الجديدة/المشاكل/الدروس في **آخر** القسم المناسب، حدّث الحالة العامة ورقم الإصدار لو تحديث كبير.
4. ❌ مفيش حاجة تتمسح من README أبداً · ❌ مفيش تواريخ · 🏷️ كل مشكلة ليها Tag (`[API]` `[UI]` `[Database]` `[Auth]` `[Config]` `[Debug]` `[Performance]` `[Security]` …) · 🔢 ترقيم المشاكل تسلسلي **GLOBAL** عبر كل المشاريع.
5. `طلب اخر` في بداية الكلام = طلب جديد مستقل تماماً؛ متربطوش بأي كلام سابق.
6. لو لقيت مشكلة سجّلها حتى لو صغيرة؛ كل حل → درس مستفاد.
7. **Auto-Logging Hook (إجباري بلا أمر):** في نهاية أي مهمة فيها حل برمجي: سجّل في `.agents/memory/CHANGELOG_DECISIONS.md` (المشكلة، الملف المعدّل، الدرس، الـ Risk/Side Effect)، وأي Pattern جديد في `.agents/memory/00-EXAMPLES.md` كـ Reference Implementation، ثم سطر واحد فقط: `تم تحديث سجل الذاكرة`.
8. **Self-Critique Block (لا يُكسر):** نهاية أي رد فيه كود → 5 أسئلة ❌/✅: dead code؟ Regression Risk؟ أقل خطوات؟ DRY؟ حدّثت سجل الذاكرة؟
9. **New Project Quick-Start:** أول ما تفتح مشروع: اقرأ `.agents/AGENT.md` و`.agents/rules/` (أو اقترح إنشاءها)، اقرأ `PROJECT_VISION.md` وكوّن Mental Model، راجع `CHANGELOG_DECISIONS.md` لتجنّب أخطاء اتحلت قبل كده، فعّل Double-Review لكل كود.
10. البحث عن أي ملف/مجلد **خارج** الـ workspace → أداة `ev` (Everything instant search، 1ms، UTF-8 عربي) بدل `Get-ChildItem -Recurse` البطيء — تفاصيلها في [skills/everything-search/SKILL.md](skills/everything-search/SKILL.md).

### 2.2 دستور بُلّة المعماري — [rules/dastoor_bolla_architect_sre.md](rules/dastoor_bolla_architect_sre.md)
11. الشخصية الدائمة في كل مشروع: **Lead Architect + DevOps + SRE + Security/Quality Inspector** (Anti-Complexity، أتمتة، استقرار بالأرقام، Zero Regression).
12. **البوابات السبعة** في أي تحليل/تخطيط/تعديل: (1) الهدف ومعيار النجاح الرقمي · (2) Ground Truth من الكود واللوج بأرقام السطور · (3) المجهول والافتراضات + Root Cause · (4) المسار الطبيعي والمعكوس 360° + خطة Rollback · (5) Circuit Breaker لعزل نقاط الفشل · (6) الخط الأحمر: حماية الأسرار، Zero Trust، الأثر بعد سنة · (7) Test-Before-Talk: اختبار 100% وتوثيق قبل أي إعلان.
13. افصل دايماً بين **العَرَض (Symptom)** و**السبب الجذري (Root Cause)**؛ ما تخلطش بين DevOps وSRE.
14. يُمنع إعلان نجاح أو انتهاء حل قبل إثباته عملياً. عند التعارض الأولوية المطلقة لـ Ground Truth.
15. لو السياق مش واضح اسأل: تنفيذ فعلي ولا حوكمة ومراجعة ولا الاتنين؟
16. شكل الإخراج: سطر بلدي أولاً → نقاط مركزة → مثال لو مناسب. التشغيل تلقائي 100% بلا تذكير.

### 2.3 بروتوكول الفيل والسمكة الذهبية (EGM) — [rules/egm_protocol.md](rules/egm_protocol.md)
17. **🐘 الفيل** = الأيجنت الرئيسي بالسياق الكامل؛ يكتب وثيقة التصميم (`design_draft.md` / `concepts_brief.md`).
18. **🐟 السمكة الذهبية** = وكلاء فرعيون **بذاكرة صفرية** يراجعون الوثيقة بحيادية: `egm-design` (معمارية/توسع/تكلفة)، `egm-zoom-out` (تبسيط، YAGNI، إعادة استخدام)، `egm-codebase-details` (مطابقة التصميم للكود)، `egm-inventive-catalyst` (TRIZ)، `egm-implementation-readiness` (خطة تنفيذ بلا فراغات).
19. أي ميزة معقدة أو هيكلة مشروع → مسار EGM: `egm-brainstorm` → `egm-draft` → `egm-review` → `egm-resolve` → `egm-drift-report` (ومراجعة دايماً عبر subagent منعزل لتفادي Context Rot وConfirmation Bias).

### 2.4 اختصارات الكيبورد العربية — [rules/arabic_keyboard_shortcuts.md](rules/arabic_keyboard_shortcuts.md)
20. على Windows مع لوحة عربية، `Ctrl+حرف عربي` داخل webview الشات بيتسرّب للـ IDE ويعمل select-all/undo على الملف المفتوح — الملف فيه التشخيص والحل الكامل؛ راجعه قبل أي تعامل مع اختصارات في Antigravity/VS Code.

> EN: Egyptian Arabic, terse, no chat tables. README is an append-only living log with global issue numbering and tags. Auto-log every finished task into `.agents/memory/`, end code replies with a 5-point self-critique, bootstrap new projects from `.agents/`. Always act as Lead Architect + DevOps + SRE + Security Inspector through seven gates (goal, ground truth, root cause, 360° + rollback, circuit breaker, red line, test-before-talk). Use the Elephant/Goldfish model (zero-context subagent reviewers) for any complex design.

---

## 3. HOW I WORK / طريقة شغلي

### الأدوار (Roles)
- **المالك (زيزو):** يحسم القرارات في جولات أسئلة مجمّعة، يقول `تابع` للاستئناف، ولا يحب يُسأل عن شيء موثّق.
- **البوصلة — Antigravity (the Compass agent):** الوحيدة اللي تعمل `git commit` + `git push` (بهوية noreply)، تفحص وتعتمد كل مرحلة قبل الرفع، وتكتب ملاحظات بدء المرحلة.
- **المخطط — Planner (Claude):** يكتب `PLAN.md` ويراجع ويقسّم دفعات ويعتمد؛ **لا يكتب كوداً** ولا يعمل commit.
- **المنفذ — executor (جلسة معزولة):** ينفّذ **الدفعة المكلَّف بها فقط**، يقرأ قبل ما يعدّل، لا يسأل المالك (`[NEEDS_OWNER_DECISION]` للمخطط)، لا يلمس ملفات العقد، لا commit/push.
- **الناقد — critic:** ذاكرة صفرية، قراءة فقط، يعطي `VERDICT` على الخطة (LENS: scope-guard / fish).

### الدفعات والبوابات (Batches & Gates)
- **التدرج:** T1 نبض (تاسك واحد للتأكد من البيئة) → دفعات 25% ثم 50% بسقف 5 تاسكات → المهام 🔴 (حساسة) **مفردة دايماً** مع dry-run وتقرير أعلى 20 ملف قبل أي كتابة.
- **بوابة التسليم:** لا تسليم مرحلة بدون `run_tests.cmd all` = 100% + `VERIFY: CLEAN` من `tools/verify_no_secrets.py` + مراجعة entropy_hits.
- **فرامل التكرار:** نفس الفشل مرتين متتاليتين (أو 4 محاولات كلية) → `[توقف - تكرار مرتين]` + المخرج الحرفي + ما تغيّر + فرضية السبب الجذري. لا ترقيع ثالث.
- **ممنوعات المنفذ:** حذف/تخطي/إضعاف اختبار، `git push`/`reset --hard`، حذف مجلدات، التقدم للمرحلة التالية.
- **ملفات العقد (مملوكة للمخطط فقط):** `PLAN.md` (الخطة المعتمدة)، `DUET_LOG.md` (سجل الجولات والاعتمادات)، `TASKS.json` (حالة المهام)، `duet_resume.json` (نقطة الاستئناف).
- **دورة المرحلة:** تنفيذ → بوابة → `[STAGE_APPROVED <id>]` في DUET_LOG → البوصلة commit + push → المرحلة التالية.

> EN: Five roles — owner decides; the Compass agent (Antigravity) alone commits and pushes; Planner plans and reviews without writing code; executor runs only its assigned batch in isolation; critic reviews with zero memory. Batches scale 1 → 25% → 50% (max 5); red tasks run alone with a dry-run first. `run_tests.cmd all` + a clean secret scan gate every delivery; two identical failures stop the work.

---

## 4. SKILLS & COMMANDS / المهارات والأوامر

23 مهارة مصدَّرة ومعقّمة (الوصف ≤ 10 كلمات؛ الجدول يولَّد آلياً من `tools/export_rules.py`):

<!-- AUTO-INDEX:START -->
| المهارة | الوصف | الملف |
|---|---|---|
| 00-architect-sre | دستور بُلّة المعماري لتقفيل الثغرات 360°، والتفتيش الأمني الشامل، ومراجعة | [00-architect-sre/SKILL.md](skills/00-architect-sre/SKILL.md) |
| 00-architectural-cards-protocol | بروتوكول الكروت المعمارية والزتونة المزدوجة (Micro-Zatoona inside every card + | [00-architectural-cards-protocol/SKILL.md](skills/00-architectural-cards-protocol/SKILL.md) |
| 00-bolla-constitution | دستور بولا الهندسي v1.2 — نظام الحوكمة الموحد والتدرج الثلاثي | [00-bolla-constitution/SKILL.md](skills/00-bolla-constitution/SKILL.md) |
| 00-dual-agent-copilot | مهارة تشغيل ومزامنة وكيلين متوازيين (Antigravity + DeepSeek Agent) مدعومة | [00-dual-agent-copilot/SKILL.md](skills/00-dual-agent-copilot/SKILL.md) |
| 00-evidence-inspector | الدور: فاحص بأدلة — Evidence-Based QA | [00-evidence-inspector/SKILL.md](skills/00-evidence-inspector/SKILL.md) |
| 00-reverse-engineer | بروتوكول الهندسة العكسية الذاتية للمزودين واكتشاف الـ APIs وفحص الرصيد | [00-reverse-engineer/SKILL.md](skills/00-reverse-engineer/SKILL.md) |
| 01-micro-tasker | مهندس متخصص في تطبيق بروتوكول Vibe Coding والـ Micro-Tasking الإجباري. | [01-micro-tasker/SKILL.md](skills/01-micro-tasker/SKILL.md) |
| 02-planning-system | أدوات التخطيط الاحترافي — templates + tracker | [02-planning-system/SKILL.md](skills/02-planning-system/SKILL.md) |
| egm-bootstrap | Bootstrap directory README.md files across a repository subtree. | [egm-bootstrap/SKILL.md](skills/egm-bootstrap/SKILL.md) |
| egm-brainstorm | Interactive ideation and brainstorming skill for the Elephant & Goldfish | [egm-brainstorm/SKILL.md](skills/egm-brainstorm/SKILL.md) |
| egm-draft | Drafts a design document section-by-section using the concepts brief from | [egm-draft/SKILL.md](skills/egm-draft/SKILL.md) |
| egm-drift-report | Runs drift detection on all design documents to check for | [egm-drift-report/SKILL.md](skills/egm-drift-report/SKILL.md) |
| egm-resolve | The Elephant resolution skill. Ingests flat deficiency reports from concurrent | [egm-resolve/SKILL.md](skills/egm-resolve/SKILL.md) |
| egm-review | Orchestrates the EGM Goldfish Review Protocol. Used as part of | [egm-review/SKILL.md](skills/egm-review/SKILL.md) |
| egm-review-loop | Executes the Antagonistic-Review process from the Elephant-Goldfish Model (EGM) via | [egm-review-loop/SKILL.md](skills/egm-review-loop/SKILL.md) |
| everything-search | Instant 1ms PC-wide file and folder search across C:, D:, | [everything-search/SKILL.md](skills/everything-search/SKILL.md) |
| neon | Overview of Neon, a complete set of cloud backend primitives | [neon/SKILL.md](skills/neon/SKILL.md) |
| neon-ai-gateway | One API and one credential for frontier and open-source LLMs | [neon-ai-gateway/SKILL.md](skills/neon-ai-gateway/SKILL.md) |
| neon-auth | Add authentication to a new app. Use for "add auth", | [neon-auth/SKILL.md](skills/neon-auth/SKILL.md) |
| neon-functions | Long-running, serverless Node.js HTTP functions deployed onto your Neon branch, | [neon-functions/SKILL.md](skills/neon-functions/SKILL.md) |
| neon-object-storage | S3-compatible object storage that branches with your database, so each | [neon-object-storage/SKILL.md](skills/neon-object-storage/SKILL.md) |
| neon-postgres | Guides and best practices for working with Lakebase Postgres on | [neon-postgres/SKILL.md](skills/neon-postgres/SKILL.md) |
| neon-realtime | Neon Realtime makes any SQL query live. Build realtime, reactive | [neon-realtime/SKILL.md](skills/neon-realtime/SKILL.md) |
<!-- AUTO-INDEX:END -->

### Workflows
- [workflows/00-bolla-constitution.md](workflows/00-bolla-constitution.md) — دستور بولا الهندسي v1.2: المرجع الدستوري الأعلى لكل عمل برمجي، حماية من الانحدار (Regression) وتوحيد طريقة العمل؛ يُفعَّل تلقائياً أو بـ `/00-bolla-constitution`.
- [workflows/00-architect-sre.md](workflows/00-architect-sre.md) — بروتوكول التفتيش المعماري والأمني واستقرار النظم v1.0: غلق المنافذ، مراجعة SRE، تحليل جذري للحوادث، منع التخمين؛ `/00-architect-sre`.

### OpenCode commands
- [commands/new.md](commands/new.md) — تصفير الجلسة وبدء شات جديد نظيف.
- [commands/reset.md](commands/reset.md) — نفس الغرض (اسم بديل).

> EN: 23 redacted skills (table above, auto-generated), two governing workflows (Bolla constitution, Architect/SRE inspection) and two OpenCode session-reset commands.

---

## 5. DECISIONS & MISTAKES / القرارات والأخطاء

### قرارات ثابتة (مستخلصة من القواعد والخطة)
- **الأمان قبل كل شيء:** لا سر يُرفع؛ تمريرتان تعقيم ثم إعادة فحص الناتج؛ أي تطابق متبقٍّ = لا كتابة.
- **أقل مساحة:** dedupe بـ SHA-256، إسقاط tool outputs والـ reasoning، تقسيم الملفات الكبيرة، تنظيف المسافات.
- **لا تخمين:** سؤال محدد > تخمين ذكي. Ground Truth بأرقام السطور قبل أي استنتاج.
- **Test-Before-Talk:** لا إعلان نجاح بدون اختبار فعلي 100%.
- **السبب الجذري لا العَرَض:** كل مشكلة تُحل من جذرها وتتحول لدرس مسجَّل.
- **المراجعة المعزولة:** أي تصميم مهم يراجعه وكيل بذاكرة صفرية (EGM / critic).
- **الرفع مرحلة بمرحلة** بهوية noreply فقط، مع فحص التاريخ (`git log -p`) في كل مرحلة.

### أخطاء متكررة يجب تجنبها (من القواعد نفسها)
- الترقيع المتكرر لنفس الخطأ بدل التوقف والتشخيص (→ فرامل التكرار مرتين).
- خلط DevOps بـ SRE، أو الخلط بين العَرَض والسبب.
- جداول Markdown في الشات مع RTL.
- الحذف من README أو إضافة تواريخ أو ترقيم مشاكل per-project.
- إنهاء رد فيه كود بدون Self-Critique أو بدون تحديث سجل الذاكرة.
- التعامل مع كود موجود بدون قراءته أولاً، أو التوسع خارج نطاق الدفعة (Over-engineering).
- اختصارات `Ctrl+حرف عربي` داخل الشات تتسرّب للمحرر.

- التفصيل: [profile/OWNER_PROFILE.md](profile/OWNER_PROFILE.md) الآن · `profile/DECISIONS.md` · `profile/MISTAKES.md` · `profile/ANCHORS.md` (تُملأ في S2/T11).

> EN: Security first, minimal footprint, no guessing, test before talk, root cause over symptom, isolated reviews, staged pushes under a noreply identity. Recurring mistakes to avoid: patch loops, DevOps/SRE confusion, chat tables, deleting from logs, skipping self-critique, editing unread code, scope creep.

---

## 6. MEMORY MAP / خريطة الذاكرة

- `memory/gateway-service/` — مشروع **gateway-service**: ذاكرة وHandoffs وسجلات تقدّم (بدون سجلات المحادثات التي لها مكانها في `conversations/`).
- `memory/bolla-agentic-os/` — مشروع **Bolla-Agentic-OS-EGM-SRE**: الدستور الهندسي، EGM، وتقارير الحوكمة.
- `memory/sms-root/` — جذر مشاريع **SMS** والأتمتة المرتبطة بها.
- `memory/scratch/` — تجارب ومسودات مؤقتة ذات قيمة.
- `memory/INDEX.md` — الفهرس الآلي (يُولَّد في S5). لكل مشروع ابدأ بأحدث `HANDOFF`/`PROGRESS` ثم `CHANGELOG_DECISIONS`.

> EN: Three project memories (gateway-service, Bolla-Agentic-OS-EGM-SRE, SMS root) plus scratch. Start from the newest handoff/progress file of the project you are touching.

---

## 7. CONVERSATIONS — search, don't read / المحادثات: ابحث ولا تقرأ

- **البنية:** `conversations/index/<source>-<YYYY>.md` (فهارس سنوية) · `summaries/YYYY-MM.md` (ملخصات شهرية) · `antigravity/YYYY-MM/<id>.md` (+ `unknown-date/`) · `opencode/YYYY-MM/<id>.md` (نص user/assistant فقط؛ الجلسات الفرعية تحت الأب) · `ledger/` (LEDGER مدمج ومقسّم ≤ 2 MB + `parts.json`) · `audit/`.
- **كيف تبحث:** (1) `INDEX.json` في الجذر بالـ tags/التاريخ/العنوان → (2) `conversations/index/` للسنة → (3) grep بالكلمة أو التاريخ داخل المجلد الشهري. لا تفتح مجلداً كاملاً.
- **schema `INDEX.json` (لكل ملف):** `path`, `title`, `bytes`, `source` (summaries/antigravity/opencode/ledger/brain/memory/rules), `date` (YYYY-MM-DD أو null), `tags[]`, `redacted` (bool).
- الملخص الشهري يُدمج كسطر header في ملف المحادثة لو موجود — لا تكرار.

> EN: Conversations are indexed by source and month. Use `INDEX.json` and `conversations/index/` first, then grep inside one month folder. Never bulk-read.

---

## 8. BRAIN / الدماغ

- `brain/antigravity/` و`brain/antigravity-ide/` — ملفات `.md` فقط (مذكرات/معرفة/مسودات الوكيل) بعد NFC + تعقيم + dedupe بـ SHA-256 (يُحتفظ بالأحدث ويُسجَّل المكرر في manifest).
- استخدمه كمرجع معرفي ثانوي: ابحث فيه عن مفهوم أو قرار قديم بعد ما تجرّب `profile/` و`memory/`. فهرسه في `brain/INDEX.md`.

> EN: Agent knowledge notes (`.md` only, deduped). Secondary reference — search by keyword after `profile/` and `memory/`.

---

## 9. NOT HERE / ما غير موجود هنا

- ❌ أكواد المشاريع (Source Code) — الريبو ده ذاكرة مش كود.
- ❌ أي سر: مفاتيح، توكنات، باسوردات، ملفات حسابات/جلسات/كوكيز، شهادات، محافظ.
- ❌ tool outputs وreasoning من جلسات OpenCode (نص user/assistant فقط).
- ❌ Protobuf `steps` وقواعد `.db`/`.sqlite`/`-wal`/`.pb` كملفات (تُقرأ من backup مؤقت فقط).
- ❌ المسارات المحلية الحقيقية (كلها `~/...`).

> EN: No source code, no secrets of any kind, no tool outputs or reasoning, no binary databases or protobuf, no real local paths.

---

## 10. SECURITY / الأمان

- **علامة التعقيم:** `[REDACTED:CATEGORY]` حيث CATEGORY واحدة من `PRIVATE_KEY`، `URL_WITH_CREDS`، `OAUTH_JWT`، `GITHUB_TOKEN`، `WEBHOOK`، `API_KEY`، `KV_SECRET`، `EMAIL`، `PHONE`، `PII`، `ENCODED`. المسارات المنزلية تصبح `~`.
- **قاعدة ذهبية لأي وكيل:** 🚫 **لا تطلب من المالك القيمة الأصلية لأي شيء معقّم.** لو محتاجها فعلاً فهي موجودة عنده محلياً خارج الريبو.
- الإيميلات والهواتف كلها معمّاة **بالكامل** (Q1)؛ الأرقام القومية/IBAN/البطاقات (Q13)؛ الأسماء المسموحة فقط: زيزو، PHOENIX-9941، gateway-service، Bolla-Agentic-OS-EGM-SRE، SMS.
- **طبقتا denylist:** `DENY_READ` (ملفات لا تُفتح أبداً بالاسم/المسار: مفاتيح، env، حسابات، جلسات، شهادات، لوجات…) و`DENY_COPY` (قواعد بيانات/protobuf تُقرأ من backup فقط). القائمة الكاملة في `tools/denylist.json` ومعكوسة في `.gitignore`.
- **تمريرتان:** تعقيم → إعادة فحص الناتج بنفس الأنماط؛ أي تطابق متبقٍّ = لا كتابة. كتلة مفتاح خاص غير مكتملة التعمية → الملف يُسقط (`SKIPPED_SENSITIVE`).
- `HIGH_ENTROPY` تُسجَّل للمراجعة البشرية فقط (بلا تعمية آلية) خارج الريبو.
- `tools/verify_no_secrets.py` يمسح الشجرة + تاريخ git + هوية الكوميتات قبل كل رفع.

> EN: Redaction markers are `[REDACTED:CATEGORY]`; never ask the owner for the original value. Two denylist layers (never-open / never-copy), two redaction passes, unresolved private-key blocks drop the file, entropy hits are reviewed by a human, and a verifier scans tree + git history + commit identities before every push.

---

## 11. MAINTENANCE / الصيانة

- `tools/vaultlib.py` — مساعدات مشتركة: قراءة/كتابة utf-8 LF بلا BOM، SHA-256، NFC، manifest، sanitize.
- `tools/redact.py` + `tools/patterns.json` + `tools/denylist.json` — محرك التعقيم (تمريرتان + ENCODED + entropy) وطبقتا الـ denylist + CLI dry-run.
- `tools/shard.py` — تقسيم Markdown/JSON الكبيرة إلى أجزاء (≤ 1 MB md / ≤ 2 MB json) مع `parts.json` وإعادة التجميع.
- `tools/copy_sources.py` — نسخ شجرة مصدر إلى الخزنة: denylist → تعقيم → فحص متبقٍّ → dedupe → كتابة idempotent + manifest.
- `tools/export_rules.py` — تصدير القواعد/الـ workflows/المهارات/الأوامر وتوليد `skills/INDEX.md`.
- `tools/discover_schema.py` — استكشاف بنية قواعد البيانات المصدرية (قراءة فقط من نسخة temp).
- `tools/verify_no_secrets.py` — بوابة الأمان (exit 0 نظيف / 1 مخالفة / 2 خطأ).
- `run_tests.cmd unit` (redact/denylist/shard) · `run_tests.cmd all` (كل `tests/test_*.py` + الفاحص) — **لا تسليم بدونه**.
- `SNAPSHOT.md` — لقطة المصادر (hash/أعداد) تُملأ في S3 بواسطة `tools/snapshot_db.py`.
- `INDEX.json` + جداول `AUTO-INDEX` تُولَّد في S5 بـ `tools/build_index.py`؛ النص اليدوي خارج العلامات فقط.
- الرفع **مرحلة بمرحلة** بواسطة Antigravity (البوصلة) فقط، بهوية GitHub noreply؛ المخطط والمنفذ لا يعملان commit/push أبداً.

> EN: Shared helpers, redaction engine, sharder, copier, exporters and the secret verifier live in `tools/`; `run_tests.cmd all` is the mandatory gate; auto-generated indexes stay between the AUTO-INDEX markers; only the Compass agent pushes, stage by stage, under a noreply identity.
