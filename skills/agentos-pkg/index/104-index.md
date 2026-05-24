> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Project.File.Index

- `Project.File.Index` is the file-level routing section of the `Index.Router`
- describes the project's file system at folder level, with individual files listed only when fundamental
- one sentence description per entry — token budget is tight, this is always-loaded context
- gives agents a structural map of where to look — not a complete listing, but the important entry points

****

## Index.Activation

- `Index.Activation` is the process of bootstrapping the `Index.Runtime` for a session
- handled through the `agentos-index` auxiliary skill or by a caller performing the `Index.Agent` role
- collects the relevant routing blocks, concept blocks, appendix material, and references for the current task
- activation is opt-in — triggered by `AGENTS.md` or manual invocation
- operational detail: `agentos-pkg/references/launch-runtime.md`

****

## Unresolved.Index.Name

- `Unresolved.Index.Name` is an unknown `Dotted.Name` that the agent cannot resolve against the index
- parked in the session — available for later resolution if more context emerges
- if the same name recurs 3+ times, suggest capture to the user
- gap detection is passive — don't interrupt conversation flow

****

## BuiltIn.Namespace

- `BuiltIn.Namespace` is an `Explicit.Namespace` that every Agentos project is expected to have
- it's an interface — can be empty, populated as the project evolves
- examples: `Project.Surfaces`

****

## Project.Index.Skill

- `Project.Index.Skill` is the `<project>-index` auxiliary skill for a package index surface
- the canonical public index content lives in the package skill, usually `skills/<package>-pkg/index/`
- it is a `Package.Aux.Skill` for the package's `Package.Skill.Index`
- the auxiliary skill may provide direct index access, research, writing, diagnosis, testing, maintenance, or index workflow framing without becoming a separate package root

****

## Concept.Cite

- `Concept.Cite` is the bracket notation for citing concept origins or materially important related concepts when inline mention is not natural
- format: `[Concept.X, Concept.Y]`; page or source qualifiers may be added when needed, e.g. `[Concept.X, Concept.Y[1]]`
- used when the citation changes how an agent should interpret, verify, maintain, or navigate the line
- not used merely because another concept is loosely related
- complements `Inline.Relatedness`: prefer natural inline `Dotted.Name` mentions, cite only when the relation matters but does not read naturally

****

## Index.Surface.Layout

- `Index.Surface.Layout` is the expected directory structure for the index system
- public index: `skills/<package>-pkg/index/` — `000-index.md` router + `100-299` flat files inside the package's `Package.Skill.Index`
- public appendix: `skills/<package>-pkg/appendix/` — `Concept.Name-appendix.md`
- local index: `notes/index/` — `001-index.md` router + `300-499` flat files
- local appendix: `notes/appendix/`
- the layout is a protocol — new projects follow this structure to be index-compatible

****

## Appendix.Discovery

- `Appendix.Discovery` is the protocol for loading depth on demand from the appendix
- trigger: when reasoning about a concept and the index block isn't sufficient
- discovery: if working with `Concept.X`, check `appendix/Concept.X-appendix.md`
- no outlink required — the naming convention is the discovery mechanism
- discovery is a cascade: index block → its appendix → hidden blocks → their appendixes
- the more blocks loaded, the more paths available — agents discover by following related blocks
- hidden blocks are not deleted — just not in the starting context
- related blocks cluster under the same appendix file when they extend related concepts

****

## Appendix.Pages

- `Appendix.Pages` extends `Appendix.Discovery` with progressive depth layers
- `Concept.X` is sugar for `Concept.X[0]` — the index block
- `Concept.X[1]` is the first appendix page (`Concept.X-appendix.md`)
- `Concept.X[2]+` are deeper pages (`Concept.X-appendix-2.md`, `Concept.X-appendix-3.md`, etc.)
- `Concept.X[:]` means all content — index block + all appendix pages (JS slice semantics)
- the notation is usable as inline reference in blocks, chat, and prompts
- discovery cascades naturally — if depth is insufficient, go deeper: more pages, or jump to other concepts
- the routing table annotates page count inline: `Concept.X[+2]` — lintable, only present when appendix exists
- no annotation means no appendix — `Concept.X` alone implies `[0]` only

****

## Placement.Heuristic

- `Placement.Heuristic` is the decision framework for where content lives in the system
- design knowledge (what, why, how it connects) → index block + appendix
- executable instructions (do this, run that, follow this loop) → skill references
- if content drift is detected, report it — don't migrate without user approval

****

## Install.Skill

- `Install.Skill` is a convention where a skill package ships guidance for adopting its support into a project
- lives in the package's `references/` as installation instructions
- can be executed agentically (agent follows the steps) or hugentically (human-agent design loop)
- example: installing the index system creates `notes/index/`, `001-index.md`, routing table
- example: installing the agentos stack sets up `AGENTS.md`, `notes/`, `skills/`

