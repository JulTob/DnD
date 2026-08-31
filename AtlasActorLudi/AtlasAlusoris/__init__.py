"""AtlasAlusoris under ActorLudi — NonPlayer generation and race catalogue."""

# [Restored 2026-08-29 after the working-tree wipe. Re-exports mirror the
#  compiled finals; the modules beneath are bytecode shims until their sources
#  are re-authored. See Documenta/Questae for the incident.]

from AtlasActorLudi.AtlasAlusoris.Map_of_NonPlayer_Generation import (
	NonPlayer_Choices,
	summon_nonplayer,
	summon_nonplayer_list,
	)
from AtlasActorLudi.AtlasAlusoris.Map_of_NonPlayer_Generation import (
	choices as nonplayer_choices,
	)
from AtlasActorLudi.AtlasAlusoris.Map_of_NonPlayer_Paths import (
	nonplayer_hash,
	parse_nonplayer_path,
	)

__all__ = (
	"NonPlayer_Choices",
	"nonplayer_choices",
	"summon_nonplayer",
	"summon_nonplayer_list",
	"nonplayer_hash",
	"parse_nonplayer_path",
	)
