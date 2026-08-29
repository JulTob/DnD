"""
Grimoire of Orders — the authoring records for generated Secret Orders.

Three record shapes, and nothing else:

	Facet     one face a Domain can turn (a creed and a goal)
	Domain    a mythic sphere: its facets, its three feat slots, its words
	Tradition Arcane / Divine / Primal — places, practices, and a safe pool

An Order is not stored here.  It is collapsed per Character by OrderKit from
these records, so two Characters never receive the same one.

Design notes that outlive any single record (QST-0048):

* Domains are **tagged, not ranked**.  An Order simply has two of them.  Some
  come to Hera for vengeance on a cruel husband and some for the safety of the
  house; neither is her first function.
* Domains are **mythic, never job descriptions**.  "Hospitality" is a trade;
  ``Home`` is a domain, and every pantheon keeps one.
* A domain **turns several faces**.  The same sphere gives sanctuary-keepers
  and the order that offers a last warm night before the knife.
* Tradition is an **independent axis**.  An Order of the Veil may be Arcane,
  Divine, or Primal for entirely different reasons, and its practices change
  completely while its magic does not.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(
	frozen=True,
	)
class Facet:
	"""One face a Domain turns: what it believes, and what it therefore wants."""

	name: str
	creed: str
	goal: str


@dataclass(
	frozen=True,
	)
class Domain:
	"""
	A mythic sphere an Order is sworn to.

	``mark`` records which published Dragonmark the mechanical slots were
	patterned after, so provenance stays greppable while the surface name
	stays mythic.

	The three slots mirror the published template exactly:
	``intuition_die`` (a d4 on named checks), ``signature_magic``
	(a cantrip plus one always-prepared spell), and ``spells_of_the_order``
	(the levelled list added to a caster's own).
	"""

	name: str
	mark: str
	checks: tuple[str, ...]
	cantrip: object
	prepared: object
	spells_of_the_order: dict[int, tuple]
	facets: tuple[Facet, ...]
	perks: tuple[str, ...]
	sacrifices: tuple[str, ...]
	descriptors: tuple[str, ...]
	cores: tuple[str, ...]
	relics: tuple[str, ...] = field(
		default_factory=tuple,
		)


@dataclass(
	frozen=True,
	)
class Tradition:
	"""
	How an Order works its magic, and therefore how it lives.

	``places`` and ``practices`` are written to be *leaked* into prose rather
	than listed: a line about a back room in a temple teaches that the temple
	is public without ever saying so.
	"""

	name: str
	places: tuple[str, ...]
	practices: tuple[str, ...]
	organizations: tuple[str, ...]
	devotions: tuple[str, ...]
	fallback: dict[int, tuple]


__all__ = (
	"Domain",
	"Facet",
	"Tradition",
	)
