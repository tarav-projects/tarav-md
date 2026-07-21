# agentos-index --back-link

> $kw: --from Demoted.Anchored.Line --from Edition.Trigger.User.Gated --from Gr.Req --from Grounding.Hugentic.Authority --from Verbatim.User.Gated --from Workflow.Neutral

Use this module when the caller wants an existing index block grounded backward: from the block as written, through git history, to the chat turns that produced it.

This is the archaeology counterpart of `references/link.md`: `--link` anchors content being produced now (edge linking); `--back-link` recovers evidence for content written in the past. Both end in the same place — an anchor and a gated `[GR]` line.

This module is `Workflow.Neutral` in the same sense as `--link`: it produces verified anchors; the index write at the end goes through `--edit` and its gates.

## Back-Link Pipeline

> $kw: --derived
> --from references/link.skw.md#Linking Pipeline
> --intent invert the linking pipeline for archaeology: block→time (git log -L),
> --cont time→session (truth tiers), session→turn (vocabulary search around the
> --cont commit), then mint through link's registration step; landing stays gated

1. **Block → time.** Git history dates the block's current wording:
   - `git log -L "/## Concept.X/,/^\*\*\*\*/:<chapter-file>" --format="%h %aI %s"` — the commits that shaped the block, newest first
   - the newest content-bearing commit's timestamp is the write moment; the design discussion precedes it (often by hours)
2. **Time → session.** Find who wrote it, escalating through the truth tiers:
   - semantic: `agentos chatlas query --file-write "<chapter-file basename>"` — precise, but misses command-string writes (Bash heredocs)
   - recall: `agentos chatlas query --tool-contains "<chapter-file basename>" [--tool-name Bash]` — total coverage, no verb claim
   - content: `agentos chatlas query --message-contains "Concept.X"` — sessions that discussed the concept by name
3. **Session → turn.** Search the tape with the block's own vocabulary, biased toward the write moment:
   - `agentos chatlas views inline --identity-hash <H> --contains "<distinctive block wording>" --role user --around "<commit time>" --radius 6 --filter turns`
   - the user turn that proposed, corrected, or accepted the block's content is the landing point; `Grounding.Hugentic.Authority` applies — user turns primarily
4. **Turn → anchor.** Mint through the linking primitive (`references/link.md` step 3): `agentos chatlas anchory register --identity-hash <H> --at "<turn time>" --hint "…"` — read the echo, confirm the neighborhood.
5. **Anchor → index.** USER-GATED: show the proposed `[GR]` line verbatim in chat and write only on explicit user approval (`Edition.Trigger.User.Gated`, `Verbatim.User.Gated`, via `--edit`). The landing is an inline trailing anchor on the line(s) the turn supports. Steps 1–4 are free; step 5 never is.

> $kw. end

## Judgment Points

- the commit dates the *write*; the *evidence* is earlier — search around and before the commit time, not at it
- a block repaired, migrated, or reworded later still grounds on the original design discussion: follow `git log -L` past mechanical commits to the content-bearing ones
- multiple sessions may have shaped one block (design + migration + revision): ground the current wording; a superseded anchor is simply dropped — the edge demotes (`Demoted.Anchored.Line`), git keeps the history
- approval-turn authority: index content lands through gated verbatim proposals — when no design-discussion turn exists, the user's approval turn ("write"/"apply" following the shown text) IS the grounding authority (`Grounding.Hugentic.Authority`: assistant material accepted or acted on); anchor the acceptance, hint it as such
- relatedness gate as always: no supporting turn found is a finding, not a failure — an ungrounded block stays ungrounded rather than gaining a weak link

## Batch Behavior

- a back-linking campaign lives in a `Gr.Req` live note (`NNN-…-gr-req.md`): one `Gr.Set` entry per grounding target — anchor, evidence, landing form, status (`ambiguous` → `proposed` → `landed`|`dropped`); the user gates by flipping statuses on `proposed` entries
- every write remains individually user-gated — batch discovery, per-line verbatim proposal, user-approved landing
