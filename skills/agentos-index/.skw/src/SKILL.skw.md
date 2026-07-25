---
name: agentos-index
description: "Workflow-neutral Package.Aux.Skill for the Agentos Index subsystem of agentos-pkg. USE WHEN you need index research, editing, diagnosis, testing, maintenance, or index design context."
---

# agentos-index

> $kw: --from Alignment.Mode --from Alignment.Surface --from Batchy.Skill --from Capture.Offer --from Gr.Req --from Index.Agendix --from Index.Appendix --from Index.Chapter --from Index.Depot --from Index.Enrichment --from Index.Line --from Index.Ontology --from Index.Skillware --from Line.Type --from Line.Type.Vocabulary --from Package.Aux.Skill --from Packages.Master.Agent --from Reviewed.Cite.Closure --from Skill.Module --from User.Attention --from User.Command --from User.Command.Arg --from User.Command.Section --from User.Command.Trigger
> --dev-from references/index-capture-context-assembly.skw.md

Workflow-neutral `Package.Aux.Skill` for the Agentos Index subsystem.

This skill is the public Batchy router for index work. It orients the caller to the subsystem by default and routes explicit operations such as `--search`, `--capture`, `--edit`, `--type`, `--link`, `--back-link`, `--gr-survey`, `--gr-review`, `--enrich`, and `--agendix` into named `Skill.Module`s.

This is a `Batchy.Skill`. Load `agentos-batchy-skills` for the full convention.

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

## User.Command.Section

This `User.Command.Section` declares the canonical commands below. Each accepted `User.Command.Trigger` resolves to one command, whose nested `User.Command.Arg` blocks govern target resolution.

### User.Command::Approve
- accept an approval-ready index draft in its current form without writing it
- triggers: `::approve`, `::approved`
- available: when `--capture`, direct `--edit`, a `Capture.Offer`, or an `--enrich` capture offer has one or more approval-ready drafts
- action: mark the resolved target approved and unlanded

#### User.Command.Arg::Target
- the draft, block, line, or revision to approve
- required: true
- resolution: Contextual
- examples: `::approve`, `::approved the block after the correction`

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

- this skill is the canonical public entry surface for working with the Agentos Index system
- it remains a `Workflow.Neutral.Skill` when no explicit arg is selected
- it routes into named modules for concrete index operations instead of splitting those operations into separate public skills
- later modules such as diagnosis or testing may be added without changing the public package entry surface

## What The Index Is

- the index is `Index.Skillware` — an executable artifact for project knowledge
- it is an `Alignment.Surface` between humans and agents
- it contains `Named.Concepts` written in `Kernel.Block::Index` blocks, organized in `Index.Chapter` files under `Index.Ontology`, routed by `000-INDEX.md`, with on-demand `Index.Appendix` depth
- the active chapter defaults to `design`; chapter files are named `NNN-<chapter>.md`
- index work happens over engaged `Index.Depot`s; `--depot` scopes which depots are engaged and `--chapter` scopes within them
- its lines carry `Line.Type` codes (`- [CT] ...`) classifying each line's act; untyped lines are pre-fence legacy
- its evidence links are `Anchory.Anchor`s (composed keys, `^c<YYYYMMDD>-<N><tag>` — namespace prefix + date + counter + optional turn tag): trailing on the lines they support — grounding is a line property (`Index.Line`) — resolving through chatlas back to the chats
- agents operate it by loading routers, concept blocks, appendix material, and references relevant to the current task

## Router Table

| Situation | Module / Surface |
|---|---|
| When the caller wants to find concepts, retrieve cited index context, inspect related blocks, discover whether appendix depth exists, understand how the index already models a topic, or ground the current visible discussion against the index; `--search`, `--research`, and `--ground` all call this module | `references/search.md` |
| When developing any managed `agentos-index` surface — load the complete common index subject universe before selecting direct dependencies, derivations, citations, or runtime-facing content | `references/index-context-assembly.md` |
| When the user wants the chat's content captured — "let's capture": load the index-capture context assembly, ground the chat and adjacent evidence, present a lightweight candidate roadmap, then codesign and land small approved clusters; `--capture` calls this module, `--agendix` calls its autonomous path with the agendix preset | `references/capture.md` |
| When a capture run needs its complete preparation context — index surface ontology, workflow-neutral writing modules, engaged-depot closure, and adjacent evidence categories — load the whole module as builder context | `references/index-capture-context-assembly.md` |
| When an index or appendix surface is being written or an approved edit needs landing — the gates, structure, naming, block quality, edit actions, drafting screens, and landing procedure that govern index writing; direct edit work (a stale line, a block revision) also starts here; `--edit`, `--write`, and `--append` all call this module | `references/edit.md` |
| When the caller wants deterministic diagnosis, linter findings, or post-edit validation for an index depot or explicit index/appendix surface; `--check` and `--lint` both call this module | `references/check.md` |
| When the caller wants line typing understood, read, or proposed — the `[XX]` syntax, the `Line.Type.Vocabulary`, validation points, reading typed lines as constraints, calibration passes and their residue | `references/type.md` |
| When material lands on the agendix or the caller needs the agendix surface understood — `agendix/` files under existing concepts, typed and anchored lines, ungated with hard provenance | `references/agendix.md` |
| When a caller needs an `Anchory.Anchor` minted for a chat context — session resolution, turn location, registration, verification; consumed by `--capture`, `--edit`, and `--agendix` | `references/link.md` |
| When the caller wants an existing block grounded backward — git dates the wording, chatlas finds the session and turns, the linking primitive mints, the gated edit lands the `[GR]` line | `references/back-link.md` |
| When the caller wants a grounding campaign surveyed — a scope swept, anchors minted, a `Gr.Req` produced with `proposed`/`ambiguous` entries, no index writes; `--gr-scout`/`--gr-scan`/`--gr-linker` are aliases | `references/gr-survey.md` |
| When the caller wants a `Gr.Req` reviewed — proposed entries walked with the user, statuses flipped, approved links landed through the gates, provenance re-verified | `references/gr-review.md` |
| When the caller wants a block enriched — `Index.Enrichment`: a scoped discussion with the user generating new touched surface, minted and landed through the gates; low-but-nonzero density blocks are the default targets | `references/enrich.md` |
| When the caller provides `--depot`, scope the selected operation to those `Index.Depot`s; otherwise use task-relevant engaged depots | applies to `references/search.md` and `references/edit.md` |
| When the caller provides `--chapter`, scope the selected operation to that `Index.Chapter` inside the engaged depots; default to `design` when no chapter is named | applies to `references/search.md` and `references/edit.md` |
| When the caller needs package-level understanding of how the index subsystem is designed, structured, and distributed across public and local surfaces | `agentos-pkg/design/`, `agentos-pkg/appendix/`, `agentos-pkg/references/` |
| When the caller needs concrete examples of good and bad block shape before proposing or judging block wording | `agentos-pkg/references/index-block-catalog.md` |
| When the caller needs behavioral testing of index entry paths, selection behavior, or usage patterns | `agentos-testground` |

