> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Agentos.Skillware

- `Agentos.Skillware` is the discipline of treating skills as software — the skill is the unit of software for agents.
- "as software" means the artifacts agents run gain engineering structure — modules, dependencies, builds, versions, lineage — so they can be reused and evolved rather than written once and forked.
- it is supported by a development toolchain — linters, builders, compilers — spanning agentic and `CPU.Impl` work, that moves package maintenance off the human. ^20260627-0
- a discipline realized by capabilities, not a single mechanism — it names the stance; specific members implement it.
- **skw** is the system realizing the discipline: the general annotation language (`Skw.Language`) and its `Skw.Backend`s ^20260711-9

### meta

- `Explicit.Namespace`; members: `Skill.Module`, `Skill.Runnable.Surface`, `Skill.Build.Surface`, `Skill.Package.Builder`, `Derivation.Rule`, `Derived.Content`, `Module.Import`, `Import.Management`, `Derived.Module`, `Skillware.Construct`, `Skillware.Recipe`, `Skw.Language`, `Skw.Backend`, `Surface.Annotation`, `Annotation.Point`, `Annotation.Authority`, `Drift.POI`, `Semantic.Router`, `Usage.Pattern.Routing`.

****

## Skill.Runnable.Surface

- `Skill.Runnable.Surface` is a surface whose purpose is to be run — loaded into agent context to do work; it carries only the executable substance.
- the system keeps it free of non-runnable artifacts, so nothing obscures or dilutes what runs — a building-backend discipline; annotated-only `Skw.Backend`s trade it for constraint co-location. ^20260627-2 ^20260711-9
- forced by context being executable — anything on it is read into context and shapes the run; non-runnable artifacts there are not inert, they interfere.

****

## Skill.Build.Surface

- `Skill.Build.Surface` is the complement of `Skill.Runnable.Surface` — it holds the artifacts that produce and maintain runnable content, and is never loaded at run time. ^20260627-1
- it is the home for everything kept off the runnable surface: derivation context, dependency declarations, lineage, dev material. ^20260627-1
- never run, it carries no "stay clean" constraint — an unconstrained workspace; that freedom is what the two-surface split buys.
- realized as the per-package `.skillware/` folder — `src/` mirror, settings, lock — organized by capability, discovered by convention. ^20260710-2

****

## Skill.Package.Builder

- `Skill.Package.Builder` is the support system for developing and maintaining a skill package's `Skill.Runnable.Surface`
- it is a bundle of agentic skills and CLI support tooling that run build workflows over the package
- a build workflow either produces runnable content or checks it — builds, drift-checks, tests, lint
- it is open-ended — any build workflow can be added; derivation is one capability, not the whole system
- the `Skill.Build.Surface` is its workspace — it holds anything the builder needs that should not live on the `Skill.Runnable.Surface`
- realized as the `agentos-skillware` `Package.Aux.Skill`, which centralizes all Skillware `Skill.Module`s — build toolchain, language, authoring, doctrine ^20260710-2

****

## Module.Import

- [DF] `Module.Import` is a declared dependency between surfaces — a consumer surface imports a target named by any legal `Skw.Address.Schema` name ^20260709-12 ^20260712-10
- [DC] three binding modes: `pointer` — resolved at load time, always fresh; `copy` — verbatim materialization at build time; `derived` — a semantic transformation materialized at build time, governed by a `Derivation.Rule` ^20260709-14
- [DC] the binding is the consumer's declaration — the imported surface never knows its importers ^20260709-12
- [DC] on building `Skw.Backend`s, declarations live on the `Skill.Build.Surface` and the `Skill.Runnable.Surface` carries only the materialized result; annotated-only backends keep declarations in place on the surface itself ^20260709-13 ^20260711-9
- each binding carries a checkable claim: pointer — the target resolves at its address; copy — equality with the target; derived — the rule still holds ^20260709-16
- [DC] a failed check is a drift finding with no predefined winner — resolution is case-by-case; a particular workflow may set auto-regeneration as its own rule ^20260709-15
- it is the Skillware linking system: copy and derived are static binding, pointer is dynamic ^20260709-12
- [DC] v1 realization: declarations are `[!skw]` recipe callouts inline in src (`.skw.md`); the toolchain materializes `copy` and `derived` — `pointer` remains routed prose, not yet toolchain-checked ^20260710-2

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
- targets are addressed by `Skw.Address.Schema` names — `Dotted.Name`s for blocks, `Locator.Name`s for files, regions, and spans, `Anchory.Anchor`s for chat moments ^20260712-10
- [PR] division of labor: the CPU materializes copy bindings and detects drift; the agent performs derivations — and performs them in src, where the `Derivation.Rule` and its current solution live side by side ^20260710-0
- [DC] v1 realization: `lock.json` holds the per-import record; check verdicts (`copy-drift`, `derived-stale`, `hand-edited`) surface drift — and a rebuild can never silently clear `derived-stale`; only an actual re-derive does ^20260710-2

