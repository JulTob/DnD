"""
BackgroundKit

One declarative construction point for every TOP Background.

Background Tags own their abilities, training, Origin Feature, narrative
Entry, and role eligibility. Pins classify each Background Tag directly:

    background_tag in Available
    background_tag in NPC_Background

The Pin Fields derive every public registry.  Adding a homebrew
Background therefore requires one ``Build_Background`` call and no parallel
choice lists.
"""

from __future__ import annotations

from collections.abc import Iterator, Mapping
from typing import Iterable

from TagKit import Action, Imprint, Pre, Report, Tag, Underlay

from AtlasActorLudi.CharactersKit import (
	Character,
	NonPlayer,
	Player,
	)
from AtlasActorLudi.Grimoire_of_AbilityScores import AbilityScores
from AtlasActorLudi.Grimoire_of_Skills import Char_Skills
from AtlasLusoris.AtlasOfBackgrounds import (
	Register_Official_2024_Backgrounds,
	)
from AtlasLusoris.AtlasOfFeatures import BACKGROUND_ORIGIN_FEATS
from AtlasLusoris.FeaturesKit import (
	Alert,
	CORE_SKILLS,
	Crafter as Crafter_Feature,
	Healer as Healer_Feature,
	Lucky,
	Magic_Initiate_Cleric,
	Magic_Initiate_Druid,
	Magic_Initiate_Wizard,
	Musician,
	Origin_Feat,
	Savage_Attacker,
	Skilled,
	Tavern_Brawler,
	Tough,
	grant,
	)
from AtlasLusoris.GuildKit import guild_ability_prefs


_ALL_ABILITIES = (
	"STR",
	"DEX",
	"CON",
	"INT",
	"WIS",
	"CHA",
	)

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


# ---------------------------------------------------------------------------
# Character Background Tags
# ---------------------------------------------------------------------------


class Background(Tag):
	"""Root Tag for exactly one Character Background."""

	NAME = "Background"

	@Pre
	def Character_Only(
		target,
		):
		return isinstance(
			target,
			Character,
			)

	@Pre
	def Single_Background(
		target,
		):
		return sum(
			target in tag
			for tag in globals().get(
				"BACKGROUNDS",
				{},
				).values()
			) <= 1

	@Imprint
	def Ensure_Feature_Bag(
		target,
		):
		if getattr(
			target,
			"features",
			None,
			) is None:
			target.features = []

	@Action
	@Underlay
	def __format__(
			target,
			prior,
			specification,
			):
		"""Render Background from current Tag membership."""
		if specification.strip().casefold() == "background":
			return Find_Background( target )

		return prior( specification )

# ---------------------------------------------------------------------------
# Pins for Background Tags
# ---------------------------------------------------------------------------


class Background_Audience(Tag):
	"""Root Pin classifying Background Tags by Character Role."""

	NAME = "Background Audience"

	@Pre
	def Background_Tag_Only(
		target,
		):
		return (
			isinstance(
				target,
				type,
				)
			and issubclass(
				target,
				Background,
				)
			)


class Available(Background_Audience):
	"""Pin for Backgrounds available to Player Characters."""

	NAME = "Available"


class NPC_Background(Background_Audience):
	"""Pin for Backgrounds available to NonPlayer Characters."""

	NAME = "NPC Background"


def _class_name(
	name: str,
	) -> str:
	safe_name = "".join(
		character
		if character.isalnum()
		else "_"
		for character in name
		)

	if not safe_name:
		raise ValueError(
			"A Background requires a non-empty semantic name."
			)

	if safe_name[0].isdigit():
		safe_name = f"Background_{safe_name}"

	return safe_name


def _validate_background_construction(
	*,
	name: str,
	audiences: tuple[type[Background_Audience], ...],
	abilities: tuple[str, str, str],
	skills: tuple[str, str],
	tools: str | tuple[str, ...],
	origin_feat: type[Origin_Feat],
	title: str,
	description: str,
	origin_feat_options: tuple[str, ...],
	source_title: str,
	source_url: str,
	source_locator: str,
	source_kind: str,
	) -> None:
	if (
		not isinstance(
			name,
			str,
			)
		or not name.strip()
		):
		raise ValueError(
			"A Background requires a non-empty name."
			)

	if any(
		tag.NAME.casefold() == name.casefold()
		for tag in Background_Audience[:]
		):
		raise ValueError(
			f"Background {name!r} is already declared."
			)

	if (
		not audiences
		or any(
			audience not in (
				Available,
				NPC_Background,
				)
			for audience in audiences
			)
		):
		raise ValueError(
			f"Background {name!r} requires a PC and/or NPC audience."
			)

	if (
		len(
			set(
				abilities
				)
			) != 3
		or any(
			ability not in _ALL_ABILITIES
			for ability in abilities
			)
		):
		raise ValueError(
			f"Background {name!r} requires three distinct valid abilities."
			)

	if (
		len(
			skills
			) != 2
		or len(
			set(
				skills
				)
			) != 2
		or any(
			skill not in CORE_SKILLS
			for skill in skills
			)
		):
		raise ValueError(
			f"Background {name!r} requires two distinct canonical skills."
			)

	if (
		not tools
		or (
			isinstance(
				tools,
				str,
				)
			and not tools.strip()
			)
		or (
			isinstance(
				tools,
				tuple,
				)
			and not all(
				isinstance(
					tool,
					str,
					)
				and tool.strip()
				for tool in tools
				)
			)
		or not isinstance(
			tools,
			(
				str,
				tuple,
				),
			)
		):
		raise ValueError(
			f"Background {name!r} requires at least one valid tool."
			)

	if (
		not isinstance(
			origin_feat,
			type,
			)
		or not issubclass(
			origin_feat,
			Origin_Feat,
			)
		):
		raise TypeError(
			f"Background {name!r} requires an Origin Feature Tag."
			)

	if (
		origin_feat_options
		and (
			origin_feat.NAME not in origin_feat_options
			or any(
				not isinstance(
					option,
					str,
					)
				or not option.strip()
				for option in origin_feat_options
				)
			)
		):
		raise ValueError(
			f"Background {name!r} has invalid Origin Feature options."
			)

	if (
		not isinstance(
			title,
			str,
			)
		or not title.strip()
		or not isinstance(
			description,
			str,
			)
		or not description.strip()
		):
		raise ValueError(
			f"Background {name!r} requires a title and description."
			)

	if (
		not isinstance(
			source_title,
			str,
			)
		or not source_title.strip()
		or not isinstance(
			source_kind,
			str,
			)
		or not source_kind.strip()
		or not isinstance(
			source_url,
			str,
			)
		or not isinstance(
			source_locator,
			str,
			)
		):
		raise ValueError(
			f"Background {name!r} requires valid source metadata."
			)


