# 🏛️ The Agora Protocol

> *The Agora is the council of the project. Here, questions are not answered by decree of a single agent, but reasoned through by the Consuls until the best path is clear — and then carried to Julio, who decides.*

The Agora exists because **no single agent's opinion is trustworthy enough to become a rule.** Good decisions come from constructive disagreement between focused experts. This protocol turns a question into a reasoned recommendation and, ultimately, a **Decree**.

---

## 🎭 The players

- **Consuls** — the expert voices. Each has a single lens (performance, clean code, abstraction & modeling, security, …). Charters in `Consuls/`. Consuls are filled by agents today and expandable to humans later.
- **Vox** — the Speaker. Vox does not hold an opinion; Vox *summarizes the council faithfully* for Julio. Charter in `Consuls/Vox.md`.
- **Julio** — the single source of truth. The Agora prepares the choice; Julio makes it.

Any agent or Consul — or Julio — may **throw a question to the Agora.**

---

## 🔁 The protocol, step by step

### 1. A Question is posed
Add an entry to `Agora/Questions.md` (short: the question, who asks, links to any Questa). Open a discussion file in `Agora/Dialogs/` named `NNNN-short-slug.md` from the template.

### 2. The issue is framed
The opening of the Dialog states: the question, the context, the constraints from Canon, and which Consuls are called (all, or a named subset marked on the Questa).

### 3. The Consuls deliberate (Socratic)
Each called Consul writes in the Dialog file, **signing every contribution**:

```
Architecture Consul (Druid): <reasoning, from the architecture lens only>
Methods Consul (Wizard): <reasoning, from the methods lens only>
Readability Consul (Barbarian): <…>
```

The full roster of seats (class-embodied) lives in `Consuls/`. Convene **1 voice** for simple quests, **2–4** for most, the **full council** only for complex, multi-domain work.

Rules of the conclave:
- Each Consul argues **only from its lens.** It does not police other lenses.
- Consuls **respond to each other** — agree, refine, object, concede. This is dialogue, not parallel monologues.
- Every objection must be **constructive**: name the problem *and* a way forward.
- Each Consul should ultimately offer a **concrete proposal** (ideally with a code sketch) from its viewpoint.

### 4. Convergence
The discussion **ends only when no Consul has an unanswered objection** and constructive feedback has been given by all called Consuls. Consensus does not mean unanimity of preference — it means every objection has been heard and addressed.

### 5. Vox reports to Julio
Vox writes a summary at the foot of the Dialog and surfaces it to Julio. The report contains, always:
- **Common ground** — what all Consuls agreed on.
- **The options** — each viable path, with its **tradeoffs**.
- **Consul recommendations** — who favored what, and why.
- **Code proposals** — concrete sketches, not just prose.
- **Vox's synthesis** — the council's leading recommendation *and* the strongest alternative.

Vox never hides a dissent and never presents only the top pick.

### 6. Julio decides
Julio may pick the top recommendation, an alternative, or a blend — or send it back for more deliberation. The choice is recorded as a **Decree** in `Agora/Decrees/` (drafted by an agent, ratified by Julio).

### 7. The Decree spawns work
Chosen solutions become new **Questae** in `Questae/Open/`, each scoped to a specific implementation step. The Dialog is marked *closed* and linked from the Decree.

---

## 🧷 Standing rules

- **Diagnose before prescribing.** A Questa describes a problem; the Agora proposes solutions. Do not pre-bake the answer into the ticket.
- **One discussion, one file.** Keep `Dialogs/` one-topic-per-file so memory stays searchable.
- **Decrees are memory.** Once settled, a Decree is binding on all agents and readable by all — it is how the project remembers its preferences.
- **Speak in character, reason in earnest.** Conclave tone is encouraged; rigor is required.
