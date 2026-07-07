"""Curated unicode symbol pools for presentation chrome.

Avoids emoji and supplementary-symbol codepoints that phones often render as colorful
emoji. Species and class keys add themed glyphs on top of the default lodges.
"""

from __future__ import annotations

import random
from typing import Literal, Sequence

SymbolRole = Literal["sol", "planet"]

# Blocks and ranges that tend to stay "plain text" across platforms.
_SAFE_SINGLE_CODEPOINT = (
    (0x0370, 0x03FF),   # Greek
    (0x16A0, 0x16FF),   # Runic
    (0x0F00, 0x0FFF),   # Tibetan
    (0x2000, 0x206F),   # General punctuation (selected use)
    (0x2190, 0x21FF),   # Arrows
    (0x2200, 0x22FF),   # Mathematical operators
    (0x2300, 0x23FF),   # Miscellaneous technical
    (0x25A0, 0x25FF),   # Geometric shapes
    (0x2600, 0x26FF),   # Miscellaneous symbols
    (0x2700, 0x27BF),   # Dingbats (non-emoji presentation)
)


def _is_safe_symbol(char: str) -> bool:
    """True when the glyph is unlikely to be emoji-rendered on mobile."""
    if not char or len(char) != 1:
        return False
    code = ord(char)
    if code >= 0x1F000:
        return False
    if 0x1F300 <= code <= 0x1FAFF:
        return False
    return any(start <= code <= end for start, end in _SAFE_SINGLE_CODEPOINT)


def _tuple_safe(symbols: Sequence[str]) -> tuple[str, ...]:
    seen: set[str] = set()
    out: list[str] = []
    for symbol in symbols:
        if not _is_safe_symbol(symbol) or symbol in seen:
            continue
        seen.add(symbol)
        out.append(symbol)
    return tuple(out)


# --- Default lodges (expanded from the original Shiny loader, emoji-free) --------

_DEFAULT_SOL: tuple[str, ...] = _tuple_safe(
    (
        "☉", "☼", "✶", "✦", "✧", "✪", "✫", "✬", "✭", "✮", "✯",
        "⚛", "⚜", "⚝", "⚚", "☤", "☥", "☯", "☮", "☸",
        "⛤", "⛥", "⛦", "⛧", "⍟", "⌘", "※", "◈", "◉", "◎",
        "♆", "♃", "♄", "♅", "☿", "♁", "⚳", "⚷", "⚵",
    )
)

_DEFAULT_PLANET: tuple[str, ...] = _tuple_safe(
    (
        "ᚠ", "ᚢ", "ᚦ", "ᚨ", "ᚱ", "ᚲ", "ᚷ", "ᚹ", "ᚺ", "ᚾ",
        "ᛁ", "ᛃ", "ᛇ", "ᛈ", "ᛉ", "ᛊ", "ᛋ", "ᛏ", "ᛒ", "ᛖ",
        "ᛗ", "ᛚ", "ᛜ", "ᛞ", "ᛟ", "ᛡ", "ᛢ", "ᛣ", "ᛤ", "ᛥ",
        "⚝", "⚚", "✦", "✶", "✧", "⛥", "☿", "♆", "◈", "◇",
        "α", "β", "γ", "δ", "ε", "ζ", "η", "θ", "λ", "π", "σ", "φ", "ψ", "ω",
        "∑", "∫", "∂", "∇", "∞", "√", "±", "×", "÷", "≈",
    )
)

# --- Species-themed alphabets ----------------------------------------------------

_SPECIES_SOL: dict[str, tuple[str, ...]] = {
    "Dwarf": _tuple_safe("ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛊᛋᛏᛒᛖᛗᛚᛜᛞᛟ"),
    "Elf": _tuple_safe("✧✦✶✷✸✹✺✻✼✽✾✿❀❁❂❃❄❅❆❇❈❉"),
    "Dragonborn": _tuple_safe("ༀ༁༂༃༄༅༆༇༈༉༊་༌།༎༏༐༑༒༓༔༕༖༗༘༙"),
    "Gnome": _tuple_safe("⚙⚛⚗⚖⚒⚔⚑⚐☊☋♁♃"),
    "Orc": _tuple_safe("ᛦᛧᛨᛩᛪ᛫᛬᛭ᛮᛯᛰ⚔⚒"),
    "Halfling": _tuple_safe("❀❁❂❃❄❅❆❇❈❉✿✾⚘"),
    "Tiefling": _tuple_safe("☤☥♆♇⚸⚶⚵⚴⚳☿"),
    "Human": _tuple_safe("☉☼★☆✪✫✬✭✮✯⚜⚛"),
}

_SPECIES_PLANET: dict[str, tuple[str, ...]] = {
    "Dwarf": _tuple_safe("ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛊᛋᛏᛒᛖᛗᛚᛜᛞᛟ"),
    "Elf": _tuple_safe("ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛊᛋᛏᛒᛖᛗᛚᛜᛞᛟ"),
    "Dragonborn": _tuple_safe("ༀ༁༂༃༄༅༆༇༈༉༊་༌།༎༏༐༑༒༓༔"),
    "Gnome": _tuple_safe("⚙⚛⚗⚖⚒⚑⚐☊☋"),
    "Orc": _tuple_safe("ᛦᛧᛨᛩᛪ᛫᛬᛭ᛮᛯᛰ"),
    "Halfling": _tuple_safe("❀❁❂❃❄❅❆❇❈❉"),
    "Tiefling": _tuple_safe("☤☥♆♇⚸⚶⚵⚴⚳"),
    "Human": _tuple_safe("☉☼★☆✪✫✬✭✮✯"),
}

