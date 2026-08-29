# QST-0050 — A CelestialKit shared by Player Species and the NPC generator

- **Type:** refactor
- **Priority:** 🟢 low
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Design Team
- **Parent:** —
- **Sidequests:** —
- **Related:** `AtlasActorLudi/SpeciesKit/Aasimar/Map_of_Ideals.py` · `AtlasActorLudi/SpeciesKit/kinship.py` · wiki `Ǝ.Cl.-Celestials`

---

## 🔍 Diagnosis (what & where)

`Map_of_Ideals` lives inside `SpeciesKit/Aasimar/`, and everything in it
describes **Celestials**, not aasimar: the eight Ideals, their aureola forms,
their metals and gems, the angelic ranks in `DESCENTS`. An aasimar is only the
mortal end of it.

The same content is wanted in two other places and cannot currently reach
either:

1. **The NPC generator**, which should be able to roll an actual Celestial and
   describe it with the same Ideals and the same aesthetics.
2. **A link between the two.** An aasimar's descent line currently names *a
   Throne of Justice* as a phrase. It should be able to name a Celestial NPC
   that exists, so the ancestor is a character the DM can put in a scene.

Dragonborn has the identical shape waiting: a draconic ancestry that should
eventually point at a generated dragon rather than at a damage type.

## 🧾 Evidence

`AtlasActorLudi/SpeciesKit/Aasimar/Map_of_Ideals.py` holds `IDEALS`,
`DESCENTS`, `PERCHES` and `Celestial_Mark`. Only `Celestial_Mark` and `PERCHES`
are aasimar-specific; the rest is Celestial lore sitting in a Species package
because that is where it was first needed.

`kinship.py` already separates *what the rules call you* from *what you
resemble*, and an aasimar is `Celestial` kin while remaining `Humanoid`. That
distinction is exactly what a shared Kit needs in order to describe both a
Celestial and its mortal descendant without confusing them.

## 🎯 Desired outcome

A `CelestialKit` holding the Ideals, the aureola vocabulary and the angelic
ranks, read by:

- `SpeciesKit/Aasimar` for a player character's visible descent
- the NPC generator, for Celestials as creatures in their own right
- optionally, a link so a PC's named ancestor **is** a generated NPC

Solved when `Map_of_Ideals` no longer lives under a single Species, and both
consumers draw from one source.

## 🧭 Notes for the Agora / implementer

**Lore already settled with Julio, so it does not need re-deciding:**

- Celestials are **emanations from the Platonic World of Forms**, prior to gods
  and not worshippers of any. They embody an Ideal without compromise, carry a
  True Name that defines and limits them, and change only as mortal
  understanding of the Ideal changes. See the wiki page.
- The cultural register is **Roman practicality applied to metaphysics**: a
  Celestial is certain, and argues methodology rather than theory. Enriched by
  Sanskrit and Jain tradition, and by Buddhist detachment (the mission and
  nothing else). Abrahamic angel traditions are all in scope.
- **Stars, Constellations, Muses and Planets are Celestials too**, which is why
  `DESCENTS` holds Angel, Muse, Constellation, Star, Planet, Throne, Seraph.
  Some Ideals hold a Greek Muse's domain, recorded on `Ideal.muse`.
- **Saints belong to the Dwarves and must stay there.** They were deliberately
  removed from `DESCENTS`: mixing the two reads as one system when they are two.
- The eight Ideals are **alignment-independent and twistable**. "I claim
  Justice for your offence", "*you* must sacrifice for me", "Truth is what I
  say it is". Vengeance was rejected as an Ideal precisely because it is
  alignment-specific; a Celestial launders grievance as Justice.
- The aureola answers to **fidelity to the Ideal, not to virtue**. A tyrant
  with a perfect ring is intended.
- **Two axes, kept apart:** talaria take the *metal*, the aureola takes the
  *gem*. Nothing is made of either; the wings shine like a metal and the halo
  glows like a stone. Metals nod at the dwarven soul-metal without confirming
  anything, and that ambiguity is deliberate DM space.
- A descent may hold **two Ideals**: one lends the aureola its form, the other
  its gem.

**Do not** give any of this a mechanical effect. Celestial Revelation carries
the rules; this carries the face.

**Sequencing:** deferred by Julio until the Species prose pass (Elf, Goliath,
Tiefling, Dragonborn) is finished, so that the shape of every Species is known
before anything is lifted out.
