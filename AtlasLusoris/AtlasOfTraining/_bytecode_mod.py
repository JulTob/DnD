"""Load an AtlasOfTraining module from vaulted bytecode (recovery 2026-08-29)."""
from __future__ import annotations

import marshal
import sys
import types
from pathlib import Path

_VAULT = Path(__file__).resolve().parents[2] / ".recovery-vault" / "training"


def load_vaulted(
		pyc_name: str,
		destination: dict,
		) -> None:
	"""``pyc_name`` like ``Map_of_Wizard_Training.cpython-314.pyc``."""
	body_name = f"AtlasLusoris.AtlasOfTraining._bc_{pyc_name.replace('.', '_')}"
	if body_name not in sys.modules:
		pyc = _VAULT / pyc_name
		body = types.ModuleType(
			body_name
			)
		body.__file__ = str(
			pyc
			)
		sys.modules[
			body_name
			] = body
		exec(
			marshal.loads(
				pyc.read_bytes()[
					16:
					]
				),
			body.__dict__,
			)
	else:
		body = sys.modules[
			body_name
			]

	for name, value in list(
		body.__dict__.items()
		):
		if name.startswith(
			"_"
			):
			continue
		destination[
			name
			] = value

	if hasattr(
		body,
		"__all__",
		):
		destination[
			"__all__"
			] = list(
			body.__all__
			)
