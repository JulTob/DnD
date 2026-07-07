# QST-0009 — Fallback import shim swallows errors and bloats the entrypoint

- **Type:** refactor
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Safety Consul (Paladin), Repair Consul (Cleric), Architecture Consul (Druid), Simplicity Consul (Monk)
- **Parent:** QST-0007 (Track A / shiny_app.py)
- **Sidequests:** —
- **Related:** QST-0003 (Flask/Shiny), QST-0004 (venvs)

---

## 🔍 Diagnosis (what & where)
shiny_app.py L29–153: a broad `try: import Atlas… except Exception as exc: print(...)` block redefines `Modifier`, `Race`, `Archetype`, `Legendary/Lair/Region`, `Character` (a ~30-line `FallbackCharacter`), and `NPC` (a ~50-line `FallbackNPC`) as **shadow models**. If any Atlas import fails, the app silently runs in a degraded fallback mode with only a printed line.

## 🧾 Evidence
- `except Exception as exc: print(f"Error importing Atlas modules: {exc}")` (L39–40) — swallows the traceback; app continues.
- ~120 lines of duplicated shadow-classes inside the entrypoint (L67–153) that can drift from the real models.

## 🎯 Desired outcome
Import failures are **loud and diagnosable** (fail fast, or a clearly-flagged, opt-in dev fallback via an env var), and the shadow models live outside the entrypoint (or are removed). No silent degraded mode in production.

## 🧭 Notes for the Agora / implementer
Do not simply delete the fallback if tests/dev rely on it — make it explicit (`GENLEGEND_FALLBACK=1`) and move it to a `fallbacks` module. Tie into QST-0004: the shim exists partly because of partial/mismatched environments.

## ✅ Resolution
*(pending — filled when Solved)*

---

## 🏛️ Council
> Safety Consul (Paladin): A bare `except Exception` that prints and continues is a silent failure by definition — the worst kind. In production this hides a broken deploy behind placeholder characters.
> Repair Consul (Cleric): And it destroys the traceback, so when a user reports "everyone is a Test Character," we have nothing to diagnose. Re-raise, or log the full stack.
> Simplicity Consul (Monk): The 120 lines of shadow-models don't belong in the entrypoint regardless. Move them out; the file loses a third of its noise.
> Architecture Consul (Druid): Make the fallback opt-in and external. No objection remains.

**Weighting:** reach 2 × severity 3 = **6** · council leaning: `build`
