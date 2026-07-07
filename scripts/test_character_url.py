#!/usr/bin/env python3
"""
Tests for character URL seeding (parse_character_params_from_query, character_params_to_query).

Run:
  python scripts/test_character_url.py

Manual test (with Shiny app running on port 8080):
  1. Open by URL: visit
     http://localhost:8080/?species=Human&char_class=Fighter&background=Soldier&level=5&gender=They&seed=42
     → Character panel should open with that character.
  2. Shareable link: generate a character from Home → URL bar updates → copy URL → open in new tab
     → Same character should load.
"""
from __future__ import annotations

import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

from app.character_url import character_params_to_query, parse_character_params_from_query


def test_parse_empty_or_no_seed() -> None:
    assert parse_character_params_from_query(None) is None
    assert parse_character_params_from_query("") is None
    assert parse_character_params_from_query("?species=Human") is None
    assert parse_character_params_from_query("?species=Human&char_class=Fighter") is None


def test_parse_seed_only() -> None:
    got = parse_character_params_from_query("?seed=123")
    assert got == {"seed": 123, "level": 1}


def test_parse_full_query() -> None:
    q = "?species=Human&char_class=Fighter&background=Soldier&level=5&gender=They&seed=42"
    got = parse_character_params_from_query(q)
    assert got == {
        "species": "Human",
        "char_class": "Fighter",
        "background": "Soldier",
        "level": 5,
        "gender": "They",
        "seed": 42,
    }


def test_parse_encoded_values() -> None:
    # "Folk Hero" → Folk%20Hero
    q = "?species=Human&char_class=Fighter&background=Folk%20Hero&level=3&seed=999"
    got = parse_character_params_from_query(q)
    assert got["background"] == "Folk Hero"
    assert got["seed"] == 999
    assert got["level"] == 3


def test_parse_level_clamped() -> None:
    got = parse_character_params_from_query("?seed=1&level=0")
    assert got["level"] == 1
    got = parse_character_params_from_query("?seed=1&level=25")
    assert got["level"] == 20


def test_build_query_empty() -> None:
    assert character_params_to_query({}) == ""
    assert character_params_to_query({"Species": "Human"}) == ""  # no seed


def test_build_query_from_character_dict() -> None:
    # character_params_to_query expects keys: species, char_class, background, level, gender, seed
    data = {
        "species": "Elf",
        "char_class": "Wizard",
        "background": "Sage",
        "level": 7,
        "gender": "They",
        "seed": 12345,
    }
    q = character_params_to_query(data)
    assert "species=Elf" in q
    assert "char_class=Wizard" in q
    assert "background=Sage" in q
    assert "level=7" in q
    assert "gender=They" in q
    assert "seed=12345" in q
    assert q.startswith("?")


def test_roundtrip() -> None:
    data = {
        "species": "Human",
        "char_class": "Fighter",
        "background": "Soldier",
        "level": 5,
        "gender": "They",
        "seed": 42,
    }
    q = character_params_to_query(data)
    parsed = parse_character_params_from_query(q)
    assert parsed == data


def main() -> None:
    test_parse_empty_or_no_seed()
    test_parse_seed_only()
    test_parse_full_query()
    test_parse_encoded_values()
    test_parse_level_clamped()
    test_build_query_empty()
    test_build_query_from_character_dict()
    test_roundtrip()
    print("All character URL tests passed.")


if __name__ == "__main__":
    main()
