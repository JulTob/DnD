#!/usr/bin/env python3
"""Flag truncated .py source before commit (QST-0052 / Decree 0008)."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def _run(*args: str) -> str:
	result = subprocess.run(args, capture_output=True, text=True, check=False)
	if result.returncode not in (0, 1):
		raise RuntimeError(result.stderr or result.stdout)
	return result.stdout


def staged_py_files() -> list[Path]:
	out = _run("git", "diff", "--cached", "--name-only", "--diff-filter=ACM")
	root = Path(_run("git", "rev-parse", "--show-toplevel").strip())
	return [root / line for line in out.splitlines() if line.endswith(".py")]


def head_size(path: Path) -> int | None:
	rel = path.as_posix()
	try:
		out = _run("git", "show", f"HEAD:{rel}")
	except RuntimeError:
		return None
	return len(out.encode("utf-8"))


def pyc_size(path: Path) -> int | None:
	pyc = path.with_suffix(".pyc")
	if not pyc.is_file():
		cache = path.parent / "__pycache__" / f"{path.stem}.cpython-*.pyc"
		matches = list(path.parent.glob(f"__pycache__/{path.stem}.cpython-*.pyc"))
		if not matches:
			return None
		pyc = matches[0]
	return pyc.stat().st_size if pyc.is_file() else None


def check_file(path: Path) -> list[str]:
	issues: list[str] = []
	if not path.is_file():
		return issues
	current = path.read_bytes()
	cur_len = len(current)
	if cur_len == 0:
		issues.append(f"{path}: empty file staged")
		return issues
	old_len = head_size(path)
	if old_len is not None and old_len > 200 and cur_len < old_len * 0.2:
		issues.append(
			f"{path}: shrank {old_len} -> {cur_len} bytes (>80% loss vs HEAD)"
		)
	if cur_len < 80:
		pyc_len = pyc_size(path)
		if pyc_len is not None and pyc_len > max(cur_len * 4, 400):
			issues.append(
				f"{path}: tiny source ({cur_len} B) with large .pyc ({pyc_len} B)"
			)
	return issues


def main() -> int:
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"--staged",
		action="store_true",
		help="Only inspect staged Python files (pre-commit mode).",
	)
	_ = parser.parse_args()
	paths = staged_py_files()
	if not paths:
		return 0
	all_issues: list[str] = []
	for path in paths:
		all_issues.extend(check_file(path))
	if all_issues:
		print("loss_detector: possible silent truncation:", file=sys.stderr)
		for line in all_issues:
			print(f"  {line}", file=sys.stderr)
		return 1
	return 0


if __name__ == "__main__":
	sys.exit(main())
