"""
BackgroundKit

TOP backgrounds (2024 PHB — all 16).

Depends on:
- CharactersKit.Character
- FeaturesKit (Origin Feats)

How to use this Kit:
	1. ``Background`` — root Tag (Character only).
	2. One concrete Tag per background (copy ``Wayfarer`` as the template).
	3. Fixed prose and tables live as **class attributes**, not ``@Record``.
	4. ``@Imprint`` *writes* plain attributes on the Character and applies Tags.

Why not ``@Record`` for title / description?
	``@Record`` is for *visible state on the Agent that TOP manages* — often
	derived or overlaid (e.g. Spell.school from the School Tag). Fixed flavor
	text and skill lists do not need that. Set them with ordinary assignment
	in Imprint (``char.background = "Wayfarer"``), or keep them as class
	attributes on the Tag and copy them across in Imprint. That is easier to
	read, debug, and match the CharactersKit / SpeciesKit style.

Usage
	char = Character(seed=1)
	Wayfarer(char)
	assert char in Wayfarer and char in Background
	assert char.background == "Wayfarer"
"""

from TagKit import Pre, Underlay, Imprint

from AtlasLusoris.CharactersKit import Character, Role
from AtlasLusoris.FeaturesKit import (
	BACKGROUND_ORIGIN_FEATS,
	Alert,
	Crafter,
	Healer,
	Lucky,
	Magic_Initiate_Cleric,
	Magic_Initiate_Druid,
	Magic_Initiate_Wizard,
	Musician,
	Savage_Attacker,
	Skilled,
	Tavern_Brawler,
	Tough,
	Feature,
	grant,
	)


# ---------------------------------------------------------------------------
# Root
# ---------------------------------------------------------------------------

class Background(Role):
	"""Root Tag for character backgrounds."""

	NAME = "Background"
	FEATURES = []
	@Pre
	def Character_Only(target):
		return isinstance(target, Character)

	@Imprint
	def ensure_bag(target):
		if getattr(target, "features", None) is None:
			target.features = []

	@Underlay
	def __contains__(agent, underlay, key):
		if isinstance(key, str):
			key = key.casefold()
			name = getattr(agent, "background", None)
			if isinstance(name, str) and key == name.casefold():
				return True
		return underlay()


# ---------------------------------------------------------------------------
# Soft ASI optimizer (class prefs + round odds → even)
# ---------------------------------------------------------------------------
# Recalled from Grimoire_of_Characters.New_stats (class primary/secondary)
# and Grimoire_of_Features._ability_to_increase (prefer odd scores so a +1
# bumps the modifier). Users notice when boosts land where they help.

_ALL_ABILITIES = ("STR", "DEX", "CON", "INT", "WIS", "CHA")

CLASS_STAT_PREFERENCES = {
	"Barbarian": ("STR", "CON"),
	"Bard": ("CHA", "DEX"),
	"Cleric": ("WIS", "STR"),
	"Druid": ("WIS", "CON"),
	"Fighter": ("STR", "CON"),
	"Monk": ("DEX", "WIS"),
	"Paladin": ("STR", "CHA"),
	"Ranger": ("DEX", "WIS"),
	"Rogue": ("DEX", "INT"),
	"Sorcerer": ("CHA", "CON"),
	"Warlock": ("CHA", "CON"),
	"Wizard": ("INT", "CON"),
	}

# 2024 background recommended abilities (assign +2/+1 or +1/+1/+1 among these)
BACKGROUND_ABILITY_CHOICES = {
	"Acolyte": ("INT", "WIS", "CHA"),
	"Artisan": ("STR", "DEX", "INT"),
	"Charlatan": ("DEX", "CON", "CHA"),
	"Criminal": ("DEX", "CON", "INT"),
	"Entertainer": ("STR", "DEX", "CHA"),
	"Farmer": ("STR", "CON", "WIS"),
	"Guard": ("STR", "INT", "WIS"),
	"Guide": ("DEX", "CON", "WIS"),
	"Hermit": ("CON", "WIS", "CHA"),
	"Merchant": ("CON", "INT", "CHA"),
	"Noble": ("STR", "INT", "CHA"),
	"Sage": ("CON", "INT", "WIS"),
	"Sailor": ("STR", "DEX", "WIS"),
	"Scribe": ("DEX", "INT", "WIS"),
	"Soldier": ("STR", "DEX", "CON"),
	"Wayfarer": ("DEX", "WIS", "CHA"),
	}

