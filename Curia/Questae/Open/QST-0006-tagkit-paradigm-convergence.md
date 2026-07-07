# QST-0006 — Treat TagKit as settled upstream (retire local-convergence premise)

- **Type:** docs/chore
- **Priority:** 🟢 low  *(mostly a correction; the premise was wrong)*
- **Status:** Open — largely resolved by Julio's ruling
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Methods Consul (Wizard)
- **Parent:** —
- **Sidequests:** —
- **Related:** `Canon/TagKit-Doctrine.md`, `requirements.txt`, Q-0003

---

## 🔍 Diagnosis (what & where)
**Correction (Julio's ruling):** this quest was minted on a false premise. It assumed TagKit's paradigm was *unsettled* and needed local convergence — because the only TagKit artifact in the repo was a stale draft guide with A/B/C/D comparison scaffolding. In fact:
- TagKit is a **finished, independent upstream project**: `github.com/JulTob/Tag_Oriented_Programming`.
- It is consumed as a **pinned dependency** in `requirements.txt` (`tagkit @ git+…@c7bd376…`), not vendored.
- The local stale guide is already gone; there is **no local TagKit to converge**.

## 🎯 Desired outcome
The Curia reflects reality: TagKit is settled + upstream; the project depends on it and proposes changes via **"Suggest to TagKit"** upstream quests (type `tagkit-upstream`), never by local convergence. (Canon already updated — `TagKit-Doctrine.md`.)

## 🧭 Notes
- **Done in this pass:** Canon `TagKit-Doctrine.md` rewritten (upstream model + Suggest-to-TagKit); the "open questions / follow implementation surface" language removed.
- **Remaining (small):** if you want, verify the pinned commit is the intended latest, and skim the GitHub Guide to confirm the API names we lean on (`Tag`, `Imprint`, composition). That's a quick check, not a convergence project.
- Q-0003 (the Agora question that framed convergence) is closed as **invalid premise**.

## ✅ Resolution
*(pending your nod to close — the substantive correction is applied; only an optional pin/API check remains)*

---

## 🏛️ Council
> Methods Consul (Wizard): The paradigm was never ours to settle — it lives upstream, pinned to a commit. My earlier "decorator-style" concern was reading a draft as if it were law. Withdrawn.
> Architecture Consul (Druid): Correct. Our concern is only that `AtlasTOP/` uses the API the pinned commit actually exposes. That's a check, not a convergence. Close the premise; keep the pin honest.

**Weighting:** reach 1 × severity 1 = **1** · council leaning: `defer`/close (premise corrected)
