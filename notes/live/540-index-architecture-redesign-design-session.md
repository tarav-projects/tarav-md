# Index Architecture Redesign — Design Session

## Session.Abstract

- grounding session for this design: `99144906-781e-43cc-9d27-b40f166e2acf`
- revisit/redesign all Agentos Index concepts to converge the generalized-index model
- this artifact is the temporary home for the updated blocks; migrate into `agentos-pkg/index/` later, safely, once converged
- convergence so far: the Index is a system of **chapters** + appendix + router
    - **chapters** = load-partition folders (default `design`, reserved `design`/`impl`, extensible, files `NNN-<chapter>.md`)
    - **`000-INDEX.md`** = chapter-sectioned lookup table (renamed from `000-index.md`; the `000-` prefix is the grep marker, `INDEX` the name)
    - **appendix** = part of the Index but not a chapter — depth, discovered not routed
    - default search scopes to `design`; other chapters load only on an explicit miss
- proof-of-shape already applied additively to `agentos-chatlas-pkg` (`design/` + `000-INDEX.md`)

## Design.Index

- concept blocks land here as each converges
- redesign order: `Index.Chapter` (keystone) → `Index.Architecture` → `Index.Surface.Layout` → `Flat.Index.Architecture` → `Index.Router` → `Index.Block` → depth-layer concepts → distributed/depot
- NEW target (split out of `Index.Router`): the search-scope concept — search has a `scope` variable defaulting to the `design` chapter, widened explicitly; lives in the search workflow, not the router
- `Tail.Capture` written — the standing duty to capture a discussion's tail (parallel alignment-loop task, user-gated, Natural.Placement-governed); closes the appendix-cluster's "user data loss" gap
- skill-side TODO: `agentos-hugentics-designer` should treat tail-capture as a parallel consolidation concern; `agentos-hugentics-capture-audit` is its operational form

### Index.Chapter
- `Index.Chapter` is a folder of the Index that groups concepts into a unit of selective loading
- concepts across chapters are peers, reached by one `Dotted.Name` lookup — a chapter sets only what loads together
- the chapter loading policy is open — if any default holds, only the default chapter is loaded/searched
- the default chapter is `design`; `impl` is reserved; a package may add any number beyond these
- a chapter's files are named `NNN-<chapter>.md`, e.g. `design/100-design.md` — the suffix names the chapter

#### appendix
- `000-INDEX.md` routes every chapter; the appendix is the Index's depth layer, reached by naming (`Appendix.Discovery`), not routed as a chapter
- a concept may carry its chapter as an optional `Dotted.Name` prefix (`Impl.Concept.A`)

### Agentos.Index.System
- `Agentos.Index.System` is the Agentos Index taken as a whole — the operable system of named concepts agents reason with
- it is a curated `User.Touched` surface — it indexes the `Touched.Space` of the project's other surfaces, the `Chat.Surface` foremost
- it is a `Hugentic.Concept` surface — user and agent collaborate over it: the agent constructs, the user gates
- it enables semantic computation over those concepts: composing them, finding contradictions, detecting design weakness

#### meta
- aliases: `Agentos.Index`

### Agentos.Index.System/Appendix
- it is `Index.Skillware` for project knowledge — a library of micro-prompts invoked by naming
- mentioning a `Dotted.Name` triggers a concept-level context load
- it manipulates the agent's context window — by controlling what enters context, you control how the agent reasons
- it is an `Explicit.Namespace` grouping the concepts that compose the index system
- the Index is a nested indexing surface — each layer indexes the one beneath it: the surface indexes the project's content across its `Surface.Types` (the `Chat.Surface` foremost), the chapters index the surface, the `Index.Router` indexes the chapters; "the index" resolves by context, the `Index.*` names disambiguate the layers

### Agentos.Index.System/Index.Surface.Layout
- `Index.Surface.Layout` is the directory protocol a package follows to host an Index
- a hosted Index is a `000-INDEX.md` lookup over one folder per `Index.Chapter`, plus a shared `appendix/`

public Index — in the package skill:
```
skills/<package>-pkg/
├── 000-INDEX.md          — concept→file lookup, sectioned by chapter
├── design/            — default chapter;     NNN-design.md
├── impl/              — reserved chapter;     NNN-impl.md
├── <chapter>/         — any further chapter;  NNN-<chapter>.md
└── appendix/          — shared depth;         Concept.Name-appendix.md
```

- each `Index.Depot` follows this shape, whether owned by a project (under `notes/`) or a `Package.Skill`; they compose via `Index.Discovery`
- the layout is a protocol — a package follows it to be Index-compatible
- within a chapter, files are flat and anonymous; writing appends to the last file, so placement is never a writing decision
- splitting an overfull file is maintenance, not a writing concern

### Writing.Friction.Reduction
- `Writing.Friction.Reduction` is the principle that the Agentos system lowers the cost of capturing design as it is discussed — by routing capture to the surface whose friction matches it
- friction is a designed gradient, and friction buys authority: `Chat.Surface` (free — talk is capture) → `Agendix` (zero user friction, agent-driven, no authority) → `Index.Appendix` (`Kernel.Line`-level approval) → `Index.Main` (`Kernel.Block`-level work unit)
- the aim is to capture as much of the user's design as possible before it is lost — structure is deferred, not skipped
- the index keeps a friction floor on purpose — too-cheap writing would flush the hugentic surface; the friction is part of the alignment
- on touched surfaces the approval gate stays — friction drops, the gate does not

