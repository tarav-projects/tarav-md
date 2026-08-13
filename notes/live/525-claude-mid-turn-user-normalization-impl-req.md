# 525 — Claude mid-turn user normalization implementation request

## Impl.Abstract

- status: completed
- scope: preserve Claude Code human mid-turn prompts as ordinary visible Chatlas user messages and independent `Normal.Turn::User.Turn` groupings
- source issue: `notes/live/524-mid-turn-user-messages-lost-in-normalization.md`
- implementation target: `agentos-py/src/agentos/chatlas/`
- out of scope: synthesizing user authority from `queue-operation` records, changing non-human queued commands, or redesigning provider-independent turn semantics
- execution authority: ^c20260813-3u

## Impl.Index

### Provider evidence

- Claude retains a delivered mid-turn prompt as an `attachment` record whose attachment has `type=queued_command`, `commandMode=prompt`, and human or absent origin.
- The same provider queue also carries task notifications. `queue-operation` therefore cannot independently prove user-input provenance.
- The attachment occupies its own raw chronological position and carries stable raw provenance. It is the canonical normalization source for the delivered prompt.

### Normal-model commitments

- `Session.Event.Tape` preserves provider recording chronology; the queued prompt is placed at the attachment record position.
- `Normal.Turn::User.Turn` represents data supplied in one user interaction and may contain attachments.
- `User.Turn.Purity` admits only positively attributable user-input data. A prompt-mode queued command qualifies; task notifications and ambiguous queue bookkeeping do not.
- The native attachment boundary is refined into an independent user interaction. Later assistant activity receives the corresponding independent assistant grouping.
- No consumer-specific authority exception is needed: downstream authority follows from the ordinary normalized user turn.
- `Session.Model.Artifact` freshness depends on normalizer/model revisions, not only raw artifact timestamps.

### Implementation design

- Add one small Claude predicate that recognizes qualifying queued user input.
- Make the Claude event assembler open an interaction on that record and normalize it as a visible `message`, `role=user`, `producer=human`, with visible model input and preserved attachment-native metadata.
- Keep all non-qualifying attachment and queue-operation records on the existing hidden session-update path.
- Keep lineage branch detection from treating Claude's dead-end attachment leaf as a conversation continuation.
- Reuse event-to-message projection so legacy message projections remain consistent automatically.
- Bump the Claude normalizer identifier, the session-model materialization revision, and the delta-checkpoint schema so no frozen v1 prefix survives the semantic change.

## Execution.Plan

1. **Vertical.Slice::Regression boundary — completed**
   - Add a Claude normalization test containing ordinary assistant activity, a human prompt-mode queued attachment, later assistant activity, and non-human queued attachments.
   - RED: the human prompt is absent from visible user events and no independent user turn exists.
   - GREEN signal: exactly the qualifying attachment becomes a human user message at its raw position; task notification and non-human variants remain excluded.
   - Check: focused Claude normalization tests.

2. **Vertical.Slice::Normalizer — completed**
   - Implement the qualifying predicate, interaction boundary, event mapping, and branch-analysis exclusion.
   - Check event payload, producer, surfaces, source refs, timestamp, turn identity, order, and following assistant grouping.
   - Check full Claude normalization suite.

3. **Vertical.Slice::Freshness and delta safety — completed**
   - Invalidate existing session-model artifacts and Claude delta checkpoints through revision changes.
   - Update assertions that expose those revision identifiers.
   - Check cache and delta-normalization suites.

4. **Vertical.Slice::Issue resolution and backfill proof — completed**
   - Update note 524 with provider evidence, accepted semantics, and completed status.
   - Rebuild the reported session from retained raw data.
   - Verify the original typo fingerprints resolve as `User.Turn`s and confirm no task-notification promotion.
   - Run the relevant Chatlas test group and review the diff.

## Risks And Deviation Triggers

- If observed attachment shapes cannot distinguish human prompts from provider-generated queue entries, stop promotion for the ambiguous shape rather than weakening `User.Turn.Purity`.
- If a delta rebuild can reuse an old frozen event prefix despite revision changes, force full derivation for stale revisions before accepting the backfill.
- If the attachment record does not precede the assistant activity it semantically influences in real raw order, preserve raw tape chronology and record the mismatch instead of repositioning events synthetically.

## Acceptance Signals

- All five reported mid-turn instructions are visible normalized user messages and independent user turns after rebuild.
- Existing ordinary Claude messages, tool records, compact summaries, and task notifications retain their current semantics.
- Cold and delta derivations agree after the new checkpoint revision.
- Relevant tests pass and no unrelated diff is introduced.

## Impl.Agendix

- execution gate: ^c20260813-3u
- `Session.Event.Tape`: `skills/agentos-chatlas-pkg/design/100-design.md`
- `Normal.Turn`: `skills/agentos-chatlas-pkg/design/100-design.md`
- `User.Turn.Purity`: `skills/agentos-chatlas-pkg/design/100-design.md`
- `Session.Model.Artifact`: `skills/agentos-chatlas-pkg/design/100-design.md`
- `Normalization.Pipeline::Chatlas.Session.Model`: `skills/agentos-chatlas-pkg/design/100-design.md`

## Impl.Log

- 2026-08-13 — execution authorized for autonomous development. ^c20260813-3u
- 2026-08-13 — no design-reality deviations. Full and delta normalization share the queued-user mapping; legacy artifacts and checkpoints are invalidated by revision.
- 2026-08-13 — reported session rebuilt successfully: every issue fingerprint resolves through user turns, two distinct Sonnet submissions remain distinct, and the task notification remains excluded.
- 2026-08-13 — complete Chatlas suite: 494 passed; Ruff semantic checks passed. Whole-file format drift predates this change and was left untouched.
