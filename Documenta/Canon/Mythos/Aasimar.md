# ✨ Aasimar
> The Mortal Angel

*Wiki entry for the design team. Deep lore and settled direction, not page text.
Compiled 2026-09-08 from the class analyses and Julio's notes; where Julio has decided, the decision is stated as such. The companion entry for the Celestials themselves, written for the NPC generator, is [Celestials.md](Celestials.md).*

> ### **In one sentence.**
> An Aasimar carries the Spark of something perfect, and it is the measuring bar; but the Aasimar is mortal, inperfect, and is always short. Not an angel, but someone who **has to live**. 
> *(Julio, 2026-09-08.)*

---

## 1. Where the Aasimar lives in the code

| What | Where | State |
|---|---|---|
| Species entry (Julio's) | `AtlasActorLudi/SpeciesKit/Aasimar/__init__.py` | Shipping. Second person, no "we". Closes on an open invitation, which stays (§10). |
| The Ideals, the Descents, the mark | `SpeciesKit/Aasimar/Map_of_Ideals.py` | Shipping. Belongs to a shared CelestialKit once QST-0050 lands. |
| Traits and their lines | `SpeciesKit/Aasimar/resolution.py` | Healing Hands, Light Bearer, Celestial Resistance, Celestial Revelation carry a line. Darkvision is chip-only (to change, §10). |
| Names | `AtlasNomina/Races/Celestial.py` | Celestial bodies from every language: a deliberate mosaic. |
| Culture keys | `athens`, `vatican`, `sangha`; legend `crusader` | The subculture's own three, kept (§4). |
| Prayer | `Map_of_Cleric_Prayers.py` | One species line. No lines yet for the three markers. |
| Warlock patron | `AtlasOfGuilds/WarlockKit.py` | Drawn from the same `DESCENTS` and `IDEALS`. To become the descent ancestor for an Aasimar (§8). |

The Aasimar and the Dragonborn are the reference kits for voice (QST-0062). A
generated Aasimar entry reads, for example:

> *Your talaria rest at your shoulder blades and fold away as the seams of a
> toga, shining like verdigris, barred across with silver. Above your head, a
> star of many points, set like a compass rose, glowing like aquamarine shading
> into diamond. It twinkles when you run, and harder when you fly. These are the
> traits of the Sphinx Aidos, so you may belong to its lineage.*

Two axes drawn apart (the wings take the metal, the halo the gem), a tell that
never names the Ideal, four sentence arrangements, and an ancestor whose name is
the thing it guards (*Aidos* is Shame, the reverence that stops a hand; the
generator gave it to an Assassin, which by the loaded-names rule is a story).

---

## 2. Origin: the spark

A Celestial is an Ideal with a shape: not a god and not a servant of one, but
Justice itself, or Mercy, standing where mortals can see it. Celestials are
emanations of the Platonic Forms, encarnated by pure collective (jungian?) belief on the goodness of the concept, and each carries a True Name that defines and limits it (QST-0050). An Aasimar carries a *spark* of one.

> **؂ Note:**  
> 💡 A Celestial and a Demon both gain power from this collective belief in the same way: How good a concept is, that Celestial is more powerful. How bad a concept is, its Demon is more powerful. Same axis, different directions. Demons punish what Celestials prevent. Both are part of the same system of control. Devils, and Fallen Angels do not participate on this axis. 


**The spark is fixed. The Aasimar is not.** 
An Ideal cannot bend, cannot care for a worshipper, cannot love. 
Only the Ideal is important. 
You are important as an artefact of this ideal. 
A mortal chooses, makes mistakes, grows, and has free will. 
The spark sets the bar and the Aasimar lives under it, always a little short, and the aureola reminds him of the distance without judging it.
This is the drama intrinsic to every Aasimar and it needs no villain.

**Eight Ideals** (from `Map_of_Ideals.py`; 
the Celestials page carries the full table): 
- Justice,
- Mercy,
- Sacrifice,
- Truth,
- Freedom,
- Beauty,
- Hope,
- Honor.
All eight are alignment-independent and twistable ("I claim Justice for your
offence"; "Truth is what I say it is").
Vengeance is not an Ideal, because it belongs to the Demons theme: Punishment. 

Saints belong to the Dwarves and are a different system.

**A spark may come from two Ideals.** 
One lends the aureola its form, the other its gem-like color, and either may lend the tell. 
Honor's standing flame, glowing like Beauty's opal, belongs to that pair and to nobody else at the table.

**The spark shapes the vessel** 
(Julio). The Aasimar is not a human with wings.
The body is a biological actualisation apt for the spark it carries: the greenish or bluish skin of the published art, the talaria, the aureola, and perhaps other features pushed toward the "ideal being". 
This is a *physical* inheritance, and the species law permits it: that law guards against monoculture and moral determinism, not against biology (Darkvision already settles the point; nobody culturises themselves into seeing in the dark).
**Self-Actualization.** An aasimar can choose the expression of their wings each time. 
That makes them Self-Actualizing to the choices they make. 
The rest of their appearance and body may follow a similar principle, where their spark and self-view shape the expression of their biology. 
A gnome-born Aasimar is still medium size in the rules. They are not a gnome anymore.

**Older readings the design team should know.** 
The Zoroastrian *Amesha Spentas* (Truth, Good Mind, Dominion, Devotion, Wholeness, Immortality) are personified principles attending the highest god: the closest historical model for an Ideal with a shape. 
The *fravashi*, the pre-existing higher self that each person is said to carry, is the closest model for the spark. 
Neither is directly named on the page nor directly ported into the system. Just inspiration sources. 

---

## 3. The vessel: physiology

**Talaria.** 
Small vestigial wings, sitting only where a wing could take a body's weight (lower neck, wrists, forearms, shoulders, shoulder blades, small of the back, base of the spine, ankles, heels), each folding into something a tailor could hide or explain: a collar, bracelets, a sash, sandal straps. 
They catch the light like a metal (black iron, gold, red iron, silver, verdigris, pearl, tin, bronze), which nods at the Dwarven soul-metals without confirming anything.

**Aureola.** 
The halo, glowing like a stone (onyx, amber, ruby, diamond, aquamarine, opal, moonstone, jade) in a form the Ideal lends: 
- a circle perfectly round from wherever anyone stands (Justice),
- a broken ring (Sacrifice),
- a compass rose (Freedom),
- a standing flame (Honor),
and so on.

In the yogic map the halo is the crown centre made visible, the thousand-petalled lotus drawn above the head; `sangha` reaches `india` at 2, so the Aasimar's own third marker carries the well.

**The tell.** 
Each aureola does one thing, and the thing never names the Ideal it belongs to: 
- it dims when you are not honest;
- it sends a chill down your spine when someone near you is afraid;
- it darkens for a moment whenever you see someone die;
- it falls into chaos when you feel anything strongly;
- it twinkles when you run and harder when you fly;
- it beats once when you see something beautiful;
- it spreads slowly over you when you are happy;
- its colour changes with your mood.
Watching a halo dim tells you somebody lied, not what they descend from.

Three rules govern the tell:

1. **It answers to fidelity, not virtue.** A tyrant whose ring stays perfect is
   entirely possible, and a better story than one whose halo goes out.
2. **It only ever says no.** Socrates' daimonion never told him what to do, only
   what not to; the tell is a daimonion made visible. No later tell may be
   written as an instruction.
3. **Open (Julio):** is the oversight internal or external? Does the Aasimar
   *cause* the halo to change, or does injustice in the room disturb it? "Do you
   feel a disturbance in Justice, or does injustice disturb you?" Both readings
   are live and the sheet must not settle it.

**The square nimbus.** In Roman and Byzantine art a square halo marked a living
person, against the round halo of the dead saint. 
The Aasimar's halo is the imperfect one, the work in progress; a Celestial's is finished. 
A well, not a rule; it also keeps Saints (round, dead, Dwarven) apart.

**"You can hide them or empower them depending on your emotional state."** The
species entry's sentence is the tell's charter, and Celestial Revelation is
the rule: for one minute the thing usually hidden stops hiding.

**Darkvision.** Decided (Julio): printed as an entry with a description and a
brief flavour line, not chip-only. *"Darkness cannot hide the truth from you."*

**Celestials do not care much about the vessel** (Julio). The body is apparatus
for the spark. This is a temperament, and it separates them from every people
who speak of their bodies with pride (the Goliath's size, the Dwarf's beard). An aasimar may take this biew by default, but some may revel (Monks, barbarians...) and focus on the vessel instead of the soul. 

---

## 4. Society: a subculture, not a nation

Decided (Julio, 2026-09-08), superseding the earlier proposal to draw a host
culture for the body.

**The Aasimar are recognisable and distinct wherever they are born.** "An emo or
a punk is easy to see whether in Mexico or in Britain. Same symbols on
different hardware." The three culture markers (`athens`, `vatican`, `sangha`)
are the subculture's own, kept as they are; the gear, the vocabulary and the
manner follow them regardless of who the parents were.

**Born to ordinary parents, like the Tiefling.** The species entry says "you
never lived among them… you are part of one of the many cultures of the
world." What follows is a *pull* out of the birth culture, in one of several
shapes, all of which work and none of which is imposed:

- Poor parents give the child to a **temple**; rich parents send the child to an
  **Academy**, believing they carry high potential.
- The Aasimar joins a **priesthood**, an **international order**, or a network
  that recognises its own on sight.
- A mother names the child with a **holy name**, or the grown Aasimar renames
  themselves with an angelic-sounding one (the name pool of celestial bodies
  from every language is this: Citlalli, Estrella, Whetū, Zvezdana).
- The Aasimar pushes the mortal culture aside for the myths and legends of the
  higher origin; or is defined by **rejecting** that origin. A Dwarvish Aasimar
  is interesting, and the choice is the player's.
- A **culture inside a culture**, like a priesthood class: above the local
  culture rather than outside it.

**A privileged minority.** The Tiefling is the target of hate by default; the
Aasimar is a *model* minority: praised, expected to be great, "the rich kids",
the quarterbacks and cheerleaders to the Tiefling's emo and punk. Both are
minorities; one is integrated upward and one is pushed out.

**The three tempers of the subculture.** Athens reasons; the Vatican
consecrates; the sangha renounces. The through-line is the contemplative order
as such, wherever found (`Cultural-Inspirations.md`). The pensive kind's
failure mode: deliberates while the thing burns. The bodhisattva is the
sangha's figure for the Aasimar: the one who could go up and stays, the
renegade angel, the explorer of life as a path of illumination. Renunciation
is what makes the Aasimar's mortality a choice rather than a defect. 
But for the aasimar the Renunciation may not have been the Aasimar's choice, but the Ideal''s. 

**The shared priesthood.** Deep lore, never on the page: the Aasimar and the
Tiefling once shared one priesthood (the Tiefling canon's crown-horns holding
a flame). The Aasimar's side separated, dichotomised, and rose above the local
cultures; the Tiefling's side was left holding the horns. This is the
theological shift of the Tiefling canon seen from the other end, and it makes
the Aasimar's privilege and the Tiefling's exclusion one event. A Character may
find an inscription that says so. Nobody in authority confirms it.

**Grammar.** The species entry has no "we", and by the mechanism above it
should not at the *species* level: there is no Aasimar homeland. The subculture
may say "we" (the order, the academy, the temple). The Tiefling canon's claim
that its entry is "the only one with no we" should be read as: the only one
whose isolation is *hostile*. The Aasimar's is upward.

---

## 5. Culture and registers

**The markers.** `athens` (the academy, the portico, the fleet), `vatican`
(sacerdotal Rome: office, vestment, canon), `sangha` (the Buddhist monastic
order of South and Southeast Asia: the khakkhara, the vajra, the dha, temple
bronze and saffron lacquer). Legend register `crusader`: late Arthur, the
Grail, the Temple, the pilgrim road, "a myth of election". `crusader` answers
to the Vatican and marches on the Levante.

**Subtler influences (Julio).** Zoroastrianism and the Persian angels;
Manichaeism. Nietzsche's Zarathustra marks the division of heaven and hell:
the departure from a Realm of Death and manifestation of Ideals (a Platonic
beyond, where principles *balance* the world) toward a Manichaean division of
Principle and Punishment, with reward notably absent: *you must be good, and
reward is not guaranteed*. Very Catholic. In that light a Celestial is
**preventionist or redemptionist**, where a fiend is **deterrence or punishing**,
and the Aasimar/Tiefling separation is tainted by this prevention/punishment
moral division and control. See the Celestials page for the NPC consequences,
including the Celestial as a campaign's antagonist.

**The sea (Julio).** Athens' gear is naval: Trireme Trident, Peltast Javelin,
Pelte Shield. The fishing and sea imagery invites two readings at once, and
both are welcome as wells:

- The **fishermen and the fish**: the register of a founder's followers, apostles
  and nets. It sits naturally on the Vatican key.
- **Atlantis**, which is Plato's own myth: the Celestials as the sea-people
  from before, with a faint "ancient astronauts" shimmer (Celestials are,
  after all, *celestial*: stars, planets, constellations). This connects the
  Aasimar to Minoan culture and enriches the Athens/Sparta split with the rest
  of the Greek world: Chios and Ionia, Alexandria, Rhodes.

**The Iliad's gods among men.** An Aasimar drinks from the Iliad's image of gods
and heroes walking on the field and striking in the war. The Odyssey belongs to
the Goliaths; or the **Trojans are the Titans**, and the Trojan War is a war of
Celestials and Titans for the heavens, which the Goliath entry already
suggests ("the gods took the heavens and the songs; the First Ones kept the
world"). Rhodes is another Greek culture available to the Giants. This is the
one place where the two peoples' myths are the same war seen from two camps.

**The stars are Arabic.** Vega, Altair, Deneb, Rigel: the star-names in the
Descents were given by the people the crusader register marches against. An
Aasimar of the Star Altair carries a Levantine name into a crusader's harness.
Never on the page; a DM's gift.

**Lucifer is a Celestial, unfallen.** The Planetars carry the Greek names of
the wandering stars and the Latin morning star is among them. In this setting
the fall is a *reading* (Tiefling canon), and the morning star never fell.
Keep him in the pool; never comment. (`DESCENTS` lists Hesperus twice: keep
one.) 
Another reading is that a Fallen Planetar or an "angel" (common term for celestials in generals, as most people only see angels, not thrones or planetars.) is not automatically a demon or devil. 
Just a Satan (adversary), and the Fallen may still serve an ideal. 
I could see a Planetar of Freedom revelling against the whole plan of controlling the morality of mortals. And both Devils and Fallen Angels being "the imaginary axis" to the controlling paradigm, where they are maybe good or bad, but free people from the simple machiavelian  reading of morality. Maybe a Devil wants to control you, and Lucifer may want you to just be free to be yourself. 
This for the player must be just a reading. 

**Prayer.** The ledger should take sayings and prayers from the Athens,
Vatican and sangha wells (Delphi's "nothing in excess", the Dhammapada's
"hatred is never appeased by hatred", and so on) as *sayings*, without
importing the real-world institutions as lore (Julio).

---

## 6. Metaphysics

**The measuring bar.** Stated in §2. Every class an Aasimar takes is a different
departure from the spark, and the aureola reports every departure.

**Fidelity, not virtue.** The tyrant with a perfect ring is intended.

**The Nephilim.** The Abrahamic root of the half-celestial is ambivalent:
"mighty men of old, men of renown", and the stated reason for the flood. The
blessed reading is also a reading. It rhymes with the Tiefling's theological
shift (one mechanism, opposite ends) and gives the Aasimar an unspoken history
that need never be resolved.

> What about the reading of the Mythic Greece? The Hero that was not good, just mighty?

**The Holy Horror** (Julio). "He made you just to do its bidding?" A Celestial
cannot love an Aasimar; it can *hire* one, and it can *make* one for the job.
The crusader register is "a myth of election", and election's shadow is exactly
this cosmic-plan horror: if you were chosen, the choosing was the Ideal's,
and your life is the shape of somebody else's decision. An Aasimar may come to
suspect that "you never lived among them" was a placement, not an accident.
Nobody confirms it. The Celestial patron's briefing voice already says the true
thing as a joke: "They will tell the one you crossed that it was your own free
will."

**Prevention and punishment.** 
A Celestial prevents the corruption of an Ideal, or redeems toward it; 
a fiend deters or punishes. 
Neither is kind. 
A Celestial that tries to installs an Ideal *into* a person, or into a party, is a legitimate
antagonist, and the Inquisitor background's superior ("send them on, the gods will know their own") is what that looks like from below.

---

## 7. Relationships with the other peoples

| People | The relation | Deep lore, never on the page |
|---|---|---|
| **Tiefling** | The mirror. One mechanism (belief makes celestials; belief makes fiends), opposite readings. Model minority against hated minority. | The shared priesthood, split by the Aasimar's side (§4). A Tiefling and an Aasimar are cousins who were told different stories about the same flame. |
| **Goliath** | The other people who hold Greece and Rome as identity, opposite halves. Athens against Sparta; the Vatican against the legion. | The Trojan War as Celestials against Titans (§5). Two camps, one war. |
| **Dragon / Dragonborn** | The fixed against the self-authored. An Ideal cannot bend; a dragon authors itself alone. | **Couatl.** A dragon bound to an Ideal, or an Ideal that Ascended into a dragon's shape: the Celestial Dragons. Julio: "That may be how Couatls are made." The Dragon Cultist Aasimar is one road to it. |
| **Dwarf** | Saints are the Dwarves' and stay there; the talaria's metals nod at the soul-metals and confirm nothing. | Two systems that look like one from a distance. The ambiguity is deliberate DM space. |
| **Elf** | Fixed against malleable: the Ideal against the collective Dream. | The Elves are the only people whose nature is decided by what everyone agrees to imagine; the Aasimar is a fixed ideal, only it's power being empowered by the affinity to that belief. |
| **Human** | Institutions. The temples and academies that take Aasimar children are mostly Human-built ("there is always a human kingdom"). | The Human Cleric's watcher is a church; the Aasimar is what the church points at. |

---

## 8. The classes: departures from the spark

The Celestials' vocabulary names several classes (Julio's etymologies). That
is colour, not fantasy: the *fantasy* of each class is its own, and an Aasimar
in it is one more mortal departing from a fixed thing.

| Class | The word | The Aasimar in it |
|---|---|---|
| **Barbarian** | *barbaros*, outsider: "the foreigners of heaven, the mortal with impulses and wants" | Living true to an emotion, coded as Rage. Plato's Sun against Plato's charioteer: no auriga, but a wild horse can still see the sun and run toward it. Three shapes: the Zealot for the Ideal; the deeply feeling wanderer who takes everything as a miracle; the philosopher who loves the Ideal and the wisdom to understand it. |
| **Monk** | *monachos*, the one who lives alone | The body taken as sacred, and the spark channelled through it: Focus flowing from the aureola down through the body into the fist. Not a departure: the spark embodied. Lived. |
| **Cleric** | *klērikos*, the allotted | The spark cannot love you, so the Aasimar Cleric looks for the parent the Ideal is not. The most obvious pairing and the best drama. |
| **Paladin** | *palatinus*, the Palatine guard (Rome, Byzantium) | Blood and vow both impeteritous, since an oath cannot bend either. The interesting Aasimar Paladin swears an Oath *against* or *in conflict* with the Ideal, and the aureola shows the strain. |
| **Warlock** | *convenire*, *diathēkē*, *berith*: the covenant. "Form, not belief; not principle but contract." | Hired by its own blood. **Decided (Julio): for an Aasimar Celestial Warlock, the patron is the descent ancestor** (same Descent, same Ideal). Drama is higher with a family member; the Holy Horror (§6) is the second horror beside instrumentality. The Fiendish or GOO patron's are interesting in the sense of corruption to the ideal. "The self vs the job". |
| **Sorcerer** | *sortiarius*, the bender of fate | Independent of species, as every class is; a synergy is welcome, not required. The spark from the Ideal may have awakened something, or been a way for something else to get in. Only a Celestial-flavoured origin would draw on the spark; a draconic or shadow origin needs another explanation, and the player gives it. |
| **Wizard** | *magi*, the astronomers and intellectuals of the East | Native through Athens, and therefore flat; the interesting Aasimar Wizard is the sangha's renouncer who studies. |
| **Bard** | *bardos*, the praiser | The Muses' class. An Aasimar of Muse descent playing the Muse's own art is the one pairing where spark and profession coincide. |
| **Druid** | the most external to a Celestial (Caesar, Pliny) | Two readings: a keeper of balance and order from the principle inherited, or a renegade who embraces the mortal world. The Circle of Stars relates to the Celestials' own realm. |
| **Ranger** | *saltuarius*, *limitanei*, *horoi*, *peripoloi*: the wardens of the frontier | The Aasimar itself is a warden of the frontier between the Celestial and the mortal realms. Hope's halo, "one unmistakable star in the dark", navigates by its own head. |
| **Fighter** | *pugnator*, *bellator*, *agonistēs*, *polemistēs*: "the hand that holds the sword" | The justiciar. The hand of the heavens. Achilles, Heracles, the Hero: the Iliad's register of gods striking on the field. And through Athens' naval gear, a marine of the fleet rather than a hoplite. |
| **Rogue** | *rogare*, the vagabond | Rejects the calling in every incarnation but one: the **Celestial Reaper**. An Assassin of Sacrifice has a halo that darkens at every kill, a tally it cannot stop keeping; an Assassin of Justice who kills without a disguise keeps a perfect ring. |
| **Artificer** | *artifex* | Daedalus was Athenian: wings built for someone else. |

**Synergies as a general mechanism** (Julio). The Warlock decision above is the
first of a family: where a species and a subclass share a source (the Aasimar
and the Celestial patron; the Dragonborn and the Draconic Sorcerer's ancestry;
others in other species), the generator should draw them as one. Independent
choices, but when they meet, they meet as family.

---

## 9. Backgrounds: the tell meets the hook

The Ideal's tell is the Aasimar's hook in every background, because it reports
on conduct without naming the principle.

- **Servant × Mercy.** Mercy's chill "when someone near you is afraid"; the
  Servant "stood at the sideboard… Not once did anyone say a mean word to
  you." The Servant of Mercy felt every guest's fear, every night, and poured.
- **Gambler × Justice.** "Your face is good." The ring above it dims when you
  bluff. A Gambler who cannot bluff and wins anyway.
- **Inquisitor.** "There was a child… she burned." An Inquisitor whose Justice
  halo dims when they say "send them on"; or one who watched a superior's halo
  stay perfect through it: the tyrant with a perfect ring, seen from below.
- **Fortune Teller × Truth.** The ring scatters when you feel strongly; or
  (Julio) the halo is what *sells* the reading, when contact is real.
- **Spirit Medium × Sacrifice.** The halo darkens for a death and not for the
  already dead: how the Medium tells a death from a haunting.
- **Revolutionary × Freedom.** "It twinkles when you run." The compass rose as
  a getaway light.
- **Shadow.** A light casts no shadow of its own; the Shadow Aasimar is
  physically consistent and nobody believes the explanation.
- **Destined.** "You glow." On an Aasimar, twice. Right, and everyone is tired
  of it.
- **Exorcist.** Celestial Resistance: the one who cannot be possessed, and so
  cannot be sure the procedure works on anyone else.
- **Debunker.** The Debunker with a halo, who has an explanation for it.
- **Bailiff × Honor.** The Badge and a mood ring; the open question of §3
  (internal or external oversight) lives here most sharply.
- **Herald.** The aureola as credential.
- **Dragon Cultist.** The fixed against the self-authored, in a cult: the road
  to a Couatl (§7).
- **Stranger.** Doubly from elsewhere; the old ones are the only people who
  might know what the halo used to mean.

---

## 10. Decisions log

**Decided (Julio, 2026-09-08)**

- The Aasimar keep `athens`, `vatican`, `sangha` as their own culture. They are
  a subculture recognisable across host peoples; no host-culture draw for the
  body. Aasimar and Tiefling stay distinct.
- The species entry's closing invitation ("Think about which ideal can inspire
  {name}") **stays as written**. The design principle (the drawn Ideal) is not
  the play principle; the player reads whatever they want from the mark, and an
  Ideal may be complex, a synthesis, or not there at all. Death of the Author.
- **Freedom's Muse is Dance** (Terpsichore). Dance is an expression of freedom;
  the empty `muse` field was a mistake, not a design. Update `Map_of_Ideals.py`.
- Darkvision is printed as an entry with a line: *"Darkness cannot hide the
  truth from you."*
- `DESCENTS` keeps one Hesperus.
- The prayer ledger takes sayings from the three wells; it does not import
  real-world institutions as lore.
- The species law ("taught, not inherited") guards against monoculture and
  moral determinism only. Physical traits are biological. The Sorcerer's "born
  different" is a legitimate fantasy and independent of species.
- For an Aasimar Celestial Warlock, the patron is the descent ancestor.
  Species-and-subclass synergies of this kind are wanted generally.

**Open**

- Whether the aureola's oversight is internal or external (§3). Keep both.
- Whether `vatican` reads too modern (`see`, `basilica`, `apostolic` are the
  alternatives) and whether `sangha` is the right name (`theravada`, `nalanda`);
  from `Cultural-Inspirations.md`.
- Which Ideal, if any, takes Euterpe (music, lyric); the only Muse still
  unassigned.

**Rejected**

- The host-culture draw for the Aasimar body.
- Any change to the closing invitation of the species entry.
- Joy as a ninth Ideal for Terpsichore (superseded by Dance as Freedom's).

---

## 11. Lines

*Julio's drafts, kept as written; the incomplete one is completed with a proposal
marked as such.*

| Entry | Line |
|---|---|
| **Darkvision** | *Darkness cannot hide the truth from you.* |
| **Celestial Revelation, Talarian Wings** | *You spread your wings to show your true self.* |
| **Celestial Revelation, Inner Radiance** | *You can feel your inner light giving you the…* (Julio's, unfinished). Proposal to complete: *You can feel your inner light, and for one minute you let it be seen.* |
| **Celestial Revelation, Necrotic Shroud** | *The brighter the light, the darker the shadow.* The only place the kit lets the Aasimar show the Tiefling's face; exactly one sentence. |
| **Monk's Focus, Aasimar only** (proposal) | *It comes down from the ring above your head and out through your hands. The body was always the instrument. You only had to consecrate it.* |
| **Celestial Patron, Aasimar only** (proposal, for the ancestor synergy) | *You know exactly who hired you. You have their wings.* |

---

## 12. Pointers

- **[Celestials.md](Celestials.md)**: the beings themselves, for the NPC
  generator: Ideals, Descents, temper, how they act, the Celestial as
  antagonist, the Couatl.
- **Tiefling**: the mirror; the shared priesthood; integration against
  exclusion.
- **Goliath**: Celestials against Titans; Rhodes; the Odyssey.
- **Dragon canon**: the Couatl as an Ideal-bound dragon.
- **Bard**: Dance is Freedom's; Euterpe open.
- **Sorcerer**: the species law read correctly; synergy, not collision.
- **QST-0050**: the CelestialKit shared between players and NPCs, which this
  page and the Celestials page both need.
