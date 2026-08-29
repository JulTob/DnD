"""Reusable Shiny rendering for generated player-character sheets."""

from __future__ import annotations

from html import escape
from typing import Any

from shiny import ui

from AtlasVenustas import Chip

from app.components.shared import attack_rolls_html
from app.components.shared import feature_item
from app.components.shared import html_prose
from app.components.shared import prose
from app.components.shared import prose_section
from app.components.shared import safe_int
from app.components.shared import safe_str
from app.components.shared import skill_rows
from app.components.shared import text_html
from app.components.spellbook import known_spells_rail_box
from app.components.spellbook import spellbook_html
from app.components.spellbook import spellcasting_chips


_ABILITY_EMOJI = {
    "Strength": "🦾",
    "Dexterity": "🥢",
    "Constitution": "🫀",
    "Intelligence": "🧩",
    "Wisdom": "🦉",
    "Charisma": "🎭",
    }

# Slot labels, read off GearKit's Loadout view. "Wearing" reads better than "Defense" for the body slot — what sits there is a garment, not a statistic. Empty slots are dropped rather than rendered as rows of "-".
_EQUIPMENT_FIELDS = (
    (
        "Wearing",
        "wearing",
        ),
    (
        "Off-hand",
        "offhand",
        ),
    (
        "Melee",
        "melee",
        ),
    (
        "Ranged",
        "ranged",
        ),
    (
        "Head",
        "headwear",
        ),
    (
        "Cloak",
        "cloak",
        ),
    (
        "Hands",
        "handwear",
        ),
    (
        "Feet",
        "footwear",
        ),
    )


def _creature_type_label(
        data: dict[str, Any],
        default: str = "Humanoid",
        ) -> str:
    explicit = safe_str(
            data.get(
                    "CreatureType",
                    "",
                    ),
            "",
            )

    if explicit:
        return explicit.replace(
                "_",
                " ",
                )

    for feature in data.get(
            "features",
            (),
            ) or ():
        if getattr(
                feature,
                "name",
                "",
                ) == "Creature Type":
            return (
                getattr(
                        feature,
                        "description",
                        default,
                        )
                or default
                )

    return default


def _normalize_chip_pairs(
        chips: Any,
        ) -> list[tuple[str, str, str]]:
    """Normalize Feature chips to ``(symbol, label, value)`` triples."""
    if not chips:
        return []
    triples: list[tuple[str, str, str]] = []
    for item in chips:
        symbol = ""
        if isinstance(
                item,
                dict,
                ):
            label = item.get(
                    "label"
                    )
            value = item.get(
                    "value"
                    )
            symbol = item.get(
                    "symbol",
                    "",
                    ) or ""
        elif (
                isinstance(
                        item,
                        (tuple, list),
                        )
                and len(
                        item
                        ) >= 2
                ):
            label, value = item[0], item[1]
            symbol = item[2] if len(item) > 2 else ""
        else:
            continue
        if label is None or value is None:
            continue
        triples.append(
                (
                        safe_str(
                                symbol,
                                "",
                                ),
                        safe_str(
                                label
                                ),
                        safe_str(
                                value
                                ),
                        )
                )
    return triples


def _iter_feature_chips(
        features: Any,
        ) -> list[tuple[str, str, str]]:
    """Collect Feature chips for the left rail (not the Entry body)."""
    pairs: list[tuple[str, str, str]] = []
    seen: set[tuple[str, str, str]] = set()
    for current_feature in features or []:
        chips = getattr(
                current_feature,
                "chips",
                None,
                )
        if chips is None and isinstance(
                current_feature,
                dict,
                ):
            chips = current_feature.get(
                    "chips",
                    )
        for key in _normalize_chip_pairs(
                chips
                ):
            if key in seen:
                continue
            seen.add(
                    key
                    )
            pairs.append(
                    key
                    )
    return pairs


