# QST-0079 — Generation recovers, and its Minions report to a log

- **Type:** bug / robustness
- **Priority:** 🔴 urgent (beta path, reported live by Julio)
- **Status:** Solved
- **Owner:** Claude
- **Route to:** Workshop, Minions
- **Parent:** QST-0072
- **Sidequests:** QST-0080
- **Related:** QST-0030 · Decree 0006

---

## 🔍 Diagnosis (what & where)

Julio's shareable URL `#/2/Orc/Exorcist/Monk/Open%20Hand/She/43215` died with
the bare ceiling message "Unable to summon a Player Character after five
attempts". Three defects stacked:

1. `Training/Monk.py` and `Training/Ranger.py` used `random.choice` without
   importing `random` (their sibling `Barbarian.py` imports it): every Monk
   and every random-subclass Ranger at subclass levels died with `NameError`.
2. `Grimoire_of_Skills.activate_expertise` drew `random.choice(skill_names)`
   before its empty-list guard, so the recursion's natural end (n=0, empty
   list) raised `IndexError` instead of returning. Deft Explorer feeds it a
   one-item list, making every Ranger level 3+ crash.
3. The five-attempt ceiling hid the real error, and the Minion reports only
   scrolled by on the console.

## 🎯 Desired outcome (Julio, in chat, 2026-08-31)

Generation recovers and tries a different path when failure happens; Minion
reports are saved to a plain-text log file, as the project always intended.

---

## ✅ Resolution

- **Decided by:** Julio's direction, 2026-08-31
- **What changed:**
  - `import random` restored in `Training/Monk.py` and `Training/Ranger.py`
    (matching the Barbarian idiom); Monk verified at levels 3/5/11 and
    Elements 4, Ranger at 3/7/12, Rogue at 6.
  - `activate_expertise` gained the same early bail-out its sibling
    `activate_proficiencies` always had. `Grimoire_of_Skills` is a Codex-lane
    foundation: flagged for Codex review at merge.
  - The retry loop already tries different paths (each retry advances the
    seed; `STRICT_GENERATION=1` keeps the first error for harnesses). Its
    exhaustion message now carries the underlying cause, so a deterministic
    bug names itself instead of hiding behind five identical walls.
  - Minion's surviving file sink (`MINION_LOG` / `set_log_file`, plain text)
    is now enabled by `scripts/run_shiny_preview.sh`, defaulting to
    `minion_app.log` in the repo root (already gitignored). Verified: 1,126
    report lines captured from live generations.
- **Practice/preference to remember:** a retry ceiling must quote its last
  cause; five silent failures are a diagnosis withheld. And when a fix
  mirrors a sibling function, say so in the comment: the sibling is the
  argument.

---

## 🏛️ Council

> Workshop Consul (Artificer): The guard belongs before the draw, as the
> sibling always knew. And the Changeling's law from the naming ladder holds
> here too: against a seeded wall, the only recovery is to ask differently.

**Weighting:** reach 3 × severity 3 = **9** · council leaning: `build`
