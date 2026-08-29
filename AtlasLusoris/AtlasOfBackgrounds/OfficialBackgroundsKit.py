"""Shared registration route: build Background Tags from ``Background`` records."""

from typing import Callable, Mapping

from AtlasLusoris.Grimoire_of_Backgrounds import Background


def Register_Backgrounds(
		*,
		records: tuple[Background, ...],
		source_title: str,
		source_url: str,
		source_locator: str,
		build_background: Callable,
		pc_background: type,
		npc_background: type,
		artisan_tools: tuple[str, ...],
		origin_feats: Mapping[str, type],
		) -> tuple[type, ...]:
	"""Register one source Map's ``Background`` records through BackgroundKit."""
	backgrounds = []

	for record in records:
		resolved_tools = (
			record.tools
			if record.tools
			else artisan_tools
			)
		origin_feat = origin_feats[
			record.origin_feat
			]

		description = record.description
		if record.roleplay:
			description = (
				f"{description}\n\n{record.roleplay}"
				if description
				else record.roleplay
				)

		try:
			backgrounds.append(
				build_background(
					name=record.name,
					audiences=(
						pc_background,
						npc_background,
						),
					abilities=record.abilities,
					skills=record.skills,
					tools=resolved_tools,
					origin_feat=origin_feat,
					origin_feat_options=record.origin_feat_options,
					title=record.name,
					description=description,
					source_title=source_title,
					source_url=source_url,
					source_locator=source_locator,
					source_kind="official-reference",
					)
				)
		except ValueError as error:
			# Recovery: NPC kit backgrounds and official Maps can share a Name
			# (e.g. Guardian). Keep the earlier declaration; log via raise only
			# when it is a different failure.
			if "already declared" not in str(
				error
				):
				raise

	return tuple(
		backgrounds
		)


__all__ = (
	"Register_Backgrounds",
	)