****

## Index.Empirical.Placement

- `Index.Empirical.Placement` is evidence-driven placement of content across index layers
- complement to `Placement.Heuristic` — design judgment places initially, empirical data optimizes over time
- evidence source: chat sessions across projects, accessed through `Chatlas.Query.Surface`
- the core signal is comparative — content at the same depth level should have similar usage profiles
- the working unit is flexible — a block, a line within a block, or a group of related blocks
- output is a migration plan — proposed moves with evidence, user approves before execution

****

## Alignment.Surface

- `Alignment.Surface` is a surface where humans and agents build shared understanding
- readable by humans (natural language), operable by agents (structured, loadable)
- neither side owns it alone — both contribute, both consume
- the index is the primary `Alignment.Surface` of an Agentos project

****

## Index.Agent

- `Index.Agent` is a role for collecting, interpreting, and returning context from the index
- `Index.Agent` is index-capable, not index-bound; it operates under `Multi.Index.Operation` unless explicitly constrained
- can be performed by a dedicated specialist agent or temporarily by a workflow agent
- the caller sends a prompt; the `Index.Agent` scans the index, does the work, and returns a result
- the caller's context is protected — the `Index.Agent` pays the cost of loading the full index, not the caller
- useful for discovery, uncertain queries, custom context extraction, and index-grounded synthesis
- not required as the default prelude when a workflow already knows its needed cited context
- must cite source blocks in returned context so summaries remain traceable and maintainable
- not a fixed API — handles any reasonable prompt against the index
- backed by the `agentos-index-agent` skill: index conventions, block structure, routing, CLI tools, appendix discovery
- can run on a medium-size model — structured, scoped work
- the caller retains direct index access when the index *is* the work target
- the caller can pass context in the prompt — a chat summary, already-loaded blocks, a topic, a question
- common patterns: grounding (pass chat summary, get relevant blocks), search (find blocks by topic), placement (where to write a new block), filtering (return namespace members minus already-loaded blocks)

****

## Multi.Index.Operation

- `Multi.Index.Operation` is the default operating condition of an `Index.Agent`
- an `Index.Agent` is not inherently attached to one index
- session context may bias the agent toward a default index, such as the active project index or currently loaded package index
- explicit user direction may also constrain which index or indexes to use
- without such constraints, the agent should treat all accessible relevant indexes as possible sources of context, citations, and conflict
- applies to index research, context collection, writing, citation, maintenance, conflict detection, and package dependency traversal
- accessible indexes may include the active project's local index, the active package index, dependency package indexes, and explicitly provided external package indexes
- agents should avoid blind exhaustive loading; search likely relevant indexes first and load only useful blocks, appendix material, or references
- concepts cited or returned from a non-default index should use qualified names, such as `<package>-pkg/Concept.Name` or `local/Concept.Name`
- disagreement across indexes is surfaced as an issue, not silently merged
- writes must respect the target index's placement rules and write gates

****

## Index.Depot

- `Index.Depot` is a concrete index instance — the set of files with index blocks, their appendix, and a router
- built on the `Agentos.Index.Framework` — follows the same block structure, routing, writing, and discovery conventions
- one depot = public part (skill-packaged, portable) + local part (`notes/index/`, project-specific)
- each depot is self-contained — its own router(s), its own flat files, its own appendix
- a concept lives in exactly one depot — the depot that naturally owns it
- composability: an agent loads multiple depots to build its working index
- the `Index.Agent` works across all loaded depots — it scans whatever routers are available

### meta

- aliases: `Agentos.Index.Depot`

****

## Provider.Instance

- `Provider.Instance` is a concrete binding of a `Provider.Family` to a local environment
- a `Provider.Family` is a supported AI assistant provider (e.g., claude-code, codex, copilot-cli, gemini-cli, opencode, pi, openclaw)
- two interpretations coexist:
  - runtime: a fully configured system — provider, home, account — such that it can run
  - disk: the observable footprint — mostly provider and home directory
- the disk interpretation is often interchanged with the concept of provider home, because the home directory is the primary observable artifact
- instance identity is derived from the provider family and environment fingerprint
- provider home discovery is declarative — each family specifies known paths, file patterns, and database locations to locate its home directory

****

## Index.Linter

- `Index.Linter` is the deterministic CLI checker for index and appendix surfaces
- finding and check codes are scoped concept names under `Index.Linter/...`
- each code names an appendix block that explains meaning, gating, or expected remediation
- agents resolve linter code meaning through normal `agentos-pkg` index and `Appendix.Discovery`
- router entries use `[+N]` to expose discovered appendix page depth for routed concepts
- the linter reports errors, warnings, blocked checks, and summary counts; semantic diagnosis belongs to `agentos-index-doctor`
