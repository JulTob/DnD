"""
Venustas — the aesthetic layer: self-formatting display primitives.

``Entry`` and ``Chip`` each *are* their own HTML (they subclass ``str``), so a
value drops straight into any sheet without a render function. Richer shapes
come from the format spec or the matching methods — HTML is the default, with an
explicit ``html`` spec too, so new code can be deliberate::

    f"{entry}"        -> HTML   (default)
    f"{entry:html}"   -> HTML   (explicit; redundant on purpose)
    f"{entry:md}"     -> Markdown
    f"{entry:plain}"  -> bare text
    entry.html() / entry.md() / entry.plain()

``kind`` self-classifies the item (Feature / Trait / Attribute …) for sheet
placement and ``if "…" in char`` target filters.
"""

from __future__ import annotations

import re


def _html_to_md(
		text: str,
		) -> str:
	"""Fold the light HTML our text carries (<br>, <b>, <i>, …) into Markdown."""
	text = re.sub(r"<br\s*/?>", "\n", str(text))
	text = re.sub(r"</?b>", "**", text)
	text = re.sub(r"</?i>", "*", text)
	text = re.sub(r"</?(p|ul|li|div|h[1-6])[^>]*>", "\n", text)
	text = re.sub(r"<[^>]+>", "", text)
	return re.sub(r"\n{3,}", "\n\n", text).strip()


def _strip_html(
		text: str,
		) -> str:
	return re.sub(r"<[^>]+>", "", str(text)).strip()


# ---------------------------------------------------------------------------
# Decorative glyph pools (for Entry symbols)
# ---------------------------------------------------------------------------
# Browser safety by Unicode block (for "renders everywhere"):
#   runes    U+16A0–16FF   — BMP, widely supported
#   dingbats U+2700–27BF   — oldest, near-universal
#   pictos   U+2600–26FF   — misc symbols, widely supported
#   alchemy  U+1F700–1F77F — astral plane, MODERN ONLY (may tofu on old fonts)

RUNES = "ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛊᛏᛒᛖᛗᛚᛜᛞᛟ"
DINGBATS = "✦✧✶✷✸✹✺✳✴❂❈❊✪✫✬✭✮✯❋❉"
PICTOGRAPHS = "★☆☉☽☾⚝♁♆⚹✵❁❂"
ALCHEMY = "🜀🜁🜂🜃🜄🜅🜆🜇🜈🜉🜊🜋🜍🜎🜏🜔🜕🜖🜚🜛"
GREEK = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"          # BMP, universal — classical vibe
TRIGRAMS = "☰☱☲☳☴☵☶☷"                        # BMP, universal — I Ching bāguà

# Default pool keeps to the near-universal blocks; MYSTIC adds alchemy for
# modern-only targets where the astral-plane glyphs are safe. (Old Italic,
# Phoenician, Old Hungarian, Old Persian, tetragrams live on the astral plane
# too and tofu on most systems — add them the same way when targeting modern.)
GLYPHS = RUNES + DINGBATS + PICTOGRAPHS
MYSTIC = GLYPHS + ALCHEMY


def glyph(
		seed="",
		pool: str = GLYPHS,
		) -> str:
	"""Pick one decorative glyph, deterministically from ``seed``.

	Seeding by an Entry title or a character seed means the same thing always
	draws the same glyph — stable across re-renders, unlike a fresh random
	pick. Pass ``MYSTIC`` for the alchemy-inclusive pool.
	"""
	if not pool:
		return ""

	index = sum(
		ord(character)
		for character in str(seed)
		) % len(pool)
	return pool[index]


# ---------------------------------------------------------------------------
# Symbol libraries per class / species — a character draws its glyphs from a
# pool that fits it. Kept to the near-universal blocks so they always render;
# swap in ALCHEMY / ancient scripts per taste on modern-only targets.
# ---------------------------------------------------------------------------
LIBRARIES = {
	# Classes / guilds
	"Wizard": GREEK, "Sorcerer": GREEK, "Mage": GREEK, "Bard": GREEK,
	"Scholar": GREEK, "Mentor": GREEK,
	"Cleric": PICTOGRAPHS, "Priest": PICTOGRAPHS, "Paladin": PICTOGRAPHS,
	"Healer": PICTOGRAPHS, "Shaman": PICTOGRAPHS,
	"Druid": RUNES, "Ranger": RUNES, "Hunter": RUNES, "Barbarian": RUNES,
	"Fighter": RUNES, "Soldier": RUNES, "Warrior": RUNES, "Knight": RUNES,
	"Guardian": RUNES,
	"Warlock": TRIGRAMS, "Witch": TRIGRAMS, "Monk": TRIGRAMS, "Cultist": TRIGRAMS,
	"Rogue": DINGBATS, "Spy": DINGBATS, "Ninja": DINGBATS, "Trickster": DINGBATS,
	"Bandit": DINGBATS, "Pirate": DINGBATS,
	# Species / creature types
	"Dwarf": RUNES, "Goliath": RUNES, "Orc": RUNES, "Goblin": RUNES,
	"Elf": GREEK, "Gnome": GREEK,
	"Human": DINGBATS, "Halfling": DINGBATS,
	"Aasimar": PICTOGRAPHS, "Celestial": PICTOGRAPHS,
	"Tiefling": TRIGRAMS, "Fiend": TRIGRAMS, "Dragonborn": TRIGRAMS,
	"Dragon": TRIGRAMS, "Undead": TRIGRAMS, "Vampire": TRIGRAMS,
	}


