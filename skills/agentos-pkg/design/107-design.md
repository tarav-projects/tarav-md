> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Agentos.Skillware

- `Agentos.Skillware` is the discipline of treating skills as software — the skill is the unit of software for agents.
- "as software" means the artifacts agents run gain engineering structure — modules, dependencies, builds, versions, lineage — so they can be reused and evolved rather than written once and forked.
- it is supported by a development toolchain — linters, builders, compilers — spanning agentic and `CPU.Impl` work, that moves package maintenance off the human. ^20260627-0
- a discipline realized by capabilities, not a single mechanism — it names the stance; specific members implement it.

### meta

- `Explicit.Namespace`; members: `Skill.Module`, `Skill.Runnable.Surface`, `Skill.Build.Surface`, `Skill.Package.Builder`, `Derivation.Rule`, `Derived.Content`, `Module.Import`, `Import.Management`, `Derived.Module`, `Import.Manifest`, `Semantic.Router`, `Usage.Pattern.Routing`.

****

## Skill.Runnable.Surface

- `Skill.Runnable.Surface` is a surface whose purpose is to be run — loaded into agent context to do work; it carries only the executable substance.
- the system keeps it free of non-runnable artifacts, so nothing obscures or dilutes what runs. ^20260627-2
- forced by context being executable — anything on it is read into context and shapes the run; non-runnable artifacts there are not inert, they interfere.

****

## Skill.Build.Surface

- `Skill.Build.Surface` is the complement of `Skill.Runnable.Surface` — it holds the artifacts that produce and maintain runnable content, and is never loaded at run time. ^20260627-1
- it is the home for everything kept off the runnable surface: derivation context, dependency declarations, lineage, dev material. ^20260627-1
- never run, it carries no "stay clean" constraint — an unconstrained workspace; that freedom is what the two-surface split buys.
- it lives in a per-package `build/` folder — build-time material organized by capability (derivation, tests, lint, lineage), discovered by convention.

****

## Skill.Package.Builder

- `Skill.Package.Builder` is the support system for developing and maintaining a skill package's `Skill.Runnable.Surface`
- it is a bundle of agentic skills and CLI support tooling that run build workflows over the package
- a build workflow either produces runnable content or checks it — builds, drift-checks, tests, lint
- it is open-ended — any build workflow can be added; derivation is one capability, not the whole system
- the `Skill.Build.Surface` is its workspace — it holds anything the builder needs that should not live on the `Skill.Runnable.Surface`
- realized as the `agentos-skill-pkg-builder` `Package.Aux.Skill`, which centralizes the build-related `Skill.Module`s

****

## Module.Import

- [DF] `Module.Import` is a declared dependency between surfaces — a consumer surface imports a target named by any legal block name (`Block.Naming.Schema`) ^20260709-12
- [DC] three binding modes: `pointer` — resolved at load time, always fresh; `copy` — verbatim materialization at build time; `derived` — a semantic transformation materialized at build time, governed by a `Derivation.Rule` ^20260709-14
- [DC] the binding is the consumer's declaration — the imported surface never knows its importers ^20260709-12
- [DC] declarations live on the `Skill.Build.Surface`; the `Skill.Runnable.Surface` carries only the materialized result — a routed pointer or the inlined content ^20260709-13
- each binding carries a checkable claim: pointer — the target resolves at its address; copy — equality with the target; derived — the rule still holds ^20260709-16
- [DC] a failed check is a drift finding with no predefined winner — resolution is case-by-case; a particular workflow may set auto-regeneration as its own rule ^20260709-15
- it is the Skillware linking system: copy and derived are static binding, pointer is dynamic ^20260709-12

****

## Derivation.Rule

- `Derivation.Rule` is the relation `Dependencies + Context → Derived` — the unit that produces a piece of derived content from declared dependencies, interpreted through a context.
- `Context` is everything informing the derivation other than the declared dependencies — case by case, from implicit (the derived surface itself + ambient knowledge) to explicit (written down).
- both dependencies and context span **inline + external** — carried inline in the derived surface, or external on a build surface; whatever isn't inline is written externally.
- run **forward** it (re)generates the derived; run as a **check** it answers the drift question — does the current derived still match what its dependencies + context would now produce?
- the check is the payoff: maintenance becomes a query the system runs, not vigilance the user keeps — and maintenance is derivation's main cost.
- it is the mechanics of the `derived` binding of `Module.Import`; the `copy` binding needs no rule — equality is its whole check ^20260709-14

