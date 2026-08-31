# Grok session salvage — 2026-08-31 02:32

Source chat: Cursor agent transcript
`55d5d61d-e19b-469b-94af-a92e71d5de8e`
(recovery night 2026-08-29 through Cleric voice, last write ~02:31).

This folder is a **read-only snapshot** of Grok-owned files at the moment
Julio opened a new recovery chat. It is not the live tree. Live files:

- `AtlasLusoris/Map_of_Cleric_Prayers.py` (781 lines; HEAD had 552)
- `AtlasLusoris/AtlasOfGuilds/ClericKit.py` (seats voice after vault load)

Durable Git object (does **not** change the branch; Julio still owns commits):

- `refs/backup/recovery-20260831-grok-session` → `d0cda34`

Off-repo copy: `~/DnD-session-work-backup/grok-20260831/`

Do not restore these copies over a newer live file. Check `ls -lt` and
`$S/RECOVERY-COORD.md` first.

## What was not lost

The previous Grok chat died after an AskQuestion turn. The working tree still
held the warm Cleric guild description Julio had just accepted, the prayer
ledgers, Domain openings/frames, and `bind_cleric_voice`. Nothing here needed
decompilation. It needed a commit (or this snapshot).

## What this snapshot cannot hold

Julio's live Python REPL (terminal 17) was still drafting Grave/Knowledge
lines at salvage time. Those lines are recorded in `repl-grave-knowledge.md`.
They were **not** merged into the live ledger (Julio was mid-edit).
