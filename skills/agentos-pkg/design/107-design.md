> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Agentos.Skillware

- `Agentos.Skillware` is the discipline of treating skills as software — the skill is the unit of software for agents.
- "as software" means the artifacts agents run gain engineering structure — modules, dependencies, builds, versions, lineage — so they can be reused and evolved rather than written once and forked.
- it is supported by a development toolchain — linters, builders, compilers — spanning agentic and `CPU.Impl` work, that moves package maintenance off the human. ^c20260627-0u
- a discipline realized by capabilities, not a single mechanism — it names the stance; specific members implement it.
- **skw** is the system realizing the discipline: the general annotation language (`Skw.Language`) and its `Skw.Backend`s ^c20260711-9u
- [DC] the `Touched.Surface.Index` is not a separate substrate: touch is an orthogonal axis over skw objects — any annotation, span, or line may be touched or not, and the TSI is the computed set of touched things ^c20260719-0u
- [DC] an annotation can be touched itself, independently of its dependencies: its support lines ground its own existence and shape to user turns — annotations range from fully agent-built to user-discussed ^c20260719-0u
- [PR] skw is where the touched-index concepts integrate at scale: declared dependencies between any two project surfaces make maintenance and change propagation explicit, and extend the `Touched.Surface.Index` to further surfaces ^c20260718-23u
- [DC] the toolchain speaks skw: `agentos skw` (build, check, bless, status) over `.skw/` build homes and `skw.json` config — `skillware` remains a deprecation alias; `agentos skw check` with no target runs project-wide over every discovered `Skw.Package`, making the whole `Skw.Network` checkable in one pass ^c20260720-13u

### meta

- `Explicit.Namespace`; members: `Skill.Module`, `Skill.Runnable.Surface`, `Skill.Build.Surface`, `Skill.Package.Builder`, `Skw.Package`, `Skw.Dependency`, `Skw.Quote.Binding`, `Skw.Language`, `Skw.Annotation`, `Skw.Backend`, `Annotation.Point`, `Annotation.Authority`, `Drift.POI`, `Semantic.Router`, `Usage.Pattern.Routing`.

****

## Skill.Runnable.Surface

- `Skill.Runnable.Surface` is a surface whose purpose is to be run — loaded into agent context to do work; it carries only the executable substance.
- the system keeps it free of non-runnable artifacts, so nothing obscures or dilutes what runs — a building-backend discipline; annotated-only `Skw.Backend`s trade it for constraint co-location. ^c20260627-2u ^c20260711-9u
- forced by context being executable — anything on it is read into context and shapes the run; non-runnable artifacts there are not inert, they interfere.

****

## Skill.Build.Surface

- `Skill.Build.Surface` is the complement of `Skill.Runnable.Surface` — it holds the artifacts that produce and maintain runnable content, and is never loaded at run time. ^c20260627-1u
- it is the home for everything kept off the runnable surface: derivation context, dependency declarations, lineage, dev material. ^c20260627-1u
- never run, it carries no "stay clean" constraint — an unconstrained workspace; that freedom is what the two-surface split buys.
- realized as the per-package `.skw/` folder (legacy `.skillware/`, still read during the rename window) — `src/` mirror, `skw.json` settings, lock — organized by capability, discovered by convention. ^c20260710-2u ^c20260720-13u

****

## Skw.Package

- [DF] a `Skw.Package` is a folder whose `.skw/` holds a `src/` of `*.skw.md` sources — the unit skw discovers, checks, and builds; the `src/` is what makes it a package ^c20260720-13u
- [DC] git-tracked: `.skw/` holds `skw.json` config, the `src/`, and `lock.json`; `.agentos/` keeps only project identity and runtime, while the tracked skw source lives in `.skw/` ^c20260720-9u ^c20260720-13u
- [DC] scope mirror: one `skw.json` schema (`depots`, `surfaces`, `exclude`, `projects`) read at both project and package scope, the package extending the project via cascade; absent config means discover every `.skw/` and check all ^c20260720-9u

****

## Skill.Package.Builder

- `Skill.Package.Builder` is the support system for developing and maintaining a skill package's `Skill.Runnable.Surface`
- it is a bundle of agentic skills and CLI support tooling that run build workflows over the package
- a build workflow either produces runnable content or checks it — builds, drift-checks, tests, lint
- it is open-ended — any build workflow can be added; derivation is one capability, not the whole system
- the `Skill.Build.Surface` is its workspace — it holds anything the builder needs that should not live on the `Skill.Runnable.Surface`
- realized as the `agentos-skillware` `Package.Aux.Skill`, which centralizes all Skillware `Skill.Module`s — build toolchain, language, authoring, doctrine ^c20260710-2u

****

## Skw.Dependency