****

## Derived.Content

- `Derived.Content` is the *Derived* side of a `Derivation.Rule` — content produced from declared dependencies and a context, a projection of those sources rather than authored standalone.
- granular — any span of a module can be `Derived.Content`; the rest is original content, and the original/derived ratio is just how much of a module is derived.
- its tie to its sources automates drift detection and aids regeneration — drift is caught when sources change; regeneration is supported by the kept context.

****

## Import.Management

- `Import.Management` is the part of the Skillware module model that maintains a module's `Module.Import`s — tracking each import's target and binding so materialized content can be checked and regenerated ^20260709-16
- it records, per import, the target (by durable address), the binding, and any context, and re-runs the check or the materialization on demand
- pointer bindings are checked for address validity, copy for equality, derived for `Derivation.Rule` drift ^20260709-14
- the more imported a module's content, the more its maintenance automates — imported spans re-materialize, while original content and the seams where it meets them stay manual
- targets are addressed by legal block names — `Dotted.Name`s for blocks, locator names for files and regions, `Anchory.Anchor`/`Chat.Grounding` for chat fallback dependencies

****

## Derived.Module

- `Derived.Module` is a `Skill.Module` whose content is mostly `Derived.Content` — the high-derivation pole.
- source-agnostic — its sources may be index blocks or other modules; derived-ness is the ratio, not the surface.
- the more derived it is, the more its maintenance automates — largely a projection of its sources, re-derived on change, with human work only at the seam with original content.

****

## Import.Manifest

- `Import.Manifest` is the explicit artifact for a module's `Module.Import` declarations — it names what the module imports and under which binding ^20260709-16
- for a `derived` binding it carries the `Derivation.Rule` parts (declared dependencies + external context) not already inline in the derived surface
- it lives on the `Skill.Build.Surface` (under `build/imports/`), kept off the runnable surface ^20260709-13
- it names each target by a durable address, so a maintainer or agent can check and re-materialize from one known place

****

## Semantic.Router

- `Semantic.Router` is a Skillware primitive: a key:value table where keys are natural-language situation descriptions and values are linked resources (a prompt, a `Skill.Module`, content, or another `Semantic.Router`).
- routing is semantic and agentic — the agent matches the live situation against the key descriptions and selects; keys must be discriminative.
- it offers options, not an order — an unordered set; the router states a `Router.Selection.Contract` so the reader knows that selecting none, one, or several rows is all normal.
- it composes — a value can be another `Semantic.Router`, giving progressive, multi-level selection.

****

## Usage.Pattern.Routing

- `Usage.Pattern.Routing` is `Semantic.Router` routing whose rows are usage patterns — keys are usage situations, values are the response for each (knowledge/surfaces to load, what to produce).
- its keys are mined from real usage — chats, repeated questions, observed friction — so the routing grows cheaply and stays reality-weighted.
- it optimizes frequent or important situations (a hot path); an unmatched situation selects nothing and falls back to the package's general routing.

****

## Specified.By.Precedence

- `Specified.By.Precedence` is a design pattern: when no explicit specification is in sight, constrain new work by the shape of the existing implementations
- the already-built instances serve as the `Reference.Implementation` for the ones not yet built — precedent is the spec
- it trades an authored contract for imitation: a new instance reads its antecedents and follows their shape
- the format evolves and converges naturally — each addition both follows and extends the precedent, no central definition to maintain
- use it where a rigid spec would over-specify a still-soft, still-converging pattern; an explicit spec, once it appears, supersedes precedent
- distinct from `Reference.Implementation`: that names one canonical owner of a contract; here the whole existing set is the soft, emergent spec

****

## Index.Main

