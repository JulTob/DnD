# QST-0052 — Generated names can carry a trailing space

- **Type:** bug
- **Priority:** 🟡 normal
- **Status:** Solved
- **Owner:** Claude
- **Route to:** —
- **Related:** QST-0051

---

## 🔍 Diagnosis (what & where)

Some generated names end in a space, which shows anywhere a name is
interpolated into a sentence. It surfaced in the Tiefling Species description,
whose hook formats `{name}` mid-sentence.

## 🧾 Evidence

Rendered from a generated Tiefling:

	Think about how your experiences as a Tiefling have shaped your path,
	and how Veltis  would approach new people during the campaign.

Two spaces between `Veltis` and `would`. The description itself has one space,
so the extra one is inside `char.name`.

## 🎯 Desired outcome

`char.name` never carries leading or trailing whitespace, and no interpolation
site has to defend against it.

## 🧭 Notes for the Agora / implementer

Fix at the source in the name generator rather than by stripping at every call
site. Likely a surname or epithet table joining an empty component, so check
for empty strings in the parts being joined rather than only trimming the
result. All ten Species descriptions interpolate `{name}`, so the blast radius
is every sheet.

---

## ✅ Resolution

- **Decided by:** Claude under the crisis mandate (Decree 0006 review scope);
  2026-08-31
- **What changed:** two guards in `AtlasNomina/Map_of_Names.py`. `_groomed`
  strips whitespace from every roster `Race_Ingredient` serves, preserving
  length and order so seeded index draws never move (the dirty entry itself,
  for example `"Veltis "`, lived in a race name table). `NewName`'s single
  exit collapses whitespace on both the stored given name and the returned
  full name, so no branch's join can leak a doubled or trailing space.
  Verified: 25 seeds generated with zero dirty names; the same seed still
  yields the same name.
- **Practice/preference to remember:** groom rosters where they are served,
  never where they are drawn: stripping entries is safe for determinism only
  while the collection keeps its length and order.
