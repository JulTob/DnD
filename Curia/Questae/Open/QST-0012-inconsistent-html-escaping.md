# QST-0012 — Inconsistent HTML escaping: NPC sheet injects model strings as raw HTML

- **Type:** bug
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Safety Consul (Paladin), Contracts Consul (Warlock)
- **Parent:** QST-0007 (Track A / shiny_app.py)
- **Sidequests:** —
- **Related:** AtlasIntelligentiaArtificialis (AI-generated text), QST-0009

---

## 🔍 Diagnosis (what & where)
`build_npc_sheet` renders many model fields via `ui.HTML(_safe_str(...).replace("\n", "<br>"))` — skills, saving throws, movement, senses, resistances, story, etc. (L1435–1470). This injects model strings as **raw HTML with no escaping**. The character sheet, by contrast, does `escape(...)` in at least one place (L1241). If any of these fields ever contains AI-generated or user-influenced text with `<`/`>`, it renders as markup (an XSS/rendering hazard).

## 🧾 Evidence
- NPC: repeated `ui.HTML(_safe_str(getattr(npc, ...)).replace("\n","<br>"))` with no `escape()`.
- Character: `ui.HTML(f"{escape(_safe_str(stat))}<br>…")` (L1241) — the safe pattern, applied inconsistently.
- The project has an `AtlasIntelligentiaArtificialis` (AI text) Atlas — model text is not guaranteed markup-safe.

## 🎯 Desired outcome
One consistent, safe rendering helper: escape text, *then* apply intended formatting (e.g. newline→`<br>`). Raw `ui.HTML` only for strings the code fully controls.

## 🧭 Notes for the Agora / implementer
A small `safe_html(text)` helper (escape → controlled replacements) used everywhere would fix it in one place — a Warlock-style single source of truth for "text to HTML."

## ✅ Resolution
*(pending — filled when Solved)*

---

## 🏛️ Council
> Safety Consul (Paladin): Any path from model text to `ui.HTML` without `escape()` is an injection waiting to happen — doubly so with an AI Atlas feeding strings. Assume the text is hostile.
> Contracts Consul (Warlock): The real fix is one helper with the invariant "escape before format," applied uniformly. The inconsistency *is* the bug. No objection.

**Weighting:** reach 2 × severity 3 = **6** · council leaning: `build`