def _eligible_for(
	target,
	tag: type[Background],
	) -> bool:
	return (
		target in Player
		and tag in Available
		) or (
			target in NonPlayer
			and tag in NPC_Background
			)


# ---------------------------------------------------------------------------
# Shared application modules
# ---------------------------------------------------------------------------


def _pick_boost_ability(
	char,
	pool,
	scores,
	):
	"""Prefer odd scores and the Character's Guild abilities."""
	primary, secondary = guild_ability_prefs(
		char
		)

	def priority(
		key,
		):
		if key == primary:
			return 0

		if key == secondary:
			return 1

		return 2

	def rank(
		key,
		):
		value = (
			getattr(
				scores,
				key,
				)
			if scores is not None
			else 10
			)

		return (
			value % 2 == 0,
			priority(
				key
				),
			-value,
			)

	best = min(
		rank(
			key
			)
		for key in pool
		)
	tied = [
		key
		for key in pool
		if rank(
			key
			) == best
		]

	return (
		char.Pick(
			tied
			)
		if len(
			tied
			) > 1
		else tied[0]
		)


def _grant_ability_boosts(
	char,
	abilities=None,
	):
	"""Apply one Background's +2/+1 or +1/+1/+1 ability pattern."""
	if abilities is None:
		name = getattr(
			char,
			"background",
			None,
			)
		tag = BACKGROUNDS.get(
			name
			)

		if tag is None:
			raise ValueError(
				"Ability boosts require a declared Background Tag."
				)

		abilities = tag.ABILITIES

	pattern = char.Pick(
		[
			(
				2,
				1,
				),
			(
				1,
				1,
				1,
				),
			]
		)
	pool = list(
		abilities
		)
	scores = getattr(
		char,
		"AS",
		None,
		)

	if (
		scores is not None
		and not isinstance(
			scores,
			AbilityScores,
			)
		):
		scores = None

	chosen = []
	remaining = list(
		pool
		)

	for bonus in sorted(
		pattern,
		reverse=True,
		):
		stat = _pick_boost_ability(
			char,
			remaining,
			scores,
			)
		remaining.remove(
			stat
			)
		chosen.append(
			(
				stat,
				bonus,
				)
			)

	if scores is None:
		char.background_asi = chosen
		return

	for stat, bonus in chosen:
		setattr(
			scores,
			stat,
			getattr(
				scores,
				stat,
				)
			+ bonus,
			)


def _grant_skills(
	char,
	skill_names,
	):
	skills = getattr(
		char,
		"skills",
		None,
		)

	if not isinstance(
		skills,
		Char_Skills,
		):
		char.background_skills = list(
			skill_names
			)
		return

	for name in skill_names:
		skill = getattr(
			skills,
			name,
			None,
			)

		if (
			skill is not None
			and hasattr(
				skill,
				"set_proficiency",
				)
			):
			skill.set_proficiency()


def _grant_tool(
	char,
	tools,
	):
	if not tools:
		return

	pick = (
		char.Pick(
			list(
				tools
				)
			)
		if isinstance(
			tools,
			(
				tuple,
				list,
				),
			)
		else tools
		)
	skills = getattr(
		char,
		"skills",
		None,
		)

	if not isinstance(
		skills,
		Char_Skills,
		):
		char.background_tool = pick
		return

	skill = getattr(
		skills,
		pick,
		None,
		)

	if (
		skill is not None
		and hasattr(
			skill,
			"set_proficiency",
			)
		):
		skill.set_proficiency()


def _grant_narrative(
	char,
	title: str,
	description: str,
	):
	grant(
		char,
		name=title,
		description=description,
		source="Background",
		)


