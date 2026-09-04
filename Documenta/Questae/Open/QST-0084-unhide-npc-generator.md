# QST-0084: Unhide NPC Generator

**Status:** Open  
**Priority:** Low  
**Depends on:** QST-0075 (NonPlayer surface)  

## Goal
Restore the NPC Generator feature from hidden (beta) state to active user-facing feature when it meets quality/robustness standards.

## Context
The NPC Generator (`alusoris_page`) exists in the codebase but is disabled in the UI with `parked=True` button styling. This feature allows users to generate legendary NPCs with the same character-generation engine, but for non-player characters.

## Requirements
- [ ] Verify NPC generation paths recover gracefully (minion log, retry logic)
- [ ] Verify all NPC-specific lore/prose is recovered and complete
- [ ] Test NPC sheet rendering against beta-quality standards
- [ ] Enable the UI button (`go_npc` action, remove `parked=True`)
- [ ] Update navigation docs in `/Documenta`
- [ ] Test user flows for common NPC generation scenarios

## Implementation Notes
- Routes: `/npc/` ASGI redirects handled in `app.routing.py`
- UI mounting: `app/pages/actor_ludi/alusoris_page` and `mount_alusoris_page`
- Server handlers: check `shiny_app.py` for `go_npc` button handler
- Lore sources: Atlas modules for NPC-specific features

## Related Files
- `app/pages/actor_ludi/alusoris.py` — NonPlayer page UI/logic
- `AtlasActorLudi/AtlasAlusoris/` — NPC generation engine
- `app/routing.py` — URL routing
- `shiny_app.py` — UI button registration

---
*Created during hide-don't-delete restoration; tracks unhiding of parked feature.*
