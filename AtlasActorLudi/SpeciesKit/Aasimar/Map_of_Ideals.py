"""
Map of Ideals — what an Aasimar descends from, and how it shows.

A Celestial is an Ideal with a shape: not a god and not a servant of one, but
Justice itself, or Mercy, or Honor, standing where mortals can see it.  An
Aasimar carries a spark of one, and the spark is visible in two places.

**Talaria** are the small vestigial wings.  They sit only where a wing could
plausibly take a body's weight, which is why none of them are on the face or the
front of the chest, and each folds into something a tailor could explain: a
torc, a sash, an embroidered collar.

**The aureola** is the halo, and it answers to *fidelity to the Ideal* rather
than to virtue.  A tyrant whose ring stays perfect is entirely possible, and is
a better story than a tyrant whose halo goes out.  Every tell is written so that
it never names the Ideal it belongs to: watching somebody's halo dim tells you
they lied, not that they descend from Justice.

An Aasimar may descend from two Ideals, and then they mix: one lends the
aureola its **form** and the other lends it **colour**.  A halo of pearl fire
that shifts with the mood belongs to Honor and Beauty together, and to nobody
else at the table.

Nothing here is mechanical.  Celestial Revelation carries the rules; this
carries the face.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
	frozen=True,
	)
class Ideal:
	"""One Platonic principle, and the mark it leaves on the mortal wearing it."""

	name: str
	# The shape the aureola takes, phrased so it can follow "an aureola of" or
	# stand as its own sentence.
	form: str
	# What it looks like it is made of.  Two options so that a mixed descent has
	# something to choose between, and so the metals nod at the dwarves without
	# ever confirming anything.
	metal: str
	gem: str
	# What the halo does, never naming the Ideal that causes it.
	tell: str
	# The Muse who holds this domain, where one does.  Some Ideals are older
	# than the Muses and answer to nobody.
	muse: str = ""


IDEALS = {
	record.name: record
	for record in (
		Ideal(
			name="Justice",
			# Justice is blind, so it lives in darkness.
			form="a circle that is perfectly round from wherever anyone stands, which is not how circles work",
			metal="black iron",
			gem="onyx",
			tell="It dims when you lie.",
			muse="History",
			),
		Ideal(
			name="Mercy",
			form="a glow with no edge anywhere, light that simply stops being light",
			metal="gold",
			gem="amber",
			tell="It warms against your scalp when someone near you is afraid.",
			muse="Sacred Song",
			),
		Ideal(
			name="Sacrifice",
			# Blood is red iron.  The metal is the meaning twice over.
			form="a ring with a piece missing, and the gap has never closed",
			metal="red iron",
			gem="ruby",
			tell="It thins when you take something for yourself.",
			muse="Tragedy",
			),
		Ideal(
			name="Truth",
			form="small lights going round it, each on its own patient orbit",
			metal="silver",
			gem="sapphire",
			tell="The lights slow when you are wrong and do not care.",
			muse="Astronomy",
			),
		Ideal(
			name="Freedom",
			# The eclipse: the light is only visible because something stands in
			# front of it.  Verdigris because that is the colour copper goes when
			# it has stood outdoors a long time and nobody has taken it down.
			form="a dark disc with the light escaping all around it, the way the sun looks with the moon in front of it",
			metal="verdigris",
			gem="aquamarine",
			tell="It drifts a hand's width off centre whenever you are told to stay.",
			muse="",
			),
		Ideal(
			name="Beauty",
			form="slow waves of rainbow running round it, one after another",
			metal="pearl",
			gem="opal",
			tell="It brightens when you look at something you like.",
			muse="Love Poetry",
			),
		Ideal(
			name="Hope",
			form="almost nothing in daylight, and unmistakable in the dark",
			metal="tin",
			gem="moonstone",
			tell="It is brightest on the worst nights.",
			muse="Comedy",
			),
		Ideal(
			name="Honor",
			form="a standing flame rather than a ring, burning without moving",
			metal="bronze",
			gem="jade",
			tell="It changes colour with your mood, and you have never been able to stop it.",
			muse="Epic Poetry",
			),
		)
	}


# What the thing you descend from is called, which depends entirely on who is
# telling it.  The Ideal is the same either way.
DESCENTS = (
	"an Angel",
	"a Muse",
	"a Constellation",
	"a Star",
	"a Planet",
	"a Saint of the Higher Planes",
	)


@dataclass(
	frozen=True,
	)
class Perch:
	"""Where the talaria sit, and what they pass for when folded."""

	place: str
	disguise: str


# Only where a wing could take a body's weight: nothing on the face, nothing on
# the front of the chest.
PERCHES = (
	Perch("the back of your neck", "an embroidered collar"),
	Perch("your wrists", "a pair of bracelets"),
	Perch("your forearms", "wound bracers"),
	Perch("your shoulders", "a mantle clasp"),
	Perch("your shoulder blades", "the seams of a toga"),
	Perch("the small of your back", "a wide sash"),
	Perch("the base of your spine, hanging like a short skirt", "a belted overskirt"),
	Perch("your ankles", "anklets"),
	Perch("your heels", "the straps of your sandals"),
	)


# How likely a spark is to come from two Ideals rather than one.
MIXED_DESCENT = 2
SINGLE_DESCENT = 3


@dataclass(
	frozen=True,
	)
class Celestial_Mark:
	"""One Aasimar's visible descent, drawn once and kept."""

	ideals: tuple[Ideal, ...]
	descent: str
	perch: Perch
	# Which Ideal lends the shape, and which lends the colour.  The same Ideal
	# for both when the descent is single.
	shape_from: Ideal
	colour_from: Ideal
	colour: str
	tell: str

	@property
	def names(
			self,
			) -> tuple[str, ...]:
		return tuple(
			ideal.name
			for ideal in self.ideals
			)

	# Which of the sentence patterns below this Aasimar was written with.  Drawn
	# with everything else, so the same Character reads the same way twice.
	voice: int = 0

	@property
	def shade(
			self,
			) -> str:
		"""What the talaria look like they are made of."""
		if len(
			self.ideals
			) > 1:
			return (
				f"{self.ideals[0].metal} shot through with "
				f"{self.ideals[1].metal}"
				)

		return self.ideals[
			0
			].metal

	def descent_line(
			self,
			) -> str:
		"""Where it came from, as whoever tells it would say."""
		held = " and ".join(
			self.names
			)
		patterns = (
			f"You descend from {self.descent} of {held}.",
			f"{_opening(self.descent)} of {held} stands somewhere behind you.",
			f"Whatever is in you came down from {self.descent} of {held}.",
			)

		return patterns[
			self.voice % len(
				patterns
				)
			]

	def talaria(
			self,
			) -> str:
		"""The wings."""
		place = self.perch.place
		disguise = self.perch.disguise
		shade = self.shade
		patterns = (
			f"Your talaria rest at {place}, {shade}, and fold away as "
			f"{disguise}.",
			f"At {place} you carry talaria of {shade}; folded, they pass for "
			f"{disguise}.",
			f"{_opening(shade)} talaria sit at {place}, and anyone who notices "
			f"them takes them for {disguise}.",
			)

		return patterns[
			self.voice % len(
				patterns
				)
			]

	def aureola(
			self,
			) -> str:
		"""The halo, and the one thing it does."""
		form = self.shape_from.form
		patterns = (
			f"Above your head, {self.colour}: {form}. {self.tell}",
			f"Your aureola is {form}, {self.colour} all through. {self.tell}",
			f"{_opening(form)} hangs over you in {self.colour}. {self.tell}",
			)

		return patterns[
			self.voice % len(
				patterns
				)
			]

	def paragraph(
			self,
			) -> str:
		return " ".join(
			(
				self.descent_line(),
				self.talaria(),
				self.aureola(),
				)
			)


