# 🏔️ Goliath

> 🚧 **Draft.** Analysis and proposals, not yet authoritative. Under review.

*Wiki entry for the design team. Deep lore and settled direction, not page text.
Compiled 2026-09-08 from the Goliath kit and its six Giant heritages, the species
entry, `Cultural-Inspirations.md` (the Celestial/Giant comparative and the
Arthur ruling), the class analyses and the design notes on the Aasimar page.*

> **In one sentence.** Giants manifested before the first things and are still
> here if you know how to look at a mountain; each Goliath carries one Giant's
> favour the way other people carry a surname, tends the Order of Things, and
> comes from a civilisation that fell. The greater they fall.

---

## 1. Where the Goliath lives in the code

| What | Where | State |
|---|---|---|
| Species entry | `AtlasActorLudi/SpeciesKit/Goliaths/__init__.py` | Shipping. First person plural ("we tend the world"). Closes on three questions that are three classes (§7). Speed 35. |
| Giant heritages | `Goliaths/Giant_Heritages/` (Cloud's Jaunt, Fire's Burn, Frost's Chill, Hill's Tumble, Stone's Endurance, Storm's Thunder) | Each carries a line: *"The favour you carry came down from a Storm Giant, and it answers weather with weather."* |
| Traits and rules | `Goliaths/resolution.py`, `traits.py` | Powerful Build: *"You were made smaller than your ancestors, never lighter."* Large Form: *"For a few minutes you are the size your ancestors never stopped being."* Dice notation settled here (`_signed_die`). |
| Names | `AtlasNomina/Races/Giant.py` | "Giants (meaning)"; Wairimu, Ōga; an Oni subtype. Thin header. |
| Culture keys | `rome`, `sparta`, `homeric`; legend `arthuriana` (early Arthur) | Noric steel, hoplite bronze, heroic bronze and Mycenaean gold, lake-tempered steel in the Materials map. |
| Prayer | `Map_of_Cleric_Prayers.py` | *The winds are fast, but they do not hurry.* *Each snowflake is small, but it is part of the avalanche.* War: *Stand your ground. Understand your enemy.* Light: *The darkest night holds the brightest stars.* |
| Canon | `Cultural-Inspirations.md` §Celestials and Giants; §Why Arthur belongs to the Giants | The crossed comparative; the decline myth; dragon versus giant. |

---

## 2. Origin: the First Ones

*"Giants manifested before the first things. And Giants are your ancestors.
Before anyone had a word for Winter, she had a name and a temper. Your
ancestors did not command the avalanche. They were the avalanche, and the
mountain, and the thunder. The gods took the heavens and the songs. The First
Ones kept the world, having never stopped being it."*

**The Giants are the world**, not its rulers. Some of them "turned and made
something much smaller, and gave it life, and many favors": each Goliath
carries one favour and knows which Giant it came from the way other people
know a surname. The heritage is a *gift* from a relative who is also a
landscape.

**The Order of Things.** *"We are part of this world, part of The Order of
Things, from the breathing sky to the living earth."* The Goliath's duty is to
tend the world and everything the Giants made, "with respect and awe". The
metaphysic in one line, from the entry: *"our strength is not our might, but
our duty."*

**Six favours**, drawn once and kept:

| Giant | Favour | The line's image |
|---|---|---|
| Cloud | Jaunt: a 30-foot teleport | "it was…" (a step through the sky) |
| Fire | Burn: extra Fire damage on a hit | "it has not…" (gone out) |
| Frost | Chill: Cold damage and slowed Speed | "it arrives the way cold does, without announcing itself" |
| Hill | Tumble: knock a target Prone | "what it puts…" (down, stays down) |
| Stone | Endurance: a Reaction that reduces damage | "stone does…" (not hurry) |
| Storm | Thunder: a Reaction that answers damage with Thunder | "it answers weather with weather" |

