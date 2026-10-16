# 524 — Mid-turn user messages were lost in Chatlas normalization

> Live note · resolved issue report · discovered and fixed 2026-08-13

## Summary

Before the fix, user messages sent **while an assistant turn was still executing**
never reached the Chatlas session model as messages. They were not misclassified
under another role: their Claude attachment records fell through to hidden
`session.update` events. Because `Touch.Authority.Surface` is defined as a
qualifying `User.Turn`, the content could not ground an `Index.Line`.

Five design-critical instructions from one working session were lost this way.

## What a mid-turn message is

A turn is one request→response cycle: the user sends input, the assistant works
(possibly for minutes, across many tool calls), then produces a final reply. That
whole span is one assistant turn.

If the user types while that span is running, Claude Code first records a
`queue-operation` enqueue. When it delivers the prompt into the active run, it
records a separate `attachment` whose payload identifies a `queued_command`, its
prompt, command mode, origin, and original timestamp. The harness labels the
delivery explicitly:

> The user sent a new message while you were working. This is how Claude Code
> surfaces messages the user sends mid-turn — within the running turn, often
> alongside the next tool result, rather than as a separate conversation turn.

The attachment occupies its own provider record at the delivery/drain point. It
is not physically embedded in a tool-result record, although delivery commonly
happens beside tool activity. Chatlas originally failed to refine this native
attachment boundary into its own semantic user interaction.

**The trigger is timing, not content.** Identical text becomes a normal user turn
or a mid-turn message depending only on whether the assistant happened to be
running a tool at that instant. Nothing marks the message as second-class from
the user's side.

## Evidence

Session under test:

- `identity_hash`: `6dcfee974c60f0b04de116f644e75cebf7a5b67c69feb160f259e4c4e355221e`
- `session_id`: `6521c5c5-7125-4dc8-8b69-288560d376eb`
- provider: `claude-code`
- project: `/Users/pereiro/projects/pereiros-projects`
- created: `2026-08-12T07:28:38Z`

The test uses **the user's own typos as fingerprints**. Typos cannot appear in
assistant paraphrase, so a zero result cannot be explained by wording drift.

Measured before the fix with
`agentos chatlas turns query --identity-hash <h> --contains <s>`, after a full
`agentos chatlas update` re-index:

| fingerprint | source message | `--turn-kind user` | any role |
|---|---|---|---|
| `becasuse` | split message (mid-turn) | 0 | 0 |
| `ammended` | split message (mid-turn) | 0 | 0 |
| `analisys` | split message (mid-turn) | 0 | 0 |
| `nermal` | "represent … as the nermal model" (mid-turn) | 0 | 0 |
| `do not do the reports now` | reports deferral (mid-turn) | 0 | 0 |
| `use sonnet subagents` | model selection (mid-turn) | 0 | 0 |
| `heve` | normal message | **1** | 3 |
| `most be tracked` | normal message | **1** | — |
| `anotations` | normal message | **1** | 2 |
| `provedance` | normal message | **2** | 2 |

Perfect separation: every mid-turn message tested is absent, every ordinary
message tested is present.

### Ruling out the obvious alternatives

- **Not display truncation.** `turns query` truncates rendered text at 500 chars,
  but `--contains` matches the full body — verified by matching a phrase ~700
  chars into a known turn.
- **Not role misclassification.** The typo fingerprints returned 0 under *every*
  role, not just `user`.
- **Not a stale index.** A full `agentos chatlas update` (35s, whole corpus) was
  run between measurements; results unchanged.
- **Not wording drift.** Fingerprints are the user's own misspellings.

### Reproduction caveat — the test contaminates itself

`becasuse` and `nermal` later returned non-zero under *any* role, resolving to
**assistant** turns timestamped after the investigation began: the agent had
quoted the fingerprints while discussing them. `--turn-kind user` stayed 0
throughout.

Run the fingerprint test **before** naming the fingerprints in conversation, or
scope every query to `--turn-kind user`.

## What was lost in this session

All five arrived mid-turn and are unanchorable:

1. **Normalization represents; the index organizes** — reshaped four index blocks
   in `g70203-pkg` (`Source.Fidelity`, `G70203.Db`, `G70203.Normal.Model`, and the
   new `Application.Index`).
2. **Analysis comes after ingestion** — the rule separating ingest from review.
3. **"Represent the content on the pdfs"** — reframed an entire ingest evaluation.
4. **Defer the checklist reports** — changed the scope of a 40-file pipeline run.
5. **Use Sonnet subagents** — model selection for every batch run that followed.

Six index lines landed ungrounded as a direct result; only 2 of 8 in that capture
could be anchored.

## Why it matters beyond grounding

Anything reconstructed later from Chatlas alone — a session recap, a
`--reconcile` pass, a support-chat audit, `tarav-support-chats --extract` — sees
the assistant adopting major design positions with no user turn preceding them.
The record implies unprompted invention where there was explicit direction.

`tarav-support-chats` already registered this session as mandatory Index support
for `g70203-pkg`. Before backfill, that registry pointed at a normalized transcript
missing the turns that motivated several supported lines. The rebuilt session now
exposes those turns for ordinary grounding and reconciliation.

## Resolution

- Canonical evidence is the delivered `attachment.type=queued_command` record,
  not `queue-operation` bookkeeping. The queue also carries task notifications,
  so queue operations alone cannot establish user-input provenance.
- A prompt-mode, non-meta queued command with human or absent origin normalizes
  as an ordinary visible `message`, `role=user`, `producer=human`.
- The message opens an independent `Normal.Turn::User.Turn` at the attachment's
  raw tape position. Subsequent assistant activity receives the corresponding
  independent assistant grouping.
- Non-human prompt origins, task notifications, and ambiguous queue records stay
  outside `User.Turn`.
- `Touch.Authority.Surface` needs no special case. The repaired event qualifies
  through the ordinary user-turn boundary.
- Existing sessions are backfillable because Claude retained the raw attachment.
  Session-model and delta-checkpoint revisions force semantic rematerialization.

### Backfill verification

The reported session was rebuilt from retained raw data after the fix:

| fingerprint | recovered `User.Turn`s |
|---|---:|
| `becasuse` / `ammended` / `analisys` | 1 shared turn |
| `nermal` | 1 |
| `do not do the reports now` | 1 |
| `use sonnet subagents` | 2 |

The two Sonnet turns are not duplicate normalization: the raw transcript contains
two distinct human queued-command attachments, at 14:47 and 16:02. The session's
task-notification queued attachment produced zero user-turn matches.

## Status

- [x] confirm that the provider transcript retains mid-turn text
- [x] normalize qualifying queued-command attachments as independent user turns
- [x] preserve non-human queue records outside the user-authority boundary
- [x] invalidate old session-model and delta-checkpoint materializations
- [x] rebuild and verify the reported session
