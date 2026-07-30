# Anchory Application-Owned Amendment Validation - impl-req

## Impl.Abstract

- **Scope:** prevent `agentos anchory amend` from writing invalid or meaning-changing Chatlas support-set replacements while keeping generic Anchory application-agnostic.
- **Status:** ready for implementation.
- **Source:** issue 515, current implementation inspection, and the autonomous development invocation.
- **Out of scope:** a field-level `--hint` command, `agentos chatlas anchory amend`, resolve-aware `anchory check`, anchor retirement, and changes to `Support.Set` semantics.
- **Support set:** autonomous design and execution authority ^c20260730-33u

## Impl.Agendix

- **Touched (index):** `Anchory.System` - integrating applications own payload meaning; Anchory owns amendment and atomic persistence (`agentos-pkg/design/107-design.md`, `agentos-pkg/appendix/Anchory.System-appendix.md`).
- **Touched (index):** `Chatlas.Anchory` - Chatlas owns `chatlas.support-set.v2`, exact visible-user-turn resolution, and timestamp integrity (`agentos-chatlas-pkg/design/100-design.md`).
- **Touched (chat):** the user authorized autonomous end-to-end development of application-owned amendment validation ^c20260730-33u
- **Structural:** `agentos-cli` is the composition root joining the generic Anchory registrar to Chatlas-owned validation, following the existing Index external-check injection pattern.
- **Open space:** support meaning is provisionally the ordered member identity and `types` cargo. `hint` and a validated `at` are repairable metadata.

## Impl.Index

### Anchory.Amend.Validator

- `AnchoryDepot.amend` accepts an optional application validator and invokes it under the exclusive depot lock after reading the current record and before writing the replacement.
- The validator receives the current and proposed normalized records; generic amendment remains unchanged when no validator is supplied.
- Validator rejection leaves the shard and runtime cache unchanged.

### Anchory.Command.Composition

- `register_anchory_commands` accepts an optional amendment validator and passes it through the command handler to the atomic library operation.
- `agentos-cli` injects the Chatlas validator; neither `agentos-py` nor generic Anchory imports Chatlas.

### Chatlas.Support.Set.Amendment

- Chatlas claims a current record when `app == "chatlas"` and validates every proposed replacement through the production support-set resolver.
- A replacement must retain `app`, schema, member order, each member's `session` and `turn_id`, and each member's optional `types` cargo.
- `hint` may change. `at` may change only to the timestamp accepted by live resolution.
- A missing or malformed `at`, unavailable session or turn, timestamp mismatch, changed member, reordering, or changed typed role rejects the write with a diagnostic.
- Records not currently owned by Chatlas pass through untouched.

### Documentation.Reconciliation

- Document the injected validator boundary in the affected project guidance.
- Mark issue 515 resolved by write-time validation while retaining deferred ergonomic and depot-sweep proposals.
- Correct the stale Chatlas Anchory appendix from v1/event identity to v2/turn identity.

## Execution.Plan

### Slice 1 - Atomic generic validator hook

- Add the optional amend validator to Anchory core and command registration.
- RED: a rejecting validator test proves the record is not mutated; a command registrar test proves injection reaches the operation.
- GREEN: generic amend round trips remain unchanged without a validator.
- Status: not started.

### Slice 2 - Chatlas semantic validation

- Add a Chatlas-owned amendment validator with tolerant current-record meaning extraction and strict proposed-record live resolution.
- RED: tests cover missing `at`, wrong `at`, changed members/order/types, and unchanged meaning with corrected metadata.
- GREEN: valid hint-only and timestamp-repair replacements pass.
- Status: not started.

### Slice 3 - Composition-root integration

- Inject the Chatlas validator into generic Anchory command registration in `agentos-cli`.
- RED: an end-to-end CLI test creates a Chatlas record, attempts a corrupt replacement, and proves the stored record is unchanged.
- GREEN: non-Chatlas generic amendments still succeed.
- Status: not started.

### Slice 4 - Reconcile owned documentation

- Update `agentos-py` and `agentos-chatlas-py` guidance, the Chatlas record-format appendix, and issue 515 status/results.
- Check: documentation matches the implemented public boundary and no deferred proposal is reported complete.
- Status: not started.

### Slice 5 - Verification

- Run focused Anchory, Chatlas Anchory, and umbrella CLI tests.
- Run the full suites for `agentos-py`, `agentos-chatlas-py`, and `agentos-cli` if focused checks pass.
- Reproduce issue 515 against an isolated test depot; do not mutate the operator's deliberately broken anchor as part of testing.
- Status: not started.

## Risks And Deviation Triggers

- Existing uncommitted cache and POI work touches the same repositories. Preserve it and stop only if the intended edits cannot be separated safely.
- Validation must occur under the mutation lock. A command-level preflight alone is insufficient.
- Current malformed records must remain repairable when their stable member meaning can be extracted; do not require the current record to resolve before accepting a corrected replacement.
- If the command registrar cannot pass the hook without coupling parser state globally, revise the injection shape and record the deviation here.

## Acceptance Signals

- The missing-`at` and wrong-`at` reproductions fail at `agentos anchory amend`, not later at resolve.
- A replacement that repoints an anchor to another turn is rejected.
- A hint-only correction with unchanged members succeeds.
- Generic non-Chatlas records retain their existing amend behavior.
- Rejected writes leave the original record intact.

## Impl.Log

- Execution gate: autonomous develop invocation ^c20260730-33u
- Design decision: application validation is injected through the generic atomic mutation boundary; generic Anchory does not dispatch on Chatlas schemas itself.
- Design decision: field-level amendment and resolve-aware depot checking are useful follow-ups but do not replace validation of the existing raw replacement surface.
- Pre-existing worktree changes are treated as external concurrent work and preserved.
