> $kw: ^capture-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^hugentics-batchy-runtime-contract
> --loading-dep SKILL.skw.md^hugentics-skill-arg-contract
> --loading-dep SKILL.skw.md^hugentics-user-command-contract
> --loading-dep SKILL.skw.md^driver-index-literacy
> --loading-dep SKILL.skw.md^hugentics-authority-contract

# Hugentic.Capture.Workflow.Module

> $kw: --from Agentos.Index.System --from Alignment.Mode --from Capture.Gradient --from Capture.Offer --from Chat.Surface --from Design.Req --from Design.Req.Promotion --from Edition.Approval.Token --from Hugentic.Capture.Workflow --from Impl.Req --from Index.Agendix --from Index.Appendix --from Index.Edition.Turn --from Index.Ontology --from Index.Presumption --from Kernel.Writing --from Line.Verbatim.Gate --from Live.Index.Line --from Not.A.Wall.Of.Text --from Open.Inference --from POI.Instance --from Support.Set --from Touch.Authority.Surface --from Touched.Data --from Touched.Decision.Cycle --from Touched.Index --from User.Attention --from User.Command --from User.Command.Arg --from Verbatim.User.Gated --from Workflow.Neutral
> --from references/design-session.skw.md#Design.Session.Knowledge.Module
> --dev-from references/index-context-assembly.skw.md

Use this module when the user wants active conversation and adjacent evidence worked into maintained durable state: "let's capture".

`Hugentic.Capture.Workflow` is the primary user-facing alignment workflow. Its target may be the reviewed main Index surfaces, `Design.Req`, `Design.Session`, or `Index.Agendix`; changing target changes the applicable landing gate, not the conversational loop. `--capture` selects the loop without selecting a durable target. Compatible flags, conversation, and declared defaults may complete the route where their rows permit it.

These are `Real.Time.Capture` workflows: they operate beside live `User.Attention`, land semantic change from the loaded chat, and backpropagate each exact grounded Index-line edition they successfully land. `Chat.Index` is never a direct Hugentics capture target; it is the chronological co-projection maintained by `Index.HEAD.Backpropagation`.

`Design.Req.Promotion` is the interruption that temporarily retargets this loop from an active design request to the index, an `Impl.Req`, or both.

## Target Resolution

| Call configuration | Resolved target |
|---|---|
| `--capture` outside the Implementation namespace | unresolved; continue discussion or permitted conversational discovery |
| `--capture --audit` | read-only capture mapping; target flags may narrow the surfaces inspected but cannot enable writing |
| `--capture --index`, `--capture --main`, `--index --capture --main` | reviewed main Index surfaces: `Index.Ontology` or `Index.Appendix` |
| `--capture --agendix`, `--agendix`, `--index --capture --agendix` | `Index.Agendix` |
| `--capture --design-session` | topic-scoped `Design.Session` live artifact |
| `--design` outside the Implementation namespace | `Design.Req` |

`--agendix` is the shorthand row that supplies the capture workflow and agendix target together. `--index` contributes the Index namespace and, in a capture call without a narrower target, resolves the reviewed main target; `--main` names that target directly. A `Design.Req` target loads `references/design-req.md` as `Design.Req.Knowledge.Module`; `--capture --design-session` loads `references/design-session.md` as `Design.Session.Knowledge.Module`.

Inside the Implementation namespace, `--impl --design` and `--impl --capture` belong to `Implementation.Workflow.Router.Module`; they do not select this module through the root meanings of `--design` or `--capture`.

## Shared Capture Loop

1. **Contextualize.** Resolve the target, active conversation, touched state, and adjacent evidence.
2. **Map.** Identify small coherent candidate clusters, overlap, dependencies, and unresolved POIs.
3. **Focus.** Foreground one cluster; let natural conversation redirect or reshape it.
4. **Propose + Discuss.** Form-fit the candidate to its target and expose the wording or material decision that needs attention.
5. **Approve.** Apply the target's gate. Approval records proposal state; it does not imply landing where the target separates those acts.
6. **Land.** Write only through the resolved target procedure.
7. **Backpropagate.** Project exact grounded lines from the successful landing to `Chat.Index.HEAD`, then best-effort onto the `Chat.Index.Delta` tape through their support-derived `Chat.Turn.Ref` horizon.
8. **Reconcile.** Re-read the changed target and maintain any active workflow artifact before continuing or completing.

### Read-Only Audit

`--audit` configures `--capture`; it does not select another workflow or module. Run **Contextualize** and **Map**, present the target-appropriate `Capture.Roadmap`, and stop before **Focus**.

This configuration is read-only. Do not draft approval-ready material, expose approval or landing commands, mutate a durable surface, or continue into later capture stages. The trailing prompt scopes the sources or surfaces to inspect; without an explicit scope, use the current conversation and active or mentioned artifacts. If the map is empty, report `Capture audit: all sources in sync.`

