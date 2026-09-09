# 👁 For Reviewers: how to read this folder

> 🧾 **Record.** A report, an index or a working document, not a specification.

*Orientation for anyone brought in to review these pages: a person, or another
model. Read this first. It states what the folder is, the rules the pages were
written against, and what a useful objection looks like here. Written
2026-09-09.*

---

## 🔎 1. What you are reading

Analysis of a Dungeons & Dragons 2024 **character generator**: a program that
produces a finished, playable character sheet from a seed. There are no player
choices at the table. Every pick was already made by seeded dice before the
page existed, and the same seed always produces the same person.

These pages are **design and literary criticism written for the project's
author**. They ask, element by element, whether each part of the generator has
a coherent fantasy, whether it is original or borrowed, and whether it is well
told.

**What they are not.** Not player-facing text. Not documentation of how the
code works. Not a specification. Nothing in them is implemented, and every
proposal in them is waiting on the author's decision.

---

## 🔎 2. The rules the pages are written against

Judge the material by these, not by general fantasy-writing advice. Several of
them invert the usual advice on purpose.

1. **Death of the Author.** The deep lore exists so the writing stays
   consistent between hands. It is never explained to the player. A player may
   work a mechanism out from the text; nobody in the fiction ever confirms it.
   **Advice to "explain the lore more" is wrong here** and will be discarded.
2. **One register per voice.** Each class and each people has a single
   consistent register: the Fighter is a training memoir, the Warlock is a
   contract, the Barbarian is a chant, the Rogue is a confession that is not
   sorry. Mixing registers inside one piece is a defect.
3. **Second person throughout, and no collective "we"** for a people with no
   shared culture. Species prose states identity and drive; it never restates
   the rules the feature entries already carry.
4. **Traits are taught, gifted or suffered, never morally inherited.** The rule
   guards against monoculture and moral determinism. Plainly physical traits
   (darkvision, size) may be biological.
5. **Loaded names stay in the pool.** A character titled "Justiciar" who is not
   just is a story, not a bug.
6. **No em-dashes** in authored text. The author is a native Spanish speaker
   writing in English, and corrections to grammar and idiom are welcome as long
   as the voice survives.
7. **Never state a real-world parallel on a species page.** A species that is
   explicitly one real group becomes a mascot and stops being a people.
   Backgrounds are the exception, because a player *chooses* a background, so
   specificity there is a gift rather than an imposition.
8. **A sheet states what the character has**, never a choice still pending, and
   prints resolved numbers rather than formulas.

---

## 🔎 3. What a useful objection looks like

Blunt and specific, quoting the line being judged. In order of value:

- **Where the analysis is wrong or overreaching.** A claim that reads well and
  does not survive the text it cites.
- **Where a "finding" is a cliché restated**, or where the pages praise
  something ordinary as though it were an achievement.
- **Literary and mythic sources missed or misattributed.**
- **Contradictions between pages.** There are 49 of them and they were written
  over one long cycle.
- **The drafted prose lines.** Which are good, which are trying too hard, and
  which break the register they claim to be in. The `Lines-Annex` gathers all
  of them in one place.
- **The three structural claims**, which are the load-bearing ones:
  1. the written backgrounds run a four-beat form whose hook is always a debt
     (`Backgrounds-Written`);
  2. the six spellcasting classes form a set of six relationships to the source,
     taken, granted, lent, contracted, performed, had;
  3. a "lineage" means something different in each people, and the ranking of
     those meanings matches how well each people is written (`Lineages`).

If those three survive a hostile read, the framework stands.

---

## 🔎 4. Reading it remotely

The repository is public. A single page can be fetched raw:

```
https://raw.githubusercontent.com/JulTob/DnD/main/Documenta/Canon/Mythos/README.md
```

Swap the filename at the end for any page. While this work is still on its
branch and not merged, replace `main` with the branch name:

```
https://raw.githubusercontent.com/JulTob/DnD/Julio_Cl/fantasy-worldbuilding-analysis-4241c5/Documenta/Canon/Mythos/README.md
```

The folder itself browses at
`https://github.com/JulTob/DnD/tree/main/Documenta/Canon/Mythos`.

**On size.** The folder is about 145,000 words, which is roughly 190,000
tokens. Do not attempt it in one pass. Take one group per sitting:

| Group | Pages | Words |
|---|---|---|
| **Orientation and findings** | `README`, `Lenses`, `Repairs-Ledger`, `Agora-Questions-Proposed`, `Wiring-Plan`, `Voices-at-the-Table` | ~11k |
| **Peoples** | the ten peoples, `Lineages`, `Celestials` | ~31k |
| **Guilds, martial** | Barbarian, Fighter, Monk, Paladin, Ranger, Rogue, `Guilds-Registers-Names-Devices` | ~29k |
| **Guilds, casters** | Artificer, Bard, Cleric, Druid, Sorcerer, Warlock, Wizard | ~28k |
| **Backgrounds and Orders** | `Backgrounds-Written`, `Backgrounds-Official`, `Orders`, `Relationships`, `Draft-Tables` | ~20k |
| **Engines** | `Feats`, `Spells-and-Invocations`, `Stories-and-Titles`, `Names`, `Places`, `Equipment-and-Masteries`, `NPCs-and-Villains`, `Sheet-Alignment-Languages`, `Brand-Voice`, `Bard-and-Sorcerer-Lines` | ~17k |

`Lines-Annex` is a generated index of every drafted line with no argument in
it. Skip it unless you are specifically judging the lines.

**Where to start.** Backgrounds and Orders. The backgrounds are the strongest
prose in the project and they carry two of the three structural claims, so a
hostile read there tells you the most about whether the rest is trustworthy.

---

## 🧾 4b. The four layers

Before objecting that a detail is arbitrary, check which layer it sits in.
Each element page opens with a `0. Rules` chapter (see the README) sorting its
content into four layers: a **fixed point**
(marked 📕 inherited from the 2024 rules, or ⚖️ ratified by a project Decree), an
**interpretation** (lore chosen so a fixed point has a body, load-bearing and
replaceable but not deletable), a **free invention** (ours, with no mechanic
underneath, and the place a future editor is licensed to play), and a **sugar
line** (the italic line on the sheet, freely rewritable inside its register).

The commonest wrong objection to this project is "cut this detail, it is not
needed." Run the test first: remove it and ask whether a rule is left with
nothing to say for itself.

## 🧾 5. The canon these pages defer to

Four documents outside this folder are settled law, and the pages cite them
rather than arguing with them. A reviewer should know they exist before
objecting to something they explain:

- `Documenta/Canon/Cultural-Inspirations.md` : one culture key is one culture,
  never fused; which people holds which key.
- `Documenta/Canon/Dragons-and-the-Overcoming.md` : a dragon is a state a
  person reaches, not a species.
- `Documenta/Canon/Elves-and-the-Dreaming.md` : elf lineages are cultures that
  drift, not bloodlines.
- `Documenta/Canon/Tieflings-and-the-Shift.md` : belief made the fiends; a
  tiefling is born to ordinary parents and has no culture of their own.

Decisions are recorded as Decrees in `Documenta/Agora/Decrees/` and
`Curia/Agora/Decrees/`, and open questions become Dialogs. A choice that lives
only in a chat log does not exist.
