#!/usr/bin/env python3
"""
Run-on-save helper: pick a random review agent and print the prompt to paste in an agent chat.

Usage:
  python scripts/random_review_prompt.py

After saving a file, run this script (e.g. via Run on Save extension or a keybinding).
Then paste the printed line into an agent chat to trigger that review lens.
"""

import random
import sys

# (display name, focus, rule reference for prompt)
AGENTS = [
    ("Architecture", "scalability, modularity, clean interfaces", "Architecture"),
    ("Domain logic", "DnD2024 rules, logic, clarity", "Domain logic"),
    ("Tag-Type", "multi-class scalability, object augmentation, cross-compatibility", "Tag-Type"),
    ("Safety/contracts", "safety, contracts, validity", "Safety/contracts"),
    ("Python practices", "Python best practices", "Python practices"),
    ("Naming and lore", "Atlases, Maps, Lodges, Ledgers, adventurous themes, clear purpose", "Naming and lore"),
]

def main() -> None:
    name, focus, rule_name = random.choice(AGENTS)
    # Prompt that runs this specific agent (so run-on-save uses the script-chosen agent)
    prompt = f"Review the current file with the {rule_name} agent."
    print(f"Agent: {name} ({focus})")
    print(f"Paste in your agent chat: {prompt}")
    if "--prompt-only" in sys.argv:
        print(prompt, end="")

if __name__ == "__main__":
    main()
