# ANCHORS — مراسي القراءة السريعة لكل مشروع / Quick reading anchors per project

> مستخلص من مصادر معقّمة فقط: `rules/`، `skills/`، `profile/`، و`memory/**` داخل هذا المستودع — صفر بيانات شخصية، صفر أسرار، صفر مسارات محلية (لو لزم الإشارة لمسار على جهاز المالك يُكتب بصيغة `~` فقط). الأسماء المسموح بها حصراً: زيزو، PHOENIX-9941، gateway-service، Bolla-Agentic-OS-EGM-SRE، SMS.
> EN: Where to start reading for each project (newest HANDOFF/PROGRESS first, then CHANGELOG), with working relative links to the sanitized `memory/**` export plus the reference files in `rules/` and `skills/`.

---

## 0. قاعدة الاستئناف العامة / The resume rule
- ابدأ دايماً بأحدث **HANDOFF** (الحالة الراهنة + خطة الاستئناف + خطة التراجع) → **PROGRESS** (فهرس المراحل) → **CHANGELOG_DECISIONS** (القرارات والمشاكل المحلولة والدروس) → **memory.md / MISTAKES** (الدروس والأخطاء).
- الفهرس الكامل لكل ملفات الذاكرة: [memory/INDEX.md](../memory/INDEX.md).
- المسارات الأصلية على جهاز المالك مش جزء من هذا المستودع؛ لو احتجت تشير لها اكتبها بصيغة `~/...` بس.

> EN: Always HANDOFF → PROGRESS → CHANGELOG → lessons/mistakes. Full file index in `memory/INDEX.md`. Owner-machine paths are never spelled out here.

## 1. gateway-service (أكبر مشروع — بوابة مزوّدي AI وجسور التليجرام)
- **ابدأ هنا:**
  - [root/HANDOFF.md](../memory/gateway-service/root/HANDOFF.md) — آخر كوبري استئناف (الجولة 30: ضغط السياق التلقائي، خطة استئناف من 3 خطوات، وخطة التراجع).
  - [PROGRESS.md](../memory/gateway-service/PROGRESS.md) → [root/PROGRESS.md](../memory/gateway-service/root/PROGRESS.md) — فهرس المراحل P0 → P16.
  - [agents-memory/CHANGELOG_DECISIONS.md](../memory/gateway-service/agents-memory/CHANGELOG_DECISIONS.md) — السجل الضخم للقرارات (مزوّدين، أدوات، تكاملات).
