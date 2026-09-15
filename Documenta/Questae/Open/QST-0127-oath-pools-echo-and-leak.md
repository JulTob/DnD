# QST-0127 — Oath pools: lines that echo across slots, and lines that leak between Oaths

- **Type:** bug · design
- **Priority:** 🟡 normal
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Contracts (Warlock) · Testing (Rogue) · Simplicity (Monk)
- **Parent:** —
- **Sidequests:** —
- **Related:** Dialog 0026 · Q-0035 · PR #7 · `AtlasLusoris/AtlasOfTraining/Map_of_Paladin_Oaths.py`

---

## 🔍 Diagnosis (what & where)

`Compose_Oath` draws each of the six slots (vow, heart, arm, word, refusal,
close) on its own. Nothing looks at the lines already drawn. Two consequences:

**An oath can say the same thing twice.** Vengeance carries two Bécquer
readings of the same Rima in different slots:

- hearts: "My heart keeps the dead company, and knows how alone they are left."
  words: "My word keeps the dead company, and the dead are left so alone."
- words: "My word is not a pardon. The pardon rises to my lip, and dies there."
  refusals: "I will not say the word of pardon. It comes to my lips, and dies there."

With ten lines per slot, each pair lands together in about one Vengeance oath
in a hundred.

**A line can leak from one Oath into another.** Two Glory words lines also sit
in `BACKGROUND_WORDS`, at the grace weight of 3:

- "My word is the one thing I never sold, and I sold a great deal." (cluster `outside`)
- "My word travels ahead of me, and arrives before I do." (cluster `wandering`)

A Devotion Paladin with an `outside` background recites Glory's swagger. Seen
on seed 3, level 11, Devotion.

**One species line reads generic.** Human hearts: "My heart is true, and my
friends are my rest." It carries no image and sits flat beside any register.

## 🧾 Evidence

A five-word-run check across the six slots of every register (run in session,
not yet in `scripts/`) finds the first Vengeance pair. The second pair differs
by one letter (lip, lips) and escapes it. A register-versus-pool check finds
the two Glory lines. The lint (`oathlint2`, in session) holds 200 lines at
three defended flags.

## 🎯 Desired outcome

An oath never repeats itself. A line written in one Oath's register never
surfaces under another Oath. The three checks (lint, cross-slot runs,
register-versus-pool) live in `scripts/` and run with the smoke gate.

## 🧭 Notes for the Agora / implementer

Two ways to keep an oath from echoing, and the choice is Julio's:

- **Data.** Rewrite one line of each pair (Dialog 0026 rules on which), and
  move the two Glory lines out of the background pools, giving those clusters
  Oath-neutral lines instead.
- **Mechanism.** One explicit rule in the composer: no two lines of one oath
  share a run of four words; when a draw would, take the next candidate in that
  slot. Deterministic, seeded as now. Protects every future register and the
  grace pools too.

The project's preference for dumb data over a clever guard argues for the
first; the fact that the pools will keep growing argues for the second. Do
not weaken the seeded Dice Bags either way.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council

> Contracts Consul (Warlock): Two invariants, stated: no line shared across Oaths (held), no line shared between a register and a grace pool (broken twice), and no phrase shared across slots of one oath (broken twice). Write them down, then choose where they live.
> Testing Consul (Rogue): A one-in-a-hundred stammer will never show in a three-seed sweep. The check has to read the pools, not the sheets.
> Simplicity Consul (Monk): If the data fix is four lines, do that first and put the checks in `scripts/`. Build the guard only when the pools outgrow the checks.

**Weighting:** reach 1 × severity 2 = **2** · council leaning: `needs a Dialog` (0026, for the lines) then `build`
