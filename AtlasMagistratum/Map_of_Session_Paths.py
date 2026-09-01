"""Session path rites for the DM Companion — NPC import URLs and `dm/<level>/<seed>`."""

from __future__ import annotations

from typing import Any
from urllib.parse import unquote
from urllib.parse import urlparse

from AtlasActorLudi.AtlasAlusoris.Map_of_NonPlayer_Paths import parse_nonplayer_path


def parse_npc_or_dm_path(
		raw: str,
		) -> dict[str, Any] | None:
	"""Parse `/npc/Race/Background/level/seed` or `/dm/level/seed`."""
	nonplayer = parse_nonplayer_path(
			raw
			)
	if nonplayer is not None:
		return nonplayer
	text = (
			raw or ""
			).strip()
	if not text:
		return None
	if text.startswith(
			"http"
			):
		text = urlparse(
				text
				).path or ""
	text = text.lstrip(
			"#"
			)
	if not text.startswith(
			"/"
			):
		text = "/" + text
	parts = [
			unquote(
					p
					)
			for p in text.split(
					"/"
					)
			if p
			]
	if len(
			parts
			) >= 3 and parts[0].lower() == "dm":
		try:
			return {
					"level": int(
							parts[1]
							),
					"seed": int(
							parts[2]
							),
					"race": None,
					"archetype": None,
					}
		except (
				TypeError,
				ValueError,
				):
			return None
	return None


def dm_session_hash(
		level: int,
		seed: int,
		) -> str:
	"""Shareable hash fragment body: `dm/<level>/<seed>` (no leading slash)."""
	return f"dm/{int(level)}/{int(seed)}"


def asgi_dm_redirect_target(
		pathname: str,
		*,
		canonical_base: str,
		) -> str | None:
	"""If pathname is a bare `/dm/<level>/<seed>` path, return hash redirect location."""
	path = pathname or ""
	if "/dm/" not in path:
		return None
	dm_tail = path[path.find("/dm/") + 1:]
	parts = [
			p
			for p in dm_tail.split(
					"/"
					)
			if p
			]
	if len(
			parts
			) < 3 or parts[0].lower() != "dm":
		return None
	try:
		int(
				parts[1]
				)
		int(
				parts[2]
				)
	except (
			TypeError,
			ValueError,
			):
		return None
	base = canonical_base or "/"
	return f"{base}#{dm_tail}"


if __name__ == "__main__":
	assert parse_npc_or_dm_path(
			"/dm/5/42"
			) == {
			"level": 5,
			"seed": 42,
			"race": None,
			"archetype": None,
			}
	assert parse_npc_or_dm_path(
			"/npc/Elf/Wizard/3/99"
			)[
			"seed"
			] == 99
	assert dm_session_hash(
			5,
			42,
			) == "dm/5/42"
	assert asgi_dm_redirect_target(
			"/app/dm/5/42",
			canonical_base="/app/",
			) == "/app/#dm/5/42"
	print(
			"Map_of_Session_Paths: ok"
			)