### Agendix
- `Agendix` is the agent-driven shadow of the Index — an untouched member of the index surface, one file per `Index.Main` concept: `agendix/Concept.X-agendix.md`, next to `appendix/`
- it is a cache the agent keeps to aid grounding on stable surfaces — no stable surface may link into it; promotion copies an entry out through the normal gates (including into the index)
- the agent cannot mint concepts — it attaches lines under existing routed concepts; the ontology primes the capture, the agent fills the gaps — the index's shadow, not a second index
- hard rule: every line is a grounded summary of chat discussion — a rejection, a constraint, a highlight the index does not yet capture — carrying its `Chat.Ref`/`File.Mention` pointer; unsourced agent reasoning does not belong
- writing rules are the appendix's — `Kernel.Writing` discipline, the same block and line forms; only the supervision differs: all work is done and supervised by agents
- capture is user-triggered but not gated — the agent may suggest a capture pass, never start one
- it extends the `Block.Line.Gradient` past the touch cut: fundamentals → `Concept.X/Appendix` (touched tail) → the concept's agendix shadow tail (untouched)
- homeless material lands in a fallback file — misfit pressure is evidence a concept is missing (concept-gap detector)
- it is index-adjacent, not part of the index — it softens the index principles on the fly, replacing the direct user touch with a grounding link to the touch event
- it is self-similar to the appendix — an untouched appendix, same form and rules; it exists because the user gate is the bottleneck: a surface for the agent to run ahead of the gate
- agendix and appendix must not duplicate content — over time the agendix drains: entries reviewed by the user are promoted through the gate or dropped
- in alignment terms: `Untouched.Space` made durable — visible, assumed untouched by the user, non-aligned; zero authority, freely rewritable; everything in it is promotion evidence

### Concept.Explosion
- `Concept.Explosion` is the failure where splitting every fact into its own named concept floods the index with low-value names
- a name should be a real node in the system's mental model — earned by being worth navigating to, not minted for every fact
- the remedy is to append a fact to the nearest fitting concept rather than name it
- slight misplacement is acceptable — capture beats taxonomy; the fact is recorded and can be relocated later
- the appendix absorbs what does not deserve a name
- heuristic: a block with no cites on any surface (`Name.As.Index`) is a candidate to fold into another concept — nothing navigates to it

### Block.Line.Gradient
- `Block.Line.Gradient` is the ordering of a concept's lines from most fundamental to most accidental
- line 0 is typically a direct definition (`Concept.X` is …); each later line tends to be more specific than the one before
- the order continues unbroken into the appendix — the appendix is the tail of the same sequence, not a separate object
- the further down the sequence a line sits, the less fundamental to the concept it can be — the tail admits lines merely filed under it
- the index/appendix split — and the cuts between appendix pages — are artificial cuts on this sequence, placed for token economy
- fundamentals are the prefix you keep if you can read only a few lines; the appendix is the rest, loaded on demand
- coherence is a gradient too: tight in the fundamentals, relaxing in the appendix, where loosely-related lines accrete without earning the core's coherence

### Appendix.Default.Block
- `Appendix.Default.Block` is the catch-all block every concept has by default, addressed `Concept.X/Appendix`
- its name is the full path — a child block of the `Concept.X` node, sharing the `Concept.Scoping` container-first notation
- it holds the tail of the concept's `Block.Line.Gradient` — the lines past the index/appendix cut
- it has no space budget — it grows freely, in `Kernel.Writing` style (direct, orthogonal lines)
- it is the landing site for `Writing.Friction.Reduction` capture and `Concept.Explosion` appends — facts filed under a concept without minting a name
- a further cut opens a page at `Concept.X/Appendix/2`

### Block.Path
- `Block.Path` is a block name written as a `/`-separated path — the full path is the name
- the root segment is a `Dotted.Name`, a top-level index concept; the path anchors on that node
- later segments may be `Dotted.Name` concepts or free labels; an author composes any path that organizes the block
- a concept segment carries `Concept.Scoping` semantics; a label segment just groups, claiming no ontology entry
- a path-named block is attached to its root and lives in the root's appendix by default — it is not itself a top-level index block
- section paths (`Concept.X/Appendix`, `Concept.X/Grounding`) are restricted to the appendix; a scoped concept-child defaults there but may be promoted

### Block.Path/Appendix
- resolution is soft and per-segment — concept segments gain meaning, label segments stay plain
- the path need not mirror the file system, but by default it does — `Concept.X/Y` resolves into `Concept.X`'s appendix file
- inside an appendix file the root is implicit — `Concept.X-appendix.md` roots every block at `Concept.X`, so a heading `Appendix` is the full path `Concept.X/Appendix`, `Concept.Y` is `Concept.X/Concept.Y`
- `./Child` abbreviates a child of the current root, legal only where a root is already established — the `namespace-members` list and appendix-file headings; in free prose spell the full `Block.Path`
- the outblock form of a `Kernel.Block.Section` is a path-named block — `Concept.X/Grounding` is the grounding section, outblock

### Block.Path/Concept.Scoping
- `Concept.Scoping` is the semantics of a concept-valued `Block.Path` segment — the block is hosted under that concept, viewed through its lens
- it captures a relationship that belongs to neither concept alone, read in the host's context
- the same concept can be hosted by several paths, each a distinct view
- example: `Agentos.Index.System/Index.Surface.Layout`

### Kernel.Block.Section
- `Kernel.Block.Section` is a named part of a `Kernel.Block`
- fundamentals are the root `Concept.X` block itself — the block is its fundamentals
- meta is always inblock — non-conceptual data kept with the concept so it loads alongside it
- appendix and grounding are path-children placed outblock by default: `Concept.X/Appendix`, `Concept.X/Grounding`, loaded on demand
- the path is the name; outblock placement (in the appendix) is the default for these depth sections

### Kernel.Block.Fundamentals
- `Kernel.Block.Fundamentals` is the conceptual core of a `Kernel.Block` — the root block, what `Concept.X` is
- it is the only required section; a block is its fundamentals, the rest is optional
- it carries the concept itself: definition, boundaries, judgments, and relations, one dimension per line
- it pays off the heading's conceptual commitment — what the block is about
- it is the compressed prefix of the `Block.Line.Gradient`; extended depth continues in `Concept.X/Appendix`

