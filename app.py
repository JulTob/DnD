#!/usr/bin/env python3
"""Run the Gen Legend app (Shiny). Usage: python app.py or make run"""
import os
import subprocess
import sys


def main():
    port = int(os.environ.get("PORT", 8080))
    script_dir = os.path.dirname(os.path.abspath(__file__))
    reload = os.environ.get("SHINY_RELOAD", "").lower() in ("1", "true", "yes")
    cmd = [
            sys.executable,
            "-m",
            "shiny",
            "run",
            "--port",
            str(port),
            "app.main:app",
            ]
    if reload:
        cmd.insert(-1, "--reload")
    os.chdir(script_dir)
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