def celestial_marks(
		char,
		) -> Celestial_Mark:
	"""
	Draw this Aasimar's visible descent, once and for life.

	The bag is named and level-free, so the same Character is answered the same
	way whenever anybody asks, and a level-up never hands somebody a different
	face.
	"""
	standing = getattr(
		char,
		"celestial_mark",
		None,
		)

	if standing is not None:
		return standing

	dice = char.Dice_Bag(
		"aasimar.descent",
		version="1",
		namespace="GenLegendActor",
		)
	pool = list(
		IDEALS
		)
	first = IDEALS[
		char.Pick(
			pool,
			dice=dice,
			)
		]
	mixed = char.Pick(
		(
			True,
			False,
			),
		(
			MIXED_DESCENT,
			SINGLE_DESCENT,
			),
		dice=dice,
		)
	ideals = (
		first,
		)

	if mixed:
		rest = [
			name
			for name in pool
			if name != first.name
			]
		ideals = (
			first,
			IDEALS[
				char.Pick(
					rest,
					dice=dice,
					)
				],
			)

	# One Ideal lends the shape, the other the colour.  With a single descent
	# both come from the same place and the halo simply looks like itself.
	shape_from = ideals[
		0
		]
	colour_from = ideals[
		-1
		]
	colour = char.Pick(
		(
			colour_from.metal,
			colour_from.gem,
			),
		dice=dice,
		)
	tell = char.Pick(
		[
			ideal.tell
			for ideal in ideals
			],
		dice=dice,
		)
	mark = Celestial_Mark(
		ideals=ideals,
		descent=char.Pick(
			list(
				DESCENTS
				),
			dice=dice,
			),
		perch=char.Pick(
			list(
				PERCHES
				),
			dice=dice,
			),
		shape_from=shape_from,
		colour_from=colour_from,
		colour=colour,
		tell=tell,
		)
	char.celestial_mark = mark

	return mark


__all__ = (
	"Celestial_Mark",
	"DESCENTS",
	"IDEALS",
	"Ideal",
	"PERCHES",
	"Perch",
	"celestial_marks",
	)
