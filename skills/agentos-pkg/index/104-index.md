> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Project.File.Index

- `Project.File.Index` is the file-level routing section of the `Index.Router`
- describes the project's file system at folder level, with individual files listed only when fundamental
- one sentence description per entry — token budget is tight, it travels with the router whenever the index is loaded
- gives agents a structural map of where to look — not a complete listing, but the important entry points

****

## Index.Activation

- `Index.Activation` is the process of bootstrapping the `Index.Runtime` for a session
- handled through the `agentos-index` auxiliary skill or directly by an index-capable caller
- collects the relevant routing blocks, concept blocks, appendix material, and references for the current task
- activation is opt-in — triggered by `AGENTS.md`, a `Package.Driver`, or manual invocation; the index has no loading policy of its own
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

## Index.Depot

- `Index.Depot` is a concrete index instance — the set of files with index blocks, their appendix, and a router
- built on the `Agentos.Index.Framework` — follows the same block structure, routing, writing, and discovery conventions
- one depot = public part (skill-packaged, portable) + local part (`notes/index/`, project-specific)
- each depot is self-contained — its own router(s), its own flat files, its own appendix
- a concept lives in exactly one depot — the depot that naturally owns it
- composability: an agent loads multiple depots to build its working index
- an index-capable agent works across all loaded depots by scanning their available routers

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
- the linter reports errors, warnings, blocked checks, and summary counts

****

## Write.Trigger.Gated

- `Write.Trigger.Gated` is a gating constraint: the user must explicitly initiate the write — the agent never starts writing on its own
- asking "should I write this?" is allowed; opening an editor without approval is not
- applies to any surface that wants human control over when mutation happens
- distinct from `Content.Verbatim.Gated`, which gates what is written rather than when
- a surface can apply one or both gates independently
- operational detail: `agentos-index-writer`

****

## Content.Verbatim.Gated

- `Content.Verbatim.Gated` is a gating constraint: the user must approve the exact wording before it is committed
- the agent proposes; the user settles — no silent rewrites or unreviewed content
- implies `Write.Trigger.Gated` — if content is gated, the trigger is necessarily gated too
- supports `Hugentic.Alignment` — the review point is where human judgment shapes the surface
- operational detail: `agentos-index-writer`

****

## Kernel.Note

- `Kernel.Note` is a portable markdown file made to contain `Kernel.Block` sections
- it is a collection surface for blocks, not a block type
- it captures or develops the fundamental structure of a subject by grouping named blocks in one file
- source material can be any inspectable thing: chat, skill, codebase, document, argument, or observed system behavior
- it can be produced from an existing corpus or maintained during an active conversation
- unlike `Kernel.Block:Index`, a `Kernel.Note` is not necessarily part of an index or routing table
- its purpose is portable block collection, conceptual extraction, and argument substrate
- a `Kernel.Note` can later be promoted into index blocks, appendix material, design artifacts, or implementation guidance