****

## Derived.Module

- `Derived.Module` is a `Skill.Module` whose content is mostly `Derived.Content` — the high-derivation pole.
- source-agnostic — its sources may be index blocks or other modules; derived-ness is the ratio, not the surface.
- the more derived it is, the more its maintenance automates — largely a projection of its sources, re-derived on change, with human work only at the seam with original content.

****

## Skillware.Construct

- [DF] `Skillware.Construct` is the single syntactic form of the skw language: a `$kw:` declaration line — a CLI-style command, `<command> [^label] [--flag value …]` — with `$kw.` continuation lines, a flat native body, and a mandatory owned closer `$kw. end-<command>` ^20260710-4 ^20260712-7
- [DC] the sigil pair splits open from belong: `$kw:` opens a construct (or declares a divider); `$kw.` marks everything belonging to the open construct — further flags, value continuations, and the closer ^20260712-7
- [DC] every machinery line carries the sigil — uniform marking, so nothing skw is ever inferred from bare host syntax; the sigil rides the host's carrier (blockquote in markdown, comments in code), making the form carrier-neutral ^20260712-7
- [DC] closure is fully explicit for body-bearing constructs: a bare `end` is invalid; a multi-close line (`end-a end-b`) unwinds the open stack innermost-first; a heading closes nothing — a construct left open at a heading or EOF is a finding ^20260710-4 ^20260711-9
- [DC] closure is declared, never positional: beyond owned ends, the registry may grant a command peer-closure — opening it closes its open peers (`when` closes `when`/`then`; a leveled `section` closes sections of level ≥ its own) — and a parent's end closes its open scoped children (`end-router` closes an open row); every closure still happens at a marked machinery line, and headings/EOF still close nothing ^20260713-0
- [CT] peer-closure is only for vocabularies where the next declaration IS the boundary by construction (rows, sections); body-bearing primitives (`text`, `copy`, `derived`) keep mandatory owned ends — nothing can infer where an arbitrary body stops ^20260713-0
- end-free annotation sections are this mechanism, not an exception: a divider is a peer-closing command, so explicit closure survives intact ^20260713-0
- [DC] no indentation: bodies sit at column 0 — nesting is logical (the parse stack + owned ends), never visual; the body is runnable prose first ^20260710-4
- [DC] three primitives instantiate it anywhere in a src: `text` (a literal, tag optional), `copy`, and `derived` — a generation function whose declaration describes the generated body and whose body is the current output ^20260710-4
- the command vocabulary is the language's growth axis: new capability is a new command over the same construct — structural commands (`router`, `when`, `then`) compose primitives ^20260710-4
- [DC] arg flags are trait annotations, orthogonal to the command list: a command gives core semantics, annotations layer constraints on the body (`--from` inbound dependency, `--intent` derivation rule, `--to` the prose explicitly sends the agent to another surface — carriable by any construct) ^20260711-0 ^20260712-7
- [PR] every annotation is a checkable constraint: the CPU checks its decidable face (resolution, structure, hashes); agents check its semantic face (does the body honor the declaration) — annotations are to prose what types are to code ^20260711-0
- [DC] trait semantics are reserved by JSONPath-style paths: `*.key` reserves the key's meaning on every command, `command.key` scopes it to one; validation is registry-driven, and a scoped semantic that generalizes is promoted up the path ^20260711-0
- [DC] any declaration may carry a `^label` token — identity riding the construct (`*.label` spelled inline); `label ^x` is the explicit command for a labeled literal (no command-less declarations); owned ends accept either owner, `end-<command>` or `end-^label`, the label matching exactly ^20260711-1 ^20260712-7
- [DC] labels extend the address grammar — `@path^label` (labeled span; the `@` agent-maintained), `^label` (file-local); a `--from` on a labeled span hashes only that span, so drift is heading-independent and fine-grained ^20260711-1 ^20260712-10
- [DC] labels are src-only machinery, stripped at compile — distinct from `Anchory.Anchor`s (global evidence links that survive in the text); renaming a label breaks importers, caught by the dead-link check ^20260711-1

