# QST-0020 — Redesign Grimoire_of_Features with TOP

- **Type:** tagkit / design
- **Priority:** 🟠 high
- **Status:** Open — diagnosis only (do not patch piecemeal)
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Contracts Consul (Warlock), Simplicity Consul (Monk), Lorekeeper
- **Parent:** —
- **Related:** QST-0016 (Character unification — features become Tags), Decree 0002

---

## 🔍 Diagnosis (what & where)
`AtlasLusoris/Grimoire_of_Features/__init__.py` (~1,476 lines) models feats/features/invocations as **per-item factory functions** — `def Lucky(): … return Feat(name=…, apply=…, description=…)`. Julio's own read: this style **complicates growth immensely** (feats and invocations especially), and it invites bugs like baking character-dependent state into a feat at *construction* time.

## 🧾 Evidence
- `Lucky()` builds its `description` as an f-string referencing `char.proficiency_bonus`, but `char` doesn't exist at construction → `NameError` on every build (surfaced live via the Chronicler). This is a *symptom* of the design: a feat shouldn't hold a specific character's numbers.
- The file is a long list of near-identical factory functions — hard to extend, easy to break.

## 🎯 Desired outcome
Features/feats/invocations re-expressed as **TOP Tags** applied to a Character (per Decree 0002's composition direction): a feat is a Tag that contributes actions/records to the agent when applied; per-character values (like Luck Points = PB) are computed **at apply time on the character**, never baked into a static description. Simpler to grow, no construction-time character coupling.

## 🧭 Notes
- **Leave Lucky (and the rest) as-is for now** — this is a whole-file redesign, not a piecemeal patch. The `NameError` is tolerated until the redesign (the summon retry loop currently rerolls past it).
- Natural companion to **QST-0016**: once Character is the tagged root, features slot in as the same kind of Tag as species/class.
- Sequence after the Character root exists (QST-0016) so features have a clean surface to attach to.

## ✅ Resolution
*(pending — Agora design pass with QST-0016)*

---

## 🏛️ Council
> Simplicity Consul (Monk): A thousand near-identical factory functions is exactly the growth tax TOP removes. One Tag shape, many feats.
> Contracts Consul (Warlock): And it kills a class of bugs — a feat that computes a character's value at *build* time (Lucky) is a contract violation; values belong on the agent, at apply time.
> Architecture Consul (Druid): Do it *with* the Character-root work (QST-0016), not before — features want a tagged root to attach to.

**Weighting:** reach 2 × severity 2 = **4** · council leaning: `needs a Dialog` (with QST-0016)
