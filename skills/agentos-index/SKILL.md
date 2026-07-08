---
name: agentos-index
description: "Workflow-neutral Package.Aux.Skill for the Agentos Index subsystem of agentos-pkg. USE WHEN you need index research, editing, diagnosis, testing, maintenance, or index design context."
---

# agentos-index

Workflow-neutral `Package.Aux.Skill` for the Agentos Index subsystem.

This skill is the public Batchy router for index work. It orients the caller to the subsystem by default and routes explicit operations such as `--search`, `--edit`, `--ground`, `--type`, `--link`, `--back-link`, and `--agendix` into named `Skill.Module`s.

This is a `Batchy.Skill`. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints usage and the public args without running.

## Skill.Arg.Section

### Skill.Arg:Search
- search the index through routing-first selective loading
- required: false
- help: "search the index and return cited context"
- examples: --search "Index.AGENTS.MD"

### Skill.Arg:Edit
- work the approved edit path for index or appendix changes
- required: false
- help: "use the index edit path for approved changes"
- examples: --edit "add Context.Hook"

### Skill.Arg:Write
- call the edit module
- required: false
- help: "use the index edit path for approved changes"
- examples: --write "add Context.Hook"

### Skill.Arg:Append
- call the edit module
- required: false
- help: "use the index edit path for approved changes"
- examples: --append "add a line to Context.Hook"

### Skill.Arg:Check
- run deterministic checks over index depots or explicit index surfaces
- required: false
- help: "run index checks"
- examples: --check --depot agentos-pkg

### Skill.Arg:Lint
- call the check module
- required: false
- help: "run index checks"
- examples: --lint --depot agentos-pkg

### Skill.Arg:Depot
- scope index work to one or more engaged index depots
- required: false
- default: task-relevant engaged depots
- help: "scope index work to an index depot"
- examples: --depot agentos-pkg, --depot agentos-chatlas-pkg

### Skill.Arg:Chapter
- scope index work to one chapter within the engaged depots
- required: false
- default: design
- help: "scope index work to a chapter"
- examples: --chapter design, --chapter impl

### Skill.Arg:Ground
- ground the current conversation or prompt against the index
- required: false
- help: "ground the current conversation against the index and report what matters"
- examples: --ground "check this design discussion against the index"

### Skill.Arg:Type
- read or propose `Line.Type` classification for index lines
- required: false
- help: "explain, read, or propose index line typing"
- examples: --type "type the Anchory.System block", --type "what binds me in this block?"

### Skill.Arg:Agendix
- capture `User.Touched` lines from the current conversation into the agendix
- required: false
- help: "run an agendix capture pass over the current conversation"
- examples: --agendix, --agendix "capture the grounding discussion"

### Skill.Arg:Link
- mint an `Anchory.Anchor` for a chat context — the linking primitive other modules consume
- required: false
- help: "mint an anchor for a chat evidence turn and return it"
- examples: --link "anchor the turn where the user picked syntax B"

### Skill.Arg:BackLink
- ground an existing index block backward: git history → session → turns → anchor
- required: false
- help: "recover chat evidence for an existing block and propose its grounding"
- examples: --back-link "Writing.Friction.Reduction", --back-link "ground the 107 chapter"

## Boundary

- this skill is the canonical public entry surface for working with the Agentos Index system
- it remains a `Workflow.Neutral.Skill` when no explicit arg is selected
- it routes into named modules for concrete index operations instead of splitting those operations into separate public skills
- later modules such as diagnosis or testing may be added without changing the public package entry surface

## What The Index Is

- the index is `Index.Skillware` — an executable artifact for project knowledge
- it is an `Alignment.Surface` between humans and agents
- it contains `Named.Concepts` written in `Kernel.Block:Index` blocks, organized in `Index.Chapter` files under `Index.Main`, routed by `000-INDEX.md`, with on-demand `Index.Appendix` depth
- the active chapter defaults to `design`; chapter files are named `NNN-<chapter>.md`
- index work happens over engaged `Index.Depot`s; `--depot` scopes which depots are engaged and `--chapter` scopes within them
- its lines carry `Line.Type` codes (`- [CT] ...`) classifying each line's act; untyped lines are pre-fence legacy
- its evidence links are `Anchory.Anchor`s (`@YYYYMMDD-N`): trailing on lines and collected in appendix `Grounding.Head`/`Grounding.Drift` sections, resolving through chatlas back to the chats
- agents operate it by loading routers, concept blocks, appendix material, and references relevant to the current task

