"""ASGI redirects that carry shareable paths into the Shiny frontline."""

from __future__ import annotations

from typing import Any

from AtlasActorLudi.AtlasAlusoris import nonplayer_hash
from AtlasActorLudi.AtlasAlusoris import parse_nonplayer_path
from app.character_url import character_params_to_hash
from app.character_url import parse_character_params_from_path
from AtlasMagistratum.Map_of_Session_Paths import asgi_dm_redirect_target


def canonical_base_path(
        pathname: str,
        ) -> str:
    """Return the mounted application base for a shareable path."""
    path = pathname or "/"
    for marker in (
            "/character/",
            "/npc/",
            "/dm/",
            ):
        marker_index = path.find(
                marker
                )
        if marker_index >= 0:
            return path[:marker_index + 1] or "/"
    for suffix in (
            "character",
            "npc",
            "dm",
            ):
        if path.endswith(
                f"/{suffix}"
                ):
            return path[:-len(suffix)] or "/"
    return path


async def _send_redirect(
        send,
        location: str,
        status: int = 307,
        ) -> None:
    headers = [
            (
                    b"location",
                    location.encode(
                            "utf-8"
                            ),
                    ),
            (
                    b"cache-control",
                    b"no-store",
                    ),
            ]
    await send(
            {
                "type": "http.response.start",
                "status": status,
                "headers": headers,
                }
            )
    await send(
            {
                "type": "http.response.body",
                "body": b"",
                }
            )


class Shareable_Path_Redirect:
    """Redirect direct Character and Magistratum paths to Shiny hashes."""

    def __init__(
            self,
            wrapped_app: Any,
            ) -> None:
        self.wrapped_app = wrapped_app

    async def __call__(
            self,
            scope,
            receive,
            send,
            ) -> None:
        is_get = (
                scope.get(
                        "type"
                        ) == "http"
                and (
                        scope.get(
                                "method"
                                ) or "GET"
                        ).upper() == "GET"
                )
        if is_get:
            path = str(
                    scope.get(
                            "path"
                            ) or ""
                    )
            if (
                    path.endswith(
                            "/character"
                            )
                    or path.endswith(
                            "/npc"
                            )
                    or path.endswith(
                            "/dm"
                            )
                    ):
                await _send_redirect(
                        send,
                        canonical_base_path(
                                path
                                ),
                        )
                return
            if "/npc/" in path:
                parameters = parse_nonplayer_path(
                        path
                        )
                if parameters is not None:
                    target_hash = nonplayer_hash(
                            **parameters
                            )
                    await _send_redirect(
                            send,
                            f"{canonical_base_path(path)}#{target_hash}",
                            )
                    return
                await _send_redirect(
                        send,
                        canonical_base_path(
                                path
                                ),
                        )
                return
            if "/character/" in path:
                parameters = parse_character_params_from_path(
                        path
                        )
                if parameters is not None:
                    url_hash = character_params_to_hash(
                            parameters
                            )
                    if url_hash:
                        await _send_redirect(
                                send,
                                f"{canonical_base_path(path)}{url_hash}",
                                )
                        return
                await _send_redirect(
                        send,
                        canonical_base_path(
                                path
                                ),
                        )
                return
            if "/dm/" in path:
                target = asgi_dm_redirect_target(
                        path,
                        canonical_base=canonical_base_path(
                                path
                                ),
                        )
                if target:
                    await _send_redirect(
                            send,
                            target,
                            )
                    return
        await self.wrapped_app(
                scope,
                receive,
                send,
                )


__all__ = (
        "Shareable_Path_Redirect",
        "canonical_base_path",
        )
