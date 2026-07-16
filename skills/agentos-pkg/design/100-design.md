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

## Natural.Placement::Skills

- `Natural.Placement::Skills` applies `Natural.Placement` to agent skill bodies
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
- `Public.Surface`s may carry chat `Anchory.Anchor`s, but those anchors are not publicly resolvable — a consumer outside the originating project context cannot follow them. This is a pragmatic exception to `Public must be self-contained`

****

## Chat.Surface

- `Chat.Surface` is the surface of user/agent direct communication — the recorded conversation itself
- it is a `Stable.Surface`, but append-only and emit-driven — a byproduct of interaction, not curation; a session is a tape, turns superseded, never edited
- it is the largest, most complete record of a project's design — user data lands here first, before any digestion
- `Natural.Placement` claim: SSOT of user/agent alignment evidence — what was said, accepted, surfaced, overwritten, and when
- primary signal lives in user turns; assistant turns supply context and forensic trace ("why did the agent do that")
- in alignment terms it holds the raw touch events: user turns are `User.Touched` surface, assistant turns are touched-adjacent — the context around the touch, not the touch itself
- the index is a curated cache over the `Chat.Surface`, not a gate: an undigested concept is retrieved from the chats, never a reason to stall (no design-paralysis)
- not every cycle starts with design; work may run implement-first, with digestion deferred to cold consolidation (`Index.Edit.Action`)
- referenceable from any surface via `Anchory.Anchor`; it participates in alignment as a precedent bank — earlier exchanges inform later reasoning
- all access is through Chatlas (`agentos-chatlas-pkg`); the project's attributed chats are `Projects.Chats`, searched by `Chat.Retrieval`

****

## Chat.Grounding

- `Chat.Grounding` is grounding whose evidence source is the `Chat.Surface` — a block or line linked back to the user/agent interaction that touched it
- it is the canonical source: the `Chat.Surface` holds the touch events, so index content should ultimately link there — built and maintained by `Index.Linking`
- other sources converge toward it: drift resolves on the `Chat.Surface`, and the resolution becomes a new link

****

## Grounding.Audit

- `Grounding.Audit` reviews a block's `Grounding.Head` lines against the block as currently written
- a fundamental block change is the trigger; editorial diffs usually do not require one
- a line whose turn no longer supports the current content moves to `Grounding.Drift` — demoted, not deleted
- a line unrelated to the block's concept is dropped: relatedness is the retention gate
- git history provides the block diff between a line's insertion and the current block
- demoted inline grounding also lands in `Grounding.Drift`
- it is part of `Index.Linking` maintenance — an index edit, user-gated like any other

****

## Index.Grounding

- `Index.Grounding` is the first `Context.Grounding` level — enriching the agent's context with the index's content on a topic
- routing-first selective loading: router → concept blocks → appendix depth as needed (`agentos-index --ground` is this level)
- it is the cheap default; when the digest is not enough, escalate to full grounding and reach the original surfaces

****

## Chat.Surface.Closure

- `Chat.Surface.Closure` is the principle that the system is closed over `Chat.Surface`
- chat is the near-universal ingress: users and heterogeneous agents both work through it
- in the limit, all meaningful information is contained in, or groundable to, the chat log
- the append-only `Chat.Surface` is an event log; other surfaces are materialized projections of it
- projection is not authority transfer: each projection stays SSOT of its own curated form
- `Chat.Surface` stays SSOT of the generative record, so projections remain re-derivable and drift-checkable
- boundary: chat is the dominant ingress, not total
- an out-of-band edit lands with no chat event; the gap is content no `Grounding.Head` line can support
- closure is self-healing: discussing ungrounded material is itself the grounding act
- the discussion emits the missing event and can become `Grounding.Head` evidence
- grounding is therefore never blocked, only pending; the discussion must re-establish the content, not just mention it
- closure (groundable in principle) holds at every moment; completeness (grounded now) is only the limit
- in the limit the chat log is a sufficient generative basis: every projection is reconstructable from it

****

## Agentos.Index.Notes

- `Agentos.Index.Notes` is one of the `Stable.Surfaces` of an Agentos-style project — the index flat files
- implements the `Agentos.Index` — `Index.Skillware` for project knowledge
- four roles: conceptual implementation of the system, discovery and navigation index, development surface, main alignment surface
- contains `Named.Concepts` written in `Index.Block` blocks, organized in flat index files
- agents operate the index by loading it through its `Package.Driver`; what loads is governed by the driver, not by the index — the index has no loading policy of its own
- catalog and model are the same act: naming and defining the parts is the modeling; elements and their interactions are both concepts, so one primitive (`Kernel.Block`) carries the whole mental model

****

## Index.Concept.Coverage

- `Index.Concept.Coverage` is the goal that the index covers all `Named.Concepts` in the project
- any `Dotted.Name` that appears in a stable surface should have an index entry
- concepts can emerge anywhere — authors use `Dotted.Notation` naturally without worrying about index maintenance
- the system detects new `Named.Concepts` and triggers index updates separately

****

## Index.Block

