# Decree 0003 — The Minions, re-backed on one logging pipeline

- **Ratified by:** Julio, 2026-07-02
- **Source:** Dialog 0004 (Q-0007)
- **Status:** active

## Decision

**Keep the Minions** — the `@minion / @watcher / @spy / @warden / @guardian` vocabulary and the emoji **bug/call trees** stay; they are both the project's charm and a real diagnostic tool.

**Re-back them onto Python's stdlib `logging` — one pipeline, different coats.** The Minions stop calling `print` and instead emit **log records**. The bug tree becomes a custom `Formatter`. What changes between environments is only *which handlers are attached*:
- **Local / testing:** a single colored **console** handler (pure stdlib) — the pretty trees, nothing else to set up.
- **Deployed web app:** the "logging system" — a rotating **file** handler plus an **error-report** sink — attached at startup.

*Same use, different behavior under the hood.* It is **one** logging pipeline with swappable handlers — **not** two parallel systems (that would recreate the duplication we just cleared).

**Split the two tangled jobs (and document their contracts):**
- **Observability** — `minion` / `watcher` / `spy` — log only; never change behavior.
- **Resilience / retry** — `warden` / `guardian` — these **do** change behavior (they retry); say so plainly. Retry only **idempotent** operations, cap attempts, and never fail silently.

**Fix the dev-grade caveats:**
- `@spy` / `inspect.stack()` is expensive — keep it off hot paths; make call-tree capture opt-in / lazy.
- No global mutable log target — configure logging once at startup so it's safe under Shiny's concurrent sessions.
- Minion self-tests live in `Minion.py`'s `if __name__ == "__main__"` block (Canon: module self-tests).

## Reasoning
The council was unanimous that the Minions must survive. Stdlib `logging` gives real levels, handlers, and formatters with zero new dependency; feeding the Minions into it keeps their personality while gaining production-grade infrastructure and deployed error reporting. Julio's "implement both" resolves cleanly as **one backbone, two handler configurations** — elegant, and free of the parallel-system bloat the Monk warned against.

## Alternatives not chosen
- **Two parallel logging systems** — rejected as duplication.
- **A first-class "Chronicle" Log-System Atlas** — good, but more surface than needed now; the handler-config can live modestly. Revisit only if observability grows into its own domain.
- **Keep as-is** — won't survive production; global-state + `print` are unsafe under concurrent Shiny.

## Consequences
- Implementation work is **not yet opened as quests** (to avoid unrequested dominoes). When Julio is ready, this Decree spawns: refactor `Minion.py` onto `logging`; bug-tree `Formatter`; per-environment handler setup; the observe/retry split + contracts; `__main__` self-tests.
- Ties to QST-0009 (the fallback shim that swallows errors) — the same "never fail silently" principle applies.
