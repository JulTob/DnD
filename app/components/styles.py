"""styles — temporarily loaded from vaulted bytecode (recovery 2026-08-29)."""
from __future__ import annotations

import marshal
import sys
import types
from pathlib import Path

_PYC = Path(__file__).resolve().parents[2] / ".recovery-vault" / "app/components" / "styles.cpython-314.pyc"

_body_name = "app.components._bc_styles"
if _body_name not in sys.modules:
	body = types.ModuleType(_body_name)
	body.__file__ = str(_PYC)
	sys.modules[_body_name] = body
	exec(marshal.loads(_PYC.read_bytes()[16:]), body.__dict__)
else:
	body = sys.modules[_body_name]

for _name, _value in list(body.__dict__.items()):
	if _name.startswith("__"):
		continue
	globals()[_name] = _value

if hasattr(body, "__all__"):
	__all__ = list(body.__all__)