def _awaken(
	char,
	tag,
	):
	"""Apply the common modules owned by one Background Tag."""
	char.background = tag.NAME
	_grant_ability_boosts(
		char,
		tag.ABILITIES,
		)
	_grant_skills(
		char,
		tag.SKILLS,
		)
	_grant_tool(
		char,
		tag.TOOLS,
		)
	_grant_narrative(
		char,
		tag.TITLE,
		tag.DESCRIPTION,
		)


def Build_Background(
	*,
	name: str,
	audiences: Iterable[type[Background_Audience]],
	abilities: tuple[str, str, str],
	skills: tuple[str, str],
	tools: str | tuple[str, ...],
	origin_feat: type[Origin_Feat],
	title: str,
	description: str,
	origin_feat_options: tuple[str, ...] = (),
	source_title: str = "Project Original",
	source_url: str = "",
	source_locator: str = "",
	source_kind: str = "project-original",
	) -> type[Background]:
	"""Construct one complete Background Shape and apply its Pins."""
	resolved_audiences = tuple(
		dict.fromkeys(
			audiences
			)
		)
	resolved_abilities = tuple(
		abilities
		)
	resolved_skills = tuple(
		skills
		)
	resolved_tools = (
		tuple(
			tools
			)
		if isinstance(
			tools,
			list,
			)
		else tools
		)
	resolved_origin_feat_options = (
		tuple(
			origin_feat_options
			)
		or (
			origin_feat.NAME,
			)
		)

	_validate_background_construction(
		name=name,
		audiences=resolved_audiences,
		abilities=resolved_abilities,
		skills=resolved_skills,
		tools=resolved_tools,
		origin_feat=origin_feat,
		title=title,
		description=description,
		origin_feat_options=resolved_origin_feat_options,
		source_title=source_title,
		source_url=source_url,
		source_locator=source_locator,
		source_kind=source_kind,
		)

	background_tag = None

	@Pre
	def Eligible_Role(
		target,
		):
		return _eligible_for(
			target,
			background_tag,
			)

	@Imprint
	def Awaken(
		target,
		):
		_awaken(
			target,
			background_tag,
			)

	background_tag = type(
		_class_name(
			name
			),
		(
			Background,
			origin_feat,
			),
		{
			"NAME": name,
			"TITLE": Report(
				title
				),
			"DESCRIPTION": Report(
				description
				),
			"ABILITIES": Report(
				resolved_abilities
				),
			"SKILLS": Report(
				resolved_skills
				),
			"TOOLS": Report(
				resolved_tools
				),
			"ORIGIN_FEAT": Report(
				origin_feat
				),
			"ORIGIN_FEAT_OPTIONS": Report(
				resolved_origin_feat_options
				),
			"SOURCE_TITLE": Report(
				source_title
				),
			"SOURCE_URL": Report(
				source_url
				),
			"SOURCE_LOCATOR": Report(
				source_locator
				),
			"SOURCE_KIND": Report(
				source_kind
				),
			"Eligible_Role": Eligible_Role,
			"Awaken": Awaken,
			"__module__": __name__,
			},
		)

	for audience in resolved_audiences:
		audience(
			background_tag
			)

	return background_tag


# ---------------------------------------------------------------------------
# Shared 2024 Player's Handbook Backgrounds
# ---------------------------------------------------------------------------


def _Build_Player_Handbook_Background(
		**record,
		) -> type[Background]:
	return Build_Background(
		source_title="Player's Handbook (2024)",
		source_url="https://www.dndbeyond.com/sources/dnd/phb-2024",
		source_locator="Chapter 4: Character Origins — Background Descriptions",
		source_kind="official-reference",
		**record,
		)


Acolyte = _Build_Player_Handbook_Background(
	name="Acolyte",
	audiences=(
		Available,
		NPC_Background,
		),
	abilities=(
		"INT",
		"WIS",
		"CHA",
		),
	skills=(
		"Insight",
		"Religion",
		),
	tools="Calligrapher_Supplies",
	origin_feat=Magic_Initiate_Cleric,
	title="Shelter of the Faithful",
	description=(
		"You and your companions can expect healing and care from communities "
		"that share your faith."
		),
	)

Artisan = _Build_Player_Handbook_Background(
	name="Artisan",
	audiences=(
		Available,
		NPC_Background,
		),
	abilities=(
		"STR",
		"DEX",
		"INT",
		),
	skills=(
		"Investigation",
		"Persuasion",
		),
	tools=ARTISAN_TOOLS,
	origin_feat=Crafter_Feature,
	title="Craftsperson",
	description=(
		"You have craft-guild connections and practical access to workshops, "
		"materials, and specialist knowledge."
		),
	)

Charlatan = _Build_Player_Handbook_Background(
	name="Charlatan",
	audiences=(
		Available,
		NPC_Background,
		),
	abilities=(
		"DEX",
		"CON",
		"CHA",
		),
	skills=(
		"Deception",
		"Sleight_of_Hand",
		),
	tools="Forgery_Kit",
	origin_feat=Skilled,
	title="False Identity",
	description=(
		"You maintain a convincing second identity supported by practiced "
		"mannerisms, documents, and useful acquaintances."
		),
	)

