"""
Ledger of Items  —  items.py
=============================

Thematic starting-equipment generator built on a small Wave-Function-Collapse
(WFC) engine, mirroring the collapse/render pattern used for the Charts of the
Monomyth.

The idea, in one line: an item is a *base noun* (cape, dagger, shield, bag…)
whose flavour is **collapsed from tags** describing the character — their
species, their class/background, and the bonds (relationships) in their life.

    Farmer      -> "A set of clothes, with a cape given by a friend"
    Noble       -> "A shield bearing the symbol of your house"
    Dragonborn  -> "A dagger shaped like a dragon tooth"
    Elf         -> "A silvery cape"
    Dwarf cleric-> "A bag marked with runes of protection"

How it works
------------
Every generated item is a *cell* in superposition over a domain of possible
descriptors.  Constraints (the character's tags + which base the descriptor can
attach to) prune that domain; then we *collapse* each slot to one concrete
choice by weighted random pick.  Two data tables drive everything:

    BASES      — the noun you start with (has `kinds` + tag `affinity`)
    MODIFIERS  — a descriptor gated by tags, restricted to certain base `kinds`

Adding items is pure data entry: append a `BaseItem(...)` or `Modifier(...)`
row.  No engine changes required.

Public API (the deliberate surface — everything else is private body):
    Equipment(npc)          -> formatted starting-equipment package (str)
    collapse(tags, ...)     -> a single Item collapsed from a tag set
    tags_for(npc)           -> the frozenset of tags an npc contributes
    Item                    -> the small OOP item class

Liberal aliases are provided for import-site convenience (see bottom of file).
"""

import random
from dataclasses import dataclass, field

import dnd


# ---------------------------------------------------------------------------
# 1.  The item — a small OOP class that renders tags into a natural phrase
# ---------------------------------------------------------------------------

class Item:
    """A single piece of equipment: a base noun dressed in collapsed modifiers.

    An Item is assembled slot by slot and rendered to a natural-language
    phrase.  Modifiers land in one of three grammatical positions:

        pre     adjectives before the noun     -> "A *silvery* cape"
        phrase  a phrase glued on with a space -> "A dagger *shaped like a
                                                    dragon tooth*"
        clause  a clause glued on with a comma -> "A cloak*, given by a friend*"
    """

    _VOWELS = "aeiou"

    def __init__(self, noun, kinds=(), article=None):
        self.noun = noun
        self.kinds = frozenset(kinds)
        self._article = article            # explicit override ("a set of …")
        self.pre = []                      # adjectives
        self.phrases = []                  # space-joined tails
        self.clauses = []                  # comma-joined tails
        self.tags = set()                  # tags that shaped this item

    # -- assembly ----------------------------------------------------------
    def add(self, modifier):
        """Attach a collapsed Modifier in its grammatical slot."""
        text = modifier.render()
        if modifier.position == "pre":
            self.pre.append(text)
        elif modifier.position == "clause":
            self.clauses.append(text)
        else:                              # "phrase"
            self.phrases.append(text)
        self.tags.update(modifier.gate)
        return self

    # -- rendering ---------------------------------------------------------
    @property
    def article(self):
        if self._article:
            return self._article
        head = (self.pre[0] if self.pre else self.noun).lstrip()
        return "an" if head[:1].lower() in self._VOWELS else "a"

    def render(self):
        head = self.noun
        if self.pre:
            head = " ".join(self.pre) + " " + head
        text = f"{self.article} {head}"
        if self.phrases:
            text += " " + " ".join(self.phrases)
        if self.clauses:
            text += ", " + ", ".join(self.clauses)
        return text[:1].upper() + text[1:]

    def __str__(self):
        return self.render()

    def __repr__(self):
        return f"Item({self.render()!r})"