ARTISAN_TOOLS = (
	"Alchemist_Supplies",
	"Brewer_Supplies",
	"Calligrapher_Supplies",
	"Carpenter_Tools",
	"Cartographer_Tools",
	"Cobbler_Tools",
	"Cook_Utensils",
	"Glassblower_Tools",
	"Jeweler_Tools",
	"Leatherworker_Tools",
	"Mason_Tools",
	"Painter_Supplies",
	"Potter_Tools",
	"Smith_Tools",
	"Tinker_Tools",
	"Weaver_Tools",
	"Woodcarver_Tools",
	)


def _class_ranked(char):
	"""Primary then secondary for char.char_class (Eldritch Knight → INT 2nd)."""
	klass = getattr(char, "char_class", None)
	primary, secondary = CLASS_STAT_PREFERENCES.get(klass, (None, None))
	subclass = getattr(char, "subclass", None) or ""
	if "Eldritch Knight" in str(subclass) or (
			hasattr(char, "__contains__") and "Eldritch Knight" in char
			):
		secondary = "INT"
	return primary, secondary


def _pick_boost_ability(char, pool, scores):
	"""
	Soft-pick one ability from pool:
	1. prefer odd scores (so +1 rounds to even and raises the modifier)
	2. prefer class primary, then secondary
	3. prefer higher current score
	Ties broken with char.Pick.
	"""
	primary, secondary = _class_ranked(char)

	def priority(key):
		if key == primary:
			return 0
		if key == secondary:
			return 1
		return 2

	def rank(key):
		value = getattr(scores, key) if scores is not None else 10
		# odds first (False < True), then class priority, then high→low
		return (value % 2 == 0, priority(key), -value)

	best = min(rank(key) for key in pool)
	tied = [key for key in pool if rank(key) == best]
	return char.Pick(tied) if len(tied) > 1 else tied[0]


def _grant_ability_boosts(char, abilities=None):
	"""
	2024 background ASI: +2/+1 or +1/+1/+1 among recommended abilities,
	soft-optimized for class prefs and odd→even rounding.
	"""
	pattern = char.Pick([(2, 1), (1, 1, 1)])
	if abilities is None:
		name = getattr(char, "background", None)
		abilities = BACKGROUND_ABILITY_CHOICES.get(name, _ALL_ABILITIES)
	pool = list(abilities)
	if len(pool) < len(pattern):
		for key in _ALL_ABILITIES:
			if key not in pool:
				pool.append(key)
			if len(pool) >= len(pattern):
				break

	scores = getattr(char, "AS", None)
	chosen = []
	remaining = list(pool)
	ordered = sorted(pattern, reverse=True)
	for bonus in ordered:
		stat = _pick_boost_ability(char, remaining, scores)
		remaining.remove(stat)
		chosen.append((stat, bonus))

	if scores is None:
		char.background_asi = chosen
		return
	for stat, bonus in chosen:
		setattr(scores, stat, getattr(scores, stat) + bonus)


# ---------------------------------------------------------------------------
# Shared imprint helpers (keep concrete Tags thin)
# ---------------------------------------------------------------------------

def _grant_skills(char, skill_names):
	skills = getattr(char, "skills", None)
	if skills is None:
		char.background_skills = list(skill_names)
		return
	for name in skill_names:
		skill = getattr(skills, name, None)
		if skill is not None and hasattr(skill, "set_proficiency"):
			skill.set_proficiency()


def _grant_tool(char, tools):
	"""Grant one tool. ``tools`` may be a single attr name or a Pick pool."""
	if not tools:
		return
	pick = char.Pick(list(tools)) if isinstance(tools, (tuple, list)) else tools
	skills = getattr(char, "skills", None)
	if skills is None:
		char.background_tool = pick
		return
	skill = getattr(skills, pick, None)
	if skill is not None and hasattr(skill, "set_proficiency"):
		skill.set_proficiency()


def _grant_narrative(char, title: str, description: str):
	"""Background feature line — FeaturesKit Feature object on char.features."""
	grant(
		char,
		name=title,
		description=description,
		source="Background",
		)


def _awaken(char, tag):
	"""Shared Imprint body — every concrete Background Tag calls this."""
	char.background = tag.NAME
	_grant_ability_boosts(char, tag.ABILITIES)
	_grant_skills(char, tag.SKILLS)
	_grant_tool(char, getattr(tag, "TOOLS", ()))
	_grant_narrative(char, tag.TITLE, tag.DESCRIPTION)
	tag.ORIGIN_FEAT(char)


