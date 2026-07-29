# agentos-hugentics --capture

> $kw: --from Agentos.Index.System --from Alignment.Mode --from Capture.Gradient --from Capture.Offer --from Edition.Approval.Token --from Edition.Trigger.User.Gated --from Index.Edition.Turn --from Index.Presumption --from Kernel.Writing --from Line.Verbatim.Gate --from Live.Index.Line --from Not.A.Wall.Of.Text --from Open.Inference --from POI.Instance --from Support.Set --from Touch.Authority.Surface --from Touched.Data --from Touched.Decision.Cycle --from Touched.Index --from User.Command --from User.Command.Arg --from Verbatim.User.Gated --from Workflow.Neutral
> --dev-from references/index-context-assembly.skw.md

Use this module when the user wants the chat's content worked into kernel writing form and landed on index surfaces — "let's capture".

This module is a workflow module: it takes control of the session and runs the capture loop. Load the whole `references/index-capture-context.md` module before the first grounding pass. The surfaces capture lands on are governed by `Workflow.Neutral` knowledge modules — `references/edit.md` for the ontology and appendix, `references/agendix.md` for the agendix.

`Capture.Offer` is the same act at single-candidate scale: agent-initiated, one draft, same destination semantics. This module is the user-initiated, whole-conversation form.

Load `references/touched-data.md` for authority and line standing, and `references/decision-cycle.md` for contextualize-act-reconcile. The current chat protocol supplies qualifying user turns and Chatlas support records; it does not make chat the conceptual boundary of `Touched.Index`.

Operationally, capture applies `Touched.Decision.Cycle` to `Touch.Authority.Surface` editions and adjacent evidence. It distinguishes `Touched.Data`, `Support.Set`, `Live.Index.Line`, `Open.Inference`, and `POI.Instance` while producing `Kernel.Writing` for the current `Agentos.Index.System` realization.

## The Capture Loop

A pass over the chat's uncaptured content, repeated until the content is exhausted or the user stops:

1. **Contextualize / Assemble.** Load `Index.Capture.Context.Module`, including the touched-data and decision-cycle modules.
2. **Contextualize / Discover.** Resolve engaged depots, live line standing, authority-surface evidence, and adjacent non-touch evidence.
3. **Contextualize / Ground.** Treat only qualifying user-turn editions as direct touched data. Follow existing support references when the digest is insufficient; preserve ungrounded live lines as `Index.Presumption`.
4. **Contextualize / POIs.** Make gaps, contradictions, ambiguity, stale projections, and missing grounding explicit before choosing a capture move.
5. **Act / Map.** Build an internal candidate map covering overlap, dependencies, natural edit actions, possible destinations, and POIs that may legitimately remain unresolved.
6. **Act / Roadmap.** In `Interactive` mode, present the small public `Capture.Roadmap`: likely block or edit clusters and one sentence explaining each.
7. **Act / Focus.** Select one block or small coherent cluster. The user may redirect, reorder, remove, or add candidates through natural conversation.
8. **Act / Propose + Discuss.** Codesign only the foreground cluster, then present a typed, landing-targeted `Index.Edition.Turn`.
9. **Act / Approve.** User approval records the current proposal as approved but unlanded. Approved material accumulates while review moves to the next cluster.
10. **Reconcile / Land + Re-ground.** A separate user command lands selected approved material, then re-contextualizes against the changed live cut and support network.

`Autonomous` mode performs the same preparation and internal mapping but does not present a roadmap or run the review loop; it proceeds through its agendix-only landing path.

Destinations occupy different positions on `Capture.Gradient`; ontology and appendix wording remains `Verbatim.User.Gated`, while the agendix is grounded but unreviewed.

## Capture.Roadmap

`Capture.Roadmap` is an attention-budgeted index of what a good candidate capture session would cover. It is a selective projection of the internal candidate map, not an evidence report or exhaustive backlog.

- list likely block or edit clusters in a useful review order
- identify the relevant block or intended edit with one short sentence explaining the capture move
- prefer names and terse pointers for concepts already present in the user's context; add a gloss only when a name would not resolve clearly
- omit evidence inventories, source lists, uncertainty columns, and destination detail unless one materially changes the proposed session
- recommend the first focus without presenting every candidate as a full draft
- keep the roadmap provisional: natural conversation may reshape it at any time

The roadmap is not approval-ready material. Do not expose `::approve` merely because a roadmap is foregrounded; that command becomes available only after one concrete draft and landing target are presented.

## Index.Edition.Turn

An approval-ready turn optimizes the user's ability to distinguish the proposed change:

- identify `Landing`, `Target`, edit operation, and `Edition.Approval.Token`
- for a modification, show current content under `Before` and proposed content under `After · Verbatim`
- for an addition, show the proposed content; for a removal, show the current content
- show unchanged context only when it improves interpretation
- place each proposed landing line undecorated somewhere in the turn
- treat this rendering as user experience, not linter syntax; headings, order, fences, and diff notation may evolve

## User.Command Checkpoints

