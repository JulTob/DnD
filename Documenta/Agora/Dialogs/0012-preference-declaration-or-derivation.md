# Dialog 0012 — Is the preference system a patch we keep re-applying?

- **Question:** Q-0015
- **Asked by:** Julio, 2026-08-24, in session
- **Called:** Architecture (Druid), Contracts (Warlock), Simplicity (Monk), Workshop (Artificer), Testing (Rogue)
- **Related:** Decree 0005 (Affinity steers selection) · `GuildKit.ability_weights` · QST-0066

---

## The question

> *"The preference system should unify the optimization scores for a unified system. But I'm
> wondering if we really need it. It solves a problem, but are we applying the solution if it
> keeps coming up? Or should we integrate it into the design steps?"* — Julio

Not "is `ability_weights` correct" — Decree 0005 settled that, and the causality points forward.
The question is **meta**: the fix has to be *applied by hand at every new site*. Is that a sign
the mechanism belongs one level down, inside the design steps, rather than being remembered each
time?

## Context

`ability_weights` is the single model of what a Character wants raised. Tags declare
`ABILITY_PREFERENCE` (what it wants) and `ABILITY_WEIGHT` (what its word is worth); every
score-choosing site reads the same dictionary.

**The recurrence is real and it drew blood this session.** Banneret was implemented with all six
features correct, and every one counts allies by the Charisma modifier. Nobody declared a
preference, so Bannerets rolled on the Guild's own STR/CON and came out at **Charisma 7 and 8** —
a rally subclass lifting exactly one ally, forever, with no error anywhere. Adding one line
(`"ABILITY_PREFERENCE": ("CHA",)`) moved the median to 16.

Eldritch Knight already carried its `INT` line. Psi Warrior and the Guilds carry theirs. So the
mechanism works — **when someone remembers.**

## Constraints from Canon

- `Feature-Text.md`: *explicit beats magical*; never infer at render time what can be written
  in the source.
- Decree 0005: **affinity is spent, not merely held.** A feature contributes affinity only where
  it *spends* the ability.
- `Single-Source-of-Truth.md`: one statement of a fact, not two that can drift.

---

## The conclave

**Architecture Consul (Druid):** I want to name the shape before anyone proposes anything. The
declaration is a *second statement of a fact the code already contains*. `_rallied_allies` calls
`_charisma_modifier`. The subclass spends Charisma in Python, and then a human writes down
separately that it spends Charisma. Two copies of one truth, no link between them, and the
failure mode is silence. That is the same defect as QST-0066, where `available_general_feats`
re-states every `@Pre` by hand. We have now found this pattern twice in one week, which suggests
it is structural rather than incidental.

**Contracts Consul (Warlock):** Then state the invariant plainly, because nothing currently does:
**a Tag that spends an ability must declare it.** That sentence is true, load-bearing, and
entirely unenforced. Nothing checks it, nothing fails when it is broken, and the breakage
produces a *plausible* Character rather than a crash. That is the worst class of contract — one
whose violation looks like a valid result.

**Simplicity Consul (Monk):** The obvious move is to delete the declaration and derive it. If
affinity is what a feature *spends*, and spending happens in code, then read the code: any
Specialization whose module references `cha_mod` spends Charisma. One source, nothing to
remember, nothing to drift.

**Architecture Consul (Druid):** I sympathise and I object. Derivation-by-introspection makes the
weight system depend on *how* a feature happens to be implemented. Rename a helper, inline a
call, read `AS.CHA` instead of `AS.cha_mod`, and a subclass silently loses its preference. We
would trade a fact somebody forgot to write for a fact somebody can accidentally erase — and the
second is worse, because writing is deliberate and refactoring is not.

**Simplicity Consul (Monk):** Conceded, and the Canon says it more sharply than I did: *explicit
beats magical.* Inference at a distance is exactly what `Feature-Text.md` forbids, and I was
proposing it one layer lower rather than avoiding it. I withdraw derivation as the primary.

**Workshop Consul (Artificer):** Can I re-frame the cost? Nobody here has yet said what actually
went wrong with Banneret. It was not architecture. It was that **the author did not know the step
existed.** Writing a subclass means: features, resources, registration, description, feature
lines — and, invisibly, a preference declaration if any feature reads a modifier. That last item
is in nobody's head and on no checklist. This is a developer-experience gap wearing an
architecture costume, and re-architecting to solve it is expensive medicine for the wrong disease.

