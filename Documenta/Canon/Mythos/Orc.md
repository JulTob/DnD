# 🐎 Orc

> 🚧 **In flow.** 1 of 11 chapters are still proposals. 🔒 4 · 🧾 3 · 🔎 3 · 🚧 1

*Wiki entry for the design team. Deep lore and settled direction, not page text.
Compiled 2026-09-08 from the Orc kit, the species entry, `AtlasNomina/Races/Orc.py`,
the peoples table in the Dragon and Elf canon, the class analyses and the design
notes.*

> **In one sentence.** The children of the horizon: the people who were on the
> plains first, were never asked, and are called raiders for riding the roads
> that were theirs. Every soul walks a wind path, and if they fall, they carry on.

---

## 🧾 1. Where the Orc lives in the code

| What | Where | State |
|---|---|---|
| Species entry | `AtlasActorLudi/SpeciesKit/Orcs/__init__.py` | Shipping. First person plural. Closes on "why {name} left the Orc Camp, and what would bring them back." |
| Traits and rules | `Orcs/resolution.py`, `traits.py` | House pattern (QST-0094). Adrenaline Rush: *"The winds of your storm are hard to catch, rider. Run, be free, and run."* Darkvision: *"The ride does not end at nightfall, and neither does your watch."* Relentless Endurance: *"Do not fall, rider! Be strong! Carry on!"* |
| Names | `AtlasNomina/Races/Orc.py` | A phonetic rule with a body inside it: "big fangs: S would bite the tongue, Z instead" (Th→z, S→Z, Gue→ke, ou→u, J→X, h→j, V→B). Inspirations listed as a fusion (§5). |
| Culture keys | **none** | ⚠️ The Orc has no row in `_CULTURES`; gear draws from the generic pool only. |
| Prayer | `Map_of_Cleric_Prayers.py` | *The storm is coming.* *The storm guides the winds.* *The wind rider must master the storm.* *The wind rider must follow the storm.* |
| Metaphysic | the peoples table | *The wind path: a route each soul walks rather than a substance it is made of.* |

---

## 🔒 2. Origin: the wind path

Each people has one organising idea. The Orc's is the only one that is a
*route* rather than a substance: the Dwarf is a metal, the Celestial an Ideal,
the Elf a dream, the Dragon a self; **the Orc is a path walked.** *"Every soul
walks a wind path, and we orcs carry our own through the storm. If we fall, we
carry on."* Relentless Endurance is the sentence as a rule: reduced to 0 Hit
Points, you drop to 1 instead, once a day.

The path is walked, not owned. The plains "are open to everyone, and riders
must travel." Nothing in the Orc's metaphysic is a possession, which is the
whole quarrel with everyone who fenced the plains.

**Physical traits.** Adrenaline Rush (a Dash as a Bonus Action with Temporary
Hit Points), Darkvision, Relentless Endurance. Endurance, speed, the watch that
does not end at nightfall: a body shaped for the long ride.

---

## 🧾 3. History: nobody asked

*"Your people were on the plains first. Then the dwarves came for the gold
underneath, the humans came to call it discovery, and the elves promised trade
and brought curses. No orc was asked."*

Three peoples, three takings, in one sentence, and each is the other people's
entry seen from the plains: the Dwarves' "long terrible expeditions" chasing
metal; the Humans' "there is nowhere humans wouldn't go"; the Elves' "found
commerce". The Orc entry is the setting's one account of what the other
peoples' virtues cost.

*"Now all orcs are riders and no camp is safe. The new peoples fence the plains
and attack when your beasts pass through the old ways. You are called raiders
instead of riders."* The exonym is the species' wound, and unlike the
Barbarian's it is *not* reclaimed: the Orc's answer is to ride further, carry
more, and go without longer than anyone who says it.

**The rule about parallels.** The Orc entry rhymes with real histories of
displacement, and the name file lists real peoples. The Tiefling canon's rule
applies in spirit: never name the parallel on the page. The entry does not, and
must not.

---

## 🔎 4. Society: riders

**The camp.** No camp is safe, so the camp moves. The Orc entry's closing
question is "why {name} left the Orc Camp, and what would bring them back": the
camp is the home, and it is the one home on the roster that is always somewhere
else.

**The rider, not the raider.** *"You ride further, carry more and go without
longer than anyone who says it."* Tireless and Roving as a people. The Ranger
page found the Orc entry is already a Ranger's; the Barbarian page found the
two storm prayers disagree on purpose (does the rider master the storm or
follow it?), which is the Zealot against the Berserker in the species' own
mouth.

**The storm.** *"The storm is coming. The storm guides the winds."* The storm
is the Orc's weather, god and road at once, and the species has no Cleric
watcher but this. The Sea Druid Orc (Druid page) found the one plain that
cannot be fenced.

**The steppe by temper, unkeyed.** The Orc reads as the steppe (the horse, the
eagle, the yak-tail tug, the epic recited without a book), but `mongol` is an
Elven key and the Orc has *no key at all* (§5). The temper is in the entry; the
vocabulary is nowhere.

---

## 🔒 5. Culture: the missing keys

⚠️ **The Orc has no culture keys.** Every playable people except the Orc and the
Halfling has a row in the gear map; the Orc draws a plain Longsword where a
Dwarf draws Toledo steel. The name file's inspirations are a *fusion* (Britain,
Celts, Vikings, cowboy America, Native Americans, pre-Columbian languages, the
Boyz of 40k), which the brief's law forbids as keys ("one culture key = one
culture; never fuse"), and none of them is assigned.

This is the decision to make, and the page records the directions without
choosing:

