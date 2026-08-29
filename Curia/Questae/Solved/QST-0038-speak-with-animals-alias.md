# QST-0038 — Speak with Animals Lodge alias

- **Type:** bug
- **Priority:** 🔴 urgent
- **Status:** Solved
- **Owner:** session 2026-08-29
- **Route to:** Repair Consul (Cleric)
- **Parent:** —
- **Sidequests:** —
- **Related:** QST-0009 (summon retries hide catalogue import failures) · Lodge alias block in `AtlasMagia/Lodge_of_Spells.py`

---

## 🔍 Diagnosis (what & where)
`ForestGnomeLineage` (`AtlasLusoris/Grimoire_of_Features/__init__.py:1160`) imports `SpeakWithAnimals` from the Lodge. The Lodge's canonical symbol is `SpeakwithAnimals`. Python raises `ImportError`. About half of Gnome draws pick Forest lineage; five summon retries often still fail. Share URLs such as `#/3/Gnome/Soldier/Fighter/He/28` showed **CHARACTER GENERATION FAILED**.

## 🧾 Evidence
```
cannot import name 'SpeakWithAnimals' from 'AtlasMagia.Lodge_of_Spells'
```
Canonical object exists: `SpeakwithAnimals.name == "Speak with Animals"`. The Plants spell already keeps both `SpeakWithPlants` and `SpeakwithPlants`.

## 🎯 Desired outcome
Forest Gnome lineage constructs. Importing either Lodge name yields the same Spell. A Gnome Generate returns a sheet.

## 🧭 Notes for the Agora / implementer
Do not rename the canonical Lodge symbol (call sites already use `SpeakwithAnimals`). Add a compatibility alias, same pattern as `SpeakwithPlants = SpeakPlants`.

---

## ✅ Resolution
- **Decided by:** Julio, 2026-08-29 — fix the Gnome issue, or alias for compatibility with Speak With Animals.
- **What changed:** `SpeakWithAnimals = SpeakwithAnimals` in the Lodge alias block. `ForestGnomeLineage` keeps the CamelCase import. Lodge self-test asserts identity and the display name.
- **Practice/preference to remember:** Lodge spell symbols should accept the natural CamelCase of the published title as an alias. Do not make the summoner retry absorb a missing name.

---

## 🏛️ Council
> Repair Consul (Cleric): The wound is a name mismatch, not a missing spell. Alias at the Lodge, the one place catalogues grow.

**Weighting:** reach 1 × severity 3 = **3** · council leaning: `build`
