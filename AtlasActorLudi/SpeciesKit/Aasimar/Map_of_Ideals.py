"""
Map of Ideals — what an Aasimar descends from, and how it shows.

A Celestial is an Ideal with a shape: not a god and not a servant of one, but Justice itself, or Mercy, or Honor, standing where mortals can see it.  An Aasimar carries a spark of one, and the spark is visible in two places.

**Talaria** are the small vestigial wings.  They sit only where a wing could plausibly take a body's weight, which is why none of them are on the face or the front of the chest, and each folds into something a tailor could explain: a torc, a sash, an embroidered collar.

**The aureola** is the halo, and it answers to *fidelity to the Ideal* rather than to virtue.  A tyrant whose ring stays perfect is entirely possible, and is a better story than a tyrant whose halo goes out.  Every tell is written so that it never names the Ideal it belongs to: watching somebody's halo dim tells you they lied, not that they descend from Justice.

An Aasimar may descend from two Ideals, and then they mix on three axes that are drawn apart: one lends the aureola its **form**, either lends the **gem** it glows like, and either lends the **tell**.  Honor's standing flame, glowing like Beauty's opal, beating once when you see something you like, belongs to that pair and to nobody else at the table.

Nothing here is mechanical. Celestial Revelation carries the rules; this carries the face.
"""

from __future__ import annotations

from dataclasses import dataclass


def _opening(
		phrase: str,
		) -> str:
	"""A phrase promoted to the start of a sentence, capital and all."""
	return phrase[
		:1
		].upper() + phrase[
		1:
		]


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
			form="a circle perfectly round from wherever anyone stands",
			metal="black iron",
			gem="onyx",
			tell="It dims when you are not being honest.",
			muse="History",
			),
		Ideal(
			name="Mercy",
			form="a glow with no edge, light that fades",
			metal="gold",
			gem="amber",
			tell="When someone near you is afraid, it sends a cold feeling down your spine.",
			muse="Sacred Song",
			),
		Ideal(
			name="Sacrifice",
			# Blood is red iron.  The metal is the meaning twice over.
			form="a broken ring, with an arc of it missing",
			metal="red iron",
			gem="ruby",
			tell="It darkens for a moment whenever you see someone die.",
			muse="Tragedy",
			),
		Ideal(
			name="Truth",
			form="a ring of small lights, each orbiting on its own",
			metal="silver",
			gem="diamond",
			tell="It falls into chaos when you feel anything strongly, good or bad.",
			muse="Astronomy",
			),
		Ideal(
			name="Freedom",
			# Verdigris because that is the colour copper goes when it has
			# stood outdoors a long time and nobody has taken it down.
			form="a star of many points, set like a compass rose",
			metal="verdigris",
			gem="aquamarine",
			tell="It twinkles when you run, and harder when you fly.",
			muse="",
			),
		Ideal(
			name="Beauty",
			form="slow waves of colour, one running after another",
			metal="pearl",
			gem="opal",
			tell="It beats once when you look at something you find beautiful.",
			muse="Love Poetry",
			),
		Ideal(
			name="Hope",
			form="a faint thing in daylight and one unmistakable star in the dark",
			metal="tin",
			gem="moonstone",
			tell="When you are happy it spreads, slowly, until it covers all of you.",
			muse="Comedy",
			),
		Ideal(
			name="Honor",
			form="a standing flame that burns without moving",
			metal="bronze",
			gem="jade",
			tell="Its colour changes with your mood.",
			muse="Epic Tales",
			),
		)
	}


@dataclass(
	frozen=True,
	)
class Descent:
	"""A kind of Celestial, and the ones anybody can name.

	These are *categories*, not a ladder.  An Angel does not answer to a
	Seraph and a Muse is not junior to a Planetar: they are different sorts of
	thing, drawn from three mythologies, and none of them outranks another.
	"""

	kind: str
	names: tuple[str, ...]


