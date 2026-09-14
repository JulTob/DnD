#!/usr/bin/env bash
# Finder and iCloud copy a ref file as "name 2".  Git cannot read a ref whose
# name has a space, and one such file makes every fetch fail with
# "fatal: bad object refs/... 2".
#
# Repair, never loss:
#   - a copy identical to its original is removed;
#   - a copy that points elsewhere is kept under refs/salvage/duplicate-refs/
#     (a local namespace, never pushed), then removed;
#   - a copy that points at no object holds nothing, and is removed.
#
# Run by hand when a fetch fails, or let pre-push run it.
set -euo pipefail

COMMON="$(cd "$(git rev-parse --git-common-dir)" && pwd)"

first_line() {
	head -n 1 "$1" | tr -d '[:space:]'
}

while IFS= read -r -d '' file; do
	rel="${file#"${COMMON}/"}"
	original="${file% [0-9]*}"
	sha="$(first_line "${file}")"

	if [[ -f "${original}" ]] && [[ "$(first_line "${original}")" == "${sha}" ]]; then
		rm -- "${file}"
		echo "repair-refs: removed ${rel} (same as ${original#"${COMMON}/"})"
	elif [[ -n "${sha}" ]] && git cat-file -e "${sha}" 2>/dev/null; then
		salvage="refs/salvage/duplicate-refs/${rel#refs/}"
		salvage="${salvage// /-}"
		if existing="$(git rev-parse --verify --quiet "${salvage}")" && [[ "${existing}" != "${sha}" ]]; then
			salvage="${salvage}-${sha:0:7}"
		fi
		git update-ref "${salvage}" "${sha}"
		rm -- "${file}"
		echo "repair-refs: kept ${rel} as ${salvage}, then removed it"
	else
		rm -- "${file}"
		echo "repair-refs: removed ${rel} (points at no object)"
	fi
done < <(find "${COMMON}/refs" -type f \( -name '* [0-9]' -o -name '* [0-9][0-9]' \) -print0)
