# Hugentic.Capture.Workflow.Module

Use this module when the user wants active conversation and adjacent evidence worked into maintained durable state: "let's capture".

`Hugentic.Capture.Workflow` is the primary user-facing alignment workflow. Its target may be the reviewed main Index surfaces, `Design.Req`, or `Index.Agendix`; changing target changes the applicable landing gate, not the conversational loop. `--capture` selects the loop without selecting a durable target. Compatible flags, conversation, and declared defaults may complete the route where their rows permit it.

`Design.Req.Promotion` is the interruption that temporarily retargets this loop from an active design request to the index, an `Impl.Req`, or both.

## Target Resolution

| Call configuration | Resolved target |
|---|---|
| `--capture` outside the Implementation namespace | unresolved; continue discussion or permitted conversational discovery |
| `--capture --audit` | read-only capture mapping; target flags may narrow the surfaces inspected but cannot enable writing |
| `--capture --index`, `--capture --main`, `--index --capture --main` | reviewed main Index surfaces: `Index.Ontology` or `Index.Appendix` |
| `--capture --agendix`, `--agendix`, `--index --capture --agendix` | `Index.Agendix` |
| `--design` outside the Implementation namespace | `Design.Req` |

`--agendix` is the shorthand row that supplies the capture workflow and agendix target together. `--index` contributes the Index namespace and, in a capture call without a narrower target, resolves the reviewed main target; `--main` names that target directly. A `Design.Req` target loads `references/design-req.md` as `Design.Req.Knowledge.Module`.

Inside the Implementation namespace, `--impl --design` and `--impl --capture` belong to `Implementation.Workflow.Router.Module`; they do not select this module through the root meanings of `--design` or `--capture`.

## Shared Capture Loop

1. **Contextualize.** Resolve the target, active conversation, touched state, and adjacent evidence.
2. **Map.** Identify small coherent candidate clusters, overlap, dependencies, and unresolved POIs.
3. **Focus.** Foreground one cluster; let natural conversation redirect or reshape it.
4. **Propose + Discuss.** Form-fit the candidate to its target and expose the wording or material decision that needs attention.
5. **Approve.** Apply the target's gate. Approval records proposal state; it does not imply landing where the target separates those acts.
6. **Land.** Write only through the resolved target procedure.
7. **Reconcile.** Re-read the changed target and maintain any active workflow artifact before continuing or completing.

### Read-Only Audit

`--audit` configures `--capture`; it does not select another workflow or module. Run **Contextualize** and **Map**, present the target-appropriate `Capture.Roadmap`, and stop before **Focus**.

This configuration is read-only. Do not draft approval-ready material, expose approval or landing commands, mutate a durable surface, or continue into later capture stages. The trailing prompt scopes the sources or surfaces to inspect; without an explicit scope, use the current conversation and active or mentioned artifacts. If the map is empty, report `Capture audit: all sources in sync.`

The index specialization loads `Hugentic.Capture.Context.Assembly.Module` from `references/index-capture-context.md` before its first grounding pass. Its surfaces are governed by `Workflow.Neutral` knowledge modules: `Index.Landing.Knowledge.Module` for ontology and appendix, and `Index.Agendix.Knowledge.Module` for agendix.

`Capture.Offer` is the same act at single-candidate scale: agent-initiated, one draft, same destination semantics. This module is the user-initiated, whole-conversation form.

Load `references/touched-data.md` for authority and line standing, and `references/decision-cycle.md` for contextualize-act-reconcile. The current chat protocol supplies qualifying user turns and Chatlas support records; it does not make chat the conceptual boundary of `Touched.Index`.

For chronological capture, work from the authoritative Chatlas transcript and delimit each semantic Delta by its `Delta.Horizon.Turn`. A Delta may summarize one user turn or a meaningful group ending at that turn. Ordinary model lines must acquire an exact Delta materialization before they are considered fully propagated; `Chat.Index.HEAD` and Project Index projections may be authored first, but the resulting missing-home condition remains a reconciliation POI until backfilled.