- [DF] `Skw.Dependency` is a declared dependency between any two surfaces — a consumer declares a target named by any legal `Skw.Address.Schema` name ^c20260709-12u ^c20260712-10u ^c20260719-1u
- [DC] three binding modes: `pointer` — resolved at load time, always fresh; `copy` — verbatim materialization at build time; `derived` — a semantic transformation materialized at build time under a recorded intent ^c20260709-14u
- [DC] the binding is the consumer's declaration — the target never knows its dependents ^c20260709-12u
- [DC] a `--from` may be refined by a `Skw.Quote.Binding` — quoted lines pinning the exact interest range inside the target ^c20260718-29u
- each binding carries a checkable claim: pointer — the target resolves at its address; copy — equality with the target; derived — the rule still holds ^c20260709-16u
- [DC] a failed check is a drift finding with no predefined winner — resolution is case-by-case; a particular workflow may set auto-regeneration as its own rule ^c20260709-15u
- it is the Skillware linking system: copy and derived are static binding, pointer is dynamic ^c20260709-12u
- [PR] division of labor: the CPU materializes copy bindings and detects drift; the agent performs derivations — in src, where the declaration and its current solution live side by side ^c20260710-0u
- [DC] on building `Skw.Backend`s, declarations live on the `Skill.Build.Surface` and the `Skill.Runnable.Surface` carries only the materialized result; annotated-only backends keep declarations in place on the surface itself ^c20260709-13u ^c20260711-9u
- [DC] v1 realization: `lock.json` holds the per-dependency record; check verdicts (`copy-drift`, `derived-stale`, `hand-edited`) surface drift — a rebuild can never silently clear `derived-stale`; only an actual re-derive does ^c20260710-2u

### meta

- aliases: `Module.Import`, `Import.Management`

****

## Skw.Quote.Binding

- [DF] `Skw.Quote.Binding` is a dependency declared by its own actual content: a `--from` address plus explicitly quoted lines defining the interest range ^c20260718-25u ^c20260718-29u
- [DC] the address is the selector — what the alarm uses to narrow the dependency; the quoted lines pin the exact range by content, not position ^c20260718-26u
- [CT] the quoted lines live on the annotation, not the generated surface — the annotation itself is maintained: a non-existing or drifted line cannot attach ^c20260718-25u
- [PR] plain block links stay legal; quoting is opt-in remarking — the quoted content sits next to the annotated surface so the generator agent cannot miss it ^c20260718-26u
- [PR] content-addressing makes the reference honest: it survives source reordering and breaks loudly under change, never silently pointing at the wrong lines ^c20260718-26u
- [DC] a quoted line no longer verbatim-present at its source raises a POI on the declaring construct — the existing unresolvable-`--from` POI extended to content ^c20260718-26u
- [DC] syntax: a repeatable `--quote` flag refining the nearest preceding `--from`; each value is one verbatim line of interest, plain continuations append ^c20260718-27u ^c20260718-28u

### meta

- aliases: `Quote.Binding`

****

## Skw.Language

- [DF] skw is an embedded annotation language for the generation of surfaces — an annotation states how a span of content is produced: from which dependencies, under which rule ^c20260711-2u
- the annotation constrains the span: the content must not contradict or drift from its declaration — every annotation is a checkable claim ^c20260711-2u
- everything frames as generation: a copy is deterministic generation (the inlining of a source, itself possibly generated); a derived span is agentic generation under its rule; a literal carries no generation claim; a link's text is a typed generated span, annotated independently of the target it points at ^c20260711-2u
- it annotates any content, but earns most on agent-generated surfaces — where the rule and its current solution living side by side is what makes maintenance checkable ^c20260711-2u
- it is embedded — skw lives inside the host surface's own format, next to the content it governs, and never replaces it ^c20260711-2u
- the language is surface-blind; a `Skw.Backend` binds it to each surface class ^c20260711-2u
- [DC] skw lines need no user grounding to be legal — touch is opt-in per object: annotations cite index blocks by `Dotted.Name`, and carry their own touched lines through `Skw.Touched.Index` ^c20260719-0u

****

## Skw.Backend

- [DF] a `Skw.Backend` binds `Skw.Language` to one surface class, named `skw-<surface>` ^c20260711-3u
- a backend owns four things: the carrier syntax, the build semantics (if any), where check state lives, and its host-native `Annotation.Point` vocabulary ^c20260711-3u
- every backend is annotated; some backends additionally build — annotation + check is the universal layer, build is backend-local ^c20260711-3u
- a building backend generates its runnable form from annotated src and strips the machinery; an annotated-only backend keeps declarations in place on the surface itself, trading surface cleanliness for constraint co-location ^c20260711-3u
- **skw-skills** is the first backend, a building one: annotated src compiles to the skill's runnable files ^c20260711-3u
- **skw-code** is the first annotated-only candidate: declarations ride the host language's comments; the body is the live fragment ^c20260711-3u

****

## Skw.Annotation

