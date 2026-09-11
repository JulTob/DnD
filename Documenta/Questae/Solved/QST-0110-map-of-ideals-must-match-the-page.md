# QST-0110 — `Map_of_Ideals` must match the Aasimar page

- **Type:** code / lore-fidelity
- **Priority:** 🟠 high
- **Status:** Solved
- **Owner:** Claude
- **Route to:** Technical Team · Lorekeeper · Julio
- **Related:** QST-0050 · `Documenta/Canon/Mythos/Aasimar.md` §0 · `AtlasActorLudi/SpeciesKit/Aasimar/Map_of_Ideals.py`

---

## 🔍 Diagnosis (what & where)

The page is the authority and the code adapts to it. Three entries in
`Map_of_Ideals.py` no longer match what the page states. All three are in one
file and one table, so they are collected here rather than split.

**1. Hope's form and tell are exchanged and rewritten.** The old `form` held a
description of visibility rather than a shape, which made it the only one of
eight that was not geometry. The page now reads:

| Field | Was | Is |
|---|---|---|
| `form` | *a faint thing in daylight and one unmistakable star in the dark* | **a band crowning around your temples** |
| `tell` | *When you are happy it spreads, slowly, until it covers all of you.* | **Faint in daylight, but unmistakable in the dark.** |

The new form is the laurel of victors and triumphs, which sits at the temples by
nature. Whether it rests there or floats is not stated, and should not be.

Note the consequence for the tell column. The other seven tells react to the
Aasimar's own state; this one reacts to circumstance. That is deliberate.

**2. Freedom's `muse` field is empty.** Dance, and therefore Terpsicore, is the
decided answer. Euterpe remains the one Muse with no Ideal.

**3. The Planetar roster lists Hesperus twice.** One should go.

**4. The mixed-descent weighting is deleted.** `MIXED_DESCENT = 2` and
`SINGLE_DESCENT = 3` skew a spark toward one Ideal three times in five. No
reason for the ratio is recorded anywhere: the comment above the constants
restates them without justifying them.

Nothing in the lore supports the skew, and one thing argues against it. Merged
concepts are how new Celestials come into being, so a mixed lineage is an
ordinary fact of the family tree rather than an exception. Primary Ideals are
few and mergers are combinatorial, so if the weighting leaned anywhere on
in-world grounds it would lean the other way.

The draw becomes even. Do not replace 2:3 with a different ratio.

## 🧾 Evidence

Read out of the module: `IDEALS` carries the stale Hope strings and the empty
`muse`; `DESCENTS` carries the duplicate under the Planetar kind.

## 🎯 Desired outcome

1. The three corrections land in `Map_of_Ideals.py`.
2. A generated Aasimar of Hope shows the new form and the new tell.
3. A generated Aasimar of Freedom can reach Dance through `Ideal.muse`.
4. Hesperus appears once in the Planetar roster.
5. A spark comes from one Ideal or two with equal chance, and no constant in the
   module encodes a preference.
5. No other field is touched: the metals, gems and remaining tells are current.

## ✅ Resolution

All four landed in `Map_of_Ideals.py`, and the page moved once more while the
work was in flight, so the values below are the page's and not this ticket's.

1. **Hope.** `form` = *a band crowning your temples*; `tell` = *It is faint when
   you wake up, but brighter as you get tired.* The diagnosis above quotes an
   earlier pass of the dialogue (*"a band crowning around your temples"*,
   *"Faint in daylight, but unmistakable in the dark."*): both were superseded on
   the page before this was implemented, the first for reading better without the
   *around*, the second because it was a tell about the light in the room rather
   than about the person carrying it. Hope is not desperation; it is the sign
   that says try again tomorrow, and it burns brightest when the day has run you
   down.
   The form is stored lower case, like every other form, because it is always
   read mid-sentence: *"Your aureola is a band crowning your temples."*
2. **Freedom's Muse is Dance** (Terpsicore). The empty string is gone.
3. **Hesperus appears once** in the Planetar roster.
4. **The weighting is deleted and not replaced.** A spark is now two draws from
   the whole list at uniform random, as the page states, with nothing removed
   from the pool between them. The same Ideal coming up twice *is* the single
   descent, so it needs no separate roll: over 4000 marks it lands at 10.5%,
   against the 11.1% an even nine-way draw predicts.

Two things not in the diagnosis were fixed in the same pass, both consequences of
the page rather than of the ticket:

- **The neck perch is gone.** Julio removed *the back of your neck | an
  embroidered collar* from the page's table in `aa43b74`, and the 📘 talaria
  paragraph he wrote in the same commit places them on *the arms and the legs,
  and the back*. Eight perches now, and the module comment follows the page's
  *nothing on the front side*.
- **Nine Medium to one Small.** The Size entry has stated the proportion all
  along and `Aasimar/__init__.py` declared no `size_weights`, so the draw was an
  even coin. It now declares `(90, 10)`, the way `Humans.py` declares `(95, 5)`.
