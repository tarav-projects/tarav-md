---
name: agentos-hugentics
description: "Canonical public control surface for Hugentic sessions. USE WHEN you need touched-data contextualization, product design, implementation design or execution, capture, reconciliation, parking, status, index research, editing, diagnosis, testing, or maintenance."
---

# Agentos Hugentics

Canonical `Package.Driver` and single public session-control surface for the Agentos Hugentic Harness.

`Touched.Index` is the global system for contextualizing relevant `Touched.Data`. The Markdown `Agentos.Index.System`, trailing Anchory anchors, and Chatlas support records are its current realization, not its conceptual boundary.

Index capabilities remain a distinct internal subsystem because nearly every Hugentic workflow depends on touched-data contextualization. The caller nevertheless controls the whole session here: product design, implementation design and execution, capture, audit, status, parking, and every Index operation route through named modules without requiring another public skill.

This is a `Batchy.Skill`; the public arguments and user commands below are its complete caller contract.

- `-h` / `--help` prints usage and the public args without running.
- declared `User.Command`s are the only way to cross their explicit workflow gates.
- when an index workflow pauses, print only the commands available at that checkpoint.

## Skill.Arg.Section

### Skill.Arg::Search

- search the index through routing-first selective loading, grounded against the current visible discussion
- required: false
- aliases: --research, --ground
- help: "search the index and return cited context grounded against the current discussion"
- examples: --search "Index.AGENTS.MD", --research "Parking.Note", --ground "check this design discussion against the index"

### Skill.Arg::Capture
- run the capture loop: work the chat's content into kernel writing form through discussion, and land approved material on user-named index surfaces
- accepts `Alignment.Mode` (`Interactive` default); `--AUTO` is the fully automatic extreme — chat to agendix, no prompting
- required: false
- help: "capture the current chat into the index: ground, draft, discuss, approve, land"
- examples: --capture, --capture "capture the design discussion we just had", --capture --AUTO

### Skill.Arg::Design
- run a `Product.Design.Session` whose decisions are contextualized through the touched index
- required: false
- help: "design a target product through touched-data contextualization and explicit What/How/Exec concerns"
- examples: --design "the Batchy skill framework", --design --artifact

### Skill.Arg::Design.Scope
- the `Target.Product` subject and boundary for `--design`
- required: false
- help: "what product or design result the session should advance"
- examples: --scope "the Batchy skill framework"

### Skill.Arg::Session.Backend
- use the artifact-backed design-session backend instead of the default in-chat backend
- required: false
- type: switch
- help: "persist the design session in an artifact"
- examples: --artifact

### Skill.Arg::Edit

- work the approved edit path for index or appendix changes
- required: false
- help: "use the index edit path for approved changes"
- examples: --edit "add Context.Hook"

### Skill.Arg::Write
- call the edit module
- required: false
- help: "use the index edit path for approved changes"
- examples: --write "add Context.Hook"

### Skill.Arg::Append
- call the edit module
- required: false
- help: "use the index edit path for approved changes"
- examples: --append "add a line to Context.Hook"

### Skill.Arg::Reconcile
- compare a changed `Target.Product` with applicable touched design and route any required gated index changes
- required: false
- help: "reconcile implementation or surface reality with the touched index"
- examples: --reconcile "compare the current Hugentics Index modules with their design"

### Skill.Arg::Check
- run deterministic checks over index depots or explicit index surfaces
- required: false
- help: "run index checks"
- examples: --check --depot agentos-pkg

### Skill.Arg::Lint
- call the check module
- required: false
- help: "run index checks"
- examples: --lint --depot agentos-pkg

### Skill.Arg::Depot
- scope index work to one or more engaged index depots
- required: false
- default: task-relevant engaged depots
- help: "scope index work to an index depot"
- examples: --depot agentos-pkg, --depot agentos-chatlas-pkg

### Skill.Arg::Chapter
- scope index work to one chapter within the engaged depots
- required: false
- default: design
- help: "scope index work to a chapter"
- examples: --chapter design, --chapter impl

### Skill.Arg::Type
- read or propose `Line.Type` classification for index lines
- required: false
- help: "explain, read, or propose index line typing"
- examples: --type "type the Anchory.System block", --type "what binds me in this block?"

### Skill.Arg::Agendix
- run the capture loop with the agendix as preset destination — `Alignment.Mode::Autonomous` by default, the agent lands and reports
- required: false
- help: "run an agendix capture pass over the current conversation"
- examples: --agendix, --agendix "capture the grounding discussion"