- `Index.Main` is the main body of the Index — the routed layer of concept fundamentals, spanning the `Index.Chapter` folders
- it is the index-level echo of `Kernel.Block.Fundamentals`: the compressed front, with depth deferred to `Index.Appendix`
- it holds the `Index.Block`s under tight `Kernel.Writing` compression, every one routed by `Index.Router`
- it is the complement of `Index.Appendix` — main body vs appendix, the split a book makes: main is routed, appendix is discovered (`Appendix.Discovery`)
- with `Index.Appendix` and `Index.Router` it composes the `Index.Surface`

### meta

- aliases: `Index.Fundamentals`

****

## Index.Surface

- `Index.Surface` is the file surface of one Index — `Index.Router`, `Index.Main`, and `Index.Appendix` taken as a single addressable surface
- it is a `Surface.Concept`: the bytes on disk, distinct from `Agentos.Index.System`, which is what those bytes do (the operable `Soft.Programming.Language`)
- it follows the `Index.Surface.Layout` directory protocol; one `Index.Surface` per `Index.Depot`
- it is the outermost layer of the nested index — the index of the project across its surfaces (`Surface.Types`), foremost the `Chat.Surface` where design originates

****

## Index.Discovery

- `Index.Discovery` is how an agent finds the `Index.Depot`s available to engage
- a depot is marked by a `000-INDEX.md` — its presence identifies an engageable index on a skill or project
- declared discovery walks the dependency graph: a project's `Project.Manifest` and each package's `Package.Manifest`
- fallback discovery: when nothing declares them, search for `000-INDEX.md` across skills and projects — cheap
- discovery is hierarchical (the dependency graph) but engagement is flat — discovered depots are peers, each router a `Semantic.Router`, routed equally
- a workflow scopes the discovered set by agent common sense — conversation context, skill descriptions, task relevance — defaulting to the whole engaged set

****

## Block.Line.Gradient

- `Block.Line.Gradient` is the ordering of a concept's lines from most fundamental to most accidental
- line 0 is typically a direct definition (`Concept.X` is …); each later line tends to be more specific than the one before
- the order continues unbroken into the appendix — the appendix is the tail of the same sequence, not a separate object
- the further down the sequence a line sits, the less fundamental to the concept it can be — the tail admits lines merely filed under it
- the index/appendix split — and the cuts between appendix pages — are artificial cuts on this sequence, placed for token economy
- fundamentals are the prefix you keep if you can read only a few lines; the appendix is the rest, loaded on demand
- coherence is a gradient too: tight in the fundamentals, relaxing in the appendix, where loosely-related lines accrete without earning the core's coherence

****

## Appendix.Default.Block

- `Appendix.Default.Block` is the catch-all block every concept has by default, addressed `Concept.X/Appendix`
- its name is the full path — a child block of the `Concept.X` node, sharing the `Concept.Scoping` container-first notation
- it holds the tail of the concept's `Block.Line.Gradient` — the lines past the index/appendix cut
- it has no space budget — it grows freely, in `Kernel.Writing` style (direct, orthogonal lines)
- it is the landing site for `Writing.Friction.Reduction` capture and `Concept.Explosion` appends — facts filed under a concept without minting a name

****

## Writing.Friction.Reduction

- `Writing.Friction.Reduction` is the principle that the Agentos system lowers the cost of capturing design as it is discussed — by routing capture to the surface whose friction matches it ^20260705-3
- friction is a designed gradient, and friction buys authority: `Chat.Surface` (free — talk is capture) → `Index.Agendix` (zero user friction, agent-driven, no authority) → `Index.Appendix` (`Kernel.Line`-level approval) → `Index.Main` (`Kernel.Block`-level work unit) ^20260705-2
- the aim is to capture as much of the user's design as possible before it is lost — structure is deferred, not skipped ^20260705-3
- the index keeps a friction floor on purpose — too-cheap writing would flush the hugentic surface; the friction is part of the alignment ^20260705-3
- on touched surfaces the approval gate stays — friction drops, the gate does not ^20260705-3

****

## Index.Agendix