Criminal = _Build_Player_Handbook_Background(
	name="Criminal",
	audiences=(
		Available,
		NPC_Background,
		),
	abilities=(
		"DEX",
		"CON",
		"INT",
		),
	skills=(
		"Sleight_of_Hand",
		"Stealth",
		),
	tools="Thieves_Tools",
	origin_feat=Alert,
	title="Criminal Contact",
	description=(
		"You know how to reach people who trade in secrets, contraband, and "
		"quietly solved problems."
		),
	)

Entertainer = _Build_Player_Handbook_Background(
	name="Entertainer",
	audiences=(
		Available,
		NPC_Background,
		),
	abilities=(
		"STR",
		"DEX",
		"CHA",
		),
	skills=(
		"Acrobatics",
		"Performance",
		),
	tools="Musical_Instrument",
	origin_feat=Musician,
	title="By Popular Demand",
	description=(
		"You can usually earn food, lodging, and local attention through a "
		"well-judged performance."
		),
	)

Farmer = _Build_Player_Handbook_Background(
	name="Farmer",
	audiences=(
		Available,
		NPC_Background,
		),
	abilities=(
		"STR",
		"CON",
		"WIS",
		),
	skills=(
		"Animal_Handling",
		"Nature",
		),
	tools="Carpenter_Tools",
	origin_feat=Tough,
	title="Rustic Hospitality",
	description=(
		"Working communities recognize your practical experience and often "
		"offer simple aid in exchange for honest labour."
		),
	)

Guard = _Build_Player_Handbook_Background(
	name="Guard",
	audiences=(
		Available,
		NPC_Background,
		),
	abilities=(
		"STR",
		"INT",
		"WIS",
		),
	skills=(
		"Athletics",
		"Perception",
		),
	tools="Gaming_Set",
	origin_feat=Alert,
	title="Watcher's Eye",
	description=(
		"You recognize the habits of lawkeepers and lawbreakers, and they "
		"often recognize your bearing in return."
		),
	)

Guide = _Build_Player_Handbook_Background(
	name="Guide",
	audiences=(
		Available,
		NPC_Background,
		),
	abilities=(
		"DEX",
		"CON",
		"WIS",
		),
	skills=(
		"Stealth",
		"Survival",
		),
	tools="Cartographer_Tools",
	origin_feat=Magic_Initiate_Druid,
	title="Pathfinder",
	description=(
		"You read terrain, weather, and tracks well enough to find safer "
		"routes and the necessities of travel."
		),
	)

Hermit = _Build_Player_Handbook_Background(
	name="Hermit",
	audiences=(
		Available,
		NPC_Background,
		),
	abilities=(
		"CON",
		"WIS",
		"CHA",
		),
	skills=(
		"Medicine",
		"Religion",
		),
	tools="Herbalism_Kit",
	origin_feat=Healer_Feature,
	title="Discovery",
	description=(
		"Solitude gave you time to uncover a truth, method, or mystery that "
		"still shapes your decisions."
		),
	)

Merchant = _Build_Player_Handbook_Background(
	name="Merchant",
	audiences=(
		Available,
		NPC_Background,
		),
	abilities=(
		"CON",
		"INT",
		"CHA",
		),
	skills=(
		"Animal_Handling",
		"Persuasion",
		),
	tools="Navigator_Tools",
	origin_feat=Lucky,
	title="Business Acumen",
	description=(
		"You can find trade contacts and negotiate transport, information, "
		"supplies, or a more favorable bargain."
		),
	)

Noble = _Build_Player_Handbook_Background(
	name="Noble",
	audiences=(
		Available,
		NPC_Background,
		),
	abilities=(
		"STR",
		"INT",
		"CHA",
		),
	skills=(
		"History",
		"Persuasion",
		),
	tools="Gaming_Set",
	origin_feat=Skilled,
	title="Position of Privilege",
	description=(
		"Your name, education, or bearing grants access to circles where rank "
		"and reputation carry practical weight."
		),
	)

Sage = _Build_Player_Handbook_Background(
	name="Sage",
	audiences=(
		Available,
		NPC_Background,
		),
	abilities=(
		"CON",
		"INT",
		"WIS",
		),
	skills=(
		"Arcana",
		"History",
		),
	tools="Calligrapher_Supplies",
	origin_feat=Magic_Initiate_Wizard,
	title="Researcher",
	description=(
		"When you do not know a piece of lore, you usually know which archive, "
		"expert, or tradition might hold it."
		),
	)

Sailor = _Build_Player_Handbook_Background(
	name="Sailor",
	audiences=(
		Available,
		NPC_Background,
		),
	abilities=(
		"STR",
		"DEX",
		"WIS",
		),
	skills=(
		"Acrobatics",
		"Perception",
		),
	tools="Navigator_Tools",
	origin_feat=Tavern_Brawler,
	title="Ship's Passage",
	description=(
		"Your knowledge of vessels and crews can secure passage or work when "
		"a suitable ship and captain are available."
		),
	)

Scribe = _Build_Player_Handbook_Background(
	name="Scribe",
	audiences=(
		Available,
		NPC_Background,
		),
	abilities=(
		"DEX",
		"INT",
		"WIS",
		),
	skills=(
		"Investigation",
		"Perception",
		),
	tools="Calligrapher_Supplies",
	origin_feat=Skilled,
	title="Scholarly Insight",
	description=(
		"You understand records, libraries, and institutions well enough to "
		"locate documents and recognize suspicious omissions."
		),
	)

