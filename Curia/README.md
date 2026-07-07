# ⚜️ The Curia

*The senate-house of the project. Where the law is kept, the newcomers are trained, and the councils are held.*

The **Curia** is the coordination layer of this codebase. It is **tool-agnostic** and **human-readable**: it does not depend on any particular AI assistant, editor, or agent framework. Whatever assistant sits at the desk — a current tool, a future tool, or a human programmer — it reads the Curia first and obeys it.

> **One rule above all:** the single source of truth is **Julio**. Agents propose; the Agora deliberates; **Julio decides**. Nothing here overrides that. See `Canon/Single-Source-of-Truth.md`.

---

## 🗺️ Map of the Hall

```
Curia/
├── README.md              ← you are here
├── Vademecum.md           the newcomer's first read (human or agent)
│
├── Canon/                 the LAW Julio sets — agents read, never edit
│   ├── Single-Source-of-Truth.md
│   ├── Conventions.md         naming & lore (Atlas / Map / Grimoire / Compass…)
│   ├── TagKit-Doctrine.md     Tag-Oriented Programming: how to use & extend TagKit
│   └── Code-Style.md          light, readable, anti-overengineering rules
│
├── Agora/                 the Socratic council
│   ├── Agora-Protocol.md      how a question becomes a decree
│   ├── Questions.md           the open questions queue
│   ├── Consuls/               one charter per expert voice
│   ├── Dialogs/               one file per live discussion
│   └── Decrees/               settled decisions, kept forever
│
├── Agentia/               the working agents (envoys of the Curia)
│   ├── README.md              the roster + how agents must behave
│   ├── Scout.md               watches 5e.tools / wikidot → opens discussion, never pushes
│   ├── Legal-Reviewer.md      IP guardrails (Open-D&D safety)
│   ├── Design-Team.md         Open-D&D rule variations
│   ├── Technical-Team.md      balance & engineering review
│   └── Agents-Compliance.md   binds every agent tool to this Canon
│
└── Questae/              the ticket system (issues, refactors, designs)
    ├── README.md              how questae work
    ├── QUESTA-template.md
    ├── Open/                  minted, awaiting the Agora or a hand
    ├── Working/               claimed and in progress
    └── Solved/                closed — kept as memory of practice & preference
```

*(Folder names are chosen for flavor and intuition. Each ticket is a **Questa** — a quest — id-prefixed `QST-####`.)*

---

## 🔁 How work flows through the Curia

1. **A need appears** — a bug, a refactor, a new rule from the Scout, a design idea, or a question from Julio.
2. **A Questa is minted** in `Questae/Open/` describing the need. Tickets *diagnose*; they do not pre-solve.
3. **The Agora convenes** for anything requiring a decision. The Consuls deliberate by Socratic dialogue in `Agora/Dialogs/`, each signing its lines (`Architecture Consul (Druid): …`).
4. **Vox speaks** — the Speaker summarizes the council for Julio: the consensus, the common ground, the tradeoffs, and concrete code proposals. Not one verdict — the reasoning.
5. **Julio decides.** The decision is recorded as a **Decree** in `Agora/Decrees/` and becomes binding on all agents.
6. **New Questae are minted** for the chosen implementation. Work proceeds. Solved questae are archived as memory.

Nothing is pushed to the codebase from an external rule source (a new D&D ruling, a design variation) without passing through a Questa and — if it changes rules or architecture — the Agora.

---

## 🧭 Reading order for a newcomer

1. `Vademecum.md` — orientation and etiquette
2. `Canon/Single-Source-of-Truth.md` — who decides
3. `Canon/Conventions.md` + `Canon/Code-Style.md` — how we write
4. `Canon/TagKit-Doctrine.md` — the paradigm this project is built on
5. `Agora/Agora-Protocol.md` — how we decide together
6. `Questae/README.md` — how to pick up work