### Kernel.Block.Meta
- `Kernel.Block.Meta` is the meta section of a `Kernel.Block` — non-conceptual data about the block as an object, never its subject
- always inblock — kept with the concept so it loads alongside it (findability)
- the strip-test: remove the line; if the block's conceptual load is unchanged, it belongs in meta
- `alias` is the paradigmatic field: alternate names that widen query hits without changing meaning

### Kernel.Block.Appendix
- `Kernel.Block.Appendix` is the extended-depth section of a `Kernel.Block`, addressed `Concept.X/Appendix`
- it is `Kernel.Writing` at relaxed constraints: coverage over compression, format-rich allowed
- it holds rationale, edge cases, examples, rejected alternatives — depth past the compressed fundamentals
- it is first-class extended writing, not a hiding place for less-important blocks
- it is the tail of the `Block.Line.Gradient`, loaded on demand (`Appendix.Discovery`)
- distinct from `Appendix.Block`, which is a whole `Kernel.Block` placed in the appendix file

### Kernel.Block.Grounding
- `Kernel.Block.Grounding` is the grounding section of a `Kernel.Block`, addressed `Concept.X/Grounding`
- it is a mechanical `Hard.Evidence` linking system — it links the block to where its evidence lives
- it carries `Grounding.Entry` links and their evidence notes, never agent reinforcement or commentary
- a grounding source can be a `Chat.Ref`, a `File.Mention`, a web page, or another evidence surface
- grounding lives only on index/appendix blocks; downstream surfaces cite the grounded block instead of re-grounding
- `*HEAD*` marks the active current grounding for the block

### Index.Surface
- `Index.Surface` is the file surface of one Index — `Index.Router`, `Index.Main`, and `Index.Appendix` taken as a single addressable surface
- it is a `Surface.Concept`: the bytes on disk, distinct from `Agentos.Index.System`, which is what those bytes do (the operable `Index.Skillware`)
- it follows the `Index.Surface.Layout` directory protocol; one `Index.Surface` per `Index.Depot`
- it is the outermost layer of the nested index — the index of the project across its surfaces (`Surface.Types`), foremost the `Chat.Surface` where design originates

### Index.Appendix
- `Index.Appendix` is the appendix layer of the Index and the root concept for it — the on-demand depth, complement of `Index.Main`
- it is the index-level echo of `Kernel.Block.Appendix`: depth deferred out of the compressed front, loaded by choice
- it is not routed — reached by naming through `Appendix.Discovery`, never loaded by default
- loading an appendix is an intentional action — the agent displays intention by choosing to go deeper
- it lives in one `appendix/` shared across chapters; files are concept-named and addressed as `Index.Pages`
- it holds every concept's tail (`Block.Line.Gradient`): `Concept.X/Appendix` catch-alls and scoped `Concept.X/Concept.Y` blocks (`Appendix.Block`)
- with `Index.Main` and `Index.Router` it composes the `Index.Surface`

### Index.Main
- `Index.Main` is the main body of the Index — the routed layer of concept fundamentals, spanning the `Index.Chapter` folders
- it is the index-level echo of `Kernel.Block.Fundamentals`: the compressed front, with depth deferred to `Index.Appendix`
- it holds the `Index.Block`s under tight `Kernel.Writing` compression, every one routed by `Index.Router`
- it is the complement of `Index.Appendix` — main body vs appendix, the split a book makes: main is routed, appendix is discovered (`Appendix.Discovery`)
- with `Index.Appendix` and `Index.Router` it composes the `Index.Surface`

#### meta
- aliases: `Index.Fundamentals`

### Index.Main/Appendix
- named `Index.Main` for the book parallel — main body vs appendix
- rejected `Index.HEAD` — collides with `*HEAD*`, the active-grounding marker (`Kernel.Block.Grounding`)
- rejected `Index.Root` — collides with the `Block.Path` root segment
- rejected `Index.Base` — leans "foundation"; the layer's real property is "primary / default"

### Index.Router
- `Index.Router` is the lookup table of the Index — `000-INDEX.md`, loaded first when the Index enters context (per the `Package.Driver`)
- it routes concept name → file, sectioned by `Index.Chapter`
- the appendix is not routed — appendix depth is reached by naming (`Appendix.Discovery`), not listed here
- it also carries file routing (`Project.File.Index`) — important project files for research
- entries may carry a one-sentence hint, but depth lives in the blocks themselves
- the routers of the engaged `Index.Depot`s compose into one working Index (`Index.Discovery`)

### Index.Pages
- `Index.Pages` is the file dimension of a concept — the pages its content spans, written `Concept.X[N]`
- `Concept.X[0]` is the index block's file; `Concept.X[1]` is the first appendix file (`Concept.X-appendix.md`); `[2]+` are further files
- `Concept.X[:]` means all of a concept's content across its files (slice semantics)
- it is orthogonal to `Block.Path` — pages address files, paths address the ontology; one page holds many path-blocks
- by default a path block lands in the matching page, but the two axes need not coincide
- the router annotates page presence inline (`Concept.X[+N]`) — lintable, only when appendix files exist

### Appendix.Discovery
- `Appendix.Discovery` is the protocol for reaching a concept's depth on demand — the appendix is not routed, it is found by naming
- loading appendix depth is an intentional act — the agent goes deeper by choice, never by default
- if a concept's block is not enough, check `appendix/Concept.X-appendix.md`; the naming convention is the discovery mechanism, no outlink needed
- that file holds the concept's path-children — its `Concept.X/Appendix` dump and any scoped `Concept.X/Concept.Y` blocks
- discovery cascades: a block → its appendix → the blocks there → their own appendixes
- hidden blocks are not deleted — just outside the default scope, reached by following the cascade