Soldier = _Build_Player_Handbook_Background(
	name="Soldier",
	audiences=(
		Available,
		NPC_Background,
		),
	abilities=(
		"STR",
		"DEX",
		"CON",
		),
	skills=(
		"Athletics",
		"Intimidation",
		),
	tools="Gaming_Set",
	origin_feat=Savage_Attacker,
	title="Military Rank",
	description=(
		"Your service and bearing can earn recognition, shelter, or limited "
		"cooperation from military organizations."
		),
	)

Wayfarer = _Build_Player_Handbook_Background(
	name="Wayfarer",
	audiences=(
		Available,
		NPC_Background,
		),
	abilities=(
		"DEX",
		"WIS",
		"CHA",
		),
	skills=(
		"Insight",
		"Stealth",
		),
	tools="Thieves_Tools",
	origin_feat=Lucky,
	title="Wayfarer",
	description=(
		"You survived through observation, odd jobs, quick decisions, and the "
		"refusal to surrender your hope to difficult circumstances."
		),
	)


# ---------------------------------------------------------------------------
# Actualized former Archetypes: full NonPlayer Backgrounds
# ---------------------------------------------------------------------------


Artist = Build_Background(
	name="Artist",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"DEX",
		"WIS",
		"CHA",
		),
	skills=(
		"Insight",
		"Performance",
		),
	tools="Painter_Supplies",
	origin_feat=Musician,
	title="Expressive Eye",
	description=(
		"You notice telling details and turn them into performances or works "
		"that move an audience."
		),
	)

Bandit = Build_Background(
	name="Bandit",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"STR",
		"DEX",
		"CHA",
		),
	skills=(
		"Intimidation",
		"Stealth",
		),
	tools="Thieves_Tools",
	origin_feat=Alert,
	title="Roadside Instinct",
	description=(
		"You understand ambush sites, frightened travelers, hidden camps, and "
		"the shifting loyalties of an outlaw company."
		),
	)

Berserker = Build_Background(
	name="Berserker",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"STR",
		"CON",
		"WIS",
		),
	skills=(
		"Athletics",
		"Intimidation",
		),
	tools="Gaming_Set",
	origin_feat=Tavern_Brawler,
	title="Fury Tempered",
	description=(
		"You learned to survive violent confrontations by committing fully "
		"when hesitation would be fatal."
		),
	)

Commoner = Build_Background(
	name="Commoner",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"STR",
		"CON",
		"WIS",
		),
	skills=(
		"Animal_Handling",
		"Insight",
		),
	tools="Carpenter_Tools",
	origin_feat=Tough,
	title="Local Roots",
	description=(
		"You know the rhythms, favors, worries, and practical work that hold "
		"an ordinary community together."
		),
	)

Crafter = Build_Background(
	name="Crafter",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"DEX",
		"INT",
		"WIS",
		),
	skills=(
		"Investigation",
		"Sleight_of_Hand",
		),
	tools=ARTISAN_TOOLS,
	origin_feat=Crafter_Feature,
	title="Practiced Hands",
	description=(
		"You diagnose material problems quickly and know how to repair, alter, "
		"or reproduce useful objects."
		),
	)

Cultist = Build_Background(
	name="Cultist",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"INT",
		"WIS",
		"CHA",
		),
	skills=(
		"Deception",
		"Religion",
		),
	tools="Disguise_Kit",
	origin_feat=Magic_Initiate_Cleric,
	title="Secret Doctrine",
	description=(
		"You know the signs, passwords, rituals, and hidden hierarchies of a "
		"secretive faith or forbidden cause."
		),
	)

Doctor = Build_Background(
	name="Doctor",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"INT",
		"WIS",
		"CHA",
		),
	skills=(
		"Investigation",
		"Medicine",
		),
	tools="Herbalism_Kit",
	origin_feat=Healer_Feature,
	title="Clinical Practice",
	description=(
		"You assess symptoms methodically, stabilize patients, and recognize "
		"when an injury or illness has an unusual cause."
		),
	)

Expert = Build_Background(
	name="Expert",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"DEX",
		"INT",
		"WIS",
		),
	skills=(
		"Insight",
		"Investigation",
		),
	tools=ARTISAN_TOOLS,
	origin_feat=Skilled,
	title="Specialist",
	description=(
		"Long practice in a narrow discipline lets you recognize fine details "
		"and solve problems others overlook."
		),
	)

Explorer = Build_Background(
	name="Explorer",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"DEX",
		"CON",
		"WIS",
		),
	skills=(
		"Perception",
		"Survival",
		),
	tools="Cartographer_Tools",
	origin_feat=Alert,
	title="Beyond the Map",
	description=(
		"You are accustomed to uncertain routes, incomplete maps, changing "
		"weather, and discoveries that reward careful preparation."
		),
	)

Guardian = Build_Background(
	name="Guardian",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"STR",
		"CON",
		"WIS",
		),
	skills=(
		"Athletics",
		"Perception",
		),
	tools="Gaming_Set",
	origin_feat=Tough,
	title="Watchful Charge",
	description=(
		"You have accepted responsibility for a person, place, threshold, or "
		"tradition and remain alert to dangers around it."
		),
	)

