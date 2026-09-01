#!/usr/bin/env bash
# Rolling safepoint — one safebox ref, not constant autosave (Decree 0008).
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

HEAD_SHA="$(git rev-parse HEAD)"
STAMP="$(date +%Y%m%d-%H%M%S)"

git tag -f safepoint/latest "$HEAD_SHA"
git tag "safepoint/${STAMP}" "$HEAD_SHA"

mkdir -p .safepoint
printf '%s\n' "$HEAD_SHA" > .safepoint/ref
printf '%s\n' "$STAMP" > .safepoint/stamp

# Stash snapshot ref (does not require clean tree)
STASH_REF="$(git stash create "safepoint-${STAMP}" 2>/dev/null || true)"
if [[ -n "${STASH_REF}" ]]; then
	printf '%s\n' "$STASH_REF" > .safepoint/stash-ref
fi

echo "safepoint/latest -> ${HEAD_SHA} (${STAMP})"
if [[ -n "${STASH_REF:-}" ]]; then
	echo "stash snapshot: ${STASH_REF}"
fi
