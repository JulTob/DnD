#!/usr/bin/env python3
"""
Validate Shiny app startup and report the first error for the App Run/Watch agent.

Usage:
  python scripts/run_app_catch_errors.py

Exits with 0 if the Shiny app module loads without raising; exits with 1 and
prints a structured error block if an exception occurs. Paste it into an agent
chat to find the source and suggest a fix.
"""

import sys
import traceback
from pathlib import Path

_project_root = Path(__file__).resolve().parent.parent
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

def main() -> int:
    try:
        import shiny_app  # noqa: F401  # validates imports and app construction
        print("Shiny app loaded successfully (shiny_app module + app object).")
        return 0
    except Exception as exc:
        tb = traceback.format_exc()
        lines = tb.strip().split("\n")
        source_block = []
        for i, line in enumerate(lines):
            if "  File " in line and ("app/" in line or "Minion.py" in line or "Atlas" in line or "shiny_app" in line):
                source_block.append(line.strip())
                if i + 1 < len(lines):
                    source_block.append(lines[i + 1].strip())
                break
        print("--- APP ERROR (paste below for App Run/Watch agent) ---")
        print(f"Exception: {type(exc).__name__}: {exc}")
        if source_block:
            print("Relevant source:")
            print("\n".join(source_block))
        print("Full traceback:")
        print(tb)
        print("--- END ---")
        return 1

if __name__ == "__main__":
    sys.exit(main())