Healer = Build_Background(
	name="Healer",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"INT",
		"WIS",
		"CHA",
		),
	skills=(
		"Insight",
		"Medicine",
		),
	tools="Herbalism_Kit",
	origin_feat=Healer_Feature,
	title="Restorative Care",
	description=(
		"You combine practical treatment with an understanding of fear, pain, "
		"and the patience recovery often demands."
		),
	)

Hero = Build_Background(
	name="Hero",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"STR",
		"CON",
		"CHA",
		),
	skills=(
		"Athletics",
		"Persuasion",
		),
	tools="Gaming_Set",
	origin_feat=Lucky,
	title="Local Legend",
	description=(
		"A remembered deed made you a symbol to a community, whether or not "
		"you feel worthy of the story now told about you."
		),
	)

Hunter = Build_Background(
	name="Hunter",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"DEX",
		"CON",
		"WIS",
		),
	skills=(
		"Perception",
		"Survival",
		),
	tools="Leatherworker_Tools",
	origin_feat=Alert,
	title="Patient Pursuit",
	description=(
		"You read spoor, habits, terrain, and silence to follow quarry without "
		"wasting movement or revealing your approach."
		),
	)

Knight = Build_Background(
	name="Knight",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"STR",
		"CON",
		"CHA",
		),
	skills=(
		"Athletics",
		"Persuasion",
		),
	tools="Gaming_Set",
	origin_feat=Savage_Attacker,
	title="Sworn Service",
	description=(
		"An oath, patron, or martial order grants you recognizable duties and "
		"a place within a wider chain of obligation."
		),
	)

Mage = Build_Background(
	name="Mage",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"INT",
		"WIS",
		"CHA",
		),
	skills=(
		"Arcana",
		"Investigation",
		),
	tools="Calligrapher_Supplies",
	origin_feat=Magic_Initiate_Wizard,
	title="Arcane Practice",
	description=(
		"You learned magic through fragmented study, service, inheritance, or "
		"another path outside a formal adventuring Guild."
		),
	)

Mentor = Build_Background(
	name="Mentor",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"INT",
		"WIS",
		"CHA",
		),
	skills=(
		"Insight",
		"Persuasion",
		),
	tools="Calligrapher_Supplies",
	origin_feat=Skilled,
	title="Guiding Hand",
	description=(
		"You recognize developing talent and know how to turn experience into "
		"questions, exercises, warnings, and useful encouragement."
		),
	)

Ninja = Build_Background(
	name="Ninja",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"DEX",
		"INT",
		"WIS",
		),
	skills=(
		"Acrobatics",
		"Stealth",
		),
	tools="Poisoners_Kit",
	origin_feat=Alert,
	title="Hidden Discipline",
	description=(
		"You trained to enter guarded places, observe without notice, and act "
		"with precision before an alarm can spread."
		),
	)

Pirate = Build_Background(
	name="Pirate",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"STR",
		"DEX",
		"CHA",
		),
	skills=(
		"Acrobatics",
		"Intimidation",
		),
	tools="Navigator_Tools",
	origin_feat=Tavern_Brawler,
	title="Freebooter's Reputation",
	description=(
		"You understand unruly crews, dangerous ports, divided prizes, and "
		"the value of a reputation that arrives before the ship."
		),
	)

Priest = Build_Background(
	name="Priest",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"INT",
		"WIS",
		"CHA",
		),
	skills=(
		"Insight",
		"Religion",
		),
	tools="Calligrapher_Supplies",
	origin_feat=Magic_Initiate_Cleric,
	title="Pastoral Office",
	description=(
		"You conduct rites, preserve doctrine, and help a community interpret "
		"its obligations, griefs, celebrations, and hopes."
		),
	)

Scholar = Build_Background(
	name="Scholar",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"INT",
		"WIS",
		"CHA",
		),
	skills=(
		"Arcana",
		"History",
		),
	tools="Calligrapher_Supplies",
	origin_feat=Skilled,
	title="Learned Correspondence",
	description=(
		"You exchange findings with other specialists and know how to compare "
		"sources, claims, translations, and competing schools of thought."
		),
	)

Shaman = Build_Background(
	name="Shaman",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"CON",
		"WIS",
		"CHA",
		),
	skills=(
		"Animal_Handling",
		"Nature",
		),
	tools="Herbalism_Kit",
	origin_feat=Magic_Initiate_Druid,
	title="Spirit Mediator",
	description=(
		"You interpret signs and maintain practical relationships between a "
		"community, its land, its ancestors, and unseen presences."
		),
	)

Spy = Build_Background(
	name="Spy",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"DEX",
		"INT",
		"CHA",
		),
	skills=(
		"Deception",
		"Stealth",
		),
	tools="Disguise_Kit",
	origin_feat=Skilled,
	title="Network of Whispers",
	description=(
		"You cultivate sources, conceal your purpose, and understand how a "
		"small observation becomes useful intelligence."
		),
	)

Trickster = Build_Background(
	name="Trickster",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"DEX",
		"INT",
		"CHA",
		),
	skills=(
		"Deception",
		"Sleight_of_Hand",
		),
	tools="Disguise_Kit",
	origin_feat=Lucky,
	title="Misdirection",
	description=(
		"You redirect attention with timing, confidence, and a practiced sense "
		"of what an observer expects to see."
		),
	)

