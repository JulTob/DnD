"""
Guild construction body.

The public TOP surface is GuildKit. This module keeps the surviving
Aug 28 bytecode for Build_Guild and its helpers until those protocols
are rewritten as source. Private names stay here; the spec re-exports
the Guild Tags and application functions.

The bytecode calls Load_Guild_Libraries while it is still executing.
That call is deferred: kits import GuildKit, so the spec must finish
re-exporting before the libraries load.
"""

from __future__ import annotations

import marshal
from pathlib import Path

from AtlasLusoris.AtlasOfGuilds import Load_Guild_Libraries as _load_guild_libraries
import AtlasLusoris.AtlasOfGuilds as _guild_libraries


_PYC = (
	Path( __file__ )
	.resolve()
	.parents[ 1 ]
	/ ".recovery-vault"
	/ "GuildKit.cpython-314.pyc"
	)

_guild_libraries.Load_Guild_Libraries = lambda: None
try:
	exec(
		marshal.loads(
			_PYC.read_bytes()[ 16: ]
			),
		globals(),
		)
finally:
	_guild_libraries.Load_Guild_Libraries = _load_guild_libraries
	Load_Guild_Libraries = _load_guild_libraries


_SKIP = frozenset(
	{
		"marshal",
		"annotations",
		"Iterable",
		"Mapping",
		"MappingProxyType",
		"Path",
		}
	)

__all__ = tuple(
	name
	for name in tuple(
		globals()
		)
	if (
		not name.startswith(
			"_"
			)
		and name not in _SKIP
		)
	)