****

## Skillware.Recipe

- [DF] `Skillware.Recipe` is the inline declaration form of a `Module.Import`: a `$kw:` declaration in a `.skw.md` src, carrying the verb (binding), `--from` targets, and `--intent` (the `Derivation.Rule` context), with the produced body directly below ^20260710-2 ^20260712-7
- the recipe and its current solution live side by side in src — declaration, rule, and result in one place ^20260710-2
- compile is deterministic: the toolchain strips the callout machinery; the runnable surface carries only the produced content ^20260710-2
- [RJ] `Import.Manifest` — a separate flat artifact per consuming module (`build/<...>-imports.md`) — was superseded before implementation: declarations live inline; `lock.json` is the machine record ^20260709-13 ^20260710-2
- [DC] recast by `Skillware.Construct`: the recipe is the section-scoped v1 instance of the general declaration+body form; v2 makes the construct position-free with enforced owned ends ^20260710-4

****

## Skw.Language

- [DF] skw is an embedded annotation language for the generation of surfaces — an annotation states how a span of content is produced: from which dependencies, under which rule ^20260711-2
- the annotation constrains the span: the content must not contradict or drift from its declaration — every annotation is a checkable claim ^20260711-2
- everything frames as generation: a copy is deterministic generation (the inlining of a source, itself possibly generated); a derived span is agentic generation under its rule; a literal carries no generation claim; a link's text is a typed generated span, annotated independently of the target it points at ^20260711-2
- it annotates any content, but earns most on agent-generated surfaces — where the rule and its current solution living side by side is what makes maintenance checkable ^20260711-2
- it is embedded — skw lives inside the host surface's own format, next to the content it governs, and never replaces it ^20260711-2
- the language is surface-blind; a `Skw.Backend` binds it to each surface class ^20260711-2

****

## Skw.Backend

- [DF] a `Skw.Backend` binds `Skw.Language` to one surface class, named `skw-<surface>` ^20260711-3
- a backend owns four things: the carrier syntax, the build semantics (if any), where check state lives, and its host-native `Annotation.Point` vocabulary ^20260711-3
- every backend is annotated; some backends additionally build — annotation + check is the universal layer, build is backend-local ^20260711-3
- a building backend generates its runnable form from annotated src and strips the machinery; an annotated-only backend keeps declarations in place on the surface itself, trading surface cleanliness for constraint co-location ^20260711-3
- **skw-skills** is the first backend, a building one: annotated src compiles to the skill's runnable files ^20260711-3
- **skw-code** is the first annotated-only candidate: declarations ride the host language's comments; the body is the live fragment ^20260711-3

****

## Surface.Annotation

- [DF] a `Surface.Annotation` is the skw content of a file — the machinery that states extra things *about* the surface it annotates, next to the content it governs ^20260711-4
- it is a deliberate subset: the fragment's fundamentals, never an exhaustive dependency capture ^20260711-4
- it answers one question: *what context can't I miss to understand this fragment?* ^20260711-4
- it is a satellite index of the design — a leaf citing the canonical index by `Dotted.Name`; the hub stays the center ^20260711-4
- it is a local grounding recipe: an agent landing on the fragment loads the declared dependencies and holds the minimal sufficient context by declaration, not by search ^20260711-4

****

## Annotation.Point

