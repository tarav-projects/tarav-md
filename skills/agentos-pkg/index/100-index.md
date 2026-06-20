> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Stable.Surface

- `Stable.Surface` is a durable, authoritative surface where a specific facet of project knowledge lives
- the "stable" contract: the content aims to be maintained, current, and trustworthy
- all `Stable.Surfaces` must stay aligned — no surface is positioned as more important than another by default
- misalignments between surfaces are resolved context-dependently, not by a fixed hierarchy
- drift between stable surfaces is the target of `Internal.Alignment` — a problem to detect and resolve

****

## Stable.Md.Surface

- `Stable.Md.Surface` is the markdown subset of `Stable.Surfaces`
- the set of `.md` stable surfaces in a project: index notes, docs, skills, AGENTS.md, and similar

****

## Natural.Placement

- `Natural.Placement` is the principle that each surface holds the facet of a concept that is natural to its function
- primarily governs where origin material naturally belongs
- the full description of a concept is distributed across surfaces — each complements the others
    - index → conceptual grounding (what it is, why, how it connects) and discovery (where to find it)
    - appendix → extended depth, rationale, scoped views through `Concept.Scoping`
    - skills → operational behavior, workflows
    - code → the implementation itself (the code IS the description)
    - chat → user/agent interaction record, the evidence trail for alignment moves
- describing in markdown what code already holds naturally is redundant placement, not useful duplication — the question is placement
- cited duplicates can also be naturally placed when local use strongly benefits from repeated content
- duplication is justified when avoiding it would harm bootstrapping, workflow performance, local readability, or agent orientation
- content that feels unnatural in a surface is probably misplaced
- uncited or stale duplication is the anti-pattern, not duplication itself
- when multiple implementations exist, one may serve as a `Canonical.Reference.Implementation` — the go-to surface for implementation details, chosen by natural fit rather than hierarchy
- drift between any surfaces is always an error to resolve, not a hierarchy to adjudicate

****

## Natural.Placement:Skills

- `Natural.Placement:Skills` applies `Natural.Placement` to agent skill bodies
- skills are natural code-like operational surfaces for procedures, gates, role framing, tool use, and execution-shaped guidance
- a skill can carry the local context it needs when that improves agent performance, bootstrapping, workflow execution, or readability
- durable concept material still belongs in package index blocks, appendix pages, or references when those surfaces are the natural place for that facet
- repeated concept context in a skill should use `Cited.Duplication` so agents can find, check, and align the related surfaces
- cited skill-local context is not suspicious by itself; uncited drift, stale copies, and unclear placement are the maintenance problems
- a skill should not become a progress log, design transcript, or durable concept dump when those facets belong in live notes, index blocks, appendix pages, or references

****

## Placement.Balance

- `Placement.Balance` is the maintained alignment state between origin surfaces and their useful local expressions across surfaces
- balanced placement is not absence of repetition
- the system is balanced when origin material lives in its natural source surfaces and cited duplicates exist only where locally useful
- duplicates remain balanced when they cite origins and can be found, checked, and updated during maintenance
- diagnostic signal: uncited repeated concept material, stale cited duplicates, or ambiguity about where the origin material lives
- complementary to `Natural.Placement` — natural placement decides where material belongs; placement balance checks whether distributed material stays aligned

****

## Reference.Implementation

- `Reference.Implementation` is the codebase surface that owns the executable definition of a protocol, schema, or behavioral contract
- the index describes semantics and intent; the Reference.Implementation owns the concrete shape
- drift between the index and the Reference.Implementation is a misalignment error — not resolved by hierarchy
- a project may designate one implementation surface as the Reference.Implementation when multiple exist (e.g., canvas-js over canvas-py)
- follows `Natural.Placement` — implementation detail belongs in code, not duplicated in markdown

### meta

- related: `Natural.Placement`, `Stable.Surface`, `Package.Skill`

****

## Cited.Duplication

