# QST-0013 — Ability modifier recomputed inline instead of the canonical `Modifier`

- **Type:** refactor
- **Priority:** 🟡 normal
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Contracts Consul (Warlock), Lorekeeper (Elf Sage), Methods Consul (Wizard)
- **Parent:** QST-0007 (Track A / shiny_app.py)
- **Sidequests:** —
- **Related:** `AtlasActorLudi.Map_of_Scores.Modifier`, TagKit-Doctrine (one source of truth per type)

---

## 🔍 Diagnosis (what & where)
The ability modifier is computed three ways: the real `Modifier` from `AtlasActorLudi.Map_of_Scores` (used in `build_npc_sheet`, L1400), a **fallback** `Modifier = (score-10)//2` (L42–43), and an **inline** `mod = (ivalue - 10) // 2` hardcoded in `build_character_sheet` (L1235). The character sheet bypasses the canonical function.

## 🧾 Evidence
- Canonical: `from AtlasActorLudi.Map_of_Scores import Modifier`; used at L1400 (`Modifier(value)`).
- Inline duplicate: L1235 `mod = (ivalue - 10) // 2`.
- Fallback duplicate: L42–43.

## 🎯 Desired outcome
One source of truth for the ability modifier — the canonical `Modifier` — used everywhere. No inline re-derivation of a game rule.

## 🧭 Notes for the Agora / implementer
Small change, but it's a **rules constant**: the Lorekeeper should confirm the 2024 formula (`floor((score-10)/2)`) and that it lives in exactly one `Map_/Compass_`. This is the pattern for *every* rule constant, not just this one.

## ✅ Resolution
*(pending — filled when Solved)*

---

## 🏛️ Council
> Lorekeeper (Elf Sage): The formula is correct 2024 canon, but a rule written in three places will eventually be *edited* in one. A rule constant must have a single home.
> Contracts Consul (Warlock): This is one-source-of-truth, plainly. Import `Modifier`; delete the inline copy. The fallback copy is QST-0009's problem.
> Methods Consul (Wizard): Trivial and correct. No objection.

**Weighting:** reach 1 × severity 2 = **2** · council leaning: `build`
