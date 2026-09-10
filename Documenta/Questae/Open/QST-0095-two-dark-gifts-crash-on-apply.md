# QST-0095 — Two Dark Gifts crash on apply and kill the Character

- **Type:** bug
- **Priority:** 🔴 urgent *(a shipped draw aborts generation)*
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Technical Team · Methods (Wizard)
- **Related:** QST-0078 (silent fallback) · `AtlasLusoris/AtlasOfFeatures/Map_of_Official_Origin_Feats.py`

---

## 🔍 Diagnosis (what & where)

`Echoing_Soul.awaken` and `Symbiotic_Being.awaken` both open with

```python
from AtlasLudus.Map_of_Languages import STANDARD_LANGUAGES
```

`STANDARD_LANGUAGES` does not exist in that module, or anywhere else in the
repository. The `ImportError` surfaces as `TagKit.errors.TagImprintError` and
aborts the whole Character.

This is on the live player path. A Human's Versatile draws from the enlarged
Origin feat pool, Dark Gifts included, so either gift can be drawn by an
ordinary generation request.

## 🧾 Evidence

- Measured: **4 per cent of seeded level-1 Humans fail to generate.** Six of a
  hundred and fifty in one sweep.
- The only three occurrences of the name in the repository are those two import
  lines and a note in `Documenta/Canon/Mythos/Human.md`.
- The module does define `all_languages` and `standard_languages` in lower case.

## 🎯 Desired outcome

1. The two gifts import a name that exists, or build their language list the way
   the other seven Dark Gifts do.
2. A generation sweep of at least 200 seeded Humans completes with no
   `TagImprintError`.
3. Consider whether a failing Origin feat should abort a Character at all, or
   whether the draw should be guarded the way `NewName` is.