# What the thing you descend from is called, which depends entirely on who is
# telling it.  The Ideal is the same either way.
DESCENTS = (
	Descent(
		kind="Angel",
		names=(
			"Raziel",
			"Camael",
			"Haniel",
			"Jofiel",
			"Barakiel",
			"Sealtiel",
			"Raguel",
			"Sariel",
			),
		),
	Descent(
		kind="Muse",
		names=(
			"Calliope",
			"Clio",
			"Erato",
			"Euterpe",
			"Melpomene",
			"Polihimnia",
			"Terpsicore",
			"Talia",
			"Urania",
			),
		),
	Descent(
		kind="Constellation",
		names=(
			"Cassiopeia",
			"Andromeda",
			"Lyra",
			"Draco",
			"Perseus",
			"Aquila",
			"Corvus",
			"Cignus",
			"Carina",
			),
		),
	Descent(
		kind="Star",
		names=(
			"Polaris",
			"Vega",
			"Sirius",
			"Altair",
			"Antares",
			"Rigel",
			"Deneb",
			"Arcturus",
			"Spica",
			"Canopus",
			),
		),
	Descent(
		# The wandering stars, under the names the Greeks gave them.
		kind="Planetar",
		names=(
			"Lucifer",
			"Hesperus",
			"Fosforos",
			"Eosforus",
			"Hesperus",
			"Piroeis",
			"Faezon",
			"Stilbon",
			"Fainon",
			"Ermis",
			"Aris",
			"Saturnus",
			"Ploutunas",
			),
		),
	Descent(
		kind="Throne",
		names=(
			"Zafkiel",
			"Ofaniel",
			"Orifiel",
			"Galgaliel",
			),
		),
	# The burning ones.
	Descent(
		kind="Seraph",
		names=(
			"Serafiel",
			"Jehoel",
			"Kemuel",
			"Nazanael",
			),
		),
	Descent(
		# Sphinxes wear the names of the things they guard.
		kind="Sphinx",
		names=(
			"Aramakis",
			"Memoris",
			"Mnemosine",
			"Sofrosine",
			"Ananke",
			"Metis",
			"Peizo",
			"Nemesis",
			"Temis",
			"Eleos",
			"Tisia",
			"Aletia",
			"Eleuteria",
			"Aglaya",
			"Elpis",
			"Aidos",
			"Dike",
			),
		),
	)


# How two metals share one pair of wings.  {a} is the first Ideal's metal and
# {b} is the second's; the drawing picks the arrangement.
PLUMAGES = (
	"{a} on the back and {b} beneath",
	"{a} at the base, running to {b} at the tips",
	"{a}, every feather edged in {b}",
	"{a}, barred across with {b}",
	"{a}, speckled with {b}",
	"{a} above, and {b} that only shows when they open",
	"{a} with one band of {b} across them",
	)

