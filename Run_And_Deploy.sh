#!/usr/bin/env bash
set -euo pipefail

source adventurer/bin/activate
export FLASK_ENV=development

python app.py || status=$?
status=${status:-$?}
if [ "$status" = "130" ]; then
    # 130 = SIGINT (Ctrl+C)
    gcloud run deploy gen-legends --source . --region us-central1 --allow-unauthenticated
elif [ "$status" = "0" ]; then
    echo "Exited normally (exit $status). Deploying:" >&2
	gcloud run deploy gen-legends --source . --region us-central1 --allow-unauthenticated
else
    echo "Skipping deploy (exit $status)" >&2
fi
