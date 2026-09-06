"""Quarantine transitional global entropy during Player generation.

The supported Player facade must replay a supplied seed exactly.  Most
recovered legacy code still reaches for one of two process-wide generators:
stdlib ``random`` and the historical ``app.random`` singleton.  Until the
Character-owned Dice migration retires those calls, a generation attempt seeds
and restores both states as one explicit compatibility boundary.
"""

from __future__ import annotations

import random
from collections.abc import Iterator
from contextlib import contextmanager
from threading import RLock

import app.random as app_random


_legacy_rng_lock = RLock()


@contextmanager
def Isolated_Legacy_RNG(
        seed: int,
        ) -> Iterator[None]:
    """Seed, serialize, and restore every transitional RNG authority."""
    with _legacy_rng_lock:
        seed_value = int(
                seed
                )
        stdlib_prior = random.getstate()
        app_prior = app_random.getstate()

        try:
            random.seed(
                    seed_value
                    )
            app_random.seed(
                    seed_value
                    )

            yield
        finally:
            app_random.setstate(
                    app_prior
                    )
            random.setstate(
                    stdlib_prior
                    )
