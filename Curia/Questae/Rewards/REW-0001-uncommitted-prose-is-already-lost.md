# REW-0001 — Uncommitted prose is already lost

- **From:** QST-0080 (Grok session salvage: Cleric voice was uncommitted, not gone)
- **Distilled:** 2026-08-31, with Julio
- **Applies to:** any session that authors prose — guild and species voice,
  descriptions, prayers, titles, Canon text

---

## The lesson

Code and prose fail differently, and the repo had only been defending code.

When code is lost there are second chances: bytecode disassembles, callers
constrain the contract, and a careful rewrite lands somewhere near the
original. The 2026-08-29 recovery ran on exactly that — 131 vault `.pyc`
files, a survey catalog, disassembly-verified fixes.

Prose has no second chance. The Cleric guild block took roughly a dozen
rounds of Julio's feedback to reach: threatening drafts, loredump drafts, a
too-oblique religious-literature draft, a King James draft that read as
costume. A rewrite would not reproduce it. It would produce different
sentences, and the tuning would have to happen again from the beginning.

So the bytes being on disk is not safety. **For authored text, the gap
between "written" and "committed" is the loss window**, and it is measured in
sessions, not in crashes.

## Why it is not obvious

Nothing broke. There was no accident, no bad restore, no truncated file. The
session simply ended, and Julio opened a new chat twelve minutes later
expecting a wipe. The work was fine. It just was not history.

That is a failure mode with no error message, which is why it needs a name:
**session-end loss** is distinct from the restore-to-old-ref accident, and the
guards for the second one do not catch the first.

The sharper trap is that a safety rule caused it. Recovery rule 4 — *do not
commit until Julio says so* — exists so that agents cannot bury good evidence
under speculative reconstructions. Correct for reconstruction. But it was
applied to **new authored content**, which has no evidence to conflict with,
and so it held finished prose out of history for about six hours across two
sessions and one expected wipe.

## What to do differently

- **A commit hold is about reconstruction, not authorship.** A rule that
  freezes commits should say so explicitly, and exempt newly authored files.
  Recovering a file and writing one are not the same act.
- **Commit prose the moment it is accepted**, before moving to the next
  question. Prose modules are single files with no build step, so a one-file
  checkpoint commit crosses no other agent's lane — the usual reason to wait
  does not apply.
- **Never rewrite recovered prose.** Preference order for text is verbatim
  transcript, then vault copy, then — only if both are gone — a rewrite that
  is labelled as new writing rather than a restoration.

## Also carried out of this quest: how the voice was written

Minting this Reward deletes QST-0080, and these rules were the expensive part
of that quest. They apply to the Domain openings still pending (QST-0080.1)
and to every other guild voice.

- **Sell the fantasy, not the job.** A guild paragraph should say what it is
  like to *be* one, the way Fighter sells *you made yourself*. Mechanics,
  ministry and stereotype ("you pray, you bless, you heal the sick") describe
  a class sheet, not a fantasy.
- **The Cleric fantasy is being watched over — recognition.** To be attended
  by something vast is to matter. It is warmer and more precise than "faith"
  or "devotion", and it holds for an evil War Cleric as readily as for a Life
  Cleric.
- **Vigilant verbs frighten; committed verbs comfort.** *Watches*, *does not
  sleep*, *does not look away* describe an eye doing work, and an eye doing
  work implies you can fail inspection. Warm scripture instead renders care as
  shelter, carrying, remembering, and answering before you ask — the watcher
  is already settled in its commitment, so there is nothing to pass.
- **Register comes from syntax, not vocabulary.** Parallel clauses, parataxis
  (*and still… and still…*), fronted clauses and concrete images read as
  scripture. *Shall* and *thee* read as costume.
- **Answer the fear.** Every calling narrative pairs *am I enough* with a
  reply. A fear left hanging turns the watcher into an examiner.
- **Leave the mold open.** Naming the watcher as a guess — maybe a god, maybe
  your ancestors, maybe the universe — invites the player in. Stating it as
  fact is loredump, however well written.

## Council / provenance

> Lorekeeper (Elf Sage): The distinctive work in the Cleric lane was voice,
> not mechanics. That is precisely the material no vault can hold.
>
> Safety Consul (Paladin): "The session ended and a new chat opened" now has a
> name and a guard. I accept rule 4 kept its purpose; I do not accept that it
> should ever have covered authored text.
>
> Workshop Consul (Artificer): The commit is the only copy that survives a
> machine. Vault copies and backup refs are insurance, not history.

**Provenance:** first landed as `a0c7da9` on `codex/recovery-2026-08-29`
(still there, with `4e2ad9a` / `24ee174`). Cherry-picked onto `main` after
that branch was force-moved to a parallel guild-kit restore. Transcript
`55d5d61d`. Sketches at
`.recovery-vault/grok-session-20260831/cleric-watcher-fantasy.md` on the
recovery branch.
