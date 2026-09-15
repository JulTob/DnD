# QST-0126 — Four Oath paragraphs still speak in the retired register, and Creation's is a first draft

- **Type:** design
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Julio (author) · Venustas (Bard) · Lorekeeper (Elf Sage)
- **Parent:** —
- **Sidequests:** —
- **Related:** PR #7 · QST-0125 · Dialog 0026 (the lines, not the paragraphs) · `AtlasLusoris/AtlasOfGuilds/PaladinKit.py`

---

## 🔍 Diagnosis (what & where)

`PaladinKit.py` seats one paragraph per Oath above the recited oath. Four of
them (`DEVOTION_DESCRIPTION`, `ANCIENTS_DESCRIPTION`, `GLORY_DESCRIPTION`,
`VENGEANCE_DESCRIPTION`) were written under the first register, "the oath
remembered": austere, and each ending on its own cost. The class text has
since become the political romantic, and ends on the stand ("You won't move.
They will."). The four paragraphs no longer sound like the text above them.

`CREATION_DESCRIPTION` is a first draft with three faults against the rules
the class text was held to:

- Its second paragraph pre-explains three features (earth rising, fire sent,
  the line nothing crosses, steel bending in a field): Smite of the Elements,
  Event Horizon and Opposite Reaction, described before the rules print them.
- Its last sentence imposes a future event ("One day you will look at a thing
  you called into being and not be able to call it back"), which is the same
  move as "You saw something", in the future tense.
- "the way a poet holds a language he has not finished learning" assumes the
  poet is a man.

It also runs three paragraphs where the class text runs two, and ends on cost
where the class text ends on the stand.

## 🧾 Evidence

The five paragraphs and the class text, side by side, in `PaladinKit.py`. The
rulings on the class text: no hedging, no origin imposed (death of the author),
no rule explained ahead of the rules, Twain's civic speech in a Knight's tale.

## 🎯 Desired outcome

Five Oath paragraphs in the ruled register, each ending where its recital can
follow ("You swore an oath to X. To be a paragon of Y:"), no rule pre-explained,
no story imposed, length in the class text's range. Each Oath keeps its own
poets.

## 🧭 Notes for the Agora / implementer

This is step five of the eight-step build Julio set (core fantasy, register,
device, class text, subclass texts, feature lines, rules, implementation).
Julio writes or approves each paragraph; an agent drafts. The class text is
ruled and is not touched. The oath lines have their own review (Dialog 0026).
No Dialog is needed for the paragraphs: texts are Julio's rulings, not the
council's.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council

> Venustas (Bard): The class text set the temperature. A paragraph under it that ends on a cost now reads as an apology.
> Lorekeeper (Elf Sage): Keep the one thing the old paragraphs got right: Sacred Weapon's light and Aura of Devotion's calm are the rules' readings, and may stay as images.

**Weighting:** reach 2 × severity 2 = **4** · council leaning: `defer` (to Julio's pen)
