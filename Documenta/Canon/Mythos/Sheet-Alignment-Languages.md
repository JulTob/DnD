# 📄 The Sheet, Alignment and Languages: the order a stranger meets you in

*Wiki entry for the design team. `app/components/character_sheet.py` decides
what a reader sees first; `AtlasActorLudi/AlignmentKit.py` draws the two
alignment axes; `AtlasLudus/Map_of_Languages.py` fills the Languages box.
Compiled 2026-09-08 from the code and sixteen generated characters.*

> **In one sentence.** The sheet reads in the right order and the alignment is
> designed better than the game's, and every character it has ever produced
> speaks Common and Halfling.

---

## 1. The reading order

The main column is a tree: **Species, then Background (hook, Secret Order,
Order hook, Origin feat), then Class (Guild, Training, Fighting Style, Weapon
Mastery), then Backstory.** Each section is headed by its own description;
the Species description is not repeated as a lead line; a record with nothing
to say renders as its chip alone.

✅ **This is the order a stranger meets a person in**: the face (species), what
happened to them (background), what they do (class), and only then the story
they tell about it. The Backstory last is correct and should stay last; the
Stories page's proposal to compose it *from* the three sections above depends
on this order, because a reader who has just read the three voices will hear
them in the fourth.

The header chips: Alignment ⚖️, Creature Type, Gender, Size, Speed, Level,
Proficiency Bonus, Hit Points, Hit Dice, Armor Class. Lookups, as the
Feature-Text canon says a chip should be. The two that are not lookups are
Alignment and Gender, which are the only two identity facts on the sheet with
no sentence anywhere.

---

## 2. Alignment: two axes, and the house names

`AlignmentKit` is a two-axis geometry. Morality (Evil, Neutral, Good) and Order
(Lawful, Neutral, Chaotic) are independent Tags; Neutral is the absence of a
Tag; the display is composed from membership.

✅✅ **The definitions are the best in-house reading of alignment the project
has**, and they are in a docstring nobody reads:

> Evil means antisocial behaviours: goals aligned only with personal benefit.
> Good means prosocial behaviours: personal needs sacrificed for the collective.
> Lawful means inclined towards organizations and structures. Chaotic means
> inclined towards individualism and personal responsibility.

No metaphysics, no cosmic teams, no "evil races": four dispositions a person
can be observed to have. This is the alignment the Death-of-the-Author setting
needs, and it agrees with the Tieflings canon (the legacy "has no effect on the
moral outlook") and the Celestials canon (an Ideal is not good).

✅ **The house display names.** Neutral on one axis prints as *True*: *True
Good, True Evil, True Lawful, True Chaotic, True Neutral*. The legacy
`Map_of_Alignments` used *Legal* for Lawful (*Legal Good, Legal Evil*), a
Spanish speaker's word that also means *decent* in Spanish (*un tío legal*),
which is a better joke than it looks. *True Evil* for Neutral Evil is the
strongest of the nine: evil without the excuse of a code or a cause. Keep the
naming; it is a voice.

⚠️ **The draw is uniform thirds on each axis**, so a third of all player
characters are Evil and a ninth are True Evil. Of twelve sampled level-one
characters, six were Evil (five True Evil). For a *player* generator that is a
design decision worth making on purpose: Julio's call, and Decree 0005 gives
the shape (a nudge, never a lock). The docstring promises "these tags influence
further decisions, like titles, story beats, and motivation"; the Stories page
found the one story beat that reads Evil ("always resented being a {species}")
misreads *antisocial* as *self-hating*.

**A line for the chip.** Alignment is the one identity chip with no prose.
Nine lines, one per cell, in the docstring's own register:

| | Lawful | Neutral | Chaotic |
|---|---|---|---|
| **Good** | *The rules are how you keep people safe. You keep them.* | *You give more than you take, and you have stopped counting.* | *You will break any rule for a person. You will not break a person for a rule.* |
| **Neutral** | *The structure holds. What it holds is somebody else's business.* | *You take the world as it comes, and you come as you are.* | *Nobody tells you. That is the whole position.* |
| **Evil** | *Everything you do is legal. That was the point of the law.* | *What is in it for you is the only question you have ever needed.* | *You want what you want, and the wanting is the only law you recognise.* |

---

## 3. Languages: one line, every sheet, the same

`Character_Languages` adds Common, then a species language (`if char ==
"Elf": Elvish` and so on), then a class language, then one from the standard
list. On sixteen generated characters across ten species and sixteen seeds,
the Languages box read **Common, Halfling** every time.

Two causes, both in one function:

- The species and class branches compare the **Character to a string** (`char
  == "Elf"`), which is never true. The same bug the Titles' `Genus` docstring
  records as fixed elsewhere: "asked TagKit whether a Tag goes by that
  string." No species has ever granted a language.
- The "any language" is `set.pop()` on the standard set: no dice, not the
  Character's, and hash-ordered, so it is constant within a process and can
  change between runs. The replay contract does not cover languages.

What the branches would print if they fired is the **2014 racial language
list**: Elvish, Dwarvish, Gnomish, Orc, Giant, Draconic, Infernal, Celestial.
Repairing the comparison would therefore *introduce* three canon breaks the bug
has been hiding:

| Would print | Canon it breaks |
|---|---|
| Tiefling: *Infernal* | Born to ordinary parents; what would they speak but their parents' tongue? |
| Aasimar: *Celestial* | No sender, no errand; a language of the Ideals is a hotline to nobody. |
| Dwarf: *Dwarvish* | The Dwarf culture is Iberian by canon and by name (*Salvaro Esteban Herrero*); the language is a stock word. |

**Proposal.** Languages are cultures, not species. The Cultural-Inspirations
canon already gives every people its keys; a tongue per key (the Human
`nomina_culture` draw is the model) makes an Elf raised elsewhere speak
elsewhere, which is what the Elf canon says happens, and a Tiefling speak what
the family spoke. Species-agnostic, drawn by the Character's Dice, two
languages beyond Common per the 2024 rule. *Common Sign Language* in the
standard list is a good 2024 touch; keep it.

The **Elvish script kit** (`AtlasScriptum/Kit_of_Elvish.py`, Tibetan glyphs as
Elvish letters) is imported by nothing. A written form is the one place a
language can appear on a sheet without a rule (the spine of the Spellbook, the
carving on the Tomb Raider's find, the Tiefling's carvings nobody reads).

---

## 4. Gender

The other chip with no sentence. The species entries use second person and
the Guild lines avoid pronouns; the Stories engine hard-codes *her* in two
templates (Stories page). The generator accepts He, She, They and draws them;
the Names page found four peoples whose names do not respond to the draw.
Nothing to write on the sheet; something to make the engines read.

---

## 5. Decisions log

**Standing**: the tree order; the two-axis alignment with Neutral as absence;
the *True* display names; the docstring definitions.

**Open (this page proposes)**: nine alignment lines for the chip; languages as
cultures, species-agnostic, drawn by the Character's Dice; the script kit put
to use.

**Julio's call**: the Evil rate on a player generator (uniform thirds today).

**Repairs**: `char == "Elf"` in `Character_Languages`; `set.pop()` as a draw;
the Rogue legacy Training's two extra `AddAnyLanguage` calls.

---

## 6. Pointers

- **Stories-and-Titles**: the fourth section this order was made for; the Evil
  gate.
- **Tiefling**, **Aasimar**, **Dwarf** pages: the three canon breaks a language
  repair would introduce.
- **Cultural-Inspirations canon**: the keys a language table would use.
- **Names**: gender response by people; the Human `nomina_culture` draw.
- **Feature-Text canon**: chips are lookups; prose is the entry.
