# Recommendation of Paseo App

- id: `86ee0f74-443a-41e9-b7f1-588f0b6eaa6c`
- title: Recommendation of Paseo App
- date: 2026-10-29 11:35:26
- workspace: ..............................................................................................................شغل فريق
- steps: 19
- chunks: 3
- archived: false
- summary:
  - Recommendation of Paseo App
  - pijsal1-tech/Claude-Fable-5

## chunk -1 (steps 0–0)

### user

(empty)

### agent

(empty)

## chunk 0 (steps 0–11)

### user

انا أنصح باستخدام برنامج
PASEO

بعد ما جربتة تركت برنامج انتىجرافتى تماما

https://antigravity.google/
https://paseo.sh/
[Paseo](https://paseo.sh/)[Plugins](https://paseo.sh/plugins)[Blog](https://paseo.sh/blog)[Docs](https://paseo.sh/docs)[Changelog](https://paseo.sh/changelog)[Download](https://paseo.sh/download)[Sponsor](https://paseo.sh/sponsor)EN
[22.4k](https://github.com/getpaseo/paseo)
The agentic developmentenvironment
Run many coding agents at once, on any machine.From your desk and from your phone.
[Download for Windows](https://paseo.sh/download/thanks?file=https%3A%2F%2Fgithub.com%2Fgetpaseo%2Fpaseo%2Freleases%2Fdownload%2Fv0.14.0%2FPaseo-Setup-0.14.0-x64.exe)
Supports
[+33 more](https://paseo.sh/agents)
BuildReviewShipExtend
New workspace
History
Schedules
Release Radar
Pinned
Sskills / dotfiles1h
Workspaces
Ready to review
Paseo homepagenow3981·passed
Add automatic page titles12m761·passed
Working
Fix commit safe area in emulators4m
Improve editor typing latency18m
Done
Release v0.7.0-beta.22h
Preserve focus between pages3h750·passed
Design semantic permission sy…7hmy-server·3981·passed
Plan modules and abstractions1d3884·passed
Resume in-progress work3d
Undefined task3d
Diagnose cloud/Codex issue re…4d
Diagnose create_workspace 37…4d
Diagnose tap interactions4d
Clarify task requirements5d
Task for abcdefghi5d
Add project
Paseo homepagepaseoCommit
Codex
Claude Code
npm run dev
https://localhost:3000
The homepage is built. It leads with Paseo’s actual value, then uses the product itself to prove the story instead of falling back to generic dashboard art.
·Reworked the hero around “The control plane for coding agents.”
·Built desktop and mobile scenes from real Paseo workflows and assets.
·Added believable agent, review, plugin, shipping, and host states.
·Matched the app’s tabs, explorer, diff tree, controls, and layout rails.
Worked for 31m 46s
Create a PR
PR opened: Rebuild the homepage around live Paseo workflows.
https://github.com/getpaseo/paseo/pull/3981·Ships the new product-led hero and interactive desktop mockup.
·Includes responsive mobile proof and the supporting homepage story.
·Formatting, typecheck, and lint are clean.
Ready for review.
Worked for 1m 18s
6/6 tasks3 subagents+1.9k-684
Message the agent, tag @files, or use /commands and /skills
GPT-5.6-SolMediumFull access
FilesChanges3981
main
Uncommitted+1.9k-684
packages/website/src+1.9k-684
components+1.5k-512
mockup+1.3k-389
mobile+480-231
atoms.tsx+56-18
chat.tsx+155-74
frame.tsx+91-0
legacy-tabs.tsx+0-139
desktop+612-143
window.tsx+167-42
titlebar.tsx+117-61
toolbar.tsx+204-0
old-tabs.tsx+0-40
shared+194-15
icons.tsx+62-15
TSgeometry.ts+17-0
TSstates.ts+115-0
hero-mockup.tsx+89-52
routes+211-96
index.tsx+44-70
download.tsx+167-0
styles+68-76
CSSmockup.css+68-47
CSSlegacy.css+0-29
Commits
When you want to step away from your desk, you can.
The native mobile app has full feature parity with desktop.
18:54
New workspace
History
Schedules
Pinned
Sskills / dotfiles1h
Workspaces
Ready to review
Paseo homepage3981·passednow
Add automatic page titles761·passed12m
Working
Fix commit safe area in emulators4m
Improve editor typing latency18m
Done
Release v0.7.0-beta.22h
Preserve focus between pages750·passed3h
Design semantic permission sy…my-server·3981·passed7h
Plan modules and abstractions3884·passed1d
Resume in-progress work3d
Undefined task3d
Diagnose cloud/Codex issue re…4d
Diagnose create_workspace 37…4d
Diagnose tap interactions4d
Clarify task requirements5d
Task for abcdefghi5d
Add project
18:53
Paseopaseo ·Mohameds-MacBook-Pro.l…
/release-beta
Shellsed -n '321,680p' docs/release.md
Shell"for p in highlight relay protocol client plu…
Shellnpx eas workflow:view 01a0493d-01cd-77…
Shellgh release view v0.7.0-beta.2 --json name…
Shellgh run list --commit 4e60c2880b4c9ebd…
Shelldocker buildx imagetools inspect ghcr.io/g…
Still in progress:
•npm tags and release notes are correct
•Docker beta image is published; latest remains unchanged
•iOS build succeeded; TestFlight distribution/Beta App Review is running
•Desktop and Android assets are still building
The heartbeat remains active.
+2,173-54
Message, @files, /commandsGPT-5.6-SolMedium
18:55
FilesChanges3981
main
Uncommitted+2,173-54
atoms.tsxpackages/website/src/componen…+56-18
@@ -7,20 +7,28 @@
7type DotTone = "success" | "danger" | "idle";
7export type DotTone =
8 | "success"
9 | "danger"
10 | "warning"
11 | "running"
12 | "idle";
13
14interface DiffStatProps {
15 add: string;
16 remove: string;
17}
18
19/** Compact diff summary. */
20export function DiffStat({
21 add,
22 remove,
23}: DiffStatProps) {
24 return (
25 <span className="flex gap-1">
25 <span className="flex gap-[4px]">
26 <span className="text-mock-success">
27 +{add}
28 </span>
29 <span className="text-mock-danger">
30 -{remove}
31 </span>
32 </span>
33 )
33 );
34}
Commits
Loved by developers
See what developers are saying about Paseo
[@ceeebeeebeeewithout a doubt the most slept on orchestrator right now. Open source, every OS, and a mobile experience that truly blew me away.](https://x.com/ceeebeeebeee/status/[REDACTED:PII])[@erikkshermancontrol agents from anywhere - mac, phone, web. one simple change transformed my health while INCREASING productivity](https://x.com/erikksherman/status/2043011630590751008)[@amankumarjagdevI have tried 100s of agent orchestrator, cli and gui. the best one i have found. Please give it a try! it's really good](https://x.com/amankumarjagdev/status/2044815258414674307)[@tietougongshibaBeing able to check and manage agent progress from my phone while I'm out is so convenient.](https://x.com/tietougongshiba/status/2050886374941925754)[@jasontorresCan interchange between Codex, Claude Code, Opencode, Pi. Stable mobile and desktop apps connected through a secure relay from your VMs.](https://x.com/jasontorres/status/2053875385515790731)
[@ceeebeeebeeewithout a doubt the most slept on orchestrator right now. Open source, every OS, and a mobile experience that truly blew me away.](https://x.com/ceeebeeebeee/status/[REDACTED:PII])[@erikkshermancontrol agents from anywhere - mac, phone, web. one simple change transformed my health while INCREASING productivity](https://x.com/erikksherman/status/2043011630590751008)[@amankumarjagdevI have tried 100s of agent orchestrator, cli and gui. the best one i have found. Please give it a try! it's really good](https://x.com/amankumarjagdev/status/2044815258414674307)[@tietougongshibaBeing able to check and manage agent progress from my phone while I'm out is so convenient.](https://x.com/tietougongshiba/status/2050886374941925754)[@jasontorresCan interchange between Codex, Claude Code, Opencode, Pi. Stable mobile and desktop apps connected through a secure relay from your VMs.](https://x.com/jasontorres/status/2053875385515790731)
[@aadtyncross platform agent orchestration with inbuilt relay and tailscale / self host daemon options + the best UI ive seen in this segment](https://x.com/aadtyn/status/[REDACTED:PII])[@bevstratovIt’s an incredible piece of software. The last building block I needed to fully work from my phone. everything super smooth.](https://x.com/bevstratov/status/2060733983042781550)[@arnoldgamboaPaseo is a really good interface for Pi. It’s not the only thing it does, but that’s my current use case for now.](https://x.com/arnoldgamboa/status/2059832028099436921)[@dongnaebiPaseo is the best software I've used this year. Absolutely amazing!](https://x.com/dongnaebi/status/2043162391941398735)
[@aadtyncross platform agent orchestration with inbuilt relay and tailscale / self host daemon options + the best UI ive seen in this segment](https://x.com/aadtyn/status/[REDACTED:PII])[@bevstratovIt’s an incredible piece of software. The last building block I needed to fully work from my phone. everything super smooth.](https://x.com/bevstratov/status/2060733983042781550)[@arnoldgamboaPaseo is a really good interface for Pi. It’s not the only thing it does, but that’s my current use case for now.](https://x.com/arnoldgamboa/status/2059832028099436921)[@dongnaebiPaseo is the best software I've used this year. Absolutely amazing!](https://x.com/dongnaebi/status/2043162391941398735)
Works with your tools
Bring your subscriptions, skills and configuration
Claude Code
Codex
OpenCode
Pi
OMP
Cursor
Muse Code
Antigravity
[+33 more](https://paseo.sh/agents)
Run it anywhere
Use Paseo locally, from another machine, or with a team
Desktop app
The one click experience, download the app and it just works, no server required
Mobile
Full client and native, not a WebView
[Download](https://paseo.sh/download)
Remote machines
Run Paseo on a home lab, or a cloud machine
[Docs](https://paseo.sh/docs#server--cli)
Teams and triggers
Share access or start work from GitHub, Slack, and Discord
[Paseo Hub](https://paseo.sh/hub)
Built for automation
Use MCP, the CLI, or the TypeScript SDK to automate Paseo
[MCP docs](https://paseo.sh/docs/mcp)[CLI docs](https://paseo.sh/docs/cli)[SDK docs](https://paseo.sh/docs/sdk)
MCP
From another agent
CLI
From the terminal
SDK
From code
Take the open GitHub issues labeled ready and fan them out to separate worktree agents.
I found two ready issues. I will run each in its own worktree.
create_agent#412claude/opus-4.6worktree
create_agent#417codex/gpt-5.6-solworktree
Done, two agents are running. I will let you know when they finish.
Extend it with plugins
Add new panels and functionality that work in desktop, web and mobile
Plugins
[Browse plugins](https://paseo.sh/plugins)[Plugin docs](https://paseo.sh/docs/plugins)
UI
Screens, workspace panels, sidebar items, slash commands, and themes
Agent lifecycle
Change config and MCP servers, answer permissions, and follow up
Providers
Add a coding agent as a provider, used like the built-in ones
Paseo is Apache 2.0.
[Fork the repo](https://github.com/getpaseo/paseo)
Sponsors
Cloud coding agents
[Become a sponsor](https://paseo.sh/sponsor#spot)
Sponsor Paseo
Paseo is an independent project used by tens of thousands of developers daily.
It is maintained by one person, full time, and shaped by the community. There are no investors and no company behind it. I have turned down funding to keep it that way. A tool that sits between you and your code, your keys and your machines has to stay neutral, and funding creates pressure to monetize.
Paseo is self-funded through sponsorship and [Paseo Hub](https://paseo.sh/hub). Your support is what lets me keep working on it.
[Mo](https://github.com/boudra), maintainer
[GitHub Sponsors](https://github.com/sponsors/boudra)[Open Collective](https://opencollective.com/paseo-ai/donate?interval=month&amount=10&contributeAs=me)[Buy Me a Coffee](https://buymeacoffee.com/paseo)[Sponsor as a company](https://paseo.sh/sponsor#spot)
Philosophy
What Paseo stands for, and what every feature is built on
Private
No telemetry, tracking, or forced login. Code stays on your machine.
Independent
Paseo doesn't answer to investors. Its users guide what gets built.
Polished
Install the app and start working. No need to know what a daemon is.
Unified
Every coding agent, used the same way. Switch providers any time.
Composable
Run agents on a laptop or a server, and connect from any device.
Extensible
If Paseo doesn't fit how you work, change it with a plugin or fork.
FAQ
+Is this free?
+Does my code leave my machine?
+What agents does it support?
+How does Paseo run providers?
+Do I need the desktop app?
+How does voice work?
+Can I connect from outside my network?
+Do I need git or GitHub?
+Can I get banned for using Paseo?
+How do worktrees work?
Product
[Blog](https://paseo.sh/blog)[Docs](https://paseo.sh/docs)[Plugins](https://paseo.sh/plugins)[Changelog](https://paseo.sh/changelog)[Hub](https://paseo.sh/hub)[CLI](https://paseo.sh/docs/cli)[Privacy](https://paseo.sh/privacy)[Terms](https://paseo.sh/terms)[Sponsor](https://paseo.sh/sponsor)
Agents
[Claude Code](https://paseo.sh/claude-code)[Codex](https://paseo.sh/codex)[OpenCode](https://paseo.sh/opencode)[Antigravity](https://paseo.sh/antigravity)[Muse Code](https://paseo.sh/muse-code)[All providers](https://paseo.sh/agents)
Alternatives
[Conductor](https://paseo.sh/alternatives/conductor)[Superset](https://paseo.sh/alternatives/superset)[OpenChamber](https://paseo.sh/alternatives/openchamber)[Happy Coder](https://paseo.sh/alternatives/happy-coder)[Codex App](https://paseo.sh/alternatives/codex-app)[Claude Desktop](https://paseo.sh/alternatives/claude-desktop)[OpenCode Desktop](https://paseo.sh/alternatives/opencode-desktop)[Orca](https://paseo.sh/alternatives/orca)
Community
[Discord](https://discord.gg/jz8T2uahpH)[Reddit](https://www.reddit.com/r/PaseoAI/)[GitHub](https://github.com/getpaseo/paseo)
Download
[App Store](https://apps.apple.com/app/paseo-pocket-engineer/id6758887924)[Google Play](https://play.google.com/store/apps/details?id=sh.paseo)[Desktop](https://github.com/getpaseo/paseo/releases)[Web App](https://app.paseo.sh/)

### agent

🎙️ **تفريغ الفويس نوت:**
> *"سؤال: واحد منزل بوست بيقول الكلام ده، مش عارف بقى هل كلامه صح ولا كلامه غلط؟ عايز أعرف برضو، لو غلط.. غلط ليه؟ ولو صح.. صح ليه؟ وطبعاً تفرغ الفويس ده، دايماً تفرغه."*

---

### ⚖️ الحكم السريع: هل كلامه صح ولا غلط؟
**كلامه مبالغ فيه و"مش صح بنسبة 100%"**، لأنه بيقارن حاجتين طبيعتهم ووظيفتهم مختلفة تماماً عن بعض (بيقرن "أداة إدارة" بـ "بيئة تطوير ذكية كاملة").

تعال نفصصها بالبلدي: ليه قال كده؟ وإيه الميزات والعيوب في المقارنة دي؟ 👇

---

### 🟢 1. هو معاه حق في إيه؟ (ليه Paseo عاجبه؟)
برنامج **Paseo** (مفتوح المصدر) مش بيئة بتكتب كود بنفسها، ده **Orchestrator / Manager** (مدير تشغيل ومتابعة):

* 📱 **التحكم من الموبايل:** عنده تطبيق رسمي على iOS وAndroid بيخليك تشغل وتتابع الـ Agents وأنت في السرير أو في الشارع.
* 🔀 **تشغيل كذا Agent في نفس الوقت:** بيفتح أكتر من وكيل برمجي (زي Claude Code, Codex, OpenCode, Aider) في وقت واحد، وكل واحد شغال في فرع (Git worktree) مستقل.
* 🌐 **التحكم عن بُعد:** تقدر تسيب كمبيوترك في البيت أو على سيرفر وتتحكم فيه من أي مكان عبر تطبيق مشفر (E2EE Relay).

> **من وجهة نظره:** لو هو مبرمج معتمد على أدوات CLI (زي Claude Code) وعايز يشغل 5 مهام مع بعض ويتابعهم من تليفونه، Paseo هيكون مريح جداً ومبهر ليه.

---

### 🔴 2. هو غلطان في إيه؟ (ليه متقدرش تستغنى عن Antigravity بيه؟)
المقارنة هنا بين **"مدير طرفيات (Terminal Wrapper)"** وبين **"Agentic IDE متكامل":**

* 🧠 **Paseo مش بيفكر، Antigravity هو العقل:**
  Paseo مجرد واجهة (Shell/UI) بتشغل برامج خارجية؛ لو معندكش اشتراكات ومفاتيح للـ CLI Agents الخارجية (زي Claude API)، Paseo مش هيعملك أي حاجة. في المقابل **Antigravity** مبني كـ بيئة ذكاء اصطناعي متكاملة مدعومة بأقوى نماذج التفكير والبرمجة من Google DeepMind مباشرة.
* 🛠️ **أدوات بيئية عميقة (Deep Tooling):**
  Antigravity مش مجرد شات؛ ده جواه:
  * متصفح مدمج للأتمتة وفحص الـ UI الحقيقي (Browser Subagent).
  * توليد صور وتصميم واجهات مباشرة.
  * نظام مهارات وتخصيصات متقدم (Skills, Plugins, Rules, Knowledge Items).
  * تصحيح الـ Linting والـ Runtime تلقائياً بدون ما يطلب منك.
* 💻 **التركيز على التطوير الحقيقي (Pair Programming):**
  Paseo معمول لمهام الـ background السريعة والـ PRs، لكن لو شغال على مشروع كبير ومحتاج تفكير معماري، فحص أمني، وتطوير عميق، Antigravity بيقدملك سياق كامل للـ Workspace مش متوفر في مجرد نافذة طرفية.

---

### 💡 الخلاصة
* **Paseo** = أداة ممتازة لو أنت أصلاً بتستخدم أدوات تيرمينال ومحتاج تشغل كذا وكيل وتراقبهم من الموبايل 📲.
* **Antigravity** = محطة عمل ذكية كاملة (Agentic IDE) مفيش غنى عنها في الشغل التقني المعقد والأتمتة الشاملة 🚀.
* **القرار:** مش لازم تترك واحد عشان التاني، ممكن تستخدم Paseo كمدير للمهام لو حابب، لكنه أبداً مش بديل يغنيك عن Antigravity!

## chunk 1 (steps 12–18)

### user

Paseo

### agent

🎙️ **تفريغ الفويس نوت:**
> *"فين الدليل على كلامك إنه هو تعبان أو هو ضعيف؟ مش عارف، حاسك بتقلل منه مش عارف ليه."*

---

يا غالي حقك عليا لو فهمت مني إني بقلل منه! بالعكس تماماً، **Paseo مش تعبان ولا ضعيف، ده برنامج ممتاز وعبقري جداً** 👏🔥..

بس خليني أوريك المفاجأة الصادمة اللي تثبتلك إن **صاحب البوست هو اللي فاهم الموضوع غلط تماماً**:

### 💣 المفاجأة: Paseo أصلاً شغال بـ Antigravity!
بص كده في اللينك ده من موقع Paseo الرسمي نفسه:
👉 **[paseo.sh/antigravity](https://paseo.sh/antigravity)**

مكتوب في أول صفحتهم بالبنط العريض إيه؟
> **"Open source app for Antigravity"**
> *"Run your installed Antigravity CLI on your machine and drive it from your phone or desktop."*
> *(شغّل Antigravity CLI المثبت على جهازك وتحكّم فيه من تليفونك أو الكمبيوتر).*

---

### 🔍 يعني إيه الكلام ده؟ وفين الدليل؟

1. **Paseo مش بديل لـ Antigravity.. ده "شاشة تحكم" ليه!** 🎮
   * صاحب البوست لما قال: *"تركت برنامج أنتي جرافيتي تماماً"* كأنه بيقول: *"أنا رميت محرك العربية واشتريت دركسيون جديد!"* 😂
   * Paseo عبارة عن واجهة وموزع (Client / Orchestrator)؛ مبيعرفش يكتب سطر كود واحد من غير ما يربطه بمحرك ذكاء اصطناعي تحته.. ومن أول المحركات المدعومة رسمياً عنده هو **Antigravity CLI** نفسه!

2. **ليه Paseo برنامج قوي ومش ضعيف أبداً؟** 💪
   * واجهة مستخدم (UI) فخمة وسريعة جداً.
   * ميزة الموبايل (Pocket Engineer): تقدر تشغل الأيجنت وأنت برة البيت وتتابع التعديلات من تليفونك.
   * إدارة التفرعات (Git Worktrees): يخليك تشغل كذا وكيل بالتوازي على نفس المشروع في فروع مختلفة.

3. **ليه صاحب البوست وقع في الفخ؟** 🪤
   * هو افتكر إن الواجهة والـ UI الجميل هو اللي بيحل الكود وبيفكر، وميعرفش إن Paseo مجرد "وسيط / Shell" بينفذ الأوامر عبر أدوات زي (Antigravity أو Claude Code أو Codex).
   * لو مسحت Antigravity وأدوات الـ CLI من جهازك ومعندكش اشتراكات ليهم.. Paseo هيكون مجرد شاشة فاضية متقدرش تعمل أي حاجة.

---

### 💡 الخلاصة والنصيحة ليك:
* **هل أنصحك تنزل Paseo وتجربه؟**
  **أكيد طبعاً!** ده مشروع مفتوح المصدر عظيم جداً وواخد 22.4k نجمة على GitHub.
* **ازاي تستفيد منه صح؟**
  نزله عندك على الويندوز أو الموبايل، ووصله بـ **Antigravity**.. ساعتها هتاخد أحسن حاجة من الاتنين: قوة وعقل وتفكير Antigravity، مع واجهة ومرونة وتحكم Paseo من الموبايل! 🚀📱
🎙️ **تفريغ الفويس نوت:**
> *"سؤال، طب هو اسمه إيه؟ باسو؟ هو إيه؟ باثيو؟ هو بيثيو دوت؟ مش عارف أنطقه الصراحة. المهم، هل ده نزلته، إيه اللي يخليني أستخدمه وما أستخدمش أنتي جرافيتي؟ يعني أنا عايز أعرف إيه اللي يخليني أستخدمه وما أستخدمش أنتي جرافيتي؟ أستخدم على الأقل الواجهة زي ما أنت بتقول، دي نقطة. النقطة التانية، هل كل واحد له اشتراك؟ ولا اشتراكاته ماشية مع، اشتراكاتهم عاملة إزاي؟"*

---

### 🗣️ أولاً: اسمه بيتنطق إزاي؟
اسمه **"باسيـو" (Paseo)** — بالإنجليزية بتتنطق زي `/pa-SAY-oh/` (كلمة أصلها إسباني معناها "فُسحة أو تمشية"). يعني انطقها ببساطة: **باسيو**.

---

### 💰 ثانياً: نظام الاشتراكات والفلوس (مين اللي هتدفعله؟)

* **برنامج Paseo = مجاني 100% (ببلاش):**
  البرنامج مفتوح المصدر (Open Source) تحت رخصة Apache 2.0. مفيش أي اشتراك، ولا رسوم، ولا كارت بنك عشان تحمله أو تستخدمه على الويندوز أو الموبايل.
* **الاشتراكات ماشية إزاي (Bring Your Own Subscriptions):**
  Paseo مش بيبيع ذكاء اصطناعي، هو مجرد واجهة بتشغل حساباتك اللي معاك بالفعل:
  * لو شغلت جواه **Antigravity**: بيستخدم حسابك ونسختك اللي موجودة على جهازك بالفعل من غير ولا مليم زيادة.
  * لو حبيت تشغل جواه **Claude Code**: بيطلب منك اشتراكك أو مفتاحك في أنثروبيك.
  * لو حبيت تشغل **Codex**: بيستخدم حسابك في OpenAI.
  👉 **الخلاصة:** Paseo واجهته مجانية تماماً، والمصاريف بتبقى حسب الأداة اللي هتربطها جواه.

---

### 🚀 ثالثاً: إيه اللي يخليك تستخدم واجهة Paseo بدل واجهة Antigravity؟

ليه مبرمج يقرر يفتح واجهة Paseo ويشغل Antigravity من خلالها؟ لـ **4 أسباب جوهرية:**

1. 📱 **التحكم الكامل من الموبايل (وأنت برة البيت):**
   * واجهة Antigravity بتشتغل بس وأنت قاعد قدام الكمبيوتر.
   * مع Paseo، بتنزل التطبيق على تليفونك (iOS أو Android)؛ تقدر تدي أمر للـ Agent وأنت في المواصلات أو في السرير، تراجع الكود (Diffs)، وتوافق على الـ PR من شاشة الموبايل والكمبيوتر شغال في بيتك.

2. 🔀 **تشغيل مهام متوازية في نفس اللحظة (Git Worktrees):**
   * في Antigravity العادي أنت شغال خطوة بخطوة في نفس المشروع.
   * في Paseo تقدر تفتح 4 أو 5 فروع في نفس اللحظة، وتخلي كل مهمة شغالة في خلفية معزولة تماماً من غير ما كود مهمة يبوظ كود المهمة التانية.

3. 🎛️ **تجميع كل الأدوات في مكان واحد (Multi-Agent Dashboard):**
   * لو عندك كذا أداة (مثلاً مهمة عايز تديها لـ Antigravity، ومهمة تانية عايز تجرب فيها Claude Code)، Paseo بيشغلهم جنب بعض في نفس الشاشة عشان تقارن النتايج.

4. ⚡ **واجهة خفيفة مركزة على النتائج:**
   * هو مش محرر كود عملاق مليان قوائم، هو لوحة مهام (Mission Control): بتديه التاسك، يخلصها، يعرضلك الفروقات (Diff Tree) وزرار الـ Commit والـ PR على طول.

---

### ⚖️ الخلاصة: تستخدم مين فيهم؟
* لو بتشتغل شغل تفاعلي محتاج فحص أخطاء، متصفح مدمج لتجربة الواجهات، وتعديل مباشر في ملفاتك كـ Pair Programmer ⬅️ **خليك في واجهة Antigravity الأصلية.**
* لو عايز تدي مهام تقيلة تاخد وقت، وتخرج تسيب الجهاز شغال وتتابع وتوافق من الموبايل ⬅️ **شغّل Antigravity من جوة Paseo واستمتع بحرية الحركة!** 📱🚀
