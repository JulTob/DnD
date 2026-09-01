"""Shared Shiny chrome surrounding every Atlas frontline."""

from __future__ import annotations

from shiny import ui

from app.components import (
    loader_head_tags,
    loader_panel,
    masonry_head_tags,
    number_input_head_tags,
    shareable_links_head_tags,
    style_tag,
    tablet_head_tags,
    )
from app.publish_scope import fantasy_button_class


_FONT_STYLESHEETS = (
    "https://fonts.googleapis.com/css2?family=Cinzel:ital@0;1&display=swap",
    "https://fonts.googleapis.com/css2?family=Cinzel+Decorative",
    "https://fonts.googleapis.com/css2?family=IM+Fell+English",
    "https://fonts.googleapis.com/css2?family=IM+Fell+DW+Pica",
    "https://fonts.googleapis.com/css2?family=IM+Fell+DW+Pica+SC",
    "https://fonts.googleapis.com/css2?family=IM+Fell+Great+Primer:ital@0;1",
    "https://fonts.googleapis.com/css2?family=IM+Fell+Great+Primer+SC",
    "https://fonts.googleapis.com/css2?family=IM+Fell+Double+Pica:ital@0;1",
    "https://fonts.googleapis.com/css2?family=IM+Fell+Double+Pica+SC",
    "https://fonts.googleapis.com/css2?family=IM+Fell+English+SC",
    "https://fonts.googleapis.com/css2?family=Spectral+SC:wght@400;600;700",
    "https://fonts.googleapis.com/css2?family=Eagle+Lake",
    "https://fonts.googleapis.com/css2?family=Italianno",
    "https://fonts.googleapis.com/css2?family=Beau+Rivage",
    "https://fonts.googleapis.com/css2?family=Fleur+De+Leah",
    "https://fonts.googleapis.com/css2?family=IM+Fell+French+Canon+SC",
    "https://fonts.googleapis.com/css2?family=Tangerine:wght@400;700",
    "https://fonts.googleapis.com/css2?family=Manufacturing+Consent",
    "https://fonts.googleapis.com/css2?family=UnifrakturMaguntia",
    )


def _head() -> ui.Tag:
    font_links = [
        ui.tags.link(
                href=font_url,
                rel="stylesheet",
                )
        for font_url in _FONT_STYLESHEETS
        ]

    return ui.tags.head(
            ui.tags.meta(
                    charset="utf-8"
                    ),
            ui.tags.meta(
                    name="viewport",
                    content="width=device-width, initial-scale=1",
                    ),
            ui.tags.title(
                    "Gen Legend (Shiny)"
                    ),
            ui.tags.link(
                    rel="preconnect",
                    href="https://fonts.googleapis.com",
                    ),
            ui.tags.link(
                    rel="preconnect",
                    href="https://fonts.gstatic.com",
                    crossorigin="",
                    ),
            *font_links,
            style_tag(),
            *tablet_head_tags(),
            *number_input_head_tags(),
            *loader_head_tags(),
            *masonry_head_tags(),
            *shareable_links_head_tags(),
            )


def _header() -> ui.Tag:
    return ui.tags.header(
            ui.h1(
                    ui.tags.a(
                            {
                                "href": "#",
                                "style": (
                                    "color: inherit; "
                                    "text-decoration: none;"
                                    ),
                                },
                            "Gen Legend",
                            )
                    ),
            ui.tags.div(
                    {"class": "header-actions"},
                    ui.input_action_button(
                            "go_home",
                            "Home",
                            class_=fantasy_button_class(),
                            ),
                    ui.input_action_button(
                            "go_character",
                            "Character",
                            class_=fantasy_button_class(),
                            ),
                    ui.input_action_button(
                            "go_npc",
                            "NPC",
                            class_=fantasy_button_class(
                                    parked=True
                                    ),
                            ),
                    ui.input_action_button(
                            "go_npclist",
                            "NPC List",
                            class_=fantasy_button_class(
                                    parked=True
                                    ),
                            ),
                    ui.input_action_button(
                            "go_dm",
                            "DM",
                            class_=fantasy_button_class(
                                    parked=True
                                    ),
                            ),
                    ),
            )


def _footer() -> ui.Tag:
    link_style = (
        "color: #f6d67c; "
        "text-decoration: none; "
        "font-weight: bold; "
        "margin: 0 1.5em;"
        )

    return ui.tags.footer(
            {
                "style": (
                    "background: #231c27; "
                    "color: #f6d67c; "
                    "padding: 1.15em 0; "
                    "text-align: center; "
                    "font-size: 1.03em; "
                    "margin-top: 2em; "
                    "border-top: 3px solid #786110; "
                    "letter-spacing: 0.01em;"
                    ),
                },
            ui.tags.a(
                    "About Us",
                    href="https://github.com/JulTob/DnD#readme",
                    target="_blank",
                    rel="noopener",
                    style=link_style,
                    ),
            ui.tags.span(
                    "|",
                    style="margin: 0 1.5em;",
                    ),
            ui.tags.a(
                    "Lore Wiki",
                    href="https://github.com/JulTob/DnD/wiki",
                    target="_blank",
                    rel="noopener",
                    style=link_style,
                    ),
            ui.tags.span(
                    "|",
                    style="margin: 0 1.5em;",
                    ),
            ui.tags.span(
                    "By ",
                    ui.tags.a(
                            "Julio Toboso",
                            href="https://github.com/JulTob",
                            target="_blank",
                            rel="noopener",
                            style=(
                                "color: #f6d67c; "
                                "text-decoration: underline dashed; "
                                "font-weight: bold;"
                                ),
                            ),
                    style="color: #f6d67c;",
                    ),
            )


def app_ui() -> ui.Tag:
    """Build the shared shell; the active page is session-rendered."""
    return ui.page_fluid(
            _head(),
            loader_panel(),
            _header(),
            ui.div(
                    {"class": "main-wrap"},
                    ui.div(
                            {"class": "container"},
                            ui.output_ui(
                                    "active_page"
                                    ),
                            ),
                    ),
            _footer(),
            )


__all__ = (
    "app_ui",
    )
