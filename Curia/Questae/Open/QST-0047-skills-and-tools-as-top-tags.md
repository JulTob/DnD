# QST-0047 — Skills and Tools as TOP Tags

- **Type:** tagkit / refactor
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Architecture Consul (Druid), Contracts Consul (Warlock), Simplicity Consul (Monk)
- **Parent:** —
- **Sidequests:** —
- **Related:** QST-0020 (redesign Features with TOP), QST-0016 (Character unification)

---

## 🔍 Diagnosis (what & where)

`AtlasActorLudi/Grimoire_of_Skills.py` already models this domain properly in OOP: `Skill`, `Tool(Skill)`, `Weapon(Tool)`, `Armor(Tool)`, and `Char_Skills`, with `set_proficiency()` as the verb. The hierarchy is sound and maps cleanly onto a Tag family — this questa is **not** a claim that the model is ad-hoc.

What is missing is **Tag membership**: the module imports no TagKit, so training exists as object state rather than as something the Tag system can be asked about. And every *grant site* reaches past the model to poke attributes, each with its own fallback branch:

- `AtlasLusoris/BackgroundKit.py` — `_grant_skills` reads `char.skills`, and if it is not a `Char_Skills` it writes `char.background_skills = [...]` and returns. `_grant_tool` does the same, falling back to `char.background_tool`.
- `AtlasLusoris/AtlasOfFeatures/Map_of_Official_Origin_Feats.py` — `_grant_training` repeats the pattern a third time, falling back to `char.feat_training`.
- `AtlasLusoris/FeaturesKit.py` — `Skilled` calls `skills.activate_proficiencies(3, pool)` guarded by `hasattr`.

Consequences:

1. **Nothing can ask "is this Character trained in Stealth?"** through the Tag
   system. Membership is invisible; only a mutated object knows.
2. **Three parallel fallback bags** (`background_skills`, `background_tool`,
   `feat_training`) exist because grants can land before `Char_Skills` does.
   Whether they are ever reconciled depends on construction order.
3. **Provenance is lost.** Once `set_proficiency()` is called, nothing records
   whether the training came from a Background, an Origin Feat, a Guild, or a
   Species — so a sheet cannot explain *why* a Character is trained.
4. Tools and Skills are conflated: `_grant_tool` resolves a tool by
   `getattr(skills, pick)`, i.e. through the skills object.

## 🧾 Evidence

Behavioural audit (2026-08-07), applying every PC Background to a fresh
Player Character:

```
ability boosts applied : 61/61
origin feat applied    : 61/61
```

but a bare `Character` has no `skills`, so the same run leaves training in the
fallback bags rather than on any Tag. Feats show the same split:

```
Agitator          lang=["Thieves' Cant"]  training=['Musical_Instrument']   ← via char.feat_training
Field Lieutenant  training=['Performance']                                  ← via char.feat_training
```

`grep` confirms three distinct fallback attributes with no single reader:
`background_skills`, `background_tool`, `feat_training`.

## 🎯 Desired outcome

One contribution contract for training, matching the Feature contract in
QST-0020:

- a **Skill Tag** and a **Tool Tag** family, minted per skill/tool, so
  `char in Stealth` and `char in Thieves_Tools` answer directly — the existing
  `Skill` / `Tool` / `Weapon` / `Armor` hierarchy is the natural shape for it,
  so this is a Tag layer over a sound model, not a replacement of it;
- applying a Tag resolves one immutable per-Character grant that records
  **provenance** (Background / Origin Feat / Guild / Species);
- **Expertise and double-training** are expressible as Tag state rather than a
  boolean on a skill object;
- the three fallback bags disappear, because a Tag does not need `Char_Skills`
  to exist before it can be applied;
- Tools stop resolving through the skills object and own their own family;
- rendering reads membership; it performs no selection.

## 🧭 Notes for the Agora / implementer

- `AtlasActorLudi/Grimoire_of_Skills.py` (`Char_Skills`) is the current home and
  the thing being replaced or wrapped. Decide **wrap vs. replace** before
  starting: a wrapper keeps sheet code working during migration.
- Canonical skill names already exist as `CORE_SKILLS` in
  `AtlasLusoris/FeaturesKit.py`; tool names are the `ARTISAN_TOOLS` tuple in
  `AtlasLusoris/BackgroundKit.py`. Neither should be re-invented.
- Grant sites to migrate, in dependency order: Background (`_grant_skills`,
  `_grant_tool`), Origin Feats (`_grant_training`, `Skilled`), Guild training,
  Species traits.
- **Do not** widen this into the Feature/Entry redesign — that is QST-0020.
  This questa is training only.
- The 2024 rule that a repeated proficiency becomes Expertise (or is swapped)
  is a **rules decision**, not an implementation detail: if the migration
  forces the question, open a Dialog rather than inventing a policy.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Moved to Solved:** —

---

## ⚗️ Reward (separate dialog — do not fill during implementation)

- **Reward file:** *(pending distillation dialog)*
- **Distilled:** *(pending)*

---

## 🏛️ Council

> *(awaiting the Agora — routed to Architecture, Contracts, and Simplicity)*

**Weighting:** reach ⟨3⟩ × severity ⟨2⟩ = **6** · council leaning: `needs a Dialog`
*(Reach 3: every grant site and the sheet. Severity 2: design/consistency, not a live correctness bug — training does land today, just invisibly.)*
