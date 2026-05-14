# Impl-Req Example

Example only. Adapt the exact wording and section weight to the current request.

```md
# Tara Mobile Design Realignment - impl-req

## Impl.Abstract

- **scope:** realign the home screen implementation with the accepted design — remove the extra entry action, preserve accepted section order and navigation model
- **status:** ready for implementation
- **source:** design discussion drift detected during revision scan

## Impl.Index

### Screen.Entry.Action.Alignment

- the accepted design specifies one clear primary entry action on the home screen
- the current implementation introduced a second entry action that was not part of the accepted design
- the layout now sends mixed signals about the primary flow
- the extra action must be removed; the accepted reordered sections must remain intact
- preserving existing data wiring unless the layout change requires modifying it

### Navigation.Model.Preservation

- the accepted navigation model must not change as part of this realignment
- no unrelated screens should be redesigned
- visual polish, analytics, and text copy outside the affected screen are out of scope

## Execution.Plan

### Slice 1 — Remove extra entry action

- remove the second entry action from the home screen
- path: home screen widget tree → action buttons → primary action
- observable: the screen exposes exactly one primary entry action
- check: visual inspection + existing navigation tests pass
- status: not started

### Slice 2 — Verify section order preserved

- confirm the accepted reordered sections remain intact after the action removal
- path: home screen layout → section list
- observable: sections appear in the accepted order
- check: visual inspection + screenshot comparison with accepted design
- status: not started

## Impl.Log

- 2026-04-16: Designer created this note after revision scan found drift between accepted design intent and current implementation.
- 2026-04-17: Implementer confirmed understanding with the user before editing. Execution not started yet.
```

## Relevant Files Or Surfaces

This example references:

- `apps/tara_mobile/lib/screens/home_screen.dart`
- `notes/live/540-home-screen-design-impl-req.md` — earlier request that this note refines
