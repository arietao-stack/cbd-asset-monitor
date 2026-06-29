# The Dashboard & Report Playbook
### Reverse-engineered from Mline's "CoBa's Daughter — Marketing Performance" dashboard, and how to go beyond it.

> Use this for any dashboard, report, or proposal. It encodes *how to think*, *how to design*, and gives you a *reusable master prompt*.

---

## PART 1 — THE MINDSET (12 principles she actually uses)

Each principle below is followed by the **evidence** from her dashboard and **how you apply it**.

**1. Answer first (BLUF — Bottom Line Up Front).**
She opens with a thesis ("Where marketing moved the needle this month") and an Executive Summary *before* any chart.
→ *Apply:* Your first screen must answer "what happened and what do we do?" without scrolling. Charts come after the conclusion, never before it.

**2. Every metric is Finding → Implication → Action ("so what / now what").**
Her bullets aren't facts, they're arguments:
*"Ad efficiency collapsed to 0.85 ROAS on 72.8% paid mix, meaning we're losing $0.15 per dollar invested; immediate audit of paid creative and channel allocation required."*
That's **[metric + direction + magnitude] → [what it means for the business] → [what to do].**
→ *Apply:* No bullet, no KPI, no chart ships without a "so what." If you can't write the implication, cut it.

**3. No naked numbers — always a comparison.**
Every figure carries a denominator or a delta: `▲ 5,805% MoM`, `72.8% of NMV`, `0.85× ROAS`, `+201 vs ▲60.8%`.
→ *Apply:* A number alone is trivia. Attach at least one of: **vs target · vs prior period (▲▼%) · share of total.**

**4. One North Star, then a metric tree.**
She doesn't dump 40 metrics. She picks the outcome that matters (NMV / revenue) and shows the inputs that move it (awareness → consideration → branded search → Amazon NMV).
→ *Apply:* Choose 1 primary metric per audience. Everything else exists only because it explains or drives that one.

**5. Speak the organization's frameworks.**
She maps raw tracker rows onto models leadership already thinks in: **Owned · Earned · Shared** (PESO), **Paid vs Non-paid**, **TOF/MOF/BOF** funnel.
→ *Apply:* Translate your data into the mental model your reader already has. Don't make them learn your columns; map your columns to their strategy.

**6. Bridge activity → money.**
Section "01B · Brand → Sales" literally builds the causal chain: brand awareness → Amazon revenue, with a chart (bars = awareness, line = revenue) and a callout naming the lever.
→ *Apply:* Always answer "does this work matter to revenue/cost?" Connect leading indicators (views, eng) to lagging outcomes (sales, CAC). State the lever explicitly.

**7. Radical transparency = credibility.**
A whole "Data & Method" section: what's **LIVE vs PENDING**, exact formulas (`Brand Buzz = posts×1.0 + (eng/100)×0.5 + (views/1000)×0.3`), units, and `≈` where numbers are estimates. Motto: *"Honest, transparent, no invented numbers."*
→ *Apply:* Pre-empt the skeptic. Show your math, your sources, your freshness, and flag estimates. Trust is a metric — transparency is how you earn it.

**8. Define the unit of analysis precisely.**
*"1 asset = 1 brand mention, strict month-to-date."* Ambiguous units = un-trustable numbers.
→ *Apply:* State exactly what one row/one count means and the time window, up front.

**9. Invent the metric you need — but show the formula.**
She created the **Brand Buzz Score** (volume × depth × reach in one number) because no off-the-shelf metric captured it. She published the formula so it's defensible, not magic.
→ *Apply:* When existing metrics don't capture the question, design a composite — and always expose the math.

**10. A report is a decision tool, not a scoreboard.**
Section "03 · Brand Perspective" gives each initiative **WHAT / HOW / WHY** plus **TEAM · NEXT STEP · CALL FOR SUPPORT.**
→ *Apply:* End on decisions and accountability — owners, next steps, what you need from leadership. A scoreboard informs; a decision tool moves the org.

