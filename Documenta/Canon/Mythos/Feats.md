# 🎯 Feats, Gifts and Boons

*Wiki entry for the design team. The feats are on every sheet at levels 1, 4, 8,
12, 16 and 19, and they are the largest surface of the generator that no page
has read for its fantasy. Compiled 2026-09-08 from `Map_of_Official_Origin_Feats.py`,
`Map_of_General_Feats.py`, `Map_of_Epic_Boons.py`, `FeaturesKit.py` and
`Grimoire_of_Features/__init__.py`.*

> **In one sentence.** The Origin feats are the backgrounds' mechanical half
> and carry their fantasy well; the General feats are what the road taught and
> say nothing about it; the Epic Boons are every class's level-19 capstone and
> the closest the rules come to the Ascending, and they arrive as abbreviations.

---

## 1. Where the feats live

| Layer | Where | State |
|---|---|---|
| Origin feats (base 2024) | `FeaturesKit.py` (`ORIGIN_FEATS`) | Skilled and Skillful carry a line (*"You trained and studied, gaining a few skills along the way. Time will tell which of them you'll need."*); the rest are rules. |
| Origin feats (setting) | `AtlasOfFeatures/Map_of_Official_Origin_Feats.py` | Twenty-five, most of them **rebrands of published faction feats** with design comments; nine are **Dark Gifts**. Rules on the sheet; no lines. `Strong Arm` is defined twice (lines 864 and 2021). |
| General feats | `AtlasOfFeats/Map_of_General_Feats.py` | Forty-three, 2024 text, no lines. The level 4, 8, 12 and 16 draws. |
| Ability Score Improvement | `Grimoire_of_Features/__init__.py` lines 329 to 339 | *"You gain +2 Strength."* Flat; "Intellicence" is a typo. |
| Epic Boons | `Grimoire_of_Features/__init__.py` lines 303 to 540 | Twelve, compressed ("+1 to any ability (max 30)", "PB", "Re-charges"). `Map_of_Epic_Boons.py` is a file of `None`s after the wipe. `ApplyEpicBoon` draws with the **global** `random`, against Decree 0002 (a QST-0089 shape). |
| Fighting Styles | `AtlasOfFeats/Map_of_Fighting_Styles.py` and a second dict in `Grimoire_of_Features` | Two definitions of the same catalogue. |

---

## 2. The Origin feats: the backgrounds' mechanical half

Every custom background has an Origin feat, and most are published faction
feats with the faction taken out and the setting put in. The design comments in
the file are the project's own reasoning and are worth keeping as lore:

| Feat | Rebrand of | Background | The comment's insight |
|---|---|---|---|
| **Cupbearer** | Vampire's Plaything | Servant | "A cupbearer served the drink *and* tasted it first for poison." The removed benefit "settled the one question the Background refuses to settle, namely whether you were a victim or an accomplice." |
| **On a Roll** | Tireless Reveler | Gambler | "The published name reads as a party. The rule is a streak: somebody else spends their luck and yours comes back, which is the hot hand, not a feast." |
| **Hard to Hold** | Vampire Hunter | Exorcist | "Both benefits are about *not being taken*. You get out of what holds you." The Exorcist's whole trade, as a feat. |
| **Aurora** | Child of the Sun | Destined | "It is an *aura*: allies within 10 feet share it, which is why the Background is about the people who follow you." |
| **Jinx** | Shadowmoor Hexer | Fated | Hex always prepared, and Backfire: the curse aimed. |
| **Spared** | Survivor (the feat) | Survivor | Renamed "so the Background may take the name." Hypervigilance and Steel Yourself: the one who was let go, and is ready. |
| **Agitator** | Harper Agent | Revolutionary | Thieves' Cant, an instrument, and "Cause a Scene" from 30 feet. |
| **Wildwarden** | Emerald Enclave Fledgling | Wildkeeper | Speak with Animals as a ritual for eight hours; "Warden's Shift". |
| **Bastion** | Tyro of the Gauntlet | Guardian | "Stand as One": the ally cannot be pushed while you stand there. |
| **Banner Bearer** | Lords' Alliance Agent | Herald | Inspiring Strike, Reassert Honor. |
| **Field Lieutenant** | Purple Dragon Rook | Squire | Rallying Cry on Initiative: "greatness has logistics." |
| **Arcane Conduit** | Spellfire Spark | Arcane Mutant | Magic Absorption, Overflow. "Magic comes to you and does not pass through." |
| **Strong Arm** | Zhentarim Ruffian | Bailiff | Exploit Opening, On My Mark. |
| **Mutant Aberration** | Aberrant Dragonmark | Aberrant Mutant | Mutant Fortitude, Mutant Magic. |
| **Dragon Cult Initiate** | Cult of the Dragon Initiate | Dragon Cultist | Dragon's Tongue, Dragon's Terror, Inspired by Fear. "Kept flavor." |
| **Sharp Eye** | Sharp Eye | Investigator | Advantage on Search and Study, Proficiency Bonus times. |