- `Cited.Duplication` is intentional duplication of concept material into another surface with an explicit `Concept.Cite` to the origin
- used when local access to repeated context improves agent performance, bootstrapping, workflow execution, package orientation, or readability
- the duplicate may be rewritten, summarized, or adapted to local task shape, but must remain aligned with the cited origin
- the cited origin anchors maintenance and gives agents or tooling a way to check drift
- if a cited duplicate clearly mirrors an edited origin, the writer may update the duplicate in the same approved write pass
- unresolved drift or ambiguous disagreement is surfaced as an issue, not silently resolved
- uncited durable concept material in a repeated surface should either be indexed, cited, or treated as unmanaged duplication

****

## Agentos.Live.Note

- `Agentos.Live.Note` is a non-`Stable.Surface` markdown working surface under `notes/live/`
- agents use live notes to store and maintain active working data that is useful beyond the immediate chat but not yet promoted as durable design truth
- live notes can back workflow artifacts such as design sessions, implementation requests, summaries, and issue reports when the workflow defines extra semantics
- the live-note surface itself defines storage and maintenance posture, not artifact meaning
- ordinary live-note allocation follows `File.Numbering.Protocol`; operational commands live in `references/file-numbering-protocol.md`
- durable signal discovered in live notes should be promoted to the natural stable surface instead of leaving the live note as the long-term source

****

## Parking.Note

- `Parking.Note` is a reserved file under `notes/live/` for parking small blocks for later
- three files form the `Parking.Note` family: `010.TODOS.md` (something to do), `011.ISSUES.md` (something wrong), `012.NOTEBOOK.md` (everything else)
- `012.NOTEBOOK.md` is the catch-all — nothing is out of place in NOTEBOOK
- entries follow `Kernel.Writing` style with relaxed constraints — direct, orthogonal lines, no space budget
- each entry is a `Kernel.Block`-style heading using `Dotted.Notation` plus prose (e.g. `## Idea.About.Fishing`)
- the capture workflow is short-lived: discuss → draft → approve → write
- operational skill: `agentos-parking-note`

****

## Agentos.Live.Script

- `Agentos.Live.Script` is a non-`Stable.Surface` code working surface under `dev/live/`
- agents use live scripts for small code snippets, runnable drafts, probes, and alignment surfaces that a user can inspect, run, and critique
- live scripts are useful when code is the clearest medium for shared alignment, but the code is not yet part of the maintained implementation
- live-script naming and allocation follow `File.Numbering.Protocol`; operational commands live in `references/file-numbering-protocol.md`
- a live script may mature into implementation code, documentation, a reference, or be archived when it no longer carries useful working signal

****

## Surface.Link.Directionality

- `Surface.Link.Directionality` defines which surfaces can reference which
- `Local.Surface` can reference `Public.Surface` — not the reverse
- `Public.Surface` must be self-contained — it cannot depend on local project knowledge
- `Local.Surface` has access to everything — it bridges public and local naturally
- this constraint exists because public surfaces are distributable — they must work outside the project
- when the full dependency project is available (`Project.Dev.Install`), the local/public boundary shifts — local surfaces of the dependency become reachable too
- `Public.Surface`s may carry `Chat.Ref`s, but those refs are not publicly resolvable — a consumer outside the originating project context cannot follow them. This is a pragmatic exception to `Public must be self-contained`

****

## Chat.Surface

- `Chat.Surface` is the surface of user/agent direct communication — the recorded conversation itself
- it is a `Stable.Surface`, but append-only
- emit-driven, not curated: it comes into existence as a byproduct of interaction; other surfaces are actively shaped by humans and agents
- append-only: a chat session is a tape; once written, turns are not edited but superseded by later turns
- `Natural.Placement` claim: SSOT of user/agent alignment evidence — what was said, accepted, surfaced, overwritten, and when
- primary signal lives in user turns; assistant turns supply context and forensic trace ("why did the agent do that")
- holds reasoning, decisions, rejections, and reactions in their original form — the most detailed description of how the project arrived at its curated state
- referenceable from any other surface via `Chat.Ref`, the same way the index is referenceable
- participates in alignment as a precedent bank — earlier exchanges inform later reasoning; the system evolves by accumulating cited precedent
- agents access chat content through `agentos-chatlas-pkg`

****

## Chat.Ref