- [DF] `Skw.Annotation` is the unit of skw: one annotation attached at an `Annotation.Point`, stating extra things *about* the content it governs ^c20260711-4u ^c20260719-1u
- [DC] its written form is the construct: a `$kw:` declaration line — a CLI-style command, optional `^label`, `--flag` traits — with `$kw.` belonging lines, a flat native body, and a mandatory owned closer ^c20260710-4u ^c20260712-7u
- [DC] every machinery line carries the sigil, riding the host's carrier (blockquote in markdown, comments in code) — carrier-neutral, nothing skw inferred from bare host syntax ^c20260712-7u
- [DC] the flag vocabulary separates by what each thing binds: deps (`--from`/`--quote`) bind the governed content to its sources; supps (`--supp`) ground the annotation itself; `--intent` carries the derivation context ^c20260719-0u ^c20260719-1u
- [PR] every annotation is a checkable constraint: the CPU checks its decidable face (resolution, structure, hashes); agents check its semantic face (does the body honor the declaration) — annotations are to prose what types are to code ^c20260711-0u
- it is a deliberate subset: the fragment's fundamentals, never an exhaustive dependency capture — it answers *what context can't I miss to understand this fragment?* ^c20260711-4u
- it is a satellite index of the design — a leaf citing the canonical index by `Dotted.Name`; the hub stays the center ^c20260711-4u
- it is a local grounding recipe: an agent landing on the fragment loads the declared dependencies and holds the minimal sufficient context by declaration, not by search ^c20260711-4u
- the command vocabulary is the language's growth axis: new capability is a new command over the same construct ^c20260710-4u

### meta

- aliases: `Skillware.Construct`, `Surface.Annotation`

****

## Annotation.Point

- [DF] an `Annotation.Point` is a named, sanctioned place where annotations attach — a small vocabulary of points so agents do not over-annotate arbitrary fragments ^c20260711-5u
- points come in two families: **host-native** — the natural divisions of the annotated surface — and **skw-native** — the language's own scoping constructs, layered on top ^c20260711-5u
- [PR] prefer the host's natural divisions; reach for skw-native scoping only where the host's divisions do not fit the annotation's true scope ^c20260711-5u
- the file is the universal host point; each backend declares the rest of its host vocabulary — functions, modules, namespaces for code; sections for markdown ^c20260711-5u
- the skw-native points: the **annotation section** (a leveled, end-free divider sectioning a file for annotation purposes only) and the **span** (an explicit construct body — the finest grain) ^c20260711-5u
- the agent attaches at the coarsest point that honestly fits ^c20260711-5u

****

## Annotation.Authority

- [DF] `Annotation.Authority` is the authority model of annotations: authority flows from grounding, not from the writer ^c20260711-6u
- annotation lines take the index's own forms: `Line.Type` codes and `Anchory.Anchor`s, with the same validation points ^c20260711-6u
- authority follows `Touched.Authority`: untouched annotation lines are hypotheses bound by the grounded span; grounded ones hold second-order authority; gated ones are first-order touched ^c20260711-6u
- what stays restricted below the gate is linkability, not worth — the `Touched.Authority` fence ^c20260711-6u
- no status is stored: drift is discovered and surfaced by the checker; authority is read from the lines' provenance ^c20260711-6u
- [CT] agent-free insertion is regulated: only the file `Annotation.Point` is open to ungated agentic annotation — every finer point lands user-gated ^c20260711-6u
- finer annotations are therefore born touched: the gating turn is their grounding evidence ^c20260711-6u

****

## Drift.POI

- [DF] a `Drift.POI` is a point of interest raised by the CPU checker: a span's declared dependencies changed — that, and nothing more ^c20260711-7u
- the CPU never rules on drift: whether the surface actually drifted is an agent's finding — the agent is always the fixer and supervisor ^c20260711-7u
- a POI carries its trigger — which dependency, what changed — so the responding agent starts contextualized ^c20260711-7u
- resolution is agentic: real drift → re-derive the span; benign change → re-bless the dependencies ^c20260711-7u

****

## Closure.Parser

- [DF] a `Closure.Parser` demands a minimal structure — the `Parse.Floor` — and is closed above it: a surface below the floor is a hard parse error; a surface at the floor always yields a full AST, and no finer detail can fail the parse ^c20260712-17u
- from the `Parse.Floor` up, the parser cares only about what it recognizes: recognized regions become structured nodes, everything else becomes text nodes, and no further errors exist ^c20260712-17u
- above the floor, an unrecognized region is simply an opaque text node — the parser does not judge it; whatever might be wrong inside is a linter concern, not a parse concern ^c20260712-17u
- the parser emits exactly one kind of failure: parse errors, only below the floor — it emits no POIs ^c20260712-17u
- [PR] one broken construct never blinds the system to the whole file ^c20260712-17u
- [CT] closed also means lossless: above the floor, every byte of the input lands in some node ^c20260712-17u
- [DC] realized: the skw parser is `Closure.Parser::Skw` — its floor is well-formed, explicitly closed `$kw` machinery; above it, construct nodes and opaque text ^c20260712-17u

****

## Poi.Linter

