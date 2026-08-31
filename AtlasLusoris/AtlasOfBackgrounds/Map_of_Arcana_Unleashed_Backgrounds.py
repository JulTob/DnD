"""Complete official Arcana Unleashed preview Background records."""

from AtlasLusoris.AtlasOfBackgrounds.OfficialBackgroundsKit import (
	Register_Backgrounds,
	)
from AtlasLusoris.Grimoire_of_Backgrounds import (
	Background,
	)

SOURCE_TITLE = "Dungeon Masters: Arcana Unleashed Play-Along Pack"
SOURCE_URL = "https://www.dndbeyond.com/sources/dnd/dmau"
SOURCE_LOCATOR = "Appendix C: Factions and Character Options"

RECORDS = (
	Background(
		name="Agent of the Ninth Quill",
		description=(
			"You learned arcane inquiry and covert acquisition while serving "
			"an organization that collects dangerous magical knowledge."
			),
		abilities=(
			"DEX",
			"INT",
			"CHA",
			),
		origin_feat="Arcane Infiltrator",
		skills=(
			"Arcana",
			"Sleight_of_Hand",
			),
		tools="Thieves_Tools",
		),
	)

# Preview Origin Feat is not on BACKGROUND_ORIGIN_FEATS yet, so
# Register_Official_2024_Backgrounds does not enroll this Map.


def Register_Arcana_Unleashed_Backgrounds(
		**routes,
		) -> tuple[ type, ... ]:
	return Register_Backgrounds(
		records=RECORDS,
		source_title=SOURCE_TITLE,
		source_url=SOURCE_URL,
		source_locator=SOURCE_LOCATOR,
		**routes,
		)


__all__ = (
	"Register_Arcana_Unleashed_Backgrounds",
	)
