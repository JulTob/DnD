# 🌙 Elf

*Wiki entry for the design team. Deep lore and settled direction, not page text.
Compiled 2026-09-08 from `Elves-and-the-Dreaming.md`, the Elf kit and its five
lineages, `AtlasNomina/Races/Elf.py`, the old wiki, the class analyses and Julio's
notes. The Elf canon's first rule governs every line: never explain the Dreaming
on the page.*

> **In one sentence.** Elves came out of the Fae, and the Fae are made of
> dream; something of that stayed in them, so an elf is malleable the way a
> dream is, and a people that lives somewhere long enough, and loves it long
> enough, begins to look like it.

---

## 1. Where the Elf lives in the code

| What | Where | State |
|---|---|---|
| Species entry (Julio's) | `AtlasActorLudi/SpeciesKit/Elves/__init__.py` | Shipping. First person plural. Three wars, one word (Elvenkind), and "seven hundred years to be patient in, and you only need one second to shoot." |
| Lineages | `Elves/Wood_Elf.py`, `High_Elf.py`, `Dark_Elf.py`, `Fae_Elf.py`, `Shadow_Elf.py` (`Drow.py` is the Dark Elf's older name) | Each carries a "we" paragraph (the body and the temper) and a lineage spell set. Fae and Shadow Elves are the Lorwyn pair, renamed. |
| Traits and rules | `Elves/traits.py`, `resolution.py` | The house pattern (QST-0094): an italic line, then the rule. Trance's line: *"Elves are said to be made of the same essence as dream and nightmare. Perhaps there is more than mere poetry to it."* |
| Names | `AtlasNomina/Races/Elf.py` | Inspirations: Persian, Nordic Fae (Huldufólk), Iceland, Romani, Celtic Ireland. "Th becomes S, T or Z: elves don't show their tongues." White pupils. Society notes in the file header. |
| Culture keys | `norse`, `rus`, `mongol`, `celt`; legends `tolkien_elves`, `fairytale_fae` | "A bit Fae and a bit other people, in a colder nature." |
| Prayer | `Map_of_Cleric_Prayers.py` | *Dreams are made to be lived.* *May the dream guide your way.* Light: *Light, love, and music will endure.* Knowledge: *We live in one another's shadow* (Irish). |
| Old wiki | `app/Wiki/Lore.html` | The "Other Folk, Fata and Hidden People"; clans called **Khans**; "a living echo of dreams." |
| Canon | `Documenta/Canon/Elves-and-the-Dreaming.md` | Lineages are cultures; the drift is collective; Fae, Fata and Shadow are one substance. |

---

## 2. Origin: the Dreaming

**Lineages are cultures, not bloodlines.** Dream of the forest for a thousand
years and you become a Wood Elf: hairier, some with little stag horns. Dream
of the deep places and you become a Dark Elf, skin like the stones of home.
Dream of the crossings and your ears grow exquisite. Never by one elf's
choosing; over centuries; and never alone. An elf raised elsewhere drifts
elsewhere, given time.

**The mechanism is collective.** A shared subconscious in the Jungian sense.
Every legend the people tell shapes them a little; every century of living
somewhere marks the whole culture; the individual carries what the people
dreamt. This is why the lineage entries are written in the first person
plural: *we* adapted, *our* forebears stayed where the trees were.

**Five lineages from three wars.** The species entry names three: painted faces
hunting intruders in the woods (Wood), icy ships conquering seas (High),
ambushers who came from below (Dark). The Fae Elf and the Shadow Elf are the
branches that never came across at all, which is why their marks are the
strangest.

**Fae, Fata, Shadow: one substance.** The Dream wears a different face
depending on who is looking, and mortals named each face separately because
they met it separately. Fae is the Dream met as court, glamour and bargain
(Titania, the Archfey). Fata is the same thing met as one old woman in a wood
(Baba Yaga; Latin *fata*, the Fates, through *fatare*, to enchant, is where
*fairy* comes from). Shadow is the Dream met as nightmare. Nothing
distinguishes them but the encounter. A fae speaker who calls itself a shadow
is telling the literal truth and the mortal hears poetry; use it once per text,
never more, or it becomes a lecture.

**What it quietly explains.** Trance: elves never entirely left the dreaming,
so four hours of meditation reach it. Why the Shadow Elf is not a villain: the
nightmare face is the same substance.

**Physical traits are biological** (Julio's reading of the species law): Keen
Senses, Fey Ancestry, Trance, Darkvision. The Dream shaped the body over
centuries; the body is what the Character has tonight.

---

## 3. The five lineages

| Lineage | The dream | The body (from the "we" paragraphs) | The temper | Where the answers come from |
|---|---|---|---|---|
| **Wood Elf** | The forest, a thousand years | Hairier; some with little stag horns; some still paint their faces | Pensive, observant, direct | The druids first |
| **High Elf** | The ice, the ships, the sea | Golden hair; skin cold to the touch whatever its tone | Patient, cold, adaptive; "found magic, found commerce, found crafts" | The magi and the wizards |
| **Dark Elf** | The Underdark, and staying | Silvery hair; skin like the stones of home | Cunning, calm, welcoming; "a meritocracy… while others poisoned our legend" | The priest and the cleric |
| **Fae Elf** | The crossings; the branch that never came across | Ears "exquisitely long, sometimes as long as our arms"; the most beautiful of elvenkind "even with our charms off" | Polite, friendly, more open to emotion | The Courts |
| **Shadow Elf** | The Shadow realm, "what was left"; the other branch that never came across | Skin any grey from perfect white to pitch black; eyes all white | Stoic, reflective, analytic: "to discern dream from thought" | The oracles and mystics |

The lineage paragraphs are Julio's and are the species' physical voice. Two
things they establish that later prose must keep: the Dark Elf's legend was
*poisoned by others* (the Drow slander is in-world slander), and the Shadow Elf
"feels scary at times, but it's home."

---

## 4. Society: the Other People

**Elvenkind.** *"War after war, we fought each other, but now one word unites
us… Today a long peace holds, and it holds because nobody is counting grudges
any more."* The peace is recent, defended by "arrow and spell", and threatened
by "Warmongers, Dark Lords and Separatists". The elves are the setting's people
who *chose to forget*, against the Dwarves who remember and the Goliaths who
fell. The Bard page found the Dream drifts on story; a people who stopped
telling the war stories stopped becoming the war.

**Khans.** The old wiki: elves wander in powerful, secretive clans called
Khans, "guardians of ancient magics and legends lost to mortal memory." The
name file's society notes add a scholarly, artistic society blending Persian
elegance with Nordic secrecy, druidic rituals, seasonal festivals, and **a
nomadic clan that travels the world, bringing music and crafts to other
cultures.** The `mongol` key is the steppe; the `rus` key is the river-road;
`norse` is the icy ships; `celt` is the woods and the harp. The Khan is what a
clan is called when its people were archers who rode.

**Speech.** *"Th becomes S, T or Z: elves don't show their tongues."* A
phonetic rule with a manner inside it, and the kind of detail the wiki should
keep.

**The Other People, the Hidden Folk.** The old wiki's register: Celtic and
Nordic legend's *aos sí* and *huldufólk*, "those who walk at the edge of the
seen and unseen." The species entry's opening is the same claim from inside:
*"The Other People. That's us."*

---

## 5. Culture and registers

**Norse**: the berserkr and the úlfheðinn are Odin's, so the Berserker's mythic
home is Elven (Barbarian page); Egil the poet-berserker and his head-ransom
(Bard); Skaði and Ullr, the huntress and the bowman, so the Elf Ranger has its
own gods and need not be Legolas (Ranger); Loki the thief (Rogue); the Hávamál
in the prayers (*"Cattle die, kinsmen die…"*); Tam Lin and Thomas the Rhymer
on the Celtic side, the only stories where an Archfey pact *ends* (Warlock).

**Celt**: the historical druids ("they think it improper to commit their
studies to writing", Caesar), so the druid as an institution is Elven and a
Human Druid is one by trade (Druid page); Gwydion the trickster-magician
(Rogue); the *filí* whose satire raised blisters (Bard); *"We live in one
another's shadow"* (Knowledge prayer); Gawain's girdle and the Wild Hunt
(Paladin, Ranger).

**Mongol and Rus**: the steppe archer's speed on foot (Monk); the river-road;
the Khan as the clan's name; *"Gods are not in strength, but in truth"* (Rus,
Knowledge); *"The Eternal Light is watching"* (Mongol, Light).

**Legends**: `tolkien_elves` (Elven blades, star-glass, mithril shirts);
`fairytale_fae` (cold iron, thorn and briar, the rowan staff; shared with the
Fae and the Goblins).

**Materials**: oak, yew and the woods' materials through the Elf and Druid
themes; mithril through the Tolkien register.

**Names**: Persian elegance, Icelandic and Celtic sagas, Romani travel, the
Huldufólk. The generator's elves: Elri Flameseeker, Nailo Dreamchaser,
Siamin Nightweaver, Dinendenan Gloryfinder, Zeirgelidrar Redresen. (The
trailing "g" on some generated Elf names, *Flameseekerg*, *Gloryfinderg*, is
QST-0052's trailing-character bug and not a naming choice.)

---

## 6. Metaphysics: the people decided by what everyone imagines

**Against the other Platonisms.** Two peoples are Platonic (Dwarf: soul-metal
given; Celestial: an Ideal fixed) and the Elves are Jungian: the only people
whose nature is decided by what everyone agrees to imagine. That is the joke,
and the design.

**The Elves are Druids at species scale.** "Dream of the forest for a thousand
years" is Archdruid's slowed ageing done unconsciously by a whole people. An
Elf Druid does on purpose, in one life, what the species does over centuries.
Never say so.

**Change is slow and shared: three tensions the classes create.**

- **The Moon Druid** changes shape nightly. Wild Shape is a learned form, not a
  lineage drift, so the canon is not broken; the elders will *think* it is.
- **The Wild Magic Sorcerer**'s surges may change an elf's body in a scene, which
  the canon says never happens. The dice can break the rule; the story is the
  Dream leaking through one person, and the elders' horror.
- **The Elf Wizard writes it down**, and the Dream is never written. The
  elders' one forbidden act. **The Elf Artificer** builds mechanisms, which the
  Gnomes left the Dream to do; the reverse Gnome. The second forbidden act.

**The Bard drifts the people.** *"Every legend the people tell shapes them a
little."* An Elf Bard's ballads are, over centuries, what the next Wood Elves
look like. The class that operates the Dream from outside (Bard page).

**The Archfey Warlock signed with the substance they are made of.** The verse's
"we shadows" is literal for an elf. A Fae Elf Archfey Warlock is the Dream's own
child taking the Dream's own terms, and "We shall never see quite where" is the
one privacy the patron grants.

**The shadow budget.** Shadow Elf, Shadow background, Warrior of Shadow, the
`shadow` gear theme: four sites that can land on one sheet. The canon's own
rule about the slip (once per text) is broken by composition. A mild negative
affinity between them (Decree 0005) keeps the word rare without closing a door.

---

## 7. The classes: the Dream in each

| Class | The Elf in it |
|---|---|
| **Barbarian** | The Berserker's mythic home (Odin's bear-shirts and wolf-coats): a High Elf Berserker off the icy ships is the truest berserkr on the roster; a Wood Elf Wild Heart is an elf mid-drift. |
| **Druid** | The species at scale; the Moon Elf's elders (§6). |
| **Ranger** | Skaði and Ullr; the Dark Elf Gloom Stalker ("ambushers who came from below"); the Fey Wanderer who came back "a little too charming for the woods". ⚠️ The Elf Ranger is the cliché's landing zone; refuse "archer". |
| **Bard** | Egil's head-ransom; the skald's *níð* as Cutting Words; the Dream drifting on story. |
| **Wizard** | The one who writes what the species dreams (§6). The Fae Elf Bladesinger and the sword dance that taught calligraphy. |
| **Warlock** | The Archfey: signed with the substance (§6). Tam Lin as the pact that ended. |
| **Rogue** | Loki, Gwydion; the Dark Elf Assassin. The shadow budget. |
| **Monk** | The steppe archer's speed; Trance and mushin are neighbours (an elf is vestigially in the Dream already). The Shadow Elf Warrior of Shadow: the nightmare face as an element. |
| **Paladin** | Gawain's girdle: the Ancients Paladin sworn to what was here first, which for an elf is the Fae, which is the Dream, which is their own subconscious. Undying Sentinel gives an elf nothing they did not have. |
| **Cleric** | The watcher is *everyone*: the shared Dream. "Maybe the universe itself" is the Elf's guess, and closer to true than they know. |
| **Sorcerer** | Wild Magic as the Dream drifting fast in one elf (§6). |
| **Fighter** | Studied Attacks across a century; the Chaotic Psi Warrior ("you are your own master") as a Dream-descended child refusing the collective. |
| **Artificer** | The reverse Gnome (§6). |

---

## 8. Backgrounds

- **Shadow.** The Shadow background ("you were born on the other side, where
  the Fae are made of dream and shadows are made of nightmare") is the Elf
  canon's own sentence. On a Shadow Elf it is redundant; on a Fae Elf it is the
  branch meeting its nightmare face. Mind the budget.
- **Fated.** "Promised to a witch." Fata is the Dream met as one old woman; a
  Fated Elf was promised to their own substance.
- **Naturalist, Wildkeeper.** The Wood Elf's defaults; the drift as a career.
- **Stranger.** An elf who left Elvenkind: "a language fewer people speak each
  year" in a people who live seven centuries is a slow catastrophe.
- **Vagabond.** The nomadic clan of the name file: the elf who brings "music
  and crafts to other cultures".
- **Ice Nomad.** The High Elf's ice, on foot.
- **Sellsword, Soldier.** The peace "needs arrow and spell to defend it";
  the Elf who defends it for pay.
- **Investigator, Debunker.** The Shadow Elf's "discern dream from thought" as a
  profession.
- **Servant, Gambler.** The elf in a drawing room, where the Dream is
  furthest away.

---

## 9. Decisions log

**Standing (canon)**

- Never explain the Dreaming on the page. Lineages are cultures, never
  bloodlines. Change is slow and shared: no elf transforms in a scene, no elf
  transforms alone. The Fae/Fata/Shadow slip once per text, at most.

**Decided (Julio)**

- The species entry speaks as "we" (`9be3a07` era); the lineage paragraphs
  likewise.
- The house pattern for trait entries (italic line, then rule) is the Elf's
  and the Halfling's, and the reference for the other peoples (QST-0094).

**Open (this page proposes)**

- The shadow budget nudge (Decree 0005) across Shadow Elf, Shadow background,
  Warrior of Shadow and the `shadow` gear theme.
- The `Drow.py` file duplicates `Dark_Elf.py` under the old name; one should
  go (QST-0091.1's one-file rule).
- The Elf Ranger and "archer": the class text, when written, should not say
  the word; the species entry already owns the bow.
- QST-0052: trailing "g" on generated Elf names.

---

## 10. Lines

*The Elf's trait lines exist and are the house pattern. Listed here as the
reference, with one proposal.*

| Entry | Line (shipping) |
|---|---|
| **Keen Senses** | *Your elven eyes are sharp and your attention focused.* |
| **Fey Ancestry** | *The echoes of the Fae still linger in you, letting you see…* |
| **Trance** | *Elves are said to be made of the same essence as dream and nightmare. Perhaps there is more than mere poetry to it.* |
| **Wood Elf lineage** | *The woods have always answered your people, and some of that answer stayed with you.* (Julio removed "first": the nativist undertone.) |
| **Dark Elf lineage** | *The dark taught your people how to survive it, and some of that lesson still answers when you call.* |
| **High Elf lineage** | *Your people traded with more than merchants, and not everything you brought home was cargo.* |
| **Fae Elf lineage** | *The crossing into the Feywild left more on you than long ears.* |
| **Shadow Elf lineage** | *Telling dream from thought took practice, and the practice stayed.* |
| **Darkvision** (proposal, if the Aasimar convention spreads) | *The dark is only the Dream with the lights off. You have never been afraid of it.* |

---

## 11. Pointers

- **Druid page**: the species at scale; the Moon Elf.
- **Bard page**: the Dream drifts on story.
- **Barbarian page**: the Berserker's Norse home.
- **Ranger page**: Skaði; refuse "archer".
- **Warlock page**: "we shadows" as literal.
- **Monk and Rogue pages**: the shadow budget.
- **Celestials page**: fixed against malleable.
