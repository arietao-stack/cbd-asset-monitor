# 🗂️ Prompt Library — copy, fill the [brackets], paste to Claude

How to work: **open a NEW chat per artifact** (keeps it fast). The kit + memory persist, so
Claude already knows your style. You bring the content; Claude builds + deploys + sends the link.

Templates (all share one engine + the full toolset + the shared comment/email backend):
- `docs/deck-template.html` — generic pitch / proposal / overview
- `docs/creator-brief-template.html` — briefing a creator
- `docs/report-template.html` — monthly performance report

Deploy any deck: `bash deploy-deck.sh docs/<deck-id>.html` → `arietao-stack.github.io/cbd-asset-monitor/<deck-id>.html`

---

## 1) Proposal / Pitch
```
New chat. Make a PROPOSAL deck from docs/deck-template.html (CoBa Deck Kit).
DECK_ID: [kebab, e.g. coba-retailerX]   DECK_NAME: [Display Name]
Audience: [who] · Decision they must make: [the ask]
Through-line thesis (repeat across slides): "[one sentence]"
Content: [paste rough notes / offer / timeline / targets — messy is fine]
Rules: answer-first; one idea per slide; numbers get count-up + a vs-benchmark;
bridge to money; proof-of-concept ask at the end; no invented numbers (mark ≈).
Then save as docs/[DECK_ID].html and deploy it; give me the live link.
```

## 2) Monthly / Performance Report
```
New chat. Make a REPORT deck from docs/report-template.html (CoBa Deck Kit).
DECK_ID: [e.g. coba-report-2026-07]   DECK_NAME: [Brand — Jul 2026]
Period: [month] · North Star: [metric] · Targets: [target values]
Data: [paste KPIs, by-channel numbers, wins/misses, top assets]
Rules: lead with the one takeaway; EVERY number vs target AND vs prior (▲▼);
wins & misses; a Decisions & Bets slide (action·owner·due) + review last month's bet;
a Data & Method slide (formula + ≈). Save as docs/[DECK_ID].html and deploy.
```

## 3) Creator Brief
```
New chat. Make a CREATOR BRIEF deck from docs/creator-brief-template.html (CoBa Deck Kit).
DECK_ID: [e.g. brief-graysonsmith-jul]   DECK_NAME: [Brand × Creator]
Creator: [@handle] · Campaign: [name] · Live by: [date]
Deliverables: [e.g. 3 Reels + 2 posts] · Code: [COBAxYOU] · Tags: [@/#]
Concept / hook: [...] · Do's: [...] · Don'ts: [...] · References: [links]
Payment & usage: [rate / commission / whitelisting]
Save as docs/[DECK_ID].html, deploy, and give me the link to send the creator
(they comment per slide; replies email me).
```

## 4) Live Dashboard (not a deck — for metrics that refresh)
```
New chat. Build a LIVE dashboard like the CBD asset tracker (not the deck kit).
Source: [Google Sheet link / data] · Metrics: [views, sales, …] · Refresh: [daily/…]
Host on GitHub Pages; auto-update via GitHub Actions where possible.
Match the editorial style in DASHBOARD_PLAYBOOK.md (answer-first, KPIs vs target, charts).
```

---

### Reusable rules (the house style — Claude applies these automatically)
1. **Answer first** — thesis + the 3 key takeaways before detail.
2. **Every number gets a comparison** — vs target / vs prior (▲▼) / share.
3. **One idea per slide**; bold editorial headline (one word in *italic accent*).
4. **Map to the audience's framework**; bridge activity → money.
5. **No invented numbers** — mark estimates ≈; include a How-We-Measure slide.
6. **End on a decision / proof-of-concept ask** with owners.
7. Keep all built-in tools (comments, edit, markup, email) untouched.

> Companion docs: `DASHBOARD_PLAYBOOK.md` (how to *think* + beat-the-benchmark) · `DECK_KIT.md` (how the kit works).