# ---------------------------------------------------------------------------
# 2.  The ledger rows — pure data
# ---------------------------------------------------------------------------
# Tags use a `namespace:value` convention so gates read unambiguously:
#     species:elf   class:noble   role:divine   bond:house   any
#
# A BaseItem's `affinity` lists tags that make it *more likely* for a matching
# character (a Dwarf leans toward axes and runes; an Elf toward bows and
# silvery cloth).  A Modifier's `gate` lists the tags that *unlock* it; an
# empty gate (or the literal "any") means it fits everyone.

@dataclass(frozen=True)
class BaseItem:
    noun: str
    kinds: tuple = ()          # ("garment",), ("weapon",), ("focus","weapon")…
    affinity: tuple = ()       # tags that boost this base's weight
    weight: float = 1.0        # baseline weight before affinity boosts
    article: str = None        # explicit article override, e.g. "a"


@dataclass(frozen=True)
class Modifier:
    template: str              # the descriptive text
    gate: tuple = ()           # tags that unlock this modifier (ANY match)
    applies_to: tuple = ("any",)   # base kinds it can attach to
    slot: str = "motif"        # WFC slot; at most one modifier per slot
    position: str = "phrase"   # "pre" | "phrase" | "clause"
    weight: float = 1.0

    def render(self):
        return self.template


# --- base items ------------------------------------------------------------
# kinds vocabulary:
#   garment  weapon  focus  instrument  tool  container  trinket  gear
BASES = [
    # -- garments (outfits & worn things) ------------------------------------
    BaseItem("set of clothes", ("garment",), article="a", weight=1.4),
    BaseItem("traveler's cloak", ("garment",), weight=1.2),
    BaseItem("cape", ("garment",),
             affinity=("species:elf", "class:noble", "role:social"), weight=1.1),
    BaseItem("hooded cloak", ("garment",), affinity=("role:stealth",)),
    BaseItem("woolen tunic", ("garment",), affinity=("role:commoner",)),
    BaseItem("leather jerkin", ("garment",), affinity=("role:martial",)),
    BaseItem("simple robe", ("garment",),
             affinity=("role:arcane", "role:divine")),
    BaseItem("pair of boots", ("garment",), article="a"),
    BaseItem("wide-brimmed hat", ("garment",), affinity=("role:arcane",)),

    # -- weapons -------------------------------------------------------------
    BaseItem("dagger", ("weapon",),
             affinity=("role:stealth", "species:dragon"), weight=1.2),
    BaseItem("shortsword", ("weapon",), affinity=("role:martial",)),
    BaseItem("hand axe", ("weapon",),
             affinity=("species:dwarf", "species:orc")),
    BaseItem("spear", ("weapon",), affinity=("role:martial", "species:lizardfolk")),
    BaseItem("shortbow", ("weapon",), affinity=("species:elf", "role:nature")),
    BaseItem("sling", ("weapon",), affinity=("role:commoner", "species:halfling")),
    BaseItem("quarterstaff", ("weapon", "focus"),
             affinity=("role:arcane", "role:nature", "role:divine")),
    BaseItem("mace", ("weapon",), affinity=("role:divine",)),

    # -- arcane / divine / nature focuses ------------------------------------
    BaseItem("holy symbol", ("focus",), affinity=("role:divine",), weight=1.2),
    BaseItem("amulet", ("focus", "trinket"),
             affinity=("role:divine", "role:arcane")),
    BaseItem("wand", ("focus",), affinity=("role:arcane",)),
    BaseItem("spellbook", ("focus",), affinity=("role:arcane",)),
    BaseItem("rune-stone", ("focus", "trinket"),
             affinity=("species:dwarf", "role:arcane")),
    BaseItem("totem", ("focus",), affinity=("role:nature", "species:orc")),
    BaseItem("sprig of holly", ("focus",), affinity=("role:nature",)),

    # -- instruments ---------------------------------------------------------
    BaseItem("lute", ("instrument",), affinity=("class:bard", "role:social")),
    BaseItem("flute", ("instrument",), affinity=("class:bard", "role:nature")),
    BaseItem("hand drum", ("instrument",), affinity=("class:bard", "species:orc")),

    # -- tools ---------------------------------------------------------------
    BaseItem("set of thieves' tools", ("tool",),
             affinity=("role:stealth",), article="a"),
    BaseItem("herbalism kit", ("tool",), affinity=("role:nature", "class:healer")),
    BaseItem("healer's kit", ("tool",), affinity=("class:healer", "role:divine")),
    BaseItem("set of smith's tools", ("tool",),
             affinity=("species:dwarf", "class:crafter"), article="a"),
    BaseItem("cook's utensils", ("tool",), affinity=("role:commoner",)),
    BaseItem("cartographer's tools", ("tool",), affinity=("class:explorer",)),

    # -- containers ----------------------------------------------------------
    BaseItem("bag", ("container",), weight=1.2),
    BaseItem("belt pouch", ("container",)),
    BaseItem("backpack", ("container",), affinity=("class:explorer", "class:traveler")),
    BaseItem("satchel", ("container",), affinity=("role:arcane",)),
    BaseItem("waterskin", ("container", "gear")),

    # -- trinkets / keepsakes ------------------------------------------------
    BaseItem("locket", ("trinket",), weight=1.1),
    BaseItem("signet ring", ("trinket",), affinity=("class:noble",)),
    BaseItem("medallion", ("trinket",), affinity=("role:divine", "class:noble")),
    BaseItem("worn journal", ("trinket",), affinity=("role:arcane", "class:scholar")),
    BaseItem("carved charm", ("trinket",), affinity=("role:nature",)),

    # -- mundane gear --------------------------------------------------------
    BaseItem("coil of rope", ("gear",), article="a"),
    BaseItem("tinderbox", ("gear",)),
    BaseItem("bullseye lantern", ("gear",), affinity=("class:explorer",)),
    BaseItem("bedroll", ("gear",), affinity=("class:traveler",)),
]


