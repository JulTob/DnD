"""
What answers a Paladin's oath and agrees to carry it.

Find Steed lets a player choose Celestial, Fey or Fiendish at the table. A
generated sheet may not print that choice: Canon/Feature-Text forbids
open-choice language, because every pick was already made inside a seeded Dice
Bag before the page existed. So the kind is drawn, and the sheet names what
came.

Drawing it is not a workaround. It is the better fantasy. The Paladin's power
is downstream of a word, and the steed is the first thing in the rules that
answers the word rather than the person: you did not summon a servant, you
said something once and something agreed with it. Which is why the kind
follows the **Oath** and not the Character's alignment, species or manners.

Two rules govern the pool, in the shape Map_of_Spellbooks fixed for the
Wizard's book.

**The oath is answered in its own nature.** What you swore to is what comes.
A vow sworn to the green is met by something out of the green; a vow sworn
against is met by something that collects. This is the Familial Preference the
Pact of the Chain familiars already use, asked of an Oath instead of a patron.

**Nothing is excluded.** A weight is not a gate. A Devotion Paladin can be
answered by something Fiendish, and the rules deliberately allow it: they
refuse to say the steed must be holy. When it happens it is a story, and the
sheet states it without apology or explanation.
"""

from __future__ import annotations

from dataclasses import dataclass


CELESTIAL = "Celestial"
FEY = "Fey"
FIENDISH = "Fiendish"


# How much the oath's own nature outweighs the other two. High enough that the
# pairing reads as a rule at the table, low enough that roughly one Paladin in
# nine is answered by something nobody expected. Same reasoning, and the same
# number, as AFFINITY_WEIGHT in Map_of_Familiars.
OATH_AFFINITY_WEIGHT = 8


@dataclass(
	frozen=True,
	slots=True,
	)
class Steed_Form:
	"""One way a steed can arrive. ``shape`` completes 'and it came as ...'."""

	kind: str
	shape: str


# What each Oath is answered by when the oath is answered in its own nature.
# Devotion and Glory share the Celestial for different reasons: one swore to a
# way of being that keeps its word, the other swore to be worth telling, and a
# story gives its hero a white horse.
OATH_NATURE = {
	"Devotion": CELESTIAL,
	"Ancients": FEY,
	"Glory": CELESTIAL,
	"Vengeance": FIENDISH,
	}


STEED_FORMS: tuple[Steed_Form, ...] = (
	Steed_Form(
		CELESTIAL,
		"a white warhorse whose hooves leave no mark on wet ground",
		),
	Steed_Form(
		CELESTIAL,
		"a stag the height of a horse, carrying its head as though it were "
		"being measured",
		),
	Steed_Form(
		CELESTIAL,
		"a lion that has never once roared in your hearing",
		),
	Steed_Form(
		CELESTIAL,
		"a bull the colour of the hour before dawn, warm to stand beside",
		),
	Steed_Form(
		FEY,
		"a grey mare who will not cross running water until she is asked "
		"politely",
		),
	Steed_Form(
		FEY,
		"a stag whose antlers are in leaf, out of season, always",
		),
	Steed_Form(
		FEY,
		"an elk out of the deep wood, with moss grown into its back where a "
		"saddle sits",
		),
	Steed_Form(
		FEY,
		"a horse the colour of river water, which is a different colour in "
		"the morning",
		),
	Steed_Form(
		FIENDISH,
		"a black horse that breathes smoke in cold air, and in warm air too",
		),
	Steed_Form(
		FIENDISH,
		"a goat built to the size of a destrier, with a destrier's patience "
		"and none of its temper",
		),
	Steed_Form(
		FIENDISH,
		"a hound you can sit astride, which watches the road behind you "
		"without being told",
		),
	Steed_Form(
		FIENDISH,
		"a ram with horns that ring like struck iron when it turns its head",
		),
	)


def _oath_of(
		char,
		) -> str | None:
	"""The Oath this Character swore, by name, or None before it is chosen."""
	for attribute in (
			"specialization",
			"Specialization",
			"subclass",
			"Subclass",
			):
		value = getattr(
				char,
				attribute,
				None,
				)
		if isinstance(
				value,
				str,
				) and value:
			return value
	return None


def _forms_of_kind(
		kind: str,
		) -> tuple[Steed_Form, ...]:
	"""Every shape recorded for one kind of steed."""
	return tuple(
		form
		for form in STEED_FORMS
		if form.kind == kind
		)


def Draw_Steed(
		char,
		) -> str:
	"""
	Settle what answered this Paladin's oath, once.

	Called from the Faithful Steed lesson's ``apply``, never from its Entry.
	An Entry that draws re-draws on every read of the sheet, which is the
	Primal Order mistake recorded in Canon/Feature-Text.
	"""
	standing = getattr(
			char,
			"paladin_steed",
			None,
			)
	if standing:
		return standing

	kind = _draw_kind(
			char,
			)
	shape = _draw_shape(
			char,
			kind,
			)
	answer = f"{kind}: {shape}"
	char.paladin_steed = answer
	return answer


def _draw_kind(
		char,
		) -> str:
	"""
	Which of the three kinds answered, weighted by the Oath's nature.

	Before an Oath is sworn there is nothing for the weight to prefer, so the
	three kinds come up evenly. That is the right answer rather than a
	fallback: an unsworn Paladin has not yet said the thing the steed
	answers. In practice Faithful Steed is a level 5 lesson and the Oath
	lands at 3, so this is only reachable off the Guild's own ladder.
	"""
	native = OATH_NATURE.get(
			_oath_of(
				char
				),
			)
	kinds = [
		CELESTIAL,
		FEY,
		FIENDISH,
		]
	weights = [
		OATH_AFFINITY_WEIGHT
		if kind == native
		else 1
		for kind in kinds
		]

	return char.Pick(
			kinds,
			weights,
			dice=char.Dice_Bag(
				"paladin.steed.kind",
				version="1",
				namespace="GenLegendLusoris",
				),
			)


def _draw_shape(
		char,
		kind: str,
		) -> str:
	"""What that kind of thing looks like when it arrives."""
	pool = _forms_of_kind(
			kind,
			)
	form = char.Pick(
			list(
				pool
				),
			dice=char.Dice_Bag(
				"paladin.steed.shape",
				version="1",
				namespace="GenLegendLusoris",
				),
			)

	return form.shape


def Steed_Sentence(
		char,
		) -> str:
	"""
	The drawn steed as one sentence, for the Faithful Steed Entry.

	Reads the settled record and never draws, because an Entry that decides
	re-decides on every read of the sheet (Canon/Feature-Text).

	The fallback is for the case where the lesson's ``apply`` has not run,
	which TrainingKit does not allow: it applies before it grants. It states
	that something answered rather than offering the three kinds back, so
	even the unreachable branch keeps the no-open-choice law.
	"""
	answer = getattr(
			char,
			"paladin_steed",
			None,
			)
	if not answer:
		return "Your steed answered the oath."

	kind, _, shape = answer.partition(
			": ",
			)

	return f"Your steed is <b>{kind}</b>, and it came as {shape}."


__all__ = (
	"CELESTIAL",
	"FEY",
	"FIENDISH",
	"OATH_AFFINITY_WEIGHT",
	"OATH_NATURE",
	"STEED_FORMS",
	"Steed_Form",
	"Draw_Steed",
	"Steed_Sentence",
	)
