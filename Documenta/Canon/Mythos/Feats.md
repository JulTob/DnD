# 🎯 Feats, Gifts and Boons

> 🎯 The fourth thing on every sheet
>
> 📜 **Settled.** No chapter is still in flow. 📜 1 · 📚 2 · 📔 5
>
> - 📕 **inherited from the 2024 rules.** Moving it costs rules compatibility.
> - 📙 **an aesthetic change.** The same rule wearing our name and look.
> - 📒 **a rule we changed.** A house rule, and it already cost compatibility.
> - 📘 **supportive lore.** It holds a rule or a core element up.
> - 📗 **deep lore.** Design that supports the fantasy rather than a rule.
> - A book marks a statement only if it can change exclusively through the
>   Questa / Agora / Decree system. Anything with no Questa and no Decree behind
>   it carries no book, however settled it feels.

*Wiki entry for the design team. Every feat in the generator, classified,
checked against the 2024 rules, and flagged where it departs. Audited by twelve
agents in two passes, every count taken by running the code rather than reading
it.*

---

## 📜 0. Rules

*The books are defined at the head of the page.*

### The rules as given

> 📕 **A feat is one of four categories**, and the category is the gate.
>
> 📕 **Origin feat.** Granted by a background at level 1. **No prerequisite.**
> A character may take one, and the Human takes a second through Versatile.
>
> 📕 **General feat.** Chosen at levels 4, 8, 12 and 16 in place of an Ability
> Score Increase, and at 19 for the Fighter's extra. **Prerequisite: level 4.**
> Most raise one ability score by 1 to a maximum of 20.
>
> 📕 **Fighting Style feat.** Granted by a class feature (Fighter, Paladin,
> Ranger) rather than chosen freely. **Prerequisite: a Fighting Style feature.**
>
> 📕 **Epic Boon.** Chosen at level 19. **Prerequisite: level 19.** Each raises
> one ability score by 1 **to a maximum of 30**, which is the only place in the
> rules a mortal passes 20.

The category is the classification this page organises by, because it is the
only thing about a feat the rules actually gate on.

**No 📒 is claimed for a category.** All four gates are the published ones.

### The supportive lore

> 📘 **A Human's Versatile draws from base feats and every setting Origin feat,
> Dark Gifts included.** The pool is deliberately enlarged rather than
> shadowed, so the species sees the same table without importing the setting
> module. Recorded at the merge site itself.

### Unratified, and what each one needs

- **That an Origin feat may carry a drawback.** Nine Dark Gifts each write a
  permanent penalty onto the sheet. No published Origin feat has one; all ten
  are pure upside. This is the category's defining departure and no Questa
  states it.
- **That the enlarged Versatile pool is a house rule rather than a defect.**
  It is marked 📒 below on the evidence of the code comment, not of a Decree.

---

## 📚 1. The inventory

106 feats, counted by running the catalogues rather than reading them.

| Category | Count | Compliant | Renamed | Changed | Benefit removed | Other |
|---|---|---|---|---|---|---|
| Origin, base | 12 | 4 | 0 | 4 | 4 | |
| Origin, setting | 17 | 1 | 10 | 4 | 1 | 1 absent |
| Dark Gifts | 9 | 0 | 0 | 8 | 1 | |
| General | 44 | 22 | 0 | 16 | 5 | 1 not from 2024 |
| Fighting Styles | 12 | 9 | 0 | 1 | 2 | |
| Epic Boons | 12 | 6 | 0 | 6 | 0 | |
| **Total** | **106** | **42** | **10** | **39** | **13** | **2** |

**The base twelve are exactly the published Origin feats**, with nothing
invented and nothing missing. **The twelve Fighting Styles are exactly the
published list**, and it is the cleanest category in the repository.

---

## 📔 2. The 2014 question

There is **no 2014 feat set** in the generator, so a 2024/2014 pair cannot be
shown from the code. What exists instead is a **legacy twin layer**: every base
Origin feat has a duplicate in `Grimoire_of_Features`, left from before the
current kit. Nothing calls them, but a module star-imports that namespace, so
the names are live.

Two things make the twins worth keeping in view rather than deleting blind.

- **Two twins are closer to the book than the live feat.** The legacy Alert
  carries the full published text; the legacy Tavern Brawler carries the 1d4
  plus Strength modifier and the 5-foot push. The legacy Magic Initiate
  actually picks the spells, prints them, and names the spellcasting ability.
  The live Tag does none of that.
- **One twin crashes if called.** The legacy `Lucky()` raises `NameError` on
  `char` because its description interpolates a Character at build time rather
  than at apply time.

If a 2014 set is wanted, it has to be authored. The twins are not it: they are
2024 feats implemented earlier, not the 2014 rules.

---

## 📙 3. The rebrands

Ten setting Origin feats are published faction feats with the faction removed
and the name chosen for the background. Same mechanics, our name.

| Ours | Renames | Background |
|---|---|---|
| 📙 Agitator | Harper Agent | Revolutionary |
| 📙 Bastion | Tyro of the Gauntlet | Guardian |
| 📙 Banner Bearer | Lords' Alliance Agent | Herald |
| 📙 Field Lieutenant | Purple Dragon Rook | Squire |
| 📙 Arcane Conduit | Spellfire Spark | Arcane Mutant |
| 📙 Strong Arm | Zhentarim Ruffian | Bailiff |
| 📙 Spared | Survivor (the feat) | Survivor |
| 📙 Cupbearer | Vampire's Plaything | Servant |
| 📙 On a Roll | Tireless Reveler | Gambler |
| 📙 Jinx | Shadowmoor Hexer | Fated |

✅ The method is the setting's own applied to rules: keep the mechanic exactly,
remove the publisher's faction, choose a name that means the background's thing.
Each carries a design comment explaining the choice, and those comments are the
best writing in the feat layer.

