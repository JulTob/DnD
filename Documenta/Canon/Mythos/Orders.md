# 🕯️ The Secret Orders

> 🚧 **In flow.** 1 of 10 chapters are still proposals. 🔒 1 · 🧾 1 · 🔎 7 · 🚧 1

*Wiki entry for the design team. The Orders are the one engine in the project
that generates prose the way the custom backgrounds are written, and the layer
of the setting that sits between a people and a class: the house a Character
actually belongs to. Compiled 2026-09-08 from `OrderKit.py`, the four Maps in
`AtlasOfOrders`, QST-0048's build notes, QST-0061, and three collapsed Orders.*

> **In one sentence.** An Order precedes the Character: a house already standing
> in the world when someone knocks, sworn to two mythic spheres it has never
> reconciled aloud, working its magic in one of three traditions, keeping one
> relic it has no right to, and holding its members to a bargain whose last
> clause is a goal older than any of them.

---

## 🔎 1. Where the Orders live in the code

| What | Where | State |
|---|---|---|
| The Order object; `Swear(char, order)`; the per-Order feat | `AtlasLusoris/OrderKit.py` | Works. `Order(seed)` collapses itself with its own dice; `Swear` binds a Character. Self-test green. |
| Records: Facet, Domain, Tradition | `AtlasOfOrders/Grimoire_of_Orders.py` | Three shapes and nothing else. |
| Twelve Domains | `AtlasOfOrders/Map_of_Domains.py` | One per published Dragonmark, wearing a mythic name (§3). |
| Three Traditions | `AtlasOfOrders/Map_of_Traditions.py` | Arcane, Divine, Primal: places, practices, organizations, devotions, a safe spell pool. |
| The story arc and its pools | `AtlasOfOrders/Map_of_Myth.py`, `Map_of_Phrasings.py` | Six beats and a hook; nested vocabulary; gated rows. |
| **Relationships** | `AtlasOfOrders/Map_of_Relationships.py` | ⚠️ **Lost in the wipe.** Seven names (`MEANS`, `RESTRAINT`, `MASK`, `DEBT`, `WOUND`, `THRESHOLD`, `REVELATION`) bound to `None`; only the docstring survives. Nothing imports it. Drafts in §8. |
| The door from the player path | `BackgroundKit.py` | ⚠️ **Gone.** QST-0061 describes an "Order Cultist" background; the current roster of 46 has no Order background. `Grimoire_of_Characters` still calls `Resolve_Order_Features`, but no player Character is ever Sworn. The engine is orphaned from the product. |
| Renderer | `AtlasEpica/Charts_of_The_Monomyth.py` | Present; shared with the Stories. |
| Design record | `Curia/Questae/Working/QST-0048-NOTES-first-slice.md`; `Documenta/Questae/Open/QST-0061` | The architecture change ("the Order precedes the Character"), the measurements (400 rolls, 397 names, zero defects), the five-entry complaint. |

---

## 🔎 2. What an Order is

**It precedes the Character.** *"It is a thing already standing in the world
when someone knocks on its door, so it owns its own dice and picks its own
nature; a Character then joins one."* With no Order supplied, `Swear` collapses
one from the Character's own seed, so the same Character always finds the same
door and two Characters never share one.

**The collapse**, each step narrowing the next and none forbidding anything:

1. **Tradition**: Arcane, Divine or Primal. Decides places, practices, the
   organization's word, the devotion, and a safe spell pool.
2. **Two Domains**, unordered. "Tagged, not ranked": some come to Hera for
   vengeance and some for the safety of the house.
3. **One Facet per Domain**: a creed and a goal.
4. **Organization**: Temple, Academy, Circle, Brotherhood, House…; "the word
   then governs the prose."
5. **Devotion**: a god with two faces, a theorem that turned out to be a door,
   a river with opinions.
6. **Name**: *organization* of the *descriptor* *core*, crossing the two
   Domains on purpose ("the Salt Anvil" rather than a label restating one).
7. **Relic, Perk, Sacrifice, Goal.**
8. **Feat**: *Sign of the …*, an Origin feat with an intuition die (a d4 on
   two named checks), a signature cantrip and always-prepared spell, and the
   Order's levelled spell list.

**Nothing is forbidden.** *"A Mercy order whose goal is a killing is a
surgeon's order that has decided what the tumour is, and it is better than a
safe one. The generator states the pair and stops; the reader supplies the
reason, faster and better than any template could."* This is the Death of the
Author principle applied to institutions, and it is the same law as the
loaded-names rule.