- `Chat.Ref` is a citation to a position on a chat tape — the reference primitive for the `Chat.Surface`
- address shape: `@<hash>-<timetag>` where `<hash>` is an `identity_hash` prefix and `<timetag>` is an ISO 8601 datetime, truncatable to any precision
- `@<hash>` alone (no timetag) is a session-level reference
- a timetag defines a window at its declared precision — narrow at second-level, broader at day or month
- explicit ranges join two timetags with `..`: `@<hash>-<timetag1>..<timetag2>`
- the readable hook is host-surface annotation alongside the ref (e.g., a trailing em-dash and prose), not part of the address itself
- resolved through `agentos chatlas` query and export surfaces

****

## Chat.Grounding

- `Chat.Grounding` is context injection and citation from `Chat.Surface` into index/appendix kernel blocks
- it grounds a `Kernel.Block:Index` or `Kernel.Block:Appendix` in prior user/agent chat interaction
- grounding only happens on index/appendix blocks; downstream surfaces cite grounded blocks instead of carrying first-class chat grounding
- grounding follows `Active.Grounding`: accepted heads remain active while they support the current block
- absence of `### grounding` is the implicit sign that a block is not grounded
- grounding has no state taxonomy; material grounding problems are marked with `Grounding.DRIFT`
- grounding drift is surfaced through alignment because the resolution happens on `Chat.Surface` and can become new grounding

****

## Chat.Grounding.Ref.Resolution

- `Chat.Grounding.Ref.Resolution` is the reading rule for resolving a `Chat.Ref` used as grounding
- a grounding ref is a landing point into `Chat.Surface`, not a claim that all evidence is contained in one exact turn
- the reader should inspect the landing turn and nearby turns needed to understand the alignment move
- a point ref is valid when it lands inside the relevant evidence neighborhood
- a range ref is preferred when grounding depends on proposal, correction, discussion, or convergence across turns
- the evidence note tells the reader what to look for around the ref
- the goal is recoverable grounding, not maximal timestamp precision

****

## Chat.Grounding.Candidate.Review

- `Chat.Grounding.Candidate.Review` decides whether a proposed chat ref should enter block grounding
- the reviewer asks whether the evidence directly supports the current factual shape of the target block
- the reviewer checks nearby context for contradiction, drift, or unresolved ambiguity
- `*HEAD*` means the evidence still supports the current block as `Active.Grounding`
- history means the evidence is retained for provenance but no longer supports the current block as written
- a later refinement does not demote earlier evidence when the earlier evidence remains compatible with the current block
- the final index write happens only after user approval of the grounding role and resolution shape

****

## Chat.Grounding.Head.Audit

- `Chat.Grounding.Head.Audit` reviews existing `*HEAD*` grounding rows against the current target block
- each `*HEAD*` is evaluated against the block version it originally supported and the current block version
- git history provides the block diff between grounding insertion and the current block
- a fundamental block change is a trigger to re-evaluate existing `*HEAD*` rows
- unchanged or editorial block diffs usually do not require full head review
- invalidated heads move to `Grounding.History`; they are not deleted
- new heads can trigger a lightweight audit of older heads when they appear to supersede prior evidence
- the purpose is to keep `Active.Grounding` aligned with the current factual shape of the block

****

## Index.Grounding

- `Index.Grounding` is context discovery and citation from existing index/appendix blocks into a target topic
- it grounds a topic in prior `Kernel.Block:Index` or `Kernel.Block:Appendix` material instead of chat turns
- it is source-specific retrieval; accepted results still land through the generic `Kernel.Block:Grounding` review semantics
- it is useful when an agent should search the index for related blocks before discussing, writing, or grounding a topic
- it does not replace `Chat.Grounding`; the two source families can produce different evidence for the same target block

****

## Chat.Surface.Closure

- `Chat.Surface.Closure` is the principle that the system is closed over `Chat.Surface`
- chat is the near-universal ingress: users and heterogeneous agents both work through it
- in the limit, all meaningful information is contained in, or groundable to, the chat log
- the append-only `Chat.Surface` is an event log; other surfaces are materialized projections of it
- projection is not authority transfer: each projection stays SSOT of its own curated form
- `Chat.Surface` stays SSOT of the generative record, so projections remain re-derivable and drift-checkable
- boundary: chat is the dominant ingress, not total
- an out-of-band edit lands with no chat event; that gap is `Grounding.DRIFT`
- closure is self-healing: discussing ungrounded material is itself the grounding act
- the discussion emits the missing event and can become `Active.Grounding`
- grounding is therefore never blocked, only pending; the discussion must re-establish the content, not just mention it
- closure (groundable in principle) holds at every moment; completeness (grounded now) is only the limit
- in the limit the chat log is a sufficient generative basis: every projection is reconstructable from it

