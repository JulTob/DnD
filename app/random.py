# app/random.py

import random as _stdlib_random

################################################################################
# INTERNAL PRNG OBJECT
################################################################################
_rng = _stdlib_random.Random()          # its own state, never global

# -- API mirror ---------------------------------------------------------------
def seed(value=None):           # match stdlib signature
    """Seed the game RNG without touching the global generator."""
    return _rng.seed(value)

def getstate():
    return _rng.getstate()

def setstate(state):
    return _rng.setstate(state)

def randint(a, b):              # and the helpers you actually use
    return _rng.randint(a, b)

def randrange(*args, **kw):
    return _rng.randrange(*args, **kw)

def choice(seq):
    return _rng.choice(seq)

def sample(pop, k):             # etc.
    return _rng.sample(pop, k)

def random():
    return _rng.random()

def uniform(a, b):
    return _rng.uniform(a, b)

# -- optional: automatically delegate *anything else* -------------------------
def __getattr__(name):          # called on unknown attribute access
    return getattr(_rng, name)