- [DF] an `Annotation.Point` is a named, sanctioned place where annotations attach — a small vocabulary of points so agents do not over-annotate arbitrary fragments ^20260711-5
- points come in two families: **host-native** — the natural divisions of the annotated surface — and **skw-native** — the language's own scoping constructs, layered on top ^20260711-5
- [PR] prefer the host's natural divisions; reach for skw-native scoping only where the host's divisions do not fit the annotation's true scope ^20260711-5
- the file is the universal host point; each backend declares the rest of its host vocabulary — functions, modules, namespaces for code; sections for markdown ^20260711-5
- the skw-native points: the **annotation section** (a leveled, end-free divider sectioning a file for annotation purposes only) and the **span** (an explicit construct body — the finest grain) ^20260711-5
- the agent attaches at the coarsest point that honestly fits ^20260711-5

****

## Annotation.Authority

- [DF] `Annotation.Authority` is the authority model of annotations: authority flows from grounding, not from the writer ^20260711-6
- annotation lines take the index's own forms: `Line.Type` codes and `Anchory.Anchor`s, with the same validation points ^20260711-6
- authority follows `Touched.Authority`: untouched annotation lines are hypotheses bound by the grounded span; grounded ones hold second-order authority; gated ones are first-order touched ^20260711-6
- what stays restricted below the gate is linkability, not worth — the `Touched.Authority` fence ^20260711-6
- no status is stored: drift is discovered and surfaced by the checker; authority is read from the lines' provenance ^20260711-6
- [CT] agent-free insertion is regulated: only the file `Annotation.Point` is open to ungated agentic annotation — every finer point lands user-gated ^20260711-6
- finer annotations are therefore born touched: the gating turn is their grounding evidence ^20260711-6

****

## Drift.POI

- [DF] a `Drift.POI` is a point of interest raised by the CPU checker: a span's declared dependencies changed — that, and nothing more ^20260711-7
- the CPU never rules on drift: whether the surface actually drifted is an agent's finding — the agent is always the fixer and supervisor ^20260711-7
- a POI carries its trigger — which dependency, what changed — so the responding agent starts contextualized ^20260711-7
- resolution is agentic: real drift → re-derive the span; benign change → re-bless the dependencies ^20260711-7

****

## Closure.Parser

- [DF] a `Closure.Parser` demands a minimal structure — the `Parse.Floor` — and is closed above it: a surface below the floor is a hard parse error; a surface at the floor always yields a full AST, and no finer detail can fail the parse ^20260712-17
- from the `Parse.Floor` up, the parser cares only about what it recognizes: recognized regions become structured nodes, everything else becomes text nodes, and no further errors exist ^20260712-17
- above the floor, an unrecognized region is simply an opaque text node — the parser does not judge it; whatever might be wrong inside is a linter concern, not a parse concern ^20260712-17
- the parser emits exactly one kind of failure: parse errors, only below the floor — it emits no POIs ^20260712-17
- [PR] one broken construct never blinds the system to the whole file ^20260712-17
- [CT] closed also means lossless: above the floor, every byte of the input lands in some node ^20260712-17
- [DC] realized: the skw parser is `Closure.Parser::Skw` — its floor is well-formed, explicitly closed `$kw` machinery; above it, construct nodes and opaque text ^20260712-17

****

## Poi.Linter

- [DF] a `Poi.Linter` lints the AST of a `Closure.Parser`, never the native text — every lint rule is a rule about node types, not text patterns ^20260712-17
- [CT] the no-shadow-parser constraint: a rule targets node types and may read inside a text node, but re-parsing the surface around the AST is forbidden ^20260712-17
- checks are layered: parse errors gate everything — below the `Parse.Floor` the linter reports the parse errors as POIs and advances no further ^20260712-17
- its output is the POI stream: each POI marks a place worth an agent's attention, and nothing more — it may carry a suggested resolution, but it asserts no verdict; the agent inspects and decides ^20260712-17
- [PR] the softness is bought, not accidental: a linter that is always right costs a robust parser — the system stays cheap and simple by tolerating wrong and missed flags, and agents are told so ^20260712-17
- opaque text nodes are its territory: what the parser deliberately ignores, linter rules may inspect and flag ^20260712-17
- [DC] realized: `agentos skillware check` — parse errors gate per file, POIs carry stable identity hashes, output is a once-per-kind legend plus bare rows ^20260712-17

****

## Poi.Bless