****

## Agentos.Index.Notes

- `Agentos.Index.Notes` is one of the `Stable.Surfaces` of an Agentos-style project — the index flat files
- implements the `Agentos.Index` — a `Soft.Programming.Language` for project knowledge
- four roles: conceptual implementation of the system, discovery and navigation index, development surface, main alignment surface
- contains `Named.Concepts` written in `Kernel.Block:Index` blocks, organized in flat index files
- agents operate the index through the `Index.Runtime`; what loads is governed by the `Package.Driver`, not by the index — the index has no loading policy of its own
- catalog and model are the same act: naming and defining the parts is the modeling; elements and their interactions are both concepts, so one primitive (`Kernel.Block`) carries the whole mental model

****

## Index.Concept.Coverage

- `Index.Concept.Coverage` is the goal that the index covers all `Named.Concepts` in the project
- any `Dotted.Name` that appears in a stable surface should have an index entry
- concepts can emerge anywhere — authors use `Dotted.Notation` naturally without worrying about index maintenance
- the system detects new `Named.Concepts` and triggers index updates separately

****

## Kernel.Block:Index

- `Kernel.Block:Index` is `Kernel.Block` placed in `index/` — the loadable unit of meaning in the index
- anchored by a heading (H2–H6) that names the concept using `Dotted.Notation`
- `Kernel.Writing` at tight space constraints — conceptual completeness under compression
- must carry enough signal for an agent to reason correctly about the concept
- the minimal unit of meaning — the starting point for the discovery cascade into the appendix
- the index must have at least a block for any meaningful concept in the system
    - blocks can link out to other surfaces rather than define everything inline
- inherits fundamentals + `### grounding` + `### appendix` + `### meta` from `Kernel.Block`
- `Content.Verbatim.Gated` — user approves exact wording before commit
- index blocks should NOT become transcripts, changelogs, progress dashboards, task lists, or implementation dumps

### meta

- aliases: `Index.Block`, `Global.Block`

****

## Kernel.Block:Appendix

- `Kernel.Block:Appendix` is `Kernel.Block` placed in `appendix/` — any material that hangs off a concept
- `Kernel.Writing` at relaxed space constraints — depth over compression
- content is not limited to conceptual depth — specs, regex, raw ideas, parked material all belong here
- the discipline is at the insertion point — find the right concept, then write freely under it
- can be cleaned and integrated later — low friction first, curation second
- no line-count ceiling, but line-length discipline still applies
- `Write.Trigger.Gated` only — user initiates, but exact wording is not gated
- discovery is implicit — agents check if `appendix/Concept.Name-appendix.md` exists

### meta

- aliases: `Appendix.Block`

****

## Kernel.Block:Design

- `Kernel.Block:Design` is `Kernel.Block` used in design artifacts — fundamentals, grounding, and appendix in a single block
- holds the full state of a concept in one place — used in conversations and design sessions
- at promotion time: fundamentals compress into `Kernel.Block:Index`, appendix material goes to `Kernel.Block:Appendix`
- the distinction: `Kernel.Block:Index` is compressed, `Kernel.Block:Appendix` is exhaustive, `Kernel.Block:Design` is both together
- preserve user's wording when it carries design judgment

### meta

- aliases: `Design.Block`, `Design.Session.Block`, `Design.Index.Block`

****

## Md.Surface

- `Md.Surface` is the markdown layer of a project — the set of `.md` files
- parameterized to scope: `Md.Surface:Agentos`, `Md.Surface:Agentos.Stack`

****

## Dotted.Notation