def library_for(
		*keys,
		default: str = GLYPHS,
		) -> str:
	"""Return the glyph pool for the first matching class/species key."""
	for key in keys:
		pool = LIBRARIES.get(
			str(key)
			)
		if pool:
			return pool
	return default


def glyph_for(
		seed,
		*keys,
		default: str = GLYPHS,
		) -> str:
	"""Pick a glyph for ``seed`` from the library of the first matching key.

	e.g. ``glyph_for(feature_title, char.char_class, char.species)`` draws from
	the character's class pool first, then species, then the neutral default.
	"""
	return glyph(
		seed,
		library_for(
			*keys,
			default=default,
			),
		)


# ---------------------------------------------------------------------------
# Spell / section ornaments — one mark per Character, genus by identity
# ---------------------------------------------------------------------------
# A Character keeps the *same* ornament between every spell card.  The genus
# narrows the alphabet by Guild / Species / Background so a Druid and a
# Warlock do not draw from the same set.  Add combo rows to GENERA to refine.

ORNAMENTS = (
	"✿",
	"❀",
	"❂",
	"☣",
	"♾",
	"✵",
	"✯",
	"✧",
	"✦",
	"❖",
	"⛤",
	"⛥",
	"哈里",
	"⛧",
	"❁",
	"❋",
	"❉",
	"✶",
	"✸",
	"☽",
	"☾",
	"★",
	)

# Keys are (guild, species, background).  ``None`` is a wildcard on that axis.
# More-specific rows win; extend this table as combos want their own alphabet.
GENERA: dict[
	tuple[str | None, str | None, str | None],
	tuple[str, ...],
	] = {
	# Guild defaults
	(
		"Druid",
		None,
		None,
		): (
			"✿",
			"❀",
			"❁",
			"✵",
			"❂",
			"❋",
			),
	(
		"Ranger",
		None,
		None,
		): (
			"✿",
			"❀",
			"✵",
			"✧",
			"✯",
			),
	(
		"Warlock",
		None,
		None,
		): (
			"⛤",
			"⛥",
			"⛧",
			"हरण",
			"♾",
			"☽",
			),
	(
		"Wizard",
		None,
		None,
		): (
			"✧",
			"✦",
			"❖",
			"✵",
			"♾",
			"✶",
			),
	(
		"Sorcerer",
		None,
		None,
		): (
			"✦",
			"✧",
			"❂",
			"♾",
			"✸",
			),
	(
		"Cleric",
		None,
		None,
		): (
			"✦",
			"✧",
			"❂",
			"✵",
			"★",
			),
	(
		"Paladin",
		None,
		None,
		): (
			"✦",
			"✧",
			"❂",
			"✵",
			"★",
			),
	(
		"Bard",
		None,
		None,
		): (
			"✧",
			"✦",
			"❀",
			"✵",
			"✯",
			),
	(
		"Monk",
		None,
		None,
		): (
			"✦",
			"✧",
			"❖",
			"✵",
			"♾",
			),
	# Background accents (any guild / species)
	(
		None,
		None,
		"Spellfire Initiate",
		): (
			"✦",
			"✧",
			"❂",
			"♾",
			"✵",
			"✸",
			),
	# Combo — Human Spellfire Druid leans radiant / weave marks
	(
		"Druid",
		"Human",
		"Spellfire Initiate",
		): (
			"✦",
			"❂",
			"♾",
			"✧",
			"✵",
			"✸",
			),
	}


def _identity_key(
		value: str | None,
		) -> str | None:
	if value is None:
		return None
	text = str(
		value
		).strip()
	return text or None


def genus(
		guild: str | None = None,
		species: str | None = None,
		background: str | None = None,
		*,
		default: tuple[str, ...] = ORNAMENTS,
		) -> tuple[str, ...]:
	"""Return the ornament alphabet for this identity combo.

	Looks up ``GENERA`` from most specific to least::

	    (guild, species, background)
	    (guild, species, None)
	    (guild, None, background)
	    (None, species, background)
	    (guild, None, None)
	    (None, species, None)
	    (None, None, background)

	Add rows to ``GENERA`` to personalize a class/species/bg pairing.
	"""
	guild_key = _identity_key(
		guild
		)
	species_key = _identity_key(
		species
		)
	background_key = _identity_key(
		background
		)

	for key in (
		(
			guild_key,
			species_key,
			background_key,
			),
		(
			guild_key,
			species_key,
			None,
			),
		(
			guild_key,
			None,
			background_key,
			),
		(
			None,
			species_key,
			background_key,
			),
		(
			guild_key,
			None,
			None,
			),
		(
			None,
			species_key,
			None,
			),
		(
			None,
			None,
			background_key,
			),
		):
		if key == (
			None,
			None,
			None,
			):
			continue
		pool = GENERA.get(
			key
			)
		if pool:
			return pool

	return default