- [DF] `Poi.Bless` is the explicit act of accepting a POI's current state as correct: an auditable command rewrites the POI's recorded expectation to match reality, and the flag clears without the surface being touched ^20260712-17
- [PR] blessing is loud: drift never clears as a side effect of rebuilds or unrelated edits — only a re-derivation of the content or an explicit bless (the no-silent-blessing rule generalized) ^20260712-17
- [CT] not every POI is blessable: parse errors are never blessable — a surface below the `Parse.Floor` is not in the language and must be fixed; blessability belongs to semantic POIs, where the current state might genuinely be the truth ^20260712-17
- [DC] realized: `agentos skillware bless --poi <hash>` — rewrites the recipe's locked dependency hashes to current, body untouched; only `derived-stale` accepts it ^20260712-17

****

## Structure.Ratchet

- [DF] the `Structure.Ratchet` is the system's direction of travel: over time, content moves from opaque text nodes into recognized structure — the target state is a fully structured surface where all remaining prose is ACTUAL prose: no parsable objects remain in the text ^20260712-17
- progress is measurable: the `Closure.Parser` knows exactly what fraction of a surface is structured nodes versus opaque text — the ratio is the ratchet's gauge ^20260712-17
- promoting a text pattern into the grammar converts a class of soft `Poi.Linter` flags into hard parse-level guarantees ^20260712-17
- [CT] promotion is an `Experience.Gated.Decision`: promote a pattern when it keeps generating the same manual POI toil, never speculatively — premature grammar is how the language dies ^20260712-17

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

- [DF] `Experience.Gated.Decision` is a design decision deliberately parked until usage experience accumulates — the question is sound, but answering it now would be a mistake ^20260711-8
- the failure it prevents is double: deciding early locks in a guess; leaving the question unnamed loses it ^20260711-8
- identification is the work: mark the topic explicitly on a durable surface so the system carries the open question forward without answering it ^20260711-8
- the gate opens on evidence — real usage, felt friction, accumulated instances — and the decision is then made from experience, not speculation ^20260711-8
- sibling of `Specified.By.Precedence`: both defer authored contracts to accumulated reality; precedence defers the spec, this defers the decision ^20260711-8

****

## Index.Ontology

- [DF] `Index.Ontology` is the concept-naming layer of the `Project.Index` — the routed body of `Index.Block`s that names and defines the project's concepts, spanning the `Index.Chapter` folders ^20260716-8
- [DC] it is the authoritative name-set: `Index.Appendix` and `Index.Agendix` attach their material to concepts the ontology names ^20260716-8
- [DC] fully composed of conceptual blocks under tight `Kernel.Writing` compression, every one routed by `Index.Router`
- [DC] it is the index-level echo of `Kernel.Block.Fundamentals`: the compressed front, depth deferred to `Index.Appendix`
- [DC] with `Index.Appendix`, `Index.Agendix`, and `Index.Router` it composes the `Index.Surface` ^20260716-9

### meta

- aliases: `Index.Main`, `Index.Fundamentals`

****

## Index.Surface

- [DF] `Index.Surface` is the file surface of one `Project.Index` — `Index.Router`, `Index.Ontology`, `Index.Appendix`, and `Index.Agendix` taken as a single addressable surface ^20260716-8
- [DC] the agendix is part of the surface — its touched, captured, ungated layer ^20260716-9
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
- friction is a designed gradient, and friction buys stability: `Chat.Surface` (free — talk is capture) → `Index.Agendix` (zero user friction, agent-driven, unstable wording) → `Index.Appendix` (`Kernel.Line`-level approval) → `Index.Ontology` (`Kernel.Block`-level work unit) ^20260705-2 ^20260716-10
- the aim is to capture as much of the user's design as possible before it is lost — structure is deferred, not skipped ^20260705-3
- the index keeps a friction floor on purpose — too-cheap writing would flush the hugentic surface; the friction is part of the alignment ^20260705-3
- on touched surfaces the approval gate stays — friction drops, the gate does not ^20260705-3

****

## Index.Agendix

