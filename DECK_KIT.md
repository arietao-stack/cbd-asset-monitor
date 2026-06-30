# 🎴 CoBa Deck Kit — make any content a bold, live, fully-tooled deck

A standard kit so every future proposal / report / pitch can be a beautiful dark-luxe
deck, **auto-published to a live link**, with the complete A–Z toolset already built in.

- **Template:** `docs/deck-template.html` (copy it to start a new deck)
- **Reference (filled):** `docs/coba-ltk-deck.html` → https://arietao-stack.github.io/cbd-asset-monitor/coba-ltk-deck.html
- **Backend (shared by all decks):** one Google Apps Script + Sheet (already deployed). New decks reuse it — **no new setup per deck**.

---

## What's built in (works with zero setup)
- **Design:** dark-luxe editorial, Fraunces display + Plus Jakarta Sans, 16:9 landscape slides that **flip horizontally**, scale-to-fit, oversized ghost section numbers, count-up numbers, scroll-reveal.
- **Present mode:** `←/→` `Space` to move, number keys jump, **`F` fullscreen**, dots + slide counter + progress bar.
- **Comments (live, shared, emailed):**
  - **＋ Comment** → click a spot, or **select text → 💬 Comment** (the text auto-highlights).
  - **Hover a pin** → the comment previews instantly; move into it → it locks open.
  - **Reply / Resolve / Delete** — on the pin popover **or** inline in the Comments side-panel.
  - Resolved comments hide from the slide (still in the panel → Reopen).
- **Markup:** 🖍 Highlighter · ✎ Pen · ⌫ Eraser · 🗑 Clear · 4 colours.
- **Edit text directly:** **✏️** → click any text, type, **⌘B bold / ⌘I italic**. Saved & synced.
- **Email:** new comment / reply / resolve → emailed to the team, **grouped into one thread per comment**. Drawings/highlights/edits don't email (no spam).
- **Fast:** every action is optimistic (instant) — network syncs in the background.
- **Shared & isolated:** all decks use one backend; each deck's comments are kept separate by `DECK_ID`.

---

## Make a NEW deck — Option A (fastest): ask Claude
Paste this, filling the brackets:

```
Make a new deck from docs/deck-template.html in the CoBa Deck Kit style.
DECK_ID: [kebab-id e.g. coba-holiday]   DECK_NAME: [Display Name e.g. CoBa Holiday]
Topic / audience / the one decision: [...]
Through-line thesis: [one sentence]
Content per section (cover, the idea, the numbers/targets, the plan/timeline, why it works,
what it looks like, how we measure, detail, the ask): [...]
Then save it to docs/[deck-id].html and deploy it live.
```
Claude fills the template, keeps all tools, and pushes it → returns the live link.

## Make a NEW deck — Option B (DIY)
1. `cp docs/deck-template.html docs/<your-deck>.html`
2. Open it, set near the top of `<script>`:
   `const DECK_ID="<your-deck>", DECK_NAME="<Display Name>";`
3. Replace every `[PLACEHOLDER]`. Each `<section class="slide">` is one slide — add/remove freely (keep `SLIDE_TITLES` in sync). Big animated numbers use `data-count`.
4. Deploy: `bash deploy-deck.sh docs/<your-deck>.html` → prints the live URL.

---

## Deploy (auto → GitHub Pages)
```bash
bash deploy-deck.sh docs/<your-deck>.html
# → commits, pushes, and prints:
#   https://arietao-stack.github.io/cbd-asset-monitor/<your-deck>.html
```
Pages rebuilds in ~1 min. Editing content later = edit file → run deploy again (comments are
kept in the backend, separate from the file, so they survive edits).

---

## The shared comment backend (one-time, already done)
- One Apps Script web app (project "Comment Backend") + a Google Sheet stores every deck's
  comments; it emails `arie.tao@lixibox.com` and threads them.
- Every deck points `CONFIG.API` at the **same** web-app `/exec` URL (already set in the template).
- `DECK_ID` keeps each deck's comments separate on that one backend.
- Backend source: `~/Downloads/comments-backend.gs`. If you ever change it, redeploy:
  Apps Script → Deploy → Manage deployments → ✏️ → New version → Deploy.

---

## Master prompt (for any deck/report/proposal, kit-aligned)
```
ROLE: Senior brand strategist + premium web designer. Output ONE self-contained deck
built on docs/deck-template.html (CoBa Deck Kit) — do not change the engine/tools/design,
only the slide content + DECK_ID/DECK_NAME.

GOAL: [dashboard / proposal / report] for [AUDIENCE] to decide [THE DECISION].
THESIS (repeat across slides): "[one sentence]".

RULES (kit house style):
- Lead with the answer; one idea per slide; bold editorial headlines (one word in <em>).
- Numbers get count-up + a comparison (vs target / prior / benchmark).
- Map to the audience's framework; bridge activity → money; "no invented numbers"
  (mark estimates ≈, include a How-We-Measure slide with the North Star + formula).
- End on a proof-of-concept ask + what you need.
- Keep all built-in tools (comments, edit, markup, email) untouched.

OUTPUT: save as docs/[DECK_ID].html, then deploy-deck.sh it and give me the live link.
```

> Tip: this kit is the deck/proposal companion to `DASHBOARD_PLAYBOOK.md` (the thinking +
> design framework). Use the playbook to decide *what to say*; use this kit to *ship it live*.
