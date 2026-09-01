from __future__ import annotations

import asyncio
import inspect
from html import escape
from pathlib import Path
from random import choice, randint
from typing import Any
from app.character_url import (
    character_params_to_hash,
    parse_character_params_from_path,
    parse_character_params_from_url,
)
from app.publish_scope import character_panel_class
from app.publish_scope import fantasy_button_class
from app.publish_scope import home_welcome
from app.publish_scope import npc_panel_class
from app.publish_scope import published_page
from app.publish_scope import tablet_title
from app.publish_scope import tablet_wrapper_attrs

import app.random as random
from app.components.character_sheet import build_character_sheet
from app.components.eldritch import eldritch_head_tags
from AtlasVenustas.Tools_of_Loader import loader_head_tags, loader_panel
from AtlasVenustas.Tools_of_Masonry import masonry_head_tags
from AtlasVenustas.Tools_of_ShareableLinks import shareable_links_head_tags
from AtlasVenustas.Tools_of_Tablet import tablet_head_tags
from AtlasVenustas.Scroll_of_Styles import style_tag
from Minion import chronicler, minion
from shiny import App, reactive, render, ui  
# pyright: ignore[reportMissingImports]

# Atlas imports — plain and loud on purpose (QST-0009, Decree 0003).
# If an Atlas is broken the app must refuse to start with the real traceback,
# never run on placeholder shadows. Resilience lives at the summoning layer,
# where the Minions report every failure and recovery rerolls the seed.
from AtlasActorLudi.Map_of_Scores import Modifier
from AtlasActorLudi.Map_of_Character_Generation import choices, summon_player
from AtlasAlusoris.Grimoire_of_NPC import NPC
from AtlasAlusoris.Map_of_Archetypes import Archetype, Archetypes
from AtlasAlusoris.Map_of_Races import Race, race_weights
from AtlasLusoris.Grimoire_of_Characters import Character
from AtlasLusoris.Map_of_Backgrounds import backgrounds
from AtlasLusoris.Map_of_Classes import classes
from AtlasLusoris.Map_of_Species import species as species_dict
from AtlasPugna.Map_of_Legendary_Actions import Lair, Legendary, Region




def _safe_str(value: Any, fallback: str = "-") -> str:
    if value is None:
        return fallback
    return str(value)


