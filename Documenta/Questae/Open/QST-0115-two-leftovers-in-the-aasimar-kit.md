# QST-0115 — Two leftovers in the Aasimar kit

- **Type:** code / hygiene
- **Priority:** 🟢 low
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Technical Team
- **Related:** QST-0110 · QST-0113 · QST-0072 (recovery)

---

## 🔍 Diagnosis (what & where)

Two small things found while reading `SpeciesKit/Aasimar/` against the page.
Neither is visible on a sheet, so neither was folded into the fidelity work.

**1. `Celestial_Mark.glow_from` is written and never read.**
`Map_of_Ideals.py` sets it to `ideals[-1]` and stores it on the frozen dataclass.
Nothing anywhere reads it: `aureola()` takes its form from `shape_from` and its
colour from the `gem` property, which blends *both* Ideals (*"diamond shading
into aquamarine"*). So the field states something the generator does not do,
which is worse than absent: a later hand will trust it. Either drop it, or keep
it and correct the comment to say it is the second Ideal of the pair rather than
the one that lends the glow.

**2. `AtlasActorLudi/SpeciesKit/Aasimar/__init__.py.source-partial` is tracked
and byte-identical to `__init__.py`.** A recovery leftover (QST-0072). Deleting a
tracked file is not a thing to do in passing, so it was left; it should go.

## 🎯 Desired outcome

1. `glow_from` either goes or means what it says.
2. The `.source-partial` duplicate leaves the index.