- [DF] a `Poi.Linter` lints the AST of a `Closure.Parser`, never the native text — every lint rule is a rule about node types, not text patterns ^c20260712-17u
- [CT] the no-shadow-parser constraint: a rule targets node types and may read inside a text node, but re-parsing the surface around the AST is forbidden ^c20260712-17u
- checks are layered: parse errors gate everything — below the `Parse.Floor` the linter reports the parse errors as POIs and advances no further ^c20260712-17u
- its output is the POI stream: each POI marks a place worth an agent's attention, and nothing more — it may carry a suggested resolution, but it asserts no verdict; the agent inspects and decides ^c20260712-17u
- [PR] the softness is bought, not accidental: a linter that is always right costs a robust parser — the system stays cheap and simple by tolerating wrong and missed flags, and agents are told so ^c20260712-17u
- opaque text nodes are its territory: what the parser deliberately ignores, linter rules may inspect and flag ^c20260712-17u
- [DC] realized: `agentos skillware check` — parse errors gate per file, POIs carry stable identity hashes, output is a once-per-kind legend plus bare rows ^c20260712-17u

****

## Poi.Bless

- [DF] `Poi.Bless` is the explicit act of accepting a POI's current state as correct: an auditable command rewrites the POI's recorded expectation to match reality, and the flag clears without the surface being touched ^c20260712-17u
- [PR] blessing is loud: drift never clears as a side effect of rebuilds or unrelated edits — only a re-derivation of the content or an explicit bless (the no-silent-blessing rule generalized) ^c20260712-17u
- [CT] not every POI is blessable: parse errors are never blessable — a surface below the `Parse.Floor` is not in the language and must be fixed; blessability belongs to semantic POIs, where the current state might genuinely be the truth ^c20260712-17u
- [DC] realized: `agentos skillware bless --poi <hash>` — rewrites the recipe's locked dependency hashes to current, body untouched; only `derived-stale` accepts it ^c20260712-17u

****

## Structure.Ratchet

- [DF] the `Structure.Ratchet` is the system's direction of travel: over time, content moves from opaque text nodes into recognized structure — the target state is a fully structured surface where all remaining prose is ACTUAL prose: no parsable objects remain in the text ^c20260712-17u
- progress is measurable: the `Closure.Parser` knows exactly what fraction of a surface is structured nodes versus opaque text — the ratio is the ratchet's gauge ^c20260712-17u
- promoting a text pattern into the grammar converts a class of soft `Poi.Linter` flags into hard parse-level guarantees ^c20260712-17u
- [CT] promotion is an `Experience.Gated.Decision`: promote a pattern when it keeps generating the same manual POI toil, never speculatively — premature grammar is how the language dies ^c20260712-17u

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

## Experience.Gated.Decision

- [DF] `Experience.Gated.Decision` is a design decision deliberately parked until usage experience accumulates — the question is sound, but answering it now would be a mistake ^c20260711-8u
- the failure it prevents is double: deciding early locks in a guess; leaving the question unnamed loses it ^c20260711-8u
- identification is the work: mark the topic explicitly on a durable surface so the system carries the open question forward without answering it ^c20260711-8u
- the gate opens on evidence — real usage, felt friction, accumulated instances — and the decision is then made from experience, not speculation ^c20260711-8u
- sibling of `Specified.By.Precedence`: both defer authored contracts to accumulated reality; precedence defers the spec, this defers the decision ^c20260711-8u

****

## Index.Ontology

- [DF] `Index.Ontology` is the concept-naming layer of the `Project.Index` — the routed body of `Index.Block`s that names and defines the project's concepts, spanning the `Index.Chapter` folders ^c20260716-8u
- [DC] it is the authoritative name-set: `Index.Appendix` and `Index.Agendix` attach their material to concepts the ontology names ^c20260716-8u
- [DC] fully composed of conceptual blocks under tight `Kernel.Writing` compression, every one routed by `Index.Router`
- [DC] it is the index-level echo of `Kernel.Block.Fundamentals`: the compressed front, depth deferred to `Index.Appendix`
- [DC] with `Index.Appendix`, `Index.Agendix`, and `Index.Router` it composes the `Index.Surface` ^c20260716-9u

### meta

- aliases: `Index.Main`, `Index.Fundamentals`

****

## Index.Surface

- [DF] `Index.Surface` is the file surface of one `Project.Index` — `Index.Router`, `Index.Ontology`, `Index.Appendix`, and `Index.Agendix` taken as a single addressable surface ^c20260716-8u
- [DC] the agendix is part of the surface — its touched, captured, ungated layer ^c20260716-9u
- it is a `Surface.Concept`: the bytes on disk, distinct from `Agentos.Index.System`, which is what those bytes do (the operable `Soft.Programming.Language`)
- it follows the `Index.Surface.Layout` directory protocol; one `Index.Surface` per `Index.Depot`
- it is the outermost layer of the nested index — the index of the project across its surfaces (`Surface.Types`), foremost the `Chat.Surface` where design originates

### meta