def _safe_int(value: Any, fallback: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return fallback


def _selection_or_none(value: str | None) -> str | None:
    if not value or value == "Random":
        return None
    return value


@minion  # every failed attempt reports its full bug tree; the caller recovers
def _attempt_npc(**kwargs: Any) -> NPC:
    """One summoning attempt. Reporting is the Minion's job; recovery is the caller's."""
    return NPC(**kwargs)


@chronicler  # one creation = one account: repeats collapse to ×N, errors gather at the end
def summon_character(
    species: str | None = None,
    char_class: str | None = None,
    background: str | None = None,
    specialization: str | None = None,
    level: int = 1,
    gender: str | None = None,
    seed: int | None = None,
) -> Character:
    """Hand the user a character via the ActorLudi production line."""
    return summon_player(
        species=_selection_or_none(species),
        guild=_selection_or_none(char_class),
        background=_selection_or_none(background),
        specialization=_selection_or_none(specialization),
        level=level,
        gender=_selection_or_none(gender),
        seed=seed,
    )


@chronicler  # one creation = one account
def summon_npc(
    race: str | None = None,
    archetype: str | None = None,
    level: int = 1,
    seed: int | None = None,
) -> NPC:
    """Always hand the user an NPC: retry fresh seeds on failure, report every error (QST-0009)."""
    max_attempts = 5
    if race == "Random" or not race:
        race = Race()
    if archetype == "Random" or not archetype:
        archetype = Archetype()

    npc_seed = int(seed) if seed is not None else randint(1, 2**16)
    last_error: Exception | None = None

    for _ in range(max_attempts):
        random.seed(npc_seed)
        try:
            return _attempt_npc(race=race, archetype=archetype, level=max(int(level), 1), seed=npc_seed)
        except Exception as exc:  # reported by the @minion above; recover with a fresh seed
            last_error = exc
            npc_seed += 1

    raise RuntimeError("Unable to summon NPC after retries.") from last_error


def _prose(text: Any, placeholder: str = "—") -> ui.Tag:
    """Render generator text as flowing markdown prose — a page, not a cramped box."""
    body = _safe_str(text, "").strip()
    return ui.markdown(body) if body else ui.p(placeholder)


def _html_prose(html: str, placeholder: str = "—") -> ui.Tag:
    """Render pre-built HTML as flowing prose (spells, features with embedded markup)."""
    body = _safe_str(html, "").strip()
    return ui.HTML(body) if body else ui.p(placeholder)


def _text_html(value: Any, placeholder: str = "-") -> ui.Tag:
    """Plain model text as HTML: escape first, then honor newlines as <br> (QST-0012).

    The one safe door for generator strings (skills, saves, senses, story...).
    Code-authored HTML goes through _html_prose instead — never through here.
    """
    text = _safe_str(value, placeholder)
    return ui.HTML(escape(text).replace("\n", "<br>"))


def _attack_rolls_html(obj: Any) -> ui.Tag:
    """Attack rolls table: ability | proficient ⚜️ | base 🔰 (borderless)."""
    abilities = getattr(obj, "ABILITIES", ("STR", "DEX", "CON", "INT", "WIS", "CHA"))
    rows: list[Any] = []
    if obj is not None:
        for abbr in abilities:
            base = getattr(obj, f"{abbr}_base", None)
            prof = getattr(obj, f"{abbr}_prof", None)
            if base is not None and prof is not None:
                rows.append(
                    ui.tags.tr(
                        ui.tags.td(abbr),
                        ui.tags.td({"class": "attack-roll-prof"}, f"{prof:+}⚜️"),
                        ui.tags.td({"class": "attack-roll-base"}, f"{base:+}🔰"),
                    )
                )
    if rows:
        return ui.tags.table(
            {"class": "attack-rolls-table"},
            ui.tags.tbody(*rows),
        )
    value = getattr(obj, "string", obj) if obj is not None else ""
    if callable(value):
        try:
            value = value()
        except Exception:
            value = ""
    return _text_html(value, "-")


def _feature_item(name: str, description: str) -> ui.Tag:
    """Feature name as a title line; description renders as markdown (embedded HTML, e.g.
    spell blurbs, passes through CommonMark untouched — only the markdown syntax is parsed)."""
    body = _safe_str(description, "").strip()
    children: list[Any] = [ui.p({"class": "feature-lead"}, f"{_safe_str(name)}.")]
    if body:
        children.append(ui.markdown(body))
    return ui.div({"class": "feature-entry"}, *children)


def prose_block(title: str, *content: Any, level: int = 2) -> ui.Tag:
    """A full-width tome section: a heading and long-form prose (rules, backstory, spells).

    No callers since QST-0008 moved the NPC sheet onto prose_section.
    Kept only while QST-0026's spell-render audit is Working - retire with it.
    """
    heading = {1: ui.h1, 2: ui.h2, 3: ui.h3}.get(level, ui.h2)
    return ui.div(
        {"class": "npc-textbox npc-textbox--full npc-prose"},
        heading(title),
        ui.div({"class": "prose-body"}, *content),
    )


def prose_section(title: str, *content: Any, level: int = 3, accent: bool = False) -> ui.Tag:
    """A titled prose section in the sheet's main column, divided by a gold rule.
    accent=True styles the heading in the fantasy display face (--font-fantasy)."""
    heading = {1: ui.h1, 2: ui.h2, 3: ui.h3}.get(level, ui.h3)
    cls = "sheet-section is-fantasy" if accent else "sheet-section"
    return ui.div(
        {"class": cls},
        heading(title),
        ui.div({"class": "prose-body"}, *content),
    )


def magic_chip(emoji: str, label: str, value: str, extra_class: str = "") -> ui.Tag:
    """One short stat as a chip: symbol, record label, value. Shared by both sheets.

    extra_class scopes themed variants (e.g. "magic-chip" gives the
    spellcasting chips their script value face) without touching the rest.
    """
    cls = f"npc-box stat-chip {extra_class}".strip()
    return ui.div(
        {"class": cls},
        ui.div({"class": "symbol"}, emoji),
        ui.div({"class": "record"}, label),
        ui.div({"class": "value"}, value),
    )


# Decree / sheet builders still say ``stat_chip``; same helper.
stat_chip = magic_chip


def spellbook_prose(caster: Any) -> str:
    """Quick-reference line above the full spellbook: DC, attack bonus, casting ability."""
    lines: list[str] = []
    try:
        ability = _safe_str(getattr(caster, "casting_stat", ""), "").strip()
        tag = f" · **[{ability.capitalize()}]**" if ability else ""
        lines.append(f"**Spell Save DC** {caster.spell_save_dc()} · **Attack** +{caster.spell_attack_bonus()}{tag}")
    except Exception:
        pass
    slots = getattr(caster, "spell_slots", None)
    if slots:
        try:
            lines.append("**Slots** — " + ", ".join(f"L{lvl}: {n}" for lvl, n in slots.items()))
        except Exception:
            pass
    return "\n\n".join(lines) if lines else "No spells known."


def spellbook_html(caster: Any) -> str:
    """Full spellbook as the caster's own rich HTML (spell slots, DC, one detailed
    card per known spell — rules text and all). Each spell's components line gets
    the casting ability appended, e.g. '[Cha]', so the reader knows what to roll."""
    try:
        html = str(caster)
    except Exception:
        return ""
    ability = _safe_str(getattr(caster, "casting_stat", ""), "").strip()
    if ability:
        html = html.replace("⦔", f" [{ability.capitalize()}]⦔")
    return html


_NPC_CREATURE_TYPE_RACES = frozenset({
    "Aberration", "Beast", "Celestial", "Construct", "Dragon",
    "Elemental", "Fey", "Fiend", "Giant", "Monstrosity", "Ooze", "Plant", "Undead",
})


def _npc_creature_type_label(npc: Any) -> str:
    race = _safe_str(getattr(npc, "race", ""), "")
    if race in _NPC_CREATURE_TYPE_RACES:
        return race
    if race == "Vampire":
        return "Undead"
    return "Humanoid"


def build_npc_sheet(npc: NPC) -> ui.Tag:
    """The NPC page in the character sheet's vocabulary: rail + chips + prose (QST-0008)."""
    race = _safe_str(getattr(npc, "race", "-"))
    subrace = _safe_str(getattr(npc, "subrace", "-"))
    background = _safe_str(getattr(npc, "background", "-"))
    score_emojis = {
        "STR": "\U0001f9be",
        "DEX": "\U0001f962",
        "CON": "\U0001fac0",
        "INT": "\U0001f9e9",
        "WIS": "\U0001f989",
        "CHA": "\U0001f3ad",
    }

    try:
        legendary = str(Legendary(npc))
    except Exception:
        legendary = "Unavailable"

    try:
        lair = str(Lair(npc))
    except Exception:
        lair = "Unavailable"

    try:
        region = str(Region(npc))
    except Exception:
        region = "Unavailable"

    ability = getattr(npc, "ability_scores", None)
    story_text = getattr(npc, "Story", None)
    if story_text in (None, ""):
        try:
            story_text = getattr(npc, "story")
        except Exception:
            story_text = "-"

    def score(name: str) -> int:
        if ability is None:
            return 10
        return _safe_int(getattr(ability, name, 10), 10)

    def row(name: str, emoji: str) -> ui.Tag:
        value = score(name)
        mod = Modifier(value)
        return ui.div(
            {"class": "npc-box", "style": "text-align: right;"},
            ui.div({"class": "symbol"}, emoji),
            ui.h2(f"{name}: {value} {mod:+d}"),
        )

    # --- The rail: scores, skills, saves, and the short list boxes ---
    scores_box = ui.div(
        {"class": "npc-box npc-scores"},
        row("STR", score_emojis["STR"]),
        row("DEX", score_emojis["DEX"]),
        row("CON", score_emojis["CON"]),
        row("INT", score_emojis["INT"]),
        row("WIS", score_emojis["WIS"]),
        row("CHA", score_emojis["CHA"]),
    )
    skills_box = ui.div(
        {"class": "npc-textbox"},
        ui.h2("Skills"),
        _text_html(getattr(getattr(npc, "skills", None), "string", lambda *_: "-")(ability)),
        ui.h4(f"Passive Perception: {_safe_str(getattr(npc, 'passive_perception', '-'))}"),
    )
    saves_box = ui.div(
        {"class": "npc-textbox"},
        ui.h2("Saving Throws"),
        _text_html(getattr(getattr(npc, "saving_throws", None), "string", "-")),
    )
    languages_box = ui.div(
        {"class": "npc-textbox"},
        ui.h2("Languages"),
        _html_prose(getattr(npc, "languages", "-")),
    )
    movement_box = ui.div({"class": "npc-textbox"}, ui.h2("Movement"), _html_prose(getattr(npc, "movement", "-")))
    senses_box = ui.div({"class": "npc-textbox"}, ui.h2("Senses"), _html_prose(getattr(npc, "senses", "-")))
    resistances_box = ui.div({"class": "npc-textbox"}, ui.h2("Resistances"), _html_prose(getattr(npc, "resistances", "-")))

    # --- Short stats as chips, same vocabulary as the character sheet ---
    stat_chips = [
        stat_chip("\u2696\ufe0f", "Alignment", _safe_str(getattr(npc, "alignment", "-"))),
        stat_chip("\U0001f464", "Creature Type", _npc_creature_type_label(npc)),
        stat_chip("\u26a7", "Gender", _safe_str(getattr(npc, "gender", "-"))),
        stat_chip("\U0001f4cf", "Size", _safe_str(getattr(npc, "size", "-"))),
        stat_chip("\u2b06\ufe0f", "Level", _safe_str(getattr(npc, "level", "-"))),
        stat_chip("\u269c\ufe0f", "Proficiency Bonus", f"+{_safe_str(getattr(npc, 'proficiency_bonus', '-'))}"),
        stat_chip("\U0001f49a", "Hit Points", _safe_str(getattr(npc, "HP", "-"))),
        stat_chip("\U0001f6e1\ufe0f", "Armor Class", _safe_str(getattr(npc, "AC", "-"))),
    ]

    # --- Long text flows as prose sections, never boxes (Dialog 0001) ---
    prose_sections = [
        prose_section(
            "Personality",
            ui.h4("Trait"),
            ui.p(ui.tags.i(_safe_str(getattr(npc, "trait", "-")))),
            ui.h4("Ideal"),
            ui.p(ui.tags.i(_safe_str(getattr(npc, "ideal", "-")))),
            ui.h4("Plot Hook"),
            ui.p(ui.tags.i(_safe_str(getattr(npc, "plothook", "-")))),
        ),
        prose_section(
            "Combat Actions",
            ui.h4(f"To hit: +{_safe_str(getattr(npc, 'to_hit_bonus', '-'))}"),
            _prose(getattr(npc, "simple_attacks", "-")),
            _prose(getattr(npc, "special_attack", "-")),
        ),
        prose_section(
            f"Spellcasting: {_safe_str(getattr(npc, 'spellcasting_ability', '-'))}",
            ui.h4(f"Spell Save DC: {_safe_str(getattr(npc, 'spell_save_dc', '-'))}"),
            ui.h4(f"To hit: +{_safe_str(getattr(npc, 'spell_attack_bonus', '-'))}"),
            _prose(getattr(npc, "spells", "-")),
            accent=True,
        ),
        prose_section("Martial Abilities", _prose(getattr(npc, "martial", "-"))),
        prose_section("Legendary", _prose(legendary)),
        prose_section("Lair", _prose(lair)),
        prose_section("Region", _prose(region)),
        prose_section("My Story", _prose(story_text)),
    ]

    return ui.div(
        {"class": "sheet note-lines"},
        ui.div(
            {"class": "npc-header"},
            ui.h2({"class": "character-name"}, _safe_str(getattr(npc, "name", "Unknown"))),
            ui.h2({"class": "character-title"}, _safe_str(getattr(npc, "title", ""))),
            ui.h1(f"{race}: {subrace}"),
            ui.h1(background),
        ),
        ui.div(
            {"class": "sheet-body"},
            ui.div(
                {"class": "sheet-rail"},
                ui.div({"class": "stat-flow"}, *stat_chips),
                scores_box,
                skills_box,
                saves_box,
                languages_box,
                movement_box,
                senses_box,
                resistances_box,
            ),
            ui.div(
                {"class": "sheet-main"},
                *prose_sections,
            ),
        ),
    )


NPC_LIST_SIZE = 5

RACES = sorted([race for race in race_weights.keys() if race])
RACES.insert(0, "Random")

SPECIES = sorted(species_dict.keys())
SPECIES.insert(0, "Random")

CLASSES = ["Random", *sorted(classes)]
# Home tablet stays lean; the sheet offers the full Player catalogue.
BACKGROUNDS = ["Random", *sorted(backgrounds)]
_SHEET_CHOICES = choices()
SHEET_BACKGROUNDS = ["Random", *list(_SHEET_CHOICES.backgrounds)]
SPECIALIZATIONS_BY_GUILD = {
    guild: ["Random", *list(specs)]
    for guild, specs in _SHEET_CHOICES.specializations.items()
}
ARCHETYPES = ["Random", *sorted(Archetypes)]


def _specialization_options(guild: str | None) -> tuple[str, ...]:
    if not guild or guild == "Random":
        return ("Random",)
    return tuple(SPECIALIZATIONS_BY_GUILD.get(guild, ["Random"]))


def _specialization_selection(
    current: dict[str, Any] | None,
    selected_guild: str | None,
    available: tuple[str, ...],
) -> str:
    current = current or {}
    if selected_guild != current.get("char_class"):
        return "Random"
    specialization = current.get("specialization")
    if specialization in available:
        return specialization
    return "Random"


home_panel = ui.div(
    {"class": "main-content"},
    ui.h2("Welcome to Gen Legend"),
    ui.p(home_welcome()),
    ui.div(
        tablet_wrapper_attrs(),
        ui.div(
            {"class": "tablet-controls"},
            ui.tags.button(
                {
                    "class": "tablet-nav prev fantasy-button",
                    "type": "button",
                    "aria-label": "Previous generator",
                    "style": "min-width:2.2em; min-height:2.2em; width:2.2em; height:2.2em; font-size:1.3em; line-height:1em; padding:0; display:inline-flex; align-items:center; justify-content:center;",
                },
                ui.HTML("<span aria-hidden='true' style='display:block;'>&#x2039;</span>"),
            ),
            ui.h3({"id": "tablet-title", "class": "tablet-title"}, tablet_title()),
            ui.tags.button(
                {
                    "class": "tablet-nav next fantasy-button",
                    "type": "button",
                    "aria-label": "Next generator",
                    "style": "min-width:2.2em; min-height:2.2em; width:2.2em; height:2.2em; font-size:1.3em; line-height:1em; padding:0; display:inline-flex; align-items:center; justify-content:center;",
                },
                ui.HTML("<span aria-hidden='true' style='display:block;'>&#x203A;</span>"),
            ),
        ),
        ui.div(
            {"class": "tablet-viewport"},
            ui.div(
                {"class": "tablet-rotator"},
                ui.tags.section(
                    {"class": character_panel_class(), "data-title": "Character Generator"},
                    ui.h3("Generate Character"),
                    ui.input_select("char_species", "Species", SPECIES),
                    ui.input_select("char_class", "Class", CLASSES),
                    ui.input_select("char_background", "Background", BACKGROUNDS),
                    ui.div(
                        {"class": "tablet-actions"},
                        ui.input_action_button(
                            "btn_gen_char",
                            "Generate Character",
                            class_="fantasy-button",
                        ),
                    ),
                ),
                ui.tags.section(
                    {"class": npc_panel_class(), "data-title": "NPC Generator"},
                    ui.h3("Generate Non Player Character"),
                    ui.div(
                        {"class": "number-input fantasy-input"},
                        ui.tags.button({"type": "button", "class": "minus fantasy-button fantasy-input"}, "-"),
                        ui.input_numeric("npc_level", "Level", value=5, min=1, max=100),
                        ui.tags.button({"type": "button", "class": "plus fantasy-button fantasy-input"}, "+"),
                    ),
                    ui.input_select("npc_race", "Race", RACES),
                    ui.input_select("npc_archetype", "Archetype", ARCHETYPES),
                    ui.div(
                        {"class": "tablet-actions"},
                        ui.input_action_button("btn_gen_npc", "Generate NPC", class_="fantasy-button"),
                        ui.input_action_button("btn_gen_list", "Generate 5 NPCs", class_="fantasy-button"),
                    ),
                ),
            ),
        ),
        ui.div({"class": "tablet-dots", "aria-label": "Generator navigation"}),
    ),
)


character_panel = ui.div(
    ui.h2({"class": "page-title"}, "Character Sheet"),
    ui.div(
        {"class": "character-reforge"},
        ui.div(
            {"class": "character-reforge-field character-reforge-field--species"},
            ui.input_select("char_sheet_species", "", SPECIES, selected="Random"),
        ),
        ui.div(
            {"class": "character-reforge-field character-reforge-field--background"},
            ui.input_select("char_sheet_background", "", SHEET_BACKGROUNDS, selected="Random"),
        ),
        ui.div(
            {"class": "character-reforge-field character-reforge-field--class"},
            ui.input_select("char_sheet_class", "", CLASSES, selected="Random"),
            ui.input_select(
                "char_sheet_specialization",
                "",
                _specialization_options(None),
                selected="Random",
            ),
        ),
        ui.div(
            {"class": "character-level-box"},
            ui.div({"class": "character-level-label"}, "Level"),
            ui.tags.div(
                {"class": "character-level-controls"},
                ui.input_action_button(
                    "btn_char_level_down",
                    "-",
                    class_="minus fantasy-button fantasy-input",
                    title="Level Down",
                    aria_label="Level Down",
                ),
                ui.input_action_button(
                    "btn_char_level_up",
                    "+",
                    class_="plus fantasy-button fantasy-input",
                    title="Level Up",
                    aria_label="Level Up",
                ),
            ),
        ),
        ui.div(
            {"class": "character-generate-wrap"},
            ui.input_action_button("btn_char_apply_selectors", "Generate", class_="fantasy-button"),
        ),
        ui.div(
            {"class": "character-share-wrap"},
            ui.input_action_button("btn_copy_char_link", "Share", class_="fantasy-button share-button"),
        ),
        ui.tags.span(
            {"id": "share-copy-status", "class": "share-copy-status character-reforge-status", "aria-live": "polite"}
        ),
    ),
    ui.hr(),
    ui.output_ui("character_result"),
)


npc_panel = ui.div(
    ui.h2({"class": "page-title"}, "NPC Sheet"),
    ui.div(
        {"class": "npc-button-selectors"},
        ui.input_action_button("btn_gen_npc_again", "Try Again", class_="fantasy-button"),
        ui.input_action_button("go_home_from_npc", "Back Home", class_="fantasy-button"),
    ),
    ui.hr(),
    ui.output_ui("npc_result"),
)


npclist_panel = ui.div(
    {"class": "main-content"},
    ui.h2({"class": "page-title"}, "Legendary NPC List"),
    ui.output_ui("npc_list_result"),
    ui.tags.br(),
    ui.input_action_button("btn_gen_list_again", "5 New NPCs", class_="fantasy-button"),
)


app_ui = ui.page_fluid(
    ui.tags.head(
        ui.tags.meta(charset="utf-8"),
        ui.tags.meta(name="viewport", content="width=device-width, initial-scale=1"),
        ui.tags.title("Gen Legend (Shiny)"),
        ui.tags.link(rel="preconnect", href="https://fonts.googleapis.com"),
        ui.tags.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=Cinzel:ital@0;1&display=swap", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=IM+Fell+English", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=IM+Fell+DW+Pica", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=IM+Fell+DW+Pica+SC", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=IM+Fell+Great+Primer:ital@0;1", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=IM+Fell+Great+Primer+SC", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=IM+Fell+Double+Pica:ital@0;1", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=IM+Fell+Double+Pica+SC", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=IM+Fell+English+SC", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=Spectral+SC:wght@400;600;700", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=Eagle+Lake", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=Italianno", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=Beau+Rivage", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=Fleur+De+Leah", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=IM+Fell+French+Canon+SC", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=Tangerine:wght@400;700", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=Manufacturing+Consent", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=UnifrakturMaguntia", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=Italianno", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=Beau+Rivage", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=Fleur+De+Leah", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=Manufacturing+Consent", rel="stylesheet"),
        ui.tags.link(href="https://fonts.googleapis.com/css2?family=UnifrakturMaguntia", rel="stylesheet"),
        style_tag(),
        *tablet_head_tags(),
        *loader_head_tags(),
        *masonry_head_tags(),
        *shareable_links_head_tags(),
        *eldritch_head_tags(),
    ),
    loader_panel(),
    ui.tags.header(
        ui.h1(ui.tags.a({"href": "#", "style": "color: inherit; text-decoration: none;"}, "Gen Legend")),
        ui.tags.div(
            {"class": "header-actions"},
            ui.input_action_button("go_home", "Home", class_=fantasy_button_class()),
            ui.input_action_button("go_character", "Character", class_=fantasy_button_class()),
            ui.input_action_button("go_npc", "NPC", class_=fantasy_button_class(parked=True)),
            ui.input_action_button("go_npclist", "NPC List", class_=fantasy_button_class(parked=True)),
        ),
    ),
    ui.div(
        {"class": "main-wrap"},
        ui.div(
            {"class": "container"},
            ui.output_ui("active_page"),
        ),
    ),
    ui.tags.footer(
        {
            "style": "background: #231c27; color: #f6d67c; padding: 1.15em 0; text-align: center; font-size: 1.03em; margin-top: 2em; border-top: 3px solid #786110; letter-spacing: 0.01em;"
        },
        ui.tags.a(
            "About Us",
            href="https://github.com/JulTob/DnD#readme",
            target="_blank",
            rel="noopener",
            style="color: #f6d67c; text-decoration: none; font-weight: bold; margin: 0 1.5em;",
        ),
        ui.tags.span("|", style="margin: 0 1.5em;"),
        ui.tags.a(
            "Lore Wiki",
            href="https://github.com/JulTob/DnD/wiki",
            target="_blank",
            rel="noopener",
            style="color: #f6d67c; text-decoration: none; font-weight: bold; margin: 0 1.5em;",
        ),
        ui.tags.span("|", style="margin: 0 1.5em;"),
        ui.tags.span(
            "By ",
            ui.tags.a(
                "Julio Toboso",
                href="https://github.com/JulTob",
                target="_blank",
                rel="noopener",
                style="color: #f6d67c; text-decoration: underline dashed; font-weight: bold;",
            ),
            style="color: #f6d67c;",
        ),
    ),
)



