# QST-0128 — The player sweep only ever uses seeds 1 to 3

- **Type:** chore/cleanup · testing
- **Priority:** 🟠 high
- **Status:** Open
- **Owner:** unclaimed
- **Route to:** Testing (Rogue) · Workshop (Artificer)
- **Parent:** —
- **Sidequests:** —
- **Related:** PR #7 (§2 of its description) · QST-0016.6.1 (seeded replay contract) · `scripts/sweep_player.py`

---

## 🔍 Diagnosis (what & where)

`scripts/sweep_player.py` varies level, species, background, Guild and
specialization, in a quick set of 78 requests and a wide set of 1167, but the
seed axis is the same three values, 1, 2 and 3, in both. A crash that depends
on the draw rather than on the request is invisible to the main gate unless
one of those three seeds happens to hit it.

## 🧾 Evidence

Two Origin Feats, Symbiotic Being and Echoing Soul, imported a name that did
not exist. Any character drawing either failed to generate, for every Guild
and every species, about one in 150. Human on seed 4 reproduced it. The wide
sweep was green throughout, because seeds 1 to 3 never drew the feats. It was
found by accident on 2026-09-14 and fixed in PR #7.

## 🎯 Desired outcome

The seed axis is wide enough that a one-in-150 crash is caught with high
probability by the wide sweep, and the quick sweep stays under a minute.
Seeds stay fixed and listed, never random, so a failure replays.

## 🧭 Notes for the Agora / implementer

Options that keep determinism: a longer fixed seed list for the wide sweep; a
seed derived from the request (species, background, Guild) so every cell gets
its own draw; a `--seeds` flag with a documented default. Report run time in
the summary line as now. No decision needed beyond the default.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council

> Testing Consul (Rogue): Three seeds is one seed with two friends. The gate has to walk the draws, not only the menus.
> Workshop Consul (Artificer): Keep the quick set quick. Spend the seeds in the wide run, and print them so a red cell can be replayed by hand.

**Weighting:** reach 3 × severity 2 = **6** · council leaning: `build`
