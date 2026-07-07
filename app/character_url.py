# app/character_url.py — URL params for shareable character links
from __future__ import annotations

from urllib.parse import parse_qs, quote, quote_plus, unquote, unquote_plus
from typing import Any

CHARACTER_URL_KEYS = ("species", "char_class", "background", "level", "gender", "seed")
PATH_NULL_MARKERS = {"", "_", "random", "none", "null"}


def _normalize_level(value: Any, default: int = 1) -> int:
    try:
        return max(1, min(20, int(value)))
    except (TypeError, ValueError):
        return default


def _normalize_seed(value: Any) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _normalize_dimension(value: Any) -> str | None:
    if value is None:
        return None
    text = unquote_plus(str(value).strip())
    if not text or text == "Random":
        return None
    return text


def _normalize_path_dimension(value: Any) -> str | None:
    if value is None:
        return None
    text = unquote(str(value).strip())
    if text.lower() in PATH_NULL_MARKERS:
        return None
    return text


def _path_segment(value: Any, *, fallback: str = "random") -> str:
    text = _normalize_dimension(value)
    if text is None:
        text = fallback
    return quote(text, safe="")


def parse_character_params_from_query(search: str | None) -> dict[str, Any] | None:
    """
    Parse URL query string into character init args. Returns None if no seed.
    Keys: species, char_class, background, level, gender, seed.
    """
    if not search or not search.strip().lstrip("?").strip():
        return None
    raw = search.strip().lstrip("?")
    try:
        parsed = parse_qs(raw, keep_blank_values=False)
    except Exception:
        return None
    if "seed" not in parsed:
        return None
    seed_raw = parsed["seed"][0] if isinstance(parsed["seed"], list) else parsed["seed"]
    seed = _normalize_seed(seed_raw)
    if seed is None:
        return None
    out: dict[str, Any] = {"seed": seed}
    for key in ("species", "char_class", "background", "gender"):
        if key in parsed and parsed[key]:
            val = parsed[key][0] if isinstance(parsed[key], list) else parsed[key]
            out[key] = _normalize_dimension(val)
    if "level" in parsed and parsed["level"]:
        out["level"] = _normalize_level(parsed["level"][0], default=1)
    else:
        out["level"] = 1
    return out


def parse_character_params_from_path(pathname: str | None) -> dict[str, Any] | None:
    """
    Parse path formats:
      New canonical format:
        /character/<level>/<species>/<background>/<char_class>/<gender>/<seed>
      Legacy Flask format:
        /character/<species>/<char_class>/<background>/<level>/<gender>/<seed>
    """
    if not pathname:
        return None
    parts = [p for p in pathname.strip().strip("/").split("/") if p]
    try:
        char_idx = parts.index("character")
    except ValueError:
        return None
    if len(parts) < char_idx + 7:
        return None
    seg1, seg2, seg3, seg4, seg5, seg6 = parts[char_idx + 1:char_idx + 7]

    # New canonical format: level/species/background/class/gender/seed
    first_as_level = _normalize_seed(unquote(seg1))
    if first_as_level is not None:
        seed = _normalize_seed(unquote(seg6))
        if seed is None:
            return None
        return {
            "level": _normalize_level(first_as_level, default=1),
            "species": _normalize_path_dimension(seg2),
            "background": _normalize_path_dimension(seg3),
            "char_class": _normalize_path_dimension(seg4),
            "gender": _normalize_path_dimension(seg5),
            "seed": seed,
        }

    # Legacy format: species/class/background/level/gender/seed
    seed = _normalize_seed(unquote(seg6))
    if seed is None:
        return None
    return {
        "species": _normalize_path_dimension(seg1),
        "char_class": _normalize_path_dimension(seg2),
        "background": _normalize_path_dimension(seg3),
        "level": _normalize_level(unquote(seg4), default=1),
        "gender": _normalize_path_dimension(seg5),
        "seed": seed,
    }


def parse_character_params_from_hash(hash_value: str | None) -> dict[str, Any] | None:
    """
    Parse compact hash format:
      #/<level>/<species>/<background>/<char_class>/<gender>/<seed>
    Also accepts optional "character" prefix in hash:
      #/character/<level>/<species>/<background>/<char_class>/<gender>/<seed>
    """
    if not hash_value:
        return None
    raw = hash_value.strip()
    if not raw:
        return None
    if raw.startswith("#"):
        raw = raw[1:]
    raw = raw.strip("/")
    if not raw:
        return None
    parts = [p for p in raw.split("/") if p]
    if parts and parts[0].lower() == "character":
        parts = parts[1:]
    if len(parts) < 6:
        return None
    level_raw, species_raw, background_raw, class_raw, gender_raw, seed_raw = parts[:6]
    seed = _normalize_seed(unquote(seed_raw))
    if seed is None:
        return None
    return {
        "level": _normalize_level(unquote(level_raw), default=1),
        "species": _normalize_path_dimension(species_raw),
        "background": _normalize_path_dimension(background_raw),
        "char_class": _normalize_path_dimension(class_raw),
        "gender": _normalize_path_dimension(gender_raw),
        "seed": seed,
    }


def parse_character_params_from_url(
    pathname: str | None,
    search: str | None,
    hash_value: str | None = None,
) -> dict[str, Any] | None:
    """
    Parse character params from URL with precedence:
      1) compact hash format
      2) path format(s)
      3) query-string format
    """
    hash_params = parse_character_params_from_hash(hash_value)
    if hash_params is not None:
        return hash_params
    path_params = parse_character_params_from_path(pathname)
    if path_params is not None:
        return path_params
    return parse_character_params_from_query(search)


def character_params_to_compact(data: dict[str, Any]) -> str:
    """
    Build canonical compact format:
      <level>/<species>/<background>/<char_class>/<gender>/<seed>
    Missing dimensions are encoded as 'random' so the format is always parseable.
    """
    seed = _normalize_seed(data.get("seed"))
    if seed is None:
        return ""
    level = _normalize_level(data.get("level"), default=1)
    species = _path_segment(data.get("species"))
    background = _path_segment(data.get("background"))
    char_class = _path_segment(data.get("char_class"))
    gender = _path_segment(data.get("gender"))
    return f"{level}/{species}/{background}/{char_class}/{gender}/{seed}"


def character_params_to_path(data: dict[str, Any]) -> str:
    compact = character_params_to_compact(data)
    return f"/character/{compact}" if compact else ""


def character_params_to_hash(data: dict[str, Any]) -> str:
    compact = character_params_to_compact(data)
    return f"#/{compact}" if compact else ""


def character_params_to_query(data: dict[str, Any]) -> str:
    """Build query string from params dict (species, char_class, background, level, gender, seed)."""
    parts = []
    for key in CHARACTER_URL_KEYS:
        val = data.get(key)
        if val is None:
            continue
        if key == "level":
            val = _normalize_level(val, default=1)
        parts.append(f"{key}={quote_plus(str(val))}")
    return "?" + "&".join(parts) if parts else ""
