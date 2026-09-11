# QST-0112 — The Celestial Warlock's patron prints a Python repr

- **Type:** bug (presentation)
- **Priority:** 🔴 critical (visible on every sheet of the specialization)
- **Status:** Solved
- **Owner:** Claude
- **Route to:** Technical Team · Lorekeeper
- **Related:** QST-0110 · QST-0111 · `AtlasLusoris/AtlasOfGuilds/WarlockKit.py` · `AtlasActorLudi/SpeciesKit/Aasimar/Map_of_Ideals.py`

---

## 🔍 Diagnosis (what & where)

`CELESTIAL_DESCRIPTION` draws a `Descent` **object** and interpolates it into
Julio's patron paragraph with `f"{descent} of {ideal.name}"`. `Descent` is a
plain frozen dataclass with no `__str__`, so the format call falls through to
`repr` and the whole roster lands on the sheet:

> …but especially that patron of yours, `Descent(kind='Throne', names=('Zafkiel',
> 'Ofaniel', 'Orifiel', 'Galgaliel'))` of Honor. Up there on their high cloud,
> judging us.

It reaches the composed Warlock entry through `extends=`, so it is not a debug
path: every Celestial Warlock has shipped with it.

The intent is recorded one paragraph above the bug, in the function's own
docstring: *"The kind and the Ideal come out of one named Dice Bag."* The kind,
not the roster and not an individual. The Aasimar names an individual ancestor
(`the {kind} {name}`) because a spark is inherited from somebody; a Warlock signs
with an office, which is also the joke the paragraph turns on.

Found while bringing `Map_of_Ideals.py` to the Aasimar page (QST-0110, QST-0111),
which is the only other consumer of `DESCENTS` and `IDEALS`.

## 🧾 Evidence

```
summon_player(guild="Warlock", specialization="Celestial", level=3, seed=5)
→ "that patron of yours, Descent(kind='Throne', names=(…)) of Honor."
```

## 🎯 Desired outcome

1. The patron reads as a being: **the Throne of Honor**, the Seraph of Sacrifice,
   the Muse of Beauty.
2. No other draw changes, so the same Character keeps the same patron.

## ✅ Resolution

`patron=f"the {descent.kind} of {ideal.name}"`. One expression, no new draw, and
the seeded paragraph is otherwise byte-identical.

Verified across three seeds: *the Throne of Honor*, *the Throne of Hope*, *the
Seraph of Sacrifice*.

**Left open on purpose.** Harmony now reaches this pool, so a Warlock may be
signed by the Muse of Harmony. That is correct and needs nothing.
