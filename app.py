#!/usr/bin/env python3
"""Run the Gen Legend app (Shiny). Usage: python app.py or shiny run shiny_app.py"""
import os
import subprocess
import sys

def main():
    port = int(os.environ.get("PORT", 8080))
    script_dir = os.path.dirname(os.path.abspath(__file__))
    shiny_app = os.path.join(script_dir, "shiny_app.py")
    if not os.path.isfile(shiny_app):
        print("shiny_app.py not found.", file=sys.stderr)
        sys.exit(1)
    # Run: shiny run --port N shiny_app.py (no --reload by default for prod)
    reload = os.environ.get("SHINY_RELOAD", "").lower() in ("1", "true", "yes")
    cmd = [sys.executable, "-m", "shiny", "run", "--port", str(port), shiny_app]
    if reload:
        cmd.insert(-1, "--reload")
    os.chdir(script_dir)
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()
