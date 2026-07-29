# agentos-hugentics --back-link

> $kw: --from Demoted.Index.Line --from Edition.Trigger.User.Gated --from Gr.Req --from Index.Presumption --from Support.Set --from Touch.Authority.Surface --from Touched.Data --from Verbatim.User.Gated --from Workflow.Neutral
> --dev-from references/index-context-assembly.skw.md

Use this module when the caller wants an existing index block grounded backward: from the block as written, through git history, to the chat turns that produced it.

This is the archaeology counterpart of `references/link.md`: `--link` builds support for content being produced now; `--back-link` recovers evidence for content written in the past. Both produce a verified support reference whose index landing remains gated.

This module is `Workflow.Neutral` in the same sense as `--link`: it produces verified anchors; the index write at the end goes through `--edit` and its gates.

The current archaeology path recovers `Touched.Data` from a qualifying `Touch.Authority.Surface` edition, builds a `Support.Set`, and routes the live change through `Edition.Trigger.User.Gated` plus `Verbatim.User.Gated`.

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
   - use `agentos chatlas events query --identity-hash <H> --pattern-json '<Event.Pattern JSON>' --backend auto` to retrieve authoritative `Event.Ref` objects for distinctive user wording or an assistant-proposal/user-approval pair
   - use the commit time only to choose among candidate neighborhoods; `turn_id` establishes turn identity and `sequence` establishes tape order — never timestamps
   - select only a user turn whose edition qualifies as touch for the supported subject; approval, correction, rejection, delegation, or direct statement may qualify
4. **Turn → anchor.** Mint through the linking primitive (`references/link.md` step 3): `agentos chatlas anchory register --member <H>:<user-turn-id> --hint "…"`; when the recovered evidence is an approval pair, add the appropriate `--member-types` cargo. Read the echo and confirm the neighborhood.
5. **Support reference → index.** USER-GATED: show the proposed inline support change through `--edit` and write only after the gate. Steps 1–4 build plumbing; step 5 changes the live index.

> $kw. end

## Judgment Points

- the commit dates the *write*; the *evidence* is earlier — search around and before the commit time, not at it
- a block repaired, migrated, or reworded later still grounds on the original design discussion: follow `git log -L` past mechanical commits to the content-bearing ones
- multiple sessions may shape one line; reinterpretation creates a new support reference, while source and Git history preserve prior network states
- changing or dropping a support reference does not itself create `Demoted.Index.Line`; demotion requires a gated reconciliation that retires the line's live standing
- when wording originated agent-side, the qualifying user approval or correction turn is the primary touched-data source; anchor it and describe what it covered
- no honest support found is a finding, not a failure; the live line remains ungrounded and carries `Index.Presumption` rather than gaining a weak link

## Batch Behavior

- a back-linking campaign lives in a `Gr.Req` live note (`NNN-…-gr-req.md`): one `Gr.Set` entry per grounding target — anchor, evidence, landing form, status (`ambiguous` → `proposed` → `landed`|`dropped`); the user gates by flipping statuses on `proposed` entries
- every write remains individually user-gated — batch discovery, per-line verbatim proposal, user-approved landing
