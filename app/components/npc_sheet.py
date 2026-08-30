"""npc_sheet — vaulted bytecode (recovery 2026-08-29)."""
from __future__ import annotations

import marshal, sys, types
from pathlib import Path

_PYC = Path(__file__).resolve().parents[2] / ".recovery-vault" / "app_components" / "npc_sheet.cpython-314.pyc"
_bn = "app.components._bc_npc_sheet"
if _bn not in sys.modules:
	body = types.ModuleType(_bn); body.__file__ = str(_PYC)
	sys.modules[_bn] = body
	exec(marshal.loads(_PYC.read_bytes()[16:]), body.__dict__)
else:
	body = sys.modules[_bn]
for _n, _v in list(body.__dict__.items()):
	if not _n.startswith("__"): globals()[_n] = _v
if hasattr(body, "__all__"): __all__ = list(body.__all__)
