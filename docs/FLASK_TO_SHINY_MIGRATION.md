# Migrating from Flask to Shiny

## Feasibility: **Yes**

The Shiny app (`shiny_app.py`) already implements the same core flows as the Flask app. Dropping Flask and using Shiny as the only web UI is feasible with a small amount of cleanup and optional enhancements.

---

## What Flask currently provides

| Route | Purpose | Shiny equivalent |
|-------|---------|------------------|
| `/` | Home + form options (species, class, background, etc.) | **home panel** + generator tablet |
| `/character`, `/character/...`, `/generate_character` | Character gen + display + shareable URL | **character panel** (form + display); no shareable URL yet |
| `/character/random` | Random character page | **character panel** + “Summon” with random options |
| `/npc`, `/npc/...`, `/generate_npc` | NPC gen + display + shareable URL | **npc panel** (form + display); no shareable URL yet |
| `/list`, `/list/<race>/<archetype>` | List of 5 NPCs | **npclist panel** |
| `/AboutUs` | About Us page | Footer link to GitHub (or add an About panel) |
| `/wiki/lore` | Lore page | Footer link to GitHub wiki (or add a Lore panel) |
| `/favicon.ico` | Favicon | Can add in Shiny `ui.tags.link` |

**Flask-only details:**

- **Session:** `session['npc']` used once in `npc_display`; Shiny keeps state in `reactive.value`s, so no migration needed.
- **Flask-SocketIO:** In `requirements.txt` but **not used** in `app/`; safe to remove.
- **Jinja context:** `Modifier`, `Dice`, `Lair`, `Legendary`, `Region` are passed to templates; Shiny builds UI in Python, so no direct equivalent needed (use the same Atlas modules where needed).

---

## What you gain by going Shiny-only

1. **Single stack:** One server (`shiny run`), one entrypoint (`shiny_app.py`), no Flask/gunicorn.
2. **Faster startup:** No Flask or `app.routes` loaded for the web app (already fixed for Shiny via deferred imports in `app/__init__.py`).
3. **Reactive UI:** No full-page redirects; state and panels live in one app.
4. **Deploy:** `app.yaml` already uses `shiny run`; remove or repurpose any gunicorn/Flask deploy config.

---

## Migration checklist

### 1. Confirm Shiny covers all use cases

- [ ] Home, Character, NPC, NPC List panels behave as you want.
- [ ] Optional: add **shareable URLs** (e.g. `?character=...&seed=...` or hash routing) if you need “link to this character/NPC” like Flask’s `/character/.../seed` and `/npc/.../seed`.

### 2. Static pages (About Us / Lore)

- **Option A:** Keep footer links to GitHub (current).
- **Option B:** Add “About” and “Lore” panels in Shiny and render the same content (e.g. markdown or HTML from files).

### 3. Remove Flask and related code

- [ ] Remove or refactor `app/__init__.py`: no `create_app()`, or keep it only for tests that still expect a Flask app.
- [ ] Remove or archive `app/routes.py` (logic already in `shiny_app.py` or Atlas).
- [ ] From `requirements.txt`: remove `Flask`, `Flask-SocketIO`, `gunicorn`, and any Flask-only deps (e.g. `Jinja2`, `Werkzeug` if only used by Flask). Keep what Shiny and Atlas need.
- [ ] Update or remove `app.py` (Flask entrypoint) and any scripts that run `create_app()` or the Flask app.
- [ ] If you use a Dockerfile that runs gunicorn, switch it to `shiny run` (as in `app.yaml`).

### 4. Preserve what you still need

- **`app.random`:** Keep; Shiny and Atlas use it. No Flask dependency after the deferred-import change.
- **Atlas modules:** Unchanged; used by both Flask and Shiny.
- **Templates:** Keep only if you serve them from Shiny (e.g. markdown/HTML panels); otherwise you can archive `app/templates/` and static assets you don’t use from Shiny.

### 5. Favicon and 404/500

- Add favicon in Shiny (`ui.tags.link(rel="icon", href="...")` or inline SVG).
- Shiny handles errors in its own way; no need to replicate Flask’s 404/500 handlers unless you want custom error pages.

---

## Summary

- **Feasible:** Yes; Shiny already provides the main functionality.
- **Effort:** Low if you accept current Shiny behavior; add shareable URLs and/or About/Lore panels if you want parity with Flask.
- **Risk:** Low; main work is deleting Flask code and trimming dependencies, not rewriting logic.
