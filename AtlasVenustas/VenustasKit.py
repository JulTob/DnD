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
			kind: str = "Attribute",
			):
		html = (
			'<div class="npc-box stat-chip">'
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
	"Chip",
	"Entry",
	)