# ---------------------------------------------------------------------------
# 2024 PHB backgrounds (copy Wayfarer shape)
# ---------------------------------------------------------------------------

class Acolyte(Background):
	NAME = "Acolyte"
	TITLE = "Shelter of the Faithful"
	DESCRIPTION = (
		"You and your companions can expect free healing and care at temples "
		"of your faith."
		)
	SKILLS = ("Insight", "Religion")
	TOOLS = "Calligrapher_Supplies"
	ABILITIES = BACKGROUND_ABILITY_CHOICES["Acolyte"]
	ORIGIN_FEAT = Magic_Initiate_Cleric

	@Imprint
	def awaken(char):
		_awaken(char, Acolyte)


class Artisan(Background):
	NAME = "Artisan"
	TITLE = "Craftsperson"
	DESCRIPTION = (
		"You have connections within craft guilds, allowing you access to "
		"workshops and specialized tools."
		)
	SKILLS = ("Investigation", "Persuasion")
	TOOLS = ARTISAN_TOOLS  # Pick one Artisan's Tools
	ABILITIES = BACKGROUND_ABILITY_CHOICES["Artisan"]
	ORIGIN_FEAT = Crafter

	@Imprint
	def awaken(char):
		_awaken(char, Artisan)


class Charlatan(Background):
	NAME = "Charlatan"
	TITLE = "False Identity"
	DESCRIPTION = (
		"You maintain a convincing second identity, complete with documents, "
		"friends, and disguises."
		)
	SKILLS = ("Deception", "Sleight_of_Hand")
	TOOLS = "Forgery_Kit"
	ABILITIES = BACKGROUND_ABILITY_CHOICES["Charlatan"]
	ORIGIN_FEAT = Skilled

	@Imprint
	def awaken(char):
		_awaken(char, Charlatan)


class Criminal(Background):
	NAME = "Criminal"
	TITLE = "Criminal Contact"
	DESCRIPTION = (
		"You have a reliable contact who acts as a liaison to the criminal "
		"underworld."
		)
	SKILLS = ("Sleight_of_Hand", "Stealth")
	TOOLS = "Thieves_Tools"
	ABILITIES = BACKGROUND_ABILITY_CHOICES["Criminal"]
	ORIGIN_FEAT = Alert

	@Imprint
	def awaken(char):
		_awaken(char, Criminal)


class Entertainer(Background):
	NAME = "Entertainer"
	TITLE = "By Popular Demand"
	DESCRIPTION = (
		"You can always find a place to perform, earning food and lodging "
		"in exchange."
		)
	SKILLS = ("Acrobatics", "Performance")
	TOOLS = "Musical_Instrument"
	ABILITIES = BACKGROUND_ABILITY_CHOICES["Entertainer"]
	ORIGIN_FEAT = Musician

	@Imprint
	def awaken(char):
		_awaken(char, Entertainer)


class Farmer(Background):
	NAME = "Farmer"
	TITLE = "Rustic Hospitality"
	DESCRIPTION = (
		"Common folk gladly offer you food and shelter in exchange for "
		"simple labour."
		)
	SKILLS = ("Animal_Handling", "Nature")
	TOOLS = "Carpenter_Tools"
	ABILITIES = BACKGROUND_ABILITY_CHOICES["Farmer"]
	ORIGIN_FEAT = Tough

	@Imprint
	def awaken(char):
		_awaken(char, Farmer)


class Guard(Background):
	NAME = "Guard"
	TITLE = "Watcher's Eye"
	DESCRIPTION = (
		"You recognise criminals and law-enforcement factions—and they "
		"recognise you."
		)
	SKILLS = ("Athletics", "Perception")
	TOOLS = "Gaming_Set"
	ABILITIES = BACKGROUND_ABILITY_CHOICES["Guard"]
	ORIGIN_FEAT = Alert

	@Imprint
	def awaken(char):
		_awaken(char, Guard)


class Guide(Background):
	NAME = "Guide"
	TITLE = "Pathfinder"
	DESCRIPTION = (
		"You can always find safe routes through the wilderness and locate "
		"food, water, or shelter."
		)
	SKILLS = ("Stealth", "Survival")
	TOOLS = "Cartographer_Tools"
	ABILITIES = BACKGROUND_ABILITY_CHOICES["Guide"]
	ORIGIN_FEAT = Magic_Initiate_Druid

	@Imprint
	def awaken(char):
		_awaken(char, Guide)