### Skill.Arg::Link
- mint an `Anchory.Anchor` for a chat context — the linking primitive other modules consume
- required: false
- help: "mint an anchor for a chat evidence turn and return it"
- examples: --link "anchor the turn where the user picked syntax B"

### Skill.Arg::BackLink
- ground an existing index block backward: git history → session → turns → anchor
- required: false
- help: "recover chat evidence for an existing block and propose its grounding"
- examples: --back-link "Writing.Friction.Reduction", --back-link "ground the 107 chapter"

### Skill.Arg::GrSurvey
- run a grounding campaign's survey phase: sweep a scope, mint anchors, produce a `Gr.Req`
- required: false
- aliases: --gr-scout, --gr-scan, --gr-linker
- help: "survey grounding evidence for a scope into a Gr.Req artifact"
- examples: --gr-survey "design/105-design.md", --gr-survey "the whole agentos-pkg depot"

### Skill.Arg::GrReview
- walk a `Gr.Req`'s proposed entries with the user and land the approved links
- required: false
- help: "review a Gr.Req: flip statuses, land gated grounding edits"
- examples: --gr-review 577, --gr-review "notes/live/577-105-gr-req.md"

### Skill.Arg::Enrich
- run `Index.Enrichment` on a block: a focused discussion producing new touched surface, landed through the gates
- required: false
- help: "enrich a block: generate new grounding surface through a scoped discussion"
- examples: --enrich "Writing.Friction.Reduction", --enrich (default: head of the gr-density worklist)

### Skill.Arg::Implementation
- select implementation design, review, execution, end-to-end development, or ready-work capture
- required: false
- aliases: --impl, --impl-design, --review, --execute, --exec, --develop, --dev, --impl-capture
- help: "run an implementation workflow"
- examples: --impl-design "add project-scoped configuration", --execute 601, --develop "add project-scoped configuration", --impl-capture

### Skill.Arg::CaptureAudit
- audit the current session and its active artifacts for material that remains upstream of its maturity
- required: false
- aliases: --capture-audit
- help: "report significant session material not yet captured in the right durable surface"
- examples: --capture-audit, --capture-audit "audit the current chat and Impl.Req"

### Skill.Arg::ChatStatus
- reconnect the user with the current chat's main thread and session todo state
- required: false
- aliases: --status, --chat-status
- help: "report the current session state and likely next move"
- examples: --status, --chat-status "what remains?"

### Skill.Arg::WorkflowStatus
- report a structured checkpoint against the active Hugentic workflow and its artifacts
- required: false
- aliases: --workflow-status
- help: "report the active workflow's done, current, stale, open, and next state"
- examples: --workflow-status

### Skill.Arg::Park
- capture a sidequest thought into a project `Parking.Note`, then return to the interrupted session
- required: false
- aliases: --parking-note
- help: "park an idea without changing the main session focus"
- examples: --park "revisit retry backoff", --parking-note "investigate a second authority surface"

### Skill.Arg::Clean
- scan a git-tracked codebase for a targeted cleanup, produce an `Impl.Req`, gate once, and execute autonomously
- required: false
- aliases: --codebase-cleaner, --cleanup
- help: "design and execute a scoped codebase cleanup"
- examples: --clean, --cleanup "centralize repeated configuration parsing"

## User.Command.Section

This `User.Command.Section` declares the canonical commands below. Each accepted `User.Command.Trigger` resolves to one command, whose nested `User.Command.Arg` blocks govern target resolution.

### User.Command::Approve
- accept an approval-ready index draft in its current form without writing it
- triggers: `::approve`, `::approved`
- available: when `--capture`, direct `--edit`, a `Capture.Offer`, or an `--enrich` capture offer has one or more approval-ready drafts
- action: mark the resolved target approved and unlanded
- policy: index workflows mint and advertise only `::approve <token>`; a bare approval is a supported semantic approval form in the general command model but does not cross this workflow's `Line.Verbatim.Gate`

#### User.Command.Arg::Token
- the fresh `Edition.Approval.Token` printed with the proposed landing content
- required: false
- resolution: Explicit
- examples: `::approve idx-edition:7d2f91c4`
- when present, resolves the proposal it was minted for and upgrades materially equivalent landed lines to CPU-checkable `Reviewed.Content`

