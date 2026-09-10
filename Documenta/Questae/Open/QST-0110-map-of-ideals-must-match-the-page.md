# QST-0110 — `Map_of_Ideals` must match the Aasimar page

- **Type:** code / lore-fidelity
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
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
nature. It floats rather than rests, in line with the physiology chapter: the
aureola never touches the body whatever shape it takes.

Note the consequence for the tell column. The other seven tells react to the
Aasimar's own state; this one reacts to circumstance. That is deliberate.

**2. Freedom's `muse` field is empty.** Dance, and therefore Terpsicore, is the
decided answer. Euterpe remains the one Muse with no Ideal.

**3. The Planetar roster lists Hesperus twice.** One should go.

## 🧾 Evidence

Read out of the module: `IDEALS` carries the stale Hope strings and the empty
`muse`; `DESCENTS` carries the duplicate under the Planetar kind.

## 🎯 Desired outcome

1. The three corrections land in `Map_of_Ideals.py`.
2. A generated Aasimar of Hope shows the new form and the new tell.
3. A generated Aasimar of Freedom can reach Dance through `Ideal.muse`.
4. Hesperus appears once in the Planetar roster.
5. No other field is touched: the metals, gems and remaining tells are current.
