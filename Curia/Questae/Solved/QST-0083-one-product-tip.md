# QST-0083 — One product tip on `main`

- **Type:** rule-update / chore
- **Priority:** 🟠 high
- **Status:** Solved
- **Owner:** Julio + Cursor
- **Route to:** Paladin, Artificer, Julio
- **Parent:** QST-0052
- **Sidequests:** —
- **Related:** Decree 0008 · Dialog 0009 · Dialog 0010 · QST-0072

---

## 🔍 Diagnosis (what & where)

Several agent sessions shared one checkout. They force-moved `main`, staged
hundreds of unrelated files, and left Finder ` 2.py` copies. `origin/main` was
a 2025 Heroku line unrelated to the Player generator.

## 🎯 Desired outcome

1. **`main` is the working product** — one tip, one name.
2. Sessions use **worktrees**, not a shared checkout.
3. Mechanical guards (Decree 0008) back the process.

## ✅ Resolution

- **Decided by:** Decree 0008 (Julio, 2026-09-01)
- **What changed:**
  - Old `origin/main` archived as `archive/main-heroku-2025-08-07`.
  - Generator line pushed to `origin/main`; local `main` tracks it.
  - Temporary `origin/product` fast-forwarded to the same tip (retire when GitHub default is `main`).
  - `product`-as-canonical workaround **superseded** — hooks and branch discipline are the cure.
- **Practice/preference to remember:** Renaming the tip without hooks was a bandage. `main` + safepoints + questa branches + installed hooks is the long-term model.

---

## 🏛️ Council

> Safety Consul (Paladin): Two names trained agents to fear `main`. One name
> plus refusal hooks is honest.
>
> Workshop Consul (Artificer): Archive the Heroku fork; do not merge its history.

**Weighting:** reach ⟨3⟩ × severity ⟨3⟩ = **9** · council leaning: `build` — done via Decree 0008