# The sheet reads outward from what a Character *is* toward what they chose:
# the Species they were born, the Background they came up in and will not
# change, and last the Class they are still becoming.
#
# Each block opens with its own title-and-description entry and then its
# rules. Within Species and Background, the second number pins a fixed
# reading order (title, description, hook, entries); within Class there is
# only one part after the Guild's own description, and it is ordered purely
# by the level each lesson was gained — "all the entries organized by level."
# Where two entries land on the same (section, part, level), the sort is
# stable, so they keep the order they were created in.
_SECTION_SPECIES = 0
_SECTION_BACKGROUND = 1
_SECTION_CLASS = 2
_SECTION_OTHER = 3

# Checked as a prefix, in order, first match wins. A longer, more specific
# prefix ("Background Hook") must be listed before the shorter one it starts
# with ("Background"), or the shorter entry would claim it first.
_SOURCE_PLACES = (
    ("Species Feature", (_SECTION_SPECIES, 1)),
    ("Background Hook", (_SECTION_BACKGROUND, 1)),
    ("Secret Order", (_SECTION_BACKGROUND, 2)),
    ("Order Hook", (_SECTION_BACKGROUND, 3)),
    ("Origin Feat", (_SECTION_BACKGROUND, 4)),  # incl. "Origin Feat — X"
    ("Background Feat", (_SECTION_BACKGROUND, 4)),  # legacy Origin Feat path
    ("Background", (_SECTION_BACKGROUND, 0)),
    ("Guild", (_SECTION_CLASS, 0)),
    ("Training:", (_SECTION_CLASS, 1)),
    ("Class:", (_SECTION_CLASS, 1)),  # legacy pre-Guild class features
    ("Fighting Style", (_SECTION_CLASS, 1)),
    ("Weapon Mastery", (_SECTION_CLASS, 1)),
    ("Eldritch Invocation", (_SECTION_CLASS, 1)),
    ("Invocation", (_SECTION_CLASS, 1)),  # incl. "Invocation — <name>" grants
    ("Invocation", (_SECTION_CLASS, 1)),  # incl. "Invocation — <name>" grants
    ("Epic Boon", (_SECTION_CLASS, 1)),
    ("Feat", (_SECTION_CLASS, 1)),
    )


def _feature_place(
        current_feature: Any,
        ) -> tuple[int, int, int]:
    """Where one Feature sits on the sheet: section, part, then level."""
    source = safe_str(
            getattr(
                    current_feature,
                    "source",
                    "",
                    ),
            "",
            )
    level = int(
            getattr(
                    current_feature,
                    "level",
                    0,
                    )
            or 0
            )
    section, part = _SECTION_OTHER, 0

    for prefix, place in _SOURCE_PLACES:
        if source.startswith(
                prefix
                ):
            section, part = place
            break

    # A block's own description is level 0 and heads it; the rules follow in
    # the order they are gained, which is what a reader climbing levels wants.
    return (
        section,
        part,
        level,
        )


def _ordered_features(
        features: Any,
        ) -> list[Any]:
    """Species, then Background, then Class, each headed by its description."""
    return sorted(
            features or [],
            key=_feature_place,
            )


def _render_feature(
        current_feature: Any,
        ) -> Any | None:
    """One Feature as sheet UI, or None for a record with nothing to say."""
    name = getattr(
            current_feature,
            "name",
            None,
            )

    if name == "Creature Type":
        return None

    if not name:
        return prose(
                str(current_feature)
                )

    description = safe_str(
            getattr(
                    current_feature,
                    "description",
                    "",
                    ),
            "",
            )
    narrative = bool(
            getattr(
                    current_feature,
                    "narrative",
                    False,
                    )
            )

    # A Feature with a chip and no prose is a *record*, not an entry:
    # "Darkvision 60 ft" says everything the paragraph would have. Its
    # chips were already collected by _iter_feature_chips.
    if not description.strip():
        return None

    # Chips live in the left rail — keep Entries as prose only.
    return feature_item(
            safe_str(name),
            description,
            chips=None,
            narrative=narrative,
            )


