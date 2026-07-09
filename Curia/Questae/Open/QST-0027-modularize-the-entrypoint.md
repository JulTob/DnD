# QST-0027 — Modularize shiny_app.py: functions and files by concern

- **Type:** refactor
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** per Dialog 0007
- **Parent:** —
- **Sidequests:** —
- **Related:** QST-0021 (presentation Kits) · QST-0016 (root refactor uses these seams)

---

## 🔍 Diagnosis (what & where)
shiny_app.py (~1230 lines) still holds several concerns in one file: summoners, sheet builders and helpers, panel definitions, server wiring, ASGI redirect. Behavior-neutral module boundaries are wanted before the Character-root refactor, so each later step touches one small file, not the monolith.

## 🧾 Evidence
Decree 0002 (the ruled design) · Dialog 0003 (the deliberation) · Questions.md field note 2026-07-09 (seed non-reproducibility).

## 🎯 Desired outcome
The entrypoint reads as wiring only; each concern lives in its own module with a clear name per Conventions. Every move is behavior-neutral and separately verified.

## 🧭 Notes for the Agora / implementer
Order and safety strategy are designed in **Dialog 0007** with Julio. Nothing here moves without his word (Canon/Modus-Operandi.md).

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
*(convenes in Dialog 0007)*
