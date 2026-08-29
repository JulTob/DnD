# QST-0056 — Features that name a benefit must grant it

- **Type:** bug
- **Priority:** 🟠 high
- **Status:** Open
- **Related:** QST-0051 · QST-0054

---

## 🔍 Diagnosis

The same class of bug that hid in DwarfKit and DragonbornKit, where Darkvision
and Resistances were described and never applied. Known remaining cases:

**Invocations that grant proficiencies.** *Beguiling Influence* (Deception and
Persuasion) and *Awaken Mind* (two skills from Arcana, History, Investigation,
Nature, Religion, plus expertise in one) print the grant and do not make it.
They must also handle the **overlap case**: if the Character is already
proficient, the invocation must not be wasted. Either repurpose the grant into
another available proficiency, or pick from what is still open.

**Spells named by a feature must reach the spell list.** *Touch of Death* (from
the Origin feat) names a spell that never enters `known_spells`, so it can
collide with chosen spells. Same shape as *Great Old One Spells* and *Mystic
Arcanum* in QST-0057.

**HTML leaking into spell text.** Tags are visible in the rendered Touch of
Death spell entry.

## 🎯 Desired outcome

Any feature naming a proficiency, a spell, a sense or a resistance also puts it
on the sheet's own ledger, and overlapping grants are repurposed rather than
lost.

## 🧭 Notes

`AtlasActorLudi/SpeciesKit/Dwarves/traits.py` shows the pattern for granting
rather than recording: read the current tuple, dedupe, write it back.