# --- Class-themed symbols --------------------------------------------------------

_CLASS_SOL: dict[str, tuple[str, ...]] = {
    "Wizard": _tuple_safe("αβγδεζηθικλμνξοπρστυφχψω∑∫∂∇∞√±×÷≈≠≤≥"),
    "Druid": _tuple_safe("✿❀❦⚘✾❁❂❃❄❅❆❇❈❉☘"),
    "Cleric": _tuple_safe("☤☥✠✝☧†‡☩♰♱☯☮"),
    "Paladin": _tuple_safe("⚜⚔⚖☤✠☩♰♱⚛"),
    "Fighter": _tuple_safe("⚔⚒⚑⚐☛☚⛊⛉"),
    "Barbarian": _tuple_safe("ᛦᛧᛨᛩᛪ᛫᛬᛭ᛮᛯᛰ⚔"),
    "Rogue": _tuple_safe("◈◇◆◊○●◐◑◒◓"),
    "Bard": _tuple_safe("♩♪♫♬♭♮♯𝄞𝄢"),
    "Monk": _tuple_safe("☸⚛☯卍卐"),
    "Ranger": _tuple_safe("⛤⛥⛦⛧✦✧✶☄"),
    "Sorcerer": _tuple_safe("✶✷✸✹✺✻✼✽✾✿"),
    "Warlock": _tuple_safe("☿♆♃♄♅⚸⚶⚵⚴⚳"),
}

_CLASS_PLANET: dict[str, tuple[str, ...]] = _CLASS_SOL

# Public defaults (backward-compatible names for the loader)
SOL_SYMBOLS: tuple[str, ...] = _DEFAULT_SOL
PLANET_SYMBOLS: tuple[str, ...] = _DEFAULT_PLANET


def _merge_pools(*pools: Sequence[str]) -> tuple[str, ...]:
    seen: set[str] = set()
    merged: list[str] = []
    for pool in pools:
        for symbol in pool:
            if symbol not in seen and _is_safe_symbol(symbol):
                seen.add(symbol)
                merged.append(symbol)
    return tuple(merged)


def symbols_for(
    *,
    role: SymbolRole = "planet",
    species: str | None = None,
    char_class: str | None = None,
    background: str | None = None,
) -> tuple[str, ...]:
    """Build a symbol pool from current selections (grows as choices accumulate)."""
    base = _DEFAULT_SOL if role == "sol" else _DEFAULT_PLANET
    species_map = _SPECIES_SOL if role == "sol" else _SPECIES_PLANET
    class_map = _CLASS_SOL if role == "sol" else _CLASS_PLANET

    pools: list[Sequence[str]] = [base]
    if species and species in species_map:
        pools.append(species_map[species])
    if char_class and char_class in class_map:
        pools.append(class_map[char_class])
    # Background-themed pools can be added here when a lodge exists.

    merged = _merge_pools(*pools)
    return merged if merged else base


def symbols_for_sol(
    *,
    species: str | None = None,
    char_class: str | None = None,
    background: str | None = None,
) -> tuple[str, ...]:
    return symbols_for(role="sol", species=species, char_class=char_class, background=background)


def symbols_for_planets(
    *,
    species: str | None = None,
    char_class: str | None = None,
    background: str | None = None,
) -> tuple[str, ...]:
    return symbols_for(role="planet", species=species, char_class=char_class, background=background)


def random_sol(
    *,
    species: str | None = None,
    char_class: str | None = None,
    rng: random.Random | None = None,
) -> str:
    pool = symbols_for_sol(species=species, char_class=char_class)
    picker = rng or random
    return picker.choice(pool)


def random_planet(
    *,
    species: str | None = None,
    char_class: str | None = None,
    rng: random.Random | None = None,
) -> str:
    pool = symbols_for_planets(species=species, char_class=char_class)
    picker = rng or random
    return picker.choice(pool)


if __name__ == "__main__":
    assert SOL_SYMBOLS, "default sol lodge must not be empty"
    assert PLANET_SYMBOLS, "default planet lodge must not be empty"
    assert len(SOL_SYMBOLS) == len(set(SOL_SYMBOLS)), "duplicate in SOL_SYMBOLS"
    assert len(PLANET_SYMBOLS) == len(set(PLANET_SYMBOLS)), "duplicate in PLANET_SYMBOLS"

    for symbol in SOL_SYMBOLS + PLANET_SYMBOLS:
        assert _is_safe_symbol(symbol), f"unsafe symbol in defaults: {repr(symbol)}"

    merged = symbols_for(role="planet", species="Dwarf", char_class="Wizard")
    assert "ᚠ" in merged
    assert "α" in merged or "∑" in merged
    assert len(merged) >= len(PLANET_SYMBOLS)

    rng = random.Random(42)
    assert random_sol(rng=rng)
    assert random_planet(rng=rng)

    print("Lodge_of_Symbols self-test passed.")
    print(f"  sol pool: {len(SOL_SYMBOLS)} glyphs")
    print(f"  planet pool: {len(PLANET_SYMBOLS)} glyphs")
    print(f"  dwarf+wizard planet pool: {len(merged)} glyphs")