- **الدروس والأخطاء:**
  - [root/memory.md](../memory/gateway-service/root/memory.md) — الدروس المستفادة المرقّمة (الحوكمة #31–#37، Genspark/NoteGPT/Voyage وغيرها).
  - [root/MISTAKES.md](../memory/gateway-service/root/MISTAKES.md) — فهرس الأخطاء بالفئة والحالة.
  - [root/VOICE_LOG.md](../memory/gateway-service/root/VOICE_LOG.md) — تفريغ حرفي للتوجيهات الصوتية (Ground Truth).
- **قواعد التشغيل الخاصة بالمشروع:**
  - [AGENTS.md](../memory/gateway-service/AGENTS.md) · [GEMINI.md](../memory/gateway-service/GEMINI.md) · [README.md](../memory/gateway-service/README.md)
  - [agents-memory/AGENT_RULES.md](../memory/gateway-service/agents-memory/AGENT_RULES.md) + [agents-memory/SYNC_DESK.md](../memory/gateway-service/agents-memory/SYNC_DESK.md) + [agents-memory/LOG.md](../memory/gateway-service/agents-memory/LOG.md) — النظام الثنائي Architect/Worker.
  - [agents-memory/AGENT_SYNC.md](../memory/gateway-service/agents-memory/AGENT_SYNC.md) · [agents-memory/AUTO_APMS_SYNC_RULES.md](../memory/gateway-service/agents-memory/AUTO_APMS_SYNC_RULES.md)
- **الرؤية والقرارات والأسلوب:**
  - [agents-memory/PROJECT_VISION.md](../memory/gateway-service/agents-memory/PROJECT_VISION.md) · [agents-memory/decisions_log.md](../memory/gateway-service/agents-memory/decisions_log.md) · [agents-memory/style_prefs.md](../memory/gateway-service/agents-memory/style_prefs.md) · [agents-memory/provider_knowledge.md](../memory/gateway-service/agents-memory/provider_knowledge.md)
- **تقارير معمارية كبيرة (اقرأها عند الحاجة فقط):**
  - [root/ANCHORS.md](../memory/gateway-service/root/ANCHORS.md) · [root/tasks.md](../memory/gateway-service/root/tasks.md) · [root/GENSPARK_FORK_COMPACTING_FULL_REPORT.md](../memory/gateway-service/root/GENSPARK_FORK_COMPACTING_FULL_REPORT.md) · [root/CLEAN_RESPONSE_ARCHITECTURE_PROPOSAL.md](../memory/gateway-service/root/CLEAN_RESPONSE_ARCHITECTURE_PROPOSAL.md) · [root/COMPREHENSIVE_SCENARIOS_AND_BEHAVIORS_REPORT.md](../memory/gateway-service/root/COMPREHENSIVE_SCENARIOS_AND_BEHAVIORS_REPORT.md) · [root/NOTEGPT_INTEGRATION_PLAN.md](../memory/gateway-service/root/NOTEGPT_INTEGRATION_PLAN.md) · [root/radar_sheet_progress.md](../memory/gateway-service/root/radar_sheet_progress.md)

> EN: Start with root/HANDOFF.md (Round 30), then PROGRESS (P0–P16) and the big CHANGELOG; lessons in root/memory.md, mistakes ledger in root/MISTAKES.md; the dual-agent rules live in agents-memory/.

## 2. Bolla-Agentic-OS-EGM-SRE (الإطار الحاكم — دستور بولا وEGM)
- **ابدأ هنا:**
  - [root/HANDOFF.md](../memory/bolla-agentic-os/root/HANDOFF.md) — كارت الاستئناف (Genesis Baseline، Turn 0).
  - [root/PROGRESS.md](../memory/bolla-agentic-os/root/PROGRESS.md) · [root/tasks.md](../memory/bolla-agentic-os/root/tasks.md)
  - [agents-memory/CHANGELOG_DECISIONS.md](../memory/bolla-agentic-os/agents-memory/CHANGELOG_DECISIONS.md) — القرارات المعمارية #001–#005 (عزل النواة، الذاكرة الحية، Zero Leak، EGM، stdlib فقط).
- **الدستور والقواعد:**
  - [AGENTS.md](../memory/bolla-agentic-os/AGENTS.md) — Living Memory System (FATAL RULE #SYNC، T0/T1/T2، قانون الإسناد، EGM Lifecycle، التجاوزات القاتلة).
  - [GEMINI.md](../memory/bolla-agentic-os/GEMINI.md) · [README.md](../memory/bolla-agentic-os/README.md)
  - [root/memory.md](../memory/bolla-agentic-os/root/memory.md) · [root/ANCHORS.md](../memory/bolla-agentic-os/root/ANCHORS.md)
- **القوالب العامة:**
  - [agents-memory/AGENT_RULES.md](../memory/bolla-agentic-os/agents-memory/AGENT_RULES.md) · [agents-memory/handoff_templates.md](../memory/bolla-agentic-os/agents-memory/handoff_templates.md) · [agents-memory/planning_prompt_master.md](../memory/bolla-agentic-os/agents-memory/planning_prompt_master.md) · [agents-memory/style_prefs.md](../memory/bolla-agentic-os/agents-memory/style_prefs.md) · [agents-memory/00-EXAMPLES.md](../memory/bolla-agentic-os/agents-memory/00-EXAMPLES.md) · [agents-memory/README.md](../memory/bolla-agentic-os/agents-memory/README.md)
- **المرجع الأصلي للدستور في هذا المستودع:** [rules/dastoor_bolla_architect_sre.md](../rules/dastoor_bolla_architect_sre.md) · [rules/egm_protocol.md](../rules/egm_protocol.md) · [skills/00-bolla-constitution/SKILL.md](../skills/00-bolla-constitution/SKILL.md) · [skills/00-architect-sre/SKILL.md](../skills/00-architect-sre/SKILL.md).

> EN: Genesis-state governance kernel: read root/HANDOFF.md, the ADR changelog (#001–#005) and AGENTS.md; the constitution itself is mirrored under rules/ and skills/.

## 3. SMS (الأتمتة — Duck.ai وتطبيقات الدردشة وقياس المزوّدين)
- **ابدأ هنا:**
  - [handoff.md](../memory/sms-root/handoff.md) — المقارنة الحية رأس برأس (6 اختبارات + الحكم النهائي ومصفوفة القرار).
  - [agents-memory/CHANGELOG_DECISIONS.md](../memory/sms-root/agents-memory/CHANGELOG_DECISIONS.md) — الهندسة العكسية لـ Duck.ai (تحدي JSA، أخطاء 418/429، نسخ PC/Mobile/V3)، قرارات Antigravity IDE، وتدفق الأدوات في الـ Gateway.
- **الأرشيف:**
  - [GEMINI_ARCHIVE_2026-09-02.md](../memory/sms-root/GEMINI_ARCHIVE_2026-09-02.md) — أرشيف قواعد وجلسات قديم (للرجوع فقط).
  - [agents-memory/00-EXAMPLES.md](../memory/sms-root/agents-memory/00-EXAMPLES.md)
- ملاحظة: مفيش `PROGRESS.md` أو مجلد `root/` لهذا المشروع في التصدير — الـ CHANGELOG هو السجل الزمني.

> EN: Start with handoff.md (live head-to-head benchmark) and the CHANGELOG (Duck.ai reverse engineering, IDE decisions). No PROGRESS/root ledgers were exported for SMS.

## 4. scratch (تجارب وأدوات مساعدة)
- **ابدأ هنا:**
  - [agents-memory/CHANGELOG_DECISIONS.md](../memory/scratch/agents-memory/CHANGELOG_DECISIONS.md) — إدارة حسابات وبروفايلات Antigravity IDE وChrome، قرارات الدفع والتحقق، الجولات 46–51 (الجسر، الـ daemon، تعقيم الحزم)، وتدقيق أدوات Frida.
  - [agents-memory/GOOGLE_ONE_HYBRID_REFERENCE.md](../memory/scratch/agents-memory/GOOGLE_ONE_HYBRID_REFERENCE.md) — مرجع تقني.
  - [agents-memory/00-EXAMPLES.md](../memory/scratch/agents-memory/00-EXAMPLES.md)
- ملاحظة: مشروع scratch مفيهوش HANDOFF أو PROGRESS — الـ CHANGELOG بترتيب الجولات هو نقطة الدخول.

> EN: Experiments folder; the CHANGELOG (rounds 46–51, IDE/Chrome profile management, Frida tool audit) is the only entry point.

## 5. الملفات المرجعية في هذا المستودع / Repo reference files
- **القواعد:** [rules/GEMINI.md](../rules/GEMINI.md) · [rules/dastoor_bolla_architect_sre.md](../rules/dastoor_bolla_architect_sre.md) · [rules/egm_protocol.md](../rules/egm_protocol.md) · [rules/arabic_keyboard_shortcuts.md](../rules/arabic_keyboard_shortcuts.md)
- **المهارات:** [skills/INDEX.md](../skills/INDEX.md) — وأهمها للحوكمة: [00-bolla-constitution](../skills/00-bolla-constitution/SKILL.md) · [00-architect-sre](../skills/00-architect-sre/SKILL.md) · [00-evidence-inspector](../skills/00-evidence-inspector/SKILL.md) · [01-micro-tasker](../skills/01-micro-tasker/SKILL.md) · [02-planning-system](../skills/02-planning-system/SKILL.md) · [egm-review](../skills/egm-review/SKILL.md) · [egm-review-loop](../skills/egm-review-loop/SKILL.md) · [00-reverse-engineer](../skills/00-reverse-engineer/SKILL.md)
- **البروفايل:** [profile/OWNER_PROFILE.md](OWNER_PROFILE.md) · [profile/DECISIONS.md](DECISIONS.md) · [profile/MISTAKES.md](MISTAKES.md)
- **الدستور العام للمستودع:** [AGENTS.md](../AGENTS.md) · [README.md](../README.md)

> EN: Rules, the governance-related skills, the three profile files and the repo-level AGENTS.md / README.md.
