# QST-0011 — NPC-list entries are dead links (`href="#"`)

- **Type:** bug
- **Priority:** 🟠 high
- **Status:** Solved (2026-07-09)
- **Owner:** unclaimed
- **Route to:** Implementation Consul (Fighter), Understanding Consul (Bard)
- **Parent:** QST-0007 (Track A / shiny_app.py)
- **Sidequests:** —
- **Related:** QST-0008, shareable-hash routing (L1655+)

---

## 🔍 Diagnosis (what & where)
`npc_list_result` (shiny_app.py ~L2257) renders each of the 5 NPCs as `ui.tags.a(..., href="#")`. The links go nowhere — clicking a listed NPC does not open its sheet. The old Flask app linked each list entry to `/npc/<race>/<archetype>/<level>/<seed>`.

## 🧾 Evidence
- `href="#"` on every row (L2273); no click handler routes to the NPC panel.
- NPCs in the list are built with deterministic `seed=seed+idx` (L2215) — so a deep link *could* reconstruct each one.

## 🎯 Desired outcome
Clicking a listed NPC opens that exact NPC's sheet (via the NPC panel and/or a shareable hash, mirroring the character deep-link that already works).

## 🧭 Notes for the Agora / implementer
The character side already has hash routing + `CharacterPathRedirectASGI`; consider the symmetric path for NPCs rather than inventing a new mechanism. May spawn a sidequest for "NPC shareable URLs" if we want parity.

## ✅ Resolution
- **Decided by:** Julio (refactor go, 2026-07-09)
- **What changed:** commits `81c66cf` + `19d1643`. Each list row is an action link; clicking shows that exact stored NPC on the NPC page. `NPC_LIST_SIZE` shared by generator, renderer, and observers.
- **Practice/preference to remember:** the stored object is shown directly because same-seed regeneration is not reproducible today (mixed RNG sources) - recorded as evidence for Dialog 0003 / QST-0016. A user who clicks a name must get that name.

---

## 🏛️ Council
> Implementation Consul (Fighter): The link literally does nothing on click — the feature reads as present but isn't. That's a correctness gap, not cosmetics.
> Understanding Consul (Bard): Users will click a name and expect the sheet. The seeds are deterministic, so the target exists; we just need to wire the route. Mirror the character deep-link. No objection.

**Weighting:** reach 1 × severity 2 = **2** · council leaning: `build`