---

## 🔎 3. The twelve Domains

Mythic spheres, never job descriptions: "Hospitality is a trade; Home is a
domain, and every pantheon keeps one." Each turns four faces.

| Domain (mark) | Its four faces | The god behind it | The classes that call it home |
|---|---|---|---|
| **the Forge** (Making) | the Maker, the Unmaker, the Fire Thief, the Price | Hephaestus, Ptah, Goibniu, Prometheus | Artificer (the Price *is* Soul of Artifice); Arcane Trickster (the Fire Thief is Spell Thief) |
| **Home** (Hospitality) | the Hearth, the Salt Debt, the Closing Door, the Last Comfort | Hestia, Hera | Cleric (Life); the Halfling's valley; the Servant background's masters, inverted |
| **the Hunt** (Finding) | the Long Pursuit, the Debt Collector, What Should Stay Lost, the Provider | Artemis, Herne | **Ranger** (the creed "everything that runs leaves a line behind it" is the class); Barbarian Wild Heart |
| **Mercy** (Healing) | the Open Hand, the Clean Cut, the Long Vigil, the Plague-Bearer | Asclepius, Guanyin | Monk (Mercy), Cleric (Life); the Inquisitor's left hand is the Clean Cut |
| **the Veil** (Shadow) | the Kind Lie, the Watcher, the Second Face, the Night Itself | Hermes, Nyx | **Rogue** (the chalk mark low on walls is Thieves' Cant); Monk (Shadow); Gloom Stalker |
| **the Road** (Passage) | the Crossing, the Messenger, the Return, the Threshold Keeper | Hermes, Legba, Janus | Vagabond, Stranger, Herald; the Fey Wanderer |
| **the Word** (Scribing) | the Record, the True Name, the Sealed Page, the Last Speaker | Thoth, Seshat | **Wizard** (the argument against forgetting), Bard (Lore), Stranger (the Last Speaker) |
| **the Storm** (Storm) | the Breaker, the Weather Eye, the Wrath, the Calm After | Zeus, Thor, Tlaloc | Barbarian (the Orc's and Goliath's), Druid (Sea), Tempest by any name |
| **the Shield** (Sentinel) | the Body Between, the Last Rank, the Oathkeeper, the Sheathed | Athena Promachos | **Paladin**, Fighter (Banneret), Guardian; the Sheathed is the Rogue as bodyguard |
| **the Wall** (Warding) | the Boundary, the Vault, the Locksmith, What Is Kept Out | Janus, Terminus | Abjurer; the Dwarves' Bank Templars; the Thief ("you cannot build a door worth trusting until you have opened every kind") |
| **the Eye** (Detection) | the Open Eye, the Sifter, the Cost of Seeing, the Unwatched | Argus, Odin's eye | Investigator, Diviner, Inquisitor; "whoever is doing the watching should also be watched" |
| **the Beast** (Handling) | the Kinship, the Yoke, the Wild Left In, the Shepherd | Pan, Cernunnos | Druid, Beast Master, Wildkeeper; "they are not lesser, they are earlier" |

Twelve domains give sixty-six pairings. The Aberrant Dragonmark is deliberately
absent: the uncontrolled-power archetype is already the Arcane Mutant.

---

## 🔎 4. The three Traditions

*"An Order of the Veil may be Arcane, Divine, or Primal for entirely different
reasons: one keeps a laboratory, one keeps a calendar of rites, one keeps a
grove. The magic barely changes; the world around it changes completely."*

| | Arcane | Divine | Primal |
|---|---|---|---|
| A place | a workshop above a shop that sells something else entirely | a back room behind a public shrine, reached through the kitchen | a stand of trees older than the field around it and never cleared |
| A practice | everything is written down twice and one copy is destroyed | confession to one other member, never to a superior | nothing is written; it is walked, and shown, and walked again |
| An organization | Academy, Cabal, Athenaeum, Conservatory, Society, Institute | Temple, Order, Choir, Congregation, Sanctum, Fellowship | Circle, Grove, Kinship, Lodge, Brotherhood, Covenant |
| A devotion | a theorem that turned out to be a door | a saint the church struck from its own rolls | a beast that is always described the same way by people who have never met |

**The devotions are the setting's peoples in disguise.** *A saint the church
struck from its own rolls* is a Dwarven Saint. *An angel that has not been seen
since the founding and is still expected* is a Celestial. *The honored dead, who
are consulted and occasionally answer* is a Grave Cleric's whole faith. *A beast
that is always described the same way by people who have never met* is a
dragon, and the Ascendant Dragon monks' slot (Dragonborn page). *The land
itself, which is owed and does the owing* is the Druid's theology seat. *A
river with opinions, and a long memory for insults* is the Basque Mari. The
Traditions never name them, which is correct, and the design team should know
that they are there.

---

## 🔎 5. The prose: an arc, not a bag

The description is six beats, each written to arrive after the one before:
**Before** (who you were and what was missing), **Contact** ("Then…"),
**Noticing** ("You noticed early that…"), **Teaching** (the two spheres and
their creeds), **Unease** ("That is not the only strange thing"), **Belonging**
("But…"). A second layer of vocabulary fills words inside the beats and stays
fixed within a beat. Rows are gated on the Order's Tradition and Domains, so a
Forge house "smells of heat and iron without using the word".

Three collapsed Orders, unedited:

> **House of the Ninth Quarry** (Divine; the Word and the Hunt). *Before them you
> were good at reading what was not meant for you and useful to no one in
> particular, and you had stopped calling that unusual. You can name the day. A
> door you had walked past for years stood open, and the person inside was
> expecting you… You are not a fool. You have met four people who left, and all
> four have prospered, and not one will speak of it. You have written it down
> somewhere they will not look. But when you are ill, somebody notices on the
> first day.*

> **Fellowship of the Patient Hammer** (Divine; the Hunt and the Forge; the
> Provider and the Price). *They came to you at a funeral, which you later
> understood was not a coincidence. Every one of them can make something with
> their hands, whatever else they do… One room is kept locked, and it is not the
> archive.*

> **House of the Unspoken Snare** (Divine; the Hunt and the Word). *Nobody ever
> states a rule here. You are simply corrected, kindly, until you no longer need
> correcting.*

✅ This is the backgrounds' voice, generated: concrete, unsentimental, the odd
detail before the doctrine, the doubt before the belonging. The Orders are the
proof that the project's register can be *collapsed* rather than only written,
which is what the whole generator is for.

**The hook** is one bargain: perk, sacrifice, goal. *"You can pick up a cold
trail that professionals abandoned, given a day and something they touched,
which is the part people envy. What they do not see is the other clause: you
are trusted with a passage you are forbidden to read. You carry it because
something older than you needs doing: restore a record that somebody spent a
fortune erasing."*

---

## 🔎 6. What is wrong (QST-0061, confirmed)

1. **The door is gone.** No player background reaches the engine. The Orders
   are the setting's middle layer and no generated Character belongs to one.
2. **The template shows.** Two of three sampled hooks opened *"Ask what
   membership is worth… Ask what it costs… Ask what it is all for"*: four hook
   forms is too few, and the "Ask" form is the most recognisable. the project's
   complaint ("they all sound off") is this.
3. **The Teaching beat confesses its own seam.** *"Nobody has ever presented
   these as a contradiction. Behind them stands…"* appears in every sampled
   description because the **Relationships** layer that was meant to say *how*
   the two creeds speak to each other is lost. The seam is the missing file.
4. **Five entries for one Order** (Background, Background Hook, Secret Order,
   Order Hook, Sign feat), two sharing a title. QST-0061 says the count is a
   design decision needing a Dialog; this page recommends **three**: one
   paragraph (the arc), one bargain (the hook, folded under the Order's name as
   its second paragraph), one feat (the Sign, which "reads cleanly and is the
   one entry that earns its place").
5. **Fourth wall**: the old Background text described the generator ("are
   collapsed the moment you are rolled"). With the background gone, so is the
   sentence; whatever replaces it must not describe the machine.
6. **Person drift and clause-length fillers**: structural until slots declare
   what shape of filler they accept (QST-0048.2, the Atlas of Vocabulary).
7. **Small sample, one Tradition.** Three seeds drew Divine three times and the
   Hunt three times. QST-0048 measured 400 rolls with good spread; worth a
   re-measure after the wipe, not a conclusion.

---

## 🔎 7. The Orders inside the setting

**The middle layer.** A species gives the spark; a class gives the fire; the
Order is the house. The Aasimar's temples and academies are Orders; the Tiefling's
house ("children in that house are nobody's, and they are ours") is an Order
with no sign cut into the lintel; the Dwarves' Bank Templars are an Order of
the Wall and the Vault; the Humans *build* Orders ("institutions and orders part
of our legacy"); the Monk's school is a jianghu sect, which is an Order with a
Primal or Arcane practice; the Warlock's patron can be an Order's devotion seen
from two distances ("somebody has been paying for all of this since before the
current members were born").

**The Orders are where the culture keys have not yet reached.** Places,
practices and organizations are written culture-free ("a workshop above a shop
that sells something else entirely"), which is why they collapse cleanly for
any people. The setting's wells for the secret society are rich and keyed:

- `iberia`: the **cofradía** (the Spanish word for exactly this: a religious
  brotherhood with rites, a house and a debt), the **Santa Hermandad** (the
  medieval brotherhood that policed the roads: an Order of the Road and the
  Shield), the **Mesta** (the shepherds' council: the Beast).
- `vatican` / `crusader`: the Templars and Hospitallers (the Shield and Mercy),
  the Beguines (Home).
- `athens`: the Pythagoreans ("nobody is admitted who cannot demonstrate the
  work"), the Eleusinian mysteries (the Veil's "what is done in the dark is done
  honestly").
- `china`: the Tiandihui, the jianghu's real secret society (the Road, the
  Veil); `japan`: the yamabushi, the mountain ascetics (Primal, the Storm).
- `levante` / `maghreb`: the Sufi tariqa (Divine, Mercy); Alamut (the Veil's
  Second Face).
- `egypt`: the House of Life (the Word). `rome`: the collegia (the Forge).

None of these need to be named; they say which pools a culture-flavoured Order
could draw from if the Orders ever take a key.

---

## 🚧 8. Relationships: the lost layer, redrafted

The docstring survives: *"No pair is forbidden. A Relationship does not add
another subject to the Order; it decides how the two selected Domain truths
speak to one another. Each form accepts complete creed sentences, so the prose
never places a long clause into a slot written for a noun phrase."*

Seven names survive with no text. **Drafts**, each taking `{creed_a}` and
`{creed_b}` as full sentences, to replace *"Nobody has ever presented these as a
contradiction"* in the Teaching beat. Proposals.

| Form | Draft |
|---|---|
| **MEANS** | *{creed_a} That is the end. {creed_b} That is how you get there, and the house does not let you forget which is which.* |
| **RESTRAINT** | *{creed_a} {creed_b} The second is there to stop the first from becoming everything. It has not always managed.* |
| **MASK** | *To the town, {creed_a} Inside the walls, {creed_b} The house wears the first so that it can keep the second.* |
| **DEBT** | *{creed_a} Because of that, {creed_b} The one was owed before the other could be taught, and the house is still paying.* |
| **WOUND** | *{creed_a} The house learned that the hard way, and it learned the second thing from the scar: {creed_b}* |
| **THRESHOLD** | *{creed_a} That is the door. {creed_b} That is what waits on the other side of it, and nobody is told which side they are standing on.* |
| **REVELATION** | *{creed_a} You were taught that first, and believed it. Then, one night: {creed_b} You have not decided whether the first was a lie or a ladder.* |

With a Relationship drawn per Order, the Teaching beat gains the one thing the
sampled descriptions lack: a reason the two creeds are in one house.

---

## 🔒 9. Decisions log

**Decided (via QST-0048)**

- The Order precedes the Character and owns its dice.
- Domains are mythic, tagged not ranked, and turn several faces. Tradition is
  an independent axis.
- Nothing is forbidden; the reader supplies the reason.

**Open (needs a Dialog, per QST-0061)**

- **The door.** Restore a player background that Swears the Character to an
  Order, under a name that is not "Order Cultist" and does not describe the
  generator (candidates: *Initiate*, *Sworn*, *the House*), with three entries.
- **The hook forms.** Seven exist; the "Ask" form should be one of many, not
  one in two.
- **The Relationships** (§8).
- **Culture-keyed Orders** (§7): whether places, practices and organizations
  should ever take the Character's markers.

**Repairs**

- `Map_of_Relationships.py` is a file of `None`s; either restore it (§8) or
  delete it until it is restored, so nothing imports a tuple of nothing.
- Re-measure distribution after the wipe (§6.7).

---

## 🧾 10. Pointers

- **Ranger, Rogue, Artificer, Wizard pages**: the Domains as the classes' guilds.
- **Dragonborn page**: the Ascendant Dragon as a Primal devotion.
- **Aasimar, Tiefling, Human pages**: the Orders as the middle layer.
- **Monk page**: the jianghu.
- **Warlock page**: the Order as a patron's front.
- **QST-0048.2** (the Atlas of Vocabulary): where the filler-shape problem
  belongs.
