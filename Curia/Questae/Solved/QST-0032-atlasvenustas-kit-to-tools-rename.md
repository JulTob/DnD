# QST-0032 — Canon/Conventions.md respecified; rename AtlasVenustas Kit_of_X → Tools_of_X

- **Type:** docs / refactor
- **Priority:** 🟡 normal
- **Status:** Solved (2026-07-15)
- **Owner:** Julio
- **Route to:** Barbarian, Bard
- **Parent:** —
- **Sidequests:** QST-0032.1 (sweep the rest of the codebase)
- **Related:** `Canon/Conventions.md`, QST-0031 (SpellsKit naming discussion that prompted this)

---

## 🔍 Diagnosis (what & where)
Julio amended `Canon/Conventions.md` directly (mid-conversation, while QST-0031's naming question — `SpellsKit` vs `Compass_of_Spells` — was being discussed) to make the file-naming law more specific to how he thinks about the project's syntax: it now adds `Charts_of_X` (algorithms/actuators), broadens `Compass_of_X` to "Abstract Types, tags, and classes to organize Maps or Charts," adds `Tools_of_X` ("Context interfaces," example `Tools_of_Loader`), and adds `XKit` ("TOP implementation of a specific class and related Tags," example `SpellsKit`).

The new `Tools_of_X` row names `Tools_of_Loader` as its own example — a direct, 1:1 match against the *existing* `AtlasVenustas/Kit_of_Loader.py`, alongside its three siblings (`Kit_of_Masonry.py`, `Kit_of_ShareableLinks.py`, `Kit_of_Tablet.py`), all presentation-layer "context interface" modules (they inject head-tags/JS/CSS for the Shiny app) that no longer fit under a bare `Kit_of_` label now that `XKit` is reserved for real TOP-Tag modules.

## 🎯 Desired outcome
`AtlasVenustas`'s four `Kit_of_X` modules renamed to `Tools_of_X`, with every import site updated, and the app verified to still run. No lingering ambiguity between "Kit" (now `XKit` = TOP) and these four (now `Tools_of_X` = presentation context interfaces).

## 🧭 Notes for the Agora / implementer
Other `Kit_of_X` files exist elsewhere in the repo (`AtlasWorldBuild/AtlasOfMapmaking/`) and were **not** touched here — that package is unrelated to this session's work and deserves its own look rather than a drive-by rename under someone else's context. Tracked as QST-0032.1.

---

## ✅ Resolution
- **Decided by:** Julio (2026-07-15, direct instruction after amending Canon himself)
- **What changed:** `AtlasVenustas/Kit_of_Loader.py` → `Tools_of_Loader.py`, `Kit_of_Masonry.py` → `Tools_of_Masonry.py`, `Kit_of_ShareableLinks.py` → `Tools_of_ShareableLinks.py`, `Kit_of_Tablet.py` → `Tools_of_Tablet.py`. Updated the four import lines in `shiny_app.py` and each file's internal self-referential self-test print/comment lines. Verified: `shiny_app` imports cleanly post-rename; dev server still serves 200.
- **Practice/preference to remember:** `XKit` (suffix, no underscore) now exclusively means "this module is a real TOP implementation, built on TagKit" — never use the `Kit` word for anything else going forward, including presentation/context-interface modules, which take `Tools_of_X` instead. When a Canon file changes on disk outside an agent's own edits mid-session, say so plainly and reconcile before continuing rather than silently working from a stale read.

---

## 🏛️ Council
> Readability Consul (Barbarian): Good split — "Kit" meaning two unrelated things was exactly the ambiguity worth killing before any real TOP code exists to get confused with it.
> Understanding Consul (Bard): Worth the pause to confirm the naming lived in Canon before renaming anything — this is exactly the kind of decision that should be legible later, not just "someone renamed some files."

**Weighting:** reach 1 × severity 1 = **1** · council leaning: `build` (done)
