# QST-0051 — 🟡 Delete the orphaned `AtlasLusoris/CharactersKit.py` (was: "foundation fails 4/8")

> **⚠️ CORRECTION (2026-08-31).** The original alarm below is **wrong about the live tree.** The
> canonical Character root is **`AtlasActorLudi/CharactersKit.py`** (every live importer resolves there),
> and it is **9/9 self-tests green** and already TagKit-`0.2.0a1`-clean. The 4/8 failure and the forbidden
> `__contains__` overrides exist only in **`AtlasLusoris/CharactersKit.py`, which has no live importer** —
> it is an orphaned stale duplicate. So the foundation is healthy; there is nothing to migrate on the live
> path. **Real action: delete the orphan** (and note the general TagKit-`__contains__` lesson for QST-0042).
> The Option A/B design question below is moot for recovery (it only concerned the dead copy). Downgraded
> to 🟡. The analysis is kept for the record and for the QST-0042 sweep.

- **Type:** chore (delete orphaned duplicate) — *was: bug (recovery regression)*
- **Priority:** 🟡 normal — *the live foundation is fine; this is cleanup + a QST-0042 note*
- **Status:** Open — **corrected; action is a deletion, not a fix**
- **Owner:** unclaimed — *the orphan has no importer; deleting it is safe once someone confirms no tooling reads it*
- **Route to:** Codex (owns CharactersKit), Wizard (Methods), Warlock (Contracts), Lorekeeper, Julio (design call)
- **Parent:** —
- **Sidequests:** —
- **Related:** QST-0042 (review Kits against the current TOP Guide — this IS the post-resync drift it predicted) · QST-0043 (string-label probe contract) · QST-0072 (recovery ledger; its "Character+Gender foundation done" checkpoint is actually red) · `$S/RECOVERY-COORD.md` · Agora Dialog 0009 (accident diagnosis)

---

## Diagnosis

Running the on-disk focused suite in `AtlasLusoris/CharactersKit.py` gives **4 pass, 4 fail**:

- pass: `_test_rng_determinism`, `_test_roll_shape`, `_test_level`, `_test_contains_core` (the pure-`Character` core is healthy)
- fail: `_test_player_role_and_underlay`, `_test_spaced_name`, `_test_nonplayer_short_circuit` with
  `TagCompositionError: Tags cannot replace TOP-managed runtime protocol(s): '__contains__'`;
  `_test_is_character_contract` fails because that same error fires before the Pre can run.

Root cause: during the recovery churn, **TagKit was bumped to `0.2.0a1` (pinned `@c7bd3761...`)**, a multi-module package (it was a single `TagKit.py` earlier in the day). The new pin changes the contract in three ways relevant here:

1. `__contains__` is now a **TOP-managed runtime protocol**: a Tag may not declare it (`runtime_types.py:502`; shipped `TagKit/IMPLEMENTATION_NOTES.md:306` states membership and Tag-application dunders "remain TOP-managed and cannot be" overridden). `Role.__contains__` and `NonPlayer.__contains__` (both `@Underlay`) are therefore rejected at application time, so `Player(char)` itself raises.
2. **Field membership is now native, both directions.** Verified with override-free tags against the real `Character`: `char in Player`, `char in Role` (base), `Player in char`, `Role in char` all return `True` with no custom `__contains__`.
3. **Native NAME-probing does not layer over a Target that owns `__contains__`.** Because `Character` defines its own (plain-class, allowed) `__contains__`, the string probe `"player" in hero` now returns **`False`** (Character's method answers the string and never consults the applied Tags' NAMEs). The deleted `Role.__contains__` was the only thing making `"player" in hero` true.

## Evidence (override-free tags vs the real `Character`, TagKit 0.2.0a1)

```
hero in Player   True     Player in hero   True     "player" in hero   False
hero in Role     True     Role   in hero   True     "role"   in hero   False
                                                      "character" in hero True   (Character sentinel)
Player(NotACharacter) -> TagPreconditionError        (is_Character Pre works natively)
"non player character" in npc  False   "npc" in npc  False   npc in NonPlayer True
```

Also observed while here (log, not this quest's fix):
- `New_Score()` on disk is back to the broken no-`char` form (`rolls = [Dice(6) ...]`, `Dice` not in scope) — the `New_Score(char)` fix + the `Pick` helper were lost in a revert. Errors on any call; not covered by the suite.
- **Two `CharactersKit.py` copies differ**: `AtlasLusoris/CharactersKit.py` vs `AtlasActorLudi/CharactersKit.py`. Pick one home before more work lands, or they drift apart.

## Desired outcome

The Character + Role foundation composes and the suite is green under the pinned TagKit, without reintroducing a forbidden `__contains__` override.

Fix has two parts: a forced deletion, and one design decision.

**Forced (not optional):** delete the `@Underlay def __contains__` from `Role` and from `NonPlayer`. TagKit rejects them.

**Design call (Julio) — how does a string like `"player"` relate to a Character?**

- **Option A (keep string NAME sugar).** Fold the NAME probe into `Character.__contains__` (the plain-class method, which is allowed): on a string miss, ask TagKit for the applied Tags and match NAME casefold. Preserves `"player" in hero`. Cost: the Target's `__contains__` grows, and it re-implements what TagKit already does for bare targets.
- **Option B (drop string NAME sugar) — recommended.** Membership is `hero in Player` / `Player in hero` (both native), i.e. characteristics are Tags queried as Fields, not strings. Simpler, paradigm-pure, and consistent with QST-0043's read that string-by-label probes are Kit convenience, not Guide law. Cost: `"player" in hero` no longer works; callers that string-probe roles must move to Field checks.

Whichever is chosen, the four Role tests are rewritten to the native contract, `NonPlayer`'s short-string aliases (`"npc"`, `"non player"`) are either dropped (Option B) or reintroduced through a TagKit-supported label mechanism (not a `__contains__` override), and `_test_is_character_contract`'s docstring loses its now-obsolete "stub needs `__contains__`" note.

## Notes for the implementer

- **Verified:** removing the two overrides makes the Field-membership and Pre behavior pass natively; the only open work is string-NAME semantics (Option A/B) and the corresponding test rewrites.
- This is exactly the drift QST-0042 anticipated ("Kits may still carry pre-sync assumptions ... Doctrine and the Guide were resynced"). The TagKit pin bump IS that resync. Any other Kit that overrides `__contains__` (or another managed dunder) has the same bug: `grep -rn "def __contains__" --include="*.py" Atlas*` and check each against the 0.2.0a1 GUIDE.
- Do not "fix" by pinning TagKit back; the bump is the intended direction. Migrate the consumer.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** —
- **What changed:** —
- **Practice/preference to remember:** —

---

## 🏛️ Council
> Methods Consul (Wizard): The healthy half proves the substrate is fine; only the Role layer assumed an old TagKit. Delete the overrides, lean on native Fields.
> Contracts Consul (Warlock): `__contains__` is now the engine's, not ours. Our contract surface is `@Pre`/`@Post` and Fields, which all still work. Good fences.
> Simplicity Consul (Monk): Option B. A Character is in the Player Field or it is not. A string spelling of the same question is a second way to ask, and second ways drift.
> Lorekeeper (Elf Sage): Whatever we pick, the test names already tell the story ("player role and underlay"); rewrite the bodies, keep the intent legible for the next reader.