## Index Operating Behavior

> $kw: --derived
> --from references/search.skw.md#Search Model
> --from references/search.skw.md#Citation Behavior
> --intent restate the search doctrine (routing-first selective loading, depot and
> --cont chapter scoping) and citation behavior as the operating checklist, and
> --cont extend it with the gate/capture lines the modules own

An agent operating the index should:

- search routing surfaces in the engaged `Index.Depot`s first, then load only relevant concept blocks, appendix material, or references
- read down the `User.Attention` gradient — the reviewed block and appendix first, then the top concept's unreviewed `Index.Agendix` leads; surface agendix material as leads, never as accepted citations (`Reviewed.Cite.Closure`)
- respect `--depot` as an `Index.Depot` scope; otherwise use task-relevant engaged depots
- respect `--chapter` as an `Index.Chapter` scope inside engaged depots; default chapter is `design`
- return context with source block citations so the caller can verify and maintain the summary
- distinguish discovered context from inference
- treat the prompt as a focus argument and compare the current visible discussion against the index whenever there is discussion state to ground
- make a `Capture.Offer` when work surfaces new aligned content: propose the exact typed line(s) at the moment, with destination options (index main, appendix, agendix, decline) — never self-write
- use `--capture` when the user wants the chat's content worked into the index — approval in chat and landing on a surface are distinct acts
- resolve `::approve` / `::approved` to `User.Command::Approve`, `::land` / `::write` to targeted `User.Command::Land`, and `::land-all-approved` to zero-argument `User.Command::LandAllApproved`; `--write` remains a skill argument while `::write` is an in-workflow transition
- during interactive capture, add approved drafts to the approved cluster and continue reviewing the roadmap; do not make immediate landing the default next move
- keep command targets foregrounded; targeted commands fail closed on ambiguous targets, and `::land-all-approved` fails closed unless one foreground index workflow owns the cluster
- use file mutation only when the user has approved an index edit
- run a linter check after applying an approved index or appendix edit

For delegated read-only research that protects the caller's context, use `Packages.Master.Agent` against the relevant package or packages.

> $kw. end

## Skill Modules

- `references/search.md` — routing-first search, selective loading, appendix discovery, citation behavior, and conversation-to-index grounding
- `references/index-context-assembly.md` — the whole-file shared builder context for every managed `agentos-index` surface
- `references/capture.md` — the capture workflow: the discussion-landing loop from chat content to index surfaces
- `references/index-capture-context-assembly.md` — the whole-file context assembly and grounding closure for working across a touched index
- `references/edit.md` — the knowledge of index and appendix writing: gates, actions, naming, placement, drafting screens, landing procedure, and maintenance
- `references/check.md` — deterministic index checks through `agentos index linter`
- `references/type.md` — line typing: syntax, vocabulary, validation points, reading typed lines, fence and residue
- `references/agendix.md` — the knowledge of the agendix surface: rules, landing form, boundaries — typed, anchored, ungated
- `references/link.md` — the linking primitive: mint and verify chat anchors through chatlas + anchory commands
- `references/back-link.md` — backward grounding: git history to evidence turns for existing blocks
- `references/gr-survey.md` — grounding campaign survey: scope sweep, minting, `Gr.Req` production (no index writes)
- `references/gr-review.md` — grounding campaign gate: per-entry user verdicts, gated landings, provenance close-out
- `references/enrich.md` — `Index.Enrichment`: block-scoped discussion generating new grounding surface, gated landings, density-delta receipt

## When To Load This Skill

- when a session needs index-grounded context or a custom index research pass
- when editing, diagnosing, testing, or maintaining the index
- when discussing or modifying the index design itself
- when debugging index behavior or resolving design questions
