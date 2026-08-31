"""ClericKit — temporarily loaded from vaulted bytecode (recovery 2026-08-29).

Voice (Guild paragraph and Domain extends) is seated after the load.
Mechanics stay in the vaulted kit; prose lives in Map_of_Cleric_Prayers.
"""

from __future__ import annotations

from AtlasLusoris.AtlasOfGuilds._bytecode_kit import load_vaulted_kit

load_vaulted_kit(
	"ClericKit",
	globals(),
	)

from AtlasLusoris.Map_of_Cleric_Prayers import bind_cleric_voice

bind_cleric_voice(
	guild=Cleric,
	domains=(
		Life,
		Light,
		Trickery,
		War,
		),
	)