**Large Form** at 5: for a few minutes the Goliath is "the size your ancestors
never stopped being." **Powerful Build**: "made smaller than your ancestors,
never lighter."

---

## 3. The comparative: Greek in myth, Roman in method

The Celestials and the Giants are the only peoples who hold Greece and Rome as
*identity*; everyone else inherits them faintly. They do not divide the
classical world: they each take half of each, and the halves are opposites.

| | **Goliath** | **Aasimar** |
|---|---|---|
| Greek half | **Sparta and the Iliad**: the agoge, the phalanx, the single combat, the giants and titans | Athens: the academy, the argument |
| Roman half | **Legionary Rome**: the road, the aqueduct, the siege engine, the drill | Vatican Rome: the see, the canon |
| Temper | Naturalist, physical, practical | Pensive, philosophical, contemplative |
| Meets a problem by | Doing it, and reasoning after | Reasoning it through first |
| Authority rests on | Deed and physical proof | Consecration and argument |
| Failure mode | Solves the wrong problem, thoroughly | Deliberates while the thing burns |
| What happened to their world | **It fell.** The empire split, interbred, ran itself into oblivion | It endured |
| So their legends are | **Aftermath**: the ruin, the warlord, the caste that outlived its reason | Continuity |

Neither is the civilised one and neither the brute: two ways of being serious.

**Homer earns his own key.** A hoplite in formation is not Achilles. `sparta`
is the agoge and the phalanx; `homeric` is the Iliad, the heroic age, the
titans and giants the Goliaths descend from. The Giants' own war is Homeric
before it is anything else.

---

## 4. History: the greater they fall

**Arthur belongs to the Giants.** Early Arthur (`arthuriana`) is what the
legion becomes once the legion has gone: a washed and half-remembered story of
a decaying garrison, sprouting a warlord who carves the people into a caste of
knights above everyone else. Not a founding myth: a **decline myth**, and the
Goliaths are the fallen civilisation. A Goliath carries the grandeur of Rome and
the wreckage of it in the same hand. Late Arthur, the Grail and the sanctified
knight, went to the Celestials as `crusader`; the two strata overlap on the
Grail Knight, and that is deliberate.

**The Arthurian epoch is thick with giants.** The beanstalk, the seven-league
boots taken from an ogre, the knights who went out to kill dragons: giant
stories before they are knight stories.

**Dragon versus giant.** The Dragonborn and the Goliaths are set against each
other in the myth layer, not merely different. The dragon-slaying knight is a
Goliath story about a Dragonborn. The `wyrm_myth` register (Dragonslayer,
Wyrmbane, Serpent's Bane) is currently held by the dragons; the brief leaves
open whether it comes to the Goliaths, and the Ranger page offers a fourth
option (the Ranger holds it by Guild). A Goliath with dragon magic is the
myth's defector.

**The war for the heavens** (the author, Aasimar page). *"The gods took the heavens
and the songs. The First Ones kept the world."* Read the Trojan War as
Celestials against Titans: the Trojans are the Titans, the Iliad's gods
striking on the field are the Celestials' register, and the Odyssey (the long
way home from a war that is over) is the Goliaths'. Rhodes stands with the
Giants: another Greek culture for a people whose Greece is Sparta and Homer,
not Athens. Two peoples, one war, two camps. Deep lore, never a proper noun on
a sheet.

**The Palatine.** *Palatinus*, the Paladin's name, is the Palatine guard, and
Rome is the Goliaths' key. The imperial guard whose empire fell: the oath that
outlived its reason, in the class's own name (Paladin page). The Goliath
Paladin is the roster's most native pairing after the Goliath Barbarian.

---

## 5. Culture and registers

**Sparta**: the agoge (the Fighter's training, the Champion's laurel), the
phalanx that marched to a flute (Tyrtaeus: the Goliath Valor Bard), the krypteia
(the Gloom Stalker's shadow, which the Goliaths do not talk about), *"We learn
by suffering"* (Aeschylus; orphaned in the prayer ledger under the dead
`greece` key and belongs here), *"Come back with your shield or on it"*.

