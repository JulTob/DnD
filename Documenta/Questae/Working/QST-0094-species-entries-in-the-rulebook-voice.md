# QST-0094 — Species entries speak the rulebook's present voice; the Dwarf says who they are

- **Type:** docs · bug
- **Priority:** 🟠 high *(user-visible sheet text)*
- **Status:** Working (rule-voice rewrite landed; inspiration lines and two conventions await Julio)
- **Owner:** Claude (branch `questa/QST-0094-dwarf-voice-and-species-entries`, 2026-09-07)
- **Route to:** Lorekeeper · Understanding (Bard) · Readability (Barbarian) · Julio
- **Parent:** QST-0091.1 (Species: one file)
- **Sidequests:** —
- **Related:** QST-0002 (the sheet) · QST-0051 (species feature voice sweep, Documenta) · `SpeciesKit/__main__.py::_assert_already_gained_vocabulary` · Elves and Halflings resolutions (the reference pattern)

> Minted under `Documenta/` (Julio, 2026-09-07: "Darkvision, or any other feature, should not say 'Gained at Level 1.' … I feel like some things are missing from the sheet. Like the flavor texts. And the features are changed.")

---

## 🔍 Diagnosis (what & where)

The sheet flattening of 2026-09-06 (`9be3a07`) removed only two heading lines ("Dwarf Description", "Dwarf Features"); the 306 lines of Species content are byte-identical before and after. What Julio saw missing is older: the vault restore brought several Species resolutions back in a recovery-era voice that the project had already outgrown.

The house pattern (Elves, Halflings, Orcs, Humans): an italic inspiration line in the project's voice, a blank line, then the rule in the 2024 rulebook's present tense. The self-test's `_assert_already_gained_vocabulary` states the law: "A rule the Character already has must not be announced as a future one" (no *gained at level*, *will gain*, *when you reach*). It was asserted only on the Aasimar path, so it never saw the Dwarf.

Audit of every playable Species at levels 1 and 5, 2026-09-07:

| Species | Entries | State before |
|---|---|---|
| Elf, Halfling, Human, Orc | all | italic line + rulebook voice: the pattern |
| Gnome, Goliath, Aasimar | all | authored prose paragraph, then the rule; no italic marker (a second convention) |
| Dragonborn | Breath Weapon | pattern; **Draconic Flight** opened "Gained at Level 5."; Darkvision is chip-only by design ("a record, not a paragraph") |
| Aasimar | Darkvision | chip-only by design |
| **Dwarf** | all four | "Gained at Level 1. Dwarven senses/stock granted …": level announcement, retrospective voice, no inspiration line |
| **Tiefling** | Darkvision, Otherworldly Presence, Fiendish Legacy | bare fragments ("Darkvision with a range of 60 feet.", "The Thaumaturgy cantrip. Charisma is its spellcasting ability.") |

The `.recovery-vault` archive shows the same "Gained at Level 1. X granted Y" voice on Orc, Halfling and Tiefling before the wipe; Orc and Halfling were rewritten to the pattern since, Dwarf and Tiefling were not.

## 🧾 Evidence

- `grep -rn "Gained at Level" AtlasActorLudi/SpeciesKit` → Dwarves/resolution.py ×4, Dragonborn/resolution.py ×1.
- Old-vs-new sheet render for Dwarf Fighter Survivor seed 7: diff = the two heading lines only.
- `python -m AtlasActorLudi.SpeciesKit` passed while the Dwarf entries violated the rule: the assertion ran on one species.

## 🎯 Desired outcome

Every Species entry on the sheet is a feature the Character has, in the rulebook's present voice, with the project's inspiration line above it where the Species follows that convention. The self-test enforces the voice for every playable Species. The Dwarf's description and docstring carry Julio's identity for the people (Iberian and Hispanic roots, clans, gold and soul-metals, the Saints).

## 🧭 Notes for the Agora / implementer

**Landed on this branch:** Dwarf ×4, Dragonborn Draconic Flight, Tiefling ×3 rewritten in the rulebook's voice from the trait constants (`Darkvision_Rules`, `Dwarven_Resilience.RESISTANCE`, `Stonecunning.*`, `heritage.DAMAGE_RESISTANCE`); `_test_playable_species` now resolves every Species' features and asserts the vocabulary rule and that no Species entry is empty unless its chips are the feature.

**Awaiting Julio (authored content, not landed):** the four Dwarf inspiration lines. Proposals, in the taught-or-gifted register the Species traits use:

- Darkvision: *The mines taught our eyes to work where the lamps do not reach.*
- Dwarven Resilience: *Every dwarf grows up tasting the mine air and the smelter's fumes. What did not kill our ancestors does not poison us.*
- Dwarven Toughness: *A dwarf is built like a ledger: every year adds a line, and none is ever struck out.*
- Stonecunning: *Lay a hand on the stone and listen. The mountain still keeps our accounts.*

**Two conventions to decide:**

1. Darkvision across Species: Elf, Orc, Gnome, Dwarf and Tiefling print the rule; Aasimar and Dragonborn print the chip only. One convention or two?
2. Species description voice: Humans, Dwarves and Elves now speak as "we/our"; Aasimar, Gnome, Goliath, Halfling, Orc, Tiefling and Dragonborn address the reader as "you". The rule exempts descriptions from the voice law; consistency is a taste call.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** Julio, 2026-09-07 (the rule-voice rewrite and the Dwarf text); inspiration lines and conventions pending.
- **What changed:** `1bf3439` launcher; `a1221a1` Dwarf description in first person plural and the corrected docstring; this branch's rule-voice commit for Dwarf, Dragonborn and Tiefling entries plus the self-test extension.
- **Practice/preference to remember:** a self-test that encodes a house rule must run over every member of the axis, not one specimen; the recovery voice ("X granted Y", "Gained at Level N") is a signature to grep for after any vault restore.

---

## 🏛️ Council

> Lorekeeper (Elf Sage): The sheet is read by a player at the table. "Gained at Level 1" tells them their own past; the rule tells them what they can do tonight.
> Understanding Consul (Bard): Elves and Halflings already found the voice. Copy the shape, propose the lines, let Julio own the words.
> Readability Consul (Barbarian): One assertion over ten species is worth more than ten reviews.

**Weighting:** reach 2 × severity 2 = **4** · council leaning: `build` (rule voice) · `needs Julio` (inspiration lines, two conventions)
