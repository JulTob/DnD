# QST-0062 — Feature entries: bloat, and five species written in a different voice

- **Type:** docs / design
- **Priority:** 🟡 normal
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Readability (Barbarian), Understanding (Bard), Simplicity (Monk), Lorekeeper
- **Parent:** —
- **Sidequests:** —
- **Related:** QST-0055 (voice sweep), QST-0061 (Order background entries), QST-0060 (sheet presentation)

---

## 🔍 Diagnosis (what & where)

Julio, reading an Orc sheet: *"'Orcish drive granted Adrenaline Rush.' is bloated text."*

The specific instances of that pattern have been removed (see Resolution note below). What remains
is the reason they existed: **five of the ten Species Kits are written in a register the other five
are not**, and the same register leaks into a few class Trainings.

### The two registers, side by side

Both of these are in the *same* Dwarf Kit:

> **Stonecunning** — "**Bonus Action.** Gain Tremorsense with a range of 60 feet for 10 minutes
> while on or touching a stone surface, natural or worked. The trait carries 4 uses per Long Rest."

> **Dwarven Toughness** — "One extra Hit Point, and one more at every level after: 12 in total at
> Level 12."

And this is the Aasimar Kit, which reads as the rulebook does:

> **Healing Hands** — "As a Magic action, you touch a creature and roll 4d4. The creature regains a
> number of Hit Points equal to the total rolled. Once you use this trait, you can't use it again
> until you finish a Long Rest."

**Aasimar, Dragonborn, Elf, Gnome and Human** address the reader in second person, as the 2024 rules
do. **Dwarf, Halfling, Orc, Tiefling and Goliath** use a clipped, agentless notation. Both are
legible; they are not the same book.

### What the second register does

Three habits, each reproducible:

**(a) Noun-phrase fragments instead of sentences.** "Darkvision with a range of 120 feet." · "A
reroll after rolling a natural 1 on the d20 of a D20 Test." · "Access to the Hide action while
obscured only by a creature that is at least one size larger." · "Defiance after reduction to 0 Hit
Points…" These state the rule correctly and never say *you*.

**(b) The feature is the subject, not the character.** "The trait carries 4 uses." · "The boon
carries 4 uses per Long Rest." · "The transformation carries 1 use per Long Rest." · "Advantage
applies to Strength checks, and Speed becomes 45 feet." · "Movement cannot end in that creature's
space." Five instances of "The *X* carries *N*" survive across Dwarf, Orc and Goliath.

**(c) Third person.** Goliath's **Powerful Build**: "…carrying capacity treats **this Character** as
one size larger." Goliath's Giant Ancestry: "After **this Character** hits a target…"

---

## 🧾 Evidence

Sweep 13 guilds × 10 species at level 12 and compare each description against its own heading and
against the rules' voice:

```python
import io, contextlib, re
from AtlasLusoris.Grimoire_of_Characters import Character, New_Player

buf = io.StringIO()
with contextlib.redirect_stdout(buf):
	c = Character(seed=88, level=12)
	New_Player(c, char_class="Fighter", species="Goliath", level=12)
for f in c.features:
	if getattr(f, "source", None) == "Species Feature" and f.level:
		print(f"[{f.name}] {f.description}")
```

Counts from that sweep, after the removals already made:

| pattern | instances | where |
|---|---|---|
| "The *X* carries *N*" | 5 | Dwarf, Orc, Goliath |
| "this Character" | 1 | Goliath (Powerful Build) |
| description restating its own heading | 0 real | *(the 18 raw hits are Julio's own Species descriptions, which correctly open with the people's name)* |

---

## 🎯 Desired outcome

A reader cannot tell which Species Kit was written first. Every feature entry speaks to the player
in the rules' own second person, and none of them narrates its own arrival.

"Solved" means the five clipped Kits read like the five that already work, with no rule lost or
changed in the move.

---

## 🧭 Notes for the Agora / implementer

- **This is a rewrite, and the prose is Julio's.** An implementer may not generate replacement
  wording to fill the gap. The mechanical removals below were safe because they deleted redundancy;
  turning "Defiance after reduction to 0 Hit Points" into a sentence is authorship.
- **Aasimar and Dragonborn are the reference.** They were rebuilt most recently and already read
  correctly; use them as the target, not a new style.
- **Do not touch the Species descriptions** (the level-0 entries). Those are Julio's, and opening
  with the people's name is deliberate.
- The 2024 rules are consistently second person and present tense — "You have Resistance to Poison
  damage", "You can see in Dim Light". Verify against the source rather than inventing a house
  voice.
- The remaining "The *X* carries *N* uses" is the most mechanical of the three and could be split
  into a sidequest if the full rewrite waits on Julio.

---

## ✅ Resolution (filled when Solved)

- **Decided by:** —
- **What changed:** *(partial, 2026-08-18)* — 19 restatements removed ahead of this quest, on
  Julio's instruction:
  - **17 in the five Species Kits** — every "Orcish drive granted…", "Dwarven senses granted…",
    "Halfling courage granted…", "Fiendish legacy granted…", "Giant heritage manifested as…",
    "Large Form awakened…" lead-in, plus two passive "*X* was established as its spellcasting
    ability" → "*X* is its spellcasting ability".
  - **`Skillful`** (`AtlasLusoris/FeaturesKit.py`) — "Skillful granted proficiency in Athletics."
    → "You have proficiency in Athletics."
  - **Ranger `Expertise`** (`Map_of_Ranger_Training.py`) — 5 × "You gained Expertise in" → "You
    have Expertise in", 2 × "you learned" → "you know".
  - SpeciesKit and FeaturesKit self-tests pass; no rule text was lost.
- **Moved to Solved:** —

---

## ⚗️ Reward (separate dialog — do not fill during implementation)

- **Reward file:** *(pending distillation dialog)*
- **Distilled:** *(pending)*

---

## 🏛️ Council

*(not yet convened)*

**Weighting:** reach ⟨2⟩ × severity ⟨1⟩ = **2** · council leaning: `build`
*(Reach: five Species Kits plus a little class Training. Severity: cosmetic — every rule is
correct, it is the voice that splits.)*