- aliases: `Project.Index.Surface`

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
- [DC] the gradient is organization above the `Index.Line` — position in the sequence never changes a line's grounding or authority ^c20260718-15u

****

## Appendix.Default.Block

- `Appendix.Default.Block` is the catch-all block every concept has by default, addressed `Concept.X/Appendix`
- its name is the full path — a child block of the `Concept.X` node, sharing the `Concept.Scoping` container-first notation
- it holds the tail of the concept's `Block.Line.Gradient` — the lines past the index/appendix cut
- it has no space budget — it grows freely, in `Kernel.Writing` style (direct, orthogonal lines)
- it is the landing site for `Writing.Friction.Reduction` capture and `Concept.Explosion` appends — facts filed under a concept without minting a name

****

## Writing.Friction.Reduction

- `Writing.Friction.Reduction` is the principle that the Agentos system lowers the cost of capturing design as it is discussed — by routing capture to the surface whose friction matches it ^c20260705-3u
- friction is a designed gradient, and friction buys stability: `Chat.Surface` (free — talk is capture) → `Index.Agendix` (zero user friction, agent-driven, unstable wording) → `Index.Appendix` (`Kernel.Line`-level approval) → `Index.Ontology` (`Kernel.Block`-level work unit) ^c20260705-2u ^c20260716-10u
- the aim is to capture as much of the user's design as possible before it is lost — structure is deferred, not skipped ^c20260705-3u
- the index keeps a friction floor on purpose — too-cheap writing would flush the hugentic surface; the friction is part of the alignment ^c20260705-3u
- on touched surfaces the approval gate stays — friction drops, the gate does not ^c20260705-3u

****

## Index.Agendix

- `Index.Agendix` is the agent-driven shadow of the Index — the ungated member of the index surface, one file per `Index.Ontology` concept: `agendix/Concept.X-agendix.md`, next to `appendix/` ^c20260705-2u ^c20260716-9u
- it is a cache the agent keeps to aid grounding on stable surfaces — no stable surface may link into it; promotion copies an entry out through the normal gates (including into the index)
- [DC] it carries no reviewed wording, so staleness is benign: a stale agendix is a worse cache, never a corrupted source — consumers verify through the anchors, not the agendix line ^c20260713-3u
- the agent cannot mint routed concepts — it attaches lines and candidate blocks under existing routed concepts; the ontology primes the capture, the agent fills the gaps — the index's shadow, not a second index ^c20260716-0u
- hard rule: every line is a grounded summary of chat discussion — a rejection, a constraint, a highlight the index does not yet capture — carrying its `Anchory.Anchor`/`File.Mention` pointer; unsourced agent reasoning does not belong ^c20260705-2u
- writing rules are the appendix's — `Kernel.Writing` discipline, the same block and line forms; only the supervision differs: all work is done and supervised by agents
- capture is user-triggered but not gated — the agent may suggest a capture pass, never start one
- it extends the `Block.Line.Gradient` past the touch cut: fundamentals → `Concept.X/Appendix` (touched tail) → the concept's agendix shadow tail (untouched) ^c20260705-2u
- homeless material lands in a fallback file — misfit pressure is evidence a concept is missing (concept-gap detector) ^c20260705-2u
- it is index-adjacent, not part of the index — it softens the index principles on the fly, replacing the direct user touch with a grounding link to the touch event
- it is self-similar to the appendix — an untouched appendix, same form and rules; it exists because the user gate is the bottleneck: a surface for the agent to run ahead of the gate
- agendix and appendix must not duplicate content — over time the agendix drains: entries reviewed by the user are promoted through the gate or dropped
- in alignment terms: durable touched-but-ungated space — its lines carry the same turn-grounded authority as any `Index.Line` (`Touched.Authority`), but not the reviewed wording or stable addresses the gate buys; everything in it is promotion evidence ^c20260711-9u ^c20260716-10u
- agendix lines are typed: every line carries a `Line.Type` from the vocabulary — the validation point applies to agent capture too ^c20260707-2u
- [DC] agendix files follow appendix writing rules with the block headed `Concept.X/Agendix`, one file per concept in `agendix/` next to `appendix/`
- [DC] captures with no routed concept land in `agendix/Unassigned-agendix.md` — the homeless pool, promotion evidence for concepts the index does not yet name, never a dump
- [DC] agendix entries may group into blocks — the appendix's block forms apply; a candidate block attaches as a path-child of a routed concept (`Concept.X/Agendix/Candidate.Name`) or pools in `Unassigned` ^c20260716-0u
- [DC] a candidate block's name is provisional — unrouted, zero authority, not citable from stable surfaces; promotion may rename it ^c20260716-0u
- [DC] blocks promote like lines: copied out through the normal gates into index main or appendix ^c20260716-0u
- [CT] the agendix holds touched but ungated material — every line grounded by a user-turn support set, no line landed through a user-gated capture ^c20260716-0u ^c20260716-10u
- [RJ] assistant-grounded capture (`[AS:XX]`, anchoring assistant turns) is excluded — assistant material enters only through the user turn that touched it ^c20260716-0u
- [PR] the agendix is the agentic path of the alignment workflow the gated edit runs hugentically — same primitives (typed `Kernel.Line`s, anchors, the current concept set), the user gate replaced by hard provenance ^c20260708-4u