**11. Design encodes priority (hierarchy of attention).**
Big bold "forest" numbers, uppercase muted eyebrows for section labels, generous whitespace, an on-brand warm palette (not generic dashboard-blue), 💡 callouts pulling the eye to the insight. Visual weight = information importance.
→ *Apply:* The most important thing should be the biggest/boldest. Make the eye land on the "so what" first.

**12. Build an operating system, not a one-off.**
Static site, **daily auto-refresh**, data from sheets + local pushes, "built timestamp", "Confidential". Same reproducible pattern every time.
→ *Apply:* Design once, run forever. Automate the refresh; date-stamp everything; make it cheap to rerun.

---

## PART 2 — THE METHOD (blank page → finished artifact)

Run these 8 steps **in order**. Most people start at Step 4 (charts) — that's the amateur move. Pros start at Step 0.

- **Step 0 — Name the audience and the ONE decision.** "This is for [CMO/founder/team] to decide [budget reallocation / what to scale / go-no-go]." Write it down. Everything serves that decision.
- **Step 1 — Pick the North Star + metric tree.** One primary metric; 3–6 inputs that drive it.
- **Step 2 — List the audience's questions in priority order.** Those questions *become your sections*, top to bottom (pyramid: Outcome → Drivers → Activity → Strategy → Method).
- **Step 3 — For each metric, choose its comparison + unit.** vs target? vs last period? share of total? What is "1 unit"? What's the time window?
- **Step 4 — Write the story FIRST, build charts to support it.** Draft the Executive Summary bullets (finding→implication→action) before making a single chart. Then build only the charts that prove those bullets.
- **Step 5 — Map onto the org's frameworks** (PESO / funnel / paid-vs-non-paid / AARRR…).
- **Step 6 — Write Data & Method** (sources, formulas, LIVE/PENDING, freshness, estimates).
- **Step 7 — Apply the design system** (Part 3).
- **Step 8 — Run the litmus test** (Part 5).

---

## PART 3 — THE DESIGN SYSTEM (how it looks senior, not "Excel-y")

**Typography & color**
- One confident display font (she uses **Plus Jakarta Sans**). Headings/numbers heavy (700–800), negative letter-spacing.
- Section labels = **uppercase, wide letter-spacing, muted** ("eyebrows"): `01 · SALES PERSPECTIVE`.
- **On-brand palette**, never default dashboard-blue. Hers: warm ivory paper, forest-green ink, clay/sand accents. Pick the brand's world.
- Semantic colors only for meaning: good=green, warn=amber, bad=red, plus one accent per channel.

**The KPI card pattern (memorize this):**
`UPPERCASE MUTED LABEL` → **BIG BOLD NUMBER** → `context tag (▲▼ % vs prior / share / vs target)`. Three lines, always.

**Components that signal seniority**
- **Comparison chips:** `▲ 12%` green / `▼ 8%` red, next to the number.
- **Insight callouts (💡):** a tinted box stating the takeaway in one sentence.
- **Ranked, clickable tables:** every row links to the *real* source ("view post ↗"). Verifiable = trustworthy. No black box.
- **Humanized numbers:** `13.2k`, `$5.1k`, `409k` — tabular figures, consistent rounding.
- **Honest charts:** minimal gridlines, axes that don't lie, annotate what changed.
- Generous whitespace; content max-width ~1100–1200px; sticky section nav for long pages.

---

## PART 4 — HOW TO BEAT HER (the next level she hasn't done yet)

She compares to **last month**. You compare to the **plan**. That's the leap.

