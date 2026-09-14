#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
HOOK_SRC="${ROOT}/scripts/git-hooks"
# Hooks live in the common git dir, which a worktree's .git file points to.
HOOK_DST="$(cd "$(git rev-parse --git-common-dir)" && pwd)/hooks"

for hook in pre-commit pre-push; do
	src="${HOOK_SRC}/${hook}"
	dst="${HOOK_DST}/${hook}"
	if [[ ! -f "${src}" ]]; then
		echo "missing ${src}" >&2
		exit 1
	fi
	cp "${src}" "${dst}"
	chmod +x "${dst}"
	echo "installed ${dst}"
done
