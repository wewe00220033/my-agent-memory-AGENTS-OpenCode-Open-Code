# Conversations Index

> يُولَّد آلياً بـ `tools/build_index.py` — لا تعدّل ما بين العلامتين يدوياً. النص خارج العلامتين مُعدّ في T17.

## المصادر الأربعة / Four sources

- **summaries** — 701 ملخص شهري لمحادثات Antigravity في 8 ملفات (2026-04 → 2026-11) · folder: [summaries/](summaries/) · index: [index/summaries-2026.md](index/summaries-2026.md)
- **antigravity** — 565 محادثة / 3,268 مقطعاً تحت `antigravity/YYYY-MM/<date>_<title>_<id>.md` (6 محادثات مقسّمة إلى أجزاء `.partNNN.md` + `.parts.json`؛ لا يوجد `unknown-date/` حالياً) · folder: [antigravity/](antigravity/) · index: [index/antigravity-2026.md](index/antigravity-2026.md)
- **opencode** — 137 + 2 = 139 جلسة / 1,883 + 1,687 = 3,570 رسالة (نص user/assistant فقط) تحت `opencode/YYYY-MM/<date>_<title>_<id>.md`؛ 119 جلسة أصل + 18 جلسة فرعية مُدرجة بمسافة بادئة تحت الأب في الفهرس · folder: [opencode/](opencode/) · index: [index/opencode-2026.md](index/opencode-2026.md)
- **ledger** — 453 ملفاً / 5,436 عنصراً في 5 أجزاء JSON (≤ 2 MB لكل جزء) + [ledger.parts.json](ledger/ledger.parts.json) + [AUDIT.md](ledger/AUDIT.md) + [SUMMARY.md](ledger/SUMMARY.md) · folder: [ledger/](ledger/) · index: [index/ledger-2026.md](index/ledger-2026.md)

## ملاحظة 453 / 5,436 (ledger)

- **453 ملفاً** = عدد ملفات LEDGER المصدرية = عدد العناصر الأعلى مستوى (كائن JSON واحد لكل ملف، `cid` فريد لكل عنصر، index 1 → 453) موزّعة على الأجزاء الخمسة (68 + 132 + 123 + 36 + 94 = 453).
- **5,436 عنصراً** = 453 × 12 = مجموع حقول البيانات (key/value) المصدّرة داخل تلك الكائنات (12 مفتاحاً لكل ملف كما في عمود «keys» بـ AUDIT.md) — أي أنّ الرقم يعدّ الحقول المُعقَّمة لا الملفات ولا المحادثات.

## FORENSIC_DATABASE

- AR: FORENSIC_DATABASE مكرر 100% لـ LEDGER (T0: 453/453 عنصراً متطابقاً بالـ canonical sha256 — قرار Q5) ولم يُصدَّر؛ لا يوجد مجلد له.
- EN: FORENSIC_DATABASE is a 100% duplicate of LEDGER (T0: 453/453 items identical by canonical sha256 — decision Q5) and was NOT exported; there is no folder for it.

## الفهارس السنوية / Yearly indexes (`index/<source>-<YYYY>.md`)

- [index/summaries-2026.md](index/summaries-2026.md)
- [index/antigravity-2026.md](index/antigravity-2026.md)
- [index/opencode-2026.md](index/opencode-2026.md)
- [index/ledger-2026.md](index/ledger-2026.md)

## كيف تبحث / How to search

- ابدأ من `INDEX.json` في الجذر (يُولَّد في S5) → الفهرس السنوي للمصدر أعلاه → grep بالكلمة أو التاريخ داخل مجلد الشهر الواحد. لا تفتح مجلداً كاملاً.
- EN: root `INDEX.json` (built in S5) → the yearly index above → grep inside one month folder. Never bulk-read.
- [audit/](audit/) محجوز لتقارير التدقيق الآلية (فارغ حالياً عدا `.gitkeep`).

<!-- AUTO-INDEX:START -->
<!-- AUTO-INDEX:END -->
