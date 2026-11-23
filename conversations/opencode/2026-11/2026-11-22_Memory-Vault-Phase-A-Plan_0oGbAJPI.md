# Memory Vault Phase A Plan

- id: `ses_dfcd3731dffeVslmT00oGbAJPI`
- title: Memory Vault Phase A Plan
- date: 2026-11-22 12:13:01
- directory: my-agent-memory-AGENTS-OpenCode-Open-Code
- agent: planner-reviewer
- model: upstage-studio/claude-fable-5-1-planner
- messages: 1 (user 1, assistant 0)
- archived: false

## 6 · user (2026-11-22 12:13:01)

أهلاً بك يا Planner & Reviewer. أنا **Antigravity (البوصلة)** وأتواصل معك بتكليف مباشر من المالك للعمل معاً في جلسة غير تفاعلية (CLI) لتجهيز مستودع الذاكرة الدائمة الخاص بالمالك.

⚠️ **تنبيه مهم لوضع التشغيل الآن:**
1. أنت الآن في **المرحلة أ (التخطيط والمراجعة المبدئية فقط)** داخل مجلد المستودع النظيف:
   `~\.gemini\antigravity\scratch\my-agent-memory-AGENTS-OpenCode-Open-Code`
2. ممنوع تنفيذ أي سكربتات تصدير أو تعديل ملفات كود أو تشغيل `git push` في هذه المرحلة؛ التزم بملفات التخطيط المسموحة لك فقط (`PLAN.md`, `TASKS.json`, `duet_resume.json`, `DUET_LOG.md`) واستدعاء مراجعة الخطة من `executor` (بدون تعديل كود) أو `critic` إن لزم.
3. لأن الجلسة غير تفاعلية، **لا تستدعِ أداة `question`**؛ بدلاً من ذلك اكتب أي أسئلة أو قرارات تحتاج حسم المالك نصياً في نهاية ردك (وفي `PLAN.md` تحت قسم `## Open Questions for Owner`) وسأنقلها أنا للمالك حرفياً.

---

### 🎯 قرارات المالك المعتمدة (ثابتة بدون تخمين):
1. **الهدف والنطاق:**
   - رفع **الذاكرة القابلة للقراءة والنقل (Portable AI Memory Vault)** إلى مستودع GitHub العام:
     `https://github.com/wewe00220033/my-agent-memory-AGENTS-OpenCode-Open-Code.git`
   - بحيث لو المالك فتح أي محادثة جديدة (في OpenCode أو Antigravity أو أي وكيل ذكاء اصطناعي آخر) أو بعث له رابط المستودع، يقدر الوكيل فوراً يفهم أسلوب المالك، قواعده، مهاراته، قراراته الهندسية، وسجل محادثاته السابقة بدون ما يعيد شرح كل شيء من الصفر.
   - **المستبعد:** لا نرفع أكواد المشاريع نفسها (Source Code) ولا نرفع نسخ الأرشيف المضغوطة المكررة القديمة. نركز فقط على الذاكرة، القواعد، المهارات، الأوامر، الـ Handoffs، وتفريغ المحادثات بشكل مقروء.

2. **الصيغ والتقسيم (Chunking):**
   - الصيغة المستهدفة: ملفات نصية مقروءة (**Markdown `.md` و/أو JSON `.json`**) متوافقة مع OpenCode (`AGENTS.md`, `skills/*/SKILL.md`, `commands/*.md`) ومع أي وكيل آخر.
   - أي ملف أو تفريغ كبير يتم تقسيمه لأجزاء صغيرة مريحة للقراءة والبحث (مثلاً حد أقصى `2–5 MB` للملف الواحد، وأقل بكثير من حد GitHub الصارم `100 MB`).
   - وجود `AGENTS.md` ذكي وخفيف في جذر المستودع يعمل كـ **Index / Bootloader** يوجّه أي وكيل جديد لما يقرأه فوراً بدون حرق الـ Context Window، ويدلّه على مسارات البحث (`grep`/`read`) للمحادثات والأرشيف عند الحاجة.

3. **سياسة الأمان والخصوصية الصارمة (المستودع Public):**
   - استبعاد تام لأي ملفات تحتوي مفاتيح أو توكنات أو إيميلات/حسابات أو كوكيز أو جلسات أو إعدادات خاصة (مثل: `keys.md`, `keys.txt`, `*.env`, `oauth_creds.json`, `google_accounts.json`, `upstage_session.json`, `*accounts*.json`, `*.session`, `*.har`, `ACCOUNT_FUNDING_REGISTER.md`, `service.json`, `unlimited-identity.json`).
   - تطبيق **تنقية وتعمية تلقائية (Automated Sanitization & Redaction)** داخل جميع النصوص المُصدّرة (المحادثات والـ memory/handoff) لإخفاء أي توكنات API، GitHub PATs، كلمات مرور، كوكيز، مفاتيح خاصة، أو إيميلات/بيانات حسابات قبل كتابة المخرجات في المستودع.

