# Decree 0007 — Every change is a proposal

- **Issued by:** Julio, in chat, 2026-09-01
- **Recorded by:** Claude, same day
- **Worked example:** the Aberrant Mutant review (commit `6de5d83`), evaluated
  before landing and committed with its findings and one open question
- **Related:** Canon/Modus-Operandi.md · Canon/TagKit-Doctrine.md ·
  Canon/Code-Style.md · Documenta/Canon/Feature-Text.md · Decree 0006

---

## The decision

Every take on the code or the content, from any hand (Julio's included, agents'
especially), is a **proposal**, never a direct commit. Before it lands, the
Agora evaluates it critically against the established standards. The committee
is deliberate and organized; "move fast and break things" is explicitly
rejected. Speed is welcome in the evaluation, never instead of it.

This holds under crisis autonomy too: when Julio has relaxed live asking, the
evaluation still happens, in writing, before the commit. What autonomy waives
is the wait for his word, not the criticism. Anything the evaluation cannot
settle is landed provisionally with the open question named, or held, and the
question travels to Julio either way.

## The standards a proposal is compared against

**For prose the player reads** (descriptions, features, roleplay, stories):

1. **Death of the Author.** The lore is for the design team, not the user. No
   lore-dumps, no institutional history the player never chose. The text
   invites; the responsibility of meaning stays with the player.
2. **Inspiration potential.** Inspiration before rule; images that open play
   rather than close it; trust-the-reader compression (one word that carries
   an incident beats a paragraph that explains it).
3. **Player agency.** Backgrounds and classes stay class- and
   alignment-agnostic; premise may be stated, personality may not be
   prescribed; open questions engage, mandates do not.
4. **Feature-Text canon.** Explicit breaks, dice notation, resolved numbers,
   no open-choice language, chips as lookups and prose as the entry.
5. **Voice.** The register that fits the class or subject; no em-dashes;
   English corrected where wrong, with the author's voice kept and every
   correction noted.

**For code:**

1. **The Canon principles.** Contract orientation, clear models, top-down
   design, modularity, readability and dumbness, safety and error discipline,
   anti-bloat.
2. **TOP doctrine.** Domain axes as Tags, never string checks; composition
   over inheritance; one source of truth per type; contracts where the
   obligation is real; new content slots in the way existing content does.
3. **Verification.** The applicable gate runs before the commit: static
   bytecode equivalence for recovery work, the module self-tests, the
   contract suites, the generation battery. Green is a precondition, not a
   follow-up.

## The procedure

1. A change arrives as a proposal, whoever wrote it.
2. The relevant Consuls compare it against the standards above, in writing:
   named standards, named findings, including what the proposal does *better*
   than the current state.
3. The evaluation is recorded where the change lives: the questa, the dialog,
   or the commit message itself.
4. Only then does the change land. Findings the evaluation cannot settle are
   carried to Julio as open questions, never silently resolved.
5. A proposal that fails a standard is returned with its findings, not
   patched into acceptability without its author.

## What this forbids

- Committing any change, however small, without the written comparison.
- Treating Julio's own proposals as exempt: his word decides, but his drafts
  deserve the same critical reading he asked for.
- Letting an agent's throughput set the tempo of judgment.
