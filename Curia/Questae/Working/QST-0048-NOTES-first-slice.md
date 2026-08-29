# QST-0048 — build notes, first slice

*Written while Julio was away. Everything here is a record, not a decision: the
questions at the bottom are the ones that need him.*

---

## What was built

| File | Holds |
|---|---|
| `AtlasLusoris/OrderKit.py` | the `Order` object, the `Sworn` Tag family, `Swear()`, the minted per-Order feat, self-test |
| `AtlasLusoris/AtlasOfOrders/Grimoire_of_Orders.py` | the three records: `Facet`, `Domain`, `Tradition` |
| `AtlasLusoris/AtlasOfOrders/Map_of_Domains.py` | **12 domains**, one per published Dragonmark |
| `AtlasLusoris/AtlasOfOrders/Map_of_Traditions.py` | Arcane · Divine · Primal |
| `AtlasLusoris/AtlasOfOrders/Map_of_Phrasings.py` | the sentence pools the prose collapses out of |

Run it: `.venv/bin/python3 -m AtlasLusoris.OrderKit` → `OK — OrderKit self-test`

Read output:

```python
from AtlasLusoris.OrderKit import Order
print(Order(seed=250).description)
```

## The architecture change he called mid-build

**The Order precedes the Character**, so it owns its own dice. `Order(seed=…)`
collapses itself with `order.Pick` / `order.Sample`; a Character then *joins*
one via `Swear(char, order)`. With no Order supplied, `Swear` collapses one
from the Character's own seed, so the same Character always finds the same
door — and two Characters never share an Order.

## All twelve marks are reachable

Every published mark has a mythic domain, so the dice can still produce the
classics:

| Mark | Domain | Mark | Domain |
|---|---|---|---|
| Making | the Forge | Sentinel | the Shield |
| Hospitality | Home | Warding | the Wall |
| Finding | the Hunt | Detection | the Eye |
| Healing | Mercy | Handling | the Beast |
| Shadow | the Veil | Passage | the Road |
| Scribing | the Word | Storm | the Storm |

12 domains → **66 pairings**. Aberrant Dragonmark is deliberately absent: the
uncontrolled-power archetype is already the **Arcane Mutant** background.

## Measured

- 400 rolls → **397 distinct names**, zero prose defects (no unfilled slots, no
  doubled articles, no double spaces)
- Reproducible: same seed → identical name, description, hook, and feat
- BackgroundKit (86), FeatKit, GuildKit all still green — nothing was touched

## Bugs found by reading output, and fixed

1. Slots landing at a sentence head stayed lowercase → capitalise the line
   start *and* anything after a full stop
2. `"a {relic}"` where relics already began with an article → doubled "a a"
3. The same `{place}` used twice in one description
4. Two domains merged gave five spells at one level, out-granting the marks we
   patterned on → thinned to two per level
5. Six domains ended on *Scrying*, four on *Creation* → each of the twelve now
   has its own capstone (Hallow, Passwall, Commune, Awaken, Wall of Force…)
6. Tradition practices mixed clauses and noun phrases, so
   *"learn quickly that confession to one other member"* → all clauses now

## Second pass — the prose became a story

Julio's read of the first output: the sentences were true but *disconnected*,
a list rather than a narrative. Rebuilt on three changes.

**1. A story arc, not a bag of pools.** `DESCRIPTION_ARC` is six beats, each
written to arrive after the one before:

| Beat | Does |
|---|---|
| BEFORE | who you were, and what was missing |
| CONTACT | how they reached you ("Then …") |
| NOTICING | the first odd thing ("You noticed early that …") |
| TEACHING | the two spheres and their creeds |
| UNEASE | the second odd thing ("That is not the only …") |
| BELONGING | why you stayed ("But …") |

The emotional movement is lack → contact → curiosity → transformation →
doubt → belonging, so the paragraph now has somewhere to go.

**2. Nested vocabulary.** A second collapse layer inside the beats: pools for
`{good_feeling}`, `{unease}`, `{former_state}`, `{odd_detail}`,
`{unease_detail}`, `{belonging}`, `{kin}`, `{reaction}`, `{contact_event}`.
Values may themselves carry slots (`{belonging}` can mention `{house}`), and
`_Vocabulary.__missing__` keeps resolving until nothing is in braces. A key
drawn inside one beat stays fixed for that beat, and is redrawn for the next,
so a sentence never contradicts itself while the paragraph still varies.

