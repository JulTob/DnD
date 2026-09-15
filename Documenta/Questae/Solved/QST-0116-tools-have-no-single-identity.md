# QST-0116 — Tools have no single identity

- **Type:** bug / architecture
- **Priority:** 🔴 urgent (QST-0116.1 stops shipped Characters from generating)
- **Status:** Solved
- **Owner:** Claude, with Julio
- **Route to:** Agora: Q-0034 · `Agora/Dialogs/0025-one-identity-for-a-tool.md`. Consuls: Architecture (Druid), Contracts (Warlock), Repair (Cleric), Simplicity (Monk), Testing (Rogue); Lorekeeper advisory
- **Parent:** —
- **Sidequests:** QST-0116.1 · QST-0116.2 · QST-0116.3 · QST-0116.4
- **Related:** QST-0047 (skills and tools as TOP Tags) · Repairs-Ledger A4 · QST-0050 · QST-0072 (recovery)

---

## 🔍 Diagnosis (what & where)

A tool is spelled in several places: `ToolsKit`'s definitions, name lists kept by hand, the mutable sheet `Char_Skills`, and the training ledger. They no longer agree. The 2024 merge of Carpenter's and Woodcarver's Tools into Woodworker's Tools reached some of those places and not others.

Each place where the disagreement shows is its own sidequest:

| Sidequest | Priority | What goes wrong |
|---|---|---|
| QST-0116.1 | 🔴 | The sheet has no `Woodworker_Tools`, so Student of War crashes |
| QST-0116.2 | 🟠 | The artisan tool list is kept by hand in three files, and the written guidance names the wrong copy |
| QST-0116.3 | 🟡 | Instruments and gaming sets are invisible to `Is_Trained` |
| QST-0116.4 | 🟡 | Backgrounds never write the training ledger |

## 🧾 Evidence

In each sidequest. All measured on `main` at `34992b6`, 2026-09-13.

## 🎯 Desired outcome

A tool has one authored identity. Every list, sheet attribute and training query derives from it, so a rename or merge made in one place can neither crash nor skew another.

## 🧭 Notes for the Agora / implementer

- This parent names the shared root. Dialog 0025 decides whether the sidequests are repaired one by one or by one redesign.
- QST-0116.1 is on the shipped player path (Decree 0004). The Agora may want its repair not to wait for the redesign.
- The merge itself is not in question: Woodworker's Tools is the 2024 rule (Lorekeeper to confirm).
- Not Solved while any sidequest is open.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** Julio, in chat, 2026-09-14: "Unify all woodworkers and fix the issues with tools"; then "we are moving forward collapsing the tools... Fix instruments and game sets, unify all tools and its proficiencies (the cool versions with the Works of Wonders and the informative descriptions). Delete duplications." Decided directly; Dialog 0025 closed without deliberation.
- **What changed:** all four sidequests, on `questa/QST-0116-one-identity-for-a-tool`. A tool is authored once, in `AtlasInventarium/ToolsKit.py` (name, ability, Practice); the sheet's attributes, the proficiency list, the kits and their descriptions, and the Artisan's Tools menus all derive from it.
- **Correction to the notes above:** the merge is not the 2024 rule. The 2024 table keeps Carpenter's, Woodcarver's and Navigator's Tools apart; one Woodworker's Tools and one Cartographer's Tools are a house rule, Julio's.
- **Practice/preference to remember:** one proficiency, one kit, one description. A player who knows woodwork can build and carve; a GM should not have to rule the difference. Old names stay as public aliases of the one tool.

---

## 🏛️ Council
*Held in `Agora/Dialogs/0025-one-identity-for-a-tool.md`.*

**Weighting:** reach ⟨3⟩ × severity ⟨3⟩ = **9** · council leaning: `needs a Dialog`