def _practice_markdown(
        practice: Any,
        ) -> str:
    """Project one structured Practice into flavour plus rules Markdown."""
    if isinstance(
            practice,
            dict,
            ):
        flavour = safe_str(
                practice.get(
                        "flavour",
                        "",
                        ),
                "",
                )
        sections = practice.get(
                "sections",
                (),
                ) or ()
    else:
        flavour = safe_str(
                getattr(
                        practice,
                        "flavour",
                        "",
                        ),
                "",
                )
        sections = getattr(
                practice,
                "sections",
                (),
                ) or ()

    paragraphs = []

    if flavour:
        paragraphs.append(
                f"*{flavour}*"
                )

    for section in sections:
        if isinstance(
                section,
                dict,
                ):
            title = safe_str(
                    section.get(
                            "title",
                            "",
                            ),
                    "",
                    )
            guidance = safe_str(
                    section.get(
                            "guidance",
                            "",
                            ),
                    "",
                    )
        else:
            title = safe_str(
                    getattr(
                            section,
                            "title",
                            "",
                            ),
                    "",
                    )
            guidance = safe_str(
                    getattr(
                            section,
                            "guidance",
                            "",
                            ),
                    "",
                    )

        if not title or not guidance:
            continue

        paragraphs.append(
                f"**{title.rstrip('.')}.** {guidance}"
                )

    return "\n\n".join(
            paragraphs
            )


def _practice_entries(
        practices: Any,
        ) -> list[Any]:
    """Render learned Practices without pretending they are Feature Tags."""
    entries = []

    for practice in practices or ():
        title = safe_str(
                practice.get(
                        "title",
                        "",
                        )
                if isinstance(
                        practice,
                        dict,
                        )
                else getattr(
                        practice,
                        "title",
                        "",
                        ),
                "",
                )
        description = _practice_markdown(
                practice
                )

        if not title or not description:
            continue

        entries.append(
                feature_item(
                        title,
                        description,
                        chips=None,
                        narrative=False,
                        )
                )

    return entries


def _grouped_feature_entries(
        features: Any,
        ) -> dict[int, list[Any]]:
    """
    Rendered entries bucketed by section — Species, Background, Class.

    A caller wants three titled blocks, not one generic "Features" dump: the
    section header should name the actual Species, Background, or Class,
    the way every other reader already expects from title/description/hook.
    Unclassified sources fold into Class, the safest default and, per the
    260-character regression sweep this was verified against, one that never
    actually receives anything.
    """
    grouped: dict[int, list[Any]] = {
        _SECTION_SPECIES: [],
        _SECTION_BACKGROUND: [],
        _SECTION_CLASS: [],
        }

    for current_feature in _ordered_features(
            features
            ):
        rendered = _render_feature(
                current_feature
                )

        if rendered is None:
            continue

        section = _feature_place(
                current_feature
                )[ 0 ]
        grouped.setdefault(
                _SECTION_CLASS
                if section == _SECTION_OTHER
                else section,
                [],
                ).append(
                rendered
                )

    return grouped


def _ability_score_boxes(
        stats: Any,
        ) -> list[Any]:
    boxes: list[Any] = []

    for stat, value in stats.items():
        score = safe_int(
                value,
                10,
                )
        modifier = (
            score - 10
            ) // 2
        emoji = _ABILITY_EMOJI.get(
                safe_str(stat),
                "",
                )
        symbol = (
            [
                ui.div(
                        {"class": "symbol"},
                        emoji,
                        ),
                ]
            if emoji
            else []
            )

        boxes.append(
                ui.div(
                        {
                            "class": "npc-box score-row",
                            "style": "text-align: right;",
                            },
                        *symbol,
                        ui.h4(
                                ui.HTML(
                                        (
                                            f"{escape(safe_str(stat))}<br>"
                                            f"{score} ({modifier:+d})"
                                            )
                                        )
                                ),
                        )
                )

    return boxes


