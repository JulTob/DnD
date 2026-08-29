# Quest: Starting Equipment Generator

**Status:** planned · **Scope:** AtlasInventarium, GearKit (new), pipeline order, masteries, AC, NPC unification
**Audit:** 7-agent parallel subsystem audit, 2026-07-29 (inventory/bag, money, weapons/masteries, class gear/AC, sheet rendering, uniqueness hooks, NPC path). All findings cross-confirmed.

---

## 1. Verdict

The equipment layer is pre-TOP legacy with the same disease Backgrounds and Divine Order had:
string-matched `if/elif` chains, choices sampled from global `random`, mechanics described but
never instantiated, and multiple parallel implementations of the same fact. It is **not patchable**
— it gets the proven treatment: **records → Kit → Tags**, one construction point, seeded streams,
forks resolved not suggested.

---

## 2. Bug Ledger (from the audit — file:line verified)

### Money
- **Budget rolled twice, second wipes the first.** `calculate_budget` ends with `self.purse = base`
  (assignment) and runs from both `GenerateEquipment` (`Grimoire_of_Characters.py:147`) and
  `set_Objects` (`:77` → `Grimoire_of_Objects.py:11`). Displayed gold is a fresh roll disconnected
  from all purchases. This is the double "Base budget" print.
- **Every weapon paid twice**: picker factories deduct purse internally (`Grimoire_of_Objects.py:799,
  905, 1017, 1124`) and `buy_item` deducts again (`:504-508`).
- `buy_item` strict `>` silently drops unaffordable/exact-price items — bag contents look arbitrary.
- Artificer has no class-budget branch → base 0 gold (`:590-613`).
- Level roll `Dice(N=lvl-1, D=40)` clamps N<1→1, so level 1 still gets +1d40 (`:615` +
  `Map_of_Dice.py:31`).
- Background gold table is string-matched; all 71 renamed backgrounds fall to `else Dice(10,5)`
  (`:617-650`).

### Records corrupted at the root
- **Value/weight transposed on every Weapon and Armor**: `super().__init__(name, weight, value, …)`
  vs `Object(name, value, weight, …)` (`Grimoire_of_Objects.py:404` and `:444`). Chain Mail costs
  55, weighs 75. Corrupts purse math, encumbrance, and the sheet repr.

### AC
- Base AC computed from default all-10 stats **before** the real roll
  (`Grimoire_of_Characters.py:107` vs `:73-77`) — Wizard/Sorcerer ship flat AC 10, never 10+DEX.
- Shield branch adds +2 **unconditionally per `set_Armor` call**, and `set_Armor` runs twice
  (`Grimoire_of_Objects.py:343-346`, called at `:245` and `:230`) → **+4**.
- Ranged weapon is equipped into the **left hand replacing the shield while its +2 stays in AC**
  (`:262` vs `:347-351`).
