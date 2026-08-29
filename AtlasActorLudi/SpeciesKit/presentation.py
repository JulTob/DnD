"""Shared projection from Species semantics to Character-sheet Entries."""

from AtlasLusoris.FeaturesKit import grant


def Project_Species_Feature(
		target,
		name,
		description,
		*,
		chips=None,
		level=0,
		narrative=False,
		):
	"""Create or refresh one idempotent Species Feature Entry."""
	for feature in getattr(
			target,
			"features",
			(),
			) or ():
		if (
			getattr(
				feature,
				"name",
				None,
				) == name
			and getattr(
				feature,
				"source",
				None,
				) == "Species Feature"
			):
			feature.description = description
			feature.chips = tuple(
				chips
				or ()
				)
			feature.level = level
			feature.narrative = bool(
				narrative
				)
			return feature

	return grant(
		target,
		name=name,
		description=description,
		source="Species Feature",
		chips=chips,
		level=level,
		narrative=narrative,
		)