def _equipment_rows(
        equipment: Any,
        ) -> list[Any]:
    if equipment is None:
        return []

    # Items render themselves as Entry HTML (Venustas Scriba); escaping it
    # would show the user literal <b>/<i> tags. Empty slots are omitted —
    # a row of "-" tells the reader nothing.
    rows = []

    for label, attribute in _EQUIPMENT_FIELDS:
        item = getattr(
                equipment,
                attribute,
                None,
                )
        if item is None:
            continue
        rows.append(
                ui.tags.tr(
                        ui.tags.td(label),
                        ui.tags.td(
                                ui.HTML(
                                        safe_str(item)
                                        )
                                ),
                        )
                )

    # Jewelry is the one slot that holds several at once.
    for worn in getattr(
            equipment,
            "jewelry",
            [],
            ) or []:
        rows.append(
                ui.tags.tr(
                        ui.tags.td("Jewelry"),
                        ui.tags.td(
                                ui.HTML(
                                        safe_str(worn)
                                        )
                                ),
                        )
                )

    return rows


def _bag_rows(
        equipment: Any,
        ) -> list[Any]:
    if equipment is None:
        return []

    return [
        ui.tags.tr(
                ui.tags.td(
                        safe_str(
                                # `called` prefers an earned title
                                # ("Club of Wounding") over the plain name.
                                getattr(
                                        item,
                                        "called",
                                        None,
                                        )
                                or getattr(
                                        item,
                                        "name",
                                        "item",
                                        )
                                )
                        ),
                ui.tags.td(
                        f"x{safe_str(getattr(item, 'quantity', 1))}"
                        ),
                ui.tags.td(
                        f"{safe_str(getattr(item, 'weight', 0))} lbs"
                        ),
                ui.tags.td(
                        f"{safe_str(getattr(item, 'value', 0))} gp"
                        ),
                )
        for item in getattr(
                equipment,
                "bag",
                [],
                ) or []
        ]


def _saving_throw_html(
        saving_throws: Any,
        ) -> ui.Tag:
    value = getattr(
            saving_throws,
            "string",
            saving_throws,
            )

    if callable(value):
        try:
            value = value()
        except Exception:
            value = saving_throws

    return text_html(
            value,
            "-",
            )


_FEATURE_CHIP_EMOJI = {
        "Favored Enemy Uses": "🎯",
        "Weapon Masteries": "⚔️",
        "Tireless Uses": "💤",
        "Nature's Veil Uses": "🌿",
        "Dreadful Strikes": "👻",
        "Blindsight": "👁️",
        "2nd Wind Uses": "💨",
        "Rage Uses": "🔥",
        "Rage Damage": "💢",
        "Spellfire Flame": "🔥",
        }


def _is_spellcasting_parameter_chip(
        label: str,
        ) -> bool:
    """Keep spell parameters in their one source-aware rail projection."""
    return label.endswith(
            (
                "Spellcasting Ability",
                "Spell Save DC",
                "Spell Attack Bonus",
                )
            )


def _character_stat_chips(
        data: dict[str, Any],
        ) -> list[Any]:
    creature_type = _creature_type_label(
            data
            )

    chips = [
        Chip(
                "⚖️",
                "Alignment",
                safe_str(
                        data.get(
                                "Alignment",
                                "-",
                                )
                        ),
                ),
        Chip(
                "👤",
                "Creature Type",
                creature_type,
                ),
        Chip(
                "⚧",
                "Gender",
                safe_str(
                        data.get(
                                "Gender",
                                "-",
                                )
                        ),
                ),
        Chip(
                "🧑‍🧒",
                "Size",
                safe_str(
                        data.get(
                                "size",
                                "-",
                                )
                        ),
                ),
        Chip(
                "👞",
                "Speed",
                safe_str(
                        data.get(
                                "Speed",
                                "-",
                                )
                        ),
                ),
        Chip(
                "🏵️",
                "Level",
                safe_str(
                        data.get(
                                "Level",
                                "-",
                                )
                        ),
                ),
        Chip(
                "⚜️",
                "Proficiency Bonus",
                f"+{safe_str(data.get('PB', '-'))}",
                ),
        Chip(
                "💚",
                # The number is the ceiling, not the current pool — say so, or
                # a reader takes it for how much the Character has left.
                "Max Hit Points",
                safe_str(
                        data.get(
                                "Health",
                                "-",
                                )
                        ),
                ),
        Chip(
                "🖤",
                "Hit Dice",
                safe_str(
                        data.get(
                                "HPD",
                                "-",
                                )
                        ),
                ),
        Chip(
                "🛡️",
                "Armor Class",
                safe_str(
                        data.get(
                                "AC",
                                "-",
                                )
                        ),
                ),
        ]
    for symbol, label, value in _iter_feature_chips(
            data.get(
                    "features"
                    )
            ):
        if _is_spellcasting_parameter_chip(
                label
                ):
            continue

        chips.append(
                Chip(
                        symbol or _FEATURE_CHIP_EMOJI.get(
                                label,
                                "✦",
                                ),
                        label,
                        value,
                        )
                )
    return [
        ui.HTML(box)
        for box in chips
        ]