****

## Capture.Gradient

- [DF] `Capture.Gradient` is the ladder a touched statement climbs across surfaces: chat → agendix → appendix/ontology ^c20260716-11u
- [DC] chat — touched, uncaptured, volatile ^c20260716-10u
- [DC] agendix — touched, captured, ungated: agent-authored wording, not a `Stable.Surface` — nothing may link into it ^c20260716-10u
- [DC] appendix/ontology — touched, captured, gated: wording passed `User.Attention`, a `Stable.Surface` — citable from other surfaces ^c20260716-10u
- [PR] the gate buys stability, not authority: authority is per-line, living in its `Chat.Support.Set` — a thinly grounded gated line can carry less weight than an agendix line grounded on an explicit user statement ^c20260716-11u
- [DC] reading order follows the gradient — ontology and appendix first, agendix later: a prior, not a verdict on any line ^c20260716-11u

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
- every line is precious — it reflects something the user asked for or approved (`Verbatim.User.Gated`), never filler
- lines order along the `Block.Line.Gradient`; block coherence is tight in the fundamentals and relaxes in the appendix
- [DC] `Index.Line` is its grounded specialization — a `Kernel.Line` carrying the `Touched.Surface.Index` grounding invariant ^c20260716-4u

****

## Index.Edit.Action

- `Index.Edit.Action` is the small set of moves that edit the index — each a named action chosen by the case that calls for it
- the moves: `Index.Edit.Create.Block`, `Index.Edit.Append.Line`, `Index.Edit.Modify.Line`, `Index.Edit.Revise.Block`
- two tempos: hot capture (append during the `Alignment.Loop`) and cold consolidation (a maintenance pass over accumulated lines, where `Index.Edit.Create.Block` and `Index.Edit.Revise.Block` mostly live)
- the bias is the lowest-cost action that captures the aligned content (`Writing.Friction.Reduction`)
- every action is user-gated and `Verbatim.User.Gated` — it is the index

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
- it is `Verbatim.User.Gated` — the replacement wording is approved before commit
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
- [CT] grounding reaches chat surfaces only through `agentos chatlas` commands — never provider raw stores or transcript files ^c20260708-0u
- `Index.Linking` is its dual: linking builds and maintains the pointers grounding follows

****

## Index.Linking

- `Index.Linking` is constructing and maintaining the index's pointers back to the surfaces it indexes — support on the `Chat.Surface` (or code, or files) for index blocks and lines
- without the links back, the index cannot be checked for completeness or correctness against the touched record
- it lands in the block's grounding section (`Concept.X/Grounding`), carried as grounding lines — an `Anchory.Anchor` plus a one-sentence note
- it is an index edit — user-gated like any edit (`Edition.Trigger.User.Gated`, `Verbatim.User.Gated`); in the `Agendix` linking runs open, agent-driven (dealt with later)
- [CT] linking accesses chat data only through `agentos chatlas` commands — never provider raw stores or transcript files ^c20260708-0u
- it is the dual of `Context.Grounding`: linking builds the pointers, grounding follows them

- [DC] linking mostly happens on the edge — anchoring content produced in the current session; self-session discovery by content matching is the entry step ^c20260708-1u
****

## Index.Enrichment

- [DF] `Index.Enrichment` is the hugentic drive to always increase the `Touched.Surface` of any block or line — no block is finished ^c20260709-7u
- [DC] grounding and enrichment split by evidence source: grounding is retrospective, mining the existing chat corpus; enrichment is generative, producing new touched surface ^c20260709-8u
- the discussion is the yield: spawning a focused discussion about a block creates the user turns that become its new grounding surface — and, through the gate, possibly new content ^c20260709-7u
- [DC] `Grounding.Density` reads as pipeline position: zero → mine the corpus first (grounding); low → generate (enrichment); high → rest until touched again ^c20260709-8u
- enrichment is block-scoped and gated — a micro design-session one block wide; the block's density delta is the receipt ^c20260709-9u
****

## Git.Dating

- [DF] `Git.Dating` is dating a file or file line by finding its last change in the git history ^c20260709-10u
- the date turns a static artifact into a searchable event: it says where in time to look further about the target — for instance in the chat corpus ^c20260709-10u
- [DC] the commit dates the write; the originating evidence is earlier — search around and before the commit time, not at it ^c20260709-11u
- `git log -L` follows a line's wording past mechanical commits to the content-bearing ones ^c20260709-11u
- it is the entry step of backward grounding: git dates the wording, chatlas finds the session and turns ^c20260709-11u
****

## Anchory.System