1. **Targets & pacing, not just trends.** Every KPI vs goal/benchmark, plus a forecast: *"At current pace, EOM = $14k vs $20k target (70%)."* MoM tells you direction; vs-target tells you if you're winning.
2. **A "Decisions & Bets" block with closed loop.** This week's bets (owner · due · expected impact) AND a review of last week's bets (did they work?). Accountability over time beats a fresh scoreboard.
3. **Confidence & freshness per tile.** Extend her honesty into a visible signal: data-quality dot, last-updated, sample size. Tells the reader how much to trust each number.
4. **Efficiency at the unit level.** $/view, $/engagement, CAC by channel/angle/creator → so the reader can *reallocate*, not just admire.
5. **Segment straight to action.** Rank by angle / concept / avatar / creator and write the verdict: *"Community angle drives 3× the eng of Product — shift the brief."*
6. **Event & anomaly annotations** on time series ("US event Jun 10" spike labeled). Explain the shape, don't just show it.
7. **One decision per view.** If a chart changes no decision, delete it. Ruthless editing is a senior signal.
8. **Honest causality.** Label leading vs lagging; never imply causation from correlation — show the mechanism or say "correlated, not proven."
9. **Pre-mortem / risk tile.** "What would make this read wrong?" Naming the risk before leadership does is a power move.

---

## PART 5 — THE LITMUS TEST (run before you ship anything)

- [ ] Can someone get the conclusion + top 3 actions in **60 seconds**, no scrolling?
- [ ] Does **every** number have a comparison (target / prior / share)?
- [ ] Does **every** section end in a decision or "so what"?
- [ ] Is there **one** clear North Star metric?
- [ ] Is the data mapped to a framework the audience already uses?
- [ ] Is there a **Data & Method** with formulas, sources, freshness, and `≈` on estimates?
- [ ] Are all sources **clickable / verifiable**?
- [ ] Is the biggest visual weight on the most important thing?
- [ ] Did you **delete** every chart that changes no decision?
- [ ] Is it **reproducible** (auto-refresh, timestamped)?

---

## PART 6 — THE REUSABLE MASTER PROMPT

Paste this to Claude (or any capable model) for any dashboard/report/proposal. Fill the [BRACKETS].

```
ROLE: You are a senior marketing/analytics strategist + data-viz designer.

TASK: Build a [dashboard / one-page report / proposal] that helps [AUDIENCE — e.g.
founder, CMO, brand lead] make this specific decision: [THE ONE DECISION].

INPUTS / DATA: [paste data, links, or describe the sources + time window].
BRAND WORLD (for design): [brand name + vibe + colors/font if any].

NON-NEGOTIABLE RULES — follow all:
1. ANSWER FIRST. Open with a 1-line thesis + an "Executive Summary" of 3–5 bullets.
   Each bullet = Finding (metric + direction + magnitude) → So what (business
   implication) → Now what (specific action). No bullet without a "so what."
2. PYRAMID ORDER: Outcome → Drivers → Activity → Strategy → Data & Method.
   Most decision-relevant info first.
3. NO NAKED NUMBERS. Every figure shows at least one comparison: vs target,
   vs prior period (▲▼ %), and/or share of total.
4. NORTH STAR. Name ONE primary metric and the 3–6 inputs (metric tree) that move
   it. Cut any metric that changes no decision.
5. FRAMEWORKS. Map the data to the model the audience already uses
   (e.g. Owned/Earned/Shared, TOF/MOF/BOF funnel, Paid vs Non-paid, AARRR).
6. BRIDGE TO MONEY. Explicitly connect leading indicators (views/eng/reach) to
   lagging outcomes (revenue/CAC). State the lever.
7. RADICAL TRANSPARENCY. Include a "Data & Method" section: sources, exact formulas
   for any composite metric, what's LIVE vs PENDING, data freshness, and mark
   estimates with ≈. No invented numbers.
8. DECISION TOOL. End sections with the decision they drive. Add a "Decisions &
   Bets" block: action · owner · due · expected impact — and review prior bets.
9. BEAT-THE-BENCHMARK: compare KPIs to targets/benchmarks (not only last period)
   and add a simple pacing/forecast where data allows.

DESIGN SYSTEM:
- One confident display font; big bold headline numbers; UPPERCASE muted section
  "eyebrows"; generous whitespace; content width ~1150px.
- On-brand palette (not default dashboard-blue). Semantic colors for good/warn/bad.
- KPI card = UPPERCASE LABEL → BIG NUMBER → context tag (▲▼/share/vs-target).
- 💡 insight callouts for takeaways. Comparison chips ▲▼ with %.
- Ranked tables where every row links to the real source. Humanized numbers (13.2k).
- Biggest visual weight on the most important metric.

OUTPUT: [single self-contained HTML file that reads data from data/*.json, auto-
refreshes / a Markdown report / slides]. Make it reproducible and timestamped.

Before finishing, run this check and fix any misses: 60-sec to conclusion?
every number compared? every section ends in a decision? one North Star? mapped to
a framework? Data & Method present? sources clickable? heaviest weight on the most
important thing? deleted charts that drive no decision?
```

