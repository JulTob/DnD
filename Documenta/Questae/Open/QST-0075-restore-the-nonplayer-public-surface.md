# QST-0075 — Restore the NonPlayer public surface

- **Type:** recovery
- **Priority:** 🟡 normal (post-beta)
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Architecture, TagKit
- **Parent:** QST-0016 (unify PC and NPC on the Character root)
- **Sidequests:** —
- **Related:** Decree 0006 · QST-0072 · QST-0073 · QST-0074

---

## 🔍 Diagnosis (what & where)

`AtlasActorLudi/AtlasAlusoris/__init__.py` is a one-line recovery stub. The public NonPlayer API that `app/main.py` composes (`nonplayer_choices`, `summon_nonplayer`, `summon_nonplayer_list`) is defined nowhere in source. The NonPlayer path served today goes through the legacy top-level `AtlasAlusoris` atlas (`Grimoire_of_NPC`), which QST-0016 was migrating away from.

`AtlasActorLudi/AtlasAlusoris/Map_of_NonPlayer_Paths.py` and `Map_of_Races.py` (vault bootstrap) survived; the package's public face did not.

## 🧾 Evidence

- `grep -rn 'def nonplayer_choices|def summon_nonplayer'` over the tree: no definitions (2026-08-29).
- The accident tar's `__pycache__` for `AtlasActorLudi/AtlasAlusoris/` is the best candidate evidence for the lost `__init__.py`.

## 🎯 Desired outcome

1. The Character-root NonPlayer surface is restored from evidence (recovery law order).
2. One NonPlayer and one NonPlayer-list generation verify against the pre-accident behavior.
3. The wing re-lights in the served app only when Julio widens the beta scope (Decree 0006).

## 🧭 Notes for the Agora / implementer

- Beta ships without this. Do not let NonPlayer recovery block or destabilize the character generator.
- The legacy `AtlasAlusoris` atlas keeps working meanwhile; it is evidence and fallback, not the destination.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council

> Architecture Consul (Druid): A wing rebuilt in the dark is rebuilt twice. Recover it when the lamps can be lit and looked at.

**Weighting:** reach 2 × severity 2 = **4** · council leaning: `defer`