**Testing Consul (Rogue):** Which points at the cheap answer. The question is not "declare or
derive" — it is **"how does the omission become loud?"** Derivation is one way to make forgetting
impossible; a failing test is another, and it costs a fraction as much. Use introspection **as an
auditor, not as the source**: scan each Specialization's module for ability-modifier reads, and
assert the declaration covers them. If a subclass spends Charisma and does not declare it, the
suite says so by name. The declaration stays authoritative and explicit; the code merely checks
that a human wrote it.

**Contracts Consul (Warlock):** That satisfies my objection, and it is the pattern we already
chose once. `Feature.__init__` refuses a callable with no subject rather than rendering an empty
string — an invariant we could not enforce structurally, converted into a loud failure at the
right place. This is the same move: the rule cannot live in the type system, so it lives in a
test that names the offender.

**Architecture Consul (Druid):** Agreed, with one addition. If introspection is only an auditor,
its fragility stops mattering — a false positive is a nuisance in CI, not a wrong Character on a
sheet. That asymmetry is what makes the compromise sound. I withdraw my objection.

**Workshop Consul (Artificer):** And answer Julio's actual question while we are here: **yes,
integrate it into the design steps** — but the design step is the *test*, not the architecture.
"Adding a Specialization" should have a written checklist, and the checklist's last line should
be enforced rather than trusted.

**Testing Consul (Rogue):** One more, since it is the same omission from the other side. Nothing
checks that a declared preference is *spent*. A subclass could declare `CHA` and never read it,
and the generator would happily raise a score the character has no use for. The auditor should
run both directions.

**Simplicity Consul (Monk):** Then the whole intervention is one test and one checklist entry.
Nothing is added to the runtime, nothing is removed from it, and the recurrence stops. That is
the smallest thing that could possibly work, which is the only proposal I am willing to sign.

---

## Code proposal

```python
# AtlasLusoris/GuildKit.py — self-test
_MODIFIER_READS = re.compile(r"\b(str|dex|con|int|wis|cha)_mod\b")

def _test_specializations_declare_what_they_spend():
    """
    Every Specialization that reads an ability modifier must declare it, and
    every declaration must be spent somewhere.

    Introspection is the AUDITOR, never the source: the declaration stays
    authoritative and explicit (Feature-Text.md, "explicit beats magical").
    A false positive here is a nuisance in CI; a missing declaration is a
    silently broken Character, which is how Banneret shipped rolling CHA 7.
    """
    for guild, spec in every_specialization():
        spent = {m.upper() for m in _MODIFIER_READS.findall(source_of(spec))}
        declared = set(getattr(spec, "ABILITY_PREFERENCE", ()) or ())
        assert not (spent - declared), (
            f"{spec.NAME} spends {sorted(spent - declared)} but declares "
            f"{sorted(declared) or 'nothing'}"
            )
        assert not (declared - spent), (
            f"{spec.NAME} declares {sorted(declared - spent)} but never "
            "spends it"
            )
```

Plus one line in the "adding a Specialization" checklist:

> **Declare what it spends.** If any feature reads an ability modifier, the Specialization's
> `ABILITY_PREFERENCE` must name it. The suite will tell you if you forget.

---

## 🕊️ Vox reports

**Common ground.** All five Consuls agree the recurrence is real, that Banneret is proof, and
that the *failure mode* — a plausible but wrong Character, with no error — is what makes it
serious. All agree `ability_weights` itself is correct and settled by Decree 0005; the question
is only how its inputs get supplied.

**The options.**

| | What it does | Cost |
|---|---|---|
| **A. Leave it manual** | Author declares each time | Proven to fail silently. Rejected by all. |
| **B. Derive from code** | Introspect what each module spends | One source, nothing to remember — but the weight system starts depending on how a feature is written, and a refactor can erase a preference invisibly. Violates *explicit beats magical*. Withdrawn by its own proposer. |
| **C. Declare, and audit** | Declaration stays authoritative; a test proves it matches what the code spends | One test, one checklist line. No runtime change. Introspection's fragility becomes a CI nuisance instead of a wrong sheet. |

**Consul recommendations.** Druid, Warlock, Monk, Artificer and Rogue all converged on **C**.
Monk proposed B and withdrew it against the Canon rule. Druid's objection to B — that refactoring
can silently erase a derived fact, and refactoring is less deliberate than writing — was the
argument that turned the room, and is worth preserving whatever Julio decides.

**Vox's synthesis.** The council's answer to Julio's question is **yes, integrate it into the
design steps — but the step is a test, not an architecture change.** The mechanism is sound; what
was missing is that nothing made its omission audible. The strongest alternative remains **B**,
and it should be reconsidered if the declaration list ever grows large enough that maintaining it
becomes its own burden.

**Dissent recorded:** none outstanding. Rogue's second direction (a declaration that is never
spent) is folded into the proposal and should not be dropped if the Decree narrows the scope.