- `Anchory.System` is the Agentos subsystem for stable symbolic links to contexts on other surfaces
- `Anchory.Anchor` carries compact identity while `Anchory.Register` carries resolution data
- `Anchory.Namespace` partitions anchor keys into independent resolution domains
- Anchory is Agentos-wide rather than project-local ^c20260706-1u
- Anchory is library-first so other subsystems can integrate directly
- integrating subsystems own payload meaning and final traversal to referenced surfaces
- `agentos anchory ...` is a thin CLI over the library contract
- referenced surfaces remain authoritative; Anchory is plumbing, not truth
- keys are composed: the caller supplies meaning (namespace, alloc-prefix, tag), Anchory supplies identity — the counter ^c20260718-3
- each `Anchory.Namespace` declares its one-letter key prefix and intention in `meta.json` — the resolution fallback context ^c20260718-3
- a depot registry with `Pwd.Upward.Search` resolves any anchor without prior depot knowledge; every touched depot auto-registers ^c20260718-3

### meta

- namespace-members: `./Anchory.Anchor`, `./Anchory.Namespace`, `./Anchory.Register`, `./Anchory.Record`, `./Anchory.Depot`, `./Integration`, `./Chat.Application`, `./Open.Design`
****

## Capture.Offer

- [DF] `Capture.Offer` is the practice of proposing an index capture at the moment the content is born — the exact typed line or block, verbatim, user-gated ^c20260718-1u ^c20260718-2u
- [PR] capture is cheapest at the moment for both sides: the agent's context is hot and the anchor mintable on the spot; the user's judgment is hot too — reviewing now beats reconstructing later
- [DC] an offer presents destination options: ontology, appendix, agendix, or decline — the user picks the landing with the gate ^c20260718-0u
- [DC] an offer arrives landing-ready: proposed type carried, target scouted for each destination it offers
- [DC] it is the hugentic sibling of agendix capture — same trigger instinct, the user gate in place of hard provenance
- [DC] offers ride any workflow — impl execution, design, review; declining is cheap and normal, the offer must never block the work
- [DC] destinations generalize with the `Touched.Surface.Index`: an offer may target any member within reach — the project index's landings, a chat's agendix, an annotation's touched lines ^c20260718-0u
- [DC] it holds block form because it must stay referenceable: downstream surfaces declare dependence on the name, and only blocks are addressable to the resolver ^c20260718-2u

****

## Touched.Surface.Index

- [DF] `Touched.Surface.Index` is the general category of surfaces composed of `Index.Line`s — statements grounded to a `Chat.Support.Set` of user turns ^c20260716-1u
- [CT] membership is the grounding invariant: every line carries at least one anchor resolving to its `Chat.Support.Set` — nothing else is required of a member ^c20260716-1u
- [DC] the `Chat.Surface` user turn is the first and unique source of user authority; every member surface roots there ^c20260716-1u
- [DC] "index" is earned by construction: every line finally points down to its chat support — a member is a cache over the chats, never authority; consumers verify through the support turns ^c20260716-1u
- [FR] the nature of the annotation varies by application: a line may restate the turn content, or contextualize why the support turns support what is being annotated ^c20260716-1u
- [DC] member surfaces differ by design axes on top of the invariant: attachment point, gating, format, ordering ^c20260716-1u
- [EX] the `Agentos.Index` is the first member — lines attached to concepts; `Chat.Agendix` attaches them to chats; `Skw.Agendix` to any `Skw.Annotation` ^c20260716-1u

****

## Touched.Support.Network

- [DF] `Touched.Support.Network` is the network relating anchored statements across all touched surfaces to their chat evidence — edges of the form `Support.Set` ↔ `Anchor.Metadata` ↔ `Anchored.Line` ^c20260716-21u ^c20260716-23u
- [DC] two surfaces meet at the edge: the `Chat.Surface` holds the turns, the anchored surface holds the line; the anchory between them can carry metadata ^c20260716-22u
- [DC] `Anchored.Line` is the general node: an `Index.Line` is one case — agendix, archive, and annotation lines ride the same edge shape ^c20260716-21u
- [DC] metadata is free at this level: optional and implementation-defined — hint, explanation, whatever the integration needs; the bare edge `Support.Set` ↔ `Anchored.Line` is valid, the line itself explaining the relationship ^c20260716-21u ^c20260716-22u
- [DC] it is a dynamic system: nodes and edges are created and eliminated as both sides evolve — the index is a view over the `Chat.Surface` contextualized by its current semantics ^c20260716-19u
- [DC] the surface holds the live cut — utility for the current model; git holds the network's history; the `Chat.Surface` holds the invariant turns ^c20260716-19u
- [DC] a turn's grounding history is traced by following the edit history of the anchors and the index — no history log on the surface ^c20260716-20u
- [DC] reinterpretation mints a new anchor rather than amending — new meaning is a new anchor, generalizing the wrong-date doctrine ^c20260716-19u
- [PR] `Chat.Support.Set` is the local view: one node's edge bundle; the network is the global object the sets compose ^c20260716-20u

### meta

