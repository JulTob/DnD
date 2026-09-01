#!/usr/bin/env bash
# Cursor agent guard — dangerous Git verbs (Decree 0008).
set -euo pipefail

input="$(cat)"
command="$(python3 -c "import json,sys; print(json.load(sys.stdin).get('command',''))" <<<"${input}")"

deny() {
	local msg="$1"
	python3 -c "import json,sys; print(json.dumps({'permission':'deny','user_message':sys.argv[1],'agent_message':'Blocked by Decree 0008 safety hook.'}))" "$msg"
	exit 0
}

if [[ "${command}" =~ git[[:space:]]+branch[[:space:]]+-f[[:space:]]+main ]]; then
	deny "git branch -f main is forbidden. Use a questa branch and fast-forward merge."
fi

if [[ "${command}" =~ git[[:space:]]+reset[[:space:]]+--hard ]]; then
	deny "git reset --hard requires make safepoint first, then Julio's approval."
fi

if [[ "${command}" =~ git[[:space:]]+add[[:space:]]+-A ]]; then
	deny "git add -A is forbidden. Stage paths explicitly."
fi

if [[ "${command}" =~ git[[:space:]]+add[[:space:]]+\.$ ]]; then
	deny "git add . is forbidden. Stage paths explicitly."
fi

if [[ "${command}" =~ git[[:space:]]+push ]] && [[ "${command}" =~ --force ]] && [[ "${command}" =~ main ]]; then
	if [[ "${command}" =~ ALLOW_FORCE_MAIN=1 ]]; then
		python3 -c "print('{\"permission\":\"allow\"}')"
		exit 0
	fi
	deny "Force-push to main is forbidden without archive tag + ALLOW_FORCE_MAIN=1."
fi

python3 -c "print('{\"permission\":\"allow\"}')"