def _species_identity(
        data: dict[str, Any],
        ) -> str:
    """Prefer a Heritage that already names its Species in plain language."""
    species = safe_str(
            data.get(
                    "Species",
                    "-",
                    )
            )
    heritage = safe_str(
            data.get(
                    "Heritage",
                    "",
                    ),
            "",
            )

    if not heritage:
        return species

    heritage_words = {
            word.casefold()
            for word in heritage.replace(
                    "-",
                    " ",
                    ).split()
            }

    if species.casefold() in heritage_words:
        return heritage

    return f"{species} ({heritage})"


def _class_heading(
        data: dict[str, Any],
        ) -> str:
    """``Covenantor (Warlock), Great Old One`` — the same string the header
    uses, shared so the Class section title never drifts from it."""
    class_title = safe_str(
            data.get(
                    "Class_Title"
                    )
            or data.get(
                    "Class",
                    "-",
                    ),
            "-",
            )
    subclass = safe_str(
            data.get(
                    "Subclass",
                    "",
                    ),
            "",
            )

    if not subclass or subclass == "-":
        return class_title

    return f"{class_title}, {subclass}"


def _rail_items(
        data: dict[str, Any],
        stats: Any,
        spellcaster: Any,
        ) -> list[Any]:
    skill_row_tags = skill_rows(
            data.get("Skills")
            )
    items: list[Any] = [
        ui.div(
                {"class": "npc-box npc-scores"},
                *_ability_score_boxes(stats),
                ),
        ui.div(
                {"class": "npc-textbox"},
                ui.h2("Skills"),
                ui.tags.table(
                        {"class": "skills-table"},
                        ui.tags.tbody(
                                *skill_row_tags,
                                ),
                        ),
                ui.h4(
                        (
                            "Passive Perception: "
                            f"{safe_str(data.get('passive_perception', '-'))}"
                            )
                        ),
                ),
        ui.div(
                {"class": "npc-textbox"},
                ui.h2("Saving Throws"),
                _saving_throw_html(
                        data.get("SavingThrow")
                        ),
                ),
        ui.div(
                {"class": "npc-textbox"},
                ui.h2("Attack Rolls"),
                attack_rolls_html(
                        data.get("AttackRolls")
                        ),
                ),
        ]
    proficiencies = data.get(
            "other_proficiencies"
            ) or []

    if proficiencies:
        items.append(
                ui.div(
                        {"class": "npc-textbox"},
                        ui.h2("Proficiencies"),
                        ui.tags.ul(
                                *[
                                    ui.tags.li(
                                            safe_str(proficiency)
                                            )
                                    for proficiency in proficiencies
                                    ],
                                ),
                        )
                )

    languages = data.get(
            "Languages"
            )
    if languages is not None:
        if hasattr(
                languages,
                "AsListHTML",
                ):
            language_body = languages.AsListHTML()
        else:
            language_body = safe_str(
                    languages,
                    "<i>Common</i>",
                    )
        items.append(
                ui.div(
                        {"class": "npc-textbox"},
                        ui.h2("Languages"),
                        html_prose(
                                language_body
                                ),
                        )
                )

    if spellcaster is not None:
        magic_chips = spellcasting_chips(
                spellcaster
                )

        if magic_chips:
            items.append(
                    ui.div(
                            {"class": "stat-flow"},
                            *magic_chips,
                            )
                    )

        known_spells = known_spells_rail_box(
                spellcaster
                )

        if known_spells is not None:
            items.append(known_spells)

    return items