**Homer**: the *aristeia* (a god breathes *menos* into the hero: the Goliath
Zealot is Diomedes in book five), the funeral games for Patroclus (the
Champion's laurel comes from a funeral), Atalanta and the Calydonian boar (the
Goliath Hunter), Hephaestus's tripods that walk (the Goliath Battle Smith),
Odysseus *polytropos* (the Goliath Rogue, inverting the size joke),
*"Always to be best and to excel above others"* (Iliad 6.208).

**Rome**: the palus (Vegetius' training post: the Fighter class text is
literally the Roman drill), Vitruvius and the aqueduct (the Goliath Wizard and
Artificer as the legion's engineers; Force Ballista is a Roman engine by
name), the road and the siege, *"While I breathe, I hope"* and *"Make haste
slowly"* in the prayers.

**Arthuriana**: Kingsword, Sword in the Stone, Oathblade, Questing Lance,
Blazoned Shield, White Harness. The aftermath knight's kit.

**Materials**: Noric steel, tinned bronze, legion-stamped iron; hoplite bronze,
olive wood, laconian iron; heroic bronze, boar-tusk, Mycenaean gold;
lake-tempered steel, chapel silver.

**Names**: the file is thin (Wairimu, Ōga, an Oni subtype: the Japanese ogre
as a Giant kind). ⚠️ The name pool does not yet carry the three keys; Spartan,
Homeric and Roman names (Leonidas, Ajax, Marcus) would put the comparative in
the first word a player reads. The generator's Goliaths (Bergoracan
Anarsiasson, Liernar Fonelarison, Bergalenon Drustson) read Norse by
patronymic, which is the Elves' key.

---

## 6. Metaphysics: duty, not might

**The Goliath entry asks three classes' questions.** *"Do you respect and
protect the land? Do you rage with the storm? Or do you observe the cycles of
the night sky?"* The Land Circle, the Storm Giant's Barbarian, the Stars
Circle. It is the only species entry that invites the class, and the model for
how the others could close (Barbarian page). The Order of Things is the
Druid's covenant, and for a Goliath the elder society the Druid never left is
literally the family.

**Doing it, and reasoning after.** The Fighter's class text ("There is no
secret. That is the secret.") is the Goliath temper. The Barbarian's ("You
lose hesitation") too. The one Goliath who reasons first is the interesting
one: the Goliath Wizard, the Goliath Rogue.

**The fallen empire and the Dwarves' fallen mountain.** Two peoples with a
lost greatness they remember; the Dwarves carry ledgers and grudges, the
Goliaths carry duty and awe. The Dwarf wants the Crown back; the Goliath tends
the ruin. The Tiefling has a lost greatness nobody remembers at all.

**Against the Celestials.** The Goliath's authority is deed; the Aasimar's is
argument. A Goliath and an Aasimar in a party are the comparative table at a
campfire, and the Trojan War is their shared ancestor story told from opposite
camps.

**The avalanche and Rage.** *"They were the avalanche."* The Barbarian is the
Goliath's home class; the Storm Giant's Thunder answers damage with Thunder,
which is Retaliation as a species trait. *"Each snowflake is small, but it is
part of the avalanche"* is the World Tree's "you are very small, you are part
of it" in the Goliath's mouth.

---

## 7. The classes: the favour in each