### Index.Block
- `Index.Block` is a `Kernel.Block` placed in an `Index.Chapter` — the routed, loadable unit of meaning in the Index
- its heading is a `Dotted.Name`, the root of the concept's `Block.Path`s and what `000-INDEX.md` routes
- it is `Kernel.Writing` under tight compression — conceptual completeness in few lines, depth pushed to `Concept.X/Appendix`
- it must carry enough signal for an agent to reason correctly about the concept
- the Index must have a block for any meaningful concept; it may link out rather than define everything inline
- `Content.Verbatim.Gated` — user approves exact wording before commit
- it must not become a transcript, changelog, dashboard, task list, or implementation dump

#### meta
- aliases: `Global.Block`, `Concept.Block`

### Appendix.Block
- `Appendix.Block` is a `Kernel.Block` placed in the appendix — a path-child of a concept (`Concept.X/Appendix`, `Concept.X/Concept.Y`)
- it is `Kernel.Writing` at relaxed constraints — depth over compression, no line-count ceiling, though line-length discipline still applies
- content is not limited to conceptual depth — specs, raw ideas, parked material belong, filed under the nearest concept (`Concept.Explosion`)
- the discipline is at the insertion point — find the right concept, then write freely under it
- `Edit.Trigger.Gated` only — the user initiates, but exact wording is not gated; the low-friction half of `Writing.Friction.Reduction`
- reached by `Appendix.Discovery`, not routed

### Tail.Capture
- `Tail.Capture` is the parallel task in the alignment loop of growing a concept's tail alongside its fundamentals
- the tail is the accepted constraints, issues, edge cases, and rejected alternatives — the `Block.Line.Gradient` past the fundamentals
- working a concept is working both: most turns grow the tail, while the fundamentals stabilize and change less
- it stays user-gated — captured through the alignment loop like any index/appendix write, not auto-written
- the default move: append a valuable, accepted point to the nearest concept's appendix (`Appendix.Default.Block`, `Concept.Explosion`)
- the tail is subject to `Natural.Placement` — it holds what no other surface holds, or what is worth stating more explicitly here
- dropping the tail is the main way user-discussed design is lost; fundamentals survive, the rest evaporates

### Index.Depot
- `Index.Depot` is a self-contained Index instance — its own `000-INDEX.md`, chapters, and appendix
- it follows `Agentos.Index.System` conventions
- a depot belongs to a surface — a project or a `Package.Skill` — and is engaged like any other, no depot privileged
- the same concept name may exist in two engaged depots; the system surfaces the collision, it does not prevent or resolve it
- it loads with its owner through the `Package.Driver` (`Context.Loading.Path`)

### Index.Discovery
- `Index.Discovery` is how an agent finds the `Index.Depot`s available to engage
- a depot is marked by a `000-INDEX.md` — its presence identifies an engageable index on a skill or project
- declared discovery walks the dependency graph: a project's `Project.Manifest` and each package's `Package.Manifest`
- fallback discovery: when nothing declares them, search for `000-INDEX.md` across skills and projects — cheap
- discovery is hierarchical (the dependency graph) but engagement is flat — discovered depots are peers, routed equally
- a workflow scopes the discovered set by agent common sense — conversation context, skill descriptions, task relevance — defaulting to the whole engaged set

### Project.Manifest
- `Project.Manifest` is a project's declaration of the `Package.Skill`s and indexes it engages — the project peer of `Package.Manifest`
- it lives in the project's `AGENTS.md`
- with `Package.Manifest` it forms the dependency graph `Index.Discovery` walks
- it is optional — without it, `Index.Discovery` falls back to searching for `000-INDEX.md`

### Explicit.Namespace
- `Explicit.Namespace` is a concept whose purpose is to group a cluster of blocks — a declared view over the concepts it gathers
- its members are listed in `#### meta` under `namespace-members` — the inventory of the cluster
- a member is either a grouped peer (a routed `Index.Block` standing on its own) or an owned child in the namespace's appendix
- the member list is where appendix-depth members surface — path-children the `Index.Router` never routes, otherwise reachable only by `Appendix.Discovery`, are named here
- the appendix is required — it is the namespace's home, holding the owned children and the guided view over the cluster
- member shape carries the relation: bare `Dotted.Name` = grouped peer, `./Child` = owned child (`Block.Path`), `Other/Child` = grouped foreign child

### Chat.Surface
- the `Chat.Surface` is the largest, most complete record of a project's design — user data lands here first, before any digestion
- the index is a curated cache over the `Chat.Surface`, not a gate: an undigested concept is retrieved from the chats, never a reason to stall (no design-paralysis)
- in alignment terms it holds the raw touch events: user turns are `User.Touched` surface, assistant turns are touched-adjacent — the context around the touch, not the touch itself
- the index is the index *of* the `Chat.Surface` for the project — the nested-index relation, at the surface level
- not every cycle starts with design; work may run implement-first, with digestion deferred to cold consolidation (`Index.Edit.Action`)
- all `Chat.Surface` access is through Chatlas; the project's attributed chats are `Projects.Chats`, searched by `Chat.Retrieval`

### Chat.Surface/Appendix
- `Projects.Chats` is the chat set attributed to a project — its own sessions plus its ancestors': for `A/B/C`, the union of `A/B/C`, `A/B`, `A` (walk the path via `chatlas query --project`, one query per level — match is exact, no prefix)
- `Chat.Retrieval` is the user-triggered "where did we last discuss X", over `Projects.Chats`, cheapest-path-first:
  - tier 1 index — digested → a named block (cache hit)
  - tier 1.5 agendix — agent-cached grounded lines pointing into the chats (`Agendix`)
  - tier 2 git-anchored — `git log` on touched files → date range → `chatlas query --active-after` → sessions (precise, cheap)
  - tier 3 direct — `chatlas query --user-contains` / `chatlas recents` over the turns (broad, complete)
  - read a hit via Chatlas views: `summary` as the cheap filter, `zip-transcript` as the trusted raw turns (`We.Distrust.Summaries`)
