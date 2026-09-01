#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
HOOK_SRC="${ROOT}/scripts/git-hooks"
HOOK_DST="${ROOT}/.git/hooks"

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
