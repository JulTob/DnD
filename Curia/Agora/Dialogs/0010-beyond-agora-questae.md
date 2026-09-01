# Dialog 0010 — What Agora + Questae cannot recover, and what sits outside them

- **Question:** After two days of recovery, which failures can the Agora and Questae not catch, and what standing tools (Git, hooks, ignore rules, one module home) should exist *beside* the Curia?
- **Raised by:** Julio (via Grok, 2026-08-31 18:15) — "Suggest solutions and diagnose problems beyond recovery by the Agora+Questa system."
- **Related Questae:** QST-0052 · QST-0072 · QST-0081 · QST-0082 · REW-0001 · Dialog 0009
- **Consuls called:** Safety (Paladin), Architecture (Druid), Workshop (Artificer), Methods (Wizard), Simplicity (Monk), Lorekeeper, Testing (Rogue)
- **Status:** 🟡 open — awaiting Julio's decision

---

## 🧭 Framing

Dialog 0009 named the 08-29 accident and minted QST-0052's seven guards.
Those guards are **still Open**. The Curia recorded the truth; it did not
install it. This Dialog is not another file-by-file restore. It is the
layer the quest log cannot be: process that runs when no agent is in the
chat.

Out of scope: which Alusoris tree is canonical (QST-0081.5), Domain openings
(QST-0080.1), TagKit pin migration (QST-0051).

---

## 🗣️ Deliberation

Safety Consul (Paladin): The Curia is an honor system. It did not stop
`git branch -f` on `main` (log 11:32), a 914-file staged dump, or
"Not committing" after Julio had already lifted rule 4. Proposal: **make
the dangerous verbs loud**. A `pre-commit` / `pre-reset` hook that refuses
`reset --hard`, `checkout` of an old ref, and `branch -f main` unless a
`safety/pre-*` tag exists. Markdown cannot intercept Git.

Architecture Consul (Druid): Three trees still answer "what is a NonPlayer?":
live `AtlasAlusoris/`, recovered `AtlasActorLudi/AtlasAlusoris/`, and
`AtlasLusoris` kits that import one or the other. Questae can *name* the
fork (QST-0081.5, QST-0005). They cannot delete the extra home. Proposal:
**one import graph**, written as a Decree, then a single questa that turns
the loser into a shim. Until then every restore has to be applied twice.

Workshop Consul (Artificer): Finder's ` 2.py` (QST-0081.3, ~224 files) poisons
agent glob. Nested worktree `.claude/worktrees/sweet-mclean-44e50b` is still
on vault bootstraps while the main checkout is source. Agents search the
repo, see both, and restore the wrong copy. Proposal: **gitignore `* 2.py` /
`* 2.md`**, move Finder backups to `~/DnD-session-work-backup/`, and do not
run recovery inside a worktree that lags the board.

Methods Consul (Wizard): Two classes named `AbilityScores` (Kit vs Grimoire).
Callers of the Grimoire passed `character=` that only the Kit declared.
Vault bytecode told the truth; the quest log described the symptom; the
import graph was the bug. Proposal: **Ada spec/body as a search rule** —
if a Kit exists, Grimoires do not export a second type of the same name.
Grep for `class AbilityScores` should return one hit.

Testing Consul (Rogue): "Done" is still a conversation. QST-0072's smoke
gate is unchecked for NPC. Proposal: one Make target `make smoke-player`
that imports `shiny_app` and `summon_player(seed=42)`. Promote it to the
definition of a recovery session, not a checkbox Julio is asked to imagine.

Simplicity Consul (Monk): Curia Questae and Documenta Questae reuse numbers
(QST-0076–0081 mean different wounds). The register in `Curia/Questae/README.md`
is stale and duplicated. Agents mint the next id by globbing two trees.
Proposal: **one Questae root**. Documenta copies become pointers or history.

Lorekeeper (Elf Sage): Bytecode does not hold Julio's voice. REW-0001 already
said so. The live Python REPL (terminal 17) is still the only copy of four
Grave lines. Agora files are not a REPL. Proposal: **snapshot the REPL at
session start**, and treat an open `>>>` composing ledgers as uncommitted
prose under REW-0001.

Monk (closing): None of this replaces the Agora. It is the floor the Agora
stands on. Dialog 0009's seven guards, plus: ignore Finder dupes, one
Questae tree, one AbilityScores type, a smoke target, and a Git hook that
does not wait for a Consul to be awake.

---

## ✅ Convergence check
- [x] Every called Consul has spoken.
- [x] Every objection answered (additive; no dissent that a quest file can intercept Git).
- [x] Concrete proposals on the table (hooks, ignore, one home, smoke, Questae root).

---

## 🕊️ Vox report

Vox: Common ground — **Questae remember; they do not enforce.** The 08-29
loss and the 08-31 uncommitted restore are the same class of event: the
working tree was the only copy, and the council was waiting on Julio.

Options:

1. **Adopt QST-0052 as a Decree now**, and add Finder-ignore + one Questae
   root + a `make smoke-player` target. Cheap. Stops the next wipe.
2. **Keep diagnosing in markdown** until recovery "feels done." The next
   session-end or `git restore` repeats the accident with reconstructed
   source that has no pyc behind it.
3. **Hybrid:** Julio commits the recovered source (QST-0082) today, and
   the hooks land as a follow-up Decree so commit and hardening are not
   one patch.

Consuls lean (3) then (1). Strongest alternative is (1) alone if the
recovered tree is too mixed to commit tonight — then the backup ref
`refs/backup/recovery-20260831-1815-grok` is the off-branch copy.

Code sketch for the floor:

```
# .gitignore
* 2.py
* 2.md
$S/

# Makefile
smoke-player:
	.venv/bin/python -c "import shiny_app; from AtlasLusoris.CharactersKit import summon_player; print(summon_player(seed=42, level=1))"
```

Plus the QST-0052 pre-reset tag, already specified.

→ Awaiting Julio's decision. To be recorded as a Decree if adopted.
