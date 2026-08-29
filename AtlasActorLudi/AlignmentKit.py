"""AlignmentKit — temporarily loaded from vaulted bytecode (recovery 2026-08-29)."""

from __future__ import annotations

import marshal
from pathlib import Path

_PYC = Path(
	"/Users/tbs/Desktop/DnD/$S/vault/AlignmentKit.cpython-314.pyc"
	)

exec(
	marshal.loads(
		_PYC.read_bytes()[16:]
		),
	globals(),
	)