- `Index.Agendix` is the agent-driven shadow of the Index — an untouched member of the index surface, one file per `Index.Main` concept: `agendix/Concept.X-agendix.md`, next to `appendix/` ^20260705-2
- it is a cache the agent keeps to aid grounding on stable surfaces — no stable surface may link into it; promotion copies an entry out through the normal gates (including into the index)
- the agent cannot mint concepts — it attaches lines under existing routed concepts; the ontology primes the capture, the agent fills the gaps — the index's shadow, not a second index ^20260705-2
- hard rule: every line is a grounded summary of chat discussion — a rejection, a constraint, a highlight the index does not yet capture — carrying its `Anchory.Anchor`/`File.Mention` pointer; unsourced agent reasoning does not belong ^20260705-2
- writing rules are the appendix's — `Kernel.Writing` discipline, the same block and line forms; only the supervision differs: all work is done and supervised by agents
- capture is user-triggered but not gated — the agent may suggest a capture pass, never start one
- it extends the `Block.Line.Gradient` past the touch cut: fundamentals → `Concept.X/Appendix` (touched tail) → the concept's agendix shadow tail (untouched) ^20260705-2
- homeless material lands in a fallback file — misfit pressure is evidence a concept is missing (concept-gap detector) ^20260705-2
- it is index-adjacent, not part of the index — it softens the index principles on the fly, replacing the direct user touch with a grounding link to the touch event
- it is self-similar to the appendix — an untouched appendix, same form and rules; it exists because the user gate is the bottleneck: a surface for the agent to run ahead of the gate
- agendix and appendix must not duplicate content — over time the agendix drains: entries reviewed by the user are promoted through the gate or dropped
- in alignment terms: `Untouched.Space` made durable — visible, assumed untouched by the user, non-aligned; zero authority, freely rewritable; everything in it is promotion evidence
- agendix lines are typed: every line carries a `Line.Type` from the vocabulary — the validation point applies to agent capture too ^20260707-2
- [DC] agendix lines may be assistant-grounded, marked `[AS:XX]`; promotion re-grounds on the approving user turn and drops the marker
- [DC] agendix files follow appendix writing rules with the block headed `Concept.X/Agendix`, one file per concept in `agendix/` next to `appendix/`
- [DC] captures with no routed concept land in `agendix/Unassigned-agendix.md` — the homeless pool, promotion evidence for concepts the index does not yet name, never a dump
- [PR] the agendix is the agentic path of the alignment workflow the gated edit runs hugentically — same primitives (typed `Kernel.Line`s, anchors, the current concept set), the user gate replaced by hard provenance ^20260708-4
****

## Concept.Explosion

- `Concept.Explosion` is the failure where splitting every fact into its own named concept floods the index with low-value names
- a name should be a real node in the system's mental model — earned by being worth navigating to, not minted for every fact
- the remedy is to append a fact to the nearest fitting concept rather than name it
- slight misplacement is acceptable — capture beats taxonomy; the fact is recorded and can be relocated later
- the appendix absorbs what does not deserve a name

****

## Tail.Capture

- `Tail.Capture` is the parallel task in the alignment loop of growing a concept's tail alongside its fundamentals
- the tail is the accepted constraints, issues, edge cases, and rejected alternatives — the `Block.Line.Gradient` past the fundamentals
- working a concept is working both: most turns grow the tail, while the fundamentals stabilize and change less
- it stays user-gated — captured through the alignment loop like any index/appendix write, not auto-written
- the default move: append a valuable, accepted point to the nearest concept's appendix (`Appendix.Default.Block`, `Concept.Explosion`)
- the tail is subject to `Natural.Placement` — it holds what no other surface holds, or what is worth stating more explicitly here
- dropping the tail is the main way user-discussed design is lost; fundamentals survive, the rest evaporates

****

## Kernel.Line

- `Kernel.Line` is the atom of index content — one statement carried by a block, the unit that accretes
- it is read in the context of its block: the block is the frame, so a line stays terse and may omit what the block already establishes (`Name.As.Index`)
- one point per line is a soft direction, not a rule — the violation is one line carrying two distinct facts; a single point spanning a few lines is fine
- every line is precious — it reflects something the user asked for or approved (`Content.Verbatim.Gated`), never filler
- lines order along the `Block.Line.Gradient`; block coherence is tight in the fundamentals and relaxes in the appendix

