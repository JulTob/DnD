# QST-0034 — Surface Minion's dev log while the web app runs

- **Type:** design
- **Priority:** 🟢 low
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Workshop Consul (Artificer), Repair Consul (Cleric), Flow Consul (Sorcerer), Safety Consul (Paladin)
- **Parent:** QST-0030 (Minion bug-report quality)
- **Sidequests:** —
- **Related:** Decree 0003 (Minions on logging), QST-0030.3 (call-tree visibility)

---

## 🔍 Diagnosis (what & where)
Minion's verbose guardian + spy logs are a deliberate developer aid, but Shiny runs server-side — `print`/Minion output goes only to the terminal that launched the app (`./run_shiny.sh` or `make run`). During live development there is no in-browser view of which call raised an issue and where.

## 🧾 Evidence
- Parked scope (formerly `GENLEGEND_TICKETS.md` TICKET-02): developers want the Minion trace — including raising location — visible while generating characters in the browser, not only in the terminal.
- Decree 0003 established Minions as the logging spine; QST-0030 addresses report *quality* — this quest addresses report *visibility in dev*.

## 🎯 Desired outcome
In **dev mode only**, generating a character that hits a problem shows the Minion trace and the raising location in the browser, not just the terminal. **Done when:** a dev can diagnose a generation failure without switching to the terminal.

## 🧭 Notes for the Agora / implementer
Options to weigh (not pre-chosen):
- **Logfile + dev panel** — Minion also writes to `logs/genlegend.log`; in `DEV=1`, a collapsible panel tails the last N lines (polled reactive). ANSI→HTML for colours.
- **`/logs` endpoint** — dev-only route streaming recent records; floating overlay subscribes.
- **Structured capture** — guardian/spy records carry `where` (module + function + line) and severity for filtering.

**Caveat:** dev-only. Never ship the log panel or endpoint to production.

---

## ✅ Resolution
*(pending)*

---

## 🏛️ Council
> Repair Consul (Cleric): The Chronicler already captures errors — the gap is surfacing them where Julio is looking during a live run.
> Safety Consul (Paladin): Dev-only is non-negotiable; no log stream in production.
> Workshop Consul (Artificer): Prefer the logfile + panel path first — smallest surface, reuses Decree 0003's file logging story.

**Weighting:** reach 1 × severity 1 = **1** · council leaning: `defer` (post-v1 dev ergonomics)