- two situations: chat-only work (worst case, but the data is there) vs work with file consequences (best — git bridges files→sessions)
- digestion gradient (extends the `Block.Line.Gradient` capture axis): index block → appendix line (`Append.Line`) → agendix line (ungated, grounded) → chat-in-place, retrieved on demand (the zero-digestion floor)
- firing is user-triggered by default; the trigger mechanism is secondary to the retrieval design
- open: `chatlas query --active-after` is a lower bound only; a true date range needs an upper bound (client-side trim or an `--active-before`)
- mostly composition — Chatlas `query`/`recents`/`views` and `chatlas-grounding-agent` git-grounding already exist; this names them as a retrieval layer

### Kernel.Line
- `Kernel.Line` is the atom of index content — one statement carried by a block, the unit that accretes
- it is read in the context of its block: the block is the frame, so a line stays terse and may omit what the block already establishes (`Name.As.Index`)
- one point per line is a soft direction, not a rule — the violation is one line carrying two distinct facts; a single point spanning a few lines is fine
- every line is precious — it reflects something the user asked for or approved (`Content.Verbatim.Gated`), never filler
- lines order along the `Block.Line.Gradient`; block coherence is tight in the fundamentals and relaxes in the appendix

### Index.Edit.Action
- `Index.Edit.Action` is the small set of moves that edit the index — each a named action chosen by the case that calls for it
- the moves: `Index.Edit.Create.Block`, `Index.Edit.Append.Line`, `Index.Edit.Modify.Line`, `Index.Edit.Revise.Block`
- two tempos: hot capture (append during the `Alignment.Loop`) and cold consolidation (a maintenance pass over accumulated lines, where `Index.Edit.Create.Block` and `Index.Edit.Revise.Block` mostly live)
- the bias is the lowest-cost action that captures the aligned content (`Writing.Friction.Reduction`)
- every action is user-gated and `Content.Verbatim.Gated` — it is the index

### Index.Edit.Create.Block
- `Index.Edit.Create.Block` is the `Index.Edit.Action` of adding a new named concept block to the index
- the case: a genuinely new concept appears — coined by the user, or revealed when accreted lines show a pattern during consolidation
- the naming hint: when lines need to be referenced — cited from elsewhere, or pointed at as a group — they need a name; referenceability is what earns a block
- it is the higher-cost action — a new frame, a router entry, a placement decision; prefer `Index.Edit.Append.Line` unless the concept is genuinely new
- it mostly lives in the cold tempo, extracted from accumulated lines, not coined hot

### Index.Edit.Append.Line
- `Index.Edit.Append.Line` is the `Index.Edit.Action` of adding a `Kernel.Line` to the nearest coherent block — the default index edit
- it is the lowest-cost capture path, which is why it is the first beat: drop the line, do not stop to architect a block
- landing selection picks the nearest coherent frame — a concept block, its appendix, or a namespace for subsystem-level lines
- it is a load-then-word operation: select the block, bring it into context, then word the line against what it already says
- the block defines the wording — terse, framed, non-redundant — never generated blind and attached

### Index.Edit.Modify.Line
- `Index.Edit.Modify.Line` is the `Index.Edit.Action` of refining or correcting an existing `Kernel.Line`, keeping its block
- the case: a statement already in the block is wrong, imprecise, or superseded by aligned discussion
- like `Index.Edit.Append.Line` it is load-then-word — the block and the existing line both frame the new wording
- it is `Content.Verbatim.Gated` — the replacement wording is approved before commit
- prefer it over stacking a contradicting append: a corrected line beats two lines that disagree

### Index.Edit.Revise.Block
- `Index.Edit.Revise.Block` is the `Index.Edit.Action` of restructuring a block whose frame no longer holds its accreted lines
- the case: lines have piled up past the block's coherence — it needs reorder, split, or promotion of lines into the appendix
- it is a consolidation move, cold tempo — done with the warm context gathered while chatting, not hot
- it may spawn `Index.Edit.Create.Block` when a promoted cluster of lines earns its own name
- it preserves the lines — restructuring moves and reframes them, it never discards aligned content

### Partial.Cite
- `Partial.Cite` is using a shortened form of a `Dotted.Name` when it still resolves unambiguously
- legal when the short form has no collision in the engaged indexes, or the full name was already cited in the same document
- it is pure ergonomics — `Append.Line` for `Index.Edit.Append.Line` once the family is established
- the canonical name is always the full path; the router and block headings carry it — shortening is reader-facing convenience only
- it is the authoring side of `Fuzzy.Dotted.Name`: resolution tolerates approximation, `Partial.Cite` deliberately relies on it

#### meta
- aliases: `Partial.Name`

### Design.Space
- `Design.Space` is the total decision space of an artifact — every choice its design comprises, centered on the user's input (renames `Conceptual.Space`)
- it partitions two orthogonal ways: by provenance (`Touched.Space` / `Untouched.Space`) and by constraint (`Open.Space` / fixed)
- it is a vector space of `Design.Variable`s — each variable one axis; `Design.Target.Model` is a point in this space
- the touched/open ratio is the control surface: the user tightens control by constraining more of the space, and delegates automation by leaving space open
- it is the object every surface nests over: the `Chat.Surface` records it, the index digests it, the codebase realizes it
- it is never required complete to proceed — the agent works `Open.Space` to keep moving, alignment catches up

