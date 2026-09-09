# 📖 Stories and Titles: the Backstory on every sheet

> 🚧 **Draft.** Analysis and proposals, not yet authoritative. Under review.

*Wiki entry for the design team. Every player sheet ends in a "Backstory"
node headed "The story of {Title}", composed by `AtlasEpica/Map_of_Stories.py`
(2,889 lines) with a title from `Map_of_Titles.py` (10,049 lines). Compiled
2026-09-08 from the code and twelve generated stories (seeds 1000 to 1011).*

> **In one sentence.** The engine is well built and the vocabulary is the
> project's oldest register: the story never reads the background's hook, it
> hard-codes the ancestry, curse and mission that the peoples' canon forbids,
> and it closes on tavern jokes under the best-written prose on the sheet.

---

## 1. How a story is made

A `Myth` dict of tokens, each a list of `(gate, text)` pairs. The host is the
Character's genus string (species, class, background, gender, alignment). A
token collapses once, to one eligible text, and is stored back ("literal
collapse", Campbell's monomyth as "the DM Character of a thousand faces").
Ungated `("", …)` entries are the fallback and are also eligible alongside
the gated ones, at equal weight. Draws come from the Character's own Dice Bag
(`identity.story`); a token that never resolves is stripped rather than leaked
("a legend with a hole beats no legend at all").

The skeleton is `{Origin}{Outro}`. `Origin` is one of forty gated templates
or falls to `GenericOrigin`; most templates end in `{Archetype}`, a second
paragraph; `Outro` is one of thirty closing lines.

✅ **The machinery is right.** Seeded, gated, degrading, never leaking, and the
same collapse the Orders use for their arcs. The Gear Titles and Materials
engines explicitly follow its shape. Nothing here needs rebuilding.

---

## 2. What the twelve stories showed

| Character | What the story did |
|---|---|
| Aasimar Paladin Acolyte | Acolyte origin (good: stained glass, "a microcosmos of a vaster war"), then the ungated "recovering buried treasures … for a generous bounty", then a destiny outro. Three registers in one paragraph. |
| Tiefling Warlock Criminal | The **Evil** gate fired: "always resented being a Tiefling". Then "All that remains is finding a decent tavern to start in." |
| Dwarf Cleric Soldier | Soldier origin (good: the night watch, the child who died), then "Their story is just beginning. This is just the first step; destiny waits on the road ahead." Two outros' worth of nothing. |
| Orc Barbarian Farmer | Farmer origin, then the **Barbarian Archetype: enslaved, gladiator's pit**. A farmer with loving parents was a gladiator slave by the second sentence. Then "Probably behind the next suspiciously glowing door." |
| Gnome Artificer Sage | Sage origin, then "Known for **her** fearless resolve … Lando prides **herself**". The template hard-codes a pronoun; no pronoun token exists in the file. |
| Human Fighter Merchant | Merchant, then a mentor called "Meral, the Great Fighter", then the **Fighter Archetype: gladiator**. Two Guilds are gladiators by default. |
| Dragonborn Sorcerer Noble | "descends from a benevolent silver dragon": the Sorcerer Origin hard-codes a bloodline the Sorcerer canon forbids (the mark is suffered, never inherited), and a chromatic ancestry the Draconic Ancestry engine already rolled differently. |
| Goliath Monk Hermit | "Once a mighty Dawnbringer, cast down into a newborn Goliath": the fallen-god origin, ungated, for anyone. |
| Elf Bard Entertainer | Amnesiac origin ("The skills of a Bard! And the knowledge of a Entertainer!"), then "First quest: survive the tavern without spending all the coin." |

Titles drawn: *The Phoenix Of The Swan Shrine, The Ash Of The Oracle, The
Reaper Of The Light, The Star Mestizo, The Sunscale Of The Enchanting Realms,
The Psychic Traveler, The Satyric Whale, The Acolyte Of The Realm, The Timely
Poet, The Wildfire Honor, The Deadly Traveler.*

---

## 3. The story never reads the background

Gates per background in the story file:

| Background | Gates | | Background | Gates |
|---|---|---|---|---|
| Noble | 54 | | Servant, Gambler, Exorcist, Destined, Fated, Survivor, Revolutionary, Wildkeeper, Guardian, Herald, Squire, Arcane Mutant, Bailiff, Aberrant Mutant, Dragon Cultist, Investigator, Spirit Medium, Shadow, Tomb Raider, Guide | **0 each** |
| Soldier | 19 | | | |
| Merchant | 13 | | | |
| Sailor | 10 | | | |

⚠️⚠️ **Not one of the twenty custom backgrounds has a single line in the story
engine.** The backgrounds are the project's reference for voice: each has a
description and a hook, and the hook is a story in one sentence. A Fated, a
Spirit Medium, a Tomb Raider, a Servant, a Gambler gets the `GenericOrigin`
("Long ago, {name} watched the tides tally the years") and the treasure-hunter
Archetype. The two prose systems were written years apart and do not meet. The
sheet says, in its best voice, *"You have never done anything. That has never
been the relevant fact,"* and then, in its oldest, *"Adventure awaits."*

This is the single largest gap between the sheet's two halves, larger than any
2014 leak, because it is on every sheet.

---

## 4. Contradictions with the peoples' canon

The species gates were written before the canon and say the opposite of it:

| Gate | Text | Canon it breaks |
|---|---|---|
| Tiefling Goal | "to break the infernal curse that haunts their **bloodline**" | Tiefling rule 1: no biological determinism; born to ordinary parents; no bloodline. |
| Aasimar Goal | "to fulfill a **celestial mission** whispered in their dreams" | Aasimar: no mission, no sender, the spark has no errand. |
| Sorcerer Origin | "descends from a benevolent silver dragon" | Sorcerer: the mark is suffered, not inherited; a dragon is a state, not an ancestor. |
| Dragonborn Goal | "to unite the **scattered clans** under a single banner" | Dragonborn: a codified, cohesive civilisation with a house that will not let you fall. |
| Orc Goal / Origin | "free from **old hatreds**"; "my village burned down and my parents were turned into cinders" | Orc: the wind path; the burned-village cliché is the one story the species entry refused. |
| Dwarf Goal | "to reclaim a lost ancestral hold" | Dwarf: soul-metal and Sainthood; the hold is Tolkien's, not ours. |
| Gnome Goal | "to invent a device that will change the world" | Gnome page: the joke Gnome the entries left behind. |
| Evil Origin | "always resented being a {species}" | Alignment as a personality; the sheet nowhere else lets Evil mean self-hatred. |
| Barbarian / Fighter Archetype | enslaved gladiator, "fights for the downtrodden" | Barbarian and Fighter pages: neither register is the arena; forces one biography on two Guilds. |
| Monk Archetype | "seeking the world's deadliest, most titanic opponents so that they might challenge and destroy them" | Monk: Bushido and the shakuhachi; this is the tournament anime the page rejected. |
| Warlock Archetype | "a small price for vast power … immaterial blade of unparalleled might" | Warlock: the terms, the device law; the price is never small. |

---

## 5. The registers

Three voices share every paragraph:

- **The Origin templates written recently** (Sailor, Sage, Scribe, Wayfarer,
  Merchant, Farmer, Acolyte, Soldier) are in the backgrounds' register: "The
  tide taught {name} to leave on time, not when ready." "Ink took to {name}'s
  hands early." "Some folk keep houses, but {name} kept horizons." ✅ These are
  the model for the rest.
- **The Archetype fillers** are dungeon-crawl copy: "recovering buried treasures
  from the perilous dungeons of {kingdom} for a generous bounty"; "ready to be
  the deadly weapon the {kingdom} needs".
- **The Outros** split between destiny ("destiny's weight settle on their
  shoulders", six near-duplicates about "mistaking gentleness for frailty") and
  the tavern joke ("Probably behind the next suspiciously glowing door", "The
  world is wide, dangerous, and utterly unprepared for {name}").

The backgrounds' rule was one register per piece. The story runs three in
four sentences.

---

## 6. Names of places

Hometowns: *Stormtor, Stormkirk, Raingate, Rainglade, Rockspring, Rockcross,
Rockspire.* Kingdoms: *United Nation, Free Court, Hollow Kingdoms, Shattered
Symmachia, Shattered Island.*

⚠️ The hometown is Weather + Anglo suffix, for every species. AtlasNomina gives
a Dwarf an Iberian name and a Human a Berber one, and then the story sends them
home to Stormkirk. Place names are the one Nomina layer that never got a
culture key. "United Nation" reads as the UN.

---

## 7. Titles

*Decree 0002 §2 makes the pair mandatory: "we always generate a `Name, Title`
pair ('John Doe, the Person of the Place')." The critique below is of the
vocabulary's keying, never of the pair.*

`Title` composes *The {Descriptor} {Rank}* (weight 20), *The {Rank} {Origin}*
(15), *The {Rank}* (4), all three (1), from vocabularies gated by the genus
string. The docstring's design rule is honest: "If you can say *The X Lord*
and sounds cool, X goes here."

- ✅ The `Genus` docstring records a real bug fixed: `"Cleric" in lusor` asked
  TagKit for a Tag and was False forever, so no conditional vocabulary had
  ever fired. Somebody read the output and noticed. That is the standard.
- ⚠️ `custom_cases` title-cases everything: "The Phoenix **Of The** Swan
  Shrine". English titles lower the particles.
- ⚠️ The composition has no meaning axis: *The Satyric Whale* (Human Fighter
  Merchant), *The Deadly Traveler* (Scribe Wizard), *The Sunscale* (Halfling).
  The Gear Titles engine keyed its vocabulary by culture and legend register
  and got *Wound Widow* and *Frozen Requiem*; the character title is the older,
  unkeyed layer it was modelled on.
- ⚠️ The story then **uses the title in prose** ("accepts the half-mocking
  epithet The Phoenix Of The Swan Shrine, trusting it will mark destiny"),
  which is a good sentence when the title means something and an accident
  when it does not.
- ❓ `Rank` contains "Mestizo" (line 4478). In Spanish it is a neutral word; in
  an English title (*The Star Mestizo*) it reads as a racial category applied
  to a character. The loaded-names rule keeps lore names in the pool; this is
  not a lore name. Undecided.

---

## 8. What the story should be

The sheet already has three voices that work: the species entry (who you are),
the background (what happened to you) and the class lines (what you can do).
The story is where they meet, and it should be composed **from** them rather
than beside them.

**Principle.** The Origin is the background's hook, told in the past tense
with the name in it. The Archetype is the Guild's register in one sentence.
The Outro is the species' organising idea, never explained. Three sentences,
one register each, and every line drawn from a table that already exists.

**Drafts: an Origin per custom background** (the hook, told):

| Background | Origin draft |
|---|---|
| **Servant** | {name} carried the cups in {hometown} and tasted every one first. Nobody asked whether that was loyalty or the other thing. |
| **Gambler** | {name} lost everything in {hometown} twice and won it back once, which is the only arithmetic that ever mattered. |
| **Exorcist** | Something had a family in {hometown}, and {name} was the one who got it out. They did not thank {name} for what it cost the house. |
| **Destined** | People followed {name} out of {hometown} before {name} had decided where to go. They are still following. |
| **Fated** | {name} was told how it ends. Everything since has been a long argument with the telling. |
| **Survivor** | Everyone else in {hometown} is a name {name} says at night. {name} was let go, and has never been sure by whom. |
| **Revolutionary** | {name} wrote the words on the wall in {hometown}. Others painted over them; the words came back in other hands. |
| **Wildkeeper** | {name} kept the boundary between {hometown} and the wood, and learned which side was asking more of it. |
| **Guardian** | {name} stood in a doorway in {hometown} once, and found out that was the whole job. |
| **Herald** | {name} carried the word from one lord of {kingdom} to another, and learned what a word weighs when it is not yours. |
| **Squire** | {name} carried the shield for someone who mattered in {hometown}. What happened to them is why {name} carries a sword now. |
| **Arcane Mutant** | The magic came to {name} in {hometown} and did not pass through. What it left behind has a pulse. |
| **Bailiff** | {name} collected what {hometown} owed and learned every face that could not pay. Some of them are still owed an answer. |
| **Aberrant Mutant** | Something from outside touched {name} in {hometown} and rearranged what it found. {name} is still learning the new order. |
| **Dragon Cultist** | {name} worshipped, in {hometown}, a thing that despises worship. Finding that out was the beginning. |
| **Investigator** | In {hometown} a question went unanswered until {name} answered it, and the answer was wrong for everyone. |
| **Spirit Medium** | The dead of {hometown} talk to {name}. Most of them lie, the way they did alive. |
| **Shadow** | {name} met the Dream in {hometown} at night, wearing its other face. It followed. |
| **Tomb Raider** | {name} opened something under {hometown} that had been closed on purpose, and sold what was inside. |
| **Guide** | {name} took strangers across the passes above {hometown} and never once told them what the last one saw. |

**An Outro per people** (the idea, never explained):

| People | Outro draft |
|---|---|
| Dwarf | *Whatever {name} is made of, the road is finding out.* |
| Elf | *{name} has been away long enough to start looking like somewhere else.* |
| Aasimar | *The light in {name} does not know what {name} intends. It has not asked.* |
| Tiefling | *{name} has never done anything. Everyone who meets {hero} already knows what {name} did.* |
| Dragonborn | *{name} left the house. The house is still there, and so is the door.* |
| Orc | *The wind that took {name} from {hometown} has not yet said where it is going.* |
| Goliath | *{name} made a promise once. The road is the shape of keeping it.* |
| Halfling | *{name} knows the way back to {hometown}. Knowing is enough.* |
| Gnome | *{name} has an idea. This is usually where the trouble starts.* |
| Human | *{name} owes half the people in {kingdom} a favour and is owed by the other half. That is the map.* |

---

## 9. Repairs

- The hard-coded pronouns ("Known for her fearless resolve", "channels her
  fighting spirit"): a `{they}/{their}` token from the Character's gender, or
  rewrite without them.
- Sorcerer silver-dragon Origin: cut, or read the Draconic Ancestry the sheet
  already has.
- `custom_cases`: lower *of, the, and* inside titles.
- The gladiator Archetypes: gate them on a background that earns them (a
  Gladiator background exists in the 2024 list), not on the Guild.
- The Evil Origin: cut.
- Hometowns through AtlasNomina's culture keys.
- "United Nation".

---

## 10. Decisions log

**Standing**: the Story engine (seeded, gated, degrading) is kept as is; the
Gear Titles and Materials engines copy its shape.

**Open (this page proposes)**: the Story composed from the three existing
voices (§8); twenty custom-background Origins; ten species Outros; the
contradiction list in §4 resolved by cutting or rewriting to canon; the
Archetype filler pool retired; the title vocabulary keyed by culture the way
the Gear Titles are.

**Undecided:** "Mestizo" in the Rank pool.

---

## 11. Pointers

- **Backgrounds-Official**: the sixteen thin ones; their hooks are the missing
  Origins for the official set as well.
- **Orders page**: the six-beat arc engine is the same collapse and could
  supply the Story's spine for a Sworn character.
- **Cultural-Inspirations canon**: place-name keys for §6.
- **Guilds-Registers-Names-Devices**: the register per Guild for the
  Archetype sentence.
- **Every species page**: the organising idea behind each Outro.
