# Index Architecture Redesign — Design Session

## Session.Abstract

- revisit/redesign all Agentos Index concepts to converge the generalized-index model
- this artifact is the temporary home for the updated blocks; migrate into `agentos-pkg/index/` later, safely, once converged
- convergence so far: the Index is a system of **chapters** + appendix + router
    - **chapters** = load-partition folders (default `design`, reserved `design`/`impl`, extensible, files `NNN-<chapter>.md`)
    - **`ROUTER.md`** = chapter-sectioned lookup table (was `INDEX.md`/`000-index.md`)
    - **appendix** = part of the Index but not a chapter — depth, discovered not routed
    - default search scopes to `design`; other chapters load only on an explicit miss
- proof-of-shape already applied additively to `agentos-chatlas-pkg` (`design/` + `ROUTER.md`)

## Design.Index

- concept blocks land here as each converges
- redesign order: `Index.Chapter` (keystone) → `Index.Architecture` → `Index.Surface.Layout` → `Flat.Index.Architecture` → `Index.Router` → `Index.Block` → depth-layer concepts → distributed/depot
- NEW target (split out of `Index.Router`): the search-scope concept — search has a `scope` variable defaulting to the `design` chapter, widened explicitly; lives in the search workflow, not the router
- `Tail.Capture` written — the standing duty to capture a discussion's tail (parallel alignment-loop task, user-gated, Natural.Placement-governed); closes the appendix-cluster's "user data loss" gap
- skill-side TODO: `agentos-hugentics-designer` should treat tail-capture as a parallel consolidation concern; `agentos-hugentics-capture-audit` is its operational form

### Index.Chapter
- `Index.Chapter` is a folder of the Index that groups concepts into a unit of selective loading
- concepts across chapters are peers, reached by one `Dotted.Name` lookup — a chapter sets only what loads together
- the Index has a default chapter that loads first; another chapter loads only when a named concept is absent from the default
- the default chapter is `design`; `impl` is reserved; a package may add any number beyond these
- a chapter's files are named `NNN-<chapter>.md`, e.g. `design/100-design.md` — the suffix names the chapter

#### appendix
- `ROUTER.md` routes every chapter; the appendix is the Index's depth layer, reached by naming (`Appendix.Discovery`), not routed as a chapter
- a concept may carry its chapter as an optional `Dotted.Name` prefix (`Impl.Concept.A`)

### Agentos.Index.System
- `Agentos.Index.System` is the Agentos Index taken as a whole — the operable system of named concepts agents reason with
- it enables semantic computation over those concepts: composing them, finding contradictions, detecting design weakness

#### meta
- aliases: `Agentos.Index`

### Agentos.Index.System/Appendix
- it is a `Soft.Programming.Language` for project knowledge — a library of micro-prompts invoked by naming
- mentioning a `Dotted.Name` triggers a concept-level context load
- it manipulates the agent's context window — by controlling what enters context, you control how the agent reasons
- it is an `Explicit.Namespace` grouping the concepts that compose the index system
- the Index is a nested indexing surface — each layer indexes the one beneath it: the surface indexes the project's content across its `Surface.Types` (the `Chat.Surface` foremost), the chapters index the surface, the `Index.Router` indexes the chapters; "the index" resolves by context, the `Index.*` names disambiguate the layers

### Agentos.Index.System/Index.Surface.Layout
- `Index.Surface.Layout` is the directory protocol a package follows to host an Index
- a hosted Index is a `ROUTER.md` lookup over one folder per `Index.Chapter`, plus a shared `appendix/`