#### meta
- aliases: `Conceptual.Space`, `Alignment.Space`

### User.Touched
- `User.Touched` is a property of a fact: it was produced by a user-gated hugentic process — carrying evidence of user-agent collaboration, not agent invention
- the agent may construct and tag the fact; the user gates it — the gating is the touch, authorship is irrelevant
- it is general over the form of touch: stated, discussed, approved, co-drafted — any user-gated production qualifies
- it is a cross-surface predicate — the index is *a* `User.Touched` surface, the `Chat.Surface` is another
- it separates `Touched.Space` from `Untouched.Space` — untouched is always `Open.Space` and off-index (the `Agendix` is its index-adjacent home); touched can be open (`FR`) or constrained (a constraint)

### Touched.Space
- `Touched.Space` is the region of the `Design.Space` carrying `User.Touched` evidence — what the hugentic process has reached
- the index is its primary alignment surface, but not the only one — the `Chat.Surface` is another hugentic surface that holds touch
- a touched decision may be constrained (`CT`/`DC`/`RJ`) or open (declared free, `FR`) — touch means *engaged*, not *decided*

### Untouched.Space
- `Untouched.Space` is the region of the `Design.Space` with no `User.Touched` evidence — the hugentic process has not reached it
- it is always `Open.Space`: with no touch there is no directive constraint, so the agent decides for itself
- it never becomes an index line — untouched material remains in the chat, the work, or the `Agendix`, never the index proper
- the chats are mixed, touched and untouched; the index earns its keep by extracting the touched part worth keeping — not user filler — which is exactly `Line.Type`'s gate
- alignment is the shrinking of `Untouched.Space`: growing touch across the `Design.Space`

### Open.Space
- `Open.Space` is the uncollapsed region of the `Design.Space` — decisions not fixed by a user directive or its consequences, the agent's domain
- it is orthogonal to touch: it spans `Untouched.Space` (always open) and touched-open (`FR`, an explicit free declaration)
- consequences logically entailed by touched constraints are NOT open — the agent may fail to derive them, but is not free to decide against them
- in it the agent makes its own decisions to act — coherent, never random — but provisional and overwritable with good reason, off-index; they become directive constraints only once touched

### Line.Type
- `Line.Type` is the classification a `Kernel.Line` carries, written as a 2-letter prefix from a small controlled vocabulary
- classifying is the line-level gate — it forces significance the way naming gates a block; the small cost is the point, a cost-zero index overwhelms the user
- naming once bundled three filters — identification, boundary, significance; the line-level tests unbundle them: a crisp single point (`Kernel.Line`), attaching to a block (`Append.Line`), and significance (`Line.Type`)
- each type is a verb on the `Design.Space`, sorted by how the line acts on it:
  - collapsing: `CT` constraint (rules out), `DC` decision (selects a point), `RJ` rejected (closes an alternative)
  - describing: `DF` definition (what a concept is), `PR` principle (a valuation or rule of thumb)
  - declaring-open: `FR` free (an explicit, touched statement that a dimension is intentionally unconstrained)
- every typed line is `User.Touched`; `FR` is delegated-open (touched), not an agent guess — agent-fill has no type because it is not in the index
- typed lines are lintable and high-signal; untagged lines are allowed and typed as the index is polished

### Line.Type/Appendix
- example lines in the light 2-letter form:
  - `CT: a `Dotted.Name` must have more than one part`
  - `DF: `Index.Main` is the routed main body of the Index`
  - `RJ: `Index.HEAD` — collides with the `*HEAD*` grounding marker`
  - `FR: blocks may be placed in any order within a chapter`
- the vocabulary is soft and curated (`Concept.Hardness`) — extensible, not a hard enum; add a type when a recurring line-act has no home
- type analytics: which types earn their keep, which are smells — a `NOTE`/`SUMMARY` type would flag chat-recounting sneaking in
- lint targets: contradictory `CT`s, `DC`s that disagree, an `RJ` later reintroduced, an `FR` a later `CT` silently overrides

## Session.Notes

- DECISION (migration review): the `Agendix` — agent-driven untouched member of the index, `agendix/Concept.X-agendix.md` next to `appendix/`; hard provenance rule; user-triggered/not-gated capture; no stable-surface links in; concept-gap detector; will likely redefine the grounding surface (`Chat.Grounding.Request` queue reconcile pending). `Writing.Friction.Reduction` reworded around the friction gradient (friction buys authority; index keeps a friction floor).

- DECISION (migration review): `Soft.Programming.Language` renamed to `Index.Skillware` — no alias; the generic name collided with the program family (`Soft.Program`, `Agentic.Program`, `Program.Hardness`); the `Soft.Program` disambiguation line dropped as no longer needed; all 8 live citations swapped; mapping refreshed (`000-INDEX.md` router, chapter file, `Kernel.Block` structure; dead names `Index.Note`, `Index.Block.Syntax` removed)

