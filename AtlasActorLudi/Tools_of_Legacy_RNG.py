"""
Tools_of_Legacy_RNG — quarantine for the module-level ``random`` calls.

Character generation is deterministic through each Character's own Dice Bags,
but legacy paths still reach for the global ``random`` module. Until the last
of them is retired (QST-0016.2 series), a generation attempt runs inside
``Isolated_Legacy_RNG``: the global state is seeded from the Character's seed
on entry and fully restored on exit, so a stray legacy call neither breaks
reproducibility nor leaks state into the next summon.

[restored 2026-08-29 from the recorded call shape after the working-tree wipe.]
"""

from __future__ import annotations

import random
from contextlib import contextmanager


@contextmanager
def Isolated_Legacy_RNG(
		seed,
		):
	"""Seed the global RNG deterministically; restore the prior state after."""
	prior = random.getstate()
	random.seed(
		int(
			seed
			)
		)
	try:
		yield
	finally:
		random.setstate(
			prior
			)