#### User.Command.Arg::Target
- the draft, block, line, or revision to approve
- required: true
- resolution: Contextual
- examples: `::approve`, `::approved the block after the correction`, `::approve idx-edition:7d2f91c4`

### User.Command::Land
- write approved, unlanded index material through its declared landing procedure
- triggers: `::land`, `::write`
- available: when the foreground index workflow holds one or more approved, unlanded targets
- action: land the resolved target set; never approve material implicitly
- presentation: workflow modules decide when to suggest landing; in `--capture`, approval normally advances to the next review item while explicit early landing remains valid

#### User.Command.Arg::Target
- the approved item or set to land
- required: true
- resolution: Contextual
- examples: `::land`, `::write all approved blocks`

### User.Command::LandAllApproved
- write the complete approved, unlanded cluster held by one foreground index workflow
- triggers: `::land-all-approved`
- available: when the foreground index workflow holds one or more approved, unlanded targets
- args: none
- action: land every approved, unlanded target in that foreground workflow; never approve material implicitly
- resolution: fail closed unless exactly one foreground index workflow supplies the approved cluster

## Boundary

- this skill is the canonical public entry surface for Hugentic session control, including the global `Touched.Index` system
- it distinguishes the general authority, support, and decision model from the current Markdown/Anchory/Chatlas realization
- it remains a `Workflow.Neutral.Skill` when no explicit arg is selected
- it routes into named modules instead of splitting session control across public skills
- Index modules own Index mechanics; the root owns public workflow selection
- the lower-level `agentos index ...` CLI remains the mechanical implementation surface
- no separate public compatibility entry exists for the Index subsystem

## What The Index Is

- `Touched.Index` curates and densely presents relevant touched data so prior alignment can condition later work
- the authority path is `Touch.Authority.Surface` → `Touched.Data` → `Support.Set` → `Support.Reference` → `Index.Line`
- the support sets of current and historical projections compose `Touched.Support.Network`
- grounded `Live.Index.Line` content carries `Touched.Authority`; ungrounded live content carries weaker `Index.Presumption`
- `Demoted.Index.Line` content is historical rather than current guidance
- contradictory or ambiguous touched positions become `POI.Instance`s and are resolved through `Open.Inference` plus, when needed, a separate gated reconciliation
- the current `Agentos.Index.System` realization is `Index.Skillware` and an `Alignment.Surface` between humans and agents
- it contains `Named.Concepts` written in `Kernel.Block::Index` blocks, organized in `Index.Chapter` files under `Index.Ontology`, routed by `000-INDEX.md`, with `Index.Appendix` depth and `Index.Agendix` leads
- the active chapter defaults to `design`; chapter files are named `NNN-<chapter>.md`
- index work happens over engaged `Index.Depot`s; `--depot` scopes which depots are engaged and `--chapter` scopes within them
- its lines carry `Line.Type` codes (`- [CT] ...`) classifying each line's act; untyped lines are pre-fence legacy
- its current support references are trailing `Anchory.Anchor`s resolving through Chatlas to qualifying user-turn evidence
- agents operate it by loading routers, concept blocks, appendix material, and references relevant to the current task

## Router Table

