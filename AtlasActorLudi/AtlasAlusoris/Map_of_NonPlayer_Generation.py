"""Public NonPlayer generation across Race, Guild, and Background."""

from __future__ import annotations

from dataclasses import dataclass
from random import Random
from secrets import randbits

from Minion import chronicler
from Minion import minion

from AtlasActorLudi.CharactersKit import Character
from AtlasActorLudi.AtlasAlusoris.Grimoire_of_NPC import NPC
from AtlasActorLudi.AtlasAlusoris.Map_of_Archetypes import Classify_Archetype
from AtlasActorLudi.AtlasAlusoris.Map_of_Archetypes import Identity_Axis
from AtlasActorLudi.AtlasAlusoris.Map_of_Races import race_weights
from AtlasLusoris.BackgroundKit import NONPLAYER_BACKGROUNDS
from AtlasLusoris.GuildKit import GUILDS


@dataclass(frozen=True, slots=True)
class NonPlayer_Choices:
	"""Selectable Alusoris dimensions exposed to a frontline."""

	races: tuple[str, ...]
	guilds: tuple[str, ...]
	backgrounds: tuple[str, ...]

	@property
	def classes(
			self,
			):
		"""Sheet-language alias for Guild choices."""
		return self.guilds


def choices(
		) -> NonPlayer_Choices:
	"""Return sorted immutable choices without presentation placeholders."""
	return NonPlayer_Choices(
			races=tuple(
					sorted(
							race
							for race in race_weights
							if race
							)
					),
			guilds=tuple(
					sorted(
							GUILDS
							)
					),
			backgrounds=tuple(
					sorted(
							NONPLAYER_BACKGROUNDS
							)
					),
			)


def _requested(
		value: str | None,
		) -> str | None:
	if value in (
			None,
			"Random",
			):
		return None
	return value


def _set_axis(
		requests: dict[Identity_Axis, str | None],
		axis: Identity_Axis,
		name: str,
		*,
		source: str,
		) -> None:
	current = requests[axis]
	if current is not None and current != name:
		raise ValueError(
				f"NonPlayer {axis.value.title()} and {source} disagree: {current!r} != {name!r}."
				)
	requests[axis] = name


def _resolve_identity_requests(
		*,
		guild: str | None,
		background: str | None,
		profile: str | None,
		archetype: str | None,
		) -> dict[Identity_Axis, str | None]:
	requests = {
			Identity_Axis.GUILD: None,
			Identity_Axis.BACKGROUND: None,
			}
	requested_guild = _requested(
			guild
			)
	requested_background = _requested(
			background
			)
	requested_profile = _requested(
			profile
			)
	requested_archetype = _requested(
			archetype
			)
	if requested_guild is not None:
		if requested_guild not in GUILDS:
			raise ValueError(
					f"Unknown NonPlayer Guild: {requested_guild!r}."
					)
		_set_axis(
				requests,
				Identity_Axis.GUILD,
				requested_guild,
				source="Guild",
				)
	if requested_profile is not None:
		if requested_profile not in NONPLAYER_BACKGROUNDS:
			raise ValueError(
					f"Unknown legacy NonPlayer Profile/Background: {requested_profile!r}."
					)
		_set_axis(
				requests,
				Identity_Axis.BACKGROUND,
				requested_profile,
				source="legacy Profile",
				)
	if requested_background is not None:
		if requested_background in NONPLAYER_BACKGROUNDS:
			identity = (
					Identity_Axis.BACKGROUND,
					requested_background,
					)
		else:
			try:
				legacy = Classify_Archetype(
						requested_background
						)
			except ValueError as error:
				raise ValueError(
						f"Unknown NonPlayer Background or legacy Archetype: {requested_background!r}."
						) from error
			identity = (
					legacy.axis,
					legacy.name,
					)
		_set_axis(
				requests,
				identity[0],
				identity[1],
				source="legacy Background",
				)
	if requested_archetype is not None:
		legacy = Classify_Archetype(
				requested_archetype
				)
		_set_axis(
				requests,
				legacy.axis,
				legacy.name,
				source="legacy Archetype",
				)
	return requests


