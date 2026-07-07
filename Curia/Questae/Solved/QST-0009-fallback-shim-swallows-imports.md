# QST-0009 — Fallback import shim swallows errors and bloats the entrypoint

- **Type:** refactor
- **Priority:** 🟠 high
- **Status:** Solved (2026-07-07)
- **Owner:** Claude session 2026-07-07, ruled by Julio
- **Route to:** Safety Consul (Paladin), Repair Consul (Cleric), Architecture Consul (Druid), Simplicity Consul (Monk)
- **Parent:** QST-0007 (Track A / shiny_app.py)
- **Sidequests:** —
- **Related:** QST-0003 (Flask/Shiny), QST-0004 (venvs), Decree 0003 (Minions on logging)

---

## 🔍 Diagnosis (what & where)
shiny_app.py L29–153: a broad `try: import Atlas… except Exception as exc: print(...)` block redefined `Modifier`, `Race`, `Archetype`, `Legendary/Lair/Region`, `Character` (a ~30-line `FallbackCharacter`), and `NPC` (a ~50-line `FallbackNPC`) as **shadow models**. If any Atlas import failed, the app silently ran in a degraded fallback mode with only a printed line.

## 🧾 Evidence
- `except Exception as exc: print(f"Error importing Atlas modules: {exc}")` — swallowed the traceback; app continued.
- ~120 lines of duplicated shadow-classes inside the entrypoint that could drift from the real models.

## 🎯 Desired outcome
Import failures are **loud and diagnosable**; no silent degraded mode in production.

---

## ✅ Resolution
- **Decided by:** Julio, 2026-07-07 — chose **removal outright** (option B) over the council's opt-in-fallback leaning, *plus a protocol*: "Use minions to report failure and recover. Provide a character to the user, but report every error so we can handle it and fix it."
- **What changed:** commit `d220d38`.
  - Atlas imports in `shiny_app.py` are now plain top-level imports: a broken Atlas stops the app with the real traceback. All shadow models and the redundant `TYPE_CHECKING` duplicate block deleted (~124 lines).
  - The resilience moved to the summoning layer: `summon_character` and `summon_npc` retry up to 5 fresh seeds; each single attempt runs through an `@minion`-wrapped `_attempt_character` / `_attempt_npc`, so every failed attempt reports its full bug tree into the `@chronicler` account. Nothing fails silently; the user still gets a character unless the breakage is systemic — which is exactly when the app *should* refuse.
- **Practice/preference to remember:** **Import-time = fail fast; generation-time = report loudly and recover.** The observe/retry split of Decree 0003 applies: `@minion` observes and re-raises; the caller owns recovery (a fresh seed, not the same doomed one). Never keep shadow models of real domain classes — they drift and they lie. The council's opt-in-fallback option was drafted when nine files didn't compile; once the ground was repaired, the simpler removal won.

---

## 🏛️ Council
> Safety Consul (Paladin): A bare `except Exception` that prints and continues is a silent failure by definition — the worst kind. In production this hides a broken deploy behind placeholder characters.
> Repair Consul (Cleric): And it destroys the traceback, so when a user reports "everyone is a Test Character," we have nothing to diagnose. Re-raise, or log the full stack.
> Simplicity Consul (Monk): The 120 lines of shadow-models don't belong in the entrypoint regardless. Move them out; the file loses a third of its noise.
> Architecture Consul (Druid): Make the fallback opt-in and external. No objection remains.
> Vox: Julio heard the expansion of both options and ruled harder than the council leaned: no fallback at all, resilience at the summoning layer, every error reported. So it was done.

**Weighting:** reach 2 × severity 3 = **6** · council leaning: `build` · **ruled: build (variant B+protocol)**
