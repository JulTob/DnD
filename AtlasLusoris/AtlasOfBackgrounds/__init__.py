"""Source-specific Background Maps beneath the canonical BackgroundKit."""

from __future__ import annotations

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
	"""Register all later official 2024-format Background source Maps."""
	return (
		*Register_Eberron_Backgrounds(**routes),
		*Register_Forgotten_Realms_Backgrounds(**routes),
		*Register_Astarion_Backgrounds(**routes),
		*Register_Lorwyn_Backgrounds(**routes),
		*Register_Ravenloft_Backgrounds(**routes),
		)


__all__ = (
	"Register_Official_2024_Backgrounds",
	)
