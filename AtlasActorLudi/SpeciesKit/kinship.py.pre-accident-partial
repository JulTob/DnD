"""
Kinship Tags: what a Character *resembles*, which is never what the rules call
them.

``Creature_Type`` in ``bases`` answers the rules question, and for every
playable Species the answer is ``Humanoid``: an Aasimar is not a Celestial, and
a spell that seeks Celestials does not find one.  This answers the other
question, the one every flavour system actually asks.  Aasimar take their names
from Celestials.  Gnomes get read as Fae whether or not they have ever seen the
Feywild.  A Goliath is spoken of the way giants are spoken of.

Kinship is carried as a Tag rather than as a field because that is exactly what
a Tag is for.  A Species declares its kin as a base, so ``character in
Celestial_Kin`` is the whole query, and nothing has to keep a list of which
Species happen to be celestial-ish.  Nothing here grants anything: no
Resistance, no sense, no trait.  It is classification, for names, titles, gear
vocabulary and familiar affinity.
"""

from TagKit import Tag
from TagKit import Pre

from AtlasActorLudi.CharactersKit import Character


class Kinship(Tag):
	"""What a Character resembles, for everything that is not a rule."""

	@Pre
	def Character_Only(
		target,
		):
		return isinstance(
			target,
			Character,
			)


class Celestial_Kin(Kinship):
	"""Read as of the Upper Planes: aasimar, and those who carry a spark."""


class Fae_Kin(Kinship):
	"""Read as of the Feywild: elves, gnomes, and anything asked to go back."""


class Fiend_Kin(Kinship):
	"""Read as of the Lower Planes: tieflings, and the inconveniently horned."""


class Dragon_Kin(Kinship):
	"""Read as draconic: dragonborn, kobolds, and the scaled."""


class Giant_Kin(Kinship):
	"""Read as of the giants: goliaths, and whoever else looms."""


class Undead_Kin(Kinship):
	"""Read as no longer entirely alive: dhampirs, reborn, and the returned."""


class Elemental_Kin(Kinship):
	"""Read as of the elements: genasi, and anything that smells of storm."""


KINSHIPS = (
	Celestial_Kin,
	Dragon_Kin,
	Elemental_Kin,
	Fae_Kin,
	Fiend_Kin,
	Giant_Kin,
	Undead_Kin,
	)


def Kinships_Of(
	character,
	) -> tuple[str, ...]:
	"""
	Every kinship a Character carries, as plain words.

	``("Celestial",)`` rather than ``(Celestial_Kin,)``, because the callers are
	name tables and affinity weights that want a word to match on.
	"""
	return tuple(
		tag.__name__.removesuffix(
			"_Kin"
			)
		for tag in KINSHIPS
		if character in tag
		)


__all__ = (
	"Celestial_Kin",
	"Dragon_Kin",
	"Elemental_Kin",
	"Fae_Kin",
	"Fiend_Kin",
	"Giant_Kin",
	"KINSHIPS",
	"Kinship",
	"Kinships_Of",
	"Undead_Kin",
	)