### Compact version (for quick reports)
```
Write a 1-page [report] for [AUDIENCE] to decide [DECISION] from this data: [DATA].
Lead with a thesis + 3 bullets, each Finding→Implication→Action. Every number gets a
vs-target or ▲▼ vs prior. Pick one North Star. Map to [framework]. End with Decisions
(action·owner·due). Add a Data & Method note with formulas + ≈ on estimates. Be honest,
skimmable in 60s, and delete anything that changes no decision.
```

### Proposal variant (swap the framing)
```
…Build a proposal for [AUDIENCE] to approve [ASK / budget].
Open with the ask + the expected return (and the cost of inaction).
Structure: Problem (with evidence) → Proposed bet → Why it works (mechanism + comps)
→ What we need (budget/owner/timeline) → How we'll measure success (North Star +
targets) → Risks & pre-mortem. Every claim cited or flagged ≈. End with a clear
yes/no decision and the 1st next step.
```

---

### The one-sentence version of her genius
> **She doesn't report numbers — she makes an argument, in the reader's own language, that ends in a decision, and shows her work so it's impossible to distrust.**
> To beat her: do all that, but measure against the *plan*, close the loop on past bets, and show the *confidence* behind every number.

---

## PART 7 — PROPOSALS / PITCH DECKS (the scrolling-HTML kind)

Reverse-engineered from her "CoBa's Daughter × Lasso — Equestrian Activation" deck.
A *dashboard reports*; a *proposal persuades*. Same design DNA, different job.

### The persuasion arc (her section order)
1. **Cover / at-a-glance** — kicker ("Prepared for [partner]"), a big headline with one
   word in italic-accent, a one-line sub, and a **meta row** (Horizon · Cadence · Model)
   that frames the whole deal in 3 facts. Plus a scroll cue.
2. **The Big Picture** — show the *plan visually first* (a timeline / Gantt: parallel
   tracks, campaigns over months) + a "how to read it" caption. Orient before detail.
3. **By Objective** — *why it works.* Two cards (e.g. Awareness vs Conversion), each with
   story bullets and a callout that states the through-line thesis.
4. **Make it tangible** — **mock-ups of the actual output** (fake but realistic Instagram
   posts, moodboard). Let them *see* it before they commit. Show, don't tell.
5. **By Campaign / workstream** — numbered rows, each: tag (objective) · products in focus
   (chips) · the specific role it plays.
6. **The Ask** — a **small first step** ("Let's start with July") with **month-one
   targets** (views · sales · ROAS) framed as "targets to align on, not guarantees", then
   a numbered **"What we need from [partner]"** list, then a CTA.
7. **Footer** — Confidential · For Partnership Alignment.

### 3 senior moves to steal
- **Proof-of-concept ask.** Don't ask for the 6-month commitment — ask for month one with
  clear targets, then expand. Lowers the barrier, earns the rest.