| Class | The Goliath in it |
|---|---|
| **Barbarian** | The species' home. "Do you rage with the storm?" A Homeric Goliath Zealot is the aristeia; a Storm Goliath Berserker answers weather with weather. |
| **Fighter** | The palus, the agoge, the laurel from a funeral. The Goliath Champion (seed 81) is native. |
| **Paladin** | The Palatine guard of a palace that is gone; Glory (Achilles' short life and long name); duty as the species' word before the class's. |
| **Druid** | Talking to relatives. The Order of Things is the Land Circle's covenant. |
| **Bard** | Tyrtaeus; the phalanx marched to a flute; "the greater they fall" is the song. |
| **Cleric** | The parent is the landscape: the most literal watcher on the roster. |
| **Wizard / Artificer** | Vitruvius; the legion's engineer; Hephaestus's tripods; the ballista. The one Goliath who reasons first. |
| **Rogue** | Odysseus. |
| **Ranger** | Atalanta; the krypteia as the Gloom Stalker's shadow. |
| **Monk** | The avalanche that learned to be light; a Cloud Goliath Shadow Monk teleports twice. |
| **Sorcerer** | The Storm as Wild Magic; Draconic as the myth's defector. |
| **Warlock** | A pact with an ancestor is a family matter; the Storm Archfey. |

---

## 8. Backgrounds

- **Guardian.** "The wall between the weak and the wolves." Duty as a job; the
  Goliath Guardian is the phalanx's one shield.
- **Soldier, Sellsword.** The legion for hire; the good name is the road you
  built.
- **Ice Nomad.** The Frost Giant's child on the ice roads.
- **Squire.** "You served someone the songs are about." The Goliath Squire
  served a Giant, which is a mountain, which does not need its horses fed.
- **Herald.** The Goliath Herald walks in past the guards because nobody stops
  someone that size; "harming a herald is how small quarrels become wars" is a
  smaller quarrel than it sounds.
- **Stranger.** The emigrant from a fallen empire whose grandeur and wreckage
  are in the same hand.
- **Archaeologist.** The ruin as a career: the Goliath Archaeologist reads
  their own people's roads.
- **Naturalist, Wildkeeper.** The Order of Things as a field diary.
- **Survivalist.** Stone's Endurance as a background.
- **Destined.** Comic: the giant-blooded chosen one who "can walk further than
  anyone else in the party" and is right.

---

## 9. Decisions log

**Decided**

- The crossed comparative (Greek in myth, Roman in method); the five atomic
  keys (QST-0046.4); early Arthur to the Giants, late Arthur to the Celestials
  (`a1f1837`, `ac9f3ce`).
- The species entry speaks as "we".

**Open**

- **`wyrm_myth`**: the brief's three options, and the Ranger page's fourth.
- **The name pool** does not carry the three keys (§5).
- **The Trojans as Titans**: a war of Celestials and Titans for the
  heavens, the Odyssey as the Goliaths', Rhodes with the Giants. Worth a
  paragraph in `Cultural-Inspirations.md` beside the comparative, as deep lore.
- **Darkvision**: the Goliath has none; nothing to decide.

**Repairs**

- Move *"We learn by suffering"* from the dead `greece` key to `sparta` or
  `homeric` in the prayer ledger (Cleric page §5).

---

## 10. Lines

*The Goliath's trait lines exist and are among the best on the roster ("made
smaller than your ancestors, never lighter"). Listed as the reference; the
heritage lines are the house pattern for a drawn ancestry. No additions
proposed.*

| Entry | Line (shipping) |
|---|---|
| **Giant Ancestry** | *The favour you carry came down from a [Cloud / Fire / Frost / Hill / Stone / Storm] Giant, and…* (six variants; the Storm's: *it answers weather with weather*; the Frost's: *it arrives the way cold does, without announcing itself*) |
| **Powerful Build** | *You were made smaller than your ancestors, never lighter.* |
| **Large Form** | *For a few minutes you are the size your ancestors never stopped being.* |

---

## 11. Pointers

- **Celestials page**: the comparative; the war for the heavens.
- **Paladin page**: the Palatine.
- **Fighter page**: the palus, the laurel.
- **Dragonborn page**: dragon versus giant; the slayer's words.
- **Dwarf page**: two fallen greatnesses.
- **Cultural Inspirations**: the Trojan reading; the name pool.
