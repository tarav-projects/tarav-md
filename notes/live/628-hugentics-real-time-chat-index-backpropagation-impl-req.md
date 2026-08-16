# Hugentics Real-Time Chat.Index Backpropagation - impl-req

## Impl.Abstract

- **Status:** Implemented and verified.
- **Scope:** Make `Index.HEAD.Backpropagation` a normal postcondition of Hugentic `Real.Time.Capture`: every successfully landed, current-chat-backed Index line is projected to `Chat.Index.HEAD`, then best-effort materialized on the chronological `Chat.Index.Delta` tape through Chatlas2 `Chat.Message.Ref` and `Chat.Turn.Ref` evidence.
- **Source alignment:** The accepted flow is `Other.HEADs -> Chat.Index.HEAD -> Chat.Index.Delta tape`. `Chat.Index` is not a direct Hugentics capture target. Real-time capture need not complete the chat index; it backpropagates the exact editions it lands while live `User.Attention` and exact support are available.
- **Targets:** `tarav-py/src/tarav/chatlas2/` and tests; managed `tarav-md/skills/tarav-hugentics/.skw/src/` plus compiled runtime surfaces.
- **Out of scope:** Background reconciliation and gap filling, the separate `tarav-chatlas-pkg --capture --session` route, whole-transcript reconstruction, migration mechanics for existing Chatlas1 Chat.Index surfaces, and completeness claims for Chat.Index.
- **Acceptance:** A Hugentic landing can batch already-grounded exact lines into one Chatlas2 Capture.Plan; validation derives chronological origins from their dossiers; apply updates Chat.Index.HEAD unconditionally, appends stable Delta receipts when a current-session origin resolves, reports head-only gaps otherwise, and repeats idempotently.

## Impl.Index

### Real.Time.Capture

- `Real.Time.Capture` is the `User.Attention`-adjacent Hugentic workflow family that lands semantic change from the loaded chat.
- The loaded conversation remains the understanding source. Chatlas2 is consulted after line support is selected, for exact message identity, containing-turn identity, and drift validation.
- `Index.HEAD.Backpropagation` runs only after the primary landing succeeds. It never manufactures chat history for an unrelated maintenance edit.

### Backpropagation.Contract

- Every exact line successfully landed by current-chat capture is placed on that chat's `Chat.Index.HEAD`.
- The line's `Support.Set` supplies candidate chronological origins. The latest support message belonging to the target session selects its containing `Chat.Turn.Ref`; batched lines may share the latest such horizon.
- A Delta says only what is supported within its horizon. The workflow makes no completeness claim about the turn, chat, HEAD, or tape.
- Delta materializations are stable receipts. Later HEAD changes create later materializations; they do not rewrite earlier receipts.
- When no current-session support member can be placed on the tape, the exact line remains on Chat.Index.HEAD and apply reports a recoverable backpropagation gap.

### Capture.Plan

- Preserve Capture.Plan as the batching boundary, but give the Chatlas2 path a narrow real-time schema rather than porting Chatlas1 semantics blindly.
- `scaffold` binds one exact session and fingerprints the current descriptor-free Chat.Index surface.
- The agent fills the plan with exact already-landed line content, concept attachment, and Chatlas2 line anchor. Support, gates, and predecessor relationships remain authoritative in the line dossier rather than being duplicated in the plan.
- `validate` resolves every dossier, verifies the attachment triplet, derives containing turns and planned HEAD/Delta effects, and refuses a stale base.
- `apply` repeats validation under a session lock, performs a recoverable directory replacement, and returns an audit of exact HEAD and Delta presence plus any head-only gaps.

### Surface.Update

- Retain the descriptor-free `HEAD.md` plus `deltas/` layout.
- HEAD maintenance is incremental and partial: preserve unrelated blocks, remove predecessor anchors declared by the new dossier, and upsert the exact new anchored line.
- Delta files are keyed by both `turn_address` and `turn_hash`, keeping a captured observation stable even if a provider later amends the same event place.
- The current Chatlas2 turn ref and diagnostic time are rendered explicitly. Existing unrelated files are preserved; this path does not claim to migrate or reinterpret prior Chatlas1 Deltas.

## Impl.Agendix

- **Execution authorization:** generic Chatlas2 support anchor `d20260816-39u` on the explicit autonomous implementation request.
- **Current grounding implementation:** `notes/live/627-hugentics-current-chat-grounding-impl-req.md` and the managed Hugentics capture/link/design-session sources.
- **Chatlas2 primitives:** `src/tarav/chatlas2/anchory.py`, `cache.py`, `turn_ref.py`, `turns.py`, and `commands.py`.
- **Reusable mechanics under review:** current Chatlas `chat_index_plan.py`, `chat_index_render.py`, and `chat_index_apply.py`; reuse ideas and low-level helpers only where they fit the accepted real-time contract.