- **Mock-ups make it real.** A realistic preview of the deliverable de-risks the yes.
- **A single through-line thesis** repeated in every section ("even awareness is shoppable
  — the code is in every caption"). The deck argues *one* idea from many angles.

### The MOTION SYSTEM (what makes it feel premium — all reproducible, pure CSS+JS, no libraries)
- **Scroll progress bar** — a 3px gradient bar at the top tracking scroll %.
- **Sticky-nav solidify** — nav is transparent over the hero, then fades to a frosted
  background + shrinks padding after ~60px scroll.
- **Scroll-reveal** — elements start `opacity:0; translateY(24px)` and animate in when they
  enter the viewport (IntersectionObserver adds `.in`). The signature "things rise as you
  scroll" feel. Stagger by putting `.reveal` on each block.
- **Scrollspy** — the active section's nav link underlines as you pass it.
- **Animated hero visual** — an SVG "nucleus" with orbiting dots spinning at different
  speeds/directions (`@keyframes spin`, 24s/38s/54s). One tasteful motion centrepiece.
- **Micro-interactions** — cards/bars lift on hover (`translateY(-3px)`), a pulsing dot,
  smooth anchor scrolling (`html{scroll-behavior:smooth}`).
- **Accessibility** — `@media (prefers-reduced-motion: reduce)` disables all of it. (Senior
  tell: motion that respects the user.)
- **Self-contained interactivity** — click/drag-to-upload image placeholders, saved to
  `localStorage`, with in-browser canvas resize. ⚠️ localStorage images live only in *your*
  browser — they are NOT saved into the .html file, so a teammate opening the file won't see
  them. To make images permanent, embed them in the HTML (see "How to update" below).

### THE PROPOSAL MASTER PROMPT (paste to Claude; fill [BRACKETS])
```
ROLE: Senior brand strategist + premium web designer. Build a single self-contained,
scrollable HTML pitch deck (no external libraries except a Google font).

GOAL: Persuade [PARTNER/AUDIENCE] to approve [THE ASK]. Through-line thesis to repeat in
every section: "[ONE-SENTENCE THESIS]".

INPUTS: [offer, timeline, products, targets, what you need from them, any real numbers].
BRAND WORLD: [brand + vibe + palette + font]. Tone: confident, warm, editorial.

SECTION ARC (in order):
1. Cover: kicker "Prepared for [partner]", big headline (one word in italic accent),
   one-line sub, a META ROW of 3 framing facts (e.g. Horizon · Cadence · Model), scroll cue.
2. Big Picture: a visual timeline/Gantt of the plan (parallel tracks across months) + a
   "how to read it" caption.
3. By Objective: 2–3 cards explaining why it works; each ends in a callout restating the thesis.
4. Make it tangible: realistic MOCK-UPS of the actual output (e.g. in-feed social posts,
   moodboard) with image placeholders.
5. By Campaign/workstream: numbered rows — tag · items-in-focus chips · the role it plays.
6. The Ask: a PROOF-OF-CONCEPT first step (e.g. "start with month one") + month-one targets
   (framed "targets to align on, not guarantees") + a numbered "What we need" list + a CTA.
7. Footer: Confidential · For [purpose].

DESIGN: one confident font; big headlines with italic-accent emphasis; UPPERCASE wide-tracked
eyebrows; warm on-brand palette; rounded cards with soft shadows + hover-lift; chips/tags;
numbered rows; content width ~1140px.

MOTION (pure CSS+JS, no libraries): top scroll-progress bar; nav transparent→frosted on
scroll; scroll-reveal (opacity+translateY via IntersectionObserver) on each block; scrollspy
active nav link; ONE tasteful animated hero visual (e.g. orbiting SVG); hover micro-lifts;
smooth scroll; and a `prefers-reduced-motion` fallback that disables all motion.
Optionally: click/drag image-upload placeholders (localStorage) — but note images won't
travel with the file.

OUTPUT: one .html file, opens offline, mobile-responsive.
```

### How to UPDATE a proposal/dashboard HTML each time
This is one self-contained file — there's no database. Three ways, easiest first:
1. **Tell Claude what changed** ("update July targets to 4M views, add a 5th campaign row")
   → I edit the HTML and hand it back. Best for copy/number/section changes.
2. **Edit the text yourself** — the words and numbers are right there in the HTML
   (e.g. `<div class="big">3M+</div>`); change between the tags, save, refresh the browser.
3. **Images:** drag/drop works for previewing, but to make them permanent (so others see
   them) embed them: either `<img src="data:image/jpeg;base64,…">` (Claude can bake them in)
   or host the images and use real URLs. The drag-drop/localStorage version is only for
   your own screen.
- **To share:** send the .html (opens anywhere, offline) OR push to GitHub Pages for a live
  link — but proposals are usually Confidential, so prefer sending the file or a private host.
