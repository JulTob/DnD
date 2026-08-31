# Status: 🟢 verified by an independent review agent (2026-08-29) — awaiting Julio's ⚪️ confirmation.
# Base image for the DnD Shiny toolkit: the project's canonical Python (3.14),
# so the cloud/Linux environment and the developer's Mac run one interpreter.
FROM python:3.14-slim

# git           — installs the pinned `tagkit` dependency from GitHub.
# build-essential — fallback compiler for any dependency lacking a 3.14 wheel.
# ubuntu (uid 1000) — matches the workspace owner so the checkout stays writable.
RUN apt-get update \
    && apt-get install -y --no-install-recommends git build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --uid 1000 ubuntu

USER ubuntu
