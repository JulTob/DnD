"""main — temporarily loaded from vaulted bytecode (recovery 2026-08-29).

The working-tree copy recovered from chat history was an older revision
(5 arguments to ``home_page_ui``); this loads the true final bytecode.
"""
from __future__ import annotations

import marshal
import sys
import types
from pathlib import Path

_PYC = Path(__file__).resolve().parents[1] / ".recovery-vault" / "app" / "main.cpython-314.pyc"

_body_name = "app._bc_main"
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