def _chosen_or_random(
		character: Character,
		dimension: str,
		requested: str | None,
		available,
		*,
		weights=None,
		) -> str:
	valid_values = tuple(
			available
			)
	if not valid_values:
		raise RuntimeError(
				f"No NonPlayer {dimension} choices are available."
				)
	if requested is not None:
		if requested not in valid_values:
			raise ValueError(
					f"Unknown NonPlayer {dimension}: {requested!r}."
					)
		return requested
	dice_bag = character.Dice_Bag(
			f"identity.nonplayer.{dimension.casefold()}",
			version="1",
			namespace="GenLegendActor",
			)
	return character.Pick(
			valid_values,
			weights=tuple(
					weights
					) if weights is not None else None,
			dice=dice_bag,
			)


@minion
def _attempt_nonplayer(
		target,
		race,
		guild,
		background,
		level,
		seed,
		light,
		):
	"""Perform one generation attempt through the current Alusoris Grimoire."""
	return NPC(
			target=target,
			race=race,
			guild=guild,
			background=background,
			level=level,
			seed=seed,
			light=light,
			)


def _generation_seed(
		seed: int | None,
		) -> int:
	"""Resolve a public seed without leaking Character's -1 sentinel."""
	if seed is None:
		return randbits(
				64
				)
	resolved = int(
			seed
			)
	if resolved < 0:
		raise ValueError(
				"A NonPlayer generation seed must be zero or greater."
				)
	return resolved


@chronicler
def summon_nonplayer(
		race: str | None = None,
		archetype: str | None = None,
		level: int = 1,
		seed: int | None = None,
		light: bool = False,
		*,
		guild: str | None = None,
		background: str | None = None,
		profile: str | None = None,
		):
	"""Generate one NonPlayer Character through Guild and Background."""
	requested_level = max(
			1,
			int(
					level
					),
			)
	current_seed = _generation_seed(
			seed
			)
	character = Character(
			seed=current_seed,
			level=requested_level,
			)
	identities = _resolve_identity_requests(
			guild=guild,
			background=background,
			profile=profile,
			archetype=archetype,
			)
	race_names = tuple(
			race_weights
			)
	selected_race = _chosen_or_random(
			character,
			"Race",
			_requested(
					race
					),
			race_names,
			weights=(
					race_weights[name]
					for name in race_names
					),
			)
	selected_guild = _chosen_or_random(
			character,
			"Guild",
			identities[Identity_Axis.GUILD],
			GUILDS,
			)
	selected_background = _chosen_or_random(
			character,
			"Background",
			identities[Identity_Axis.BACKGROUND],
			NONPLAYER_BACKGROUNDS,
			)
	last_error = None
	for _ in range(
			5
			):
		try:
			return _attempt_nonplayer(
					target=character,
					race=selected_race,
					guild=selected_guild,
					background=selected_background,
					level=requested_level,
					seed=current_seed,
					light=light,
					)
		except Exception as error:
			last_error = error
			current_seed += 1
			character = Character(
					seed=current_seed,
					level=requested_level,
					)
	raise RuntimeError(
			"Unable to summon a NonPlayer Character after five attempts."
			) from last_error


def summon_nonplayer_list(
		race: str | None = None,
		archetype: str | None = None,
		count: int = 5,
		seed: int | None = None,
		*,
		guild: str | None = None,
		background: str | None = None,
		profile: str | None = None,
		level: int | None = None,
		) -> list[Character]:
	"""Generate a deterministic list of independently seeded Characters."""
	if count < 1:
		raise ValueError(
				"A NonPlayer list must contain at least one Character."
				)
	batch_seed = _generation_seed(
			seed
			)
	result = []
	for index in range(
			count
			):
		character_seed = batch_seed + index
		if level is not None:
			character_level = max(
					1,
					int(
							level
							),
					)
		else:
			character_level = Random(
					character_seed
					).randint(
					1,
					20,
					)
		result.append(
				summon_nonplayer(
						race=race,
						archetype=archetype,
						guild=guild,
						background=background,
						profile=profile,
						level=character_level,
						seed=character_seed,
						)
				)
	return result


__all__ = (
		"NonPlayer_Choices",
		"choices",
		"summon_nonplayer",
		"summon_nonplayer_list",
		)
