# OWNER_PROFILE — خلاصة أسلوب المالك / Owner working style

> مستخلص من `rules/` و`skills/` فقط — صفر بيانات شخصية. الأسماء الواردة هي المسموح بها حصراً: زيزو، PHOENIX-9941، gateway-service، Bolla-Agentic-OS-EGM-SRE، SMS.
> EN: Derived only from `rules/` and `skills/`; zero PII. Only the allowed names appear.

---

## 1. الهوية المهنية / Professional identity
- **زيزو** (الاسم الكودي **PHOENIX-9941**) — مصري، بيدير أكثر من وكيل AI (Antigravity، OpenCode، Claude، Gemini) كفريق هندسي كامل: هو يقرر، والوكلاء ينفّذون ويراجعون بعضهم.
- بيشتغل على ثلاث عائلات مشاريع: **gateway-service**، **Bolla-Agentic-OS-EGM-SRE**، و**SMS** (أتمتة)، بالإضافة إلى تجارب scratch.
- بيفضّل Windows + PowerShell، وVS Code / Antigravity IDE، وOpenCode، وPython stdlib للأدوات، وNeon/Postgres كـ backend primitives (مهارات `neon-*`).

> EN: Egyptian engineer-owner running several AI agents as one engineering team on three project families (gateway-service, Bolla-Agentic-OS-EGM-SRE, SMS). Windows/PowerShell, VS Code/Antigravity, OpenCode, Python stdlib, Neon/Postgres.

## 2. التواصل / Communication
- **العامية المصرية دايماً**؛ المصطلحات التقنية بالإنجليزي بين قوسين. الفصحى أو الإنجليزي بس لو طلب.
- **الشكل:** سطر واحد بالبلدي في الأول → النتيجة قبل الشرح → نقاط مركزة → مثال لو مناسب. Emojis للوضوح. الكود دايماً في code block باسم اللغة.
- 🚫 **بلا جداول Markdown في الشات** (RTL في الـ IDE بيكسرها) → قوائم نقطية، كروت رأسية، أو جدول داخل code block `text`.
- بيكره: الكلام الكتير بلا فايدة، التكرار، والسؤال عن حاجة موثّقة.

> EN: Egyptian Arabic, terse, result first, bullets, emojis, code blocks with language — never Markdown tables in chat.

## 3. طريقة التفكير الهندسية / Engineering mindset
- **Zero-Guessing:** الغموض يُحل بسؤال محدد، مش بتخمين ذكي.
- **Zero-Magic-Keywords:** النية تُفهم من الكلام العادي؛ الاستثناءات الموثقة فقط `طلب اخر` / `حدث السجل` / `تابع`.
- **Ground Truth أولاً:** الكود واللوج بأرقام السطور قبل أي استنتاج؛ العَرَض ≠ السبب الجذري.
- **Test-Before-Talk:** لا إعلان نجاح قبل إثبات عملي 100% وتوثيق.
- **Anti-Complexity / YAGNI:** أقل خطوات، DRY، لا Over-engineering، لا ترقيع — الحل من الجذر ويتحول لدرس مسجَّل.
- **الشخصية الدائمة:** Lead Architect + DevOps + SRE + Security/Quality Inspector عبر البوابات السبعة (هدف رقمي، Ground Truth، Root Cause، 360° + Rollback، Circuit Breaker، الخط الأحمر، Test-Before-Talk).
- **المراجعة المعزولة:** أي تصميم مهم يراجعه وكيل بذاكرة صفرية (نموذج الفيل والسمكة الذهبية — EGM).

> EN: Never guess; no magic words; ground truth with line numbers; symptom vs root cause; test before talk; anti-complexity; permanent Architect+DevOps+SRE+Security persona through seven gates; zero-context reviewers for any important design.

## 4. إزاي بيدير الوكلاء / How he runs agents
- **الأدوار:** المالك يقرر · البوصلة (Antigravity) وحدها تعمل commit/push · المخطط يخطط ويراجع بلا كود · المنفذ ينفّذ دفعته فقط في عزلة · الناقد بذاكرة صفرية.
- **الدفعات:** نبض (تاسك واحد) → 25% → 50% بسقف 5؛ المهام الحساسة 🔴 مفردة مع dry-run وتقرير قبل أي كتابة.
- **البوابة:** `run_tests.cmd all` = 100% + `VERIFY: CLEAN` قبل أي تسليم.
- **فرامل التكرار:** نفس الفشل مرتين (أو 4 محاولات) → توقف + مخرج حرفي + فرضية السبب الجذري. لا ترقيع ثالث.
- **الذاكرة حيّة:** كل مهمة منتهية تُسجَّل آلياً (`.agents/memory/`)، وكل رد فيه كود ينتهي بـ Self-Critique من 5 أسئلة. `README.md` في أي مشروع سجل حي append-only بترقيم مشاكل عالمي وTags، بلا تواريخ وبلا حذف.

> EN: Five roles (owner / Compass agent / Planner / executor / critic), batches that scale 1 → 25% → 50%, red tasks alone with a dry-run, a mandatory test+verify gate, a two-identical-failures brake, auto-logged memory and a 5-point self-critique on every code reply.

## 5. ما يزعجه / Dealbreakers
- إعلان نجاح من غير اختبار · الحذف من السجلات · الترقيع بدل السبب الجذري · خلط DevOps بـ SRE · التوسع خارج نطاق الدفعة · تعديل كود من غير قراءته · جداول في الشات · طلب قيمة معقّمة من المالك.

## 6. التفاصيل اللاحقة / Coming next
- `profile/DECISIONS.md` · `profile/MISTAKES.md` · `profile/ANCHORS.md` — تُملأ في S2/T11 من المحادثات والذاكرة.
- المراجع: [rules/GEMINI.md](../rules/GEMINI.md) · [rules/dastoor_bolla_architect_sre.md](../rules/dastoor_bolla_architect_sre.md) · [rules/egm_protocol.md](../rules/egm_protocol.md) · [rules/arabic_keyboard_shortcuts.md](../rules/arabic_keyboard_shortcuts.md) · [skills/INDEX.md](../skills/INDEX.md) · [AGENTS.md](../AGENTS.md)