- aliases: `Index.Support.Network`

****

## Demoted.Anchored.Line

- [DF] a `Demoted.Anchored.Line` is a demoted network edge: the anchored line, with its `Support.Set` and `Anchor.Metadata`, existed in some version of `Touched.Support.Network` and exists in none now — the relation demotes as one ^c20260716-30u ^c20260716-31u
- [DF] an `Index.Demoted.Turn` is a turn with no live edge left ^c20260716-27u ^c20260716-30u
- [CT] distinct from unindexed: past edges are the witness ^c20260716-26u ^c20260716-27u
- [DC] demotion is evidence-based and computed: git holds every surface version — presence in history, absence in the live cut; no surface is constrained by it and none is required for it ^c20260716-28u ^c20260716-29u
- [DC] the nature of a demotion is unknown by design: the edge existed and now it does not — no stored account; a turn rejoins by a fresh edge ^c20260716-25u ^c20260716-27u
- [RJ] archive surfaces, frozen drift lines, maintained drift explanations as demotion machinery — git and the chat already hold the full context ^c20260716-25u ^c20260716-27u

****

## Index.Line

- [DF] `Index.Line` is the atom of the `Touched.Surface.Index`: one statement, grounded to a `Chat.Support.Set` by its trailing anchor ^c20260716-4u
- [CT] one line, one fact — atomic and reorderable, surviving on its own (`Kernel.Writing` granularity) ^c20260716-4u
- [DC] the line is the unit of grounding, approval, and audit: gates, linters, and drift checks run per line ^c20260716-4u
- [DC] a line with its anchor in place is a `Grounded.Line`; one still missing it is an `Ungrounded.Line` — a legacy backlog, not a licensed state ^c20260716-33u ^c20260717-0u
- [DC] lines carry a `Line.Type` classifying their act ^c20260716-4u
- [EX] on a `Verbatim.User.Gated` surface, each line's support set holds a `Turn.Type::Project.Index.Gate` turn ^c20260716-4u ^c20260716-10u
- [PR] everything above the line is organization — blocks, surfaces, attachment points; everything below it is evidence — anchors, support sets, turns ^c20260716-4u

****

## User.Attention

- [DF] `User.Attention` is the scarce resource of the hugentic system: what the user can actually read, judge, and approve ^c20260716-6u
- [PR] the system economizes it deliberately — surfaces are designed by how much of it they spend ^c20260716-6u
- [DC] `Verbatim.User.Gated` spends it on purpose — that spend is what buys stability; the `Index.Agendix` scales precisely because it spends none ^c20260716-6u ^c20260716-10u
- [DC] analogous to attention in LLMs: the limited context the human can condition on — "we must make Y pass through the `User.Attention`" ^c20260716-6u
- [EX] spend it on the `Project.Index`; offload everything else to agent-driven surfaces ^c20260716-6u

****

## Skw.Touched.Index

- [DF] `Skw.Touched.Index` is the `Touched.Surface.Index` member attached to `Skw.Annotation`s: `Index.Line`s riding annotations on generated surfaces — file, module, region, construct ^c20260717-7u ^c20260717-10u
- [DC] one mixed surface: gated and ungated lines share the place — a line is gated iff its support set holds the gate-typed turn (`Turn.Type::<Surface>.Gate`); the split is computed, not geographic ^c20260717-6u ^c20260717-7u
- [DF] `Skw.Appendix` and `Skw.Agendix` are its computed strata — the gated and the ungated lines: the appendix and agendix of a block, where the block is the annotation — same mechanics, no file split ^c20260717-9u
- [DC] promotion is a state change, not a relocation: a line passes the gate where it stands — the gate turn joins its set; nothing moves ^c20260717-6u ^c20260717-10u
- [DC] two worlds meet at the annotation: the skw development stack reads it to generate, judge, and evolve the surface; the touched lines ground to the `Chat.Surface` — the user-grounded part of that context ^c20260717-8u
- [DC] syntax: `--supp <line> ^<anchor>` — the construct's own touched lines: the annotation is its own block, deps (`--from`/`--quote`) bind its content while supps ground the annotation itself ^c20260719-0u

****

## Skw.Network

- [DF] `Skw.Network` is the graph of annotated surfaces linked by the relationships the skw system defines between them ^c20260715-6u
- [DC] relationships are explicit or implicit: explicit ones are the declared links a `Skw.Dependency` carries; implicit ones are derived by the system, such as support-set intersection between chat anchors ^c20260715-6u
- [DC] the network is computed from consumer-side declarations — a target never registers its dependents; followers are derived, so an imported surface stays ignorant of its importers ^c20260715-6u
- [PR] the network's job is notification, not judgment: when a surface changes, the `CPU.Program` notifies every surface the network links to it — a purely mechanical fan-out along the edges ^c20260715-6u
- [DC] an `Agentic.Program` interprets each notification: whether the change is benign or a real change to propagate is a semantic verdict only the agent carries ^c20260715-6u
