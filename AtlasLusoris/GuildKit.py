"""
GuildKit — temporarily resurrected from surviving bytecode (recovery 2026-08-29).

Loads the vaulted Aug 28 ``GuildKit.cpython-314.pyc`` directly into this
module's namespace (so Guild kit libraries can ``from AtlasLusoris.GuildKit
import …`` while ``Load_Guild_Libraries`` runs). Vault path avoids
``__pycache__`` clobber on import.
"""

from __future__ import annotations

import marshal
from pathlib import Path

_PYC = Path(
	"/Users/tbs/Desktop/DnD/$S/vault/GuildKit.cpython-314.pyc"
	)

exec(
	marshal.loads(
		_PYC.read_bytes()[16:]
		),
	globals(),
	)
