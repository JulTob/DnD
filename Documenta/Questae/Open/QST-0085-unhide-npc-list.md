# QST-0085: Unhide NPC List

**Status:** Open  
**Priority:** Low  
**Depends on:** QST-0084 (NPC Generator)  

## Goal
Restore the NPC List feature from hidden (beta) state to active user-facing feature when it meets quality/robustness standards.

## Context
The NPC List feature (`alusoris_list_page`) exists in the codebase but is disabled in the UI with `parked=True` button styling. This feature generates and displays a list of legendary NPCs (typically five at a time) for bulk NPC generation or encounter design.

## Requirements
- [ ] Verify NPC list generation paths recover gracefully
- [ ] Verify list rendering and pagination logic work correctly
- [ ] Test sheet formatting for multiple NPCs in list view
- [ ] Enable the UI button (`go_npclist` action, remove `parked=True`)
- [ ] Verify "5 New NPCs" button generates fresh batch correctly
- [ ] Update navigation docs in `/Documenta`

## Implementation Notes
- Routes: `/npclist/` ASGI redirects handled in `app.routing.py`
- UI mounting: `app/pages/actor_ludi/alusoris_list_page` and `mount_alusoris_list_page`
- Server handlers: check `shiny_app.py` for `go_npclist` button handler
- List logic: likely in `AtlasActorLudi/AtlasAlusoris/` or higher-level composition

## Related Files
- `app/pages/actor_ludi/alusoris_list.py` — NPC List page UI/logic
- `AtlasActorLudi/AtlasAlusoris/` — NPC list generation engine
- `app/routing.py` — URL routing
- `shiny_app.py` — UI button registration

---
*Created during hide-don't-delete restoration; tracks unhiding of parked feature.*
