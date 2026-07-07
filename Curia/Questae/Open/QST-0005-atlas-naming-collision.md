# QST-0005 — Resolve AtlasLusoris vs AtlasAlusoris near-collision

- **Type:** refactor
- **Priority:** 🟡 normal
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Readability Consul (Barbarian) → **Q-0002**
- **Related:** `Canon/Conventions.md`

---

## 🔍 Diagnosis (what & where)
Two top-level Atlases differ by a single letter:
- `AtlasLusoris` — players/PCs (Backgrounds, Species, Classes, `Grimoire_of_Characters`)
- `AtlasAlusoris` — NPCs (Races, Archetypes, `Map_of_NPC`)

They are easy to confuse, easy to mistype, and both are load-bearing across imports in `app/routes.py` and elsewhere. This is a latent source of import bugs and reader confusion.

## 🧾 Evidence
`app/routes.py` imports from **both** in adjacent lines, e.g. `from AtlasAlusoris.Map_of_Races import race_weights` and `from AtlasLusoris.Map_of_Backgrounds import backgrounds`.

## ✅ Resolved by Decree 0002 — **merge, don't rename**
Julio's ruling dissolves the collision at the root: *Lusoris* is the character domain; *A-lusoris* (Non-player) is a **tag** on a Character, not a parallel Atlas. So **`AtlasAlusoris` folds into `AtlasLusoris`** — there is one character Atlas, and NPC is a Non-tagged Character. Q-0002's "rename vs alias" options are moot.

## 🧭 Notes for the implementer
- This merge is executed as part of the unification (QST-0016) and the AtlasTOP removal (QST-0018) — the NPC's `kind` flag becomes the Non/Player tag.
- Move `AtlasAlusoris`'s modules (Races, Archetypes, `Map_of_NPC`, `Grimoire_of_NPC`) into `AtlasLusoris`, updating imports (currently in `shiny_app.py`, `app/routes.py`, etc.). Do it in one deliberate pass; imports depend on exact names.
- Q-0002 is closed (superseded by the merge decision).
