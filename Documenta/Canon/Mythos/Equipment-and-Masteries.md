# ⚔️ Equipment and Masteries: what the character is holding

> 🔒 **Settled.** No chapter is still in flow. 🔒 2 · 🧾 1 · 🔎 5

*Wiki entry for the design team. `AtlasInventarium/GearKit.py` is the loadout
policy over `Grimoire_of_Items`; `Ledger_of_Weapons`, `Ledger_of_Gear` and
`Ledger_of_Wonders` are the catalogues; `Map_of_Gear_Titles` and
`Map_of_Materials` name and personalise; `ToolsKit` carries the tool
Practices; `Map_of_Weapon_Masteries` decides the drills. Compiled 2026-09-08
from the code and six generated loadouts (levels 3 to 16).*

> **In one sentence.** The gear layer is the best-engineered prose engine on
> the sheet, its titles and tool Practices are in the house register, and the
> weapon in the character's hand is the one line on the page with nothing
> written under it.

---

## 🔒 1. The design, which is right

GearKit's own "thought pattern" is the doctrine: items are policy-free
primitives crafted by Tags; proficiency is read from Guild Tags, never from
class names; every pick comes from a per-character seeded stream; nothing is
stored that a read can derive (Armour Class is summed live). The pack is
bought, **opened**, and its contents go into the bag while the empty pack does
not linger on the sheet. A Fighter with six masteries carries six weapons,
because "otherwise the training is a line of text about nothing."

✅ **The drills are balanced on purpose**: half reach far (Ranged or Thrown),
half are close work, "so a hero is never left with six ways to hit an enemy
they cannot reach." Candidates are ordered by what the hero already carries,
then filled from the Guild's training.

✅ **The wonders are gated by level tier** (1, 5, 11, 17) and their bonuses are
`grants` summed at read time, gone the moment the item is sold.

---

## 🔎 2. What six loadouts looked like

| Character | Armour | Weapons | Titles |
|---|---|---|---|
| Orc Farmer Fighter, L3 | Scale Mail; "a scarred oak shield" | Lance, Light Crossbow, Dagger, Whip | none |
| Orc Farmer Rogue, L5 | *Studded Leather of the Standing Stone* | Whip, Hand Crossbow | armour only |
| Orc Farmer Cleric, L9 | *Scale Coat of Redemption*; "a hide-bound iron shield" | Quarterstaff, Sling | armour only |
| Gnome Vagabond Fighter, L12 | *Lorica Segmentata of Thatch and Iron*; "a garnet-set steel shield" | *Sledge of Harvest's End* (Maul), Heavy Crossbow | armour and one weapon |
| Gnome Vagabond Wizard, L7 | none | *Focus-Rod of the Traced Line* (Quarterstaff), Light Crossbow | the staff |
| Aasimar Gambler Paladin, L16 | *Full Harness of Steadfast Faith*; "a reliquary gold shield" | *Beak of the Reckoning* (War Pick), *Windlass of the Reckoning* (Heavy Crossbow) | armour and both weapons, as a pair |

✅✅ **The titles are the standard.** *Lorica Segmentata* on a Gnome is the
Italian key reaching the Roman noun; *Focus-Rod of the Traced Line* is a
Wizard's staff and nothing else; *Beak of the Reckoning* and *Windlass of the
Reckoning* share an epithet, so a Paladin's two weapons read as a set nobody
was told to make. The shields are personalised by material and culture in
their description (*reliquary gold* for the Aasimar, *hide-bound iron*, *scarred
oak*), which proves the Materials engine reaches the description slot.

⚠️ **No wonder appeared in six loadouts, including level 16.** The purse after
the kit is about 30 gp at every level sampled, and the cheapest wonder costs
far more. The tiers exist; the money never does. Whether a level-16 Paladin
should own a *Cloak of Protection* is a design call; today the answer is
silently never.

---

## 🔎 3. The bare line

`Ledger_of_Weapons` has 38 weapons and **two descriptions** (Musket and
Pistol). `Ledger_of_Gear` has 30 adventuring items and 18 descriptions. So the
Cleric's *Quarterstaff*, the Rogue's *Whip* and the Fighter's *Lance* print as a
word, while the Backpack beside them says "Holds a cubic foot or 30 pounds of
gear" and the Oil says "fuel for a lamp, or thrown and lit."