# --- modifiers -------------------------------------------------------------
# Grouped by slot.  A single item fills at most one modifier per slot, so the
# slots act like WFC "channels": a material *and* a motif *and* a provenance
# can co-occur, but never two materials.
MODIFIERS = [
    # == material / quality (pre-adjective) =================================
    Modifier("silvery", ("species:elf",), ("garment", "weapon", "trinket"),
             slot="material", position="pre", weight=1.4),
    Modifier("moon-pale", ("species:elf",), ("garment",),
             slot="material", position="pre"),
    Modifier("iron-banded", ("species:dwarf",), ("container", "weapon", "gear"),
             slot="material", position="pre"),
    Modifier("gilded", ("class:noble", "role:social"), ("garment", "trinket", "focus"),
             slot="material", position="pre"),
    Modifier("weathered", ("role:martial", "class:traveler", "class:explorer"),
             ("garment", "gear", "container"), slot="material", position="pre"),
    Modifier("finely wrought", ("class:crafter",), ("weapon", "tool", "trinket"),
             slot="material", position="pre"),
    Modifier("scale-patterned", ("species:dragon", "species:lizardfolk"),
             ("garment", "container"), slot="material", position="pre"),
    Modifier("well-worn", (), ("garment", "tool", "container", "gear"),
             slot="material", position="pre", weight=0.5),

    # == motif / shape (phrase) ============================================
    Modifier("shaped like a dragon tooth", ("species:dragon",),
             ("weapon", "trinket"), slot="motif", weight=1.6),
    Modifier("etched with elven leaves", ("species:elf",),
             ("weapon", "focus", "trinket"), slot="motif"),
    Modifier("carved from a single antler", ("role:nature",),
             ("focus", "weapon", "trinket"), slot="motif"),
    Modifier("wrapped in worn leather", ("role:martial", "role:stealth"),
             ("weapon", "tool"), slot="motif"),
    Modifier("bearing the symbol of your house", ("class:noble", "bond:house"),
             ("garment", "focus", "trinket", "container"), slot="motif", weight=1.5),
    Modifier("marked with runes of protection",
             ("species:dwarf", "role:divine", "role:arcane"),
             ("container", "focus", "garment", "gear"), slot="motif", weight=1.3),
    Modifier("stamped with a merchant's seal", ("class:merchant",),
             ("container", "trinket"), slot="motif"),
    Modifier("inked with faded star-charts", ("role:arcane", "class:scholar"),
             ("trinket", "focus", "container"), slot="motif"),
    Modifier("strung with hunting-trophies", ("class:hunter", "species:orc"),
             ("garment", "container"), slot="motif"),
    Modifier("blessed at a wayside shrine", ("role:divine",),
             ("focus", "trinket", "garment"), slot="motif"),

    # == provenance / bond (clause) ========================================
    Modifier("given by a friend", ("bond:friend",), ("any",),
             slot="provenance", position="clause", weight=1.2),
    Modifier("handed down through your family", ("bond:family",), ("any",),
             slot="provenance", position="clause"),
    Modifier("a gift from your mentor", ("bond:mentor",), ("any",),
             slot="provenance", position="clause"),
    Modifier("bearing the crest of your house", ("bond:house",),
             ("garment", "trinket", "focus"), slot="provenance", position="clause"),
    Modifier("entrusted to you by your order", ("bond:order",),
             ("focus", "trinket", "container"), slot="provenance", position="clause"),
    Modifier("won from an old rival", ("bond:rival",), ("weapon", "trinket"),
             slot="provenance", position="clause"),
    Modifier("all that remains of a lost love", ("bond:love",), ("trinket", "garment"),
             slot="provenance", position="clause"),
    Modifier("scavenged on the road", ("class:urchin", "class:traveler"), ("any",),
             slot="provenance", position="clause", weight=0.7),
]