Traveler = Build_Background(
	name="Traveler",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"DEX",
		"CON",
		"WIS",
		),
	skills=(
		"Insight",
		"Survival",
		),
	tools="Navigator_Tools",
	origin_feat=Lucky,
	title="Roadwise",
	description=(
		"You adapt quickly to unfamiliar customs, temporary shelter, uncertain "
		"roads, and the small negotiations every journey requires."
		),
	)

Warrior = Build_Background(
	name="Warrior",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"STR",
		"DEX",
		"CON",
		),
	skills=(
		"Athletics",
		"Intimidation",
		),
	tools="Gaming_Set",
	origin_feat=Savage_Attacker,
	title="Battle Proven",
	description=(
		"You learned violence through service, necessity, or tradition and can "
		"read the mood and readiness of other fighting people."
		),
	)

Witch = Build_Background(
	name="Witch",
	audiences=(
		NPC_Background,
		),
	abilities=(
		"INT",
		"WIS",
		"CHA",
		),
	skills=(
		"Arcana",
		"Nature",
		),
	tools="Herbalism_Kit",
	origin_feat=Magic_Initiate_Wizard,
	title="Hedge Mysteries",
	description=(
		"You preserve a personal body of charms, remedies, warnings, and "
		"unsettling lore learned beyond formal institutions."
		),
	)


# ---------------------------------------------------------------------------
# Later official 2024-format source Maps
# ---------------------------------------------------------------------------


OFFICIAL_2024_BACKGROUNDS = Register_Official_2024_Backgrounds(
	build_background=Build_Background,
	pc_background=Available,
	npc_background=NPC_Background,
	artisan_tools=ARTISAN_TOOLS,
	origin_feats=BACKGROUND_ORIGIN_FEATS,
	)

globals().update(
	{
		tag.__name__: tag
		for tag in OFFICIAL_2024_BACKGROUNDS
		}
	)


# ---------------------------------------------------------------------------
# Field-derived registries
# ---------------------------------------------------------------------------


class Background_Registry(
	Mapping[
		str,
		type[Background],
	],
	):
	"""Live read-only view over Background Pin Fields."""

	def __init__(
			registry,
			*,
			source: type[Background_Audience] | None = None,
			required: tuple[type[Background_Audience], ...] = (),
			excluded: tuple[type[Background_Audience], ...] = (),
			):
		registry.source = source
		registry.required = required
		registry.excluded = excluded

	def _tags(
			registry,
			) -> tuple[type[Background], ...]:
		candidates = (
			tuple(
				registry.source[:]
				)
			if registry.source is not None
			else tuple(
				Background_Audience[:]
				)
			)

		return tuple(
			tag
			for tag in candidates
			if all(
				tag in audience
				for audience in registry.required
				)
			and all(
				tag not in audience
				for audience in registry.excluded
				)
			)

	def __getitem__(
			registry,
			name: str,
			) -> type[Background]:
		for tag in registry._tags():
			if tag.NAME == name:
				return tag

		raise KeyError(
			name
			)

	def __iter__(
			registry,
			) -> Iterator[str]:
		return (
			tag.NAME
			for tag in registry._tags()
			)

	def __len__(
			registry,
			) -> int:
		return len(
			registry._tags()
			)


def Backgrounds_For(
	audience: type[Background_Audience],
	):
	"""Return a live read-only registry derived from one audience Field."""
	if audience not in (
		Available,
		NPC_Background,
		):
		raise ValueError(
			"Backgrounds_For requires Available or NPC_Background."
			)

	return Background_Registry(
		source=audience
		)


PLAYER_BACKGROUNDS = Backgrounds_For(
	Available
	)
NONPLAYER_BACKGROUNDS = Backgrounds_For(
	NPC_Background
	)
SHARED_BACKGROUNDS = Background_Registry(
	source=Available,
	required=(
		NPC_Background,
		),
	)
NONPLAYER_ONLY_BACKGROUNDS = Background_Registry(
	source=NPC_Background,
	excluded=(
		Available,
		),
	)
NONPLAYER_ONLY_BACKGROUND_NAMES = tuple(
	NONPLAYER_ONLY_BACKGROUNDS
	)
BACKGROUNDS = Background_Registry(
	source=Background_Audience
	)


def Find_Background(
		target,
		) -> str:
	"""Find the narrative Background label from current Tag membership."""
	carried = tuple(
		tag
		for tag in BACKGROUNDS.values()
		if target in tag
		)

	if len( carried ) > 1:
		raise ValueError(
			"A Character carries conflicting Backgrounds: "
			+ ", ".join(
				tag.NAME
				for tag in carried
				)
			+ "."
			)

	return (
		carried[ 0 ].NAME
		if carried
		else ""
		)


def Background_Is_Available(
	char,
	tag,
	) -> bool:
	"""Return whether the Character Role matches a Pin on the Background Tag."""
	if (
		not isinstance(
			tag,
			type,
			)
		or not issubclass(
			tag,
			Background,
			)
		):
		return False

	return _eligible_for(
		char,
		tag,
		)


