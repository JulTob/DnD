# QST-0082 — First publish parks NPC and DM chrome

- **Type:** design / docs
- **Priority:** 🔴 urgent
- **Status:** Working
- **Owner:** Cursor (Grok)
- **Route to:** Julio · Architecture · Flow
- **Parent:** QST-0001
- **Sidequests:** —
- **Related:** Decree 0004 · `STRATEGY.md` · QST-0002 · QST-0050.2 · QST-0072

---

## 🔍 Diagnosis (what & where)

The live Home tablet still opens on **NPC Generator** and auto-rotates to it. The header still offers NPC and NPC List (`shiny_app.py`); `app/shell.py` also offers DM. First publish is the Player Character generator only. NPC and DM Atlas code is not ready to be a product, and working it now delays the cut.

## 🧾 Evidence

- Julio, 2026-08-31: keep only Character functionality for first publishing; deactivate other top-bar buttons and the NPC trait tablet in a recoverable way.
- `summon_player(seed=42, level=1)` is green (Nikolas Amexafa). `summon_nonplayer` is not (QST-0050.4 / QST-0081.5).
- Decree 0004 records the cut.

## 🎯 Desired outcome

Home shows only the Character generator. Header shows Home and Character. NPC / NPC List / DM buttons and the NPC tablet face remain in the source, hidden behind `PLAYER_ONLY_PUBLISH` in `app/publish_scope.py`. Navigation to parked pages lands on Home. Questae for NPC/DM/Epica wait until after first publish.

## 🧭 Notes for the Agora / implementer

- Do **not** delete NPC or DM modules. Flip the one flag to restore chrome.
- Do **not** use this questa to hide Artificer; that is QST-0050.2.
- Live preview launches `shiny_app:app`. Park both `shiny_app.py` and `app/` so `app.main` matches when it becomes the door.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** Decree 0004
- **What changed:** `PLAYER_ONLY_PUBLISH` in `app/publish_scope.py`; header NPC/List/DM and the NPC tablet face are `is-parked`; navigation to those pages lands on Home. Flip the flag to restore.
- **Practice/preference to remember:** first-publish scope lives in one flag, not in deleted files.

---

## 🏛️ Council

> Architecture Consul (Druid): one flag, markup kept, navigation gated — that is a park, not a demolition.
> Flow Consul (Sorcerer): the tablet must not still advertise NPC as the default face.

**Weighting:** reach 2 × severity 2 = **4** · council leaning: `build`
