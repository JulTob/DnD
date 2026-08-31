"""Humanoid Species Shapes used by the NonPlayer production line."""

from AtlasActorLudi.SpeciesKit.bases import Humanoid
from AtlasActorLudi.SpeciesKit.bases import Species
from AtlasActorLudi.SpeciesKit.declarations import Legacy_NonPlayer


class Aven(
	Species,
	Humanoid,
	):
	"""A birdlike Humanoid lineage."""


Legacy_NonPlayer(Aven)


class Beastfolk(
	Species,
	Humanoid,
	):
	"""A Humanoid lineage with bestial traits."""


Legacy_NonPlayer(Beastfolk)


class Catfolk(
	Species,
	Humanoid,
	):
	"""A feline Humanoid lineage."""


Legacy_NonPlayer(Catfolk)


class Goblin(
	Species,
	Humanoid,
	):
	"""A Goblin Humanoid lineage."""


Legacy_NonPlayer(Goblin)


class Kobold(
	Species,
	Humanoid,
	):
	"""A Kobold Humanoid lineage."""


Legacy_NonPlayer(Kobold)


class Lizardfolk(
	Species,
	Humanoid,
	):
	"""A reptilian Humanoid lineage."""


Legacy_NonPlayer(Lizardfolk)


class Snakefolk(
	Species,
	Humanoid,
	):
	"""A serpentine Humanoid lineage."""


Legacy_NonPlayer(Snakefolk)