- These checkpoints apply the skill's declared `User.Command` transitions and resolve each required `User.Command.Arg` against the foreground capture state.
- When an approval-ready draft becomes foreground, mint a fresh opaque `Edition.Approval.Token`, show it in the same assistant turn as the proposed landing content, and pause with the resolved `::approve <token>` command (`::approved` equivalent). The command approves that presented edition and never writes it.
- The token identifies one proposal and may cover several lines. Reuse it while materially significant wording and the landing target hold; presentation-only changes do not require a new attention checkpoint.
- Do not offer or use bare `::approve` in this workflow. If the user gives it anyway, explain that it records at most semantic edit-event approval, leave the draft approval-ready, and reprint the exact `::approve <token>` command required to satisfy `Line.Verbatim.Gate`.
- Approval adds the resolved draft to the approved, unlanded cluster and returns the loop to **Focus**. When roadmap candidates remain, the default next move is to codesign and present the next approval-ready draft, not to pause for landing.
- An explicit `::land [target]` (`::write` equivalent) remains valid whenever its approved target resolves clearly, including before the workflow suggests it.
- `::land-all-approved` takes no target argument and lands the complete approved, unlanded cluster of the single foreground index workflow.
- Suggest landing at a deliberate landing pause: when the roadmap is exhausted, when the approved cluster is significant and coherent enough to land together, or when the user asks to land or requests status.
- Do not create a landing pause solely because the first draft entered the approved cluster.
- A bare targeted command may resolve its contextual target only when one foreground target is possible. If several drafts or approved sets could receive it, ask which one and leave every transition unresolved.
- `::land-all-approved` removes target ambiguity, not workflow ambiguity: if several workflows could supply the approved cluster, ask which workflow is foreground and leave every transition unresolved.
- Free-form replies continue the discussion without crossing either gate. If discussion changes an approved draft's wording or landing target, return that draft to approval-ready state.
- Print the available command line only at a real pause or on a status request. Do not append it to ordinary conversational turns.
- Render each command in resolved, copy-pasteable form: pre-fill the token or target from foreground state. Use template placeholders only when nothing resolves yet.
- When several drafts are approval-ready, print each proposal's distinct token command on its own line. The user disambiguates by echoing one token.

Example review pause footer:

```text
Available User.Commands:
  ::approve idx-edition:7d2f91c4  approve the presented Background.Job proposal
  ::approve idx-edition:3a84e6d2  approve the presented Serialized.Lane proposal
```

Example landing pause footer:

```text
Available User.Commands:
  ::land Agentos.Daemon  write this approved item (also ::write)
  ::land-all-approved    write the whole approved cluster
```

## Mode

- capture accepts `Alignment.Mode` — `Interactive` (default) or `Autonomous`
- `Interactive` presents the roadmap, then runs the focused codesign loop: checkpoints are alignment opportunities, discussion and approval happen per small cluster
- `Autonomous` runs without user prompting: the loop collapses to ground → propose → land → report, and it can land only on the agendix — a user gate (`Edition.Trigger.User.Gated`) cannot be resolved autonomously
- `--AUTO` is the extreme case as a flag: the full workflow automatic, chat to agendix, the invocation is the one trigger that covers the pass
- `--agendix` presets the agendix destination and defaults to `Autonomous`; the user engaging mid-pass simply is `Interactive`

## Landing

> $kw: --derived
> --from references/edit.skw.md#Landing Procedure
> --from references/agendix.skw.md#Landing Form
> --intent digest the two landing paths into the routing summary capture needs:
> --cont gate semantics per surface and the form-fit move; do not restate the
> --cont procedures — the knowledge modules own them

Landing form-fits material to the named surface under that surface's own gate. Approval-ready candidates show the concrete `Landing`, `Target`, operation, and proposed content; the destination may remain loose only while discussion is exploratory.

- **ontology / appendix** — token approval establishes reviewed content, while a separate landing command executes the gated edit; the approval turn enters the line's support set only when it qualifies under the current chat authority protocol
- **agendix** — one user trigger covers the pass without per-line review; each line still lands typed and grounded through a resolvable support set under a routed concept or provisional path
- every landing updates the live cut; capture re-contextualizes afterward and reports remaining POIs without treating them as automatic edits

> $kw. end

## Behavior

- the discussion is free: capture is pulled by the user, never a standing obligation on the conversation — not every discussion involves blocks
- `Not.A.Wall.Of.Text` governs the loop: the opening turn may show the broader `Capture.Roadmap`, but not the context-assembly load or evidence inventory; after orientation stay on one block or small coherent cluster, never re-dump the full harvest
- after approval, continue directly to the next roadmap cluster while the approved material accumulates; landing is a batch checkpoint rather than the default response to each approval
- after a write, refresh the internal map; show only a compact roadmap delta unless the session's big picture materially changed
- know what is approved and unlanded at any moment — the conversation itself is the record; no tracking mechanism is required
- never silently delete, demote, or rewrite a contradictory live line; capture may propose reconciliation, while the landing gate controls the surface change
- material not worth the full hugentic review can always take the agendix exit rather than staying stranded in chat
- load `references/type.md` before drafting lines and `agentos-pkg/references/index-block-catalog.md` before proposing block wording
