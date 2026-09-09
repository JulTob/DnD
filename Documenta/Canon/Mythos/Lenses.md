# 🔭 Lenses: the generator read as a designed thing

> 🚧 **Draft.** Analysis and proposals, not yet authoritative. Under review.

*Wiki entry for the design team. The thirty-six pages before this one read
the generator element by element. This one reads it whole, through the three
craft books in the project's book folder (a game-design lens book, a
worldbuilding workbook, a backstory workbook) and the villain sourcebook.
Compiled 2026-09-08. Nothing here is a rule; each section is a question the
books ask and the answer the generator gives today.*

> **In one sentence.** The generator is a toy that hands you a stranger and
> dares you to want to play them; where it is alive it is because two things
> that were never told about each other agree, and where it is dead it is
> because a table was filled and nobody read the output.

---

## 1. Purpose, and the contradictions against it

**The lens of the problem statement.** What is this for? The Canon answers
across three documents: a generator, not a builder; every pick made before the
page existed; Death of the Author; nothing explained. Put together:

> *To hand a person a character they did not choose, in a world nobody
> explains, and make them want to play it.*

**The lens of inner contradiction** ("a good game cannot contain properties
that defeat the game's very purpose"). Five were found, and every one is a
subsystem doing the opposite of the purpose:

| Contradiction | Where |
|---|---|
| A generator that prints choices still pending | "Choose one of your known Warlock cantrips"; "of your choice (see Origin Feats in FeaturesKit)" |
| A nothing-explained setting whose story engine explains | "to break the infernal curse that haunts their bloodline"; "descends from a benevolent silver dragon"; "to fulfill a celestial mission" |
| A seeded-replay promise with three unseeded draws | `NewName`, `ApplyEpicBoon`, `AddAnyLanguage` |
| An "explicit beats magical" doctrine with a family of silent string-compares | `"Cleric" in lusor` (fixed), `char == "Elf"` (languages, live), `Character` vs string in the Story host |
| One setting with two vocabularies | thirty-two written backgrounds for players; sixteen official plus twenty-four role names for NPCs |

None is a matter of taste. Each is a place the machine argues with its own
brief.

---

## 2. The toy, and surprise

**The lens of the toy** ("if my game had no goal, would it be fun at all?").
The generator has no goal. It is a toy first: a seed, a button, a stranger.
That is its strength and it should be protected: the replay contract (same
seed, same person) is what makes the toy a toy and not a slot machine.

**The lens of surprise.** Surprise is budgeted well where it is drawn from a
keyed table and badly where it is uniform:

- ✅ *Beak of the Reckoning* and *Windlass of the Reckoning* on one Paladin.
  *Lorica Segmentata* on a Gnome. A Cleric's prayer in the culture's voice. A
  Dark Gift on a Human. A Secret Order nobody asked for. The Servant's letter.
- ⚠️ A Bladesinger with *Gentle Repose* and *Arcane Lock*: surprise with no
  resonance is noise. Six loadouts and no wonder: no surprise at all. Every
  character speaks Halfling: the anti-surprise, the same card every time.

The rule the good cases share: **surprise comes from a second table that the
first was never told about, and both are keyed to the same person.** Uniform
draws surprise once and then bore; constant results never surprise.

---

## 3. Resonance, and the hidden power

**The lens of resonance** ("what is it about my game that feels powerful and
special?"). Three things, and all three are already in the Canon:

1. **The peoples disagree and none is refuted.** Soul-metal, the fixed Ideal,
   the collective dream, the self-authored dragon, the wind path. Five answers
   to one question, on one table, and the generator seats them together.
2. **Nothing is explained on the page.** The mechanism is deep lore; the
   sheet says "we adapted and became like the woods" and stops.
3. **One register per voice.** The chant, the training memoir, the terms, the
   confession that is not sorry, the walker's field diary.

Everything that felt alive in thirty-six pages came from one of these three.
Everything that felt dead broke one of them: the Story explains, the Archetype
fillers have no register, the NPC Celestial table refutes the Ideals.

---

## 4. Meaningful choice, removed on purpose

**The lens of meaningful choices** ("what choices am I asking the player to
make?"). The generator's answer is radical: none, before play. The choice it
leaves is the reading. Death of the Author is not only a writing rule here; it
is the player's one meaningful choice, made about a person they did not build.
"A justiciar is not automatically Just" is a design principle for the pool and
an invitation to the reader.

The only choices that may appear on the sheet are the ones made *in play*
(the Long Rest swap, the breath weapon's shape, the Celestial Revelation each
transformation). The Feature-Text canon already sorts every sentence into the
two piles. The leaks are listed in §1.

---

## 5. Reward and visible progress

**The lens of reward** and **the lens of visible progress.** A level-N sheet is
a record of progress that happened offstage, and the generator's device for
showing it is right: an upgrade feature states only what it changed, and the
live number sits in the one entry that owns it. The arc is legible.

⚠️ The reward at the end is not. Level 19 is the one place a mortal passes the
cap of 20, the rules' whisper of the Ascending for every class, and it prints
"+1 to any ability (max 30)" and "Re-charges on initiative." Level 4's reward
prints "You gain +2 Strength." The rewards are real and read as notes to self.
The tool Practices show what the same rules text looks like written for a
reader.

---

## 6. Transparency

**The lens of transparency** ("the ideal interface becomes invisible"). The
chips are lookups and the prose is the entry: correct. The interface shows
through in exactly the places the earlier pages flagged as leaks:

- `Descent(kind='Star', names=(…))` in the Celestial patron paragraph.
- "Epic Boom!" printed to the console at level 19.
- "(see Origin Feats in FeaturesKit)" on the sheet.
- "Arcane Trickster: 3", "see PHB '24 pp145-150", "CHA" as a word.
- `Noble Frazarme` for a They Noble.

Every one is the machine speaking in its own voice on a page that has a voice
of its own.

---

## 7. Fantasy, projection and the avatar

**The lens of fantasy** ("who does the player fantasize about being?"), **the
lens of projection** ("what is there that players can relate to?"), **the lens
of the avatar** ("does my avatar have iconic qualities that let a player
project themselves into the character?").

The generator's projection device is **the second person**. Every species
entry, every background, every Guild line says *you*. "You have never done
anything. That has never been the relevant fact." A reader cannot be told that
about a stranger without becoming them for the length of the sentence. The
thirteen core fantasies (Dialogs 0013 to 0018) name who the player is being;
the registers say how it feels from inside.

The **iconic quality** the avatar lens asks for is, on this sheet, an object:
the Spellbook of palm leaves, *Beak of the Reckoning*, the signet of the
house, the Cleric's seated prayer. The signature-object Kit proposed on the
Guild and Equipment pages is the avatar lens applied: one thing per character
that is only theirs.

---

## 8. The world, and its gateways

**The lens of the world** ("how is my world better than the real world? Can
there be multiple gateways?"). Better: nobody explains it, nobody is refuted,
and being read wrongly is load-bearing for two peoples and one Guild. Three
gateways exist: the player sheet, the NonPlayer sheet, the Dungeon Master
Companion. Today the second cannot summon and the third cannot generate a
scene (NPCs page §1). One gateway of three is open. The world is only as big
as the door.

---

## 9. The nameless quality

**The lens of the nameless quality** asks which of Alexander's fifteen
properties the design has. Where the generator has them:

| Property | Where it lives |
|---|---|
| **Levels of scale** | Four names on a Dwarf; a hook inside a background inside a people. |
| **Strong centres** | One idea per people; one register per Guild. |
| **Echoes** | *Luz* in the Celestial and Fiend pools. Athens against Rome. *Reckoning* twice on one belt. The Fighter and Monk closing on the same inversion. |
| **Roughness** | *Legal Good*. "Pusillanimous" where a swear would go. "Tragones y Mazmorras." The author's hand, left in. |
| **The void** | The Tiefling's missing "we". The Stranger's empty compact. The Barbarian's hidden table of contents. |
| **Not-separateness** | The Cleric prayer that reads species, culture and Domain at once. The shield that reads material and culture. |

Where it does not: the Archetype fillers ("recovering buried treasures for a
generous bounty"), the Outro jokes, the constant language line, the uniform
spell list. Alexander's word for these would be *dead*: parts filled to be
full.

---

## 10. Atmosphere

**The lens of atmosphere** ("without using words, how can I describe the
atmosphere of my game?"). The wordless layer is thin: chip emoji, one gothic
title face for the Warlock, the eldritch glyph span, the 【】 and 〖〗 brackets
on the spell list. The Elvish script kit exists and is imported by nothing. A
generator that refuses to explain has more to gain from atmosphere than most,
because atmosphere is how a world is felt without being told. The script on
a Spellbook's spine, a Guild's title face, a Tiefling carving that renders as
glyphs: this is the budget. The house preference for plain Unicode over
hosted fonts is the constraint; Tibetan glyphs as Elvish already honour it.

---

## 11. The worldbuilding workbook: six aspects of magic

The workbook's frame for any magic is **Source, Cost, Potency, Commonality and
Accessibility, Mastery**, across paths it names *Scientific, Artisan, Arcane,
Natural, Legendary, Forbidden*. The setting answers most of it without a rule:

| Aspect | The setting's answer | Where it is thin |
|---|---|---|
| **Source** | Belief (Celestials, fiends), the Dream (Elves, Fae), the mark (Sorcerer), the terms (Warlock), the metal (Dwarf) | The Wizard's source is the stolen fire, and the list of spells never says where it was stolen from (Spells page). |
| **Cost** | The terms; the body turning; the proof; the Ideal that does not care what you meant | **The Cleric's.** What does the Kept seat cost? The one caster whose price the canon has not named. |
| **Potency** | The Boon at 19: the cap exceeded, the whisper of Ascending | Printed as "+1 (max 30)". |
| **Commonality** | Every sheet is an adventurer, so magic reads common | The sheet never says how rare a Wizard is in the world. A Decree-shaped answer: the NPC tables are where rarity lives, and they are dark. |
| **Mastery** | The Practices ("you have learned how to invite the change without becoming the price") | The General feats: mastery with no sentence. |

The workbook's Arcane path lists **Birthright** as a source. The Sorcerer page
rejected exactly that word; the setting's answer is *marked*, and it is the
one place the generator is more original than the workbook.

---

## 12. The backstory workbook: what a person carries

The workbook builds a fantasy backstory from **Accessory, Food, Sound, Tool,
Reputation** (Renown, Concealability, Authority, Utility) and **a Code of
Honor** with penalties in three grades (Minor: an apology, a small sacrifice;
Medium: a quest, a trial, lost dignity; Major: death, excommunication, a
curse, permanent loss of standing).

The generator has an engine for almost every column and never labels them so:

| Workbook column | Engine |
|---|---|
| Accessory | The signature object (proposed); the Spellbook (built). |
| Food | The Halfling's cuisine; the Servant's cups; the Brewing Practice. |
| Sound | The Bard's instrument map (proposed); the Barbarian chant; the shakuhachi. |
| Tool | The twenty-one Practices. ✅ Complete. |
| Reputation | The Title (Renown); the Rogue's confession (Concealability); the Herald (Authority). |
| Code of Honor | The Orders (six beats, a Sign, seven Relationship forms) and the Paladin's unquoted sentence. |

**The penalty ladder is the piece the Orders lack.** The Orders page drafted
the Relationship forms (MEANS, RESTRAINT, MASK, DEBT, WOUND, THRESHOLD,
REVELATION) and no consequence for breaking the Sign. The workbook's three
grades are a ready table: Minor (the Order asks for an apology, a small
sacrifice), Medium (a labour, a trial), Major (excommunication, a curse the
Order can lay, which is a story and not a bloodline). One draw per Order, on
the Order's Dice.

---

## 13. The villain sourcebook: values, not morals

"Rather than thinking of villains in terms of morality, frame them in terms
of values. Morals are shaped by external forces; values exist internally."
The AlignmentKit docstring arrived at the same place independently
(antisocial, prosocial, organisations, individualism), which is why the two
agree and the Stories engine's Evil gate does not.

The sourcebook's practical proposal fits every character, not only villains:
**one value, stated as a line the table can play.** The 2014 background ideals
in the NPC engine are the ancestor of this; the written backgrounds' hooks
already imply one each (the Gambler never leaves a table before it is
finished; the Exorcist charges). A "value" line, drawn per background and
printed under the hook, would give the sheet its fourth sentence.

---

## 14. Five sentences

Every character the generator makes should be able to say five things, and the
sheet should say them in this order:

1. **Who you are.** The species entry. Written.
2. **What happened to you.** The background and its hook. Written, for thirty-two;
   sixteen thin.
3. **What you do.** The Guild and its lines. Written for four Guilds; drafted
   for nine.
4. **What you want.** The value. Not written anywhere; implied by every hook.
5. **What you hold.** The object. Built for the Spellbook and the titled gear;
   proposed for the rest.

The Backstory is where the five meet, and today it reads none of them.

*Measured (README, "Voice coverage"): the background says its sentence 92% of
the time, the species 58%, the Guild 41%, the feats never.*

---

## 15. Pointers

- **README**: the consolidated open decisions this page argues for.
- **Stories-and-Titles**: the composed Backstory (§14).
- **Orders**: the penalty ladder (§12).
- **Equipment-and-Masteries**, **Guilds-Registers-Names-Devices**: the object
  (§7, §14).
- **Sheet-Alignment-Languages**: values and the alignment axes (§13).
- **Spells-and-Invocations**: Source and Cost for the casters (§11).
- **NPCs-and-Villains**: the two dark gateways (§8).
