# Chatlas2 initial Views - impl-req

## Impl.Abstract

- **scope:** introduce the first provider-neutral `tarav chatlas2 views` surface with `list` and `get`, initially exposing `full`, `transcript`, `user`, and `events`
- **status:** implemented and verified; implementation remains uncommitted after checkpoints `163dfc1` and `2da6509`
- **source:** explicit autonomous implementation invocation in Codex session `01a001c2-8fb1-72e0-8aa1-0bbc52c4b5e8`
- **target:** pure Chatlas2 view projections, cache-backed CLI reads, focused tests, and maintained Chatlas2 guidance
- **out of scope:** porting current Chatlas view internals; `replay`; `zip-transcript`; cross-session selection; message search; consumer cutover beyond this new public route
- **acceptance:** the four views read one exact session through the canonical Normal Model provider, preserve chronological order, apply bounds while streaming collections, and introduce no new authoritative model or cache policy

## Impl.Agendix

- **touched (authorization):** introduce the initial Views under `tarav chatlas2 views` and execute autonomously. ^c20260816-23u
- **touched (design):** the canonical provider transparently validates or rebuilds disposable Normal Model caches. `527-chatlas2-normal-model-redesign-design-session.md` → `Normal.Model.Cache` ^c20260816-36u
- **touched (design):** read limits apply while streaming independently readable cached collections. `527-chatlas2-normal-model-redesign-design-session.md` → `Normal.Model.Cache` ^c20260816-33u
- **touched (design):** `Chat.Message` is the complete primary user-agent exchange projected over the event tape. `527-chatlas2-normal-model-redesign-design-session.md` → `Chat.Message` ^c20260815-7u

## Impl.Index

### View boundary

- a Chatlas2 View is a disposable read projection over current Normal Model content; it owns neither normalization nor cache validation
- `full` returns the complete canonical Normal Model unchanged
- `transcript` returns chronological cached `Chat.Message` records for both sides
- `user` returns the same projection restricted to user-side messages
- `events` returns chronological Normal Events from the cached event tape
- projected collection records retain their canonical model objects; Views do not invent another event, message, or reference identity

### Public route

- `tarav chatlas2 views list` reports the implemented view names and their projected collection
- `tarav chatlas2 views get (--session-id | --identity-hash) [--view NAME] [--limit N]` reads one exact session; `full` is the default
- `--limit` is valid for collection views and is applied during cache iteration; it is rejected for `full` rather than silently changing complete-model semantics
- output is inspectable JSON, compact by default and indented with `--json`, following the existing Chatlas2 messages surface

## Execution.Plan

### Vertical.Slice 1 - RED public contract

- add focused CLI tests for view discovery, the complete `full` model, chronological transcript, user-only projection, event tape, bounds, and invalid full-model bounds
- observable: the new commands do not exist before implementation
- check: run the focused new tests and record the expected parser failure

### Vertical.Slice 2 - Pure projections and cache-backed route

- add a small Chatlas2 Views module containing the implemented registry and projection operations
- wire `views list|get` into the existing CLI selector and canonical Normal Model provider
- observable: collection views stream only their own JSONL collection and `full` reuses the provider's complete-model path
- check: focused Views and complete Chatlas2 tests

### Vertical.Slice 3 - Live trial and guidance

- exercise all four views against the current Codex session
- update architecture, repository guidance, and the active Chatlas2 design session with the implemented boundary and explicit deferrals
- observable: the current user conversation is readable through `user` and the complete model remains available through `full`
- check: corpus verification, repository suite, Ruff/diff checks, and Git status review

## Impl.Log

- **2026-08-16 — execution gate:** autonomous development is authorized and grounded as `^c20260816-23u`
- **2026-08-16 — scope decision:** initial migration is deliberately limited to `full`, `transcript`, `user`, and `events`; `replay` and `zip-transcript` wait for an evidenced consumer need
- **2026-08-16 — RED/GREEN:** the focused CLI regression first failed because `views` was absent at the parser boundary; the registry and four projections now pass with complete-model and bounded-collection behavior
- **2026-08-16 — live Codex trial:** the current session returns 123 user messages and the latest is the authorizing Views invocation; bounded transcript/events reads stop at three records, while `full` returns the canonical model with 11,627 events and 509 Chat.Message annotations
- **2026-08-16 — live Claude trial:** user view reads the archived Claude session `890050c4-9473-4b4f-ab2f-a67c54d57894` through the same provider-neutral route with user-only origin intact
- **2026-08-16 — verification:** all 1,967 repository tests pass; focused Chatlas2 plus architecture coverage passes 66 tests; all 21 conformance captures verify and normalize; focused Ruff, format, and diff checks pass; Skillware retains 30 pre-existing POIs with none targeting Chatlas2. Repository-wide Ruff remains blocked only by the pre-existing unused `local_storage_paths` import in `src/tarav/skills/routing.py`
