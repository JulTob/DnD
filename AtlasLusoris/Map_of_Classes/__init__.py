# AtlasLusoris/Map_of_Classes/__init__.py

"""Public façade: `from AtlasLusoris.Map_of_Classes import Wizard`"""

# Re-export the abstract base & helpers
from Minion import Initialized, Alert, Inform, Warning, News, Ends, Fail, Catched, FailureError

from .Scroll_of_Constants import CLASSES, SUBCLASSES
from .Grimoire_of_Health  import roll_health, health_dice, HIT_DIE_TABLE
from .Codex_of_Progression  import (
		Progression,
		get_class_progression,
		get_features,
		apply_class_proficiencies
		)

# Import concrete classes independently so a missing file cannot hide the rest.
def _load_training(name):
	import importlib
	try:
		module = importlib.import_module(f".Training.{name}", __name__)
		return getattr(module, name)
	except Exception as err:
		Warning(f"[Map_of_Classes] could not load {name}: {err}")
		return None

Barbarian = _load_training("Barbarian")
Bard      = _load_training("Bard")
Cleric    = _load_training("Cleric")
Druid     = _load_training("Druid")
Fighter   = _load_training("Fighter")
Monk      = _load_training("Monk")
Paladin   = _load_training("Paladin")
Ranger    = _load_training("Ranger")
Rogue     = _load_training("Rogue")
Sorcerer  = _load_training("Sorcerer")
Warlock   = _load_training("Warlock")
Wizard    = _load_training("Wizard")
Multiclass = _load_training("Multiclass")

# ── backward-compat shim for Flask route ─────────────
classes = list(CLASSES)        # same data, old variable name
subclasses = SUBCLASSES          # same dict, different alias

GetClassProgression = get_class_progression   # function's CamelCase alias

__all__ = [
	# data
	"HIT_DIE_TABLE", "CLASSES", "SUBCLASSES",
	# helpers
	"roll_health", "health_dice", "Progression",
	"get_features", "get_class_progression",
	# concrete
	"Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk",
	"Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard",
	"Multiclass",
	"classes", "subclasses",
	"get_class_progression", "GetClassProgression",
	"apply_class_proficiencies", "apply_class_features"]

GetFeatures = get_features # legacy Camel-Case alias so old code continues to work
__all__.extend(["get_features", "GetFeatures"])