public Index — in the package skill:
```
skills/<package>-pkg/
├── ROUTER.md          — concept→file lookup, sectioned by chapter
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
- `Writing.Friction.Reduction` is the principle that the Agentos system relentlessly lowers the cost of capturing design as it is discussed
- the aim is to capture as much of the user's design as possible before it is lost — structure is deferred, not skipped
- the appendix is the low-friction capture surface — dump-capture without the index's space budget, promote to fundamentals in later iterations
- capture stays user-gated — friction drops, the approval gate stays

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
- far enough down the sequence, a line is merely filed under the concept, barely about it
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

### Kernel.Block.Grounding
- `Kernel.Block.Grounding` is the grounding section of a `Kernel.Block`, addressed `Concept.X/Grounding`
- it is a mechanical `Hard.Evidence` linking system — it links the block to where its evidence lives
- it carries `Grounding.Entry` links and their evidence notes, never agent reinforcement or commentary
- a grounding source can be a `Chat.Ref`, a `File.Mention`, a web page, or another evidence surface
- grounding lives only on index/appendix blocks; downstream surfaces cite the grounded block instead of re-grounding
- `*HEAD*` marks the active current grounding for the block

### Index.Surface
- `Index.Surface` is the file surface of one Index — `Index.Router`, `Index.Main`, and `Index.Appendix` taken as a single addressable surface
- it is a `Surface.Concept`: the bytes on disk, distinct from `Agentos.Index.System`, which is what those bytes do (the operable `Soft.Programming.Language`)
- it follows the `Index.Surface.Layout` directory protocol; one `Index.Surface` per `Index.Depot`
- it is the outermost layer of the nested index — the index of the project across its surfaces (`Surface.Types`), foremost the `Chat.Surface` where design originates

### Index.Appendix
- `Index.Appendix` is the appendix layer of the Index and the root concept for it — the on-demand depth, complement of `Index.Main`
- it is the index-level echo of `Kernel.Block.Appendix`: depth deferred out of the compressed front, loaded by choice
- it is not routed — reached by naming through `Appendix.Discovery`, never loaded by default
- it lives in one `appendix/` shared across chapters; files are concept-named and addressed as `Appendix.Pages`
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

### Index.Router
- `Index.Router` is the lookup table of the Index — `ROUTER.md`, loaded first when the Index enters context (per the `Package.Driver`)
- it routes concept name → file, sectioned by `Index.Chapter`
- the appendix is not routed — appendix depth is reached by naming (`Appendix.Discovery`), not listed here
- it also carries file routing (`Project.File.Index`) — important project files for research
- entries may carry a one-sentence hint, but depth lives in the blocks themselves
- the routers of the engaged `Index.Depot`s compose into one working Index (`Index.Discovery`)

### Appendix.Pages
- `Appendix.Pages` is the file dimension of a concept — the pages its content spans, written `Concept.X[N]`
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
- its heading is a `Dotted.Name`, the root of the concept's `Block.Path`s and what `ROUTER.md` routes
- it is `Kernel.Writing` under tight compression — conceptual completeness in few lines, depth pushed to `Concept.X/Appendix`
- the Index must have a block for any meaningful concept; it may link out rather than define everything inline
- `Content.Verbatim.Gated` — user approves exact wording before commit
- it must not become a transcript, changelog, dashboard, task list, or implementation dump

#### meta
- aliases: `Global.Block`

### Appendix.Block
- `Appendix.Block` is a `Kernel.Block` placed in the appendix — a path-child of a concept (`Concept.X/Appendix`, `Concept.X/Concept.Y`)
- it is `Kernel.Writing` at relaxed constraints — depth over compression, no line-count ceiling
- content is not limited to conceptual depth — specs, raw ideas, parked material belong, filed under the nearest concept (`Concept.Explosion`)
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
- `Index.Depot` is a self-contained Index instance — its own `ROUTER.md`, chapters, and appendix
- it follows `Agentos.Index.System` conventions
- a depot belongs to a surface — a project or a `Package.Skill` — and is engaged like any other, no depot privileged
- the same concept name may exist in two engaged depots; the system surfaces the collision, it does not prevent or resolve it
- it loads with its owner through the `Package.Driver` (`Context.Loading.Path`)

### Index.Discovery
- `Index.Discovery` is how an agent finds the `Index.Depot`s available to engage
- a depot is marked by a `ROUTER.md` — its presence identifies an engageable index on a skill or project
- declared discovery walks the dependency graph: a project's `Project.Manifest` and each package's `Package.Manifest`
- fallback discovery: when nothing declares them, search for `ROUTER.md` across skills and projects — cheap
- discovery is hierarchical (the dependency graph) but engagement is flat — discovered depots are peers, routed equally
- a workflow scopes the discovered set by agent common sense — conversation context, skill descriptions, task relevance — defaulting to the whole engaged set

### Project.Manifest
- `Project.Manifest` is a project's declaration of the `Package.Skill`s and indexes it engages — the project peer of `Package.Manifest`
- it lives in the project's `AGENTS.md`
- with `Package.Manifest` it forms the dependency graph `Index.Discovery` walks
- it is optional — without it, `Index.Discovery` falls back to searching for `ROUTER.md`

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
- the index is the index *of* the `Chat.Surface` for the project — the nested-index relation, at the surface level
- not every cycle starts with design; work may run implement-first, with digestion deferred to cold consolidation (`Index.Edit.Action`)
- all `Chat.Surface` access is through Chatlas; the project's attributed chats are `Projects.Chats`, searched by `Chat.Retrieval`

### Chat.Surface/Appendix
- `Projects.Chats` is the chat set attributed to a project — its own sessions plus its ancestors': for `A/B/C`, the union of `A/B/C`, `A/B`, `A` (walk the path via `chatlas query --project`, one query per level — match is exact, no prefix)
- `Chat.Retrieval` is the user-triggered "where did we last discuss X", over `Projects.Chats`, cheapest-path-first:
  - tier 1 index — digested → a named block (cache hit)
  - tier 2 git-anchored — `git log` on touched files → date range → `chatlas query --active-after` → sessions (precise, cheap)
  - tier 3 direct — `chatlas query --user-contains` / `chatlas recents` over the turns (broad, complete)
  - read a hit via Chatlas views: `summary` as the cheap filter, `zip-transcript` as the trusted raw turns (`We.Distrust.Summaries`)
- two situations: chat-only work (worst case, but the data is there) vs work with file consequences (best — git bridges files→sessions)
- digestion gradient (extends the `Block.Line.Gradient` capture axis): index block → appendix line (`Append.Line`) → chat-in-place, retrieved on demand (the zero-digestion floor)
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

## Session.Notes

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
- naming locked: Index = system; chapters = folders; `ROUTER.md` = table; `Index.Block` stays valid (a block in any chapter)
- REDESIGN DECISION: appendix/grounding/scoped blocks are path-named outblocks (`Concept.X/Appendix`, `Concept.X/Grounding`, `Concept.X/Concept.Y`), appendix-placed by default; fundamentals and meta stay inblock (meta loads with the concept for findability)
- consequence: `Kernel.Block.Section` reframed — outblock form = a `Block.Path`; the section family (`Kernel.Block.Section`, `…Appendix`, `…Meta`, `…Grounding`, `…Fundamentals`) is now a redesign target
- migration rule: `540` uses full `Block.Path`s in one flat file; when a block migrates into a `Concept.X-appendix.md`, shorten its heading to the relative path (implicit root)

- chat-integration reframe: the index is a cache over the `Chat.Surface`, not a gate — captured as `Chat.Surface` block + `Chat.Surface/Appendix` (defines `Projects.Chats`, `Chat.Retrieval`); grounded on real Chatlas primitives (`query`/`recents`/`views` + `chatlas-grounding-agent` git-grounding); augments the existing `Chat.Surface` block in real `100` (reconcile at migrate); `Projects.Chats`/`Chat.Retrieval` promotable to scoped blocks if cited
- open (chat integration): date-range upper bound for `chatlas query`; whether `Chat.Retrieval` firing stays user-triggered or becomes a light alignment-loop reflex

## Session.Log

- session opened; backend = artifact; scope = all Index-architecture concepts
- appendix-philosophy thread written: `Writing.Friction.Reduction`, `Concept.Explosion`, `Block.Line.Gradient`, `Appendix.Default.Block`
- path-model written: `Block.Path` (+`/Appendix`, +`/Concept.Scoping`); `Concept.Scoping` demoted into `Block.Path` appendix
- `Kernel.Block.Section` reframed (sections = path-children outblock; fundamentals+meta inblock); members written: `…Fundamentals`, `…Meta`, `…Appendix`, `…Grounding` (trimmed of form-mechanics, now owned by `Block.Path`)
- implicit-root convention added to `Block.Path/Appendix` (appendix file roots its blocks)
- structural cluster: `Index.Router` (→ROUTER.md, scope removed as misplaced), `Appendix.Pages` (file axis, orthogonal to `Block.Path`), `Appendix.Discovery` (reach-by-naming); `Extended.Index.Scope` deleted/folded
- model spine settled: ontology (`Block.Path`) × storage (`Appendix.Pages`), two orthogonal axes
- `Index.Chapter` converged + written (keystone: chapters = selective-loading folders, default `design`)
- `Index.Architecture` trimmed to a pure `Explicit.Namespace` anchor (one line, no meta) — membership/structure live in the member blocks
- `Agentos.Index.System` trimmed: fundamentals = whole-system identity + semantic computation; SPL/micro-prompts/context-manipulation/namespace-grouping moved to its appendix
- `Index.Surface.Layout` rewritten for chapters/`ROUTER.md` and captured as `Agentos.Index.System/Index.Surface.Layout` (scoped appendix block); local paths under `notes/`
- depot cluster written: `Index.Depot`, `Index.Discovery`, `Project.Manifest`; `Distributed.Index` retired
- `Explicit.Namespace` rewritten (grouped-peer vs owned-child, member list as discoverability surface, appendix required); `./Child` sugar folded into `Block.Path/Appendix`
- chat integration written as `Chat.Surface` block + appendix (index-as-cache-over-chats; `Projects.Chats`, `Chat.Retrieval` 3 tiers on real Chatlas primitives) — captured practicing the line-centric philosophy
- part-naming COMPLETE: `Index.Surface` (whole, `Surface.Concept` = bytes vs `Agentos.Index.System` = semantics), `Index.Main`(+alias `Index.Fundamentals`), `Index.Appendix` (root of the appendix layer), `Index.Router` (lookup) — the two layers mirror `Kernel.Block.Fundamentals`/`Kernel.Block.Appendix`; the index indexes all `Surface.Types`, `Chat.Surface` foremost (not only chat)
- line-centric reframe written: `Kernel.Line` (atom), `Index.Edit.Action` + the `Index.Edit.*` family (`Create.Block`/`Append.Line`/`Modify.Line`/`Revise.Block`), `Partial.Cite`(+`Partial.Name`); enrichments: `Block.Line.Gradient` coherence line, nested-index line in `Agentos.Index.System/Appendix`; `Index.Editor.Maintenance.Pass` cold-tempo reframe logged for migration