⚠️ None of the ten states its published name on the sheet, so a reader holding
the book cannot find the feat. The 📙 form exists for exactly this and should be
applied: *Cupbearer [renames Vampire's Plaything]: the rule.*

---

## 📔 4. Benefits removed: thirteen, and only three on purpose

This is the question that prompted the audit, and the answer is that **removal
is systematic and mostly unintentional**.

### Deliberate, and therefore 📒

> 📒 **Skilled** chooses from skills, artisan's tools and thieves' tools only.
> The published feat offers *any* combination of three skills or tools, so
> Gaming Sets, Musical Instruments, and also the Disguise, Forgery, Herbalism
> and Poisoner's kits are cut from the choice. Eighteen of thirty-five tools.
>
> 📒 **Shadow Cast** drops **Domain Traveler**, Mist Walker's planar-travel
> benefit. The class docstring states the reason: it was the one benefit whose
> text named Ravenloft's geography.
>
> 📒 **Cupbearer** drops the benefit that settled whether the Servant was a
> victim or an accomplice, which the background refuses to settle.

Three deliberate removals, each with its reasoning recorded at the site. That
is the standard the rest should have met.

### Not deliberate: ten defects wearing the same clothes

| Feat | What is missing |
|---|---|
| **Resilient** | The saving-throw proficiency, which is the entire feat. Described, never granted. QST-0067 already names it. |
| **Blessed Warrior** | The whole mechanical payload. No `apply=` is passed, so it grants a paragraph and no cantrips. |
| **Druidic Warrior** | The same, and the legacy copy at least sampled the cantrips. |
| **Magic Initiate** (Cleric, Druid, Wizard) | Grants nothing at all: no cantrips, no level-1 spell, no use tracking. Also drops "you can cast it using spell slots" and the spellcasting-ability clause. |
| **Athlete** | The Climb Speed. |
| **Dual Wielder** | Quick Draw. |
| **Medium Armor Master** | The Stealth benefit, and the armour-training prerequisite. |
| **Ritual Caster** | The ritual casting itself. The text says only that the spells are prepared. |
| **Dragon Cult Initiate** | Dragon's Tongue is half implemented: the "if you already know Draconic" branch never fires. |

**A defect is not a house rule.** None of these carries 📒, on the precedent set
on the Goliath page: a dropped benefit with no stated intent is a bug. Each now
has its own open Questa: QST-0096 (Blessed and Druidic Warrior), QST-0097 (Magic
Initiate), QST-0098 (the four General feats), QST-0100 (Dragon Cult Initiate).
Resilient was already QST-0067.

---

## 📔 5. Flagged as unorthodox

**Field Marshal** is the one General feat with no published equivalent. It
grants 2d6 plus an ability modifier in temporary hit points at 30 feet,
proficiency-bonus times per Long Rest, **and standing Advantage on attack rolls
while Bloodied**, uncapped, with no action cost and no duration. No published
General feat grants standing Advantage on attack rolls. It is the level-4 half
of Field Lieutenant, and it makes the page's old count of forty-three wrong.

**Every Dark Gift carries a drawback.** No published Origin feat does. That is
the category's real unorthodoxy rather than any individual gift, and it is the
file's stated design.

**Arcane Infiltrator does not exist.** It is named as the Agent of the Ninth
Quill's Origin feat and implemented nowhere in the repository.

**Blind Fighting states no rule**, only a Blindsight chip, where all eleven
siblings print theirs.

**Boon of Truesight prints a sense the character does not carry.** The working
line is commented out, so the boon raises an ability score and stops.

---

## 📔 6. Structural defects

- **The General feat catalogue is orphaned.** Nothing outside its own folder
  imports `FeatKit`. The live level 4, 8, 12 and 16 draw is `ApplyRandomFeats`
  in `Grimoire_of_Features`, which reads a different catalogue. The gated,
  prerequisite-checking path is exercised only by its own self-test.
- **`Map_of_Epic_Boons.py` defines nothing.** All twelve names are bound to
  `None`, so the entire TagKit boon path, including its real level-19
  precondition, is dead. The texts that reach a sheet live elsewhere.
- **Two Dark Gifts crash on apply.** Echoing Soul and Symbiotic Being import a
  name that exists nowhere. Measured: 4 per cent of seeded level-1 Humans fail
  to generate.
- **`Strong_Arm` is defined twice and the surviving copy is the degraded one.**
  The dead copy has the `<br>`; the live one does not, so its two sub-benefits
  print run together.
- **The Fighting Style catalogue exists twice**, and so does the base Origin
  feat set.
- **`BACKGROUND_ORIGIN_FEATS` is a no-op merge**, since the dict it spreads was
  already updated four lines above.

---

## 📔 7. What the feats do not say

Measured across generated sheets, the feat layer carries **no inspiration line
at all**: General feats 0 of 44, Fighting Styles 0 of 12, Epic Boons 0 of 12.

The Dark Gifts are the exception and they do not know it. Each carries its line
already, as a docstring the sheet never prints: *"Something in you is already
partway across."* *"Something is always looking, and it is not on your side."*
Moving those nine strings into the descriptions is the cheapest voice
improvement available anywhere in the project.

---

## 📚 8. Pointers

**Fifteen Questae opened from this page**, one per issue: QST-0095 to QST-0109.
They are listed in section F of the Repairs Ledger.

- **Backgrounds-Written**: the backgrounds these Origin feats belong to.
- **Repairs-Ledger**: the defects in section 4 and 6.
- **Wiring-Plan**: the lines in section 7.
- **Human**: Versatile and the enlarged pool.
- **Aasimar**: the worked chapter 0 this page follows.