The index specialization loads `Hugentic.Capture.Context.Assembly.Module` from `references/index-capture-context.md` before its first grounding pass. Its surfaces are governed by `Workflow.Neutral` knowledge modules: `Index.Landing.Knowledge.Module` for ontology and appendix, and `Index.Agendix.Knowledge.Module` for agendix.

`Capture.Offer` is the same act at single-candidate scale: agent-initiated, one draft, same destination semantics. This module is the user-initiated, whole-conversation form.

Load `references/touched-data.md` for authority and line standing, and `references/decision-cycle.md` for contextualize-act-reconcile. The current chat protocol supplies qualifying user `Chat.Message.Ref` assertions and Chatlas2 grounding records; it does not make chat the conceptual boundary of `Touched.Index`.

For current-session capture, use the live conversation already in agent context as the default understanding source. Consult Chatlas2 after selecting qualifying messages, to resolve and validate their exact references. Transcript reconstruction is an escalation for ambiguity, missing compacted context, or explicitly historical work—not a default preparation step.

Every target uses the same Chatlas2 grounding and backpropagation boundary. Target modules retain their own gates and surface writes; Chatlas2 retains exact `Chat.Message.Ref`, `Chat.Turn.Ref`, line-dossier validation, and descriptor-free Chat.Index mechanics.

Load `Real.Time.Grounding.Knowledge.Module` from `references/link.md` before minting the landing batch and `Real.Time.Validation.Knowledge.Module` from `references/check.md` after the primary patch. These are internal capture primitives; neither file defines a public route.

## Real.Time.Capture And Index.HEAD.Backpropagation

`Index.HEAD.Backpropagation` is a required postcondition for each exact grounded Index line successfully landed from the current chat:

```text
Other.HEADs -> Chat.Index.HEAD -> Chat.Index.Delta tape
```

- `Chat.Index.HEAD` receives every exact landed edition, even when chronological placement cannot yet be proven.
- The Delta tape receives a stable receipt when the line dossier's support includes a message on the target chat. The latest local supporting message selects its containing `Chat.Turn.Ref`; one coherent landing batch may share the latest such horizon.
- A Delta may have any completeness. Its only semantic constraint is that every line it contains is supported within its horizon.
- Later HEAD changes produce later receipts, often on another `Chat.Surface`; they never rewrite earlier receipts merely to keep the current model tidy.
- A head-only result is a recoverable reconciliation gap, not a reason to roll back the primary landing or invent an origin.

Use the Chatlas2 real-time `Capture.Plan` after the primary target's final anchor batch is known:

1. Scaffold one plan with `tarav chatlas2 chat-index scaffold --identity-hash <current-chat-identity> --stage <empty-stage> --json`.
2. Register the final line-dossier batch and patch the primary target through its normal landing procedure.
3. Fill `plan.json.landed_lines` with stable `client_id`, target `concept`, exact unanchored `line_content`, and the returned `d…` `anchor`; set `status` to `ready`. Do not duplicate support, gates, or predecessors from the dossier.
4. Run `tarav chatlas2 chat-index validate --plan <plan.json> --json`. It verifies attachment triplets, support standing, containing turns, the base fingerprint, and the planned HEAD/Delta effects without writing Chat.Index.
5. Run `tarav chatlas2 chat-index apply --plan <plan.json> --json`. Apply revalidates under the session lock, updates the partial Chat HEAD, appends the stable Delta receipt when possible, and audits exact presence.
6. Report every `head_only_gaps` item for background reconciliation. A failed or interrupted backpropagation remains retryable and must be reported, but it does not undo an already successful primary landing.

The plan is a batching boundary, not a second semantic model. It names editions already landed elsewhere; the Chatlas2 line dossier remains the authority for support, gates, predecessors, and attachment drift.

Operationally, capture applies `Touched.Decision.Cycle` to `Touch.Authority.Surface` editions and adjacent evidence. It distinguishes `Touched.Data`, `Support.Set`, `Live.Index.Line`, `Open.Inference`, and `POI.Instance` while producing `Kernel.Writing` for the current `Agentos.Index.System` realization.

## Index Target Specialization

A pass over the chat's uncaptured content, repeated until the content is exhausted or the user stops:

1. **Contextualize / Assemble.** Load `Hugentic.Capture.Context.Assembly.Module`, including the touched-data and decision-cycle knowledge modules.
2. **Contextualize / Discover.** Resolve engaged depots and live line standing, read the materially relevant Index blocks directly, and select only current Chatlas2 `^d…` references for relationship inspection. Legacy anchors remain visible history but are not resolved by this workflow.
3. **Contextualize / Ground.** Resolve only those selected references with `tarav chatlas2 anchory resolve`; escalate only the messages or containing turns needed, and preserve ungrounded live lines as `Index.Presumption`.
4. **Contextualize / POIs.** Make gaps, contradictions, ambiguity, stale projections, and missing grounding explicit before choosing a capture move.
5. **Act / Map.** Build an internal candidate map covering overlap, dependencies, natural edit actions, possible destinations, and POIs that may legitimately remain unresolved.
6. **Act / Roadmap.** In `Interactive` mode, present the small public `Capture.Roadmap`: likely block or edit clusters and one sentence explaining each.
7. **Act / Focus.** Select one block or small coherent cluster. The user may redirect, reorder, remove, or add candidates through natural conversation.
8. **Act / Propose + Discuss.** Codesign only the foreground cluster, then present a typed, landing-targeted `Index.Edition.Turn`.
9. **Act / Approve.** User approval records the current proposal as approved but unlanded. Approved material accumulates while review moves to the next cluster.
10. **Reconcile / Land + Backpropagate.** A separate user command lands selected approved material, performs `Index.HEAD.Backpropagation` for its exact anchored lines, then re-contextualizes against the changed live cut and support network.
11. **Reconcile / Continue.** Report head-only or failed tape placements as advisory POIs for later background reconciliation without blocking the originating edit.

`Autonomous` mode performs the same preparation and internal mapping but does not present a roadmap or run the review loop; it proceeds only through a target contract that admits one-trigger agentic landing.

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
- `Autonomous` runs without user prompting: the loop collapses to ground → propose → land → report, and it may land only on a target whose contract admits one-trigger agentic capture — currently `Index.Agendix` and `Design.Session`
- `--AUTO` explicitly selects autonomous mode without changing a separately resolved target; the target contract still decides whether agentic landing is permitted
- `--agendix` presets the agendix destination and defaults to `Autonomous`; the user engaging mid-pass simply is `Interactive`
- `--capture --design-session` presets the design-session destination and defaults to `Autonomous`; the invocation covers the bounded pass

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
- `Alignment.Mode::Autonomous` has no stance: it lands only on a one-trigger, non-reviewed target such as the agendix or a design session, so no draft is ever presented for approval

## Landing

> $kw: --derived
> --from references/edit.skw.md#Landing Procedure
> --from references/agendix.skw.md#Landing Form
> --from references/design-session.skw.md#Landing
> --intent digest the landing paths into the routing summary capture needs:
> --cont keep gate semantics and form-fit moves aligned without restating target
> --cont procedures — the knowledge modules own them

Landing form-fits material to the named surface under that surface's own gate. Approval-ready candidates show the concrete `Landing`, `Target`, operation, and proposed content; the destination may remain loose only while discussion is exploratory.

- **ontology / appendix** — token approval establishes reviewed content, while a separate landing command executes the gated edit; landing records substantive user-message support plus independent proposal/approval message gates
- **agendix** — one user trigger covers the pass without per-line review; each line still lands typed and grounded through a resolvable support set under a routed concept or provisional path
- **design session** — one user trigger covers the bounded pass without per-line review; typed lines grounded in Chatlas2 user `Chat.Message.Ref` assertions land in the resolved topic-scoped `Design.Index`, while unresolved material stays in `Session.Notes`
- support resolution and anchor allocation are landing work through the internal Chatlas2 `Real.Time.Grounding.Knowledge.Module`; they occur against the final approved proposal and its qualifying substantive support, never while the proposal remains open to revision
- a multi-line landing previews and registers its exact final bodies as one anchor batch, then applies the returned line-to-anchor mapping in one surface patch; the single-line path remains for one line
- after that primary patch succeeds, the same exact line-to-anchor mapping becomes one Chatlas2 real-time Capture.Plan and is backpropagated to Chat.Index.HEAD and, when support supplies a local horizon, the Delta tape
- `Real.Time.Validation.Knowledge.Module` re-reads only the newly landed source lines, resolves their Chatlas2 anchors, and checks the exact backpropagation audit; broader diagnosis remains parked
- every landing updates the live cut; capture re-contextualizes afterward and reports remaining POIs without treating them as automatic edits

> $kw. end

## Behavior

- the discussion is free: capture is pulled by the user, never a standing obligation on the conversation — not every discussion involves blocks; `::discuss` is how the user says so for a stretch rather than one draft at a time
- `Not.A.Wall.Of.Text` governs the loop: the opening turn may show the broader `Capture.Roadmap`, but not the context-assembly load or evidence inventory; after orientation stay on one block or small coherent cluster, never re-dump the full harvest
- after approval, continue directly to the next roadmap cluster while the approved material accumulates; landing is a batch checkpoint rather than the default response to each approval
- after a write, refresh the internal map; show only a compact roadmap delta unless the session's big picture materially changed
- know what is approved and unlanded at any moment — the conversation itself is the record; no tracking mechanism is required
- never silently delete, demote, or rewrite a contradictory live line; capture may propose reconciliation, while the landing gate controls the surface change
- material not worth the full hugentic review can always take the agendix exit rather than staying stranded in chat
- load `references/type.md` before drafting lines and `tarav-pkg/references/index-block-catalog.md` before proposing block wording