def ornament_for(
		seed="",
		*,
		guild: str | None = None,
		species: str | None = None,
		background: str | None = None,
		default: tuple[str, ...] = ORNAMENTS,
		) -> str:
	"""Pick one ornament for ``seed`` from the genus of this identity.

	Stable across re-renders: the same seed + genus always yields the same
	mark, so every spell separator on the sheet matches.
	"""
	pool = genus(
		guild,
		species,
		background,
		default=default,
		)
	if not pool:
		return "✦"

	index = sum(
		ord(
			character
			)
		for character in str(
			seed
			)
		) % len(
		pool
		)
	return pool[
		index
		]


def _format(
		value,
		spec: str,
		):
	"""Shared ``__format__`` dispatch for the Venustas primitives."""
	spec = (spec or "").strip().lower()

	if spec in ("", "html"):
		return value.html()
	if spec in ("md", "markdown"):
		return value.md()
	if spec in ("plain", "text", "str"):
		return value.plain()

	raise ValueError(
		f"Unknown format {spec!r} — use html, md, or plain."
		)


class Entry(str):
	"""A titled feature/hook that *is* its own HTML; also .md() / .plain()."""

	def __new__(
			cls,
			title: str = "",
			definition: str = "",
			description: str = "",
			speech: str = "",
			*,
			symbol: str = "",
			kind: str = "Feature",
			):
		if symbol == "random":
			symbol = glyph(
				title
				)

		head = (
			f"{symbol} {title}".strip()
			if symbol
			else title
			)

		if not title:
			html = ""
		elif not definition:
			html = f"<b>{head}</b>"
		elif not description:
			html = f"<b>{head}:</b> <i>{definition}</i>"
		else:
			html = (
				f"<b>{head}:</b>\n"
				f'<div class="bc4">{description}</div>'
				f"<i>{definition}</i>"
				)

		entry = super().__new__(
			cls,
			html,
			)
		entry.title = title
		entry.definition = definition
		entry.description = description
		entry.speech = speech
		entry.symbol = symbol
		entry.kind = kind
		return entry

	def html(
			self,
			) -> str:
		return str.__str__(
			self
			)

	def _head(
			self,
			) -> str:
		return (
			f"{self.symbol} {self.title}".strip()
			if self.symbol
			else self.title
			)

	def md(
			self,
			) -> str:
		lines = []
		head = self._head()

		if head:
			lines.append(
				f"# {head}"
				)
		if self.definition:
			lines.append(
				_html_to_md(
					self.definition
					)
				)

		return "\n\n".join(
			lines
			).strip()

	def plain(
			self,
			) -> str:
		parts = []
		head = self._head()

		if head:
			parts.append(
				f"{head}."
				)
		if self.definition:
			parts.append(
				_strip_html(
					self.definition
					)
				)

		return " ".join(
			parts
			).strip()

	def __format__(
			self,
			spec: str,
			) -> str:
		return _format(
			self,
			spec,
			)


class Chip(str):
	"""A compact left-column datum that *is* its own HTML (symbol/label/value)."""

	def __new__(
			cls,
			symbol: str = "",
			label: str = "",
			value: str = "",
			*,
			extra_class: str = "",
			kind: str = "Attribute",
			):
		css = f"npc-box stat-chip {extra_class}".strip()
		html = (
			f'<div class="{css}">'
			f'<div class="symbol">{symbol}</div>'
			f'<div class="record">{label}</div>'
			f'<div class="value">{value}</div>'
			"</div>"
			)

		chip = super().__new__(
			cls,
			html,
			)
		chip.symbol = symbol
		chip.label = label
		chip.value = value
		chip.extra_class = extra_class
		chip.kind = kind
		return chip

	def html(
			self,
			) -> str:
		return str.__str__(
			self
			)

	def md(
			self,
			) -> str:
		return f"**{self.label}:** {self.value}"

	def plain(
			self,
			) -> str:
		return f"{self.label}: {self.value}"

	def __format__(
			self,
			spec: str,
			) -> str:
		return _format(
			self,
			spec,
			)


__all__ = (
	"ALCHEMY",
	"Chip",
	"DINGBATS",
	"Entry",
	"GENERA",
	"GLYPHS",
	"GREEK",
	"LIBRARIES",
	"MYSTIC",
	"ORNAMENTS",
	"PICTOGRAPHS",
	"RUNES",
	"TRIGRAMS",
	"genus",
	"glyph",
	"glyph_for",
	"library_for",
	"ornament_for",
	)
