# QST-0080 — Latent NameErrors and the damaged Scores map

- **Type:** bug / recovery
- **Priority:** 🟡 normal (off the live path today)
- **Status:** Open
- **Owner:** unclaimed (Codex foundation lane; claim on the recovery board)
- **Route to:** Workshop
- **Parent:** QST-0072
- **Sidequests:** —
- **Related:** QST-0079

---

## 🔍 Diagnosis (what & where)

The QST-0079 sweep found more of the same disease, currently dormant:

1. `AtlasActorLudi/Map_of_Scores.py` never imports `random` but defines
   `roll_stat`/`generate_stats` that use it; worse, its middle is visibly
   accident-damaged: a stray dict fragment (tab-indented) sits interleaved
   before a space-indented duplicate of the same functions. Generation does
   not import this module for rolling (the Character's own Dice path does
   that), so the damage is latent, but the file is not healthy source.
2. `AtlasLudus/Compass_of_Damages.py` calls `random.choice` in three
   classmethods without importing `random`: any caller of those random
   pickers will NameError.
3. `Training/Ranger.py` picks a random subclass when none is requested but
   never writes it back, so the sheet's Subclass field renders empty for
   random Rangers.

## 🎯 Desired outcome

1. `Map_of_Scores.py` restored from evidence (accident tar pycache first) or
   deliberately retired if the Character root has truly absorbed its duties.
2. `Compass_of_Damages.py` imports what it uses, with a caller check.
3. A random-summoned Ranger's subclass appears on the sheet like any other.

## 🧭 Notes for the Agora / implementer

Files 1 and 2 sit in Codex's foundation lane on the recovery board: claim
there before editing. The static sweep that found these
(`git grep 'random\.'` against import headers) is cheap; consider making it a
standing verification step.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council

> Workshop Consul (Artificer): A module that names a tool it never picked up
> will drop it exactly once: in front of a user.

**Weighting:** reach 2 × severity 2 = **4** · council leaning: `build`