| Situation | Module / Surface |
|---|---|
| When a consumer needs the general authority, support-network, line-standing, and current-realization model behind every index operation | `references/touched-data.md` |
| When an operation makes a decision or changes a target product — contextualize touched constraints, act through the remaining open region, then reconcile changed surfaces | `references/decision-cycle.md` |
| When the caller wants to find concepts, retrieve cited index context, inspect related blocks, discover whether appendix depth exists, understand how the index already models a topic, or ground the current visible discussion against the index; `--search`, `--research`, and `--ground` all call this module | `references/search.md` |
| When the caller wants product design or organic design work begins; `--design` is the canonical entry | `references/design.md`, then the selected module under `references/design/` |
| When developing any managed Hugentics Index surface — load the complete common index subject universe before selecting direct dependencies, derivations, citations, or runtime-facing content | `references/index-context-assembly.md` |
| When the user wants the chat's content captured — "let's capture": load the index-capture context module, ground the chat and adjacent evidence, present a lightweight candidate roadmap, then codesign and land small approved clusters; `--capture` calls this module, `--agendix` calls its autonomous path with the agendix preset | `references/capture.md` |
| When a capture run needs its complete preparation context — index surface ontology, workflow-neutral writing modules, engaged-depot closure, and adjacent evidence categories — load the whole runtime module | `references/index-capture-context.md` |
| When an index or appendix surface is being written or an approved edit needs landing — the gates, structure, naming, block quality, edit actions, drafting screens, and landing procedure that govern index writing; direct edit work (a stale line, a block revision) also starts here; `--edit`, `--write`, and `--append` all call this module | `references/edit.md` |
| When a changed product or implementation must be compared with touched design; `--reconcile` applies the decision cycle and routes any surface mutation through the edit gate | `references/decision-cycle.md`, then `references/edit.md` when a write is needed |
| When the caller wants deterministic diagnosis, linter findings, or post-edit validation for an index depot or explicit index/appendix surface; `--check` and `--lint` both call this module | `references/check.md` |
| When the caller wants line typing understood, read, or proposed — the `[XX]` syntax, the `Line.Type.Vocabulary`, validation points, reading typed lines as constraints, calibration passes and their residue | `references/type.md` |
| When material lands on the agendix or the caller needs the agendix surface understood — `agendix/` files under existing concepts, typed and anchored lines, ungated with hard provenance | `references/agendix.md` |
| When a caller needs an `Anchory.Anchor` minted for a chat context — session resolution, turn location, registration, verification; consumed by `--capture`, `--edit`, and `--agendix` | `references/link.md` |
| When the caller wants an existing block grounded backward — git dates the wording, chatlas finds the session and turns, the linking primitive mints, the gated edit lands the `[GR]` line | `references/back-link.md` |
| When the caller wants a grounding campaign surveyed — a scope swept, anchors minted, a `Gr.Req` produced with `proposed`/`ambiguous` entries, no index writes; `--gr-scout`/`--gr-scan`/`--gr-linker` are aliases | `references/gr-survey.md` |
| When the caller wants a `Gr.Req` reviewed — proposed entries walked with the user, statuses flipped, approved links landed through the gates, provenance re-verified | `references/gr-review.md` |
| When the caller wants a block enriched — `Index.Enrichment`: a scoped discussion with the user generating new touched surface, minted and landed through the gates; low-but-nonzero density blocks are the default targets | `references/enrich.md` |
| When the caller selects implementation design, review, execution, end-to-end development, or ready-work capture | `references/impl.md`, then the selected module under `references/impl/` |
| When the caller asks whether significant session material remains uncaptured | `references/capture-audit.md` |
| When the caller wants to reconnect with the current chat and its todo state | `references/chat-status.md` |
| When the caller wants a structured checkpoint against an active workflow | `references/workflow-status.md` |
| When the caller wants to park a sidequest thought and return to the current session | `references/parking-note.md` |
| When the caller wants a codebase cleanup designed and executed through one gated handoff | `references/codebase-cleaner.md`, then `references/impl/` |
| When the caller needs the phase model, alignment frame, shared development principles, or interruption vocabulary | `references/harness.md` |
| When the caller provides `--depot`, scope the selected operation to those `Index.Depot`s; otherwise use task-relevant engaged depots | applies to `references/search.md` and `references/edit.md` |
| When the caller provides `--chapter`, scope the selected operation to that `Index.Chapter` inside the engaged depots; default to `design` when no chapter is named | applies to `references/search.md` and `references/edit.md` |
| When the caller needs package-level understanding of how the index subsystem is designed, structured, and distributed across public and local surfaces | `agentos-pkg/design/`, `agentos-pkg/appendix/`, `agentos-pkg/references/` |
| When the caller needs concrete examples of good and bad block shape before proposing or judging block wording | `agentos-pkg/references/index-block-catalog.md` |
| When the caller needs behavioral testing of index entry paths, selection behavior, or usage patterns | `agentos-testground` |

## Index Operating Behavior

An agent operating the index should:

- apply `Touched.Decision.Cycle` to material decisions: contextualize, surface incoherence as POIs, act through the remaining open region, and reconcile changed products
- search routing surfaces in the engaged `Index.Depot`s first, then load only relevant concept blocks, appendix material, or references
- distinguish grounded live lines, ungrounded live lines, and demoted history; apply `Touched.Authority`, `Index.Presumption`, or no current decision weight accordingly
- read down the `User.Attention` gradient — reviewed live blocks and appendix first, then unreviewed grounded leads and finally original authority surfaces
- respect `--depot` as an `Index.Depot` scope; otherwise use task-relevant engaged depots
- respect `--chapter` as an `Index.Chapter` scope inside engaged depots; default chapter is `design`
- return context with source block citations so the caller can verify and maintain the summary
- distinguish discovered context from inference
- treat the prompt as a focus argument and compare the current visible discussion against the index whenever there is discussion state to ground
- make a `Capture.Offer` when work surfaces new aligned content: propose typed line content and its landing operation at the moment, with destination options (index main, appendix, agendix, decline) — never self-write on a gated surface
- use `--capture` when the user wants the chat's content worked into the index — approval in chat and landing on a surface are distinct acts
- resolve `::approve` / `::approved` to `User.Command::Approve`, but in index workflows mint, render, and require the proposal's explicit token; if the user gives a bare approval, leave the verbatim gate unresolved and reprint the exact tokenized command; resolve `::land` / `::write` to targeted `User.Command::Land`, and `::land-all-approved` to zero-argument `User.Command::LandAllApproved`; `--write` remains a skill argument while `::write` is an in-workflow transition
- during interactive capture, add approved drafts to the approved cluster and continue reviewing the roadmap; do not make immediate landing the default next move
- keep command targets foregrounded; targeted commands fail closed on ambiguous targets, and `::land-all-approved` fails closed unless one foreground index workflow owns the cluster
- use file mutation only when the applicable surface gate is satisfied
- keep action separate from index reconciliation: open inference may advance other work without silently rewriting touched positions
- run a linter check after applying an approved index or appendix edit

For delegated read-only research that protects the caller's context, use `Packages.Master.Agent` against the relevant package or packages.

## Skill Modules

- `references/touched-data.md` — the authority flow, support network, line standing, decision weight, and current implementation mapping
- `references/decision-cycle.md` — contextualize-act-reconcile discipline shared by search, design, capture, implementation, and reconciliation
- `references/design.md` — `Product.Design.Session` entry and router for the detailed move library under `references/design/`
- `references/search.md` — routing-first search, selective loading, appendix discovery, citation behavior, and conversation-to-index grounding
- `references/index-context-assembly.md` — the whole-file shared builder context for every managed Hugentics Index surface
- `references/capture.md` — the capture workflow: the discussion-landing loop from chat content to index surfaces
- `references/index-capture-context.md` — the whole-file runtime context and grounding closure for working across a touched index
- `references/edit.md` — the knowledge of index and appendix writing: gates, actions, naming, placement, drafting screens, landing procedure, and maintenance
- `references/check.md` — deterministic index checks through `agentos index linter`
- `references/type.md` — line typing: syntax, vocabulary, validation points, reading typed lines, fence and residue
- `references/agendix.md` — the knowledge of the agendix surface: rules, landing form, boundaries — typed, anchored, ungated
- `references/link.md` — the linking primitive: mint and verify chat anchors through chatlas + anchory commands
- `references/back-link.md` — backward grounding: git history to evidence turns for existing blocks
- `references/gr-survey.md` — grounding campaign survey: scope sweep, minting, `Gr.Req` production (no index writes)
- `references/gr-review.md` — grounding campaign gate: per-entry user verdicts, gated landings, provenance close-out
- `references/enrich.md` — `Index.Enrichment`: block-scoped discussion generating new grounding surface, gated landings, density-delta receipt
- `references/impl.md` and `references/impl/` — implementation design, review, execution, development, and ready-work capture
- `references/capture-audit.md` — whole-session capture audit
- `references/chat-status.md` — lightweight current-chat realignment
- `references/workflow-status.md` — artifact-aware workflow checkpoint
- `references/parking-note.md` — short-lived sidequest capture and return
- `references/codebase-cleaner.md` — scan, scope, gate, and execute a targeted cleanup
- `references/harness.md` — phase model, alignment frame, shared principles, and interruption vocabulary

## Unified Harness Model

The Hugentic Harness exposes `What.Design`, `How.Design`, and `Impl.Exec` as selectable concerns rather than a rigid pipeline. A workflow exposes only the unresolved concerns needed for its `Target.Product`; `Touched.Decision.Cycle` governs material decisions inside each concern.

Any active loop may be interrupted for capture, audit, consolidation, implementation handoff, parking, splitting, or status work. The interruption preserves a compact return point and hands control back to the prior session state when it finishes.

## When To Load This Skill

- when a session needs index-grounded context or a custom index research pass
- when the user wants to control, inspect, interrupt, or resume a Hugentic session
- when designing or realizing a target product
- when editing, diagnosing, testing, or maintaining the index
- when discussing or modifying the index design itself
- when debugging index behavior or resolving design questions