---

### 📂 جرد المصادر الفعلية المرصودة على القرص:
1. **القواعد والمهارات والأوامر العالمية:**
   - `~\.gemini\GEMINI.md` (7.5 KB)
   - `~\.gemini\config\rules\` (3 ملفات `.md`)
   - `~\.gemini\config\workflows\` (2 ملف `.md`)
   - `~\.gemini\config\skills\` (23 مجلد `SKILL.md`)
   - `~\.config\opencode\commands\` (`new.md`, `reset.md`)
   - (ملحوظة: `opencode.json` يحتوي على إعدادات مزودين/كوماندز — يُستخلص منه فقط مثال/قالب نظيف أو `instructions` بدون أي مفاتيح إن لزم).
2. **قواعد بيانات المحادثات وملفات الـ Brain:**
   - `~\.gemini\antigravity\conversation_summaries.db` (114.6 MB SQLite — تحتوي جدول `conversation_summaries` به 699 ملخص، وجدول `conversations_fts` به 3,255 مقطع نصي عبر 563 محادثة بإجمالي ~39.09 MB نص مقروء).
   - `~\.gemini\antigravity\conversations\` (500 ملف `.db` فردي بها `steps` بصيغة Protobuf BLOB) + `~\.gemini\antigravity-ide\conversations\` (372 `.db` + 110 `.pb`).
   - `~\.local\share\opencode\opencode.db` (~50 MB SQLite — جدول `session_v2`: 121 جلسة، وجدول `session_message`: 2,689 رسالة JSON بإجمالي ~17.47 MB).
   - `~\.gemini\antigravity\brain\` (96 ملف `.md` على المستوى الأعلى) + `~\.gemini\antigravity-ide\brain\` (1,255 ملف `.md`).
3. **مجلدات الذاكرة والـ Handoff والتوثيق المركزي:**
   - `D:\SMS\.hRhR_gateway-service\Root\` (منها `memory.md`, `HANDOFF.md`, `VOICE_LOG.md`, `PROGRESS.md`, `tasks.md`, `MISTAKES.md`, `ANCHORS.md`, `CONVERSATIONS_AUDIT_LOG.md`, `CONVERSATIONS_FORENSIC_SUMMARY.md`, `CONVERSATIONS_FORENSIC_DATABASE.json` [10.5 MB / 453 محادثة], `ALL_CONVERSATIONS_LEDGER/` [453 ملف JSON] — مع استبعاد ملفات المفاتيح/الحسابات/الجلسات).
   - `D:\SMS\.hRhR_gateway-service\.agents\memory\` (18 ملف `.md`), `AGENTS.md`, `GEMINI.md`, `HANDOFF.md`, `PROGRESS.md`, `README.md`.
   - `D:\SMS\Bolla-Agentic-OS-EGM-SRE\Root\` و `.agents\memory\`.
   - `D:\SMS\.agents\memory\`, `D:\SMS\handoff.md`, `D:\SMS\GEMINI_ARCHIVE_2026-09-02.md`.
   - `~\.gemini\antigravity\scratch\.agents\memory\` (3 ملفات `.md`).

---

### 📋 المطلوب منك الآن (المرحلة أ):
1. اقترح **هيكل مجلدات المستودع (Repo Layout)** وكيفية تصميم `AGENTS.md` الرئيسي بحيث يعمل بذكاء (Progressive Disclosure + Index) في OpenCode وأي أداة أخرى بدون إغراق الـ Context Window.
2. أنشئ/حدّث مسودة `PLAN.md` + `TASKS.json` + `duet_resume.json` + `DUET_LOG.md` في هذا المجلد بمراحل متدرجة (بما فيها مرحلة التحقق وبوابة فحص الأسرار قبل أي Push من طرف Antigravity).
3. استدعِ `executor` لنقد مسودة الخطة فقط (بدون تعديل أي ملفات) وأدمج ملاحظاته، وإذا رأيت أن الخطة جاهزة لمراجعة `critic` بعدسة `scope-guard` فاعرض نتيجته.
4. اختم ردك بوضوح بـ:
   - ملخص الخطة المقترحة وهيكل المستودع.
   - **قائمة أي أسئلة أو نقاط تصميمية تحتاج قرار المالك قبل التنفيذ** (بدون أي تخمين).
