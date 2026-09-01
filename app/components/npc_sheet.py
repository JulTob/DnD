"""Reusable Shiny rendering for generated non-player-character sheets."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from shiny import ui

from AtlasActorLudi.AtlasAlusoris.Map_of_NonPlayer_Projections import Resolve_Legacy_Attribute
from AtlasActorLudi.AtlasAlusoris.Map_of_NonPlayer_Projections import Resolve_Legacy_Section
from AtlasVenustas import Chip
from app.components.shared import feature_item
from app.components.shared import html_prose
from app.components.shared import prose
from app.components.shared import prose_section
from app.components.shared import safe_int
from app.components.shared import safe_str
from app.components.shared import skill_rows
from app.components.shared import text_html


SectionRenderer = Callable[[Any], Any]
_CREATURE_TYPE_RACES = frozenset(
        {
            "Beast",
            "Fey",
            "Dragon",
            "Giant",
            "Fiend",
            "Celestial",
            "Monstrosity",
            "Elemental",
            "Undead",
            "Construct",
            "Ooze",
            "Plant",
            "Aberration",
            }
        )
_SCORE_EMOJIS = {
        "STR": "🦾",
        "DEX": "🥢",
        "CON": "🫀",
        "INT": "🧩",
        "WIS": "🦉",
        "CHA": "🎭",
        }


def _creature_type_label(
        npc: Any,
        ) -> str:
    explicit = safe_str(
            getattr(
                    npc,
                    "creature_type",
                    "",
                    ),
            "",
            )
    if explicit:
        return explicit.replace(
                "_",
                " ",
                )
    race = safe_str(
            getattr(
                    npc,
                    "race",
                    "",
                    ),
            "",
            )
    if race in _CREATURE_TYPE_RACES:
        return race
    if race == "Vampire":
        return "Undead"
    return "Humanoid"


def _render_optional_section(
        npc: Any,
        section: str,
        renderer: SectionRenderer | None,
        ) -> str:
    if renderer is None:
        return "Unavailable"
    try:
        return str(
                Resolve_Legacy_Section(
                        npc,
                        section,
                        renderer,
                        )
                )
    except Exception:
        return "Unavailable"


def _story_text(
        npc: Any,
        ) -> Any:
    story = getattr(
            npc,
            "Story",
            None,
            )
    if story not in (
            None,
            "",
            ):
        return story
    return _legacy_attribute(
            npc,
            "story",
            )


def _legacy_attribute(
        npc: Any,
        attribute: str,
        default: object = "-",
        ) -> object:
    try:
        return Resolve_Legacy_Attribute(
                npc,
                attribute,
                default,
                )
    except Exception:
        return default


def _score(
        ability_scores: Any,
        name: str,
        ) -> int:
    if ability_scores is None:
        return 10
    return safe_int(
            getattr(
                    ability_scores,
                    name,
                    10,
                    ),
            10,
            )


def _score_row(
        ability_scores: Any,
        name: str,
        emoji: str,
        ) -> ui.Tag:
    value = _score(
            ability_scores,
            name,
            )
    modifier = (value - 10) // 2
    return ui.div(
            {
                "class": "npc-box",
                "style": "text-align: right;",
                },
            ui.div(
                    {"class": "symbol"},
                    emoji,
                    ),
            ui.h2(
                    f"{name}: {value} {modifier:+d}"
                    ),
            )


def _scores_box(
        ability_scores: Any,
        ) -> ui.Tag:
    return ui.div(
            {"class": "npc-box npc-scores"},
            *[
                    _score_row(
                            ability_scores,
                            name,
                            _SCORE_EMOJIS[name],
                            )
                    for name in (
                            "STR",
                            "DEX",
                            "CON",
                            "INT",
                            "WIS",
                            "CHA",
                            )
                    ],
            )


def _skills_box(
        npc: Any,
        ability_scores: Any,
        ) -> ui.Tag:
    skills = getattr(
            npc,
            "skills",
            None,
            )
    passive_perception = safe_str(
            _legacy_attribute(
                    npc,
                    "passive_perception",
                    )
            )
    return ui.div(
            {"class": "npc-textbox"},
            ui.h2(
                    "Skills"
                    ),
            ui.tags.table(
                    {"class": "skills-table"},
                    ui.tags.tbody(
                            *skill_rows(
                                    skills
                                    )
                            ),
                    ),
            ui.h4(
                    f"Passive Perception: {passive_perception}"
                    ),
            )


def _rail_text_box(
        title: str,
        content: Any,
        *,
        trusted_html: bool = False,
        ) -> ui.Tag:
    body = html_prose(
            content
            ) if trusted_html else text_html(
            content
            )
    return ui.div(
            {"class": "npc-textbox"},
            ui.h2(
                    title
                    ),
            body,
            )


def _npc_stat_chips(
        npc: Any,
        ) -> list[Any]:
    alignment = safe_str(
            _legacy_attribute(
                    npc,
                    "alignment",
                    )
            )
    proficiency_bonus = safe_str(
            _legacy_attribute(
                    npc,
                    "proficiency_bonus",
                    )
            )
    chips = [
            Chip(
                    "⚖️",
                    "Alignment",
                    alignment,
                    ),
            Chip(
                    "👤",
                    "Creature Type",
                    _creature_type_label(
                            npc
                            ),
                    ),
            Chip(
                    "⚧",
                    "Gender",
                    safe_str(
                            getattr(
                                    npc,
                                    "gender",
                                    "-",
                                    )
                            ),
                    ),
            Chip(
                    "🧑\u200d🧒",
                    "Size",
                    safe_str(
                            getattr(
                                    npc,
                                    "size",
                                    "-",
                                    )
                            ),
                    ),
            Chip(
                    "🏵️",
                    "Level",
                    safe_str(
                            getattr(
                                    npc,
                                    "level",
                                    "-",
                                    )
                            ),
                    ),
            Chip(
                    "⚜️",
                    "Proficiency Bonus",
                    f"+{proficiency_bonus}",
                    ),
            Chip(
                    "💚",
                    "Max Hit Points",
                    safe_str(
                            getattr(
                                    npc,
                                    "HP",
                                    "-",
                                    )
                            ),
                    ),
            Chip(
                    "🛡️",
                    "Armor Class",
                    safe_str(
                            getattr(
                                    npc,
                                    "AC",
                                    "-",
                                    )
                            ),
                    ),
            ]
    spell_save = _legacy_attribute(
            npc,
            "spell_save_dc",
            None,
            )
    spell_attack = _legacy_attribute(
            npc,
            "spell_attack_bonus",
            None,
            )
    missing = (
            None,
            "",
            "-",
            )
    if spell_save not in missing:
        chips.append(
                Chip(
                        "🔮",
                        "Spell Save DC",
                        safe_str(
                                spell_save
                                ),
                        )
                )
    if spell_attack not in missing:
        ability = safe_str(
                _legacy_attribute(
                        npc,
                        "spellcasting_ability",
                        "",
                        ),
                "",
                ).strip()
        attack = "+" + safe_str(
                spell_attack
                )
        if ability and ability != "-":
            attack += f" [{ability}]"
        chips.append(
                Chip(
                        "🎯",
                        "Spell Attack Bonus",
                        attack,
                        )
                )
    contributed: set[Any] = set()
    for feature in getattr(
            npc,
            "npc_features",
            (),
            ):
        for chip in getattr(
                feature,
                "chips",
                (),
                ):
            if chip.key in contributed:
                continue
            contributed.add(
                    chip.key
                    )
            chips.append(
                    Chip(
                            chip.icon,
                            chip.label,
                            chip.value,
                            )
                    )
    return [
            ui.HTML(
                    box
                    )
            for box in chips
            ]


def _tactical_feature_sections(
        npc: Any,
        ) -> list[Any]:
    features = tuple(
            getattr(
                    npc,
                    "npc_features",
                    (),
                    )
            )
    if not features:
        return []
    sections = []
    for activation in (
            "Trait",
            "Action",
            "Bonus Action",
            "Reaction",
            ):
        entries = []
        for feature in features:
            if str(
                    getattr(
                            feature,
                            "activation",
                            "",
                            )
                    ) != activation:
                continue
            roles = ", ".join(
                    str(
                            role
                            )
                    for role in getattr(
                            feature,
                            "tactical_roles",
                            (),
                            )
                    )
            contributors = ", ".join(
                    getattr(
                            feature,
                            "contributing_tags",
                            (),
                            )
                    )
            details = roles
            if contributors:
                details += f" · Tags: {contributors}"
            description = safe_str(
                    getattr(
                            feature,
                            "description",
                            "",
                            ),
                    "",
                    )
            if details:
                description += f"\n\n*{details}*"
            entries.append(
                    feature_item(
                            safe_str(
                                    getattr(
                                            feature,
                                            "name",
                                            "Feature",
                                            )
                                    ),
                            description,
                            )
                    )
        if not entries:
            continue
        sections.append(
                prose_section(
                        activation,
                        *entries,
                        accent=activation == "Action",
                        )
                )
    return sections


def _character_feature_sections(
        npc: Any,
        ) -> list[Any]:
    tactical_keys = {
            feature.key
            for feature in getattr(
                    npc,
                    "npc_features",
                    (),
                    )
            }
    entries = []
    for feature in getattr(
            npc,
            "features",
            (),
            ):
        key = getattr(
                feature,
                "key",
                None,
                )
        if key in tactical_keys:
            continue
        name = getattr(
                feature,
                "name",
                None,
                )
        if not name:
            continue
        entries.append(
                feature_item(
                        safe_str(
                                name
                                ),
                        safe_str(
                                getattr(
                                        feature,
                                        "description",
                                        "",
                                        ),
                                "",
                                ),
                        )
                )
    if not entries:
        return []
    return [
            prose_section(
                    "Character Features",
                    *entries,
                    )
            ]


def _prose_sections(
        npc: Any,
        legendary: Any,
        lair: Any,
        region: Any,
        ) -> list[Any]:
    to_hit_bonus = safe_str(
            _legacy_attribute(
                    npc,
                    "to_hit_bonus",
                    )
            )
    spellcasting_ability = safe_str(
            _legacy_attribute(
                    npc,
                    "spellcasting_ability",
                    )
            )
    sections = []
    sections.extend(
            _character_feature_sections(
                    npc
                    )
            )
    sections.extend(
            _tactical_feature_sections(
                    npc
                    )
            )
    sections.append(
            prose_section(
                    "Personality",
                    ui.h4(
                            "Trait"
                            ),
                    ui.p(
                            ui.tags.i(
                                    safe_str(
                                            _legacy_attribute(
                                                    npc,
                                                    "trait",
                                                    )
                                            )
                                    )
                            ),
                    ui.h4(
                            "Ideal"
                            ),
                    ui.p(
                            ui.tags.i(
                                    safe_str(
                                            _legacy_attribute(
                                                    npc,
                                                    "ideal",
                                                    )
                                            )
                                    )
                            ),
                    ui.h4(
                            "Plot Hook"
                            ),
                    ui.p(
                            ui.tags.i(
                                    safe_str(
                                            _legacy_attribute(
                                                    npc,
                                                    "plothook",
                                                    )
                                            )
                                    )
                            ),
                    )
            )
    sections.append(
            prose_section(
                    "Combat Actions",
                    ui.h4(
                            f"To hit: +{to_hit_bonus}"
                            ),
                    prose(
                            _legacy_attribute(
                                    npc,
                                    "simple_attacks",
                                    )
                            ),
                    prose(
                            _legacy_attribute(
                                    npc,
                                    "special_attack",
                                    )
                            ),
                    )
            )
    sections.append(
            prose_section(
                    f"Spellcasting: {spellcasting_ability}",
                    prose(
                            _legacy_attribute(
                                    npc,
                                    "spells",
                                    )
                            ),
                    accent=True,
                    )
            )
    sections.append(
            prose_section(
                    "Legendary",
                    prose(
                            legendary
                            ),
                    )
            )
    sections.append(
            prose_section(
                    "Lair",
                    prose(
                            lair
                            ),
                    )
            )
    sections.append(
            prose_section(
                    "Region",
                    prose(
                            region
                            ),
                    )
            )
    sections.append(
            prose_section(
                    "My Story",
                    prose(
                            _story_text(
                                    npc
                                    )
                            ),
                    )
            )
    return sections


def build_npc_sheet(
        npc: Any,
        *,
        legendary_renderer: SectionRenderer | None = None,
        lair_renderer: SectionRenderer | None = None,
        region_renderer: SectionRenderer | None = None,
        ) -> ui.Tag:
    """Build the NPC sheet without coupling presentation to generators."""
    race = safe_str(
            getattr(
                    npc,
                    "race",
                    "-",
                    )
            )
    subrace = safe_str(
            getattr(
                    npc,
                    "subrace",
                    "-",
                    )
            )
    background = safe_str(
            getattr(
                    npc,
                    "background",
                    "-",
                    )
            )
    guild = safe_str(
            getattr(
                    npc,
                    "char_class",
                    "-",
                    )
            )
    ability_scores = _legacy_attribute(
            npc,
            "ability_scores",
            None,
            )
    legendary = _render_optional_section(
            npc,
            "legendary",
            legendary_renderer,
            )
    lair = _render_optional_section(
            npc,
            "lair",
            lair_renderer,
            )
    region = _render_optional_section(
            npc,
            "region",
            region_renderer,
            )
    return ui.div(
            {"class": "sheet note-lines"},
            ui.div(
                    {"class": "npc-header"},
                    ui.h2(
                            {"class": "character-name"},
                            safe_str(
                                    getattr(
                                            npc,
                                            "name",
                                            "Unknown",
                                            )
                                    ),
                            ),
                    ui.h2(
                            {"class": "character-title"},
                            safe_str(
                                    getattr(
                                            npc,
                                            "title",
                                            "",
                                            )
                                    ),
                            ),
                    ui.h1(
                            f"{race}: {subrace}"
                            ),
                    ui.h1(
                            f"{guild} · {background}"
                            ),
                    ),
            ui.div(
                    {"class": "sheet-body"},
                    ui.div(
                            {"class": "sheet-rail"},
                            ui.div(
                                    {"class": "stat-flow"},
                                    *_npc_stat_chips(
                                            npc
                                            ),
                                    ),
                            _scores_box(
                                    ability_scores
                                    ),
                            _skills_box(
                                    npc,
                                    ability_scores,
                                    ),
                            _rail_text_box(
                                    "Saving Throws",
                                    getattr(
                                            getattr(
                                                    npc,
                                                    "saving_throws",
                                                    None,
                                                    ),
                                            "string",
                                            "-",
                                            ),
                                    ),
                            _rail_text_box(
                                    "Languages",
                                    _legacy_attribute(
                                            npc,
                                            "languages",
                                            ),
                                    trusted_html=True,
                                    ),
                            _rail_text_box(
                                    "Movement",
                                    getattr(
                                            npc,
                                            "movement",
                                            "-",
                                            ),
                                    trusted_html=True,
                                    ),
                            _rail_text_box(
                                    "Senses",
                                    _legacy_attribute(
                                            npc,
                                            "senses",
                                            ),
                                    trusted_html=True,
                                    ),
                            _rail_text_box(
                                    "Resistances",
                                    _legacy_attribute(
                                            npc,
                                            "resistances",
                                            ),
                                    trusted_html=True,
                                    ),
                            ),
                    ui.div(
                            {"class": "sheet-main"},
                            *_prose_sections(
                                    npc,
                                    legendary,
                                    lair,
                                    region,
                                    ),
                            ),
                    ),
            )


__all__ = [
        "SectionRenderer",
        "build_npc_sheet",
        ]