- **Unarmored Defense exists three times**: description-only TOP tags
  (`Map_of_Monk_Training.py:272`, `Map_of_Barbarian_Training.py:299`, `apply=None`);
  a dead feat that would crash (`Grimoire_of_Features/__init__.py:212-234` calls
  `get_worn_armor()`/`is_wearing_shield()` — don't exist on Inventory); and the live skill-flag
  hack in `set_Armor` (`:325-337`) doing mismatched comparisons (armor-without-shield vs
  UD-with-stacked-shield).
- Guild armor tags (`Unarmored/LightlyArmored/ModeratelyArmored/HeavilyArmored`,
  `GuildKit.py:199-235`) are stamped but **never queried** by any equipment/AC code.
- Clothes fallback equips an item whose own AC (10+DEX) contradicts sheet AC 10 (`:339-341`).

### Weapons & masteries
- **`Melee_Martial`/`Ranged_Martial` are verbatim copies of the Simple lists**
  (`:908-1018`, `:1020-1125`) — no PC can ever own a martial weapon.
- Masteries sample the **full 37-weapon catalogue** with stdlib `random`, no
  proficiency/ownership/class-restriction filter (`Map_of_Weapon_Masteries.py:130-150`);
  `char.weapon_mastery_picks` is written/read only inside that module.
- Fighter/Barbarian/Paladin/Rogue mastery trainings ship **"of your choice" prose**
  (`Map_of_Fighter_Training.py:200-209`, Barbarian `192-204/309-316`, Paladin `252-260`,
  Rogue `207-216`); only Ranger resolves (`Map_of_Ranger_Training.py:303-326`).
- Masteries resolve during `apply_class_features` (`Grimoire_of_Characters.py:132`) **before**
  equipment exists (`:147`) — the disconnect is structural.
- Bows/crossbows/sling built with `Mod=STR_mod` (`:765,777,789`). Mace named "Light Hammers"
  (`:852,:964`). `properties` concatenated without separators (`:454`).
- The only PHB-accurate per-class gear code, `apply_class_proficiencies`
  (`Codex_of_Progression.py:63`: Fighter chain mail, Wizard spellbook, Cleric mace+shield…),
  is **dead** — sole caller `SetFeatures` (`Grimoire_of_Characters.py:214-223`) is never invoked.
  Only Fighter/Wizard/Rogue/Cleric/Paladin have branches anyway, and only at `lvl==1` exactly.

### Bag & sheet
- Duplicate ranged weapon parked in `Inventory.equipped` — a list **no sheet renders**
  (`:264-272` + `:511-529`).
- Two identical shield blocks (`:274-278`, `:281-285`) — dead because left hand is occupied.
- Rope bought twice at different weights, Torch twice (`:299-318` vs `:307-313`).
- Weaver's Tools buys `tinker_Tools` — latent `NameError` if Weaver-but-not-Tinker proficient
  (`:153-158`).
- Description-only "magic items": Cloak of Protection changes no AC, Scroll of Fireball
  regardless of class (`:288-296`).
- Sheet: Melee/Ranged rows permanently "-" (slots never populated); Right/Left rows render
  **escaped raw HTML** (Weapon.__str__ returns an Entry, `safe_str` + Shiny escape it —
  `character_sheet.py:266-279`); Defense row shows debug `__repr__` with transposed numbers;
  fractional purse renders ("123.7 gp").
- `equip_left` refund bug: gates on `self.right`, refunds `self.left.value` — `AttributeError`
  when right set and left None (`:543-547`); crash then **eaten by `summon_player`'s 5-retry
  loop** (`Map_of_Character_Generation.py:165-183`), which silently re-rolls the seed —
  hides bugs and breaks determinism.

### NPCs
- **No inventory at all** (zero Inventory refs in AtlasActorLudi). AC is synthetic dice-rolled
  modifiers (`Grimoire_of_NPC.py:432-477`), attacks come from a **second, incompatible Weapon
  class** (`Grimoire_of_Weapons.py`) via `Lodge_of_Basic_Weapons`.
- Archetype weapon-flavor lists in `AtlasPugna/Map_of_Attacks.py:28-32` are **initialized empty
  and never filled** — guild identity contributes nothing to NPC weapons; races dominate.
- `npc.abilities` returns tactical Abilities, not ability scores (collides with PC `.abilities`
  → `char.AS`) — blocks naive reuse (`Grimoire_of_NPC.py:273-276`).
- NPC guild helper tags (`MartialArms`, `HeavilyArmored`…) are stamped but never bridged to
  proficiency flags.

### Dead weight (delete or rewrite)
- `Ledger_of_Weapons.py` — imports nonexistent `AtlasOfForge`; broken + orphaned.
- `Ledger_of_Armors.py` — imports nonexistent module, undefined names; broken + orphaned.
- `gear_gen.py` — orphan, `print`s at import, space-indented.
- `items.py` — orphan, imports nonexistent `dnd`.
- `Compass_of_Recharging.py:17` — module-level `random.choice` consumes seeded RNG at import.
- `choose_melee_weapon` (`:1146-1291`) — dead; duplicate entries; invalid mastery names
  ("Swords", "Axes"); Longsword twice with different damage.
- `Grimoire_of_Characters.SetFeatures` (`:214-223`) — never called.
- `NonPlayer.set_stats` (`Grimoire_of_NPC.py:286-303`) — dead, would crash on properties.
- Background `EQUIPMENT` Report (`BackgroundKit.py:828`) — stamped on all 87 tags, read by nothing.
- No equipment tests anywhere (no `tests/`; nothing in `scripts/`; BackgroundKit self-test
  skips EQUIPMENT).

---

## 3. Target Architecture — `GearKit` (superseded design, kept for record — see §3.0)

### 3.0 Revision (2026-07-29): generic `Item` + Tags, not typed Armor/Weapon classes

User redesign, now the live plan — implemented and self-tested in
`AtlasInventarium/Grimoire_of_Items.py`:

- **One generic `Item`**: name, price, weight, description. No `Armor`/`Weapon` subclasses.
  `Build_Armour`/`Build_Weapon`/`Build_Shield`/`Build_Item` are the single construction
  points; Tags (`Armour`, `Weapon`, `Shield`, `Wearable`/`Wieldable`, `Simple`/`Martial`,
  `Melee`/`Ranged`, `Magical`) craft meaning onto it — the same records→Tags shape as
  Backgrounds/Trainings.
- **`Equipped` is a Tag, not a slot pointer.** Ownership is a plain list on the character
  (`char.belongings`); "in use" is Field membership. This makes "two armours are equipped
  at once" an ASKABLE question (`equipped(char, Armour)`) with a real ANSWER
  (`reconcile()`: keep the better piece, sell the rest, refund the purse) — not a slot
  overwrite that silently loses the previous item (the Quest 0 bug this replaces).
- **Artifact grants are summed at read time, never written.** `Item.grants` is a plain
  dict (`{"AC": 1, "saves": 1}`); `armour_class()`/`grant_total()` sum over everything
  currently `Equipped`. Unequip/sell an artifact and its contribution disappears on its
  own — nothing to overwrite, nothing to desync. This is also how the natural formulas
  (Unarmored Defense, base 10+DEX) stay untouched: they are passed in as `unarmoured=`,
  and the derived AC is `max(natural, worn) + shields + grants`.
- **TagKit gotcha recorded**: un-applying a Tag is `Tag.Rip(agent)`, not `.remove()`
  (verified against `TagKit.py:1984`; `unequip()` uses `Equipped.Rip(item)`).

Self-test (`python -m AtlasInventarium.Grimoire_of_Items`) proves: Tag crafting +
membership gates; heavy armor ignoring DEX; shields stacking; Unarmored Defense beating
weak armor via `max()` with no special-casing; artifact grant added then cleanly removed
on unequip; double-armour reconciled (sold, refunded, single winner kept); bag vs
equipped separation; purchase respecting the purse.

Everything in §3.1–3.6 below describes the OLD `Outfit`/`Inventory` design from before
this revision. It is being superseded incrementally — read it for the POLICY layer
(budget, loadout algorithm, pipeline order, NPC deferral) which still applies; the DATA
layer (typed Armor/Weapon classes, slot attributes) is replaced by Grimoire_of_Items.

### Quest 1 — Ledgers on the new Item system ✅ DONE (2026-07-29)

`AtlasInventarium/Ledger_of_Weapons.py`, `Ledger_of_Armors.py`, `Ledger_of_Gear.py` —
full PHB 2024 catalogues, each built entirely with `Build_Weapon`/`Build_Armour`/
`Build_Shield`/`Build_Item` (no direct `Item(...)` construction outside the builders).
Each has a `python -m` self-test; all four modules (including `Grimoire_of_Items`) pass;
`app.main` still imports clean. These ledgers were dead/orphaned files before this quest
(broken imports, `AtlasOfForge` that doesn't exist) — this is purely additive, nothing
regressed.

- **Weapons** (38 + 2 firearms): all 10 Simple Melee, 4 Simple Ranged, 18 Martial Melee,
  4 Martial Ranged from the 2024 PHB core table, mastery-consistent with the existing
  `Map_of_Weapon_Masteries.WEAPON_MASTERIES` dict (every mastery name cross-checked).
  Musket/Pistol tagged `Firearm` (a `Weapon` subtype) rather than plain `Weapon` —
  fixes the audit's exact complaint that Martial proficiency alone let a Ranger
  "master" a gun. Self-test asserts: no duplicate names, every weapon has a mastery,
  every weapon is exactly one of Simple/Martial and exactly one of Melee/Ranged.
- **Armor** (12 + Shield): 3 Light / 5 Medium / 4 Heavy, AC climbing within each tier,
  `dex_cap` correctly None/2/0 per tier, `str_requirement` recorded for Chain Mail(13)/
  Splint(15)/Plate(15) (enforcement is a later quest — Quest 2/3 territory).
- **Gear**: 17 Artisan's Tools at the 2024 PHB's unified 50 gp (a real, confident rules
  fact — 2014 varied 1-50 gp per tool; weights carried over from the project's prior
  values, flagged as not re-verified line-by-line, so anyone who spots a wrong one has
  a one-line fix); 7 other tool proficiencies (Thieves' Tools, Disguise Kit, …); 8
  adventuring gear staples; **one** fully-specified pack (Explorer's Pack — contents,
  weight summed from real component weights, price validated ≤ loose total). The other
  six PHB packs (Burglar's, Diplomat's, Dungeoneer's, Entertainer's, Priest's,
  Scholar's) were deliberately NOT guessed at — their contents differ in ways I wasn't
  confident reproducing from memory; flagged here as the explicit next slice rather
  than silently shipped wrong.

**TagKit lesson confirmed while building this:** subtype Tags compose with `isinstance`-
style membership — `Firearm(item)` alone makes `item in Weapon` true (`Firearm(Weapon)`
subclassing is enough; no need to also stamp `Weapon` by hand).

Not yet done (next slices): wiring `GearKit`/`Outfit` to actually issue these Ledger
items to characters (still on the old `Grimoire_of_Objects.GenerateEquipment` path from
Quest 0); deriving `Map_of_Weapon_Masteries.WEAPON_MASTERIES` FROM the weapon ledger
instead of keeping the parallel dict (both are consistent today, but only because they
were hand-checked against each other — a real fix removes the duplication); enforcing
`str_requirement`/`stealth_disadvantage`.

### Slots, Wonders, and Crafts ✅ DONE (2026-07-30)

**Body slots.** `Armour` is now the "Wearing" slot, joined by `Headwear`, `Footwear`,
`Cloak`, `Handwear`, `Jewelry`. `reconcile()` generalised from a hardcoded
Armour/Shield pair to a `SLOTS` capacity table — one hat, one cloak, but **three**
jewelry (rings + amulet coexist). Over-capacity slots keep the best piece by
`_worth()` (protection → granted magnitude → price) and sell the rest.
Sheet label renamed **Defense → Wearing** ([character_sheet.py:35](app/components/character_sheet.py:35));
the finer slots are deliberately NOT added to the sheet table yet — the live sheet
still reads the legacy `Inventory`, which has no such attributes, so they would render
as permanent "-" rows.

**Copper flooring.** `copper(gold)` floors to 1/100 gold (`math.floor(g*100)/100`) —
always down, so float crumbs never invent a coin. Applied in `buy`, `sell`, and the
final purse.

**Consumables stack.** New `Consumable` Tag (potions, scrolls, oil, rations) — exempt
from the one-of-a-kind slot rule and from name-uniqueness checks. Carrying four Potions
of Healing is the point, not a duplication bug.

**`Ledger_of_Wonders`** — 9 worn wonders (Cloak of Protection, Ring of Protection,
Bracers of Defense, Boots of Striding, Amulet of Health, Circlet of Insight, Brooch of
Shielding, Goggles of Night, Gauntlets of Might), 1 carried (Bag of Holding — **not** a
body slot; it briefly occupied Jewelry, which was wrong and is now asserted against),
6 consumables. Gated by `WONDER_TIERS` at levels 1/5/11/17. **Honesty rule enforced by
the self-test**: an item whose effect is not yet mechanised (Bag of Holding's capacity,
Goggles' darkvision, Gauntlets' STR override) carries NO `grants` and must say
"not yet" in its description — an unimplemented effect must never masquerade as a
number on the sheet.

**`Grimoire_of_Crafts`** — the personalisation layer, and the payoff of the grants
design. A Craft is a *property*, not an item: "of Defense" is `grants={"AC": 1}` stamped
as a Tag onto whatever carries it. Because grants are already summed at read time, a
crafted item needs **zero** new plumbing.
- `Build_Craft(name, grants, tier, affix, applies_to, requires, forbids)` — `applies_to`
  gates by item kind (a weapon-craft cannot land on boots), `requires`/`forbids` gate by
  the **Hero's own Tags**, `tier` (1/2/3/4 → levels 1/5/11/17) gates by depth.
- `forge(item, craft, hero)` merges grants **in plain code, deliberately, once** — NOT
  in an Imprint, because `instantiate()` re-stamps tags when cloning and an Imprint would
  silently double every bonus.
- 10 starting crafts: of Defense, Warding, Precision, Wounding, the Bear, Swiftness,
  Vigilance, the Aegis, Ruin, the Paragon.
- `GearKit._apply_crafts` spends a `level // 5` craft budget on the hero's own gear;
  `_fit_wonders` grants tier-appropriate marvels.

**Items have a `name` and an earned `title`** — the same split Characters already use
(`name` + `title`). Crafting does NOT rename a thing: a crafted Club is still a Club, it
has simply come to be called "Club of Wounding". `item.name` is identity and is never
rewritten (so catalogue lookups and the future mastery bridge keep working);
`item.title` is what this particular specimen earned; `item.called` returns the title
if there is one, else the name, and is what the sheet renders.
(First implemented backwards — decorating `name` and hiding identity in a `base_name` —
which my own GearKit invariant caught as "Wizard wields untrained Club of Wounding".
Author corrected the model: it should be a title, not a new name.)

Known wart: stacking several crafts concatenates suffixes
("Club of Wounding of Precision"). Fine mechanically, clumsy to read — a later pass
could title from the highest-tier craft only, or fuse them.

Verified end-to-end on a level-20 Paladin: `Splint of Defense` + `Cloak of Protection` +
`Greatsword of Ruin` + `Longbow of Ruin`, **AC 23 with magic → 15 with the granting items
removed** — proving grants are live, never written into the Character.

### GearKit is LIVE ✅ (2026-07-31) — the legacy path is retired

`Grimoire_of_Characters.set_char_features` now calls `Outfit_Player(char)` and exposes
`char.equipment = Loadout(char)`; the second pass (`char.set_Objects()` → `setObjects`,
which re-rolled the budget and clobbered the first pass) is **deleted**. Gear lives on
`char.belongings` as Tagged Items; `Loadout` is a pure derived view (stores nothing —
every slot is a Tag query at read time), and it implements the
`get_worn_armor()`/`is_wearing_shield()` API the Unarmored Defence feature had always
expected but that never existed.

**The Cloak of Protection finally counts** — the thing that motivated the whole quest.
Verified live on a generated Ranger: wearing `Studded Leather of Defense` +
`Cloak of Protection` → **AC 20; unequip the cloak → 19; re-equip → 20**, with `+1 saves`
derived alongside. On the legacy path the cloak was a description-only `Object` sitting
inert in the bag.

Sheet now renders the real slots (Wearing / Off-hand / Melee / Ranged / Head / Cloak /
Hands / Feet, plus repeating Jewelry rows), skipping empty ones instead of printing rows
of "-". Items state their mechanics via `Item.blurb()`: `AC 11 + Dex, Light armour`,
`AC 14 + Dex (max +2), Medium armour`, `2d6 Slashing, Heavy, Two-Handed. Mastery: Graze`,
and crafts/wonders append what they grant (`+3 AC, +2 saves`).

`scripts/verify_equipment.py` rewritten for the GearKit contract. It now gates things the
old shape could not express: AC **exactly equals** its derived ceiling
(best-of(worn, Unarmored Defence) + shield + grants) and `char.AC` agrees with it; slot
capacities; weapons restricted to the Guild's training with no firearms; armour within
armour training; Monks stay unarmoured; everything equipped is owned; consumables are
**exempt** from the duplicate check. 180 characters ALL GREEN.

**Bug the new gate caught — `copper()` was destroying coins.** `0.29 * 100` is
28.999999999999996 in binary floating point, so a bare `floor()` returned **0.28**.
Found because the gate flagged two purses, which on inspection were *correct* values and
a *float-naive assertion* — but chasing it exposed the real defect underneath. Fixed with
a 1e-6 epsilon in both `Grimoire_of_Items.copper()` and the legacy `Inventory.purse`
setter, verified exhaustively over 200,000 values (0 losses, genuine fractions still
floor: 12.999 → 12.99), and locked behind a self-test.

Also fixed while verifying in the running app: the Explorer's Pack was listed in the bag
*beside* its own unpacked contents (now the pack is opened and consumed).

Still legacy, still to retire: `Grimoire_of_Objects` (`Inventory`, `GenerateEquipment`,
`setObjects`, `set_Armor`, `choose_melee_weapon`) is now unreachable from the player
pipeline but still imported and still used by NPCs indirectly. Deleting it is a separate
cleanup. NPCs remain on their own path by explicit decision.

Open question for the author: Equipment-as-a-Chip. Recommendation is *no* for the item
list (a Chip is symbol·label·value; equipment is a multi-column table) but *yes* for its
scalars — Purse and Carried Weight would make good Chips. Not implemented pending a call.

---

## 3. Target Architecture — `GearKit`

Same proven shape as BackgroundKit / TrainingKit / Divine Order: **frozen records in Ledgers
(data) → one Kit as the single construction point (behavior) → TOP tags for membership →
`apply=` mutators that instantiate → callable descriptions resolved at awaken → per-character
seeded streams**.

```
AtlasInventarium/
  Ledger_of_Weapons.py   # REWRITE: PHB 2024 catalogue, frozen records:
                         #   name, category (Simple|Martial), reach (melee|ranged),
                         #   dmg (N, D, type), properties tuple (Light, Finesse, Two-Handed,
                         #   Versatile(d), Thrown(r), Ammunition(r), Loading, Heavy, Reach),
                         #   mastery, value, weight
  Ledger_of_Armors.py    # REWRITE: name, type (Light|Medium|Heavy|Shield), base_ac,
                         #   dex_cap, str_req, stealth_dis, value, weight
  Ledger_of_Gear.py      # NEW: packs (with contents), tools, consumables — records only
  GearKit.py             # NEW — the ONLY behavior module. Public surface: Outfit(char)
  Grimoire_of_Objects.py # Inventory survives (render contract), fixed + slimmed
```

**One catalogue, three consumers**: PC loadouts, NPC attacks (retiring the `Lodge` fork),
and `Map_of_Weapon_Masteries` (mastery lives ON the weapon record; the dict becomes a
derivation; `MASTERY_TEXT` stays). One fact, one owner — mastery↔equipment synergy becomes
structural, not a patch.

### 3.1 `Outfit(char)` — the single pass (one POLICY over shared primitives)

GearKit separates **primitives** (catalogue queries by category/property/tier, buy/equip,
`_resolve_ac`, mastery derivation) from **loadout policies**. `Outfit` below is the first
policy — the PC adventurer. NPCs get a different policy later (§3.6) on the same primitives.

```python
def Outfit(char):
    rng = gear_stream(char)         # Named_Stream(char, "gear") — never global random
    budget = _budget(char)          # Reports on Guild + Background tags — no if/elif
    _arm(char, budget, rng)         # weapons: guild kit ∩ ability bias (STR→heavy/thrown,
                                    #   DEX→finesse/bows); martial only if trained
    _armor(char, budget, rng)       # best wearable that BEATS the unarmored formula;
                                    #   shield only if legal (Monk UD: never;
                                    #   two-handed primary: no; hand free)
    _pack(char, budget, rng)        # class pack + background items + proficient tools
                                    #   + level-band extras; leftover stays in purse
    _resolve_ac(char)               # THE one AC owner (see 3.2)
    grant(char, name="Equipment", ...)  # sheet Entry via FeaturesKit like everything else
```

Deterministic: same seed → byte-identical loadout (Divine Order precedent — salted
per-character stream, `char.dices`/Named_Stream, never `app.random`).

### 3.2 One AC owner: `_resolve_ac`

Reads TOP tags + actually equipped items. Kills the skill-flag hack, the double +2, and the
dead feat.

- `AC = max(armor_formula(worn), unarmored_formulas(char)) + shield_bonus(equipped, legal)`
- Unarmored formulas come from the **UD training tags** (Monk `10+DEX+WIS`, Barbarian
  `10+DEX+CON`), which get real `apply=` hooks — sheet prose and the number can never disagree.
- Base for everyone else: `10 + DEX` (fixes the flat-10 bug).
- `Inventory` finally grows `get_worn_armor()` / `is_wearing_shield()` — the API the dead
  feat already specified.
- Legality table is explicit + testable: Monk UD excludes shields; Barbarian UD allows them;
  two-handed primary excludes them; armor requires the training tag
  (`char in HeavilyArmored` etc.), not string-matched class names.

### 3.3 Budget = Reports, not string matching

- `Build_Guild` chassis gains a `GOLD` Report (class die × count — keep the current curve:
  50d4 martials, 40d4 half, 20d4 monk/druid/barb, + Artificer which today gets 0).
- Background tags' existing `EQUIPMENT` Report (dead "50 GP" today) becomes real:
  `gold + items tuple`. The 71 renamed backgrounds stop falling to the anonymous `else`.
  This is the surface the deferred **thematic-item ledger** quest (backgrounds thread)
  plugs into.
- Level scaling: ONE roll (fix the N=0 clamp so level 1 adds nothing), spent once,
  leftover = purse shown. Level bands upgrade quality: armor grades at 5/10/15,
  consumables, and magic items **only when their effect is instantiated**
  (a Cloak of Protection that doesn't change AC does not exist).

### 3.4 Pipeline reorder (verified feasible)

Proficiency flags are set in `set_stats` → `set_Skills` (before any features). Therefore in
`set_char_features`:

```
apply_species_features()
apply_background_features()
Outfit(char)                 # ← equipment now exists BEFORE trainings awaken
apply_class_features()       # masteries can read owned weapons
...
(delete GenerateEquipment call at :147 and set_Objects at awaken_player :77)
```

### 3.5 Mastery bridge

`pick_weapon_masteries(char, n)` becomes: **owned weapons first, then proficient catalogue**,
filtered by class restriction (Barbarian melee-only, Rogue proficient-only; no firearms
without proficiency). Wire as `apply=` on the four unresolved mastery trainings — the exact
Divine Order pattern. Draw from the character's stream, not stdlib random.

### 3.6 NPC gear — a different POLICY, same primitives (DEFERRED by decision)

**Decision (2026-07-29): leave NPCs on Lodge/AtlasPugna for now.** When their quest opens,
NPCs do NOT get the PC adventurer loadout — being different here is a feature:

- **Characteristic weapons.** The signature weapon comes from archetype/guild identity
  (queried from the shared Ledger records), not from a shopping trip. A Knight carries a
  longsword because it is a Knight.
- **Travel light.** No packs, tools, or purse simulation — an NPC carries only what its role
  implies plus a few **lootables**.
- **Lootables raise combat proficiency.** The few carried items are the interesting drops,
  each mechanically instantiated on the NPC (a weapon tier, an armor grade, a consumable) —
  so looting them means something at the table.

Groundwork the PC quests must leave in place: policy-free primitives (`Outfit_Player` as the
first policy, `Outfit_NonPlayer` as a later one), one shared weapon catalogue, and the AC
resolver taking "natural armor" as an input. Entry point when it opens:
`Grimoire_of_NPC.py` `Finish_Awakening` after `Apply_Background_Training` (L167), gated on
`not light`; proficiency bridge from guild helper tags (`MartialArms`→`Martial_Weapons`, …);
adapter for the `.abilities` collision; determinism via `Named_Stream(npc, "gear")`;
`SetAC` → `max(natural, equipped)`; `SimpleAttack` renders owned weapons — retiring the
empty AtlasPugna flavor lists and the parallel Weapon class only then.

---

## 4. Quest Ladder (each shippable, each gated on ALL GREEN)

### Quest 0 — Triage ✅ DONE (2026-07-29)
Gate: `PYTHONPATH=. STRICT_GENERATION=1 .venv/bin/python3 scripts/verify_equipment.py`
→ **ALL GREEN**, verified at 720 characters (12 guilds × 5 levels × 12 seeds).
Default sweep is gate-sized (3 seeds); `EQUIPMENT_SEEDS=N` widens it — the 12-seed sweep
caught 62 failures the 3-seed sweep missed, so run it wide before closing a quest.

Landed:
- **Value/weight transposition fixed** at the root (`Armor`/`Weapon` `super().__init__`) —
  every price and encumbrance in the game was swapped.
- **One budget per character**: `setObjects` no longer re-rolls; it spends what is left.
  Budget `print`s removed; the level roll no longer fires at level 1.
- **AC is honest**: base AC is rebased on the *rolled* Dexterity (`set_stats`) instead of
  the placeholder 10s `set_combat_attributes` saw — characters with a negative DEX modifier
  were shipping an inflated AC; shield grants +2 exactly once (idempotent via
  `is_wearing_shield`); armor upgrades preserve the shield bonus; AC only rises when the
  armor is actually affordable and worn (`equip_defense` now reports success); the Clothes
  fallback writes AC.
- **Slots make sense**: melee → right+melee, ranged → its own slot (no longer displaces the
  shield). The sheet's Melee/Ranged rows are no longer permanently "-".
- **Bag deduplicated**: duplicate ranged weapon, duplicate shield blocks, and double
  Rope/Torch purchases removed; survival items bought at most once (`has_item`).
- **Crashes fixed**: Weaver's Tools `NameError`; `equip_left` refund `AttributeError`.
- **Inventory API added**: `get_worn_armor()`, `is_wearing_shield()`, `has_item()` —
  the surface `Grimoire_of_Features.set_UnarmoredDefense` already expected.
- **Strict mode**: `STRICT_GENERATION=1` makes `summon_player` raise the first failure
  instead of re-rolling the seed 5 times.

Strict mode immediately unmasked **three pre-existing crashes** the retry loop was hiding
(all unrelated to equipment, all fixed):
1. Forest Gnome lineage → `ImportError: SpeakWithAnimals` (casing; lodge defines
   `SpeakwithAnimals`) — fixed with an alias, matching the lodge's own convention.
2. Eldritch Knight below level 3 → `IndexError` in `random.choices` on an empty pool.
3. Arcane Trickster below level 3 → `ValueError: max() iterable argument is empty`.

Deliberately left for later quests: description-only magic items (Quest 4), fake
`Melee_Martial`/`Ranged_Martial` catalogues (Quests 1–2), escaped-HTML weapon rows and
`Armor.__repr__` on the sheet (Quest 2), mastery↔equipment disconnect (Quest 3).

### Quest 1 — Ledgers (data only)
Rewrite `Ledger_of_Weapons`/`Ledger_of_Armors` as full PHB 2024 record catalogues;
add `Ledger_of_Gear`; `WEAPON_MASTERIES` becomes a derivation; delete `gear_gen.py`,
`items.py`; fix `Compass_of_Recharging` import side effect.
**Accept:** ledger self-test — every weapon has valid mastery + category, no duplicate names;
every `Lodge` weapon resolvable against the catalogue.

### Quest 2 — `GearKit.Outfit` for PCs (the core)
Budget Reports; loadout algorithm; Inventory API (`get_worn_armor`, `is_wearing_shield`,
sane `buy_item` with `>=` + explicit failure); `_resolve_ac`; pipeline reorder; retire
`GenerateEquipment`/`setObjects`/`set_Armor`/`choose_melee_weapon`/`SetFeatures`/
`apply_class_proficiencies` (mine its PHB kits into records first). Sheet: render weapon
Entries as HTML (not escaped), Armor gets a real `__str__`, drop-or-populate Melee/Ranged
rows, purse as a Chip, integer gold.
**Accept:** 13 guilds × levels {1,3,5,10,20} × 40 seeds — no crash, RAW-correct AC, zero
duplicate items, `purse == budget − Σspends`, byte-identical rerun per seed.

### Quest 3 — Masteries & synergies resolved
Mastery bridge (owned ∪ proficient, class-restricted); `apply=` resolves the four
"of your choice" mastery texts; UD tags get real `apply=`; `_resolve_ac` reads tags.
**Accept:** every sheet names concrete mastered weapons, ≥1 owned; Monk never has a shield;
Barbarian UD AC is exactly `10+DEX+CON(+2 shield)`; Wizard AC is `10+DEX` unarmored.

### Quest 4 — Flavor layer (the "unique" part)
Background gear records (reopens the deferred thematic-item ledger on a now-real surface);
species biases as loadout *weights* (Dwarf → smith's tools likelihood, not hard rules);
level-band magic items with instantiated effects only.
**Accept:** two same-guild characters with different backgrounds/species differ in gear;
every magic item's effect is mechanically present on the character.

### Quest 5 — NPC signature loadouts (DEFERRED — see §3.6; NPCs untouched until then)
`Outfit_NonPlayer` policy: characteristic weapon from archetype identity; minimal carry;
lootables with instantiated effects. Proficiency bridge; item-derived AC/attacks; NPC sheet
gear section reusing PC components; `Named_Stream(npc, "gear")`.
**Accept:** NPC attacks reference owned weapons; every lootable's effect is mechanically
present; light-NPC path unaffected; NPC≈PC combat quality at equal level.

### Quest 6 — Verification harness
`scripts/verify_equipment.py` in the style of `verify_2024_trainings.py`: the invariant
suite from Quests 0–5 as a permanent ALL-GREEN gate. Kit self-tests
(`python -m AtlasInventarium.GearKit`).

---

## 5. Design Principles (growth criteria)

1. **Records → Kit → Tags.** Data in Ledgers/Maps (frozen dataclasses), behavior in exactly
   one Kit, semantic membership as Tags. Adding a weapon = one record. A guild's gear =
   chassis Reports. A background's kit = one field.
2. **One fact, one owner.** One weapon catalogue for PC/NPC/masteries; one AC resolver;
   one budget roll. Parallel implementations are the root cause of this audit.
3. **Forks resolved, never suggested.** Loadout, masteries, and UD are generator decisions,
   deterministic per seed (salted per-character streams). No "of your choice" reaches a sheet.
4. **Mechanics instantiated, not described.** If an item's effect isn't on the character
   object, the item doesn't exist. (Divine Order precedent.)
5. **Public spec vs private body.** `AtlasInventarium/__init__` exports a deliberate surface
   (`Outfit`, `Inventory`, ledger queries); everything else is private. Stable import
   contracts for app/ and AtlasActorLudi/.
6. **Every Kit self-tests; every quest gates on ALL GREEN.** Crashes must surface —
   strict mode disables retry masking in tests.