# ---------------------------------------------------------------------------
# 3.  Tag extraction — turn an npc into the tag set that constrains collapse
# ---------------------------------------------------------------------------
# Backgrounds double as classes in this project, so each one contributes both a
# `class:<name>` tag and one or more broad `role:` tags used by many modifiers.
ROLE_MAP = {
    "martial":   {"Warrior", "Soldier", "Knight", "Guard", "Hero", "Barbarian",
                  "Berserker", "Bandit", "Pirate", "Mercenary"},
    "arcane":    {"Mage", "Warlock", "Witch", "Scholar", "Cultist"},
    "divine":    {"Cleric", "Priest", "Healer", "Monk"},
    "nature":    {"Druid", "Shaman", "Ranger", "Hunter", "Explorer", "Traveler"},
    "stealth":   {"Rogue", "Spy", "Criminal", "Charlatan", "Urchin", "Pirate", "Bandit"},
    "social":    {"Noble", "Merchant", "Bard", "Artist", "Charlatan"},
    "commoner":  {"Commoner", "Crafter", "Expert", "Urchin", "Healer"},
}

# Which bonds a background is *drawn* to.  "friend" and "family" are always in
# the pool so anyone can end up with a keepsake from a loved one.
BOND_MAP = {
    "Noble":    ["house", "family", "mentor"],
    "Knight":   ["order", "house", "mentor"],
    "Cleric":   ["order", "mentor", "friend"],
    "Priest":   ["order", "mentor", "friend"],
    "Monk":     ["order", "mentor"],
    "Cultist":  ["order", "rival"],
    "Soldier":  ["friend", "rival", "mentor"],
    "Warrior":  ["friend", "rival"],
    "Mage":     ["mentor", "rival"],
    "Warlock":  ["mentor", "rival"],
    "Scholar":  ["mentor", "friend"],
    "Bard":     ["friend", "love", "rival"],
    "Artist":   ["love", "friend"],
    "Merchant": ["family", "friend"],
    "Rogue":    ["rival", "friend"],
    "Spy":      ["mentor", "rival"],
    "Urchin":   ["friend", "family"],
    "Criminal": ["rival", "friend"],
    "Ranger":   ["mentor", "friend"],
    "Hunter":   ["family", "mentor"],
    "Druid":    ["mentor", "order"],
    "Shaman":   ["family", "order"],
}
_DEFAULT_BONDS = ["friend", "family", "mentor"]


