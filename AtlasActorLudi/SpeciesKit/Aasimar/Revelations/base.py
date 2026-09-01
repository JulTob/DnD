"""The internal Celestial Revelation Geometry."""

from TagKit import Pre

from AtlasLusoris.FeaturesKit import Trait


class Celestial_Revelation(Trait):
	"""A level-three Aasimar transformation mode."""

	LEVEL = 3
	ACTION = "Bonus Action"
	DURATION_MINUTES = 1
	END_ACTION = "No Action"
	USES = 1
	RECOVERY = "Long Rest"

	@Pre
	def Aasimar_Only(
		target,
		):
		from AtlasActorLudi.SpeciesKit.Aasimar import Aasimar

		return target in Aasimar

	@Pre
	def Gained_At_Level_Three(
		target,
		):
		return int(
			getattr(
				target,
				"level",
				1,
				)
			) >= Celestial_Revelation.LEVEL


def Current_Revelation(
	target,
	):
	"""Return the one Revelation Shape currently carried."""
	from AtlasActorLudi.SpeciesKit.Aasimar.Revelations import (
		AASIMAR_REVELATIONS,
		)

	carried = tuple(
		revelation
		for revelation in AASIMAR_REVELATIONS
		if target in revelation
		)

	if len(
		carried,
		) > 1:
		raise ValueError(
			"An Aasimar carries conflicting Celestial Revelations: "
			+ ", ".join(
				revelation.__name__
				for revelation in carried
				)
			+ "."
			)

	if carried:
		return carried[ 0 ]

	return None


def Imprint_Revelation(
	target,
	revelation,
	) -> None:
	"""Imprint one generated Revelation while Tagging stays atomic."""
	current = Current_Revelation(
		target,
		)

	if (
		current is not None
		and current is not revelation
		):
		raise ValueError(
			"An Aasimar cannot carry two Celestial Revelations: "
			f"{current.__name__!r} and {revelation.__name__!r}."
			)

	target.celestial_revelation = revelation.__name__.replace(
		"_",
		" ",
		)