## Router Table

| Situation | Module / Surface |
|---|---|
| When the caller wants to find concepts, retrieve cited index context, inspect related blocks, discover whether appendix depth exists, or understand how the index already models a topic before proposing changes | `references/search.md` |
| When the caller wants to draft, redraft, critique, tighten, or otherwise shape index-block or appendix-block wording; when the task is proposing concept text, revising a block, appending a line, or preparing an approved index or appendix edit; includes block-shaping work even before file mutation is approved; `--edit`, `--write`, and `--append` all call this module | `references/edit.md` |
| When the caller wants the current prompt or ongoing conversation grounded against the index; when the task is to surface the most relevant concepts, tensions, contradictions, significant accepted remarks, or missing coverage; when the caller wants the relationship between the live discussion and the existing index made explicit rather than running a raw lookup | `references/ground.md` |
| When the caller wants deterministic diagnosis, linter findings, or post-edit validation for an index depot or explicit index/appendix surface; `--check` and `--lint` both call this module | `references/check.md` |
| When the caller wants line typing understood, read, or proposed — the `[XX]` syntax, the `Line.Type.Vocabulary`, validation points, reading typed lines as constraints, calibration passes and their residue | `references/type.md` |
| When the user triggers agendix capture — harvesting `User.Touched` lines from the current conversation into `agendix/` files under existing concepts, typed and anchored, ungated | `references/agendix.md` |
| When a caller needs an `Anchory.Anchor` minted for a chat context — session resolution, turn location, registration, verification; consumed by `--edit` and `--agendix` | `references/link.md` |
| When the caller wants an existing block grounded backward — git dates the wording, chatlas finds the session and turns, the linking primitive mints, the gated edit lands the `[GR]` line | `references/back-link.md` |
| When the caller provides `--depot`, scope the selected operation to those `Index.Depot`s; otherwise use task-relevant engaged depots | applies to `references/search.md`, `references/edit.md`, and `references/ground.md` |
| When the caller provides `--chapter`, scope the selected operation to that `Index.Chapter` inside the engaged depots; default to `design` when no chapter is named | applies to `references/search.md`, `references/edit.md`, and `references/ground.md` |
| When the caller needs package-level understanding of how the index subsystem is designed, structured, and distributed across public and local surfaces | `agentos-pkg/design/`, `agentos-pkg/appendix/`, `agentos-pkg/references/` |
| When the caller needs concrete examples of good and bad block shape before proposing or judging block wording | `agentos-pkg/references/index-block-catalog.md` |
| When the caller needs behavioral testing of index entry paths, selection behavior, or usage patterns | `agentos-testground` |

## Index Operating Behavior

An agent operating the index should:

- search routing surfaces in the engaged `Index.Depot`s first, then load only relevant concept blocks, appendix material, or references
- respect `--depot` as an `Index.Depot` scope; otherwise use task-relevant engaged depots
- respect `--chapter` as an `Index.Chapter` scope inside engaged depots; default chapter is `design`
- return context with source block citations so the caller can verify and maintain the summary
- distinguish discovered context from inference
- use `--ground` when the caller wants the live discussion compared against the index instead of a direct query lookup
- use file mutation only when the user has approved an index edit
- run a linter check after applying an approved index or appendix edit

For delegated read-only research that protects the caller's context, use `Packages.Master.Agent` against the relevant package or packages.

## Skill Modules

- `references/search.md` — routing-first search, selective loading, appendix discovery, and citation behavior
- `references/edit.md` — approved edit path for index and appendix changes: gates, actions, naming, placement, edit loop, and maintenance
- `references/ground.md` — conversation-to-index grounding: derive the active themes, search selectively, and report matches, tensions, and gaps
- `references/check.md` — deterministic index checks through `agentos index linter`
- `references/type.md` — line typing: syntax, vocabulary, validation points, reading typed lines, fence and residue
- `references/agendix.md` — agentic capture path: typed, anchored `User.Touched` lines into the agendix, ungated
- `references/link.md` — the linking primitive: mint and verify chat anchors through chatlas + anchory commands
- `references/back-link.md` — backward grounding: git history to evidence turns for existing blocks

## When To Load This Skill

- when a session needs index-grounded context or a custom index research pass
- when editing, diagnosing, testing, or maintaining the index
- when discussing or modifying the index design itself
- when debugging index behavior or resolving design questions