def _roles_for(background):
    return {role for role, names in ROLE_MAP.items() if background in names}


def _pick_bond(background, rng):
    pool = BOND_MAP.get(background, []) + _DEFAULT_BONDS
    return rng.choice(pool)


def tags_for(npc, rng=random):
    """Collapse an npc into the frozenset of tags that constrain its gear.

    Contributes: species (race + subrace), class/background, broad role tags,
    and exactly one *bond* tag standing in for the character's relationships.
    Works with the project's NPC objects (attributes) or a plain dict.
    """
    def attr(name, default=""):
        if isinstance(npc, dict):
            return npc.get(name, default)
        return getattr(npc, name, default)

    background = (attr("background") or "").strip()
    race = (attr("race") or "").strip()
    subrace = (attr("subrace") or "").strip()

    tags = {"any"}
    if race:
        tags.add(f"species:{race.lower()}")
    if subrace:
        tags.add(f"species:{subrace.lower()}")
    if background:
        tags.add(f"class:{background.lower()}")
    for role in _roles_for(background):
        tags.add(f"role:{role}")
    tags.add(f"bond:{_pick_bond(background, rng)}")
    return frozenset(tags)


# ---------------------------------------------------------------------------
# 4.  The WFC engine — collapse a tag set into a concrete Item
# ---------------------------------------------------------------------------

def _weighted_choice(options, weights, rng):
    return rng.choices(options, weights=weights, k=1)[0]


def _base_weight(base, tags):
    """A base's weight is its baseline, boosted for every affinity tag met."""
    w = base.weight
    for a in base.affinity:
        if a in tags:
            w += 1.3
    return w


def _modifier_weight(mod, tags):
    """Specific (gated-and-matched) modifiers outweigh universal filler, so the
    result feels personal rather than generic."""
    if not mod.gate or "any" in mod.gate:
        return mod.weight * 0.6            # universal filler: quieter
    matched = sum(1 for g in mod.gate if g in tags)
    return mod.weight * (1.0 + matched)    # louder the better it fits


def _compatible(mod, base, tags):
    gate_ok = (not mod.gate or "any" in mod.gate
               or any(g in tags for g in mod.gate))
    kind_ok = ("any" in mod.applies_to
               or bool(base.kinds & set(mod.applies_to)))
    return gate_ok and kind_ok


def collapse(tags, kinds=None, max_mods=2, slots=None, rng=random):
    """Collapse `tags` into a single Item.

    kinds     restrict the base to these kinds (e.g. {"weapon"}); None = any
    max_mods  how many modifier slots to try to fill
    slots     preferred slot order to fill; None = shuffle of all slots
    """
    tags = set(tags)

    # -- collapse the base cell -------------------------------------------
    pool = BASES if not kinds else [b for b in BASES if b.kinds & set(kinds)]
    if not pool:
        pool = BASES
    weights = [_base_weight(b, tags) for b in pool]
    base = _weighted_choice(pool, weights, rng)

    item = Item(base.noun, base.kinds, base.article)

    # -- collapse the modifier cells, one per slot ------------------------
    order = slots or ["motif", "material", "provenance"]
    order = list(order)
    rng.shuffle(order)
    filled = 0
    used_slots = set()
    for slot in order:
        if filled >= max_mods:
            break
        candidates = [m for m in MODIFIERS
                      if m.slot == slot and m.slot not in used_slots
                      and _compatible(m, base, tags)]
        if not candidates:
            continue
        w = [_modifier_weight(m, tags) for m in candidates]
        chosen = _weighted_choice(candidates, w, rng)
        item.add(chosen)
        used_slots.add(slot)
        filled += 1
    return item


