# QST-0002 — Character-sheet view (Markdown + CSS) for long text

- **Type:** design
- **Priority:** 🔴 urgent
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Understanding Consul (Bard) · Design-Team + Lorekeeper (advisory) → **Q-0001**
- **Related:** QST-0001, Dialog `0001-character-sheet-vs-boxes.md`

---

## 🔍 Diagnosis (what & where)
The current dynamic boxes look great for **Skills and Scores** (short gridded values) but **do not work for long text** (features, traits, lore, spell descriptions). Julio proposes a **5e.tools-style character sheet** rendered largely as **Markdown styled by the CSS file**, so prose flows well while short stats keep a tidy block.

## 🧾 Evidence
- Julio's direct observation: dynamic boxes break for long text.
- Reference target: `5e.tools` character/statblock layout.

## 🎯 Desired outcome
A character display that reads beautifully for both short stats and long prose, is easy to restyle from CSS alone, and looks like a real character sheet — not a form dump. First publish is the **Player** sheet (Decree 0004); NPC sheet waits.

## 🧭 Notes for the Agora / implementer
- **This needs a decision first → Dialog 0001 is open.** Consuls deliberate; Vox reports; Julio decrees the layout direction before implementation.
- Keep the door open for a future shareable/print view.
- Out of scope here: final palette, shareable-URL routing.