def server(input, output, session):
    page_state = reactive.value("home")
    character_state = reactive.value(None)
    character_params_state = reactive.value(None)
    character_error = reactive.value(None)
    npc_state = reactive.value(None)
    npc_error = reactive.value(None)
    npc_list_state = reactive.value([])
    npc_list_error = reactive.value(None)
    initial_character_url_processed = reactive.value(False)

    def show_page(page: str) -> None:
        page_state.set(published_page(page))

    def _send_custom_message(message_type: str, message_data: dict[str, Any]) -> None:
        message = session.send_custom_message(message_type, message_data)

        if inspect.isawaitable(message):
            asyncio.create_task(message)

    def _set_loader(action: str) -> None:
        _send_custom_message("set_loader", {"action": action})

    def _clean_character_param(value: Any) -> str | None:
        if value is None:
            return None
        text = str(value).strip()
        if not text or text == "Random":
            return None
        return text

    def _character_params_from_data(
        data: dict[str, Any] | None,
        fallback: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        base = fallback or {}
        payload = data or {}
        level_value = payload.get("Level", base.get("level", 1))
        level = max(1, min(20, _safe_int(level_value, 1)))
        seed_value = payload.get("Seed", payload.get("seed", base.get("seed")))
        try:
            seed = int(seed_value) if seed_value is not None else None
        except (TypeError, ValueError):
            seed = None
        return {
            "species": _clean_character_param(payload.get("Species", base.get("species"))),
            "char_class": _clean_character_param(payload.get("Class", base.get("char_class"))),
            "specialization": _clean_character_param(
                payload.get("Specialization", base.get("specialization"))
            ),
            "background": _clean_character_param(payload.get("Background", base.get("background"))),
            "level": level,
            "gender": _clean_character_param(payload.get("Gender", base.get("gender"))),
            "seed": seed,
        }

    def _apply_character_form_defaults(params: dict[str, Any]) -> None:
        species = params.get("species") if params.get("species") in SPECIES else "Random"
        char_class = params.get("char_class") if params.get("char_class") in CLASSES else "Random"
        background = params.get("background") if params.get("background") in BACKGROUNDS else "Random"
        ui.update_select("char_species", selected=species)
        ui.update_select("char_class", selected=char_class)
        ui.update_select("char_background", selected=background)
        _apply_character_sheet_defaults(params)

    def _apply_character_sheet_defaults(params: dict[str, Any]) -> None:
        species = params.get("species") if params.get("species") in SPECIES else "Random"
        char_class = params.get("char_class") if params.get("char_class") in CLASSES else "Random"
        available = _specialization_options(_selection_or_none(char_class))
        specialization = _specialization_selection(params, _selection_or_none(char_class), available)
        background = (
            params.get("background")
            if params.get("background") in SHEET_BACKGROUNDS
            else "Random"
        )
        ui.update_select("char_sheet_species", selected=species)
        ui.update_select("char_sheet_class", selected=char_class)
        ui.update_select(
            "char_sheet_specialization",
            choices=list(available),
            selected=specialization,
        )
        ui.update_select("char_sheet_background", selected=background)

    def _push_character_url(params: dict[str, Any]) -> None:
        if params.get("seed") is None:
            return
        url_hash = character_params_to_hash(params)
        if url_hash:
            _send_custom_message("update_character_url", {"hash": url_hash})
            _send_custom_message("set_share_hash", {"hash": url_hash})

    def _generate_character_from_params(
        params: dict[str, Any],
        *,
        show_character_page: bool = True,
        sync_form_defaults: bool = False,
    ) -> None:
        try:
            character = summon_character(
                species=params.get("species"),
                char_class=params.get("char_class"),
                specialization=params.get("specialization"),
                background=params.get("background"),
                level=max(1, min(20, _safe_int(params.get("level"), 1))),
                gender=params.get("gender"),
                seed=params.get("seed"),
            )
            data = character.to_dict()
            character_state.set(data)
            character_error.set(None)
            canonical = _character_params_from_data(data, fallback=params)
            character_params_state.set(canonical)
            _apply_character_sheet_defaults(canonical)
            if sync_form_defaults:
                _apply_character_form_defaults(canonical)
            _push_character_url(canonical)
            if show_character_page:
                show_page("character")
        except Exception as exc:
            character_error.set(str(exc))
            if show_character_page:
                show_page("character")
        finally:
            _set_loader("hide")

    @reactive.effect
    def _init_character_from_url() -> None:
        if initial_character_url_processed():
            return
        pathname_fn = getattr(session.clientdata, "url_pathname", None)
        pathname = pathname_fn() if callable(pathname_fn) else None
        search = session.clientdata.url_search()
        hash_fn = getattr(session.clientdata, "url_hash", None)
        hash_value = hash_fn() if callable(hash_fn) else None
        params = parse_character_params_from_url(pathname, search, hash_value)
        if params is None:
            initial_character_url_processed.set(True)
            return
        initial_character_url_processed.set(True)
        _set_loader("show")
        _generate_character_from_params(
            params,
            show_character_page=True,
            sync_form_defaults=True,
        )

    @reactive.effect
    @reactive.event(input.go_home, input.go_home_from_npc)
    def _go_home() -> None:
        show_page("home")

    @reactive.effect
    @reactive.event(input.go_character)
    def _go_character() -> None:
        initial_character_url_processed.set(True)
        _set_loader("show")
        _generate_character_from_params(
            {"level": 1, "seed": randint(0, 2**16)},
            show_character_page=True,
        )

    @reactive.effect
    @reactive.event(input.go_npc)
    def _go_npc() -> None:
        show_page("npc")

    @reactive.effect
    @reactive.event(input.go_npclist)
    def _go_npclist() -> None:
        show_page("npclist")

    @reactive.effect
    @reactive.event(input.btn_gen_char)
    def _generate_character_from_form() -> None:
        initial_character_url_processed.set(True)
        _set_loader("show")
        _generate_character_from_params(
            {
                "species": _selection_or_none(input.char_species()),
                "char_class": _selection_or_none(input.char_class()),
                "background": _selection_or_none(input.char_background()),
                "level": 1,
                "seed": randint(0, 2**16),
            },
            show_character_page=True,
        )

    @reactive.effect
    @reactive.event(input.btn_char_level_down)
    def _level_character_down() -> None:
        initial_character_url_processed.set(True)
        current = character_params_state() or _character_params_from_data(character_state())
        current_level = max(1, min(20, _safe_int(current.get("level"), 1)))
        next_level = max(1, current_level - 1)
        if next_level == current_level or current.get("seed") is None:
            _set_loader("hide")
            return
        next_params = dict(current)
        next_params["level"] = next_level
        _set_loader("show")
        _generate_character_from_params(next_params, show_character_page=False)

    @reactive.effect
    @reactive.event(input.btn_char_level_up)
    def _level_character_up() -> None:
        initial_character_url_processed.set(True)
        current = character_params_state() or _character_params_from_data(character_state())
        current_level = max(1, min(20, _safe_int(current.get("level"), 1)))
        next_level = min(20, current_level + 1)
        if next_level == current_level or current.get("seed") is None:
            _set_loader("hide")
            return
        next_params = dict(current)
        next_params["level"] = next_level
        _set_loader("show")
        _generate_character_from_params(next_params, show_character_page=False)

    @reactive.effect
    @reactive.event(input.btn_char_apply_selectors)
    def _apply_character_selectors() -> None:
        initial_character_url_processed.set(True)
        current = character_params_state() or _character_params_from_data(character_state())
        level = max(1, min(20, _safe_int(current.get("level"), 1)))
        params = {
            "species": _selection_or_none(input.char_sheet_species()),
            "char_class": _selection_or_none(input.char_sheet_class()),
            "specialization": _selection_or_none(input.char_sheet_specialization()),
            "background": _selection_or_none(input.char_sheet_background()),
            "gender": current.get("gender"),
            "level": level,
            "seed": randint(0, 2**16),
        }
        _set_loader("show")
        _generate_character_from_params(params, show_character_page=True)

    @reactive.effect
    def _update_specialization_selector() -> None:
        selected_guild = _selection_or_none(input.char_sheet_class())
        available = _specialization_options(selected_guild)
        current = character_params_state() or _character_params_from_data(character_state())
        selected = _specialization_selection(current, selected_guild, available)
        ui.update_select(
            "char_sheet_specialization",
            choices=list(available),
            selected=selected,
        )

    @reactive.effect
    @reactive.event(input.btn_gen_npc)
    def _generate_npc_from_form() -> None:
        selected_race = input.npc_race()
        selected_archetype = input.npc_archetype()
        level = _safe_int(input.npc_level(), 5)
        _set_loader("show")

        try:
            npc = summon_npc(
                race=selected_race,
                archetype=selected_archetype,
                level=level,
                seed=randint(1, 2**16),
            )
            npc_state.set(npc)
            npc_error.set(None)
            show_page("npc")
        except Exception as exc:
            npc_error.set(str(exc))
            show_page("npc")
        finally:
            _set_loader("hide")

    @reactive.effect
    @reactive.event(input.btn_gen_npc_again)
    def _generate_npc_again() -> None:
        current = npc_state()
        _set_loader("show")

        try:
            if current is None:
                npc = summon_npc(level=_safe_int(input.npc_level(), 5), seed=randint(1, 2**16))
            else:
                npc = summon_npc(
                    race=getattr(current, "race", None),
                    archetype=getattr(current, "archetype", None),
                    level=_safe_int(getattr(current, "level", 1), 1),
                    seed=randint(1, 2**16),
                )
            npc_state.set(npc)
            npc_error.set(None)
        except Exception as exc:
            npc_error.set(str(exc))
        finally:
            _set_loader("hide")

    @reactive.effect
    @reactive.event(input.btn_gen_list, input.btn_gen_list_again)
    def _generate_npc_list() -> None:
        race_in = input.npc_race()
        archetype_in = input.npc_archetype()
        seed = randint(0, 16383)
        _set_loader("show")

        try:
            npcs = []
            for idx in range(NPC_LIST_SIZE):
                current_race = race_in
                current_archetype = archetype_in

                if current_race == "Random":
                    current_race = choice(list(race_weights.keys()))
                if current_archetype == "Random":
                    current_archetype = choice(Archetypes)

                npcs.append(
                    NPC(
                        race=current_race,
                        archetype=current_archetype,
                        lvl=randint(1, 20),
                        seed=seed + idx,
                    )
                )

            npc_list_state.set(npcs)
            npc_list_error.set(None)
            show_page("npclist")
        except Exception as exc:
            npc_list_error.set(str(exc))
            show_page("npclist")
        finally:
            _set_loader("hide")

    @output
    @render.ui
    def active_page() -> ui.Tag:
        pages = {
            "home": home_panel,
            "character": character_panel,
            "npc": npc_panel,
            "npclist": npclist_panel,
        }
        return pages.get(page_state(), home_panel)

    @output
    @render.ui
    def character_result() -> ui.Tag:
        err = character_error()
        if err:
            return ui.div({"class": "fallback-card"}, ui.h3("Character generation failed"), ui.p(err))

        data = character_state()
        if not data:
            return ui.div({"class": "fallback-card"}, ui.p("Generate a character from Home."))

        return build_character_sheet(data)

    @output
    @render.ui
    def npc_result() -> ui.Tag:
        err = npc_error()
        if err:
            return ui.div({"class": "fallback-card"}, ui.h3("NPC generation failed"), ui.p(err))

        npc = npc_state()
        if npc is None:
            return ui.div({"class": "fallback-card"}, ui.p("Generate an NPC from Home."))

        return build_npc_sheet(npc)

    def _open_npc_from_list(index: int) -> None:
        """A list entry was clicked: show that exact NPC on the NPC page.

        The stored object is shown directly - regenerating from its seed is
        NOT reproducible today (mixed RNG sources; evidence for Dialog 0003),
        and the user clicked a name, so the name must match.
        """
        npcs = npc_list_state()
        if not npcs or index >= len(npcs):
            return
        npc_state.set(npcs[index])
        npc_error.set(None)
        show_page("npc")

    for _list_index in range(NPC_LIST_SIZE):

        @reactive.effect
        @reactive.event(getattr(input, f"npc_list_open_{_list_index}"))
        def _open_listed_npc(index: int = _list_index) -> None:
            #-- default-arg pins each observer to its own slot (no late binding)
            _open_npc_from_list(index)

    @output
    @render.ui
    def npc_list_result() -> ui.Tag:
        err = npc_list_error()
        if err:
            return ui.div({"class": "fallback-card"}, ui.h3("NPC list generation failed"), ui.p(err))

        npcs = npc_list_state()
        if not npcs:
            return ui.div({"class": "fallback-card"}, ui.p("Generate 5 NPCs from Home."))

        rows = []
        for index, npc in enumerate(npcs[:NPC_LIST_SIZE]):
            rows.append(
                ui.input_action_link(
                    f"npc_list_open_{index}",
                    ui.TagList(
                        ui.h1(ui.tags.i(_safe_str(getattr(npc, "name", "Unknown")))),
                        ui.h2(_safe_str(getattr(npc, "title", ""))),
                        ui.h3(f"{_safe_str(getattr(npc, 'race', '-'))} {_safe_str(getattr(npc, 'archetype', '-'))}"),
                    ),
                    style="color: inherit; text-decoration: none;",
                )
            )

        return ui.div(
            {"class": "npc-list", "style": "display: flex; flex-direction: column; gap: 1.3em; font-size: 1.1em; padding-top: 1em;"},
            *rows,
        )


def _canonical_base_path(pathname: str) -> str:
    path = pathname or "/"
    marker = "/character/"
    idx = path.find(marker)
    if idx >= 0:
        path = path[: idx + 1]
    elif path.endswith("/character"):
        path = path[: -len("character")]
    return path or "/"


async def _send_redirect(send, location: str, status: int = 307) -> None:
    headers = [
        (b"location", location.encode("utf-8")),
        (b"cache-control", b"no-store"),
    ]
    await send({"type": "http.response.start", "status": status, "headers": headers})
    await send({"type": "http.response.body", "body": b""})


class CharacterPathRedirectASGI:
    """
    Accept legacy/shareable /character/... paths and redirect to canonical hash URLs,
    so direct opens don't hit a 404 before Shiny starts.
    """

    def __init__(self, wrapped_app):
        self.wrapped_app = wrapped_app

    async def __call__(self, scope, receive, send):
        if scope.get("type") == "http" and (scope.get("method") or "GET").upper() == "GET":
            path = str(scope.get("path") or "")
            if path.endswith("/character"):
                await _send_redirect(send, _canonical_base_path(path), status=307)
                return

            if "/character/" in path:
                params = parse_character_params_from_path(path)
                if params is not None:
                    url_hash = character_params_to_hash(params)
                    if url_hash:
                        target = f"{_canonical_base_path(path)}{url_hash}"
                        await _send_redirect(send, target, status=307)
                        return
                # If malformed character path, still land users on app instead of raw 404.
                await _send_redirect(send, _canonical_base_path(path), status=307)
                return

        await self.wrapped_app(scope, receive, send)


_shiny_app = App(app_ui, server, static_assets={"/static": Path(__file__).parent / "app" / "static"})
app = CharacterPathRedirectASGI(_shiny_app)