- `Index.Agendix` is the agent-driven shadow of the Index — the ungated member of the index surface, one file per `Index.Ontology` concept: `agendix/Concept.X-agendix.md`, next to `appendix/` ^20260705-2 ^20260716-9
- it is a cache the agent keeps to aid grounding on stable surfaces — no stable surface may link into it; promotion copies an entry out through the normal gates (including into the index)
- [DC] it carries no reviewed wording, so staleness is benign: a stale agendix is a worse cache, never a corrupted source — consumers verify through the anchors, not the agendix line ^20260713-3
- the agent cannot mint routed concepts — it attaches lines and candidate blocks under existing routed concepts; the ontology primes the capture, the agent fills the gaps — the index's shadow, not a second index ^20260716-0
- hard rule: every line is a grounded summary of chat discussion — a rejection, a constraint, a highlight the index does not yet capture — carrying its `Anchory.Anchor`/`File.Mention` pointer; unsourced agent reasoning does not belong ^20260705-2
- writing rules are the appendix's — `Kernel.Writing` discipline, the same block and line forms; only the supervision differs: all work is done and supervised by agents
- capture is user-triggered but not gated — the agent may suggest a capture pass, never start one
- it extends the `Block.Line.Gradient` past the touch cut: fundamentals → `Concept.X/Appendix` (touched tail) → the concept's agendix shadow tail (untouched) ^20260705-2
- homeless material lands in a fallback file — misfit pressure is evidence a concept is missing (concept-gap detector) ^20260705-2
- it is index-adjacent, not part of the index — it softens the index principles on the fly, replacing the direct user touch with a grounding link to the touch event
- it is self-similar to the appendix — an untouched appendix, same form and rules; it exists because the user gate is the bottleneck: a surface for the agent to run ahead of the gate
- agendix and appendix must not duplicate content — over time the agendix drains: entries reviewed by the user are promoted through the gate or dropped
- in alignment terms: durable touched-but-ungated space — its lines carry the same turn-grounded authority as any `Index.Line` (`Touched.Authority`), but not the reviewed wording or stable addresses the gate buys; everything in it is promotion evidence ^20260711-9 ^20260716-10
- agendix lines are typed: every line carries a `Line.Type` from the vocabulary — the validation point applies to agent capture too ^20260707-2
- [DC] agendix files follow appendix writing rules with the block headed `Concept.X/Agendix`, one file per concept in `agendix/` next to `appendix/`
- [DC] captures with no routed concept land in `agendix/Unassigned-agendix.md` — the homeless pool, promotion evidence for concepts the index does not yet name, never a dump
- [DC] agendix entries may group into blocks — the appendix's block forms apply; a candidate block attaches as a path-child of a routed concept (`Concept.X/Agendix/Candidate.Name`) or pools in `Unassigned` ^20260716-0
- [DC] a candidate block's name is provisional — unrouted, zero authority, not citable from stable surfaces; promotion may rename it ^20260716-0
- [DC] blocks promote like lines: copied out through the normal gates into index main or appendix ^20260716-0
- [CT] the agendix holds touched but ungated material — every line grounded by a user-turn support set, no line landed through a user-gated capture ^20260716-0 ^20260716-10
- [RJ] assistant-grounded capture (`[AS:XX]`, anchoring assistant turns) is excluded — assistant material enters only through the user turn that touched it ^20260716-0
- [PR] the agendix is the agentic path of the alignment workflow the gated edit runs hugentically — same primitives (typed `Kernel.Line`s, anchors, the current concept set), the user gate replaced by hard provenance ^20260708-4

****

## Capture.Gradient

- [DF] `Capture.Gradient` is the ladder a touched statement climbs across surfaces: chat → agendix → appendix/ontology ^20260716-11
- [DC] chat — touched, uncaptured, volatile ^20260716-10
- [DC] agendix — touched, captured, ungated: agent-authored wording, not a `Stable.Surface` — nothing may link into it ^20260716-10
- [DC] appendix/ontology — touched, captured, gated: wording passed `User.Attention`, a `Stable.Surface` — citable from other surfaces ^20260716-10
- [PR] the gate buys stability, not authority: authority is per-line, living in its `Chat.Support.Set` — a thinly grounded gated line can carry less weight than an agendix line grounded on an explicit user statement ^20260716-11
- [DC] reading order follows the gradient — ontology and appendix first, agendix later: a prior, not a verdict on any line ^20260716-11

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
- [DC] `Index.Line` is its grounded specialization — a `Kernel.Line` carrying the `Touched.Surface.Index` grounding invariant ^20260716-4

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
- [CT] grounding reaches chat surfaces only through `agentos chatlas` commands — never provider raw stores or transcript files ^20260708-0
- `Index.Linking` is its dual: linking builds and maintains the pointers grounding follows