- The entry's *temper* is the steppe rider (the horse, the eagle, the long
  ride, the standard that is not a flag, the epic without a book). `mongol` is
  already the Elves'; the brief models overlap by influence, not by sharing.
- The name file's phonetics ("S would bite the tongue") are a design in their
  own right and survive any key.
- The class pages have already read the Orc through the steppe: the berkutchi's
  golden eagle (Beast Master), the *nerge* ring-hunt (Hunter), the manaschi's
  half-million lines (Lore Bard), the yak-tail tug (Banneret), the morin khuur
  (instrument). If the Orc gets a key, those readings land on it; if not, they
  stay as the wells a DM reaches for.

**Prayers**: the four storm lines. **Materials**: none of the Orc's own; horn
and sinew and felt-bound iron sit under `mongol`.

---

## 🔒 6. Metaphysics: the storm and the path

**Rage's second cosmology.** *"If we fall, we carry on"* is Relentless Rage in
nine words, and the storm is the Orc's Rage. The rider carried by the storm
(Berserker) and the rider who masters it (Zealot) are the two prayers.

**The pact as the first consent.** *"No orc was asked."* A Warlock's pact is the
one time in the species' history somebody asked (Warlock page).

**The first book.** The Primal practice is "nothing is written; it is walked",
which is the Orc's metaphysic word for word: a *route*. An Orc Wizard is the
first of the riders to write the epic down, and the manaschi will not forgive
them (Wizard page). An Orc Artificer's Steel Defender is the first horse an Orc
never had to bury (Artificer page).

**Against the Dwarves.** The Dwarf came for the gold underneath; the Orc was on
top of it. The two entries are one event from both sides, and a Dwarf and an
Orc in one party carry it.

**The unfenced plain.** The sea signs nothing and cannot be fenced (Druid page):
the Orc Sea Druid is the species' happiest pairing and the dice found it.

---

## 🔎 7. The classes: the ride in each

| Class | The Orc in it |
|---|---|
| **Ranger** | The species entry is already a Ranger's. Horde Breaker is the nerge from the horde's side; the golden eagle on the arm. |
| **Barbarian** | Rider carried or rider mastering: the two prayers. Adrenaline Rush is Instinctive Pounce as a species trait. |
| **Paladin** | Vengeance: the species grievance as a vow. Glory: the rider's kleos. The Banneret's tug ("a banner is not always a flag"). |
| **Druid** | The Sea: the one plain that cannot be fenced. The Land Circle's covenant ("what may be taken, what must be left") is the Orc grievance as doctrine. |
| **Bard** | The manaschi: the horde's memory, no book. "No orc was asked" is the epic's first line. |
| **Monk** | "Run, be free, and run" is Step of the Wind with a species name. |
| **Cleric** | The storm is the watcher; the two prayers disagree about whether it carries or commands. |
| **Wizard / Artificer** | The first book; the unburied horse. |
| **Warlock** | The first consent. |
| **Fighter** | The tercio's alférez becomes the tug-bearer; endurance as the drill. |
| **Rogue** | ⚠️ "You are called raiders instead of riders" is the exonym; an Orc Thief or Assassin who decided to earn it is a dangerous story and must not be the default. Keep alignment out. |
| **Sorcerer** | Wild Magic as the storm in one rider. |

---

## 🔎 8. Backgrounds

- **Ice Nomad.** *"Your people do not stay; they follow: the herds, the thaw,
  the old roads."* The Orc's background in all but the ice; the two texts
  should be read together, and an Orc Ice Nomad is nearly redundant.
- **Stranger.** "You will be from somewhere else for the rest of your life."
  The Orc whose somewhere else is a camp that moved.
- **Vagabond.** "The road raised you." The ride without the horde.
- **Survivalist.** "Carry nothing you can't carry yourself."
- **Wildkeeper, Naturalist.** The plains as the field; the herds.
- **Sellsword.** The rider for hire, called a raider by the employer.
- **Herald.** The camp's envoy to the peoples who fenced it.
- **Renegade.** "You took a corner of the world and dared them to come get
  it": the fence, reversed.
- **Bailiff.** The law that fenced the plains, served by one of the fenced.
- **Guardian.** "No camp is safe." The one who stands at the camp's edge.
- **Revolutionary.** The Cause is the plains.
- **Squire, Servant.** The rider who served a settled master.

---

## 🔒 9. Decisions log

**Decided**

- The species entry speaks as "we"; the three trait lines are the house
  pattern's reference along with the Elf's and the Halfling's (QST-0094).
- The wind path as the metaphysic (peoples table).

**Open**

- **The Orc's culture keys.** None assigned; the name file's list fuses. The
  steppe temper is in the entry.
- **Materials**: none of the Orc's own until a key exists.
- **The name file's inspirations** should be split into distinct keys or
  cut, per the law, whichever the author chooses.

**Repairs**

- None found in the Orc's own text. The Cleric ledger's Orc lines are clean.

---

## 🚧 10. Lines

*The three trait lines exist and are the reference. No additions.*

| Entry | Line (shipping) |
|---|---|
| **Adrenaline Rush** | *The winds of your storm are hard to catch, rider. Run, be free, and run.* |
| **Darkvision** | *The ride does not end at nightfall, and neither does your watch.* |
| **Relentless Endurance** | *Do not fall, rider! Be strong! Carry on!* |

---

## 🧾 11. Pointers

- **Cultural Inspirations**: the Orc's keys (open).
- **Ranger, Druid, Bard, Barbarian pages**: the steppe readings.
- **Dwarf page**: the gold underneath.
- **Tiefling page**: the rule about parallels.