**3. One hook instead of four announcements.** `HOOK_FORMS` carries the pro,
the con, and the purpose in a single flowing statement. The hook fell from
about 110 words to **64**, and reads as a bargain rather than a contract.

Measured after the rebuild: 400 rolls, **zero prose defects**, **400 distinct
hooks**, descriptions averaging 255 words.

Two grammar breaks that only appeared once vocabulary nested, both fixed:
templates ending in `"… and no expectation of getting any"` and
`"you feel {good_feeling} that you are …"` assumed a short noun phrase and
broke when a long clause landed there.

## Third pass — reading four aloud, and what it caught

Generated a batch and read it critically. Every defect below was invisible in
the code and obvious in the prose, which is the argument for always reading
output rather than trusting the pools.

**Grammar breaks, all caused by a long value landing in a tight slot:**

| Broke as | Because |
|---|---|
| "…a beast described the same way by people who have never met, **which is spoken of rarely**" | a relative clause hung on `{devotion}` attaches to the wrong noun |
| "because **whoever was awake** clearly never needed them to" | not every `{kin}` value works as a sentence subject |
| "There is a room at **a temple with one altar nobody is allowed to tend** that is kept locked" | a long `{place}` embedded mid-sentence garden-paths |
| "…for as long as **you may not be photographed**" | sacrifices are declarative clauses, not conditions |
| "None of that changes what **the work is real, and it is yours** means" | `{belonging}` is a clause, not a noun phrase |
| "That is worth **a doubt you never said out loud** at three in the morning" | several `{unease}` values already carry their own hour |
| "**There, there is** an examination" | `{practice}` may itself begin with "there is" |
| "…where no river **is is** older than…" | a relic ending in "is" met a template starting with "is" |

**Dead weight found by repetition:** *"That is the whole of what there is to
say about it"* appeared in three of four — and worse, it **closes the
paragraph in the opening beat**, which fights the arc. Removed. Same for
*"and that nobody had thought to warn you."*

**Pools were too shallow.** Five entries in a slot drawn every single time
reads as a template within three examples. `contact_event` went 6 → 11,
`odd_detail` 6 → 11, `former_state` 6 → 9, `belonging` 5 → 8, and the beat
pools grew similarly.

Those findings are now written at the top of `Map_of_Phrasings.py` as four
writing rules, so the next person adding a pool does not rediscover them.

**Measured after the third pass:** 1000 orders, **zero defects** (no unfilled
slots, no stutters, no doubled articles); 300 seeds → **300 distinct
descriptions**.

## Open questions (need Julio)

1. **How does an Order reach a Background?** `Build_Background` takes a single
   static `ORIGIN_FEAT` class, but an Order mints its feat per Character. So
   the Order background cannot be declared the way the other 86 are without
   either (a) allowing a callable/deferred feat, or (b) leaving Orders outside
   the Background system and attaching them separately. **Nothing was wired
   into `Map_of_Eberron_Backgrounds.py`** — the 12 heirs are untouched, as
   agreed.
2. **Does an Order pick its own Perk/Sacrifice, or does the Character?** Right
   now the Order carries one of each, which is why two Characters in the same
   Order (should that ever be allowed) would owe the same price.
3. **Should Tradition weight the Domain pick?** It does not today — a Primal
   Order of the Forge is as likely as a Primal Order of the Beast. That is
   arguably correct ("no exclusion lists"), but it is a live choice.
4. **Greater Orders?** The published set has 14 Greater Marks at level 4+. The
   general-feat gate already exists (`requires_feat_any`, built for Field
   Marshal), so a second tier is cheap whenever wanted.
5. **How many spells per level is right?** Currently capped at 2, matching the
   marks. Two domains can offer five, so the cap is doing real work.

## Deliberately not done

- No Background record was created or deleted
- `Map_of_Magic.py` was not refactored (that is QST-0048.1)
- `Map_of_Titles.py` was not split (QST-0048.2); the name vocabulary lives in
  the domains themselves for now, as `descriptors` and `cores`