# ---------------------------------------------------------------------------
# 5.  The package — a background's full starting-equipment loadout
# ---------------------------------------------------------------------------
# Each slot names the base `kinds` it may draw from and how insistently it
# appears.  `signature` kinds are chosen from the character's role, so a mage
# gets a focus, a soldier a weapon, a rogue tools.
SIGNATURE_KINDS = {
    "martial": ("weapon",),
    "arcane":  ("focus",),
    "divine":  ("focus",),
    "nature":  ("focus", "tool"),
    "stealth": ("weapon", "tool"),
    "social":  ("instrument", "trinket"),
    "commoner": ("tool", "weapon"),
}


def _signature_kinds(tags):
    kinds = set()
    for role, ks in SIGNATURE_KINDS.items():
        if f"role:{role}" in tags:
            kinds.update(ks)
    return tuple(kinds) or ("weapon", "tool")


def Equipment(npc, rng=random, as_list=False):
    """Generate a background's thematic starting-equipment package.

    Returns a formatted bullet list by default (drop-in for the NPC sheet), or
    the raw list of Item objects when `as_list=True`.

    This is the entry point the character/NPC generator calls: the package is
    collapsed fresh from the npc's tags every time it is built.
    """
    tags = tags_for(npc, rng=rng)

    package = []
    # 1. an outfit — everyone is clothed
    package.append(collapse(tags, kinds={"garment"}, max_mods=2, rng=rng))
    # 2. a signature piece — the tag-charged heart of the loadout
    package.append(collapse(tags, kinds=set(_signature_kinds(tags)),
                            max_mods=2, rng=rng))
    # 3. a kit or pack — practical, still lightly themed
    package.append(collapse(tags, kinds={"tool", "container", "gear"},
                            max_mods=1, rng=rng))
    # 4. a keepsake — a bond-item, sometimes
    if rng.random() < 0.6:
        package.append(collapse(tags, kinds={"trinket", "garment"},
                                max_mods=1, slots=["provenance", "material"],
                                rng=rng))

    if as_list:
        return package
    return "\n".join(f"- {item.render()}" for item in package)


# ---------------------------------------------------------------------------
# 6.  Public surface & aliases  (modular-API convention: stable import names)
# ---------------------------------------------------------------------------
equipment = Equipment                # snake_case alias
StartingEquipment = Equipment
starting_equipment = Equipment
Collapse = collapse
Tags = tags_for


def Item_of(npc, **kw):
    """Convenience: one collapsed signature Item for an npc (not the package)."""
    return collapse(tags_for(npc), kinds=set(_signature_kinds(tags_for(npc))), **kw)


__all__ = [
    "Item", "BaseItem", "Modifier",
    "Equipment", "equipment", "StartingEquipment", "starting_equipment",
    "collapse", "Collapse", "tags_for", "Tags", "Item_of",
    "BASES", "MODIFIERS",
]


# ---------------------------------------------------------------------------
# 7.  Standalone demo — `python items.py`
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    samples = [
        {"race": "Human", "subrace": "", "background": "Commoner"},
        {"race": "Human", "subrace": "", "background": "Noble"},
        {"race": "Dragon", "subrace": "", "background": "Warrior"},
        {"race": "Elf", "subrace": "", "background": "Ranger"},
        {"race": "Dwarf", "subrace": "", "background": "Cleric"},
        {"race": "Halfling", "subrace": "", "background": "Rogue"},
        {"race": "Orc", "subrace": "", "background": "Shaman"},
        {"race": "Gnome", "subrace": "", "background": "Mage"},
    ]
    for s in samples:
        label = f"{s['race']} {s['background']}"
        print(f"\n=== {label} ===")
        print(Equipment(s))
