> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Agentos.Skillware

- `Agentos.Skillware` is the discipline of treating skills as software — the skill is the unit of software for agents.
- "as software" means the artifacts agents run gain engineering structure — modules, dependencies, builds, versions, lineage — so they can be reused and evolved rather than written once and forked.
- it is supported by a development toolchain — linters, builders, compilers — spanning agentic and `CPU.Impl` work, that moves package maintenance off the human.
- a discipline realized by capabilities, not a single mechanism — it names the stance; specific members implement it.

### meta

- `Explicit.Namespace`; members: `Skill.Module`, `Skill.Runnable.Surface`, `Skill.Build.Surface`, `Skill.Package.Builder`, `Derivation.Rule`, `Derived.Content`, `Module.Dependency.Management`, `Derived.Module`, `Derivation.Manifest`, `Semantic.Router`, `Usage.Pattern.Routing`.

****

## Skill.Runnable.Surface

- `Skill.Runnable.Surface` is a surface whose purpose is to be run — loaded into agent context to do work; it carries only the executable substance.
- the system keeps it free of non-runnable artifacts, so nothing obscures or dilutes what runs.
- forced by context being executable — anything on it is read into context and shapes the run; non-runnable artifacts there are not inert, they interfere.

****

## Skill.Build.Surface

- `Skill.Build.Surface` is the complement of `Skill.Runnable.Surface` — it holds the artifacts that produce and maintain runnable content, and is never loaded at run time.
- it is the home for everything kept off the runnable surface: derivation context, dependency declarations, lineage, dev material.
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

## Derivation.Rule

- `Derivation.Rule` is the relation `Dependencies + Context → Derived` — the unit that produces a piece of derived content from declared dependencies, interpreted through a context.
- `Context` is everything informing the derivation other than the declared dependencies — case by case, from implicit (the derived surface itself + ambient knowledge) to explicit (written down).
- both dependencies and context span **inline + external** — carried inline in the derived surface, or external on a build surface; whatever isn't inline is written externally.
- run **forward** it (re)generates the derived; run as a **check** it answers the drift question — does the current derived still match what its dependencies + context would now produce?
- the check is the payoff: maintenance becomes a query the system runs, not vigilance the user keeps — and maintenance is derivation's main cost.

****

## Derived.Content

- `Derived.Content` is the *Derived* side of a `Derivation.Rule` — content produced from declared dependencies and a context, a projection of those sources rather than authored standalone.
- granular — any span of a module can be `Derived.Content`; the rest is original content, and the original/derived ratio is just how much of a module is derived.
- its tie to its sources automates drift detection and aids regeneration — drift is caught when sources change; regeneration is supported by the kept context.

****

## Module.Dependency.Management

- `Module.Dependency.Management` is the part of the Skillware module model that maintains a module's `Derivation.Rule`s — tracking dependencies and the context so derived content can be drift-checked and regenerated.
- it records, per derived span, the dependencies (by durable address) and the context, and re-runs the rule on demand.
- the more derived a module, the more its maintenance automates — derived spans re-project, while original content and the seams where it meets derived content stay manual.
- dependencies are addressed by the in-place linking mechanism — `Dotted.Names` for blocks, `Chat.Ref`/`Chat.Grounding` for chat fallback dependencies.

****

## Derived.Module

- `Derived.Module` is a `Skill.Module` whose content is mostly `Derived.Content` — the high-derivation pole.
- source-agnostic — its sources may be index blocks or other modules; derived-ness is the ratio, not the surface.
- the more derived it is, the more its maintenance automates — largely a projection of its sources, re-derived on change, with human work only at the seam with original content.

****

## Derivation.Manifest

- `Derivation.Manifest` is the explicit artifact for a `Derivation.Rule` — it carries the parts of the rule (declared dependencies + external context) not already inline in the derived surface.
- it lives on the `Skill.Build.Surface` (under `build/derivation/`), kept off the runnable surface.
- it names each dependency by a durable address and holds the external context, so a maintainer or agent can re-derive and drift-check from one known place.

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

- `Writing.Friction.Reduction` is the principle that the Agentos system lowers the cost of capturing design as it is discussed — by routing capture to the surface whose friction matches it
- friction is a designed gradient, and friction buys authority: `Chat.Surface` (free — talk is capture) → `Index.Agendix` (zero user friction, agent-driven, no authority) → `Index.Appendix` (`Kernel.Line`-level approval) → `Index.Main` (`Kernel.Block`-level work unit)
- the aim is to capture as much of the user's design as possible before it is lost — structure is deferred, not skipped
- the index keeps a friction floor on purpose — too-cheap writing would flush the hugentic surface; the friction is part of the alignment
- on touched surfaces the approval gate stays — friction drops, the gate does not

****

## Index.Agendix

- `Index.Agendix` is the agent-driven shadow of the Index — an untouched member of the index surface, one file per `Index.Main` concept: `agendix/Concept.X-agendix.md`, next to `appendix/`
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
- `Index.Linking` is its dual: linking builds and maintains the pointers grounding follows

****

## Index.Linking

- `Index.Linking` is constructing and maintaining the index's pointers back to the surfaces it indexes — support on the `Chat.Surface` (or code, or files) for index blocks and lines
- without the links back, the index cannot be checked for completeness or correctness against the touched record
- it lands in the block's grounding section (`Concept.X/Grounding`), carried as `Grounding.Entry` rows
- it is an index edit — user-gated like any edit (`Edit.Trigger.Gated`, `Content.Verbatim.Gated`); in the `Agendix` linking runs open, agent-driven (dealt with later)
- it is the dual of `Context.Grounding`: linking builds the pointers, grounding follows them
