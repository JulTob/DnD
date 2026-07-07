#!/usr/bin/env python3
"""
Scheduled review queue: advance through all project Python files and print the next
review prompt. Run every 30 minutes (e.g. via cron) until every file has been reviewed.

Usage:
  python scripts/next_review.py              # Next file + random agent; advance state
  python scripts/next_review.py --prompt-only # Print only the prompt line (for cron)
  python scripts/next_review.py --list        # List all files and current position
  python scripts/next_review.py --reset      # Reset to first file (new pass)

State is stored in .review_queue_state.json.
"""

from pathlib import Path
import json
import random
import sys

# Same agents as random_review_prompt.py
AGENTS = [
    ("Architecture", "Architecture"),
    ("Domain logic", "Domain logic"),
    ("Tag-Type", "Tag-Type"),
    ("Safety/contracts", "Safety/contracts"),
    ("Python practices", "Python practices"),
    ("Naming and lore", "Naming and lore"),
]

# Directories to skip when collecting project .py files
SKIP_DIRS = {
    ".venv", "venv", "env", "env.bak",
    "__pycache__", ".git",
    "node_modules", "instance",
    "DnD",  # nested venv-like folder if present
}
SKIP_PREFIXES = (".",)


def find_repo_root() -> Path:
    """Project root: directory containing Curia and scripts."""
    cur = Path(__file__).resolve().parent
    for _ in range(10):
        if (cur / "Curia").is_dir() and (cur / "scripts").is_dir():
            return cur
        parent = cur.parent
        if parent == cur:
            break
        cur = parent
    return Path(__file__).resolve().parent.parent


def collect_py_files(root: Path) -> list[str]:
    """Return sorted relative paths of project .py files (exclude SKIP_DIRS)."""
    out = []
    for path in root.rglob("*.py"):
        if path.name.startswith(SKIP_PREFIXES):
            continue
        try:
            rel = path.relative_to(root)
        except ValueError:
            continue
        parts = rel.parts
        if any(p in SKIP_DIRS for p in parts):
            continue
        out.append(str(rel).replace("\\", "/"))
    return sorted(out)


def state_path(root: Path) -> Path:
    return root / ".review_queue_state.json"


def load_state(root: Path, file_list: list[str]) -> tuple[int, list[str]]:
    """Return (current_index, file_list). Rebuild file_list if state is stale."""
    path = state_path(root)
    if not path.exists():
        return 0, file_list
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        idx = data.get("index", 0)
        saved_list = data.get("files", [])
        if saved_list != file_list:
            idx = 0
        return idx, file_list
    except (json.JSONDecodeError, OSError):
        return 0, file_list


def save_state(root: Path, index: int, file_list: list[str]) -> None:
    path = state_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"index": index, "files": file_list}, f, indent=2)


def main() -> None:
    root = find_repo_root()
    file_list = collect_py_files(root)

    if "--reset" in sys.argv:
        save_state(root, 0, file_list)
        print("Reset review queue to first file.")
        return

    if "--list" in sys.argv:
        idx, _ = load_state(root, file_list)
        print(f"Total files: {len(file_list)} (next index: {idx})")
        for i, f in enumerate(file_list):
            mark = " <- next" if i == idx else ""
            print(f"  {i+1:4} {f}{mark}")
        return

    if not file_list:
        print("No project .py files found.")
        return

    idx, file_list = load_state(root, file_list)
    total = len(file_list)

    if idx >= total:
        print("All files reviewed in this pass. Starting a new pass.")
        idx = 0
        save_state(root, 0, file_list)

    file_path = file_list[idx]
    agent_name, agent_prompt = random.choice(AGENTS)
    prompt = f"Review {file_path} with the {agent_prompt} agent."

    # Advance state for next run
    next_idx = idx + 1
    save_state(root, next_idx, file_list)

    progress = f"({idx + 1}/{total})"
    if "--prompt-only" in sys.argv:
        print(prompt, end="")
        return

    print(f"File {progress}: {file_path}")
    print(f"Agent: {agent_name}")
    print(f"Paste in your agent chat: {prompt}")
    if next_idx >= total:
        print("(Next run will start a new pass over all files.)")


if __name__ == "__main__":
    main()
