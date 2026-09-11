# QST-0111 — Harmony joins the Ideals, and the roster stops being counted

- **Type:** code / lore
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Technical Team · Lorekeeper · Julio
- **Related:** QST-0110 · QST-0050 · `Documenta/Canon/Mythos/Aasimar.md` §0 · `AtlasActorLudi/SpeciesKit/Aasimar/Map_of_Ideals.py`

---

## 🔍 Diagnosis (what & where)

The page carries a ninth Ideal that `Map_of_Ideals.py` does not have, and the
page no longer states how many Ideals there are. The code owes it both.

**Harmony is a primary Ideal, not a merger.** It does not descend from Beauty
and Justice: Justice does not affect mathematics, and Beauty does not affect a
ratio even when the ratio makes a beautiful sound. Proportion is its own
principle and answers to neither.

The row as the page states it:

| Field | Value |
|---|---|
| `name` | Harmony |
| `form` | rotating triangles with perfect proportions |
| `metal` | brass |
| `gem` | quartz |
| `tell` | It stutters when you are in pain, of body or of mind. |
| `muse` | Lyric & Flute (Euterpe) |

This closes Euterpe, who was the last Muse with no Ideal.

**The roster is open, and nothing should count it.** More Celestials may be
raised later, so no document states a number of Ideals. The Muses are the
principal Celestials of their kind, not a complete set, so a future Ideal may
arrive with no Muse at all and that is not a gap.

## 🧾 Evidence

Read out of the module: `IDEALS` holds eight entries and no Harmony. Every
counted reference in the wiki has been removed in the same change that opened
this Questa.

## 🎯 Desired outcome

1. `Map_of_Ideals.py` gains the Harmony entry exactly as the page states it.
2. Nothing in the code, the tests or the docs asserts a count of Ideals. Any
   test that hard-codes eight is rewritten to read the map.
3. A generated Aasimar can descend from Harmony, alone or mixed, and its talaria
   take brass while its aureola glows like quartz.
4. `Ideal.muse` is allowed to be empty without that meaning the entry is
   unfinished.
