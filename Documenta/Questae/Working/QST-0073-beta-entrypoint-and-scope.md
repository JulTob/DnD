# QST-0073 — Beta entrypoint and scope: one door, one service

- **Type:** design
- **Priority:** 🔴 urgent
- **Status:** Working
- **Owner:** Claude (worktree `sweet-mclean-44e50b`, branch `Julio_Cl/dnd-genlegend-recovery-ea160e`)
- **Route to:** Architecture, Workshop, Venustas
- **Parent:** —
- **Sidequests:** —
- **Related:** Decree 0006 · QST-0072 · QST-0074 · QST-0075 · QST-0027

---

## 🔍 Diagnosis (what & where)

Decree 0006 fixes the beta to the character generator alone. The codebase, mid-recovery, offers two candidate roots:

- `app/main.py`: the intended modular composition root (per `Curia/Current-State.md`). It cannot boot. Its composition layer is lost to the accident: `app/navigation.py`, `app/session.py`, `app/routing.py`, `app/client.py`, and `app/pages/__init__.py` do not exist, and it imports a NonPlayer public surface (`nonplayer_choices`, `summon_nonplayer`, `summon_nonplayer_list`) that no source file defines.
- `shiny_app.py`: the monolith root. It boots and generates players today (Cursor's recovery, 2026-08-29 19:37 on the board). It still serves NonPlayer pages through the legacy `AtlasAlusoris` atlas.

`scripts/run_shiny_preview.sh` still execs `app.main:app`, which no longer exists as a bootable target.

## 🧾 Evidence

- `ImportError: cannot import name 'nonplayer_choices' from 'AtlasActorLudi.AtlasAlusoris'` on `import app.main` (2026-08-29 21:01, worktree, codex tip `4fa25dc`).
- `find app -name '*.py'`: no `navigation.py`, `session.py`, `routing.py`, `client.py`, no `app/pages/__init__.py`.
- `$S/RECOVERY-COORD.md`: player summon green through `shiny_app` (`summon_player(seed=42, level=1)` → Gale Greystone, Orc Paladin Farmer L1).

## 🎯 Desired outcome

1. The beta serves **one root that boots**: `shiny_app.py`, until QST-0074 restores the modular root.
2. The character generator is the front and center of the served app. NonPlayer, list, and Magistratum surfaces are **dark**: not linked, not routed, but their code is not deleted.
3. `scripts/run_shiny_preview.sh` and `.claude/launch.json` point at the served root, so "run the app" means the beta.
4. The whole beta path (generation → sheet → styles → shareable link) is reviewed for correctness, canon, and craft. Improvements are minted as questae, not slipped in.

## 🧭 Notes for the Agora / implementer

- This is the short-run ruling. `Curia/Current-State.md` keeps `app.main` as the destination; QST-0074 carries that torch. Do not let the monolith grow new responsibilities: changes to `shiny_app.py` stay within beta scope.
- Going dark is a scope cut, not an amputation: prefer removing navigation entry points over deleting pages or atlas code. The NonPlayer wing must be re-lightable by QST-0075 without archaeology.
- Entrypoint files (`run_shiny_preview.sh`, `launch.json`, `shiny_app.py` UX) are held by Cursor on the recovery board. Changes to them go through `$S/RECOVERY-COORD.md`, not around it.

---

## ✅ Resolution (filled when Solved)
- **Decided by:** Decree 0006 (scope); entrypoint ruling proposed here, to be confirmed by Julio at merge
- **What changed:** in progress
- **Practice/preference to remember:** when a migration is caught mid-stride by a disaster, ship the root that works and keep the destination as a questa, never as a half-boot.

---

## 🏛️ Council

> Architecture Consul (Druid): The composition root is the one file that may not lie. `app.main` promises pages it cannot summon; `shiny_app` keeps every promise it makes today. Serve the honest one, and let QST-0074 rebuild the beautiful one.
> Workshop Consul (Artificer): The preview script must exec what exists. A launcher pointing at a ghost is a trap for every future hand that types "run".
> Venustas Consul (Bard): Scope narrowing is a gift to craft: one page, polished, beats five pages explained. The dark wings keep their walls; we only dim their lamps.

**Weighting:** reach 3 × severity 3 = **9** · council leaning: `build`
