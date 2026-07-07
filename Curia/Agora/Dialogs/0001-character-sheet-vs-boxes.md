# Dialog 0001 — Character display: dynamic boxes vs. Markdown character sheet

- **Question:** For the Shiny front, keep the dynamic boxes for Skills/Scores, or move to a 5e.tools-style Markdown "character sheet" styled by CSS?
- **Raised by:** Julio
- **Related Questae:** QST-0002 (character-sheet view), QST-0001 (finish Shiny front)
- **Consuls called:** Architecture (Druid), Understanding (Bard), Readability (Barbarian), Flow (Sorcerer) · Design-Team + Lorekeeper (advisory)
- **Status:** 🟡 open — awaiting framing & deliberation

---

## 🧭 Framing
Julio's observation: the dynamic boxes look great for **Skills and Scores** (short, gridded values) but **break down for long text** (features, traits, lore, spell descriptions). The proposal on the table: adopt a **character-sheet layout** like `5e.tools` — primarily **Markdown content styled by the CSS file** — so long text flows well while short stats can still sit in a tidy header block.

A good answer must:
- read beautifully for both short stats *and* long prose;
- be light to render in Shiny and easy to restyle from CSS alone;
- keep the door open to a future shareable/print view (parity with the old Flask `/character/.../seed` URLs);
- fit the project aesthetic — a real character sheet, not a form dump.

Out of scope here: the exact CSS palette (that is a later design pass), and shareable-URL routing (its own Question if pursued).

---

## 🗣️ Deliberation
*Consuls: sign every line, argue only from your lens, be constructive, end with a proposal. (Awaiting the conclave — this section is seeded, not yet argued.)*

Architecture Consul (Druid): …

Understanding Consul (Bard): …

Readability Consul (Barbarian): …

Flow Consul (Sorcerer): …

*(Design-Team and the Lorekeeper may append advisory notes — the 5e.tools sheet structure, header stat-block vs. body prose, and which fields are canon — for the Consuls to weigh.)*

---

## ✅ Convergence check
- [ ] Every called Consul has spoken.
- [ ] Every objection answered or conceded.
- [ ] A concrete layout proposal (with a small markup/CSS sketch) is on the table.

---

## 🕊️ Vox report
Vox: *(pending convergence)*

→ Awaiting Julio's decision. To be recorded as Decree 0001.