- `Index.Block` is a `Kernel.Block` placed in an `Index.Chapter` — the routed, loadable unit of meaning in the Index
- [DC] its heading is a legal `Skw.Address.Schema` name — the root of the concept's `Block.Path`s and what `000-INDEX.md` routes ^20260712-5
- it is `Kernel.Writing` under tight compression — conceptual completeness in few lines, depth pushed to `Concept.X/Appendix`
- it must carry enough signal for an agent to reason correctly about the concept
- the Index must have a block for any meaningful concept; it may link out rather than define everything inline
- `Verbatim.User.Gated` — user approves exact wording before commit
- it must not become a transcript, changelog, dashboard, task list, or implementation dump

### meta

- aliases: `Global.Block`, `Concept.Block`

****

## Appendix.Block

- `Appendix.Block` is a `Kernel.Block` placed in the appendix — a path-child of a concept (`Concept.X/Appendix`, `Concept.X/Concept.Y`)
- it is `Kernel.Writing` at relaxed constraints — depth over compression, no line-count ceiling, though line-length discipline still applies
- content is not limited to conceptual depth — specs, raw ideas, parked material belong, filed under the nearest concept (`Concept.Explosion`)
- the discipline is at the insertion point — find the right concept, then write freely under it
- `Edition.Trigger.User.Gated` only — the user initiates, but exact wording is not gated; the low-friction half of `Writing.Friction.Reduction`
- reached by `Appendix.Discovery`, not routed

****

## Design.Block

- `Design.Block` is `Kernel.Block` used in design artifacts — fundamentals, grounding, and appendix in a single block
- holds the full state of a concept in one place — used in conversations and design sessions
- at promotion time: fundamentals compress into `Index.Block`, appendix material goes to `Appendix.Block`
- the distinction: `Index.Block` is compressed, `Appendix.Block` is exhaustive, `Design.Block` is both together
- preserve user's wording when it carries design judgment

### meta

- aliases: `Design.Block`, `Design.Session.Block`, `Design.Index.Block`

****

## Md.Surface

- `Md.Surface` is the markdown layer of a project — the set of `.md` files
- parameterized to scope: `Md.Surface::Agentos`, `Md.Surface::Agentos.Stack`

****

## Dotted.Notation

- `Dotted.Notation` identifies named concepts in an ontology surface
- [DF] it is the concept form of `Skw.Address.Schema` — compact, symbolic, natural-text friendly ^20260712-3
- a dotted name is a signal that the phrase refers to a concept, not casual prose
- [CT] every name has at least two parts — the schema's minimum-sigil rule applied to `.`; dot depth is flexible and natural to the concept ^20260712-3
- dots provide context but are not a strict hierarchy — definition and relationships live in notes and registry entries, not the name
- `Explicit.Namespace` must be explicit; do not infer a namespace from a dotted prefix alone
- a dotted name can appear before it is registered
    - agents infer concept maturity from the repository: prose-only, registry entry, or dedicated note
- registry lookup is opportunistic, not mandatory — use it when concept identity matters, avoid turning ordinary work into ontology maintenance
- [DF] type statements extend a dotted name with `::` (`Line.Type::DF`) — the full string names the entity (`Addressing.Sigil.Vocabulary`) ^20260712-3
- an approximate chat-side form exists — see `Fuzzy.Dotted.Name`

****

## File.Numbering.Protocol

- `File.Numbering.Protocol` defines numeric filename conventions for stable, addressable files in project surfaces
- numeric prefixes are stable handles — the title may change, but the prefix should not be renumbered
- canonical prefixes use three digits; allocation is append-only; gaps are allowed; do not renumber or fill gaps if unnecessary
- design depth lives in `appendix/File.Numbering.Protocol-appendix.md`
- operational allocator usage lives in `references/file-numbering-protocol.md`

### Current Agentos range model

- `000-099`: reserved files with fixed system roles
- `000-INDEX.md` — the `Index.Router`, one per `Index.Depot`, at the depot root
- `010.TODOS.md` — TODO parking, lives in `notes/live/`
- `011.ISSUES.md` — issue parking, lives in `notes/live/`
- `012.NOTEBOOK.md` — idea/observation parking, lives in `notes/live/`
- `100-299`: public `Index.Chapter` files (`design/NNN-design.md`)
- `300-499`: local `Index.Chapter` files (project depot)
- `500-999`: rolling other files (live notes, live scripts)

### CLI support

- `agentos stdlib prefix` provides deterministic allocation
- desired direction: project-wide duplicate detection, range validation, append-only enforcement

****

## Maintenance.System

- `Maintenance.System` defines how a project surface is diagnosed over time
- diagnosis-first, not fix-first — report issues with evidence, then the user decides
- parameterized: `Maintenance.System::Agentos` is the Agentos instance
- reports must be evidence-based — suggestions without evidence must be marked as such

****

## Index.Editor.Maintenance.Pass

- `Index.Editor.Maintenance.Pass` is the maintenance check performed when editing an existing authoritative concept block
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

## Dot.Agentos.AGENTS.File

- `Dot.Agentos.AGENTS.File` is the Agentos-local instruction file at `.agentos/AGENTS.md`
- human-writable — contains project-specific guidance for Agentos workflows and skills
- skills may load it when they need custom local instructions or interpretation guidance
- does not define project identity — the marker remains `.agentos/project.json`
