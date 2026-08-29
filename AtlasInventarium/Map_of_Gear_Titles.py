"""Map_of_Gear_Titles — temporarily loaded from vaulted bytecode (recovery 2026-08-29)."""
from __future__ import annotations

import marshal
import sys
import types
from pathlib import Path

_VAULT = Path(__file__).resolve().parents[1] / "$S" / "vault" / "inventarium"
_PYC = _VAULT / "Map_of_Gear_Titles.cpython-314.pyc"

_body_name = "AtlasInventarium._bc_Map_of_Gear_Titles"
if _body_name not in sys.modules:
	body = types.ModuleType(
		_body_name
		)
	body.__file__ = str(
		_PYC
		)
	sys.modules[
		_body_name
		] = body
	exec(
		marshal.loads(
			_PYC.read_bytes()[
				16:
				]
			),
		body.__dict__,
		)
else:
	body = sys.modules[
		_body_name
		]

for _name, _value in list(
	body.__dict__.items()
	):
	if _name.startswith(
		"_"
		):
		continue
	globals()[
		_name
		] = _value

if hasattr(
	body,
	"__all__",
	):
	__all__ = list(
		body.__all__
		)
