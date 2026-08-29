"""
Map of Traditions — Arcane, Divine, and Primal.

The tradition axis is **independent of Domain** (QST-0048).  An Order of the
Veil may be Arcane, Divine, or Primal for entirely different reasons: one
keeps a laboratory, one keeps a calendar of rites, one keeps a grove.  The
magic barely changes; the world around it changes completely.

The classification is the D&D One playtest split, used here as a project
axis, not as a 2024 rule.

Two working purposes:

1. **Prose.** ``places`` and ``practices`` are phrased to be leaked into a
   sentence rather than listed, so a reader learns the world sideways.
2. **Safety.** ``fallback`` guarantees a non-empty spell pool when a Domain's
   own list runs thin, so the generator can never emit an empty list.
"""

from __future__ import annotations

from AtlasLusoris.AtlasOfOrders.Grimoire_of_Orders import Tradition
from AtlasMagia.Lodge_of_Spells import (
	Alarm,
	Blur,
	Barkskin,
	Bless,
	CalmEmotions,
	ConjureAnimals,
	Counterspell,
	CureWounds,
	DetectMagic,
	DetectThoughts,
	DispelMagic,
	EnhanceAbility,
	FogCloud,
	Identify,
	LesserRestoration,
	Levitate,
	Longstrider,
	SeeInvisibility,
	Sanctuary,
	SpeakwithAnimals,
	ZoneOfTruth,
	)


ARCANE = Tradition(
	name="Arcane",
	places=(
		"a workshop above a shop that sells something else entirely",
		"a reading room with more locks on the inside than the outside",
		"a cellar where the chalk is never fully scrubbed away",
		"three rented rooms in three cities, and only one of them real",
		"a lecture hall that is used for lectures, most nights",
		),
	practices=(
		"everything is written down twice and one copy is destroyed",
		"nobody is admitted who cannot demonstrate the work, whatever their name",
		"the tools are inventoried aloud before and after, every time",
		"an examination, once, and it is not repeated for anyone",
		"the youngest present always speaks first, so seniority cannot lean on the answer",
		),
	organizations=(
		"Academy",
		"Cabal",
		"Athenaeum",
		"Conservatory",
		"Society",
		"Institute",
		),
	devotions=(
		"a sorcerer four centuries dead whose notes are still being argued over",
		"a theorem that turned out to be a door",
		"the First Experiment, which nobody will describe",
		"a name that is written but never said",
		"an equation the founder solved and then hid",
		),
	fallback={
		1: (
			DetectMagic,
			Identify,
			),
		2: (
			Blur,
			Levitate,
			SeeInvisibility,
			),
		3: (
			Counterspell,
			DispelMagic,
			),
		},
	)


DIVINE = Tradition(
	name="Divine",
	places=(
		"a back room behind a public shrine, reached through the kitchen",
		"a chapel that keeps its doors open and its crypt closed",
		"a temple with one altar nobody is allowed to tend",
		"a hospice whose upper floor has no stair anyone will point out",
		"a roadside shrine that is repaired far more often than its traffic explains",
		),
	practices=(
		"the rites are kept exactly, including the ones nobody can explain any more",
		"a fast before any decision that cannot be undone",
		"confession to one other member, never to a superior",
		"the calendar governs everything, and the calendar is not negotiable",
		"a name is spoken aloud at every meeting so that it is never forgotten",
		),
	organizations=(
		"Temple",
		"Order",
		"Choir",
		"Congregation",
		"Sanctum",
		"Fellowship",
		),
	devotions=(
		"a god with a public face and a second, older one",
		"a saint the church struck from its own rolls",
		"the honored dead, who are consulted and occasionally answer",
		"an angel that has not been seen since the founding and is still expected",
		"a covenant signed by people whose descendants have all forgotten it",
		),
	fallback={
		1: (
			Bless,
			CureWounds,
			Sanctuary,
			),
		2: (
			CalmEmotions,
			LesserRestoration,
			ZoneOfTruth,
			),
		3: (
			DispelMagic,
			),
		},
	)


PRIMAL = Tradition(
	name="Primal",
	places=(
		"a stand of trees that is older than the field around it and has never been cleared",
		"a spring that is kept clean by people nobody sees doing it",
		"a stone circle a village walks around rather than through",
		"a hill farm whose barn is much older than its house",
		"a cave mouth with offerings at it that are always fresh",
		),
	practices=(
		"nothing is written; it is walked, and shown, and walked again",
		"the season decides when the order meets, not the order",
		"a share of everything taken is left where it was taken from",
		"the eldest present is asked last, so the young commit before they are corrected",
		"members are known by what they carry, not by what they say",
		),
	organizations=(
		"Circle",
		"Grove",
		"Kinship",
		"Lodge",
		"Brotherhood",
		"Covenant",
		),
	devotions=(
		"a beast that is always described the same way by people who have never met",
		"the land itself, which is owed and does the owing",
		"a river with opinions, and a long memory for insults",
		"the first ancestor, who is spoken of as though still on the road",
		"a season that arrives late and is negotiated with",
		),
	fallback={
		1: (
			Longstrider,
			SpeakwithAnimals,
			),
		2: (
			Barkskin,
			EnhanceAbility,
			FogCloud,
			),
		3: (
			ConjureAnimals,
			),
		},
	)


TRADITIONS = (
	ARCANE,
	DIVINE,
	PRIMAL,
	)


# Any Order may wear any of these; the tradition pools are additions, not walls.
COMMON_ORGANIZATIONS = (
	"Brotherhood",
	"Order",
	"House",
	"Company",
	"Lodge",
	)


__all__ = (
	"ARCANE",
	"COMMON_ORGANIZATIONS",
	"DIVINE",
	"PRIMAL",
	"TRADITIONS",
	)
