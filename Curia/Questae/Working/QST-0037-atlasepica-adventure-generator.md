# QST-0037 — AtlasEpica: BBEG Oracle for the dungeon master

- **Type:** design / refactor
- **Priority:** 🟠 high
- **Status:** Working — product reshaped 2026-07-16 (BBEG Oracle; see QST-0037.16)
- **Owner:** session 2026-07-16
- **Route to:** Architecture Consul (Druid), Understanding Consul (Bard), Lorekeeper, Workshop Consul (Artificer), Flow Consul (Sorcerer), Methods Consul (Wizard), Design-Team
- **Parent:** —
- **Sidequests:** QST-0037.1 · QST-0037.2 · QST-0037.3 *(parked — CYOA)* · QST-0037.4 · QST-0037.5 · QST-0037.6 · QST-0037.7 *(parked — choice-path URL)* · QST-0037.8 ✓ · QST-0037.9 · QST-0037.10 · QST-0037.11 · QST-0037.12 · QST-0037.13 *(Theme soft / later — see .16)* · QST-0037.14 · QST-0037.15 · **QST-0037.16 (BBEG Oracle — active product)**
- **Related:** AtlasAlusoris NPC generator · AtlasWorldBuild/AtlasOfDungeons (grid maps — distinct) · Decree 0002 · QST-0021.6 · QST-0016 · QST-0027 (titles)

---

## 🔍 Diagnosis (what & where)
`AtlasEpica` is the syntax-of-stories Atlas (Titles, adventure frame, DM Companion). An early prose sketch and a CYOA/choice-path experiment grew unwieldy. Julio confirmed the real product: a **BBEG Oracle** — one villain NPC, locked Area + Lair, one inspiration card per Generate — not a branching adventure machine.

## 🧾 Evidence
- Live modules: `Grimoire_of_Adventure`, `Map_of_Scenes` (ex Prose Adventure), `Map_of_Stories` (moved from ActorLudi), `Map_of_Titles`, `Charts_of_Myth_Collapse`; DM chrome in `shiny_app.py`.
- Product contract and working checklist: **QST-0037.16**.
- Older intent list (vague resolutions, Pointy Hat axes, CYOA, choice URL, Theme-on-choice, …) remains in sidequests for history; several are parked under .16.

## 🎯 Desired outcome
A DM Companion the table can run from when ideas run dry: coherent with *this* BBEG in *this* Area/Lair; presentation-only scene cards; real NPCs with links; TOP Tags open/close the Lodge (Titles-style). Theme Tags later, soft.

## 🧭 Notes for the Agora / implementer
- **Canon home for scope:** Questae (not `docs/plans`). Shape the code; grow Lodges artistically.
- Do not conflate Epica with WorldBuild grid WFC.
- Active build track: **QST-0037.16**.

---

## ✅ Resolution
*(pending — rides with QST-0037.16)*

---

## 🏛️ Council
> Understanding Consul (Bard): DM companion = inspiration, not railroad.
> Architecture Consul (Druid): AtlasEpica stays narrative forge; grid maps stay WorldBuild.
> Methods Consul (Wizard): Collapse must be Tag-gated seeded choice, not metaphor alone.
> Simplicity Consul (Monk): Oracle beats CYOA for carrying cost.

**Weighting:** reach 3 × severity 2 = **6** · council leaning: `build`