****

## Index.Linking

- `Index.Linking` is constructing and maintaining the index's pointers back to the surfaces it indexes — support on the `Chat.Surface` (or code, or files) for index blocks and lines
- without the links back, the index cannot be checked for completeness or correctness against the touched record
- it lands in the block's grounding section (`Concept.X/Grounding`), carried as grounding lines — an `Anchory.Anchor` plus a one-sentence note
- it is an index edit — user-gated like any edit (`Edition.Trigger.User.Gated`, `Verbatim.User.Gated`); in the `Agendix` linking runs open, agent-driven (dealt with later)
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
- [DC] an offer presents destination options: ontology, appendix, agendix, or decline — the user picks the landing with the gate ^20260718-0
- [DC] an offer arrives landing-ready: proposed type carried, target scouted for each destination it offers
- [DC] it is the hugentic sibling of agendix capture — same trigger instinct, the user gate in place of hard provenance
- [DC] offers ride any workflow — impl execution, design, review; declining is cheap and normal, the offer must never block the work
- [DC] destinations generalize with the `Touched.Surface.Index`: an offer may target any member within reach — the project index's landings, a chat's agendix, an annotation's touched lines ^20260718-0

****

## Touched.Surface.Index

- [DF] `Touched.Surface.Index` is the general category of surfaces composed of `Index.Line`s — statements grounded to a `Chat.Support.Set` of user turns ^20260716-1
- [CT] membership is the grounding invariant: every line carries at least one anchor resolving to its `Chat.Support.Set` — nothing else is required of a member ^20260716-1
- [DC] the `Chat.Surface` user turn is the first and unique source of user authority; every member surface roots there ^20260716-1
- [DC] "index" is earned by construction: every line finally points down to its chat support — a member is a cache over the chats, never authority; consumers verify through the support turns ^20260716-1
- [FR] the nature of the annotation varies by application: a line may restate the turn content, or contextualize why the support turns support what is being annotated ^20260716-1
- [DC] member surfaces differ by design axes on top of the invariant: attachment point, gating, format, ordering ^20260716-1
- [EX] the `Agentos.Index` is the first member — lines attached to concepts; `Chat.Agendix` attaches them to chats; `Skw.Agendix` to any `Skw.Annotation` ^20260716-1

****

## Touched.Support.Network

- [DF] `Touched.Support.Network` is the network relating anchored statements across all touched surfaces to their chat evidence — edges of the form `Support.Set` ↔ `Anchor.Metadata` ↔ `Anchored.Line` ^20260716-21 ^20260716-23
- [DC] two surfaces meet at the edge: the `Chat.Surface` holds the turns, the anchored surface holds the line; the anchory between them can carry metadata ^20260716-22
- [DC] `Anchored.Line` is the general node: an `Index.Line` is one case — agendix, archive, and annotation lines ride the same edge shape ^20260716-21
- [DC] metadata is free at this level: optional and implementation-defined — hint, explanation, whatever the integration needs; the bare edge `Support.Set` ↔ `Anchored.Line` is valid, the line itself explaining the relationship ^20260716-21 ^20260716-22
- [DC] it is a dynamic system: nodes and edges are created and eliminated as both sides evolve — the index is a view over the `Chat.Surface` contextualized by its current semantics ^20260716-19
- [DC] the surface holds the live cut — utility for the current model; git holds the network's history; the `Chat.Surface` holds the invariant turns ^20260716-19
- [DC] a turn's grounding history is traced by following the edit history of the anchors and the index — no history log on the surface ^20260716-20
- [DC] reinterpretation mints a new anchor rather than amending — new meaning is a new anchor, generalizing the wrong-date doctrine ^20260716-19
- [PR] `Chat.Support.Set` is the local view: one node's edge bundle; the network is the global object the sets compose ^20260716-20

### meta

- aliases: `Index.Support.Network`

****

## Demoted.Anchored.Line

