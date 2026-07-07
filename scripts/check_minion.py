#!/usr/bin/env python3
"""
Run-on-save: analyze a Python file and suggest Minion decorators (@minion, @warden, @watcher, @spy, @guardian).

Usage:
  python scripts/check_minion.py [path/to/file.py]
  If no path given, reads path from stdin (one line).

Output: Plain-text suggestions to stdout. Empty output means no suggestions.
"""

import ast
import sys
from pathlib import Path
from typing import List, Optional, Set, Tuple

# Decorator names from Minion.py that we consider "already minionified"
MINION_DECORATORS = frozenset({"minion", "warden", "watcher", "spy", "guardian"})

# File names to skip (no point suggesting minions for the minion system itself)
SKIP_FILES = frozenset({"Minion.py", "check_minion.py"})

# Name patterns → suggested decorator (first match wins)
# @minion: log success/failure, re-raise on failure
# @warden: log + retry with default args on failure
# @watcher: log + enriched error with file locator
# @spy: log call tree (chain of command)
# @guardian: retry with same args until success or max attempts
SUGGESTIONS = (
    # Entry points / main flows → minion (clear success/fail logging)
    (("main", "run", "execute", "start", "entry"), "minion"),
    # Handlers / callbacks → watcher (good error context)
    (("handle", "on_", "callback", "process_"), "watcher"),
    # Fetch/load/save (I/O) → watcher or warden if idempotent
    (("fetch", "load", "read", "get_", "save", "write", "send"), "watcher"),
    # Retry-friendly (default args exist) → warden
    (("connect", "retry", "init_", "setup"), "warden"),
    # Critical / flaky → guardian
    (("critical", "ensure", "must_"), "guardian"),
    # Debug / trace → spy
    (("chain_", "dispatch", "route"), "spy"),
)


def _get_decorator_names(node: ast.FunctionDef) -> Set[str]:
    """Return the names of decorators (e.g. @minion -> 'minion')."""
    names = set()
    for dec in node.decorator_list:
        if isinstance(dec, ast.Name):
            names.add(dec.id)
        if isinstance(dec, ast.Attribute):
            names.add(dec.attr)
        if isinstance(dec, ast.Call):
            if isinstance(dec.func, ast.Name):
                names.add(dec.func.id)
            elif isinstance(dec.func, ast.Attribute):
                names.add(dec.func.attr)
    return names


def _suggest_decorator(func_name: str) -> Optional[str]:
    """Suggest a Minion decorator for a function name, or None."""
    name_lower = func_name.lower()
    for patterns, decorator in SUGGESTIONS:
        for p in patterns:
            if p in name_lower or name_lower.startswith(p.rstrip("_")) or name_lower.endswith(p.lstrip("_")):
                return decorator
    return None


def analyze(path: Path, source: str) -> List[Tuple[str, str]]:
    """
    Return list of (function_name, suggested_decorator) for functions that
    might benefit from a Minion decorator and don't already have one.
    """
    suggestions = []
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return suggestions

    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        if node.name.startswith("_"):
            continue
        decorator_names = _get_decorator_names(node)
        if decorator_names & MINION_DECORATORS:
            continue
        suggested = _suggest_decorator(node.name)
        if suggested:
            suggestions.append((node.name, suggested))

    return suggestions


def main() -> None:
    if len(sys.argv) >= 2:
        file_path = Path(sys.argv[1]).resolve()
    else:
        try:
            line = sys.stdin.readline()
            file_path = Path(line.strip()).resolve() if line else None
        except Exception:
            file_path = None

    if not file_path or not file_path.is_file():
        print("Usage: python scripts/check_minion.py <path/to/file.py>", file=sys.stderr)
        sys.exit(1)

    if file_path.name in SKIP_FILES:
        sys.exit(0)

    try:
        text = file_path.read_text(encoding="utf-8")
    except OSError as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        sys.exit(1)

    rel = file_path.name
    suggestions = analyze(file_path, text)

    if not suggestions:
        sys.exit(0)

    print(f"Minion suggestions for {rel}:")
    for name, dec in suggestions:
        print(f"  Consider @{dec} for {name}()")
    print("(See Minion.py: @minion, @warden, @watcher, @spy, @guardian)")


if __name__ == "__main__":
    main()
