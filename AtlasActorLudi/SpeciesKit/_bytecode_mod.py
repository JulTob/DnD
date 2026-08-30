"""Load a SpeciesKit module from vaulted bytecode (recovery 2026-08-29)."""
from __future__ import annotations
import marshal, sys, types
from pathlib import Path

_VAULT = Path("/Users/tbs/Desktop/DnD/.recovery-vault/species")

def load_vaulted(relative_pyc: str, destination: dict) -> None:
	"""relative_pyc like 'Aasimar/base.cpython-314.pyc'."""
	body_name = f"AtlasActorLudi.SpeciesKit._bc_{relative_pyc.replace('/', '_').replace('.', '_')}"
	if body_name not in sys.modules:
		pyc = _VAULT / relative_pyc
		body = types.ModuleType(body_name)
		body.__file__ = str(pyc)
		sys.modules[body_name] = body
		exec(marshal.loads(pyc.read_bytes()[16:]), body.__dict__)
	else:
		body = sys.modules[body_name]
	for name, value in list(body.__dict__.items()):
		if name.startswith("_"):
			continue
		destination[name] = value
	if hasattr(body, "__all__"):
		destination["__all__"] = list(body.__all__)
