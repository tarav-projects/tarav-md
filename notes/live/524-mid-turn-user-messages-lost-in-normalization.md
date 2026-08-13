# 524 — Mid-turn user messages are lost in Chatlas normalization

> Live note · issue report · discovered 2026-08-13

## Summary

User messages sent **while an assistant turn is still executing** never reach the
Chatlas session model. They are not misclassified — they are absent under every
role. Because `Touch.Authority.Surface` is defined as a qualifying `User.Turn`,
this content can never ground an `Index.Line`, no matter how consequential it was.

Five design-critical instructions from one working session were lost this way.

## What a mid-turn message is

A turn is one request→response cycle: the user sends input, the assistant works
(possibly for minutes, across many tool calls), then produces a final reply. That
whole span is one assistant turn.

If the user types while that span is running, Claude Code does not queue the text
until the turn ends. It injects it into the **already-running** turn, piggybacked
onto the next tool result. The harness labels this explicitly:

> The user sent a new message while you were working. This is how Claude Code
> surfaces messages the user sends mid-turn — within the running turn, often
> alongside the next tool result, rather than as a separate conversation turn.

So the text physically arrives inside an assistant turn's tool-result stream,
never opening a user-turn boundary of its own.

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

Measured with `agentos chatlas turns query --identity-hash <h> --contains <s>`,
after a full `agentos chatlas update` re-index:

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
`--reconcile` pass, a support-chat audit, `agentos-support-chats --extract` — sees
the assistant adopting major design positions with no user turn preceding them.
The record implies unprompted invention where there was explicit direction.

`agentos-support-chats` already registered this session as mandatory Index support
for `g70203-pkg`. That registry now points at a transcript missing the turns that
motivated several of the lines it supports.

## Open questions for the fix

- Does the provider transcript retain the text at all, or is it dropped before
  Chatlas sees it? Determines whether this is recoverable for past sessions or
  only fixable going forward.
- If retained: should a mid-turn message be promoted to its own `User.Turn`, or
  recorded as a distinct event kind within the assistant turn?
- If promoted, where does it sit in tape order — at injection point, or at the
  end of the turn it interrupted?
- Should `Touch.Authority.Surface` qualification extend to mid-turn user content
  once it is representable? It is genuine user touch by every criterion except
  its container.
- Is there a backfill path for sessions already captured?

## Status

- [ ] confirm whether the provider transcript retains mid-turn text
- [ ] decide the normalization target shape
- [ ] fix the capture path
- [ ] decide backfill for existing sessions
