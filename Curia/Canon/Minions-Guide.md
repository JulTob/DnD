# 🧞 The Minions — a Guide for the Curia

> *A companion to `Minion.py`. What the Minions are, when to summon each, and how to keep them useful without letting them become noise. Living reference — it evolves with Decree 0003 (Minions on one `logging` pipeline).*

## What a Minion is
A **Minion** is a decorator you place on a function. It **watches** that function and reports to the log — success, failure, or the path that led there. A Minion **never changes the function's return value**; it only observes. (Two of them, `@warden`/`@guardian`, *do* change behaviour by retrying — see the caution below.)

They exist because a generator that summons characters from seeds produces a lot of small steps, and when something breaks you want the *innermost* cause, drawn as a readable tree — not a wall of framework traceback.

## The roster — when to summon which

| Minion | Summon it on… | What it does |
|--------|---------------|--------------|
| `@minion` | entry points / main flows | logs the result; on failure prints the **bug tree**, then re-raises |
| `@watcher` | I/O, handlers, boundaries | logs the result; on failure prints an enriched `file:line` locator, then re-raises |
| `@spy` | dispatch / "who called this?" | logs the **call tree** (chain of command) on every call |
| `@warden` | flaky *idempotent* work | on failure, retries **once** with the same args |
| `@guardian` | critical *idempotent* work | retries (same args) until success or 100 attempts |

**One Minion per meaningful boundary — not on every function.** Decorate the entry points and the I/O edges; leave the small pure helpers bare. A Minion on everything is just noise.

## The Chronicler (`×N` + deferred errors)
During one generation you'll call the same helpers many times. Put **`@chronicler`** on the top-level job (the summon) and the log stays readable — the little Minions report *into the Chronicler's account* instead of straight to the screen:

```python
from Minion import chronicler

@chronicler                 # one creation = one account
def summon_character(...):
    ...
```

While a Chronicler is open:
- the **first** time a line appears, it prints live;
- **repeats collapse** — reported once at the end as a quiet `… ×7` under a separator;
- **errors are held back** to a closing section, each bug tree under its own separator.

The little Minions don't need to know any of this — they just report; the Chronicler owns the gathering and the flush. A nested `@chronicler` joins the outermost account (only it opens and closes), so batches (e.g. 5 NPCs) collapse as one. Outside any Chronicler, Minions behave exactly as before (immediate output). The summon entry points in `shiny_app.py` already carry `@chronicler`.

## Benefits
- **Signal over noise** — the one thing that changed or broke stands out.
- **Root cause, fast** — the bug tree points at the innermost project frame (the real culprit), not the Minion wrapper.
- **Zero intrusion** — return values are untouched; you can add or remove a Minion freely.
- **Same tool, dev and prod** — see below.

## Good practices
- **Retry only idempotent work.** `@warden`/`@guardian` re-run with the *same args*; on a write, a network call, or anything with side effects, that repeats the effect. Never use them to paper over a real bug, and never let them fail silently.
- **Keep `@spy` off hot paths.** It walks the stack on every call (`inspect.stack()` is slow). Great for a dispatcher; wrong for a per-roll helper.
- **Errors are yellow (`FAIL_COLOR`).** That's how a session tells an error from a normal line and routes it to the closing section — don't reuse that colour for non-errors.
- **Self-test in `__main__`.** `Minion.py` ends with a runnable demo (`python Minion.py`) that doubles as documentation — per the Canon's module self-test rule.
- **File vs console.** `set_log_file("path.log")` sends records to a file; unset (default) prints to the coloured console.

## Deployment — where the errors go online
The app deploys to Google Cloud (`gcloud run deploy`). Anything written to **stdout/stderr is captured by Google Cloud Logging** — so in production the Minions just write to stdout, and you read errors in the **GCP Console → Logs Explorer** (filter severity = ERROR), or `gcloud run services logs read`, and can set a **log-based alert** to email you when one fires. Local dev keeps the coloured console. (This is the "one pipeline, two coats" of Decree 0003.)

## The road ahead (Decree 0003)
The Minions will be **re-backed onto Python's stdlib `logging`** — same decorators and trees, but emitting real log records so handlers differ by environment (coloured console locally; rotating file + error-report in prod). The bug tree becomes a `Formatter`; this session's `×N`/defer logic becomes a `Filter`. When that lands, this guide updates; the *usage* above stays the same.
