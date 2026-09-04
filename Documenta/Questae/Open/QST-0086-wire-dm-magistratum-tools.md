# QST-0086: Wire DM/Magistratum Tools

**Status:** Open  
**Priority:** Low  
**Depends on:** Decree 0006 (beta consolidation)  

## Goal
Integrate Dungeon Master companion tools from the Magistratum module into the user-facing application when design and robustness targets are met.

## Context
The `AtlasMagistratum` module and `app/pages/magistratum.py` provide Dungeon Master tools for session management, NPC briefings, encounter inspiration, and other DM-workflow features. These are currently not wired into the main UI navigation (`shiny_app.py`), making them inaccessible to users.

## Requirements
- [ ] Design UX flow for DM tools (new nav button? separate section? menu?)
- [ ] Wire Magistratum page into main navigation
- [ ] Test session/NPC path handling and URL sharing
- [ ] Verify all DM-specific lore/tools render correctly
- [ ] Document DM tool capabilities in `/Documenta`
- [ ] Test common DM workflows (encounter prep, NPC briefings, etc.)
- [ ] Decide scope: beta launch includes DM tools or post-beta phase?

## Implementation Notes
- Page module: `app/pages/magistratum.py` (exists, not mounted)
- Atlas engine: `AtlasMagistratum/` (session paths, inspiration generation, NPC briefing)
- Routing: `/dm/` paths handled in `app.routing.py`
- Server handlers: need to add mounting and button handlers to `shiny_app.py`

## Related Files
- `app/pages/magistratum.py` — DM page UI/logic
- `AtlasMagistratum/` — DM engine and utilities
- `app.routing.py` — URL routing
- `shiny_app.py` — UI navigation and mounting

## Open Questions
- Should DM tools launch in beta, or post-beta phase?
- What is the priority vs. NPC generator/list features?

---
*Created during hide-don't-delete restoration; tracks wiring of unmounted feature.*