****

## Index.Edit.Action

- `Index.Edit.Action` is the small set of moves that edit the index — each a named action chosen by the case that calls for it
- the moves: `Index.Edit.Create.Block`, `Index.Edit.Append.Line`, `Index.Edit.Modify.Line`, `Index.Edit.Revise.Block`
- two tempos: hot capture (append during the `Alignment.Loop`) and cold consolidation (a maintenance pass over accumulated lines, where `Index.Edit.Create.Block` and `Index.Edit.Revise.Block` mostly live)
- the bias is the lowest-cost action that captures the aligned content (`Writing.Friction.Reduction`)
- every action is user-gated and `Content.Verbatim.Gated` — it is the index

****

## Index.Edit.Create.Block

- `Index.Edit.Create.Block` is the `Index.Edit.Action` of adding a new named concept block to the index
- the case: a genuinely new concept appears — coined by the user, or revealed when accreted lines show a pattern during consolidation
- the naming hint: when lines need to be referenced — cited from elsewhere, or pointed at as a group — they need a name; referenceability is what earns a block
- it is the higher-cost action — a new frame, a router entry, a placement decision; prefer `Index.Edit.Append.Line` unless the concept is genuinely new
- it mostly lives in the cold tempo, extracted from accumulated lines, not coined hot

****

## Index.Edit.Append.Line

- `Index.Edit.Append.Line` is the `Index.Edit.Action` of adding a `Kernel.Line` to the nearest coherent block — the default index edit
- it is the lowest-cost capture path, which is why it is the first beat: drop the line, do not stop to architect a block
- landing selection picks the nearest coherent frame — a concept block, its appendix, or a namespace for subsystem-level lines
- it is a load-then-word operation: select the block, bring it into context, then word the line against what it already says
- the block defines the wording — terse, framed, non-redundant — never generated blind and attached

****

## Index.Edit.Modify.Line

- `Index.Edit.Modify.Line` is the `Index.Edit.Action` of refining or correcting an existing `Kernel.Line`, keeping its block
- the case: a statement already in the block is wrong, imprecise, or superseded by aligned discussion
- like `Index.Edit.Append.Line` it is load-then-word — the block and the existing line both frame the new wording
- it is `Content.Verbatim.Gated` — the replacement wording is approved before commit
- prefer it over stacking a contradicting append: a corrected line beats two lines that disagree

****

## Index.Edit.Revise.Block

- `Index.Edit.Revise.Block` is the `Index.Edit.Action` of restructuring a block whose frame no longer holds its accreted lines
- the case: lines have piled up past the block's coherence — it needs reorder, split, or promotion of lines into the appendix
- it is a consolidation move, cold tempo — done with the warm context gathered while chatting, not hot
- it may spawn `Index.Edit.Create.Block` when a promoted cluster of lines earns its own name
- it preserves the lines — restructuring moves and reframes them, it never discards aligned content

****

## Partial.Cite

- `Partial.Cite` is using a shortened form of a `Dotted.Name` when it still resolves unambiguously
- legal when the short form has no collision in the engaged indexes, or the full name was already cited in the same document
- it is pure ergonomics — `Append.Line` for `Index.Edit.Append.Line` once the family is established
- the canonical name is always the full path; the router and block headings carry it — shortening is reader-facing convenience only
- it is the authoring side of `Fuzzy.Dotted.Name`: resolution tolerates approximation, `Partial.Cite` deliberately relies on it

### meta

- aliases: `Partial.Name`

****

## Context.Grounding

- `Context.Grounding` is enriching an agent's context with `Hard.Evidence`-linked data before it acts
- foundation: all `User.Touched` data is on the `Chat.Surface`; the index is an index of it and points back to it — for completeness and correctness checking
- it runs at levels: `Index.Grounding` loads the index's digest of the topic; full grounding also follows the pointers out to the original surfaces — the chats via Chatlas + git history, the code directly
- it is read-only and ungated — it changes the agent's context, never a surface
- grounded blocks make prior work reusable — settled context reaches the agent without the user re-explaining it
- [CT] grounding reaches chat surfaces only through `agentos chatlas` commands — never provider raw stores or transcript files ^20260708-0
- `Index.Linking` is its dual: linking builds and maintains the pointers grounding follows

