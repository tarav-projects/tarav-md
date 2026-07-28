# agentos-index --capture

Use this module when the user wants the chat's content worked into kernel writing form and landed on index surfaces — "let's capture".

This module is a workflow module: it takes control of the session and runs the capture loop. Load the whole `references/index-capture-context.md` module before the first grounding pass. The surfaces capture lands on are governed by `Workflow.Neutral` knowledge modules — `references/edit.md` for the ontology and appendix, `references/agendix.md` for the agendix.

`Capture.Offer` is the same act at single-candidate scale: agent-initiated, one draft, same destination semantics. This module is the user-initiated, whole-conversation form.

Authority lives in the index: `Agentos.Index.System`, `Hugentic.Concept`, `Kernel.Writing`, `Grounding.Hugentic.Authority`, `Workflow.Neutral` own the concepts.

## The Capture Loop

A pass over the chat's uncaptured content, repeated until the content is exhausted or the user stops:

1. **Assemble.** Load `Index.Capture.Context.Module`: the complete operational model and task-relevant knowledge categories needed to work across the touched index.
2. **Discover.** Resolve the engaged depots and adjacent evidence surfaces before deciding what the chat adds.
3. **Ground.** Ground both the visible conversation and relevant external evidence. What the touched index already models is out; gaps, tensions, and fresh `User.Touched` material are candidates.
4. **Map.** Build an internal candidate map broad enough to understand the likely session, including overlap, dependencies, natural edit actions, and possible destinations.
5. **Roadmap.** In `Interactive` mode, present the small public `Capture.Roadmap`: the likely block or edit clusters and one sentence explaining each. This first-turn orientation precedes detailed drafting.
6. **Focus.** Select one block or small coherent cluster from the roadmap. The user may redirect, reorder, remove, or add candidates through natural conversation.
7. **Propose + Discuss.** Codesign only the foreground cluster with the user, then present its exact typed, landing-targeted draft. The goal is to reason while preparing kernel text — convergence happens in the discussion, not at the write.
8. **Approve.** User approval accepts the current form in chat — it is not a write. Approved material accumulates while the discussion rolls to the next cluster.
9. **Land + Re-ground.** A separate, user-triggered act lands all or selected approved material. Keep the review loop active, re-ground against the changed touched index, update the internal candidate map, and refresh only the roadmap entries whose meaning or order changed.

`Autonomous` mode performs the same preparation and internal mapping but does not present a roadmap or run the review loop; it proceeds through its agendix-only landing path.

## Capture.Roadmap

`Capture.Roadmap` is an attention-budgeted index of what a good candidate capture session would cover. It is a selective projection of the internal candidate map, not an evidence report or exhaustive backlog.

- list likely block or edit clusters in a useful review order
- identify the relevant block or intended edit with one short sentence explaining the capture move
- prefer names and terse pointers for concepts already present in the user's context; add a gloss only when a name would not resolve clearly
- omit evidence inventories, source lists, uncertainty columns, and destination detail unless one materially changes the proposed session
- recommend the first focus without presenting every candidate as a full draft
- keep the roadmap provisional: natural conversation may reshape it at any time

The roadmap is not approval-ready material. Do not expose `::approve` merely because a roadmap is foregrounded; that command becomes available only after one exact draft and landing target are presented.

## User.Command Checkpoints

- These checkpoints apply the skill's declared `User.Command` transitions and resolve each required `User.Command.Arg` against the foreground capture state.
- When an approval-ready draft becomes foreground, mint a fresh opaque `Edition.Approval.Token`, show it in the same assistant turn as the exact draft, and pause with the resolved `::approve <token>` command (`::approved` equivalent). The command accepts that exact draft and never writes it.
- The token identifies one exact proposal and may cover several verbatim lines. Reuse it while the wording and landing target hold; if either changes, invalidate it, mint a fresh token, and show the complete revised proposal again.
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
  ::approve idx-edition:7d2f91c4  approve the exact Background.Job proposal
  ::approve idx-edition:3a84e6d2  approve the exact Serialized.Lane proposal
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

Landing form-fits approved material to the named surface, one rung up the `Capture.Gradient`, under that surface's own gate. Approval-ready candidates show the concrete `Landing:` file and `Target:` ontology location before the draft text; the destination can stay loose only while the discussion is still exploratory.

- **ontology / appendix** — gated (`Edition.Trigger.User.Gated`, `Verbatim.User.Gated`): a draft that already matches the surface lands as an approved forward pass through the `references/edit.md` landing procedure; a cluster approved in chat lands under one gate
- **agendix** — ungated, user-triggered: the routing verdict is the whole trigger; material lands in kernel form per `references/agendix.md` — lines under routed concepts, candidate blocks intact as path-children — captured but ungated, promotion-ready, reported at the end
- the grounding anchor for a landed ontology or appendix item targets its tokenized approval turn and carries the proposal/approval event refs needed by `Line.Verbatim.Gate`; the landing trigger is execution, not evidence

## Behavior

- the discussion is free: capture is pulled by the user, never a standing obligation on the conversation — not every discussion involves blocks
- `Not.A.Wall.Of.Text` governs the loop: the opening turn may show the broader `Capture.Roadmap`, but not the context-assembly load or evidence inventory; after orientation stay on one block or small coherent cluster, never re-dump the full harvest
- after approval, continue directly to the next roadmap cluster while the approved material accumulates; landing is a batch checkpoint rather than the default response to each approval
- after a write, refresh the internal map; show only a compact roadmap delta unless the session's big picture materially changed
- know what is approved and unlanded at any moment — the conversation itself is the record; no tracking mechanism is required
- material not worth the full hugentic review can always take the agendix exit rather than staying stranded in chat
- load `references/type.md` before drafting lines and `agentos-pkg/references/index-block-catalog.md` before proposing block wording