def _equipment_section(
        equipment: Any,
        ) -> ui.Tag:
    content: list[Any] = [
        ui.tags.table(
                {"class": "objects-table"},
                ui.tags.tbody(
                        *_equipment_rows(equipment),
                        ),
                ),
        ]
    bag = _bag_rows(equipment)

    if bag:
        content.append(
                ui.h4("Bag")
                )
        content.append(
                ui.tags.table(
                        {"class": "objects-table"},
                        ui.tags.tbody(
                                *bag,
                                ),
                        )
                )

    content.append(
            ui.h4(
                    (
                        "Purse: "
                        f"{safe_str(getattr(equipment, 'purse', '-'))} gp"
                        )
                    )
            )

    return prose_section(
            "Equipment",
            *content,
            )


def _prose_sections(
        data: dict[str, Any],
        raw_features: Any,
        spellcaster: Any,
        ) -> list[Any]:
    # Three titled blocks, not one generic "Features" dump — a reader could
    # not tell Species from Background from Class under one flat heading,
    # and every entry already knows which of the three it belongs to.
    grouped = _grouped_feature_entries(
            raw_features
            )

    def _block(
            title: str,
            entries: list[Any],
            ) -> Any:
        return prose_section(
                title,
                *(
                    entries
                    or (
                        ui.p(
                                "None"
                                ),
                        )
                    ),
                )

    sections: list[Any] = [
        _block(
                _species_identity(
                        data
                        ),
                grouped[ _SECTION_SPECIES ],
                ),
        _block(
                safe_str(
                        data.get(
                                "Background",
                                "-",
                                ),
                        "-",
                        ),
                grouped[ _SECTION_BACKGROUND ],
                ),
        _block(
                _class_heading(
                        data
                        ),
                grouped[ _SECTION_CLASS ],
                ),
        ]
    practices = _practice_entries(
            data.get(
                    "Practices",
                    (),
                    )
            )

    if practices:
        sections.append(
                prose_section(
                        "Practices",
                        *practices,
                        )
                )

    equipment = data.get("equipment")

    if equipment is not None:
        sections.append(
                _equipment_section(equipment)
                )

    sections.append(
            prose_section(
                    "Backstory",
                    ui.div(
                            {"class": "narrative-prose"},
                            prose(
                                    data.get(
                                            "Story",
                                            "",
                                            )
                                    ),
                            ),
                    )
            )

    if spellcaster is not None:
        sections.append(
                prose_section(
                        "Spells",
                        html_prose(
                                spellbook_html(
                                        spellcaster
                                        )
                                ),
                        accent=True,
                        )
                )

    return sections


def build_character_sheet(
        data: dict[str, Any],
        ) -> ui.Tag:
    """Build the complete, behavior-compatible character-sheet UI."""
    stats = data.get("Stats") or {}
    spellcaster = data.get("Spellcaster")
    # Grouped into Species/Background/Class inside _prose_sections, not
    # flattened here — the raw Features still carry the source and level
    # that decide which of the three titled blocks each one belongs to.
    raw_features = data.get(
            "features",
            [],
            )

    return ui.div(
            {"class": "sheet note-lines"},
            ui.div(
                    {"class": "npc-header"},
                    ui.h2(
                            {"class": "character-name"},
                            safe_str(
                                    data.get(
                                            "name",
                                            "Unknown",
                                            ),
                                    "Unknown",
                                    ),
                            ),
                    ui.h2(
                            {"class": "character-title"},
                            safe_str(
                                    data.get(
                                            "title",
                                            "",
                                            ),
                                    "",
                                    ),
                            ),
                    ui.h1(
                            _class_heading(
                                    data
                                    )
                            ),
                    ui.h1(
                            (
                                f"{_species_identity(data)} "
                                f"{safe_str(data.get('Background', '-'))}"
                                )
                            ),
                    ),
            ui.div(
                    {"class": "sheet-body"},
                    ui.div(
                            {"class": "sheet-rail"},
                            ui.div(
                                    {"class": "stat-flow"},
                                    *_character_stat_chips(data),
                                    ),
                            *_rail_items(
                                    data,
                                    stats,
                                    spellcaster,
                                    ),
                            ),
                    ui.div(
                            {"class": "sheet-main"},
                            *_prose_sections(
                                    data,
                                    raw_features,
                                    spellcaster,
                                    ),
                            ),
                    ),
            )


