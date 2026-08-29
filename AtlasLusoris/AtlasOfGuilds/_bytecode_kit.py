"""Load a Guild kit module from a vaulted ``.pyc`` (recovery 2026-08-29)."""

from __future__ import annotations

import marshal
import sys
import types
from pathlib import Path

_VAULT = Path(
	"/Users/tbs/Desktop/DnD/$S/vault/guilds"
	)


def load_vaulted_kit(
		kit_name: str,
		destination: dict,
		) -> None:
	"""
	Execute ``{kit_name}.cpython-314.pyc`` into ``destination`` globals.

	Uses a private module name so loading does not re-enter the bootstrap ``.py``.
	"""
	body_name = f"AtlasLusoris.AtlasOfGuilds._{kit_name}_bytecode"
	if body_name not in sys.modules:
		pyc = _VAULT / f"{kit_name}.cpython-314.pyc"
		body = types.ModuleType(
			body_name
			)
		body.__file__ = str(
			pyc
			)
		sys.modules[body_name] = body
		code = marshal.loads(
			pyc.read_bytes()[16:]
			)
		exec(
			code,
			body.__dict__,
			)
	else:
		body = sys.modules[body_name]

	for name, value in list(
		body.__dict__.items()
		):
		if name.startswith(
			"_"
			):
			continue
		destination[name] = value

	if hasattr(
		body,
		"__all__",
		):
		destination["__all__"] = list(
			body.__all__
			)