class Hermit(Background):
	NAME = "Hermit"
	TITLE = "Discovery"
	DESCRIPTION = (
		"During your isolation you uncovered a unique and powerful secret."
		)
	SKILLS = ("Medicine", "Religion")
	TOOLS = "Herbalism_Kit"
	ABILITIES = BACKGROUND_ABILITY_CHOICES["Hermit"]
	ORIGIN_FEAT = Healer

	@Imprint
	def awaken(char):
		_awaken(char, Hermit)


class Merchant(Background):
	NAME = "Merchant"
	TITLE = "Business Acumen"
	DESCRIPTION = (
		"You can find trade contacts and secure favourable deals, transport, "
		"or information."
		)
	SKILLS = ("Animal_Handling", "Persuasion")
	TOOLS = "Navigator_Tools"
	ABILITIES = BACKGROUND_ABILITY_CHOICES["Merchant"]
	ORIGIN_FEAT = Lucky

	@Imprint
	def awaken(char):
		_awaken(char, Merchant)


class Noble(Background):
	NAME = "Noble"
	TITLE = "Position of Privilege"
	DESCRIPTION = (
		"People of high birth treat you with deference. You have access to "
		"high society."
		)
	SKILLS = ("History", "Persuasion")
	TOOLS = "Gaming_Set"
	ABILITIES = BACKGROUND_ABILITY_CHOICES["Noble"]
	ORIGIN_FEAT = Skilled

	@Imprint
	def awaken(char):
		_awaken(char, Noble)


class Sage(Background):
	NAME = "Sage"
	TITLE = "Researcher"
	DESCRIPTION = (
		"If you don't know a piece of lore, you usually know where to find it."
		)
	SKILLS = ("Arcana", "History")
	TOOLS = "Calligrapher_Supplies"
	ABILITIES = BACKGROUND_ABILITY_CHOICES["Sage"]
	ORIGIN_FEAT = Magic_Initiate_Wizard

	@Imprint
	def awaken(char):
		_awaken(char, Sage)


class Sailor(Background):
	NAME = "Sailor"
	TITLE = "Ship's Passage"
	DESCRIPTION = (
		"You can secure free passage on a vessel for yourself and companions "
		"in exchange for work."
		)
	SKILLS = ("Acrobatics", "Perception")
	TOOLS = "Navigator_Tools"
	ABILITIES = BACKGROUND_ABILITY_CHOICES["Sailor"]
	ORIGIN_FEAT = Tavern_Brawler

	@Imprint
	def awaken(char):
		_awaken(char, Sailor)


class Scribe(Background):
	NAME = "Scribe"
	TITLE = "Scholarly Insight"
	DESCRIPTION = (
		"You have easy access to libraries, archives, and institutions of "
		"knowledge."
		)
	SKILLS = ("Investigation", "Perception")
	TOOLS = "Calligrapher_Supplies"
	ABILITIES = BACKGROUND_ABILITY_CHOICES["Scribe"]
	ORIGIN_FEAT = Skilled

	@Imprint
	def awaken(char):
		_awaken(char, Scribe)


class Soldier(Background):
	NAME = "Soldier"
	TITLE = "Military Rank"
	DESCRIPTION = (
		"Your rank lets you invoke authority in military organisations and "
		"secure aid or shelter."
		)
	SKILLS = ("Athletics", "Intimidation")
	TOOLS = "Gaming_Set"
	ABILITIES = BACKGROUND_ABILITY_CHOICES["Soldier"]
	ORIGIN_FEAT = Savage_Attacker

	@Imprint
	def awaken(char):
		_awaken(char, Soldier)


class Wayfarer(Background):
	"""
	Gold-standard background Tag.

	Class attributes = fixed data (easy to scan).
	Imprint = write attributes + apply Origin Feat Tag.
	"""

	NAME = "Wayfarer"
	TITLE = "Wayfarer"
	DESCRIPTION = (
		"You grew up on the streets among castoffs — some friends, some rivals. "
		"You slept where you could and worked for food; hunger sometimes meant theft. "
		"You kept your pride and your hope."
		)
	SKILLS = ("Insight", "Stealth")
	TOOLS = "Thieves_Tools"
	ABILITIES = BACKGROUND_ABILITY_CHOICES["Wayfarer"]
	ORIGIN_FEAT = Lucky

	@Imprint
	def awaken(char):
		_awaken(char, Wayfarer)


