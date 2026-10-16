# Anchory Application-Owned Amendment Validation - impl-req

## Impl.Abstract

- **Scope:** prevent `agentos anchory amend` from writing invalid or meaning-changing Chatlas support-set replacements while keeping generic Anchory application-agnostic.
- **Status:** implemented and verified; one gated appendix reconciliation remains deferred.
- **Source:** issue 515, current implementation inspection, and the autonomous development invocation.
- **Out of scope:** a field-level `--hint` command, `agentos chatlas anchory amend`, resolve-aware `anchory check`, anchor retirement, and changes to `Support.Set` semantics.
- **Support set:** autonomous design and execution authority ^c20260730-33u

## Impl.Agendix

- **Touched (index):** `Anchory.System` - integrating applications own payload meaning; Anchory owns amendment and atomic persistence (`tarav-pkg/design/107-design.md`, `tarav-pkg/appendix/Anchory.System-appendix.md`).
- **Touched (index):** `Chatlas.Anchory` - Chatlas owns `chatlas.support-set.v2`, exact visible-user-turn resolution, and timestamp integrity (`tarav-chatlas-pkg/design/100-design.md`).
- **Touched (chat):** the user authorized autonomous end-to-end development of application-owned amendment validation ^c20260730-33u
- **Structural:** `agentos-cli` is the composition root joining the generic Anchory registrar to Chatlas-owned validation, following the existing Index external-check injection pattern.
- **Touched (implementation):** `agentos-py` now exposes `^anchory-amend-validator` and extends `^anchory-poi-command`, grounded to `Anchory.System`.
- **Touched (implementation):** `agentos-chatlas-py` now exposes `^chatlas-anchory-amend-validation`, grounded to `Chatlas.Anchory`.
- **Touched (implementation):** `agentos-cli` extends `^agentos-cli` as the composition point joining both owned surfaces.
- **Open space:** support meaning is provisionally the ordered member identity and `types` cargo. `hint` and a validated `at` are repairable metadata.

## Impl.Index

### Anchory.Amend.Validator

- `AnchoryDepot.amend` accepts an optional application validator and invokes it under the exclusive depot lock after reading the current record and before writing the replacement.
- The validator receives the depot root plus the current and proposed normalized records; generic amendment remains unchanged when no validator is supplied.
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
- Route the stale Chatlas Anchory appendix from v1/event identity to v2/turn identity through its separate Index edit gate.

## Execution.Plan

### Slice 1 - Atomic generic validator hook

- Add the optional amend validator to Anchory core and command registration.
- RED: a rejecting validator test proves the record is not mutated; a command registrar test proves injection reaches the operation.
- GREEN: generic amend round trips remain unchanged without a validator.
- Status: done; 18 focused Anchory tests pass.

### Slice 2 - Chatlas semantic validation

- Add a Chatlas-owned amendment validator with tolerant current-record meaning extraction and strict proposed-record live resolution.
- RED: tests cover missing `at`, wrong `at`, changed members/order/types, and unchanged meaning with corrected metadata.
- GREEN: valid hint-only and timestamp-repair replacements pass.
- Status: done; 16 focused Chatlas Anchory tests pass.

### Slice 3 - Composition-root integration

- Inject the Chatlas validator into generic Anchory command registration in `agentos-cli`.
- RED: an end-to-end CLI test creates a Chatlas record, attempts a corrupt replacement, and proves the stored record is unchanged.
- GREEN: non-Chatlas generic amendments still succeed.
- Status: done; 8 focused umbrella Anchory tests pass.

### Slice 4 - Reconcile owned documentation

- Update `agentos-py` and `agentos-chatlas-py` guidance, the Chatlas record-format appendix, and issue 515 status/results.
- Check: documentation matches the implemented public boundary and no deferred proposal is reported complete.
- Status: partially done; project guidance and issue 515 match the implementation. The accepted Chatlas Anchory appendix correction is deferred to its separate Index edit gate.

### Slice 5 - Verification

- Run focused Anchory, Chatlas Anchory, and umbrella CLI tests.
- Run the full suites for `agentos-py`, `agentos-chatlas-py`, and `agentos-cli` if focused checks pass.
- Reproduce issue 515 against an isolated test depot; do not mutate the operator's deliberately broken anchor as part of testing.
- Status: done; touched-file Ruff checks pass, full suites pass (`agentos-py` 592, `agentos-chatlas-py` 277, `agentos-cli` 71), and the installed CLI rejects the isolated missing-`at` reproduction without mutation.

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
- Autonomous deviation: the initial callback shape lacked depot context. It now receives the exact depot root so Chatlas validation resolves against the owning dataset rather than assuming the global default.
- Autonomous deviation: the planned accepted-appendix correction requires a separate verbatim Index approval token. The implementation workflow did not supply that gate, so the edit was reverted and remains reconciliation debt.
- Verification note: repository-wide Ruff is not a usable baseline because `_DEPRECATED/` and an unrelated development script currently produce 584 pre-existing findings. Ruff check and format pass on every touched Python file.
- Installed-CLI reproduction: missing-`at` amendment exited 1 with the resolve-grade diagnostic, and a fresh read confirmed the original hint and timestamp remained stored.