- [DF] a `Demoted.Anchored.Line` is a demoted network edge: the anchored line, with its `Support.Set` and `Anchor.Metadata`, existed in some version of `Touched.Support.Network` and exists in none now — the relation demotes as one ^20260716-30 ^20260716-31
- [DF] an `Index.Demoted.Turn` is a turn with no live edge left ^20260716-27 ^20260716-30
- [CT] distinct from unindexed: past edges are the witness ^20260716-26 ^20260716-27
- [DC] demotion is evidence-based and computed: git holds every surface version — presence in history, absence in the live cut; no surface is constrained by it and none is required for it ^20260716-28 ^20260716-29
- [DC] the nature of a demotion is unknown by design: the edge existed and now it does not — no stored account; a turn rejoins by a fresh edge ^20260716-25 ^20260716-27
- [RJ] archive surfaces, frozen drift lines, maintained drift explanations as demotion machinery — git and the chat already hold the full context ^20260716-25 ^20260716-27

****

## Index.Line

- [DF] `Index.Line` is the atom of the `Touched.Surface.Index`: one statement, grounded to a `Chat.Support.Set` by its trailing anchor ^20260716-4
- [CT] one line, one fact — atomic and reorderable, surviving on its own (`Kernel.Writing` granularity) ^20260716-4
- [DC] the line is the unit of grounding, approval, and audit: gates, linters, and drift checks run per line ^20260716-4
- [DC] a line with its anchor in place is a `Grounded.Line`; one still missing it is an `Ungrounded.Line` — a legacy backlog, not a licensed state ^20260716-33 ^20260717-0
- [DC] lines carry a `Line.Type` classifying their act ^20260716-4
- [EX] on a `Verbatim.User.Gated` surface, each line's support set holds a `Turn.Type::Project.Index.Gate` turn ^20260716-4 ^20260716-10
- [PR] everything above the line is organization — blocks, surfaces, attachment points; everything below it is evidence — anchors, support sets, turns ^20260716-4

****

## User.Attention

- [DF] `User.Attention` is the scarce resource of the hugentic system: what the user can actually read, judge, and approve ^20260716-6
- [PR] the system economizes it deliberately — surfaces are designed by how much of it they spend ^20260716-6
- [DC] `Verbatim.User.Gated` spends it on purpose — that spend is what buys stability; the `Index.Agendix` scales precisely because it spends none ^20260716-6 ^20260716-10
- [DC] analogous to attention in LLMs: the limited context the human can condition on — "we must make Y pass through the `User.Attention`" ^20260716-6
- [EX] spend it on the `Project.Index`; offload everything else to agent-driven surfaces ^20260716-6

****

## Skw.Touched.Index

- [DF] `Skw.Touched.Index` is the `Touched.Surface.Index` member attached to `Skw.Annotation`s: `Index.Line`s riding annotations on generated surfaces — file, module, region, construct ^20260717-7 ^20260717-10
- [DC] one mixed surface: gated and ungated lines share the place — a line is gated iff its support set holds the gate-typed turn (`Turn.Type::<Surface>.Gate`); the split is computed, not geographic ^20260717-6 ^20260717-7
- [DF] `Skw.Appendix` and `Skw.Agendix` are its computed strata — the gated and the ungated lines: the appendix and agendix of a block, where the block is the annotation — same mechanics, no file split ^20260717-9
- [DC] promotion is a state change, not a relocation: a line passes the gate where it stands — the gate turn joins its set; nothing moves ^20260717-6 ^20260717-10
- [DC] two worlds meet at the annotation: the skw development stack reads it to generate, judge, and evolve the surface; the touched lines ground to the `Chat.Surface` — the user-grounded part of that context ^20260717-8

****

## Skw.Network

- [DF] `Skw.Network` is the graph of annotated surfaces linked by the relationships the skw system defines between them ^20260715-6
- [DC] relationships are explicit or implicit: explicit ones are the declared links a `Module.Import` carries; implicit ones are derived by the system, such as support-set intersection between chat anchors ^20260715-6
- [DC] the network is computed from consumer-side declarations — a target never registers its dependents; followers are derived, so an imported surface stays ignorant of its importers ^20260715-6
- [PR] the network's job is notification, not judgment: when a surface changes, the `CPU.Program` notifies every surface the network links to it — a purely mechanical fan-out along the edges ^20260715-6
- [DC] an `Agentic.Program` interprets each notification: whether the change is benign or a real change to propagate is a semantic verdict only the agent carries ^20260715-6
