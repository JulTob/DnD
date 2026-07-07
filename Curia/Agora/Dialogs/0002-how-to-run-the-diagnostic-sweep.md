# Dialog 0002 — How to run the QST-0007 diagnostic sweep

- **Question (Q-0005):** How should we run the QST-0007 file-by-file diagnostic sweep — order, method, and how findings branch into questae/sidequests?
- **Raised by:** Julio (arbiter)
- **Related Questae:** QST-0007 (the sweep), QST-0004 (committed venvs), QST-0001 (finish the Shiny front)
- **Consuls called:** Full council — Bard, Druid, Artificer, Ranger, Monk, Rogue, Sorcerer, Wizard, Lorekeeper
- **Status:** 🟢 converged — awaiting Julio's arbitration

---

## 🧭 Framing
The Curia was seeded from a **first-pass** reading. QST-0007 is the **complete, file-by-file diagnostic** of the real source. The council is asked *not* to run it yet, but to decide **how** it should be run: what order, what per-file method, how to keep findings minimal and one-purpose, and how work should branch into **sidequests**. Canon constraints: **diagnose, don't solve**; **one purpose per questa**; **front is the priority** (QST-0001); the sweep is currently obscured by committed virtualenvs (QST-0004).

---

## 🗣️ Deliberation
*Each Consul argues only from its lens, signs every line, refines the others, and ends with something concrete.*

Understanding Consul (Bard): Before order or tooling, name the shape of the task. A "diagnostic" is a **mapping**, not a repair: for every real source file we produce *observations*, each of which is either "fine" or "a named problem." The unit of output is the **finding**, and a finding becomes exactly one minimal Questa. If we agree on that shape, everything else is logistics.

Architecture Consul (Druid): Agreed, and the logistics follow the structure of the system. Sweep **by boundary, in dependency order**: leaves first, roots last, so that when we read a caller we already understand its callees. Concretely — the `Compass_*`/`Map_*` data and type modules first, then the `Grimoire_*` cores, then the Atlas packages that compose them, then the app layer on top. One **sidequest per Atlas** keeps the tree legible.

Flow Consul (Sorcerer): One amendment, Druid — Julio's stated priority is the **front**. Pure dependency order would leave `shiny_app.py` for last. Propose a **two-track** sweep: Track A walks the runtime path that renders the app (`shiny_app.py` → the modules it actually imports) so we unblock QST-0001 fastest; Track B does the exhaustive boundary-order pass for completeness. Track A first.

Architecture Consul (Druid): Accepted — that's better. Track A is a spine; Track B is the full skeleton. No objection.

Workshop Consul (Artificer): I have to raise the floor we're standing on. The real source is buried under ~6 committed virtualenvs (QST-0004). If we sweep naively we'll drown in `site-packages`. But full cleanup is its own approved quest and needs Julio's confirmation to delete tracked files — we should **not** block the diagnostic on it. Proposal: a tiny **sidequest of QST-0007** that produces a *file manifest* — an enumerated list of real project files with venvs/`__pycache__`/`.git`/site-libs filtered out. The sweep reads the manifest; the deletion stays QST-0004.

Ecosystem Consul (Ranger): Second the manifest, and I'll own the filter — I know which paths are third-party terrain: every `*/lib/python*/`, `*/site-packages/`, `env/`, `.venv/`, `venv/`, `AtlasWorldBuild/venv/`, the R `site_libs/`, `.Rproj.user/`. One caution for the manifest sidequest: **distinguish** "our code that imports a dependency" from "the dependency itself." We diagnose the former; we only *inventory* the latter.

Simplicity Consul (Monk): Good — but hold the line on minimalism. One finding, one Questa, one purpose. The temptation in a sweep is the mega-ticket ("fix AtlasLusoris") that quietly swallows ten concerns. Rule for the sweep: if a finding has two verbs, it is two questae. Bigger work **branches a sidequest**, it does not fatten the parent. And resist scoring everything — see Wizard.

Methods Consul (Wizard): On ordering the *output*: once findings exist, they need a priority so Julio isn't handed 60 flat tickets. Propose a light score — **reach × severity**, each 1–3 (reach = how much of the system it touches; severity = correctness/safety > design > cosmetic). No framework, just two integers in the header. That's enough to sort.

Simplicity Consul (Monk): Accepted, with a leash: two integers, no rubric document, no tooling. The moment it needs a spreadsheet it has failed.

Testing Consul (Rogue): My concern is **coverage** — that nothing is silently skipped. The manifest is also the checklist: every file on it ends the sweep marked *read* with a verdict (clean / N findings). And a standing observation I'll turn into its own Questa regardless of the sweep: the project has **no test harness**, which makes every refactor these findings propose risky. That's a finding in its own right, not a blocker here.

