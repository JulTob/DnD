# QST-0035 — TagKit rollout sequence (after Phase 0)

- **Type:** tagkit / design
- **Priority:** 🟠 high
- **Status:** Open — sequence for Agora evaluation, not implementation order by itself
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Methods Consul (Wizard), Contracts Consul (Warlock), Lorekeeper
- **Parent:** QST-0016 (Character root flagship)
- **Sidequests:** —
- **Related:** QST-0020 (Features TOP), QST-0031 (Spells TOP), QST-0019 item 5 (Underlay/Conditions doctrine), Decree 0002

---

## 🔍 Diagnosis (what & where)
TagKit is pinned in `requirements.txt` but still largely **unimported in domain code** — a clean slate after Phase 0 (real generation, no import shim, AtlasTOP removed). The project needs an agreed **rollout order** for layering Tags onto the generator so work does not scatter or invert dependencies.

## 🧾 Evidence
- Parked plan (formerly `GENLEGEND_STATUS_AND_PLAN.md` §3): proposed sequence —
  1. **Conditions** (`Map_of_Conditions`) — overlay Tags on one creature-Agent.
  2. **Species / Class / Background** — Tags on one stable identity (QST-0020 for Features).
  3. **Resistances / Weaknesses / Senses** (AtlasPugna) as contributions.
  4. **Spell effects / Enchantments** as Imprint/Rip duals.
- QST-0016 sidequests (`.1`–`.6`) cover the Character root; QST-0031 covers spells in parallel — this quest **sequences the cross-Atlas TOP axes** after the root exists.
- Doctrine note: consult the pinned TagKit Guide before designing; QST-0019 item 5 (Underlay, Conditions) still awaits settled upstream text.

## 🎯 Desired outcome
Julio ratifies a **ordered rollout** (which axis first, which blocked on which) so implementers know what to tag next and what must wait. Each step becomes or links to an existing sidequest — this quest does not absorb implementation.

## 🧭 Notes for the Agora / implementer
- **Do not patch piecemeal** — sequence is for planning; each step gets its own questa once approved.
- Natural dependency: Character root (QST-0016) before role/species/class Tags; Features (QST-0020) after root; Spells (QST-0031) may proceed in parallel once spell Tag shape is decreed.
- Open a Dialog if Conditions vs. Species ordering conflicts with Decree 0002's minimal Character design.

---

## ✅ Resolution
*(pending — Agora sequence ratification)*

---

## 🏛️ Council
> Architecture Consul (Druid): Order matters — tagging Conditions before a stable Character root invites rework. Root first, overlays second.
> Methods Consul (Wizard): The four-step plan is a sketch, not law — each step needs a litmus test and a sidequest before code.
> Contracts Consul (Warlock): Pugna contributions and spell Imprint/Rip duals must share Compass types — one source of truth per axis, per Doctrine.

**Weighting:** reach 3 × severity 2 = **6** · council leaning: `needs a Dialog`