- migration deletions (remove from real `agentos-pkg/index/` on migrate): `Index.Architecture` (merged into `Agentos.Index.System`); `Flat.Index.Architecture` (folded into `…/Index.Surface.Layout` appendix); `Extended.Index.Scope` (folded into `Appendix.Discovery`); `Distributed.Index` (replaced by `Index.Depot` + `Index.Discovery`)
- new concepts: `Index.Discovery`, `Project.Manifest` (project peer of `Package.Manifest`, in `AGENTS.md`); depot collisions are surfaced, not prevented
- resolved: namespace-prefixing → the `Index.Edit.*` family uses a shared `Index.Edit.` name prefix for legibility; `Partial.Cite`/`Partial.Name` fixes the verbosity cost (short form when unambiguous or already cited)
- REDESIGN DECISION: the index atom is the `Kernel.Line`, not only the block — the assistant was block-creation-centric; the balanced model is `Index.Edit.Action` (create/append/modify/revise) with `Append.Line` as the default hot beat and consolidation as the cold tempo
- `Index.Editor.Maintenance.Pass` (real `100`) reframes on migrate: from janitorial to the cold-consolidation tempo — resolve contradictions, move lines (`Block.Line.Gradient` cut), extract patterns into `Index.Edit.Create.Block`, check codebase↔index, run with warm chat context
- both blocks and lines stay primitives: a block is a coherent frame (tight fundamentals, coherence decaying into the appendix), which is what makes it a good append point; a line is a statement-in-context-of-its-block, so append is load-then-word
- RENAME (write→edit, operation/role only; craft stays "writing"): the index operation and the agent role are "edit"/"editor"; `Kernel.Writing` and `Writing.Friction.Reduction` keep "writing" (the craft of producing a line's text). concrete renames to apply on migration to real files: `Index.Writer.Maintenance.Pass`→`Index.Editor.Maintenance.Pass`; `Write.Trigger.Gated`→`Edit.Trigger.Gated`; `agentos-index --write` module→`--edit` (file `write.md`→`edit.md`); "index writer" role→"index editor"; prose "index write"→"index edit". `Content.Verbatim.Gated`, `Independent.Reader.Block`, `Kernel.Writing`, `Writing.Friction.Reduction` unchanged
- resolved: `Explicit.Namespace` revisited → groups blocks (peers + owned children); `namespace-members` is the inventory and the discoverability surface for path-children the router can't reach; appendix required; old "mechanics are `Concept.Scoping`, difference is intent" framing dropped for grouped-peer vs owned-child
- resolved: appendix-routing relationship → general appendix stays unrouted (`Appendix.Discovery`); the namespace member list is the one surface that names appendix-depth blocks at the top
- resolved: `./Child` relative-reference sugar added to `Block.Path/Appendix` — legal only where a root is established (member list, appendix-file headings)
- resolved: `Appendix.Pages` is the file axis (`Concept.X[N]`), orthogonal to `Block.Path` (ontology axis); they overlap by default but are independent — not a notation conflict, two axes
- `Concept.Scoping` revisited → narrowed to "semantics of a concept-valued `Block.Path` segment" and moved into `Block.Path`'s appendix
- migration: at migrate, replace standalone `Concept.Scoping` (103) with `Block.Path` + its appendix; refresh stale examples (`Index.Architecture/Flat.File.Design` → `Agentos.Index.System/Index.Surface.Layout`); replace the old `Explicit.Namespace` (103) with the rewrite (no longer cites `Concept.Scoping`)
- naming locked: Index = system; chapters = folders; `000-INDEX.md` = table; `Index.Block` stays valid (a block in any chapter)
- DECISION (router filename): the lookup table is `000-INDEX.md` (not `ROUTER.md`) — user prefers `INDEX`; `000-` keeps a unique grep marker for `Index.Discovery`; one router name for every depot (no separate public/local router file). the NNN file-numbering system is KEPT as-is (revisit later, not part of this migration)
- REDESIGN DECISION: appendix/grounding/scoped blocks are path-named outblocks (`Concept.X/Appendix`, `Concept.X/Grounding`, `Concept.X/Concept.Y`), appendix-placed by default; fundamentals and meta stay inblock (meta loads with the concept for findability)
- consequence: `Kernel.Block.Section` reframed — outblock form = a `Block.Path`; the section family (`Kernel.Block.Section`, `…Appendix`, `…Meta`, `…Grounding`, `…Fundamentals`) is now a redesign target
- migration rule: `540` uses full `Block.Path`s in one flat file; when a block migrates into a `Concept.X-appendix.md`, shorten its heading to the relative path (implicit root)

- chat-integration reframe: the index is a cache over the `Chat.Surface`, not a gate — captured as `Chat.Surface` block + `Chat.Surface/Appendix` (defines `Projects.Chats`, `Chat.Retrieval`); grounded on real Chatlas primitives (`query`/`recents`/`views` + `chatlas-grounding-agent` git-grounding); augments the existing `Chat.Surface` block in real `100` (reconcile at migrate); `Projects.Chats`/`Chat.Retrieval` promotable to scoped blocks if cited
- open (chat integration): date-range upper bound for `chatlas query`; whether `Chat.Retrieval` firing stays user-triggered or becomes a light alignment-loop reflex
- RENAME (migration): `Conceptual.Space` → `Design.Space` (user prefers the name); keep `Conceptual.Space`, `Alignment.Space` as aliases; `Design.Target.Model` stays "a point in the `Design.Space`"
- FOUNDATIONAL cluster (not index-architecture — tag for an alignment/foundational surface at migration): `Design.Space` (two-axis partition + the touched/open control-surface line — the framework thesis: user governs by constraining vs delegating), `User.Touched` (predicate: user-gated hugentic provenance, not authorship; a cross-surface property — index is *a* touched surface, chats another), `Touched.Space`/`Untouched.Space`/`Open.Space` (provenance × constraint axes; untouched⟹open; entailed consequences are not open; agent self-decisions are provisional/overwritable/off-index)
- `Line.Type`: 2-letter typed-line vocabulary (`CT`/`DC`/`RJ`/`DF`/`PR`/`FR`) = the line-level significance gate that replaces the block naming-filter; each type is a verb on the `Design.Space`; index holds only `Touched.Space` (no agent-fill/`OPEN` type); touch-necessary-but-not-sufficient (index = touched ∩ significant, not user filler); lintable + type-analytics; soft/curated vocabulary
- reframe: the index is a rolling digestion of `Touched.Space` — bypassable (just work), but always hugentic, never fully agentic
- RECONCILE (do over the already-migrated index, partially — not now): the alignment framework overlaps existing `Alignment.*.Axis` — `Open.Space` delegated ↔ `Alignment.Agentic.Axis`; touch grows on `Alignment.Hugentic.Axis`. link/merge the two vocabularies at migration; keep this as the standing reconcile note
- MIGRATION PLAN (detail later): operating contract = structure-free / content-gated — rename/move/split folders freely; any block wording or new line stays `Content.Verbatim.Gated`. `540` migrates to THREE homes, not one: index-architecture → `agentos-pkg` index (chapters/`ROUTER`/appendix); chat cluster (`Chat.Surface`/`Projects.Chats`/`Chat.Retrieval`) → home TBD (chatlas vs agentos-pkg); foundational cluster (`Design.Space`, `User.Touched`, `Touched.Space`/`Untouched.Space`/`Open.Space`, `Line.Type`) → a foundational/alignment surface, not the index cluster. approach: incremental till compliant, chatlas as pilot. open decisions: `INDEX.md` vs `000-INDEX.md`; cluster homes; plan artifact (Impl.Req vs live note)
- TOOLING DEBT (found during arch migration): `agentos index linter` encodes the OLD index model — it only accepts a router named `000-index.md`/`001-index.md` *inside* the index dir and hardcodes `NNN-index.md` filenames; it rejects the new layout (`000-INDEX.md`, chapter folders, `NNN-<chapter>.md`). the linter (and any other index tooling) must be updated to the new model — a separate later effort. during the arch migration the linter is NOT used for validation (agent-convention only). there is no runtime driver — index loading is agent-convention (the linter is the only structural-aware tool)
- parked candidate: `Digestion.Gradient` — promote the "index block → appendix line (`Append.Line`) → chat-in-place (`Chat.Retrieval`)" spine to a named concept if it earns cites; revisit later

## Session.Log

- arch-migration handoff: wrote `561-index-arch-migration-impl-req.md` (structural only — chapters/`000-INDEX.md`/appendix layout, chatlas pilot → agentos-pkg; numbering kept; content upgrade is a separate later Impl.Req); router locked to `000-INDEX.md` and applied across `540`

- session opened; backend = artifact; scope = all Index-architecture concepts
- appendix-philosophy thread written: `Writing.Friction.Reduction`, `Concept.Explosion`, `Block.Line.Gradient`, `Appendix.Default.Block`
- path-model written: `Block.Path` (+`/Appendix`, +`/Concept.Scoping`); `Concept.Scoping` demoted into `Block.Path` appendix
- `Kernel.Block.Section` reframed (sections = path-children outblock; fundamentals+meta inblock); members written: `…Fundamentals`, `…Meta`, `…Appendix`, `…Grounding` (trimmed of form-mechanics, now owned by `Block.Path`)
- implicit-root convention added to `Block.Path/Appendix` (appendix file roots its blocks)
- structural cluster: `Index.Router` (→000-INDEX.md, scope removed as misplaced), `Appendix.Pages` (file axis, orthogonal to `Block.Path`), `Appendix.Discovery` (reach-by-naming); `Extended.Index.Scope` deleted/folded
- model spine settled: ontology (`Block.Path`) × storage (`Appendix.Pages`), two orthogonal axes
- `Index.Chapter` converged + written (keystone: chapters = selective-loading folders, default `design`)
- `Index.Architecture` trimmed to a pure `Explicit.Namespace` anchor (one line, no meta) — membership/structure live in the member blocks
- `Agentos.Index.System` trimmed: fundamentals = whole-system identity + semantic computation; SPL/micro-prompts/context-manipulation/namespace-grouping moved to its appendix
- `Index.Surface.Layout` rewritten for chapters/`000-INDEX.md` and captured as `Agentos.Index.System/Index.Surface.Layout` (scoped appendix block); local paths under `notes/`
- depot cluster written: `Index.Depot`, `Index.Discovery`, `Project.Manifest`; `Distributed.Index` retired
- `Explicit.Namespace` rewritten (grouped-peer vs owned-child, member list as discoverability surface, appendix required); `./Child` sugar folded into `Block.Path/Appendix`
- chat integration written as `Chat.Surface` block + appendix (index-as-cache-over-chats; `Projects.Chats`, `Chat.Retrieval` 3 tiers on real Chatlas primitives) — captured practicing the line-centric philosophy
- grounded the alignment framework on the real index (`/agentos-index --ground`): found `Design.Space` = `Conceptual.Space` (renamed), delegated-open ≈ `Alignment.Agentic.Axis`; new = touch-coverage, untouched-vs-delegated, provisional agent-fill
- alignment-framework cluster written: `Design.Space` (control-surface thesis), `User.Touched`, `Touched.Space`/`Untouched.Space`/`Open.Space` (two orthogonal axes), `Line.Type`(+appendix) — the 2-letter typed-line vocabulary that gates line capture (replaces the block naming-filter); index = rolling digestion of `Touched.Space`, always hugentic
- part-naming COMPLETE: `Index.Surface` (whole, `Surface.Concept` = bytes vs `Agentos.Index.System` = semantics), `Index.Main`(+alias `Index.Fundamentals`), `Index.Appendix` (root of the appendix layer), `Index.Router` (lookup) — the two layers mirror `Kernel.Block.Fundamentals`/`Kernel.Block.Appendix`; the index indexes all `Surface.Types`, `Chat.Surface` foremost (not only chat)
- line-centric reframe written: `Kernel.Line` (atom), `Index.Edit.Action` + the `Index.Edit.*` family (`Create.Block`/`Append.Line`/`Modify.Line`/`Revise.Block`), `Partial.Cite`(+`Partial.Name`); enrichments: `Block.Line.Gradient` coherence line, nested-index line in `Agentos.Index.System/Appendix`; `Index.Editor.Maintenance.Pass` cold-tempo reframe logged for migration
