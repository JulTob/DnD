"""Messages from the Shiny server to one connected browser."""

from __future__ import annotations

import asyncio
import inspect
from dataclasses import dataclass
from typing import Any


@dataclass(
        frozen=True,
        slots=True,
        )
class Client_Messages:
    """Send frontend effects without exposing transport details to pages."""

    session: Any

    def send(
            self,
            message_type: str,
            message_data: dict[str, Any],
            ) -> None:
        pending = self.session.send_custom_message(
                message_type,
                message_data,
                )
        if inspect.isawaitable(
                pending
                ):
            asyncio.create_task(
                    pending
                    )

    def set_loader(
            self,
            action: str,
            ) -> None:
        self.send(
                "set_loader",
                {
                    "action": action,
                    },
                )

    def set_character_hash(
            self,
            url_hash: str,
            ) -> None:
        self.send(
                "update_character_url",
                {
                    "hash": url_hash,
                    },
                )
        self.send(
                "set_share_hash",
                {
                    "hash": url_hash,
                    },
                )


__all__ = (
        "Client_Messages",
        )