- `Dotted.Notation` identifies named concepts in an ontology surface
- a dotted name is a signal that the phrase refers to a concept, not casual prose
- every name has at least two parts; dot depth is flexible and natural to the concept
- dots provide context but are not a strict hierarchy — definition and relationships live in notes and registry entries, not the name
- `Explicit.Namespace` must be explicit; do not infer a namespace from a dotted prefix alone
- a dotted name can appear before it is registered
    - agents infer concept maturity from the repository: prose-only, registry entry, or dedicated note
- registry lookup is opportunistic, not mandatory — use it when concept identity matters, avoid turning ordinary work into ontology maintenance
- an approximate chat-side form exists — see `Fuzzy.Dotted.Name`

****

## Dotted.Parameterized.Notation

- `Dotted.Parameterized.Notation` identifies a target or instance of a named concept without creating a new concept
- form: `Concept.Name:Target`
- the part before the colon is the concept, the part after is the parameter
- colon parameters may themselves use dots
- parameterized references are instances of the same concept, not different concepts
    - use a new dotted name when the meaning changes
    - use a colon parameter when the same concept is applied to a different target
- examples: `Maintenance.System:Agentos`, `Md.Surface:Agentos.Stack`, `Project.CLI:Agentos`

****

## File.Numbering.Protocol

- `File.Numbering.Protocol` defines numeric filename conventions for stable, addressable files in project surfaces
- numeric prefixes are stable handles — the title may change, but the prefix should not be renumbered
- canonical prefixes use three digits; allocation is append-only; gaps are allowed; do not renumber or fill gaps if unnecessary
- design depth lives in `appendix/File.Numbering.Protocol-appendix.md`
- operational allocator usage lives in `references/file-numbering-protocol.md`

### Current Agentos range model

- `000-099`: reserved files with fixed system roles
- `000-index.md` — public `Index.Router`, lives in the package index surface
- `001-index.md` — local `Index.Router`, lives in `notes/index/`
- `010.TODOS.md` — TODO parking, lives in `notes/live/`
- `011.ISSUES.md` — issue parking, lives in `notes/live/`
- `012.NOTEBOOK.md` — idea/observation parking, lives in `notes/live/`
- `100-299`: public index flat files in the package index surface
- `300-499`: local index flat files (`notes/index/`)
- `500-999`: rolling other files (live notes, live scripts)

### CLI support

- `agentos stdlib prefix` provides deterministic allocation
- desired direction: project-wide duplicate detection, range validation, append-only enforcement

****

## Maintenance.System

- `Maintenance.System` defines how a project surface is diagnosed over time
- diagnosis-first, not fix-first — report issues with evidence, then the user decides
- parameterized: `Maintenance.System:Agentos` is the Agentos instance
- reports must be evidence-based — suggestions without evidence must be marked as such

****

## Index.Writer.Maintenance.Pass

- `Index.Writer.Maintenance.Pass` is the maintenance check performed when editing an existing authoritative concept block
- starts by finding all mentions and citations of the edited concept across stable markdown surfaces
- checks cited duplicates, workflow copies, package routers, auxiliary skills, and related references for needed updates
- may update clear cited duplicates in the same approved write pass when they mirror the edited origin
- surfaces unresolved drift, ambiguous disagreement, or unclear origin placement as issues
- prevents index edits from leaving known duplicated or cited material stale

****

## Agentos.Project

- `Agentos.Project` is a concrete project that adopts the `Agentos.Stack` model
- exists when the project root contains `.agentos/project.json` — the `Agentos.Project.Marker`
    - `.agentos/config.json`, `.agentos/AGENTS.md`, skill depots, `.agents/`, `.claude/` do not define project existence
- `.agentos/AGENTS.md` is the project-local natural-language instruction surface — human-writable, loadable by skills
- naming boundary: `Agentos.Project` means a project that adopts Agentos, not the Agentos implementation itself
    - `Agentos.Project:agentos-py` = agentos-py as an adopting project
    - `Agentos.Implementation:agentos-py` = agentos-py as part of the Agentos implementation
    - the same repo can be both under different reference frames

****

## Agentos.AgentInstructions

- `Agentos.AgentInstructions` is the project-local natural-language instruction surface at `.agentos/AGENTS.md`
- human-writable — contains project-specific guidance for Agentos workflows and skills
- skills may load it when they need custom local instructions or interpretation guidance
- does not define project identity — the marker remains `.agentos/project.json`
