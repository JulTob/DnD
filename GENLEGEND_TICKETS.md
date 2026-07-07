# GenLegend — Tickets

Parked ideas, captured so they don't get lost. Not started — these are scope for later.

---

## TICKET-01 — Typographic system (fonts per element, class, and race)

**Want:** distinct, meaningful fonts per *syntactic element* of a sheet, not one body font everywhere.

- **Identity** (name, species, class, background) — a display face. Cinzel / Cinzel Decorative, or a "vintage Frankfurt" face (e.g. Manufacturing Consent) for titles.
- **Titles / headings** — IM Fell **SC** small-caps (DW Pica SC, Great Primer SC).
- **Body / lore / backstory** — IM Fell **DW Pica**; **Great Primer** for emphasis and pull-quotes.
- **Skills / stats** — a clean, legible face for tabular data.
- **Magic** — its own face (something arcane) so spells read differently from martial text.
- **Per class / race flavour** — optionally swap the display face by class or race (e.g. a runic feel for Dwarves, a flowing hand for Fey).

**Sketch of approach:** a font map keyed by section (`identity`, `skills`, `magic`, …) and an optional override keyed by class/race, applied as CSS classes (`.syn-magic`, `.race-dwarf`, …) on the relevant blocks. Define the faces once as CSS variables; let class/race add a body-level class that re-points the variables.

**Done when:** changing one map flips the fonts for that element everywhere, and a Dwarf wizard visibly reads different from an Elf bard.

*Now (interim):* IM Fell DW Pica + DW Pica SC + Great Primer + Great Primer SC are loaded; gold rules separate prose sections.

---

## TICKET-02 — Surface Minion's dev log while the web app runs

**Want:** keep Minion's verbose, tree/emoji guardian + spy logs (they're a deliberate developer's aid), but *see them while the Shiny app is running* — including which call raised an issue and where — without only watching the terminal.

**Context:** Shiny runs server-side, so `print`/Minion output goes to the terminal that launched it (`./run_shiny.sh`). It is not in the browser by default.

**Options to weigh:**
- **Logfile + dev panel** — have Minion also write to `logs/genlegend.log`; in a `DEV=1` mode, add a collapsible panel in the app that tails the last N lines (polled via a small reactive). Keeps colours via ANSI→HTML.
- **/logs endpoint** — expose a tiny dev-only route that streams recent log records; a floating overlay in the page subscribes to it.
- **Structured capture** — wrap the guardian/spy decorators so each record carries `where` (module + function + line) and severity, making issues filterable.

**Done when:** in dev mode, generating a character that hits a problem shows the Minion trace — and the raising location — in the browser, not just the terminal.

**Caveat:** dev-only. Never ship the log panel or endpoint to production.