✅ **The rebrands are the setting's method applied to rules**: the mechanic is
kept exactly, the faction is removed (Death of the Author), and the name is
chosen to mean the background's thing rather than the publisher's. The
comments explain each choice, which is the standard the Warlock kit set.

⚠️ **None of it reaches the sheet as a line.** An Origin feat prints its bold
sub-features and rules. The design comments are the mythos, and the player never
sees a sentence of it. One italic line per Origin feat, drawn from the comment,
would make the background's mechanical half speak in the background's voice.

---

## 3. The Dark Gifts

*"A boon that arrived uninvited and kept a share of you."* Nine, from the
Ravenloft register, and every one of them carries a one-line identity as a
Python docstring:

| Dark Gift | Docstring (not on the sheet) | Background |
|---|---|---|
| **Gathered Whispers** | (Spirit Medium's; Grave Words, Augury without slot) | Spirit Medium |
| **Shadow Cast** | Mist Walker renamed; "Domain Traveler is deliberately absent. It was the one benefit whose text named Ravenloft's geography." | Shadow |
| **Aberrant Anatomy** | *Exposure to something from outside has rearranged you.* | (pool) |
| **Echoing Soul** | *You remember a life that was not this one.* | (pool) |
| **Living Shadow** | *Your shadow moves on its own, and occasionally on its own behalf.* | (pool) |
| **Touch of Death** | *Something in you is already partway across.* | (pool) |
| **Watchers** | *Something is always looking, and it is not on your side.* | (pool) |
| **Second Skin** | *There is another shape in you, and it does not always wait to be asked.* | (pool) |
| **Symbiotic Being** | *Something else lives in you, helps you, and is not on your errand.* | (pool) |

✅✅ **These docstrings are already the inspiration lines.** They are in the
house register (second person, the fact and the unease, no proper noun), they
are one sentence each, and they are hidden in the source. Moving them to the
sheet is the cheapest improvement on the roster.

**Versatile draws them, by Julio's call.** *"A Human's Versatile draws from base
feats and every setting Origin feat, Dark Gifts included."* The Warlock and
Human pages flagged a Human Tomb Raider carrying *Shadow Cast* ("It Follows")
with no story as a leak; it is a decision, and the pages are corrected. What
remains true: a Dark Gift that arrives through Versatile needs *its line* on the
sheet more than any other feat does, because the background did not explain
it. "Something in you is already partway across" under Touch of Death does the
whole job. The Dark Gift is the Human entry's "power of friendship" turned over:
the boon that came from the one alliance nobody chose.

---

## 4. The General feats: what the road taught

Forty-three feats, drawn at levels 4, 8, 12 and 16, printed as 2024 rules with
the ability-score clause first: *"Increase your Constitution or Wisdom by 1, to
a maximum of 20. You have proficiency with Cook's Utensils…"*. No lines. The
Ability Score Improvement prints *"You gain +2 Constitution."*

These are the sheet's account of the years between the levels, and they say
nothing about them. The principle for a line: **a General feat is what the road
taught, and the line says where.** Never a mood; a place or a habit.

| Feat | Draft line |
|---|---|
| **Ability Score Improvement** | *The road asked, and the body answered.* |
| **Alert** | *You stopped being surprised. It was cheaper than being brave.* |
| **Lucky** | *Three times in your life the dice were wrong in your favour. You have not asked why.* |
| **Tough** | *You have been hit more than you have been missed, and you are still here.* |
| **Resilient** | *One thing used to get past you. It does not any more.* |
| **Durable** | *You heal like someone who cannot afford to stay hurt.* |
| **Speedy** | *You learned that most trouble is slower than you are.* |
| **Chef** | *Somebody has to feed them. You found out it was you, and you got good at it.* |
| **Fey-Touched** | *Something on the other side of a hedge took an interest. You can step the way it does.* |
| **Shadow-Touched** | *The dark did you a favour once. You have not finished paying.* |
| **Inspiring Leader** | *You say the thing before the fight that lets them walk into it.* |
| **Keen Mind** | *You read faster than trouble arrives, and you remember what you read.* |
| **Observant** | *You watched. That was the whole training.* |
| **War Caster** | *You can hold a spell in one hand and a sword in the other and lose neither.* |
| **Great Weapon Master** | *You stopped swinging carefully. It turned out careful was the problem.* |
| **Sharpshooter** | *Distance is a number, and you learned to ignore it.* |
| **Sentinel** | *Nobody walks past you to get to them.* |
| **Polearm Master** | *You learned the reach, then the butt of it, then the moment they step in.* |
| **Ritual Caster** | *Slow magic, from a book, by candlelight. It works, and nobody stops you.* |
| **Skill Expert** | *One more thing you do the way other people breathe.* |

The rest follow the same rule when Julio wants them; twenty is the set the
generator draws most.

---

## 5. The Epic Boons: level 19, and the cap

Twelve Boons, one at level 19 (and the Fighter's at 19 by class). Every Boon
opens *"Increase one ability score by 1, to a maximum of 30"*: the one place on
the sheet where a mortal passes the mortal cap of 20.

✅ **The Boon is the rules' whisper of the Ascending, for every class.** Primal
Champion, Body and Mind, Arcane Apotheosis and the Boon all say the same thing
in the same round: the inner nature, fully lived, exceeds the species. The
Dragon canon's mechanism ("realisation actualises the body") is a level-19
feat with a different name on every sheet. Never say so; let the line hint.

⚠️ The texts arrive compressed ("+1 to any ability (max 30)", "PB", "CON mod",
"Re-charges on initiative", "Once you use this benefit. (once per Long Rest)"),
which is the one place on the sheet a capstone should not read as a note to
self. And `ApplyEpicBoon` draws with the global `random` and prints "Epic
Boom!": a QST-0089 shape (a Character's draws go through its own Dice), and a
possible break in the seeded replay at level 19. Rules work; recorded.

| Boon | Draft line |
|---|---|
| **Boon of Irresistible Offense** | *Nothing they are made of turns your blow any more.* |
| **Boon of Combat Prowess** | *Once a round, you decide the miss did not happen.* |
| **Boon of Dimensional Travel** | *Distance stopped applying to you between one thing and the next.* |
| **Boon of Energy Resistance** | *Two kinds of fire chose you, and you choose which two each morning.* |
| **Boon of Fate** | *Luck within sixty feet of you is yours to lean on.* |
| **Boon of Fortitude** | *Forty more of you, and every mending mends more.* |
| **Boon of Spell Recall** | *Sometimes the slot does not spend. You have stopped counting on it and started noticing it.* |
| **Boon of Recovery** | *You have gone down for the last time. It did not take.* |
| **Boon of Skill** | *Everything, a little. One thing, entirely.* |
| **Boon of Speed** | *Thirty more feet, and nothing can hold you.* |
| **Boon of the Night Spirit** | *The dark stopped hiding you and started being you.* |
| **Boon of Truesight** | *You see what is there. All of it. It is not always a gift.* |

---

## 6. Decisions log

**Decided (Julio)**

- Versatile draws from base feats and every setting Origin feat, Dark Gifts
  included.
- The rebrand method: published mechanics kept, faction removed, name chosen
  for the background.

**Open (this page proposes)**

- Move the Dark Gift docstrings to the sheet as italic lines (§3).
- One line per setting Origin feat, drawn from its design comment (§2).
- General feat lines on the rule "where the road taught it" (§4).
- Epic Boon texts written out and given lines (§5).
- A line for the Ability Score Improvement.

**Repairs**

- `Strong Arm` defined twice; keep one.
- "Intellicence".
- `Map_of_Epic_Boons.py` is a file of `None`s; `ApplyEpicBoon` uses the global
  `random` and prints "Epic Boom!".
- Fighting Styles defined twice.
- The Epic Boon texts' abbreviations and the broken "Once you use this
  benefit." sentence.

---

## 7. Pointers

- **Backgrounds-Official**: the Origin feat is the half that already works.
- **Human page**: Versatile corrected to Julio's call.
- **Warlock page**: the Dark Gift finding corrected.
- **Dragonborn page**: the Boon as the Ascending's whisper.
- **Feature-Text canon**: the docstring-as-line pattern.