# ---------------------------------------------------------------------------
# Registry — all 16 PHB 2024 backgrounds
# ---------------------------------------------------------------------------

BACKGROUNDS = {
	"Acolyte": Acolyte,
	"Artisan": Artisan,
	"Charlatan": Charlatan,
	"Criminal": Criminal,
	"Entertainer": Entertainer,
	"Farmer": Farmer,
	"Guard": Guard,
	"Guide": Guide,
	"Hermit": Hermit,
	"Merchant": Merchant,
	"Noble": Noble,
	"Sage": Sage,
	"Sailor": Sailor,
	"Scribe": Scribe,
	"Soldier": Soldier,
	"Wayfarer": Wayfarer,
	}


def Apply_Background(char, name=None):
	"""Apply a Background Tag by name (default: char.background)."""
	name = name or getattr(char, "background", None)
	if not name:
		raise ValueError("Apply_Background: no background name")
	tag = BACKGROUNDS.get(name)
	if tag is None:
		raise KeyError(f"BackgroundKit has no Tag for {name!r}")
	if char not in tag:
		tag(char)
	return tag


# ---------------------------------------------------------------------------
# Self-test — also serves as the usage example
# ---------------------------------------------------------------------------

def _test_wayfarer():
	char = Character(seed=21)
	Wayfarer(char)
	assert char in Wayfarer and char in Background
	assert "wayfarer" in char
	assert char.background == "Wayfarer"
	assert char in Lucky
	names = {getattr(f, "name", None) for f in char.features}
	assert "Wayfarer" in names
	assert "Lucky" in names
	assert all(isinstance(f, Feature) for f in char.features if f.name in names)


def _test_acolyte():
	char = Character(seed=22)
	Acolyte(char)
	assert char in Acolyte
	assert char.background == "Acolyte"
	assert char in Magic_Initiate_Cleric


def _test_all_backgrounds():
	"""Every PHB 2024 background Tag awakens with its Origin Feat."""
	assert set(BACKGROUNDS) == set(BACKGROUND_ORIGIN_FEATS)
	assert set(BACKGROUNDS) == set(BACKGROUND_ABILITY_CHOICES)
	for i, (name, tag) in enumerate(BACKGROUNDS.items()):
		char = Character(seed=100 + i)
		tag(char)
		assert char in tag and char in Background
		assert char.background == name
		assert char in tag.ORIGIN_FEAT
		assert tag.ORIGIN_FEAT is BACKGROUND_ORIGIN_FEATS[name]
		assert tag.ABILITIES == BACKGROUND_ABILITY_CHOICES[name]
		assert len(tag.SKILLS) == 2
		assert getattr(tag, "TOOLS", None)


def _test_ability_boost_soft_opt():
	"""Odd scores + class prefs steer picks (recalled soft optimizer)."""
	char = Character(seed=24)
	char.char_class = "Rogue"

	class FakeAS:
		STR, DEX, CON, INT, WIS, CHA = 10, 15, 12, 11, 13, 14

	char.AS = FakeAS()
	assert _pick_boost_ability(char, ["DEX", "CHA", "WIS"], char.AS) == "DEX"
	assert _pick_boost_ability(char, ["CHA", "WIS"], char.AS) == "WIS"
	char.char_class = "Wizard"
	assert _pick_boost_ability(char, ["INT", "CON"], char.AS) == "INT"
	before = (char.AS.STR, char.AS.DEX, char.AS.CON, char.AS.INT, char.AS.WIS, char.AS.CHA)
	_grant_ability_boosts(char, ("DEX", "CHA", "WIS"))
	after = (char.AS.STR, char.AS.DEX, char.AS.CON, char.AS.INT, char.AS.WIS, char.AS.CHA)
	assert after[0] == before[0] and after[2] == before[2] and after[3] == before[3]
	assert sum(a - b for a, b in zip(after, before)) == 3


def _test_apply_by_name():
	char = Character(seed=23)
	char.background = "Soldier"
	Apply_Background(char)
	assert char in Soldier and char in Savage_Attacker


def _self_test():
	_test_wayfarer()
	_test_acolyte()
	_test_all_backgrounds()
	_test_ability_boost_soft_opt()
	_test_apply_by_name()
	for name, tag in BACKGROUNDS.items():
		assert tag.ORIGIN_FEAT is BACKGROUND_ORIGIN_FEATS[name]
	print("OK — BackgroundKit self-test (16 backgrounds)")


if __name__ == "__main__":
	_self_test()
