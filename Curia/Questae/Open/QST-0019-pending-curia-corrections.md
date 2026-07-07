# QST-0019 — Pending Curia corrections (to determine)

- **Type:** to-determine  *(a parking ticket — questions for Julio, not an action order)*
- **Priority:** 🟢 low
- **Status:** Open — awaiting Julio, item by item
- **Owner:** unclaimed
- **Route to:** Julio (decide) · then Barbarian/Bard for wording
- **Parent:** —
- **Related:** Canon (`Conventions`, `Code-Style`, `TagKit-Doctrine`), `.cursor` removal

---

## 🔍 Purpose
A single place to hold the small corrections Julio raised, so none are lost while we work **step by step**. **Nothing here is acted on without Julio picking it up.** Each is a `Council call` / `to determine` item.

## 🧾 The parked items
1. **Delete QST-0006 entirely** — Julio would rather remove it than leave a confusing quest. (Currently repurposed; his preference was outright deletion.)
2. **Strip leftover `.cursor` references from Canon** — `.cursor` was deleted (it collided with the Curia). `Conventions.md`, and any other Canon/agent file, should not reference Cursor. It was a breach of abstraction.
3. **Conventions table wording** — list Atlases as just the meaningful word (`Pugna`, `Nomina`, `Scriptum`…), not `AtlasPugna` etc. The "OneWord" glued form is hard to read in a reference table.
4. **`Makrotag`, not "God-object"** — in Code-Style, the "bridge/God-object is a smell" line is off in TOP: a Target grows dynamically and that's fine if the Tag structure is clear. Reframe the smell as a **Makrotag** (a God-*Tag*), and aim the warning at object-centric bloat.
5. **TagKit-Doctrine updates (needs the GitHub Guide):** `Augmentation/Extension/Mutation` were draft-only — drop them; **Underlay** is the current thought process. Revisit **Conditions**. Reconsider the "one source of truth per type" line (Tags crunch objects with records/actions and *overwrite often*, so the rule as written doesn't fit).
6. **`if kind == "wizard"` → `agent in Wizard`** — record the TOP idiom as the pattern to prefer (once we're tagging).

## 🧭 Notes
- Items 1–4 are quick wording/cleanups once Julio confirms each.
- Item 5 should wait until we can read the settled GitHub TagKit Guide, so the doctrine reflects the real API (Underlay, Conditions, etc.).
- Take them one at a time, in conversation — do not batch.

## ✅ Resolution
*(open — resolved item by item as Julio decides)*

---

## 🏛️ Council
> Bard (Understanding): This is a holding pen, not a work order — its whole job is to keep threads from dropping while we move slowly. Each line waits for Julio.
