# QST-0070 — Background workflows die on session limits and report success

- **Type:** bug
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Consul-Lorekeeper, Consul-Artificer
- **Parent:** —
- **Sidequests:** —
- **Related:** QST-0058 (minion recovery on precondition failure)

---

## 🔍 Diagnosis (what & where)

Three multi-agent background workflows were launched during the naming-safeguards
session. **All three returned a clean, successful-looking result while every one
of their agents had failed.**

| run | agents | done | errored | returned |
|---|---|---|---|---|
| `wf_29db6554-7d3` naming audit | 5 | 0 | 5 | `{"confirmed_count":0,"confirmed":[]}` |
| `wf_5d434323-0aa` naming audit, re-run | 5 | 0 | 5 | `{"confirmed_count":0,"confirmed":[]}` |
| `wf_44958c38-66d` Psi Warrior design | 8 | 0 | 8 | `{"directions":[],"verdicts":[],...}` |

The failure modes reported were `You've hit your session limit` (11 agents) and
`Your computer went to sleep mid-response` (2 agents).

The defect is **not** that agents can fail. It is that a total failure is
indistinguishable from a clean pass at the point where the result is read. The
scripts follow the documented pattern `(await parallel(...)).filter(Boolean)`,
and a dead agent resolves to `null`, so `filter(Boolean)` silently discards it.
An audit that found nothing and an audit that never ran return the same value.

This is the same shape as QST-0058 and as the `@guardian` defect fixed in
`Minion.py` this session: **a recovery path that erases the distinction between
"no problem" and "never checked".** The naming ladder was built precisely to
report every demotion rather than absorb it; the workflow layer above it does
the opposite.

## 🧾 Evidence

Task notification for `wf_5d434323-0aa`:

```
<result>{"confirmed_count":0,"confirmed":[]}</result>
<failures>
[find:silent]       failed: API Error: Your computer went to sleep mid-response.
[find:contract]     failed: API Error: Your computer went to sleep mid-response.
[find:deadcode]     failed: You've hit your session limit · resets 8am
[find:output]       failed: You've hit your session limit · resets 8am
[find:determinism]  failed: You've hit your session limit · resets 8am
</failures>
<usage>agents 5 · done 0 · error 5 · subagent_tokens 739433 · tool_uses 370</usage>
```

739k subagent tokens and 370 tool calls were spent, and the reported answer was
"nothing found". The failures are present in the notification envelope but not
in the value the script returns, so any consumer reading only the result is
misled. Two of the three runs were also reported to the user before the
distinction was noticed.

## 🎯 Desired outcome

A workflow cannot report an empty success when its agents did not run.

1. A script can tell a `null` that means "this agent answered nothing" from a
   `null` that means "this agent died". Today both are `null`.
2. The returned value carries the run's health: how many agents were asked, how
   many answered, how many died and why.
3. A run whose agents all failed is a **failed run**, not an empty one.
4. Whatever the fix, it should be expressible as a house pattern the scripts in
   `workflows/scripts/` can all adopt, not a fix in one script.

## 🧭 Notes for the Agora / implementer

- Do **not** solve this by retrying. A session limit is deterministic until it
  resets, and retrying it is the `@guardian` mistake: a hundred replays of a
  failure that never had a second outcome. See the `@changeling` note in
  `Minion.py`. If anything retries, it must first establish the failure is
  transient.
- The two causes are different and deserve different answers. `session limit`
  is a resource ceiling and is knowable in advance; `computer went to sleep` is
  an interruption and may be genuinely resumable via `resumeFromRunId`.
- Cost matters here: the three runs together spent over a million subagent
  tokens to return nothing. A cheap pre-flight check would have been worth it.
- Consider whether the Minion doctrine applies to the workflow layer at all, or
  whether this is a harness concern the project can only work around. If it is
  the latter, the deliverable is a documented house pattern plus a note in
  `Canon/Minions-Guide.md`, not code.
- **Open a Dialog** if the answer is "the project should stop using background
  workflows", because that is a decision about how work gets done, not a bug fix.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Moved to Solved:** —

---

## ⚗️ Reward (separate dialog — do not fill during implementation)

> *This section is filled in a later conversation with Julio, after the quest is in `Solved/`.*

- **Reward file:** *(pending distillation dialog)*
- **Distilled:** *(pending)*

---

## 🏛️ Council
*Pending. Routed to Consul-Lorekeeper (does this belong to Minion doctrine?) and
Consul-Artificer (what can actually be built against the harness?).*
