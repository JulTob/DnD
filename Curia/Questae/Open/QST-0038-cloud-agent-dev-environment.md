# QST-0038 — A reproducible Cloud Agent / bare-Linux dev environment

- **Type:** chore/cleanup
- **Priority:** 🟠 high
- **Status:** Open — diagnosis only; execution awaiting Julio's go/no-go
- **Owner:** unclaimed
- **Route to:** Workshop Consul (Artificer), Ecosystem Consul (Ranger), Safety Consul (Paladin)
- **Parent:** —
- **Sidequests:** —
- **Related:** Decree 0001 (venv arbitration) · QST-0004 (unify venvs) · QST-0003 (Flask→Shiny) · QST-0016.6 (reproducibility rites)

> **Numbering note for Julio:** the Curia board sequence sits at QST-0037, but
> `Documenta/Questae` already uses QST-0064 / Decree 0006. This ticket takes the
> next Curia-board id (0038); renumber if the tracks should be reconciled.

---

## 🔍 Diagnosis (what & where)
There is no declared, reproducible definition of the development environment for
a fresh Linux machine (a Cloud Agent VM, CI runner, or a bare clone). Today the
environment is reconstructed by hand or by scripts that assume a developer's Mac:

- **No `.cursor/environment.json`** (nor any equivalent manifest) exists, so a
  Cloud Agent has nothing to build from on boot.
- The common Linux base image ships **`python3.12` without the `venv`/`ensurepip`
  module**, so `python3 -m venv .venv` fails out of the box until a system
  package is installed.
- `run_shiny.sh` probes newest→oldest Python and assumes macOS/Homebrew
  (`/opt/homebrew/...`); `Run_And_Deploy.sh` still `source adventurer/bin/activate`
  and exports `FLASK_ENV` — the retired Flask path (QST-0003), not `shiny run`.
- The project **targets the newest stable Python (3.14)** — `.python-version`,
  `app.yaml`, and the `QST-0004` standing preference (Decree 0001 defers the
  actual version to Julio; it is not yet ratified law) — but a bare Linux base
  provides only 3.12, and there is no ruling on how Linux should obtain 3.14 (or
  whether a documented notch-back is acceptable there). See QST-0039.

## 🧾 Evidence
- Fresh `python3 -m venv .venv` on Ubuntu 24.04 base:
  `ensurepip is not available ... apt install python3.12-venv`.
- `.python-version` = `3.14`; `app.yaml` = `runtime: python314` — the canonical
  target is 3.14, confirming the mismatch with a 3.12-only Linux image.
- `Run_And_Deploy.sh` lines 4–6 activate `adventurer/` and set `FLASK_ENV`.
- QST-0004 Ranger note: "Newest Python is fine *if* Shiny + numpy already ship
  3.14 wheels ... else we pin one notch back." — the same trade-off recurs here.

## 🎯 Desired outcome
A single, Canon-aligned way to stand up the app on a fresh Linux box that:
- builds **one root `.venv`** from `requirements.txt` (per Decree 0001), and
- boots the Shiny app (`shiny run shiny_app.py`) with no manual steps,
with the **Python-version approach decided by Julio**, not chosen silently.

## 🧭 Notes for the Agora / implementer
This needs a Dialog before anything lands. Open questions for Julio:
1. **Python on Linux.** Provision 3.14 (e.g. a `python:3.14-slim` Docker base, or
   `uv`/`pyenv`/deadsnakes), or accept a **documented notch-back to 3.12** on the
   cloud VM while the Mac stays 3.14? (Ranger already opened this door in QST-0004.)
2. **Where the manifest lives.** In-repo `.cursor/environment.json` (versioned,
   follows branches/PRs) vs. a dashboard-managed environment (no committed file)?
   Precedence: a committed file wins over dashboard config.
3. **Scope discipline.** Keep this strictly the *environment manifest*; do **not**
   fold in the stale `Run_And_Deploy.sh`/`adventurer` cleanup — that is QST-0003.

**Do not** commit any venv (QST-0004 / `.gitignore`), and **do not** pin a
Python older than the Canon preference without a recorded decision here.

> **Field note (2026-08-29):** a draft `.cursor/environment.json` + `.cursor/install.sh`
> were built and verified end-to-end (fresh `.venv`, deps installed, `shiny run`
> serving HTTP 200, NPC generation working) on a 3.12 VM, opened as a **draft PR
> for review only**. It is a proposal to show, not a landed decision — it awaits
> the rulings above before it may merge, and must move to 3.14 if Julio so rules.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
*Routed to the same lens as QST-0004; they refine the road, they do not pave it.*

> Workshop Consul (Artificer): A repo-versioned manifest that rebuilds one root
> `.venv` from `requirements.txt` is the honest workshop — the same shape Decree
> 0001 already blessed, now made runnable on Linux. The only real question is the
> interpreter, and that is Julio's to rule.
> Ecosystem Consul (Ranger): I favour a `python:3.14-slim` base so Linux and the
> Mac speak the same interpreter; if a wheel in `requirements.txt` lacks 3.14
> support we pin one notch back — but that notch is a *recorded* decision, never a
> silent default like the 3.12 the base image happened to hand us.
> Safety Consul (Paladin): Fail-fast at the boundary — the manifest must error
> loudly if the interpreter or a dependency is missing, never boot on a shadow
> environment (Decree 0003 spirit). And no secret, no venv, ever enters the tree.

**Weighting:** reach 2 × severity 2 = **4** · council leaning: `needs a Dialog`
*(Reach: touches how every Linux contributor and agent boots the app. Severity:
correctness of the run environment + Canon alignment, not cosmetic.)*