Use the Chatlas `Capture.Plan` application boundary for mechanical writes. In maintain mode, `head.preserve: true` permits a Delta-only backfill while retaining the complete existing HEAD. The `Index.Line.Anchor` dossier asserts the current `Line.Type + body + Anchor.Id` triplet and records independent support, gate, and provenance relationships. Delta materialization and `Line.Home` are derived from exact containment and authoritative tape order. Placement on a HEAD does not create touched authority.

Operationally, capture applies `Touched.Decision.Cycle` to `Touch.Authority.Surface` editions and adjacent evidence. It distinguishes `Touched.Data`, `Support.Set`, `Live.Index.Line`, `Open.Inference`, and `POI.Instance` while producing `Kernel.Writing` for the current `Agentos.Index.System` realization.

## Index Target Specialization

A pass over the chat's uncaptured content, repeated until the content is exhausted or the user stops:

1. **Contextualize / Assemble.** Load `Hugentic.Capture.Context.Assembly.Module`, including the touched-data and decision-cycle knowledge modules.
2. **Contextualize / Discover.** Resolve engaged depots and live line standing, then batch the materially relevant existing anchors into a reference-detail line manifest before inspecting authority-surface or adjacent non-touch evidence.
3. **Contextualize / Ground.** Treat the manifest as a volatile relationship projection, not authority. Use it to select support references, escalate only the references whose original turns or bounded context are needed, and preserve ungrounded live lines as `Index.Presumption`.
4. **Contextualize / POIs.** Make gaps, contradictions, ambiguity, stale projections, and missing grounding explicit before choosing a capture move.
5. **Act / Map.** Build an internal candidate map covering overlap, dependencies, natural edit actions, possible destinations, and POIs that may legitimately remain unresolved.
6. **Act / Roadmap.** In `Interactive` mode, present the small public `Capture.Roadmap`: likely block or edit clusters and one sentence explaining each.
7. **Act / Focus.** Select one block or small coherent cluster. The user may redirect, reorder, remove, or add candidates through natural conversation.
8. **Act / Propose + Discuss.** Codesign only the foreground cluster, then present a typed, landing-targeted `Index.Edition.Turn`.
9. **Act / Approve.** User approval records the current proposal as approved but unlanded. Approved material accumulates while review moves to the next cluster.
10. **Reconcile / Land + Re-ground.** A separate user command lands selected approved material, then re-contextualizes against the changed live cut and support network.
11. **Reconcile / Propagate.** Audit Project lines against registered support Chat.Indexes. Missing Delta homes or current Chat HEAD projections remain advisory POIs and may be repaired in either direction without blocking the originating edit.

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
- do not resolve support or allocate an anchor while the proposal remains open to revision; when a future anchor must be shown, use the inert `^<anchor-on-landing>` placeholder
- treat this rendering as user experience, not linter syntax; headings, order, fences, and diff notation may evolve

## User.Command Checkpoints

- These checkpoints apply the skill's declared `User.Command` transitions and resolve each required `User.Command.Arg` against the foreground capture state.
- When an approval-ready draft becomes foreground, mint a fresh opaque `Edition.Approval.Token`, show it in the same assistant turn as the proposed landing content, and pause with the resolved `::approve <token>` command (`::approved` equivalent). The command approves that presented edition and never writes it.
- The token identifies one proposal and may cover several lines. Reuse it while materially significant wording and the landing target hold; presentation-only changes do not require a new attention checkpoint.
- Do not offer or use bare `::approve` in this workflow. If the user gives it anyway, explain that it records at most semantic edit-event approval, leave the draft approval-ready, and reprint the exact `::approve <token>` command required to satisfy `Line.Verbatim.Gate`.
- Approval adds the resolved draft to the approved, unlanded cluster and returns the loop to **Focus**. In `Capture.Stance::Review`, when roadmap candidates remain, the default next move is to codesign and present the next approval-ready draft, not to pause for landing.
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

Example `Capture.Stance::Discuss` footer:

```text
Available User.Commands:
  ::review  resume presenting blocks for approval
```

## Mode

- capture accepts `Alignment.Mode` — `Interactive` (default) or `Autonomous`
- `Interactive` presents the roadmap, then runs the focused codesign loop: checkpoints are alignment opportunities, discussion and approval happen per small cluster
- `Autonomous` runs without user prompting: the loop collapses to ground → propose → land → report, and it can land only on the agendix — a user gate (`Edition.Trigger.User.Gated`) cannot be resolved autonomously
- `--AUTO` is the extreme case as a flag: the full workflow automatic, chat to agendix, the invocation is the one trigger that covers the pass
- `--agendix` presets the agendix destination and defaults to `Autonomous`; the user engaging mid-pass simply is `Interactive`

## Capture.Stance

`Capture.Stance` is the user's steering of the `Interactive` loop: whether the agent answers with a draft or with conversation. The workflow, its target, and its gates are identical either way.

- `Capture.Stance::Review` is the default and is the loop as written above: after each user turn the next move is the next approval-ready draft
- `Capture.Stance::Discuss` holds ordinary conversation: present no `Index.Edition.Turn` and make no `Capture.Offer`, and answer the user's point instead
- `::discuss` is sticky — it holds until `::review`, and no other move restores drafting: not a status request, not a landing, not an interruption and return
- `::review` resumes drafting from the current foreground with no preamble, delta, or re-orientation
- entering `Capture.Stance::Discuss` never discards a foreground approval-ready draft; the draft stands with its token intact and stays approvable
- a stance changes what the agent presents, never what it tracks: candidates continue to accumulate and `--capture --audit` still reports them
- neither stance changes a command's `available:` condition; `::approve` simply has nothing to resolve once no draft is foreground
- in `Capture.Stance::Discuss` the only advertised command is `::discuss`'s exit, `::review`
- `Alignment.Mode::Autonomous` has no stance: it lands only on a non-reviewed target like the agendix, so no draft is ever presented for approval

## Landing

Landing form-fits material to the named surface under that surface's own gate. Approval-ready candidates show the concrete `Landing`, `Target`, operation, and proposed content; the destination may remain loose only while discussion is exploratory.

- **ontology / appendix** — token approval establishes reviewed content, while a separate landing command executes the gated edit; landing resolves qualifying substantive support plus the approval turn into the line's support set
- **agendix** — one user trigger covers the pass without per-line review; each line still lands typed and grounded through a resolvable support set under a routed concept or provisional path
- support resolution and anchor allocation are landing work; they occur against the final approved proposal, its qualifying substantive support, and its approval turn, never while the proposal remains open to revision
- a multi-line landing previews and registers its exact final bodies as one anchor batch, then applies the returned line-to-anchor mapping in one surface patch; the single-line path remains for one line
- every landing updates the live cut; capture re-contextualizes afterward and reports remaining POIs without treating them as automatic edits

## Behavior

- the discussion is free: capture is pulled by the user, never a standing obligation on the conversation — not every discussion involves blocks; `::discuss` is how the user says so for a stretch rather than one draft at a time
- `Not.A.Wall.Of.Text` governs the loop: the opening turn may show the broader `Capture.Roadmap`, but not the context-assembly load or evidence inventory; after orientation stay on one block or small coherent cluster, never re-dump the full harvest
- after approval, continue directly to the next roadmap cluster while the approved material accumulates; landing is a batch checkpoint rather than the default response to each approval
- after a write, refresh the internal map; show only a compact roadmap delta unless the session's big picture materially changed
- know what is approved and unlanded at any moment — the conversation itself is the record; no tracking mechanism is required
- never silently delete, demote, or rewrite a contradictory live line; capture may propose reconciliation, while the landing gate controls the surface change
- material not worth the full hugentic review can always take the agendix exit rather than staying stranded in chat
- load `references/type.md` before drafting lines and `tarav-pkg/references/index-block-catalog.md` before proposing block wording