****

## Index.Linking

- `Index.Linking` is constructing and maintaining the index's pointers back to the surfaces it indexes — support on the `Chat.Surface` (or code, or files) for index blocks and lines
- without the links back, the index cannot be checked for completeness or correctness against the touched record
- it lands in the block's grounding section (`Concept.X/Grounding`), carried as grounding lines — an `Anchory.Anchor` plus a one-sentence note
- it is an index edit — user-gated like any edit (`Edit.Trigger.Gated`, `Content.Verbatim.Gated`); in the `Agendix` linking runs open, agent-driven (dealt with later)
- [CT] linking accesses chat data only through `agentos chatlas` commands — never provider raw stores or transcript files ^20260708-0
- it is the dual of `Context.Grounding`: linking builds the pointers, grounding follows them

- [DC] linking mostly happens on the edge — anchoring content produced in the current session; self-session discovery by content matching is the entry step ^20260708-1
****

## Index.Enrichment

- [DF] `Index.Enrichment` is the hugentic drive to always increase the `Touched.Surface` of any block or line — no block is finished ^20260709-7
- [DC] grounding and enrichment split by evidence source: grounding is retrospective, mining the existing chat corpus; enrichment is generative, producing new touched surface ^20260709-8
- the discussion is the yield: spawning a focused discussion about a block creates the user turns that become its new grounding surface — and, through the gate, possibly new content ^20260709-7
- [DC] `Grounding.Density` reads as pipeline position: zero → mine the corpus first (grounding); low → generate (enrichment); high → rest until touched again ^20260709-8
- enrichment is block-scoped and gated — a micro design-session one block wide; the block's density delta is the receipt ^20260709-9
****

## Git.Dating

- [DF] `Git.Dating` is dating a file or file line by finding its last change in the git history ^20260709-10
- the date turns a static artifact into a searchable event: it says where in time to look further about the target — for instance in the chat corpus ^20260709-10
- [DC] the commit dates the write; the originating evidence is earlier — search around and before the commit time, not at it ^20260709-11
- `git log -L` follows a line's wording past mechanical commits to the content-bearing ones ^20260709-11
- it is the entry step of backward grounding: git dates the wording, chatlas finds the session and turns ^20260709-11
****

## Anchory.System

- `Anchory.System` is the Agentos subsystem for stable symbolic links to contexts on other surfaces
- `Anchory.Anchor` carries compact identity while `Anchory.Register` carries resolution data
- `Anchory.Namespace` partitions anchor keys into independent resolution domains
- Anchory is Agentos-wide rather than project-local ^20260706-1
- Anchory is library-first so other subsystems can integrate directly
- integrating subsystems own payload meaning and final traversal to referenced surfaces
- `agentos anchory ...` is a thin CLI over the library contract
- referenced surfaces remain authoritative; Anchory is plumbing, not truth

### meta

- namespace-members: `./Anchory.Anchor`, `./Anchory.Namespace`, `./Anchory.Register`, `./Anchory.Record`, `./Anchory.Depot`, `./Integration`, `./Chat.Application`, `./Open.Design`
****

## Capture.Offer

- [DF] `Capture.Offer` is the practice of proposing an index capture at the moment the content is born — the exact typed line or block, verbatim, user-gated
- [PR] capture is cheapest at the moment for both sides: the agent's context is hot and the anchor mintable on the spot; the user's judgment is hot too — reviewing now beats reconstructing later
- [DC] an offer presents destination options: index main, appendix, agendix, or decline — the user picks the landing with the gate
- [DC] an offer arrives landing-ready: proposed type carried, target scouted for each destination it offers
- [DC] it is the hugentic sibling of agendix capture — same trigger instinct, the user gate in place of hard provenance
- [DC] offers ride any workflow — impl execution, design, review; declining is cheap and normal, the offer must never block the work
