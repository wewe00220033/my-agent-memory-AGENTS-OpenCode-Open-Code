# Scope-guard gate on PLAN v3

- id: `ses_dfc7847f3ffeivgtFNXzqtkW39`
- title: Scope-guard gate on PLAN v3
- date: 2026-11-22 13:52:35
- directory: my-agent-memory-AGENTS-OpenCode-Open-Code
- parent: `ses_dfcd24e0cffedy37KozhKsoVtd`
- agent: critic
- model: upstage-studio/claude-fable-5-1
- messages: 3 (user 1, assistant 2)
- archived: false

## 4 · user (2026-11-22 13:52:35)

You are a subagent spawned by another session.
LENS: scope-guard

# كبسولة الفحص — PLAN.md v3 (Portable AI Memory Vault)

المجلد: `~\.gemini\antigravity\scratch\my-agent-memory-AGENTS-OpenCode-Open-Code`
اقرأ بـ `read` فقط: `PLAN.md` (v3 المعتمدة)، `OWNER_DECISIONS_R2.md` (قرارات المالك الحرفية)، `TASKS.json`، `run_tests.cmd`. **ممنوع تعديل أو إنشاء أي ملف، وممنوع أي شِل.**

## 1. الهدف
مستودع GitHub **عام** يحوي قواعد/مهارات/ذاكرة/تفريغ محادثات المالك بصيغ md/json مقسّمة، مع `AGENTS.md` كـ Bootloader مضغوط ثنائي اللغة لأي وكيل. الأولوية المطلقة للمالك: لا مفتاح/توكن/باسورد/إيميل/هاتف/PII يُرفع. الثانية: أقل مساحة.

## 2. القيود
- الرفع مرحلة بمرحلة (S0→S5) عبر البوصلة فقط بهوية noreply؛ المخطط/المنفذ لا commit/push.
- Python stdlib فقط في `tools/`؛ `run_tests.cmd` موجود (unit/all).
- قرارات المالك في `OWNER_DECISIONS_R2.md` نهائية (Q1–Q19) — لا تُعاد مناقشتها، بل تُفحص الخطة بمدى التزامها بها وبعدم تجاوز النطاق.

## 3. التعديل/الملفات المعنية
`PLAN.md` v3 (الأقسام 1–9) و`TASKS.json` (S0–S5، T0–T21). المرحلة القادمة فوراً: **T0 قراءة فقط** (discover_schema + تقرير محلي في `_local/` غير مرفوع)، ثم S0 (T1–T4: gitignore/هيكل، redact TDD، shard، verify).

## 4. دليل الاختبار
لا كود بعد. البوابة: `run_tests.cmd all` لكل مرحلة + `verify_no_secrets.py` (tracked+untracked+git log -p+noreply) + اختبار سلبي + مراجعة entropy_hits قبل كل تسليم.

## 5. نقطة القلق (scope-guard)
1. هل الخطة تلتزم **بالضبط** بقرارات المالك Q1–Q19 دون زيادة أو نقصان أو تفسير متوسّع؟ (خاصة Q4 بلا سقف صلب، Q6 تعقيم بلا إسقاط، Q9 push مرحلة بمرحلة، Q11/Q12 إسقاط tool outputs/reasoning، Q14 أسماء المشاريع تبقى).
2. هل هناك scope creep: مهام/أدوات/ملفات في الخطة لم يطلبها المالك ولا تخدم الهدف مباشرة؟ أو العكس: شيء طلبه المالك وغير مغطّى بتاسك؟
3. هل سياسة الدفع التدريجي (Q9) تفتح ثغرة أمنية لم تُعالَج في الخطة (تاريخ git، Push Protection، فحص قبل كل مرحلة)؟
4. هل T0 بالفعل قراءة فقط ولا يلمس أي مصدر أو يرفع شيئاً؟
5. هل تصنيف 🔴 وحجم الدفعات متسق مع المناطق الحمراء المذكورة؟

## صيغة الرد المطلوبة
- قائمة مرقمة، كل بند `[Blocker] | [Major] | [Nitpick]` + موقعه (قسم/تاسك) + دليل (اقتباس قصير من الملف) + اقتراح في سطر.
- اختم حرفياً بسطر واحد: `VERDICT: PASS` أو `VERDICT: PASS_WITH_FIXES` أو `VERDICT: BLOCK`.

## 5 · assistant (2026-11-22 13:52:35)

بدء الفحص بعدسة scope-guard: أقرأ الملفات الأربعة المذكورة في الكبسولة قراءةً فقط.

## 27 · assistant (2026-11-22 13:52:53)

VERDICT: PASS_WITH_MAJORS

1. [Major] — §4/§5 T0 (PLAN.md:90, :101 مقابل :103): T0 يطلب "يجرب الأنماط على عينة لرصد أعلى hits" و"عينات (معقّمة)" وقبوله "أعلى 20 نمط hits"، بينما `patterns.json`/`redact.py` لا تُبنى إلا في T2 (PLAN.md:103). تبعية مقلوبة تدفع T0 لتكرار منطق التعقيم خارج TDD (scope creep داخل تاسك "قراءة فقط"). اقتراح: اقصر T0 على schema/أعداد/بنية LEDGER-FORENSIC، وانقل تجربة الأنماط إلى T2 (dry-run على عينة من `_local/`).

2. [Major] — §4 T0 (PLAN.md:90-91, :101): T0 يفتح القواعد الثلاث مباشرة، بينما القراءة الآمنة (`snapshot_db.py` + `backup()` + `mode=ro`) محجوزة لـ T12 في S3؛ قبول T0 "لا تعديل لأي مصدر" غير قابل للتحقق لأن فتح قاعدة WAL حيّة بلا `?mode=ro&immutable=1` قد يُنشئ/يلمس `-shm`/`-wal`. اقتراح: أضف لقبول T0 صراحةً: فتح عبر URI `mode=ro&immutable=1` أو من نسخة مؤقتة فقط، مع مقارنة hash المصدر قبل/بعد.

3. [Major] — §5 تصنيف 🔴 (PLAN.md:98, :102, :125؛ TASKS.json:15, :64-65): تعريف 🔴 = "dry-run + تقرير أعلى 20 ملف تعقيماً قبل الكتابة"، لكن T1 (gitignore/هيكل بلا أي مصدر) مُعلَّم 🔴 بينما T18/T19 (نسخ وتعقيم 96 + 1,255 ملف Brain من المصادر) غير 🔴 — مخالف لـ§1/Q2 ("تعقيم آلي بلا فحص فردي" يحتاج بوابة dry-run أشد لا أخف). اقتراح: `red:true` لـ T18/T19 و`red:false` لـ T1.

ما تحقق: Q1/Q4/Q6/Q9/Q11/Q12/Q14/Q15/Q16/Q17/Q18 مغطاة حرفياً (PLAN.md:18, :48, :73-75, :80, :84-87, :91, :120)؛ لا commit/push من المخطط/المنفذ (:87)؛ `git log -p` + noreply + filter-repo مقابل ثغرة الدفع التدريجي (:80, :86, :143).

VERDICT: PASS_WITH_MAJORS
