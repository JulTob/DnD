# Dialog 0004 — Evaluate the Minions

- **Question (Q-0007):** What are the Minions, are they sound, and where should they go — kept as-is, evolved into a Log System, and/or made to report errors when deployed?
- **Raised by:** Julio (arbiter)
- **Consuls called:** Full council — Bard, Cleric, Warlock, Paladin, Wizard, Sorcerer, Monk, Artificer, Ranger, Rogue
- **Status:** 🟢 converged — awaiting Julio's arbitration
- **Related:** `Minion.py`; Canon Code-Style (self-tests); QST-0009 (fallback shim swallows errors)

---

## 🧭 Framing
Julio values the Minions: the **personalized bug trees**, the sense of *keeping tabs*, the minimalist record-keeping. He knows they're not optimized, and wonders whether they should migrate to a **Log System** or become **deployment error reporting**. The council evaluates *everything* about them.

**What they are (from `Minion.py`):** five decorators that wrap a function and feed a "log system" — the **console** (ANSI-colored, emoji minions) by default, or a **plain-text file** if `set_log_file()` is called. They render two emoji trees: a **bug tree** (`bugged_tree`, the exception path) and a **call tree** (`get_call_tree`, via `inspect.stack`). Roster: `@minion` (log ok/fail + bug tree, re-raise), `@watcher` (log; on fail an enriched `file:line`, re-raise), `@spy` (log the call tree on *every* call), `@warden` (on fail, retry once, same args), `@guardian` (retry ≤100×, same args). None change the **return value**.

---

## 🗣️ Deliberation

Understanding Consul (Bard): First, name what they are — a *themed aspect layer* over functions. But two different jobs are tangled inside one toolkit: **observing** (`minion`/`watcher`/`spy`) and **retrying** (`warden`/`guardian`). Keeping tabs and self-healing are different concerns; we should think of them separately even if they share the theme.

Repair Consul (Cleric): Whatever we do, keep the trees. `bugged_tree` gives the innermost project frame at a glance — it's the single most useful thing here for diagnosing a real fault. That formatter is an asset; preserve it.

Contracts Consul (Warlock): A precision point: the docstrings promise "does not change the return value" — true — but `warden`/`guardian` **change behavior** (they retry). That's a real contract change wearing an observability skin. A reader slapping `@guardian` on may not expect 100 silent re-runs. Split resilience from logging and state each one's contract plainly.

Safety Consul (Paladin): And retry is *dangerous by default*. `@guardian` re-runs the **same args** up to 100×; on a non-idempotent op (a write, a network call, a seed mutation) that repeats side effects and can mask a real failure as a hang. `@warden` retries once on *any* `Exception`, same hazard. Rule: only retry idempotent work, cap it, never swallow.

Methods Consul (Wizard): Performance. `@spy` calls `inspect.stack()` on **every** invocation, and `get_call_tree` walks the whole stack — `inspect.stack()` is famously slow. Our generation paths are heavily decorated; that's real overhead per call.

Flow Consul (Sorcerer): Compounded by concurrency — the log target is a **global** `_log_path` with `print`, not thread-safe. Under Shiny's concurrent sessions, interleaved writes and shared global state will bite. Dev-grade as written.

Simplicity Consul (Monk): Here's the elegant resolution: Python already *has* logging — levels, handlers, formatters, rotation. Don't reinvent the infrastructure. Keep the **personality** (the decorator vocabulary, the trees) but re-back it onto stdlib `logging`: the bug tree becomes a custom `Formatter`, the minions emit records to a logger. Julio's flavor on a real backbone. No new framework, no new dependency.

Workshop Consul (Artificer): That's exactly what deployment needs. In prod: a rotating **file handler**, real **levels**, and optionally an **error-report handler** (a file sink now; an HTTP/Sentry-style one later). In dev: the colored console we love. Same Minions, different handlers per environment — that's the migration path to "report errors when deployed."

Ecosystem Consul (Ranger): Lean on stdlib `logging` — zero dependency. Only weigh an external error-reporting service *later*, as a deliberate dependency; not now.

Testing Consul (Rogue): `Minion.py` already ends in an `if __name__ == "__main__"` demo — it's the self-test pattern the Canon now mandates. Formalize it: assert each decorator preserves return values, and that retries do what they claim.

Monk (closing): Keep the surface — `@minion/@watcher/@spy/@warden/@guardian` is a lovely vocabulary. Re-back it; don't grow it. No objection remains.

---

## ✅ Convergence check
- [x] Every called Consul has spoken.
- [x] Objections addressed (retry-vs-observe split; performance of `inspect.stack`; global-state under Shiny).
- [x] A concrete direction with tradeoffs is on the table.

---

## 🕊️ Vox report

Vox: Report on **Q-0007 — the Minions.**

**Common ground (unanimous):**
- **Keep the Minions.** The bug/call trees and the decorator vocabulary are genuinely valuable and worth preserving — this is the project's charm *and* a real diagnostic tool.
- **Two jobs are tangled:** observability (`minion`/`watcher`/`spy`) vs. resilience/retry (`warden`/`guardian`). Split them conceptually; document each contract (retry *is* a behavior change).
- **Re-back the backbone onto stdlib `logging`** — levels, handlers, formatters — instead of `print` + a global `_log_path`. The bug tree becomes a custom `Formatter`. Zero new dependency.
- **Caveats to fix:** `inspect.stack()` in `@spy` is dev-grade (keep off hot paths / make call-tree capture opt-in); global mutable log target isn't safe under concurrent Shiny; `@warden`/`@guardian` retries are only safe on idempotent ops and must be capped and never silent.

**Options & tradeoffs (where the Minions go):**
1. **Re-back on stdlib `logging`, keep the Minion skin** *(council's lead).* Same decorators; they emit to a logger; trees become a Formatter; environment picks handlers (colored console in dev; rotating file + optional error-report in prod). *Pro:* keeps the flavor, gains real infra + deployment error reporting, no dependency. *Con:* a focused refactor of `Minion.py`.
2. **Grow a first-class Log System** (a "Chronicle"/"Ledger" in its own Atlas) that the Minions feed. *Pro:* observability becomes a real domain with a home. *Con:* more surface — risks the exact bloat we just fought (Monk wary).
3. **Keep as-is for now**, defer. *Pro:* zero work. *Con:* won't survive production; the print/global-state fragility remains under Shiny.

**Synthesis:**
- **Leading recommendation:** Option **1** — re-back the Minions on stdlib `logging`, split observe-vs-retry, keep the trees as a Formatter, and add a production handler for deployed error reporting. Smallest change that keeps their soul and gains the infrastructure.
- **Strongest alternative:** Option **2**, if you'd like observability to become a first-class "Chronicle" domain worth its own Atlas.

→ **Awaiting Julio's decision.** Your arbitration becomes **Decree 0003**.
