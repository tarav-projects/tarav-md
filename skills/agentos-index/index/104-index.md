> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

## Project.File.Index

- `Project.File.Index` is the file-level routing section of the `Index.Router`
- describes the project's file system at folder level, with individual files listed only when fundamental
- one sentence description per entry — token budget is tight, this is always-loaded context
- gives agents a structural map of where to look — not a complete listing, but the important entry points

****

## Index.Activation

- `Index.Activation` is the process of bootstrapping the `Index.Runtime` for a session
- handled by `agentos-index-activate` — a dedicated bootstrap skill
- loads the full index into context, then activates operating behavior
- activation is opt-in — triggered by `AGENTS.md` or manual invocation
- operational detail: `references/launch-runtime.md`

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

- `Project.Index.Skill` is the `<project>-index` skill that holds the public index
- the canonical public surface for the index — other skills assume it exists
- contains `index/`, `appendix/`, and `references/`

****

## Concept.Cite

- `Concept.Cite` is the inline citation notation for referencing related concepts: `[Concept.X, Concept.Y]`
- used when the relationship is relevant but doesn't come up naturally in the writing
- goes inline — next to the line it relates to, like academic paper citations

****

## Index.Surface.Layout

- `Index.Surface.Layout` is the expected directory structure for the index system
- public index: `skills/<project>-index/index/` — `000-index.md` router + `100-299` flat files
- public appendix: `skills/<project>-index/appendix/` — `Concept.Name-appendix.md`
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