## Execution.Plan

### Vertical.Slice.1 - Chatlas2 backpropagation model and RED tests

- **Status:** Complete.
- **RED:** Add focused tests proving that no Chatlas2 Capture.Plan/surface path currently projects an anchored landed line to HEAD and its containing-turn Delta.
- **GREEN:** Implement the narrow plan parser, exact dossier/turn resolution, partial HEAD update, stable Delta receipt, base fingerprint, and head-only gap result.
- **Checks:** Focused unit tests cover create, multi-line batching, predecessor replacement, missing local origin, stale base refusal, and idempotent repeat.

### Vertical.Slice.2 - Recoverable application and CLI

- **Status:** Complete.
- **RED:** Extend the CLI test to call an absent `chatlas2 chat-index scaffold|validate|apply` path.
- **GREEN:** Expose the three operations, lock and revalidate apply, install through recoverable replacement, and return structured effects/audit.
- **Checks:** End-to-end synthetic Codex session test verifies materialized Markdown, exact anchors, Chat.Turn.Ref metadata, repeated no-op behavior, and cache-backed reads.

### Vertical.Slice.3 - Hugentics Real.Time.Capture integration

- **Status:** Complete.
- **RED:** Confirm the runnable capture module still treats chronological Chat.Index work as later reconciliation and retains a Chatlas1 Capture.Plan dependency.
- **GREEN:** Update managed Skillware sources so every successful current-chat semantic landing batches `Index.HEAD.Backpropagation` after primary landing: scaffold, fill exact landed lines, validate, apply, and report head-only gaps without blocking the primary landing.
- **Checks:** Rebuild the package; inspect compiled capture, root literacy, target landing summary, and direct loading context; run Skillware check and context projection.

### Vertical.Slice.4 - Reconciliation and regression

- **Status:** Complete.
- **GREEN:** Update `tarav-py/AGENTS.md` for the new Chatlas2 consumer surface and update this artifact with results and deviations.
- **Checks:** Run focused Chatlas2 tests, the complete `tests/chatlas2` suite, Ruff on touched Python, `tarav skw check`, and `git diff --check` in both repositories.

## Impl.Log

- **2026-08-16:** Designed from the accepted `Real.Time.Capture`, `Index.HEAD.Backpropagation`, partial Chat.Index, and `Other.HEADs -> Chat.Index.HEAD -> Index.Tape` discussion. Execution authorization is grounded at `d20260816-39u`.
- **2026-08-16 — checkpoint:** Before implementation, checkpointed the two active repositories at `tarav-py@b4e3e78` and `tarav-md@24f0c4b` as required by the autonomous development workflow.
- **2026-08-16 — slice 1:** Added the narrow Chatlas2 real-time Capture.Plan and descriptor-free Chat.Index applicator. Validation resolves exact line dossiers, checks current message state, derives containing user turns conservatively, sends every line to HEAD, and batches eligible lines at the latest proven local horizon. Focused RED/GREEN coverage proves stable receipts, predecessor replacement, head-only gaps, stale-base refusal, and idempotence.
- **2026-08-16 — slice 2:** Added `tarav chatlas2 chat-index scaffold|validate|apply`, per-session locking, revalidation under lock, recoverable directory replacement, and post-write audit. The installed editable CLI exposes the route and the synthetic end-to-end test repeats with no second mutation.
- **2026-08-16 — slice 3:** Rebuilt the managed Hugentics Skillware so shared capture, ontology/appendix landing, agendix, and design-session paths treat `Index.HEAD.Backpropagation` as a postcondition of successful current-chat landing. The compiled path uses Chatlas2 only; Chat.Index is a co-projection rather than a direct landing target.
- **2026-08-16 — verification:** `uv run pytest tests/chatlas2 -q` passes 79 tests; Ruff and both repository diff checks pass. Skillware build reports no findings and its context projection reaches the new real-time contract. Skillware check retains only six pre-existing `Derived.Stale` advisories in unrelated alignment and implementation modules.
- **Deviation:** Existing Chatlas1 Chat.Index files are preserved as opaque unrelated surface material. This implementation neither migrates nor reinterprets historical files; the accepted real-time Chatlas2 path begins producing exact current-chat projections and receipts while background reconciliation remains separate.
