"""Humanoid Species Shapes used by the NonPlayer production line."""

from AtlasActorLudi.SpeciesKit.bases import Humanoid
from AtlasActorLudi.SpeciesKit.bases import Species
from AtlasActorLudi.SpeciesKit.declarations import Legacy_NonPlayer


class Aven(
	Species,
	Humanoid,
	):
	"""A birdlike Humanoid lineage."""


class Beastfolk(
	Species,
	Humanoid,
	):
	"""A Humanoid lineage with bestial traits."""


class Catfolk(
	Species,
	Humanoid,
	):
	"""A feline Humanoid lineage."""


class Goblin(
	Species,
	Humanoid,
	):
	"""A Goblin Humanoid lineage."""


class Kobold(
	Species,
	Humanoid,
	):
	"""A Kobold Humanoid lineage."""


class Lizardfolk(
	Species,
	Humanoid,
	):
	"""A reptilian Humanoid lineage."""


class Snakefolk(
	Species,
	Humanoid,
	):
	"""A serpentine Humanoid lineage."""


Legacy_NonPlayer(
	Aven,
	)
Legacy_NonPlayer(
	Beastfolk,
	)
Legacy_NonPlayer(
	Catfolk,
	)
Legacy_NonPlayer(
	Goblin,
	)
Legacy_NonPlayer(
	Kobold,
	)
Legacy_NonPlayer(
	Lizardfolk,
	)
Legacy_NonPlayer(
	Snakefolk,
	)