__all__ = [
    "build_character_sheet",
    ]


def _test_generated_practices() -> None:
    """A trained Tool projects exactly one rendered Practice Entry."""
    from contextlib import redirect_stdout
    from io import StringIO

    from AtlasActorLudi.Map_of_Character_Generation import summon_player

    fixtures = (
        (
            "Charlatan",
            700,
            "Forgery Kit Proficiency",
            "Power often travels on paper.",
            "Borrowed Authority.",
            ),
        (
            "Hermit",
            701,
            "Herbalism Proficiency",
            "The smallest leaf may close a wound",
            "The Living Apothecary.",
            ),
        (
            "Investigator",
            702,
            "Disguise Kit Proficiency",
            "Most doors are guarded by expectations",
            "Play the Part.",
            ),
        )

    for background, seed, title, flavour, heading in fixtures:
        with redirect_stdout(
                StringIO()
                ):
            character = summon_player(
                    species="Human",
                    guild="Fighter",
                    background=background,
                    level=1,
                    seed=seed,
                    )
            data = character.to_dict()

        matches = tuple(
                practice
                for practice in data[ "Practices" ]
                if practice[ "title" ] == title
                )
        assert len( matches ) == 1, background

        sheet = str(
                build_character_sheet(
                        data
                        )
                )
        assert sheet.count( title ) == 1, background
        assert f"<em>{flavour}" in sheet, background
        assert f"<strong>{heading}</strong>" in sheet, background
        assert sheet.index( "Practices" ) < sheet.index( "Equipment" )


def _self_test() -> None:
    class ExampleFeature:
        name = "Example"
        description = "A story with no rule."
        chips = ()
        source = "Example"
        level = 0

    assert _species_identity(
            {
                "Species": "Elf",
                "Heritage": "Dark Elf",
                }
            ) == "Dark Elf"
    assert _species_identity(
            {
                "Species": "Gnome",
                "Heritage": "Forest Gnome",
                }
            ) == "Forest Gnome"
    assert _species_identity(
            {
                "Species": "Tiefling",
                "Heritage": "Infernal",
                }
            ) == "Tiefling (Infernal)"
    assert _class_heading(
            {
                "Class": "Fighter",
                "Subclass": "Battle Master League",
                }
            ) == "Fighter, Battle Master League"
    assert _is_spellcasting_parameter_chip(
            "Species Spell Save DC"
            )
    assert _is_spellcasting_parameter_chip(
            "Spell Attack Bonus"
            )
    assert not _is_spellcasting_parameter_chip(
            "Attack Rolls"
            )

    narrative = ExampleFeature()
    narrative.narrative = True
    narrative_html = str(
            _render_feature(
                    narrative
                    )
            )
    assert "feature-entry is-narrative" in narrative_html

    rule = ExampleFeature()
    rule.narrative = False
    rule_html = str(
            _render_feature(
                    rule
                    )
            )
    assert "feature-entry is-narrative" not in rule_html

    practice_html = str(
            _practice_entries(
                    (
                            {
                                "title": "Disguise Kit Proficiency",
                                "flavour": "Most doors are guarded by expectations.",
                                "sections": (
                                        {
                                            "title": "Play the Part",
                                            "guidance": "You can create a disguise.",
                                            },
                                        ),
                                },
                            )
                    )[ 0 ]
            )
    assert "Disguise Kit Proficiency" in practice_html
    assert "<em>Most doors are guarded by expectations.</em>" in practice_html
    assert "<strong>Play the Part.</strong>" in practice_html

    _test_generated_practices()

    print( "OK — character sheet presentation self-test" )


if __name__ == "__main__":
    _self_test()
