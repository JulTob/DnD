# Dialog 0025 — One identity for a tool

- **Question:** How does a tool get one authored identity, so that the sheet, the menus, the training ledger and the bridge between them can no longer disagree?
- **Raised by:** Agent (Claude), from Julio's review of 2026-09-13
- **Related Questae:** QST-0116 (parent) · QST-0116.1 · QST-0116.2 · QST-0116.3 · QST-0116.4 · QST-0047 · QST-0050 · Repairs-Ledger A4
- **Consuls called:** Architecture (Druid), Contracts (Warlock), Repair (Cleric), Simplicity (Monk), Testing (Rogue); Lorekeeper advisory on the 2024 merge
- **Status:** 🔵 decided by Julio, 2026-09-14 (no deliberation held)

---

## 🧭 Framing

**Context.** QST-0116, one root, four sidequests:
1. **QST-0116.1:** `Char_Skills` has no `Woodworker_Tools`, so Student of War crashes (2 of 80 Artisan Fighters, 2 of 200 Human Fighters).
2. **QST-0116.2:** the artisan tool list is hand-kept three times in three formats; BackgroundKit's copy double-weights Woodworker's Tools, and QST-0047 names that copy as canonical.
3. **QST-0116.3:** `_Legacy_Training_Rank` skips every capability whose `legacy_attribute` differs from its key, which is every instrument and gaming set.
4. **QST-0116.4:** Backgrounds write only the mutable sheet, never the ledger.

**Constraints from Canon.**
- Modular API criterion: one deliberate public surface per module; liberal public aliases keep old import contracts working.
- TagKit doctrine, and QST-0047 as the standing plan to make skills and tools TOP Tags.
- Decree 0004: the player path comes first, and QST-0116.1 is on it.

**A good answer must satisfy.**
1. One place authors each tool; names, menus and sheet attributes derive from it.
2. A merge such as Carpenter + Woodcarver → Woodworker cannot silently double-weight a draw.
3. Instruments and gaming sets are visible to `Is_Trained`.
4. A contract check fails the moment two spellings of a tool disagree.
5. The shipped crash is not held hostage by the redesign.

**Out of scope.** Whether the 2024 merge is right; completing all of QST-0047 in one step.

**Options raised in the review.** Starting points for the council, not its proposals:
- **A. Minimal repair** (QST-0116.1). Add `Woodworker_Tools` to `Char_Skills`, with the two old names as aliases of the same object (mirroring `ToolsKit.py:370-371`), and list it once in the sheet's tool list. Verified on a scratch copy of `34992b6`: Artisan Fighters 80 of 80; FeaturesKit self-test passes end to end (once QST-0117 is also repaired); `replay-player` replays exactly; `verify-aasimar` all clear; `sweep-player` 78 of 78 with no failures. Addresses QST-0116.1 only; `Grimoire_of_Training.py` would still hold the old pair.
- **B. Derive, don't copy** (QST-0116.2). Delete the `BackgroundKit` and `FighterKit` tuples and import from `ToolsKit`; take display names from `Tool_Definition.name`.
- **C. Close the bridge** (QST-0116.3). Let `_Legacy_Training_Rank` read variant capabilities, or stop decision code reading the sheet at all.
- **D. Finish the direction** (QST-0116.4). Make the ledger the only writer (BackgroundKit's `_grant_tool` and `_grant_skills` through `Commit_Training_Gain`) and the sheet a pure projection.
- **E. Correct QST-0047:82** (QST-0116.2) to whatever the council settles as the source of tool names.

---

## 🗣️ Deliberation
*Each Consul signs every line. Argue only from your lens. Objections must be constructive. End with a concrete proposal.*

Architecture Consul (Druid): …

Contracts Consul (Warlock): …

Repair Consul (Cleric): …

Simplicity Consul (Monk): …

Testing Consul (Rogue): …

Lorekeeper (Elf Sage), advisory: …

---

## ✅ Convergence check
- [ ] Every called Consul has spoken.
- [ ] Every objection has been answered or conceded.
- [ ] At least one concrete proposal (with code sketch) is on the table.

---

## 🕊️ Vox report
Vox: no council was held. Julio decided the question directly in chat on 2026-09-14.

## ✅ Julio's decision
*"Unify all woodworkers and fix the issues with tools."* Then: *"we don't need both carpenter/woodcarver and Navigator/cartographer as separate Tool Proficiencies (And collapsing the tool packs too...). One Woodworker Tools and Woodworker Tool Proficiency is enough. And Navigator/Cartographer is the same problem... Fix instruments and game sets, unify all tools and its proficiencies (the cool versions with the Works of Wonders and the informative descriptions. Those are the ones I worked on most). Delete duplications."*

In the terms of the framing: options A (repair the sheet), B (derive, don't copy), D (the ledger is the writer) and E (correct QST-0047) are all taken; C (the bridge) is answered by granting named kinds instead of widening the bridge. Recorded in QST-0116 and its four sidequests, all Solved.