# And how one metal wears them alone.
SINGLE_PLUMAGES = (
	"{a}",
	"{a}, darker at the tips",
	"{a}, paler underneath",
	"{a} all the way through",
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
	Perch("the base of your spine", "a belted overskirt"),
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
	"""
	One Aasimar's visible descent, drawn once and kept.

	Two axes, deliberately separate.  The talaria take their **metal** and the aureola takes its **gem**, so a silver-winged aasimar under a ruby halo is a different creature from a red-iron-winged one under diamond, and neither is a restatement of the other.  Nothing is *made* of either: the wings shine like a metal and the halo glows like a stone.  Comparison, not actual material.
	"""

	ideals: tuple[Ideal, ...]
	# "the Muse Talia": kind and name spoken together, article included.
	ancestor: str
	perch: Perch
	plumage: str
	# Which Ideal lends the aureola its form, and which the gem it glows like.
	shape_from: Ideal
	glow_from: Ideal
	# What the halo does, drawn from either Ideal, never naming it.
	tell: str
	# His, her, their, or its: how the ancestor's line is spoken of.
	ancestor_possessive: str
	# Which of the sentence patterns below this Aasimar was written with.  Drawn
	# with everything else, so the same Character reads the same way twice.
	voice: int = 0
	arrangement: int = 0

	@property
	def names(
			self,
			) -> tuple[str, ...]:
		return tuple(
			ideal.name
			for ideal in self.ideals
			)

	@property
	def metal(
			self,
			) -> str:
		"""What the talaria catch the light like."""
		return self.plumage.format(
			a=self.ideals[
				0
				].metal,
			b=self.ideals[
				-1
				].metal,
			)

	@property
	def gem(
			self,
			) -> str:
		"""What the aureola glows like."""
		if len(
			self.ideals
			) > 1:
			return (
				f"{self.ideals[0].gem} shading into "
				f"{self.ideals[1].gem}"
				)

		return self.ideals[
			0
			].gem

	def _pick(
			self,
			patterns: tuple[str, ...],
			) -> str:
		return patterns[
			self.voice % len(
				patterns
				)
			]

	def opening(
			self,
			) -> str:
		"""The line that names the ancestor, before the marks are described."""
		return self._pick(
			(
				f"The marks suggest a tie to {self.ancestor}; you may belong to "
				f"{self.ancestor_possessive} lineage.",
				f"Your talaria and aureola resemble the traits of "
				f"{self.ancestor}, so you may belong to "
				f"{self.ancestor_possessive} lineage.",
				f"Whatever is in you resembles {self.ancestor}; you may have a place in "
				f"{self.ancestor_possessive} lineage.",
				)
			)

	def closing(
			self,
			) -> str:
		"""The same line, said after the marks instead of before."""
		return self._pick(
			(
				f"These are the traits of {self.ancestor}, so you may belong to "
				f"{self.ancestor_possessive} lineage.",
				f"Together, these marks resemble {self.ancestor}; you may belong to "
				f"{self.ancestor_possessive} lineage.",
				f"They echo the signs of {self.ancestor}, so you may have a place in "
				f"{self.ancestor_possessive} lineage.",
				)
			)

	def talaria(
			self,
			) -> str:
		"""The wings."""
		place = self.perch.place
		disguise = self.perch.disguise
		metal = self.metal

		return self._pick(
			(
				f"Your talaria rest at {place} and fold away as {disguise}, shining like {metal}.",
				f"At {place} you carry talaria that catch the light like {metal}, and folded they pass for {disguise}.",
				f"Talaria sit at {place}, shining like {metal}, and whoever notices takes them for {disguise}.",
				f"Most people wouldn't suspect your {disguise} actually hide talarian wings, as its shining surface resembles {metal}, and they rest comfortably at {place}",
				)
			)

	def aureola(
			self,
			) -> str:
		"""The halo, and the one thing it does."""
		form = self.shape_from.form
		gem = self.gem

		return self._pick(
			(
				f"Above your head, {form}, glowing like {gem}. {self.tell}",
				f"Your aureola is {form}, and it glows like {gem}. {self.tell}",
				f"Floating behind your head, your aureola is {form}, lit like {gem}. {self.tell}",
				f"Suspended above your head like a dim reflection, your aureola is {form}, lit like {gem}. {self.tell}",
				)
			)

	def paragraph(
			self,
			) -> str:
		"""
		The three sentences, in the order this Aasimar was drawn with.

		Four arrangements, so two Aasimar at one table do not read as the
		same hand.
		"""

		arrangements = (
			(
				self.opening(),
				self.talaria(),
				self.aureola(),
				),
			(
				self.talaria(),
				self.aureola(),
				self.closing(),
				),
			(
				self.aureola(),
				self.talaria(),
				self.closing(),
				),
			(
				self.opening(),
				self.aureola(),
				self.talaria(),
				),
			)

		return " ".join(
			arrangements[
				self.arrangement % len(
					arrangements
					)
				]
			)


def celestial_marks(
		char,
		) -> Celestial_Mark:
	"""
	Draw this Aasimar's visible descent, once and for life.

	The bag is named and level-free, so the same Character is answered the same way whenever anybody asks, and a level-up never hands somebody a different face.
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

	# The form and the glow; with a single descent both are the same Ideal.
	shape_from = ideals[
		0
		]
	glow_from = ideals[
		-1
		]
	kind = char.Pick(
		list(
			DESCENTS
			),
		dice=dice,
		)
	pronoun_dice = char.Dice_Bag(
		"aasimar.descent.ancestor_possessive",
		version="1",
		namespace="GenLegendActor",
		)
	mark = Celestial_Mark(
		ideals=ideals,
		# The kind and one of its names, told together the way anyone would.
		ancestor=f"the {kind.kind} "
		+ char.Pick(
			list(
				kind.names
				),
			dice=dice,
			),
		perch=char.Pick(
			list(
				PERCHES
				),
			dice=dice,
			),
		plumage=char.Pick(
			list(
				PLUMAGES
				if mixed
				else SINGLE_PLUMAGES
				),
			dice=dice,
			),
		shape_from=shape_from,
		glow_from=glow_from,
		# The tell is its own draw.  Either Ideal may lend it, so two Aasimar
		# sharing a pair can still read differently: same form, same glow,
		# different habit.
		tell=char.Pick(
			[
				ideal.tell
				for ideal in ideals
				],
			dice=dice,
			),
		ancestor_possessive=char.Pick(
			(
				"his",
				"her",
				"their",
				"its",
				),
			dice=pronoun_dice,
			),
		voice=char.Pick(
			(
				0,
				1,
				2,
				),
			dice=dice,
			),
		arrangement=char.Pick(
			(
				0,
				1,
				2,
				3,
				),
			dice=dice,
			),
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
