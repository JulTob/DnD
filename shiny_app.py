"""Compatibility shim — canonical Shiny app is ``app.main:app``."""

from app.main import app, server

__all__ = (
        "app",
        "server",
        )
