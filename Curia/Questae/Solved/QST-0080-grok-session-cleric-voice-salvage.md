# QST-0080 — 🟠 Grok session salvage: Cleric voice was uncommitted, not gone

- **Type:** recovery / docs
- **Priority:** 🟠 high
- **Status:** Solved
- **Owner:** Cursor (Grok) — this session
- **Route to:** Lorekeeper, Paladin, Artificer, Julio
- **Parent:** QST-0072
- **Sidequests:** QST-0080.1
- **Related:** Dialog 0013 · QST-0052 · `$S/RECOVERY-COORD.md` · transcript `55d5d61d`

---

## 🔍 Diagnosis (what & where)

The Grok chat that wrote Cleric faith-lines and guild voice ended ~02:20–02:31
on 2026-08-31. Julio opened a new chat twelve minutes later, expecting a wipe.

The live tree still had the work. Git did not. `Map_of_Cleric_Prayers.py` is
781 lines on disk and **552 at HEAD**. `ClericKit.py` only seats that voice
after the vaulted kit loads. Neither file is in the nine local commits that
already sit ahead of `origin/codex/recovery-2026-08-29`.

This is a different wound from 2026-08-29 (restore-to-old-ref). The files were
never deleted. They were never made into a branch commit, and the branch was
never pushed.

## 🧾 Evidence

- `git diff --stat`: `Map_of_Cleric_Prayers.py` +415 / −(older body).
- Last applied guild block matches transcript `55d5d61d` (warm register,
  "carried farther than you know", shorter burden line).
- Claude's log at 23:30 and 00:06 explicitly left ClericKit / prayers
  untouched as another agent's live files.
- Snapshot: `refs/backup/recovery-20260831-grok-session` → `d0cda34`.
- File copies: `.recovery-vault/grok-session-20260831/` and
  `~/DnD-session-work-backup/grok-20260831/`.

## 🎯 Desired outcome

1. Other agents do not overwrite the two Cleric files.
2. Julio can commit (or refuse) the voice with the snapshot in hand.
3. REPL Grave lines and the watcher-fantasy thread survive in the vault
   even if the Python REPL or the working tree dies.
4. Domain openings, still plainer than the guild block, have their own
   sidequest rather than being silently "finished."

## 🧭 Notes for the Agora / implementer

- **Do not rewrite the guild description.** Julio accepted the warm block.
- **Do not merge REPL Grave lines** until Julio says which opening stays
  (`From dust, and to it again` vs `From dust we come…`).
- Claude still owns `Map_of_Gear_Titles.py` and Aasimar `_opening`
  (QST-0050.3 Solved). This questa does not touch them.
- Recovery-coord rule 4 forbade branch commits. This snapshot used
  `git stash create` + a `refs/backup/` ref, which does not move the branch.
  A real checkpoint commit still needs Julio.

---

## ✅ Resolution (filled when Solved)

- **Decided by:** Julio, 2026-08-31 08:24 — "commit to the main".
- **What changed:**
  - `a0c7da9` — the prayer ledger and the Guild/Domain voice, committed.
    `Map_of_Cleric_Prayers.py` +322 / −93 against HEAD.
  - `4e2ad9a` — `ClericKit.py` as real `Build_Specialization` source that
    seats `bind_cleric_voice` after the Shapes exist (rode with QST-0081,
    since it is the same restoration pattern as the other ten kits).
  - Guild block is the warm register Julio accepted: watcher as keeper,
    care written as shelter and remembering rather than vigilance.
  - Snapshot ref `refs/backup/recovery-20260831-grok-session` and the two
    file copies are now redundant, but kept — they cost nothing.
- **Closed with a sidequest still open.** QST-0080.1 (Domain openings in
  the older register) stays Open by design; this questa's single purpose
  was getting the authored voice out of "disk only", and that is done.
- **Practice/preference to remember:** uncommitted authored prose is
  already a loss, even when the bytes are still on disk. The gap here was
  ~6 hours between the last accepted sentence and the commit, across two
  sessions and one expected wipe. Prose is the least reconstructible thing
  in the repo — bytecode can be disassembled, a voice cannot.

---

## 🏛️ Council

> Lorekeeper (Elf Sage): The distinctive work in this lane is voice, not
> mechanics. Snapshot the sentences. Do not "improve" them in recovery.
>
> Safety Consul (Paladin): The 29th's restore-to-old-ref is not what happened
> here. Treat "session ended, Julio opened a new chat" as a first-class
> failure mode. A backup ref is the cheap guard until Julio allows a commit.
>
> Workshop Consul (Artificer): Two copies (vault + `$HOME/DnD-session-work-backup`)
> plus one Git object. Agora markdown cannot replace that.

**Weighting:** reach ⟨2⟩ × severity ⟨3⟩ = **6** · council leaning: `build`
