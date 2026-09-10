# QST-0103 — Legacy `Lucky()` raises NameError if anyone calls it

- **Type:** bug / dead code
- **Priority:** 🟡 normal *(dead today, a landmine tomorrow)*
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Technical Team
- **Related:** QST-0093.3 (delete what nothing imports) · `AtlasLusoris/Grimoire_of_Features/__init__.py`

---

## 🔍 Diagnosis (what & where)

The legacy `Lucky()` factory builds its description with an f-string that
interpolates `{char.proficiency_bonus}`, but `char` is a parameter of the inner
`apply()`, not of the factory. Calling it raises `NameError: name 'char' is not
defined`.

Nothing calls it today. It matters because `Map_of_Species.py` star-imports that
module, so the name is live in that namespace, and because every other legacy
twin builds successfully, which makes this one look safe.

## 🧾 Evidence

Reproduced by calling the factory. Every other legacy feat twin builds.

## 🎯 Desired outcome

1. Either the description resolves at apply time, the way an Entry callable
   should, or the legacy factory is deleted with its siblings.
2. Decide the fate of the legacy twin layer as a whole. Two twins (Alert, Tavern
   Brawler) currently carry more of the published text than the live feats do,
   so deletion should follow a comparison rather than precede it.
