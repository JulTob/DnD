"""AtlasMagistratum — production routes for the Game Master's seat.

DM Character Oracle binding and `dm/…` path rites live here.
The DM Character is morally open — villain, Quest Master, contested guardian,
or any figure whose will frames the session (not “BBEG-only”).

Story syntax stays in AtlasEpica. Shiny chrome lives in ``app.pages``.
"""

# [Reconstructed 2026-08-29 from compiled bytecode after the working-tree
#  wipe. Declarations are verbatim; see Documenta/Questae for the incident.]

from AtlasMagistratum.Charts_of_Scene_Binder import bind_dm_character
from AtlasMagistratum.Charts_of_Scene_Binder import briefing_for
from AtlasMagistratum.Charts_of_Scene_Binder import draw_inspiration
from AtlasMagistratum.Map_of_Session_Paths import asgi_dm_redirect_target
from AtlasMagistratum.Map_of_Session_Paths import dm_session_hash
from AtlasMagistratum.Map_of_Session_Paths import parse_npc_or_dm_path