def Apply_Background(
	char,
	name=None,
	):
	"""Apply one declared Background allowed by the Character's Role."""
	resolved_name = (
		name
		or getattr(
			char,
			"background",
			None,
			)
		)

	if not resolved_name:
		available_names = tuple(
			sorted(
				tag.NAME
				for tag in BACKGROUNDS.values()
				if Background_Is_Available(
					char,
					tag,
					)
				)
			)

		if not available_names:
			raise ValueError(
				"No Background is available to this Character Role."
				)

		dice_bag = char.Dice_Bag(
			"identity.background",
			version="1",
			namespace="GenLegendActor",
			)
		resolved_name = char.Pick(
			available_names,
			dice=dice_bag,
			)

	current = getattr(
		char,
		"background",
		None,
		)

	if (
		current
		and current != resolved_name
		):
		raise ValueError(
			"A Character cannot carry two Backgrounds: "
			f"{current!r} and {resolved_name!r}."
			)

	tag = BACKGROUNDS.get(
		resolved_name
		)

	if tag is None:
		raise KeyError(
			f"BackgroundKit has no Tag for {resolved_name!r}."
			)

	if not Background_Is_Available(
		char,
		tag,
		):
		raise ValueError(
			f"Background {resolved_name!r} is not available to this "
			"Character Role."
			)

	if char not in tag:
		tag(
			char
			)

	return tag


def Apply_Background_Training(
	char,
	):
	"""Replay the applied Background's Tag-owned training onto its skill bag."""
	name = getattr(
		char,
		"background",
		None,
		)
	tag = BACKGROUNDS.get(
		name
		)

	if tag is None:
		raise ValueError(
			f"Cannot apply training for unknown Background {name!r}."
			)

	skill_names = getattr(
		char,
		"background_skills",
		tag.SKILLS,
		)
	tool = getattr(
		char,
		"background_tool",
		None,
		)

	_grant_skills(
		char,
		skill_names,
		)

	if tool:
		_grant_tool(
			char,
			tool,
			)

	return char.skills


def Apply_Background_Abilities(
	char,
	):
	"""Materialize the Background ability Record after scores exist."""
	if getattr(
		char,
		"background_abilities_applied",
		False,
		):
		return char.AS

	chosen = getattr(
		char,
		"background_asi",
		None,
		)

	if not chosen:
		return char.AS

	for stat, bonus in chosen:
		setattr(
			char.AS,
			stat,
			getattr(
				char.AS,
				stat,
				)
			+ bonus,
			)

	char.background_abilities_applied = True

	return char.AS


# ---------------------------------------------------------------------------
# Focused contracts
# ---------------------------------------------------------------------------


def _test_meta_fields():
	assert len(
		tuple(
			Background_Audience[:]
			)
		) == 87
	assert len(
		tuple(
			Available[:]
			)
		) == 61
	assert len(
		tuple(
			NPC_Background[:]
			)
		) == 87
	assert Merchant in Available
	assert Merchant in NPC_Background
	assert Doctor not in Available
	assert Doctor in NPC_Background


def _test_all_backgrounds():
	for index, (
		name,
		tag,
		) in enumerate(
			BACKGROUNDS.items()
			):
		character = Character(
			seed=100 + index
			)

		if tag in Available:
			Player(
				character
				)
		else:
			NonPlayer(
				character
				)

		tag(
			character
			)

		assert character in tag
		assert character in Background
		assert character.background == name
		assert character in tag.ORIGIN_FEAT
		assert len(
			tag.ABILITIES
			) == 3
		assert len(
			tag.SKILLS
			) == 2
		assert tag.TOOLS


def _test_ability_boost_soft_opt():
	from AtlasLusoris.GuildKit import Rogue

	character = Character(
		seed=24
		)
	Player(
		character
		)
	Rogue(
		character
		)
	character.AS = AbilityScores(
		STR=10,
		DEX=15,
		CON=12,
		INT=11,
		WIS=13,
		CHA=14,
		character=character,
		)

	assert _pick_boost_ability(
		character,
		[
			"DEX",
			"CHA",
			"WIS",
			],
		character.AS,
		) == "DEX"


def _test_apply_by_name():
	character = Character(
		seed=23
		)
	Player(
		character
		)
	Apply_Background(
		character,
		"Soldier",
		)

	assert character in Soldier
	assert character in Savage_Attacker
	assert Find_Background( character ) == "Soldier"
	assert f"{character:Background}" == "Soldier"


def _self_test():
	_test_meta_fields()
	_test_all_backgrounds()
	_test_ability_boost_soft_opt()
	_test_apply_by_name()

	print(
		"OK — BackgroundKit MetaTOP self-test "
		f"({len(BACKGROUNDS)} backgrounds)"
		)


__all__ = (
	"ARTISAN_TOOLS",
	"Available",
	"BACKGROUNDS",
	"Background",
	"Background_Audience",
	"Background_Is_Available",
	"Backgrounds_For",
	"Build_Background",
	"Find_Background",
	"NPC_Background",
	"NONPLAYER_BACKGROUNDS",
	"NONPLAYER_ONLY_BACKGROUNDS",
	"NONPLAYER_ONLY_BACKGROUND_NAMES",
	"OFFICIAL_2024_BACKGROUNDS",
	"PLAYER_BACKGROUNDS",
	"SHARED_BACKGROUNDS",
	"Apply_Background",
	"Apply_Background_Training",
	*tuple(
		tag.__name__
		for tag in BACKGROUNDS.values()
		),
	)


if __name__ == "__main__":
	_self_test()
