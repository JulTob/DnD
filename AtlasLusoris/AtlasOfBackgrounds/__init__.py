"""Source-specific Background Maps beneath the canonical BackgroundKit."""

from __future__ import annotations

from AtlasLusoris.AtlasOfBackgrounds.Map_of_Arcana_Unleashed_Backgrounds import (
	Register_Arcana_Unleashed_Backgrounds,
	)
from AtlasLusoris.AtlasOfBackgrounds.Map_of_Astarion_Backgrounds import (
	Register_Astarion_Backgrounds,
	)
from AtlasLusoris.AtlasOfBackgrounds.Map_of_Eberron_Backgrounds import (
	Register_Eberron_Backgrounds,
	)
from AtlasLusoris.AtlasOfBackgrounds.Map_of_Forgotten_Realms_Backgrounds import (
	Register_Forgotten_Realms_Backgrounds,
	)
from AtlasLusoris.AtlasOfBackgrounds.Map_of_Lorwyn_Backgrounds import (
	Register_Lorwyn_Backgrounds,
	)
from AtlasLusoris.AtlasOfBackgrounds.Map_of_Ravenloft_Backgrounds import (
	Register_Ravenloft_Backgrounds,
	)


def Register_Official_2024_Backgrounds(
		**routes,
		) -> tuple[type, ...]:
	"""Register all later official 2024-format Background source Maps.

	Arcana Unleashed is recovered as a Map but not enrolled here: its
	preview Origin Feat (Arcane Infiltrator) is not on
	BACKGROUND_ORIGIN_FEATS yet.
	"""
	return (
		*Register_Eberron_Backgrounds(**routes),
		*Register_Forgotten_Realms_Backgrounds(**routes),
		*Register_Astarion_Backgrounds(**routes),
		*Register_Lorwyn_Backgrounds(**routes),
		*Register_Ravenloft_Backgrounds(**routes),
		)


__all__ = (
	"Register_Arcana_Unleashed_Backgrounds",
	"Register_Official_2024_Backgrounds",
	)