Lorekeeper (Elf Sage): One lens the six-part checklist under-serves: **rules-correctness**. As we read generation code (modifiers, proficiency, dice, conditions) I will flag anything that diverges from 2024 canon or is unmarked homebrew. Those findings route to me and, where the expression is protected, onward to Design-Team and Legal-Reviewer. Add a seventh column to the per-file checklist: *game-canon*.

Understanding Consul (Bard): Then the shape is complete. Per file, seven lenses — architecture, methods, safety/contracts, simplicity/readability, naming-lore, **game-canon**, and testing-gaps — each producing zero or more one-purpose findings, sorted by reach×severity, delivered as a **digest**, not a wall.

Testing Consul (Rogue): No remaining objection.

Workshop Consul (Artificer): None here — manifest-sidequest first, then sweep.

Architecture Consul (Druid): Converged.

---

## ✅ Convergence check
- [x] Every called Consul has spoken.
- [x] Every objection answered or conceded (Sorcerer's front-first amendment; Artificer's manifest vs. cleanup; Monk's leash on scoring).
- [x] Concrete method on the table, with a sidequest structure.

---

## 🕊️ Vox report

Vox: Report on **Q-0005 — how to run the QST-0007 diagnostic sweep.**

**Common ground (unanimous):**
- The sweep **diagnoses, never solves**; output is a **digest**, not a wall.
- Unit of output = a **finding** → exactly **one minimal, one-purpose Questa**; bigger work **branches a Sidequest**, never fattens the parent.
- Per file, apply **seven lenses**: architecture · methods · safety/contracts · simplicity+readability · naming-lore · **game-canon (Lorekeeper)** · testing-gaps.
- Do **not** block the sweep on the venv cleanup (QST-0004); instead filter it out.

**Options & tradeoffs (the one real fork — how to handle the venv clutter):**
1. **Filter-now (manifest sidequest)** — a `QST-0007.1` produces an enumerated manifest of real project files, venvs excluded; the sweep reads that. *Pro:* unblocks immediately, no destructive action, no confirmation needed. *Con:* the clutter still sits in the repo until QST-0004 runs.
2. **Clean-first** — do QST-0004 (untrack/remove venvs + `.gitignore`) before sweeping. *Pro:* a clean tree for good. *Con:* needs your confirmation to delete tracked files, and delays the diagnostic.

**Consul positions:**
- Sorcerer & Druid: **two-track order** — Track A follows the app's runtime path (`shiny_app.py` → its real imports) to unblock the front (QST-0001) first; Track B is the exhaustive boundary-order pass (data/types → grimoires → atlases → app), one sidequest per Atlas.
- Artificer & Ranger: **filter-now**; Ranger owns the exclusion list and the "our-code vs dependency" distinction.
- Monk: minimalism leash — one purpose per questa; scoring is **two integers only**.
- Wizard: sort findings by **reach × severity** (each 1–3).
- Rogue: the manifest doubles as a **coverage checklist**; also mint a standalone finding — **no test harness exists**.
- Lorekeeper: add the **game-canon** lens to each file.

**Code/plan proposal (sketch):**
```
QST-0007  (parent: run the diagnostic)
├── QST-0007.1  sidequest: build the file manifest (Ranger's filter) — coverage checklist
├── Track A (front-first): shiny_app.py → its real imports   [unblocks QST-0001]
└── Track B (exhaustive): Compass_*/Map_* → Grimoire_* → Atlas packages → app/scripts
      ├── QST-0007.2  sidequest: sweep AtlasLusoris
      ├── QST-0007.3  sidequest: sweep AtlasAlusoris
      └── … one sidequest per Atlas …
Per file → 7-lens pass → each finding = one minimal Questa, header tagged  reach×severity (1–3 each)
Deliver: a digest of new questae, routed to the seat that owns each.
```

**Synthesis:**
- **Leading recommendation:** *Filter-now + two-track, front-first.* Throw `QST-0007.1` (manifest) immediately, sweep Track A to unblock the Shiny front, then Track B by Atlas. Keep QST-0004 (real cleanup) as its own quest for when you're ready to confirm deletions.
- **Strongest alternative:** *Clean-first* — if you'd rather I get your go-ahead on QST-0004 now and sweep a pristine tree, we lose a little time but gain a clean repo before the census.

→ **Awaiting Julio's decision.** Your arbitration sets the method; I'll record it as **Decree 0001** and open the resulting questae/sidequests accordingly.
