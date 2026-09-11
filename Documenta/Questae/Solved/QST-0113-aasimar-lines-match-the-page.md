# QST-0113 — The Aasimar's eight lines, as the page states them

- **Type:** code / lore-fidelity
- **Priority:** 🟠 high
- **Status:** Solved
- **Owner:** Claude
- **Route to:** Technical Team · Lorekeeper · Julio
- **Related:** QST-0110 · QST-0111 · QST-0094 · `Documenta/Canon/Mythos/Aasimar.md` §0 §11 · `AtlasActorLudi/SpeciesKit/Aasimar/resolution.py`

---

## 🔍 Diagnosis (what & where)

The page settles a flavour line for all eight Aasimar entries. The code carried
four of them, none matching, and had no line at all for the other four.

Ruled by Julio, 2026-09-11: *"we are editing the Aasimar md so we actualize the
code with some guidance. A discrepancy of the code is a mistake."* The page is
the authority, so each of these is a defect in `resolution.py` and not a
disagreement.

| Entry | The page | The code carried |
|---|---|---|
| Darkvision | *Darkness cannot hide the truth from you.* | nothing, and no rule either: a bare chip |
| Celestial Resistance | *Life flows through you. Death passes over you.* | *Whatever burns or rots reaches you and finds nothing to take hold of.* |
| Healing Hands | *Life finds your way.* | *Something in you remembers what a body is supposed to feel like, and lends it out.* |
| Light Bearer | *There is always a spark of light inside of you. Relentless.* | *Your aureola never fully goes out, not even when you'd rather it did.* |
| Celestial Revelation | *Be not afraid, for you bear a star.* | *For a little while, the thing you usually hide stops hiding.* |
| Talarian Wings | *Something in you answers the sky's calling.* | nothing |
| Inner Radiance | *Your inner spark becomes an aurora of pure light.* | nothing |
| Necrotic Shroud | *The brighter the light, the darker the shadow.* | nothing |

Three rule texts had drifted from the page too, all inside Celestial Revelation:

- **Talarian Wings** grew *"in a burst of celestial energy, spreading from
  vestigial into two full spectral wings"*. The page: *"You spread your talaria
  into fully grown wings."*
- **Inner Radiance** kept the published *"searing light radiates from your eyes
  and mouth"*. The page: *"Your eyes shine brightly and your halo grows into a
  bright aurora."*
- **Necrotic Shroud** spent the talaria (*"your talaria spread into flightless
  wings"*). The page: *"your halo collapses like a Dark Sun."*

And each option ended in a bare `<i>Radiant.</i>` where the page says *"Your
extra damage is Radiant."*

Two defects found in the same file while reading it:

- The eleven lines that publish the Revelation's shared facts onto the Character
  were **written twice, back to back**, comment and all.
- Darkvision was the only Aasimar entry projected with an empty description, so
  a player reading the sheet never saw the rule. QST-0094 recorded the
  cross-species convention as open; Julio settled it for the Aasimar on the page
  and then deleted the ticket's *Unratified* entry himself.

## 🎯 Desired outcome

1. Every one of the eight lines reaches the sheet, in the house format the other
   species use: `*line*` then a blank line, then the rule.
2. The three option paragraphs read as the page writes them.
3. Darkvision prints the shared `Darkvision_Rules` text under its line, and keeps
   its chip.

## ✅ Resolution

All of it, verified by generating a level-5 Aasimar and reading the projected
entries back against §0 line by line. The duplicated block is gone.

**Flagged, not fixed**, because they are the page's to settle and the page is
Julio's:

- **The option rules say "halo" where the rest of the page says "aureola".**
  Aureola is the declared 📙 rename and the species description introduces it by
  name. The code follows the page and says *halo* in those two rules.
- **Inner Radiance and Necrotic Shroud are marked 📕** *inherited from the
  rules*, but both now depart from the published wording. By the legend that
  makes them 📙 *an aesthetic change*.
- **The "What that buys beyond the rule" paragraph quotes a sentence that no
  longer exists.** It argues the Revelation set is one body by citing Necrotic
  Shroud spending the talaria, which the rewritten rule replaced with the halo.
  The argument still holds and is now stronger (Inner Radiance and Necrotic
  Shroud share the aureola, Talarian Wings has the talaria, and one spark is
  behind all three), but its evidence needs restating. The ⚠️ warning below it
  says *"Necrotic Shroud's own sentence stops meaning anything"* if a later hand
  removes the talaria, and that sentence has already gone.