The weapon is the thing the character is holding on the cover of the story,
and it is the one object on the sheet with nothing written under it. Two ways
to fix it, and the second is already built:

1. **One line per weapon**, neutral, what it is for. Thirty-eight sentences.
2. **Let `personalise` reach weapons as it reaches shields.** "A scarred oak
   shield" exists because the Materials engine writes the description; the
   same call on the melee slot would give the Farmer's whip a braided hide
   and the Aasimar's pick a reliquary steel, in the culture's register, with
   no new text.

**The Farmer with a lance.** Masteries are drawn from the Guild's pool with no
tilt from background or culture, so an Orc Farmer Fighter drills lance and
whip. The mechanism for a tilt already exists in the sentence "candidates are
ordered by what the hero already carries": if the background issued one
weapon first (a Farmer's sickle, a Soldier's spear, a Guard's halberd, a
Sailor's dagger), the drills would follow it. One table, background to weapon,
Decree 0005 shape.

---

## 🔎 4. Weapon Mastery on the sheet

The Feature prints *"You feel comfortable with the weapons you trained with,"*
then the weapons in bold, then one blurb per mastery ("On a hit you have
Advantage on your next attack roll against that creature"). The Long Rest swap
is a mid-adventure decision and stays, per the Feature-Text canon.

⚠️ "Comfortable" is the weakest verb the Fighter page found anywhere in the
class. The Fighter's register is the yard at dawn; the mastery is the drill.
Draft:

*The weapon knows the drill. So do you.*

And one line per mastery, in the same register, before the rule:

| Mastery | Draft line |
|---|---|
| Cleave | *The swing does not stop at the first one.* |
| Graze | *Even the miss costs them something.* |
| Nick | *The second blade is already moving.* |
| Push | *You decide where they stand.* |
| Sap | *They will be slower to answer.* |
| Slow | *You take the ground out from under their feet, a step at a time.* |
| Topple | *Down is a place you can send them.* |
| Vex | *You have read them now. The next one lands.* |

---

## 🔎 5. Tool Practices: the second-best prose on the sheet

Twenty-one tools carry a **Practice**: a flavour paragraph, then rules
sections ("Principles of Transformation", "Works of Wonder") with a worked
example and a DC. The sheet projects them as flavour plus rules.

> *Writing teaches words to wait. A spoken word has the life of a butterfly;
> once written, it may last forever.* (Calligraphy)
>
> *Grain remembers sunlight, fruit preserves a summer, and a shared cup can
> turn strangers into…* (Brewing)
>
> *Every map is a promise that something can be found.* (Cartography)

✅✅ This is the backgrounds' register applied to rules text, with the rule
kept exact and the example concrete. It is the model for the General feats
and the Epic Boons (Feats page). One nod to record: Alchemy's "by the law of
equivalence, every transformation demands something in return" is Fullmetal
Alchemist's law, in the one place an anime register belongs on a sheet that
gives the Monk its own.

---

## 🔎 6. The hook object

Several background hooks already name an object: the Servant's *signet of the
house*, the Gambler's *paper with your name and a number*, the Exorcist's
*salt, iron, running water*, the Squire's *shield*, the Bailiff's *ledger of
faces*, the Herald's *banner*. None of them is in the bag. The earlier pages'
**signature-object Kit** (the Spellbook's mechanism, eight consumers) is the
place for them: one item per background, issued free, described in the hook's
register, worthless to sell. A wonder the purse cannot buy is replaced by an
object the story already gave.

---

## 🔒 7. Decisions log

**Standing**: GearKit's doctrine; masteries as carried weapons; the pack
opened; titles and personalised shields; tool Practices.

**Open (this page proposes)**: `personalise` on weapons, or thirty-eight
lines; the background-to-first-weapon table; the mastery line and eight
property lines; the hook object per background; a decision on wonders (budget,
or never, on purpose).

**Undecided:** whether a high-level character should ever own a wonder.

---

## 🧾 8. Pointers

- **Fighter page**: the yard register the mastery lines are written in.
- **Guilds-Registers-Names-Devices**: the signature-object Kit proposal.
- **Backgrounds-Official**: the hooks that name objects.
- **Feats page**: the Practices as the model for feat and Boon prose.
- **Cultural-Inspirations canon**: the keys the titles and shields already
  read.
