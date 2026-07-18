# agentos-index --gr-review

Use this module to run a grounding campaign's gate phase: walk a `Gr.Req`'s `proposed` entries with the user, flip statuses, and land the approved links. The grounding analogue of `agentos-hugentics-impl --exec` — except the executer here is the USER's judgment; this module is its clerk.

This module is NOT `Workflow.Neutral`: it applies gated index writes (`Edition.Trigger.User.Gated`, `Verbatim.User.Gated`) — one user verdict per entry, never a blanket apply.

## Inputs

- a `Gr.Req` (note number or path); only entries at `status: proposed` enter the walk — `ambiguous` entries are reported as pending discovery (`--gr-survey`'s job), not reviewed

## Review Loop (per proposed entry)

1. **Show**: the target line as it stands today (re-locate by content, never trust stale line numbers), the proposed anchor + hint + why, the landing form.
2. **On doubt, resolve live**: `agentos chatlas views inline --anchor <key> --radius 3 --filter turns` — the user judges the actual turns, not the maker's summary.
3. **Verdict**:
   - land → apply the edit (trailing inline anchor on the supported line); status → `landed`
   - drop → status → `dropped`, reason into `Gr.Log`
   - skip → stays `proposed`; the review is resumable across sittings — state lives in the artifact, not the chat
4. Batch small runs of verdicts are fine (the user may approve a table of entries at once — that approval is the gate for those entries).

## Closing A Sitting

- run `agentos index linter --depot <depot>` — the provenance bridge independently re-verifies every landed anchor (resolves it, checks the landing turn's role); any finding here blocks the close until resolved
- refresh `Gr.Abstract`: coverage after (`--warn-unlinked` recount), status (`landed` when no `proposed` entries remain, else `partially landed`)
- append to `Gr.Log`: drops with reasons, deviations, anything the next sitting needs
- commit per the project's commit policy

## Discipline

- statuses are edited in place in the `Gr.Set` — the artifact is the single record through the campaign; no parallel lists
- never land an entry the user has not seen this sitting or explicitly batch-approved
- a `dropped` entry's anchor stays in the register (anchors are immutable, never reused) — the drop is an index decision, not a register one
