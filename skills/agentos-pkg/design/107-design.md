> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Agentos.Skillware

- `Agentos.Skillware` is the discipline of treating skills as software — the skill is the unit of software for agents.
- "as software" means the artifacts agents run gain engineering structure — modules, dependencies, builds, versions, lineage — so they can be reused and evolved rather than written once and forked.
- it is supported by a development toolchain — linters, builders, compilers — spanning agentic and `CPU.Impl` work, that moves package maintenance off the human. ^c20260627-4u
- a discipline realized by capabilities, not a single mechanism — it names the stance; specific members implement it.
- **skw** is the system realizing the discipline: the general annotation language (`Skw.Language`) and its `Skw.Backend`s ^c20260711-11u
- [CT] touch is an orthogonal axis over skw objects: an annotation, span, or line becomes touched only through its own touch provenance ^c20260729-159u
- [DC] `Skw.Touched.Index` materializes `Touched.Index` through grounded `Index.Line`s attached to `Skw.Annotation` instances ^c20260729-173u
- [PR] declared dependencies across project surfaces make maintenance and change propagation explicit around those indexed annotations ^c20260729-331u
- [DC] the toolchain speaks skw: `agentos skw` (build, check, bless, status) over `.skw/` build homes and `skw.json` config — `skillware` remains a deprecation alias; `agentos skw check` with no target runs project-wide over every discovered `Skw.Package`, making the whole `Skw.Network` checkable in one pass ^c20260720-46u

### meta

- `Explicit.Namespace`; members: `Skill.Module`, `Runnable.Surface`, `Inline.Annotation`, `Build.Surface`, `Build.Annotation`, `Skill.Runnable.Surface`, `Skill.Build.Surface`, `Skill.Package.Builder`, `Skw.Package`, `Skw.Ann.Dependency`, `Skw.Pkg.Dependency`, `Skw.Quote.Binding`, `Skw.Language`, `Skw.Annotation`, `Skw.Backend`, `Annotation.Point`, `Annotation.Authority`, `Drift.POI`, `Non.Skw.Annotation`, `Batchy.Router`, `Batchy.Router.Row`, `Routing.Table`, `Usage.Pattern.Routing`.

****

## Runnable.Surface

- [DF] a `Runnable.Surface` is a surface whose purpose is to be run, loaded, or used ^c20260723-46u
- [DF] an `Inline.Annotation` is a `Skw.Annotation` embedded in the runnable surface itself — no separate source, no compile step ^c20260723-47u
- [PR] splitting a `Build.Surface` out of the runnable is a response, not a default: reach for it only when the runnable cannot carry annotations without interference — otherwise annotate inline ^c20260723-52u
- [EX] skills split out a `Build.Surface` — the runnable loads into agent context, so embedded machinery would pollute the run; code annotates inline — comments are inert to execution, so the runnable hosts annotations for free ^c20260723-50u

****

## Skill.Runnable.Surface

- `Skill.Runnable.Surface` is a surface whose purpose is to be run — loaded into agent context to do work; it carries only the executable substance.
- the system keeps it free of non-runnable artifacts, so nothing obscures or dilutes what runs — a building-backend discipline; annotated-only `Skw.Backend`s trade it for constraint co-location. ^c20260627-6u
- forced by context being executable — anything on it is read into context and shapes the run; non-runnable artifacts there are not inert, they interfere.
- [DC] it specializes `Runnable.Surface`: loaded into agent context, it is kept clean — its annotations split out to the `Skill.Build.Surface` ^c20260723-34u

****

## Build.Surface

- [DF] a `Build.Surface` is the off-runnable home for the source skw compiles into its `Runnable.Surface` — never loaded at run time ^c20260723-45u
- [DF] a `Build.Annotation` is a `Skw.Annotation` on the `Build.Surface`, stripped from the compiled runnable so no machinery reaches what runs ^c20260723-44u

****

## Skill.Build.Surface

- `Skill.Build.Surface` is the complement of `Skill.Runnable.Surface` — it holds the artifacts that produce and maintain runnable content, and is never loaded at run time. ^c20260627-3u
- it is the home for everything kept off the runnable surface: derivation context, dependency declarations, lineage, dev material. ^c20260627-5u
- never run, it carries no "stay clean" constraint — an unconstrained workspace; that freedom is what the two-surface split buys.
- realized as the per-package `.skw/` folder (legacy `.skillware/`, still read during the rename window) — `src/` mirror, `skw.json` settings, lock — organized by capability, discovered by convention. ^c20260710-6u
- [DC] it specializes `Build.Surface` — the `.skw/` realization of the off-runnable source home ^c20260723-33u

****

## Skw.Package

- [DF] a `Skw.Package` is a folder with a `.skw/` — the `.skw/` makes it a package: the unit skw discovers, checks, and builds ^c20260720-47u
- [DC] git-tracked: `.skw/` holds `skw.json` config, the `src/`, and `lock.json`; `.agentos/` keeps only project identity and runtime, while the tracked skw source lives in `.skw/` ^c20260720-38u
- [DC] scope mirror: one `skw.json` schema (`depots`, `surfaces`, `exclude`, `projects`) read at both project and package scope, the package extending the project via cascade; absent config means discover every `.skw/` and check all ^c20260720-42u
- [DC] a package holds managed surfaces of both kinds: a `Build.Surface` under `.skw/src`, and inline-annotated `Runnable.Surface`s elsewhere in its tree — a code-only package carries no `src/` ^c20260723-31u
- [DC] a package may also host an `Index.Depot` — its concept store, co-located under the same `.skw/` and addressed by `Dotted.Name` ^c20260724-62u
- [DC] a surface belongs to the nearest-enclosing `.skw/`, co-located in the same repo; reach across packages or repos is `Skw.Pkg.Dependency` only — a `.skw/` never manages surfaces outside its own tree ^c20260723-32u

****

## Skill.Package.Builder

- `Skill.Package.Builder` is the support system for developing and maintaining a skill package's `Skill.Runnable.Surface`
- it is a bundle of agentic skills and CLI support tooling that run build workflows over the package
- a build workflow either produces runnable content or checks it — builds, drift-checks, tests, lint
- it is open-ended — any build workflow can be added; derivation is one capability, not the whole system
- the `Skill.Build.Surface` is its workspace — it holds anything the builder needs that should not live on the `Skill.Runnable.Surface`
- realized as the `agentos-skillware` `Package.Aux.Skill`, which centralizes all Skillware `Skill.Module`s — build toolchain, language, authoring, doctrine ^c20260710-5u

****

## Skw.Ann.Dependency

- [DF] `Skw.Ann.Dependency` is the annotation-level dependency edge — a `--from` declaring a target by `Skw.Address.Schema` name: the declaration and how it resolves, not how the target is materialized ^c20260724-82u
- [DC] the consumer declares; the target never knows its dependents ^c20260709-28u
- [DC] a `--from` may be refined by a `Skw.Quote.Binding` — quoted lines pinning the exact interest range inside the target ^c20260718-36u
- [DC] resolution: an in-package target resolves by address; a cross-package target resolves through `Skw.Pkg.Dependency` ^c20260724-72u

### meta

- aliases: `Module.Import`, `Import.Management`

****

## Skw.Pkg.Dependency

- [DF] `Skw.Pkg.Dependency` is the named registry resolving a cross-package dependency: an `id → package` map a package declares, the sole sanctioned way a `--from` leaves its own package ^c20260724-84u
- [CT] a `--from` may not address a surface outside its package by raw path — a path leaving the package is rejected; the cross-package edge resolves only through a declared id ^c20260724-40u
- [DC] one `id → package` resolution reaches both of the package's addressable stores: its `Index.Depot` by `Dotted.Name` and its `.skw.md` src by `@<id>/<rel-path>` — same id, two addressing forms ^c20260724-71u
- [CT] only skw-parsable targets cross the boundary: index concepts (`Dotted.Name`) and `.skw.md` regions or spans — never a compiled target or a raw file ^c20260724-53u
- [DC] the `@<id>/<rel-path>` form: `@` anchors file space, `<id>` is the registry-resolved root (`Addressing.Sigil.Vocabulary`'s context variable), the tail resolves inside that package's src, recursively expanded ^c20260724-75u
- [PR] the indirection is the point: the location lives once in config, so a dependent's address survives the target package moving — layout-independence a raw path cannot give ^c20260724-118u
- [DC] target design is two-tier: local config names the dependency, a global registry resolves name → location — no config carries absolute paths (migrated from `Index.Depot.Dependency`) ^c20260722-33u
- [DC] the current `skw.json` `deps` map is one-tier relative paths — the `Current.Implementation`, not yet the target ^c20260724-77u

****

## Skw.Quote.Binding

- [DF] `Skw.Quote.Binding` is a dependency declared by its own actual content: a `--from` address plus explicitly quoted lines defining the interest range ^c20260718-49u
- [DC] the address is the selector — what the alarm uses to narrow the dependency; the quoted lines pin the exact range by content, not position ^c20260718-46u
- [CT] the quoted lines live on the annotation, not the generated surface — the annotation itself is maintained: a non-existing or drifted line cannot attach ^c20260718-35u
- [PR] plain block links stay legal; quoting is opt-in remarking — the quoted content sits next to the annotated surface so the generator agent cannot miss it ^c20260718-51u
- [PR] content-addressing makes the reference honest: it survives source reordering and breaks loudly under change, never silently pointing at the wrong lines ^c20260718-50u
- [DC] a quoted line no longer verbatim-present at its source raises a POI on the declaring construct — the existing unresolvable-`--from` POI extended to content ^c20260718-39u
- [DC] syntax: a repeatable `--quote` flag refining the nearest preceding `--from`; each value is one verbatim line of interest, plain continuations append ^c20260718-45u
- [DC] `Touched.Surface.Index` lines are cited through it: a block cite is a bare `--from Block.Path`, a line cite adds `--quote` ^c20260723-29u
- [DC] a block cite needs a stable-named target; a provisionally-named block (promotion may rename) is cited by file line quote only — the rename then surfaces as a loud POI, not a silent miss ^c20260723-30u
- [CT] an ungrounded line is never quoted — it could leak assistant-untouched content into the cite; a quoted TSI line carries its anchor verbatim, the pin and the grounding handle ^c20260723-22u
- [DC] re-grounding is not transparent to citers: reinterpretation mints a new anchor (`Demoted.Index.Line`), changing the quoted content and raising the drift POI even when prose is unchanged — a re-confirm signal, not silent drift ^c20260723-35u

### meta

- aliases: `Quote.Binding`

****

## Skw.Language

- [DF] skw is an embedded annotation language for the generation of surfaces — an annotation states how a span of content is produced: from which dependencies, under which rule ^c20260711-70u
- the annotation constrains the span: the content must not contradict or drift from its declaration — every annotation is a checkable claim ^c20260711-44u
- [DC] one written form — a named block whose features are `--flag`s ^c20260720-40u
- the binding mode is a flag: `--copy` is deterministic generation (inlining a source, itself possibly generated), `--derived` is agentic generation under its `--intent`, a block with no binding flag makes no generation claim; a link's text is a typed generated span ^c20260711-45u
- [DC] the three binding modes differ by when they resolve: `--copy`/`--derived` materialize statically at build time, `--pointer` resolves dynamically at load time, always fresh ^c20260709-29u
- it annotates any content, but earns most on agent-generated surfaces — where the rule and its current solution living side by side is what makes maintenance checkable ^c20260711-31u
- it is embedded — skw lives inside the host surface's own format, next to the content it governs, and never replaces it ^c20260711-34u
- the language is surface-blind; a `Skw.Backend` binds it to each surface class ^c20260711-53u
- [DC] skw lines need no user grounding to be legal — touch is opt-in per object: annotations carry documentation and citations by address, and their own touched lines through `Skw.Touched.Index` ^c20260719-31u

****

## Skw.Backend

- [DF] a `Skw.Backend` binds `Skw.Language` to one surface class, named `skw-<surface>` ^c20260711-68u
- a backend owns four things: the carrier syntax, the build semantics (if any), where check state lives, and its host-native `Annotation.Point` vocabulary ^c20260711-16u
- every backend is annotated; some backends additionally build — annotation + check is the universal layer, build is backend-local ^c20260711-25u
- a building backend generates its runnable form from annotated src and strips the machinery; an annotated-only backend keeps declarations in place on the surface itself, trading surface cleanliness for constraint co-location ^c20260711-17u
- **skw-skills** is the first backend, a building one: annotated src compiles to the skill's runnable files ^c20260711-12u
- [DC] skw-code is annotated-only — the comment is its carrier (`# $kw:` opens, `# --flag` belongs, `# $kw. end` closes) and the annotated code is the body itself ^c20260722-32u
- [DC] a backend is a `Carrier` over one shared `$kw` frame core: the core consumes carrier-stripped tokens, the carrier strips its host syntax (markdown `>`, code comment `#`) — the split keeps `Skw.Language` surface-blind ^c20260722-31u
- [DC] a failed check is a drift finding with no predefined winner — resolution is case-by-case; a workflow may set auto-regeneration as its own rule ^c20260709-25u
- [PR] division of labor: the CPU materializes copy bindings and detects drift; the agent performs derivations — in src, where the declaration and its current solution live side by side ^c20260710-12u
- [DC] v1 realization: `lock.json` holds the per-dependency record; check verdicts (`copy-drift`, `derived-stale`, `hand-edited`) surface drift — a rebuild can never silently clear `derived-stale`; only an actual re-derive does ^c20260710-11u

****

## Skw.Annotation

- [DF] `Skw.Annotation` is the unit of skw: a named block attached at an `Annotation.Point`, stating things *about* the content it names — its identity is one explicit `Skw.Address.Schema` address ^c20260711-66u
- [DC] features are additive `--flag`s: `--note` (documentation), `--from` (dependency), `--derived`/`--copy`/`--pointer` (binding mode), `--intent`, `--supp` (its own touched lines); a pure note carries only `--note` lines ^c20260720-37u
- [DC] the address is declared relative (resolved against the current surface) and cited absolute (the full locator); a block may fence its generated target, whose element name checks the address ^c20260720-43u
- [DC] `--note [TYPE] <text> ^anchor` carries documentation as an `Index.Line` — typed and grounded; a block's `--note` lines are the index attached to whatever it names, reaching any surface without a `.md` ^c20260720-35u
- [CT] `Index.Block` and `Skw.Annotation` are the same object — a named block of typed lines: an index concept is it addressed by a `Dotted.Name` with only `--note` lines; a pure dependency is it with `--from` and no notes ^c20260720-31u
- [PR] every annotation is a checkable constraint: the CPU checks its decidable face (resolution, structure, hashes); agents check its semantic face (does the body honor the declaration) — annotations are to prose what types are to code ^c20260711-71u
- it is a deliberate subset: the fragment's fundamentals — it answers *what context can't I miss to understand this fragment?* ^c20260711-32u
- it is a local grounding recipe: an agent landing on the fragment loads the declared dependencies and holds the minimal sufficient context by declaration, not by search ^c20260711-33u
- [DC] the flag vocabulary is the language's growth axis: new capability is a new flag on the same named block ^c20260710-10u

### meta

- aliases: `Skillware.Construct`, `Surface.Annotation`

****

## Annotation.Point

- [DF] an `Annotation.Point` is a named, sanctioned place where annotations attach — a small vocabulary of points so agents do not over-annotate arbitrary fragments ^c20260711-69u
- points come in two families: **host-native** — the natural divisions of the annotated surface — and **skw-native** — the language's own scoping constructs, layered on top ^c20260711-37u
- [PR] prefer the host's natural divisions; reach for skw-native scoping only where the host's divisions do not fit the annotation's true scope ^c20260711-72u
- the file is the universal host point; each backend declares the rest of its host vocabulary — functions, modules, namespaces for code; sections for markdown ^c20260711-50u
- the skw-native points: the **annotation section** (a leveled, end-free divider sectioning a file for annotation purposes only) and the **span** (an explicit construct body — the finest grain) ^c20260711-56u
- the agent attaches at the coarsest point that honestly fits ^c20260711-43u
- [DC] the sanctioned points are a configurable policy the linter enforces, not a fixed set: a per-surface allow-set, each point carrying placement, cardinality, and presence rules — strict defaults that `skw.json` relaxes as finer points earn their place ^c20260723-40u
- [DF] `illegal-attachment` is a well-parsed annotation at a point outside the allow-set — attached nowhere sanctioned; opening a finer point in config moves its attachments illegal→legal ^c20260723-43u
- [DC] skw-code starts strict: its one point is the file, its block at line 1, exactly one, required — a block off line 1 or a second block is an `illegal-attachment`, a managed file with no line-1 block a `missing-header` ^c20260723-36u

****

## Annotation.Authority

- [DF] `Annotation.Authority` is the authority model of annotations: authority flows from grounding, not from the writer ^c20260711-64u
- annotation lines take the index's own forms: `Line.Type` codes and `Anchory.Anchor`s, with the same validation points ^c20260711-18u
- authority follows `Touched.Authority`: untouched annotation lines are hypotheses bound by the grounded span; grounded ones hold second-order authority; gated ones are first-order touched ^c20260711-22u
- what stays restricted below the gate is linkability, not worth — the `Touched.Authority` fence ^c20260711-60u
- no status is stored: drift is discovered and surfaced by the checker; authority is read from the lines' provenance ^c20260711-36u
- [CT] agent-free insertion is regulated: only the file `Annotation.Point` is open to ungated agentic annotation — every finer point lands user-gated ^c20260711-62u
- finer annotations are therefore born touched: the gating turn is their grounding evidence ^c20260711-26u

****

## Drift.POI

- [DF] a `Drift.POI` is a point of interest raised by the CPU checker: a span's declared dependencies changed — that, and nothing more ^c20260711-67u
- the CPU never rules on drift: whether the surface actually drifted is an agent's finding — the agent is always the fixer and supervisor ^c20260711-41u
- a POI carries its trigger — which dependency, what changed — so the responding agent starts contextualized ^c20260711-14u
- resolution is agentic: real drift → re-derive the span; benign change → re-bless the dependencies ^c20260711-39u

****

## Non.Skw.Annotation

- [DF] a `Non.Skw.Annotation` is a raw comment on a skw-managed surface that resolves to no `Skw.Annotation` — a `Drift.POI` kind: an annotation leaking outside the language ^c20260722-36u
- [PR] skw owns the annotation channel completely: on a managed surface every comment must be a `Skw.Annotation` — prose is content skw may annotate, structured comments are directives it replaces ^c20260722-37u
- [CT] a pure `--note` (no `--from`) is a legal wrap: an explanation with no design target is still tracked by its type and anchor — the floor is "every comment is an annotation," not "every comment links to design" ^c20260722-29u
- [DC] three resolutions close it: wrap the comment as whatever `Skw.Annotation` fits (the same authoring as any annotation), delete the comment, or bless it as genuine throwaway (`Poi.Bless`) — the POI is only the trigger ^c20260722-34u
- [PR] the flood is closed elsewhere: because finer `Annotation.Point`s are user-gated (`Annotation.Authority`), an agent cannot spray notes — this POI closes the raw-comment leak, gating prevents an unregulated annotation system ^c20260722-39u
- [CT] the regulated unit is the full-line comment: only full-line comments must be annotations — an inline trailing comment (or `#` inside a string) is free space, because skw machinery needs its own full comment line and cannot ride an inline one ^c20260723-25u

### meta

- aliases: `Non.Skw.Comment`

****

## Floor.Model

- [DF] a `Floor.Model` is a structured representation whose declared minimum guarantees support dependable downstream interpretation ^c20260724-88u
- [CT] its floor identifies the structural facts consumers may rely on ^c20260724-52u
- [RJ] it does not promise semantic resolution or completeness beyond its declared floor ^c20260724-125u
- [PR] a `Floor.Model` decouples consumers from the mechanism that produced their input ^c20260724-108u
- [FR] a parser, normalization pipeline, or another model producer may provide a `Floor.Model` ^c20260724-104u
- [EX] a `Closure.Parser` AST is a `Floor.Model` when its source satisfies the `Parse.Floor` ^c20260724-96u
- [EX] `Chatlas.Session.Model` is a `Floor.Model` produced through normalization ^c20260724-95u

****

## Closure.Parser

- [DF] a `Closure.Parser` enforces a `Parse.Floor`, the minimum source structure required to produce a dependable `Floor.Model` ^c20260724-87u
- [PR] the `Parse.Floor` stays minimal: only structurally certain failures belong below it ^c20260724-115u
- [DC] below the `Parse.Floor`, the source is unprocessable and the parser is not required to return an AST ^c20260724-66u
- [DC] at or above the `Parse.Floor`, the parser returns an AST that is a `Floor.Model` ^c20260724-65u
- [CT] the AST contains every detectable parsable element from the source ^c20260724-54u
- [CT] unresolved regions above the floor are preserved as fallback structure ^c20260724-57u
- [RJ] unresolved detail above the floor does not produce parser errors or warnings ^c20260724-126u
- [RJ] a `Closure.Parser` does not emit `Point.Of.Interest` instances ^c20260724-123u
- [PR] its AST may serve `POI.Linter` and other model consumers ^c20260724-112u

****

## POI.Linter

- [DF] a `POI.Linter` evaluates a `Floor.Model` by executing one or more `POI.Check`s ^c20260725-138u
- [CT] it emits zero or more `POI.Instance`s carrying their `POI.Class` identities and occurrence evidence ^c20260725-74u
- [CT] it consumes the dependable model supplied to it, not the producer’s raw source ^c20260725-72u
- [PR] heuristic and policy concerns become reviewable instances rather than failures of the model producer ^c20260725-160u
- [CT] its instances enter the shared `POI.System` for class resolution, presentation, documentation, and permitted resolution acts ^c20260725-79u
- [RJ] a linter does not produce its input model or own authoritative class semantics ^c20260725-166u
- [RJ] it does not render final policy by itself or resolve the instances it emits ^c20260725-172u

****

## POI.System

- [DF] a `POI.System` is the shared machinery that carries POIs from detection through presentation, documentation discovery, and resolution ^c20260725-140u
- [CT] producers emit `POI.Instance`s carrying stable `POI.Class` identities ^c20260725-82u
- [CT] the system resolves each instance’s canonical `Wayfinder.Reference` through `Agentos.Wayfinder` before rendering, explaining, or resolving the instance ^c20260729-157u
- [CT] `POI.Renderer`, `POI.Explain`, and `Poi.Bless` consume the same resolved class-and-instance model ^c20260725-53u
- [CT] catalog or documentation failures are reported without hiding the original instances ^c20260725-63u
- [PR] different linters share one POI lifecycle while domain semantics remain with their owning packages ^c20260725-159u
- [RJ] the system does not own producer input models, domain checks, or authoritative documentation ^c20260725-174u

****

## POI.Check

- [DF] a `POI.Check` is one named evaluation that a `POI.Linter` runs over its `Floor.Model` ^c20260725-136u
- [CT] it declares the `POI.Class` identities it may emit ^c20260725-73u
- [CT] each match produces a `POI.Instance` with stable identity, target location, and concrete evidence ^c20260725-69u
- [PR] checks own detection mechanics while classes own meaning, documentation, and resolution policy ^c20260725-157u
- [CT] several checks may participate in one linter, and several linters may emit instances of the same class ^c20260725-85u
- [RJ] a check does not bless instances or determine their final disposition ^c20260725-165u

****

## POI.Class

- [DF] a `POI.Class` is the durable domain-owned semantic definition shared by occurrences of one reviewable situation ^c20260730-97u
- [DC] each class is a `Kernel.Block` contained in the `POI.Catalog` of its owning `Package.Skill` ^c20260730-70u
- [DC] the stable identity of a class is its canonical `Wayfinder.Reference.Type::Index.Block` reference ^c20260730-87u
- [CT] the class block is its canonical `POI.Documentation` root and declares its short runtime description, evaluation protocol, allowed resolution acts, and required context surfaces ^c20260730-58u
- [CT] many `POI.Instance`s may carry the same class reference; class data is resolved when needed rather than duplicated into each instance ^c20260730-54u
- [PR] package ownership keeps class meaning and evaluation guidance with the domain that owns them, independently of which subsystem emits an instance ^c20260730-110u
- [RJ] a `POI.Class` is not a concrete occurrence, evaluation verdict, or resolution ^c20260730-113u

****

## POI.Instance

- [DF] a `POI.Instance` is one concrete occurrence of a situation defined by a `POI.Class` ^c20260725-137u
- [CT] it carries a stable instance identity, the canonical `Wayfinder.Reference` of its `POI.Class`, target location, and concrete evidence describing the current situation ^c20260729-108u
- [CT] its identity remains stable across repeated checks while the same occurrence persists ^c20260725-78u
- [CT] it is the unit of resolution acts; when its class permits blessing, `Poi.Bless` blesses only that instance ^c20260725-76u
- [PR] class metadata is resolved through the class reference rather than duplicated into the instance ^c20260725-158u
- [RJ] resolving one instance does not resolve its class, another instance, or a future occurrence ^c20260725-173u
- [CT] a `POI.Instance` signals a situation requiring attention; its existence alone does not determine resolution, which is evaluated through its evidence and resolved `POI.Class` guidance ^c20260729-53u

****

## POI.Catalog

- [DF] a `POI.Catalog` is the dedicated `poi` chapter of a `Package.Skill.Index`, containing the package-owned `POI.Class` blocks available for machine discovery ^c20260729-283u
- [DC] a `Package.Skill` that owns POI classes registers them as blocks in its catalog ^c20260729-182u
- [CT] each `POI.Class` block is the canonical indexed documentation root for that class ^c20260729-88u
- [CT] a class is addressed by a `Wayfinder.Reference.Type::Index.Block` reference rooted at its owning `Package.Skill` ^c20260729-57u
- [CT] common POI machinery resolves the class reference through `Agentos.Wayfinder`, independently of which subsystem emitted its instances ^c20260729-80u
- [CT] missing or ambiguous class resolution emits a resolution POI without hiding the original `POI.Instance` ^c20260729-120u
- [RJ] a catalog contains class definitions and documentation roots, not `POI.Instance` occurrences ^c20260729-361u

****

## POI.Documentation

- [DF] `POI.Documentation` is the authoritative content that defines a `POI.Class` and how its instances should be evaluated ^c20260730-94u
- [DC] its canonical root is the class block contained in the owning `Package.Skill` index’s `POI.Catalog` ^c20260730-79u
- [CT] the class block contains the class definition, evaluation protocol, and guidance required to reason about its instances ^c20260730-57u
- [CT] common POI machinery retrieves the documentation root by resolving the class’s `Wayfinder.Reference` through `Agentos.Wayfinder` ^c20260730-48u
- [FR] a class block may reference additional documentation surfaces through further `Wayfinder.Reference`s without changing its canonical root ^c20260730-103u
- [FR] a documentation surface may carry a `Skw.Surface.Token` and participate in a required context checkpoint for an act such as `Poi.Bless` ^c20260730-104u
- [RJ] documentation is not duplicated into each `POI.Instance` ^c20260730-117u

****

## Skw.Surface.Token

- [DF] a `Skw.Surface.Token` is a machine-readable opaque token attached to one addressable managed surface ^c20260730-100u
- [CT] the token is parsable from the surface itself ^c20260730-61u
- [CT] a block surface may carry its token in `### meta` ^c20260730-37u
- [CT] a file surface may carry its token in its surface-level Skw annotation or header ^c20260730-38u
- [CT] a managed surface carries at most one current surface token ^c20260730-39u
- [PR] surface-owned tokens let tooling retrieve the current checkpoint mechanically without copying token values into dependent policies ^c20260730-111u
- [RJ] a surface token does not declare what acts or POI classes it unlocks ^c20260730-115u

****

## POI.Renderer

- [DF] a `POI.Renderer` presents `POI.Instance`s using their resolved `POI.Class` definitions ^c20260725-139u
- [CT] it resolves each instance’s canonical `Wayfinder.Reference` through `Agentos.Wayfinder` before presenting its `POI.Class` definition ^c20260729-111u
- [CT] it prints each class identity and short description once, followed by its compact instances ^c20260725-77u
- [CT] each instance presentation identifies its target, current situation, and instance identity ^c20260725-68u
- [PR] the output orients the agent and provides a path to deeper `POI.Documentation` ^c20260725-164u
- [CT] unresolved or ambiguous classes are reported without hiding their instances ^c20260725-95u
- [RJ] a renderer does not own class semantics, documentation, or resolution policy ^c20260725-167u

****

## POI.Explain

- [DF] `POI.Explain` is the common discovery act that retrieves the authoritative documentation for a POI class or instance ^c20260729-263u
- [CT] an instance request obtains the canonical `Wayfinder.Reference` carried by its `POI.Instance` ^c20260729-71u
- [CT] a class request accepts a canonical reference or a `Wayfinder.Reference.Sugar` form that parses into one ^c20260729-58u
- [CT] `POI.Explain` resolves the class reference through `Agentos.Wayfinder` and presents the resolved `POI.Class` block ^c20260729-50u
- [CT] failed class or documentation resolution surfaces its `Wayfinder.Resolution.POI` without hiding the original explain request ^c20260729-100u
- [PR] agents use one explanation interface without needing to understand package ownership, registry state, or index layout ^c20260729-327u
- [RJ] `POI.Explain` resolves and presents documentation; it does not copy or own it ^c20260729-359u
- [EX] a command surface may expose the act as `agentos poi explain <class-or-instance>` ^c20260729-294u

****

## Chat.POI.Linter

- [DF] a `Chat.POI.Linter` is a `POI.Linter` that consumes a full `Chatlas.Session.Model` as its `Floor.Model` ^c20260724-86u
- [CT] it consumes normalized session data, never provider-native data ^c20260724-51u
- [DC] its rules inspect facts represented by the `Session.Event.Tape` ^c20260724-69u
- [CT] each emitted POI identifies the relevant session state and routes to its `POI.Documentation` ^c20260724-46u
- [RJ] a `Chat.POI.Linter` does not modify the session or determine how its POIs are resolved ^c20260724-122u

****

## Poi.Bless

- [DF] `Poi.Bless` is the explicit, auditable act of accepting one `POI.Instance` in its current situation ^c20260730-95u
- [CT] blessing is available only when the instance’s `POI.Class` declares it as an allowed resolution act ^c20260730-46u
- [CT] the class owns the blessing policy and declares its required context surfaces ^c20260730-59u
- [CT] a required context surface may or may not carry a `Skw.Surface.Token` ^c20260730-42u
- [CT] when a required context surface carries a token, blessing validates the matching provided unlock receipt ^c20260730-64u
- [CT] blessing may require receipts for several tokened surfaces ^c20260730-47u
- [CT] refusal identifies each missing required surface without disclosing its token ^c20260730-55u
- [FR] a blessing policy may later route required surfaces through reusable `Skw.Context.Gate`s ^c20260730-101u
- [FR] a blessing policy may later use `Poi.Bless.Question` as a stronger context checkpoint ^c20260730-102u
- [RJ] blessing one instance does not bless its class, another instance, or a future occurrence ^c20260730-116u
- [PR] blessing is loud: an instance never clears through rebuilds, unrelated edits, or implicit baseline changes ^c20260730-107u

****

## Poi.Unlock.Token

- [DF] a `Poi.Unlock.Token` is the returned receipt value proving satisfaction of one tokened surface checkpoint for a protected act ^c20260730-99u
- [CT] its value is the current `Skw.Surface.Token` of the represented surface ^c20260730-52u
- [CT] a protected act may require several unlock tokens when it requires several tokened surfaces ^c20260730-40u
- [PR] the token prevents a protected act from completing when a required tokened context checkpoint was omitted ^c20260730-112u
- [PR] it provides mechanically checkable pre-validation that can be examined more deeply through the supporting chat ^c20260730-109u
- [RJ] token satisfaction alone does not guarantee that the context was read, understood, or correctly applied ^c20260730-118u

****

## Poi.Unlock.Registry

- [DF] a `Poi.Unlock.Registry` is a derived tooling surface that indexes tokened managed surfaces and their current unlock values for mechanical lookup ^c20260730-98u
- [CT] its source authority is the token-bearing surfaces themselves, not independent registry-written token values ^c20260730-51u
- [CT] a registry entry identifies the represented surface through `Skw.Address.Schema` ^c20260730-41u
- [CT] tooling may derive or refresh the registry by scanning managed surfaces for `Skw.Surface.Token`s ^c20260730-62u
- [PR] a derived registry accelerates lookup, validation, and linting without making token state a second authority ^c20260730-106u
- [RJ] a `Poi.Unlock.Registry` does not decide what acts or `POI.Class`es require a surface token ^c20260730-114u

****

## Poi.Bless.Question

- [DF] `Poi.Bless.Question` is a future stronger bless gate: a checkable question about the context required to evaluate a POI ^c20260723-41u
- [PR] questions test understanding more directly than unlock tokens ^c20260723-51u
- [CT] questions add authoring, validation, versioning, and stale-question costs ^c20260723-24u
- [DC] `Poi.Bless.Question` stays a later level; `Poi.Unlock.Token` is the simpler first gate ^c20260723-27u

****

## Structure.Ratchet

- [DF] the `Structure.Ratchet` is the system's direction of travel: over time, content moves from opaque text nodes into recognized structure — the target state is a fully structured surface where all remaining prose is ACTUAL prose: no parsable objects remain in the text ^c20260712-82u
- progress is measurable: the `Closure.Parser` knows exactly what fraction of a surface is structured nodes versus opaque text — the ratio is the ratchet's gauge ^c20260712-19u
- promoting a text pattern into the grammar converts a class of soft `POI.Linter` flags into hard parse-level guarantees ^c20260712-20u
- [CT] promotion is an `Experience.Gated.Decision`: promote a pattern when it keeps generating the same manual POI toil, never speculatively — premature grammar is how the language dies ^c20260712-34u

****

## Batchy.Router

- [DF] `Batchy.Router` is the single runtime routing mechanism of a `Batchy.Skill` ^c20260731-191u
- [DC] it resolves the current run configuration from explicit `Batchy.Skill.Flag`s, the live conversation, and declared defaults ^c20260731-157u
- [DC] a `Batchy.Skill.Flag` supplies explicit routing configuration for the current run ^c20260731-123u
- [CT] explicit configuration takes precedence over inferred or default configuration for the same route ^c20260731-81u
- [DC] the live conversation may automatically resolve routes that permit semantic discovery ^c20260731-179u
- [DC] a declared default resolves when no higher-authority configuration supplies the route ^c20260731-126u
- [CT] each route declares whether an explicit flag is required, automatic routing is permitted, or a default is available ^c20260731-78u
- [CT] a resolved route may bind a `Skill.Arg`, select a `Skill.Module`, or contribute or continue routing through a `Routing.Table` ^c20260731-59u
- [DC] `Batchy.Router` composes compatible route contributions into one resolved run configuration ^c20260731-115u
- [CT] flag order does not affect resolution; configured compatibility and precedence govern composition ^c20260731-83u
- [CT] incompatible explicit contributions leave the run unresolved unless a configured row declares their composition ^c20260731-85u
- [DC] calls that resolve to the same canonical run configuration are operationally equivalent ^c20260731-141u

****

## Batchy.Router.Row

- [DF] `Batchy.Router.Row` is one configured route available to `Batchy.Router` ^c20260731-187u
- [DC] it relates its permitted resolution inputs to one routed destination ^c20260731-156u
- [CT] a row may require an explicit `Batchy.Skill.Flag`, permit automatic discovery from the live conversation, declare a default, or combine the permitted resolution paths ^c20260731-61u
- [CT] its destination may bind a `Skill.Arg`, select a `Skill.Module`, or contribute or continue routing through a `Routing.Table` ^c20260731-90u
- [CT] explicit configuration takes precedence when several permitted paths resolve the same row ^c20260731-82u
- [FR] a row style may specialize how resolution and its routed effect are described without creating another runtime router ^c20260731-229u
- [DC] configured aliases may map several flag keys to one routed effect ^c20260731-143u
- [DC] a shorthand row may contribute the compatible configuration otherwise supplied by several flags ^c20260731-132u
- [CT] omitted routing context may be filled only by defaults declared by applicable rows ^c20260731-95u

****

## Routing.Table

- [DF] `Routing.Table` is the declarative router artifact consumed by `Batchy.Router` ^c20260731-212u
- [DC] Skillware represents a `Routing.Table` and each of its `Batchy.Router.Row` members as independently addressed `Skw.Annotation` instances ^c20260731-113u
- [CT] each row declares table membership explicitly and carries its canonical flags, aliases, matching policy, defaults, destinations, load paths, and `--when`/`--then` prompts as annotation fields ^c20260731-79u
- [CT] a row matching policy may require explicit configuration, permit semantic discovery, or accept either resolution path ^c20260731-60u
- [CT] a table declares whether resolution may select none, one, or several rows ^c20260731-62u
- [DC] rows are routing options rather than ordered steps ^c20260731-170u
- [DC] a row's routed effect may bind a `Skill.Arg`, select a `Skill.Module`, contribute run configuration, or continue routing through another `Routing.Table` ^c20260731-130u

****

## Usage.Pattern.Routing

- [DF] `Usage.Pattern.Routing` is a `Batchy.Router.Row` style whose discovery key describes a usage situation and whose destination describes the response that situation needs ^c20260731-215u
- [PR] usage patterns are mined from chats, repeated questions, and observed friction so routing remains weighted by real use ^c20260731-240u
- [CT] the style targets frequent or important situations where a prepared route provides a valuable hot path ^c20260731-109u
- [CT] its destination may identify knowledge or surfaces to load, behavior to perform, or output to produce ^c20260731-91u
- [DC] a usage-pattern row may be selected automatically from the live conversation when its configuration permits discovery ^c20260731-133u
- [DC] an unmatched situation leaves the row unresolved and allows the broader `Batchy.Router` run resolution to continue ^c20260731-135u

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

- [DF] `Experience.Gated.Decision` is a design decision deliberately parked until usage experience accumulates — the question is sound, but answering it now would be a mistake ^c20260711-65u
- the failure it prevents is double: deciding early locks in a guess; leaving the question unnamed loses it ^c20260711-49u
- identification is the work: mark the topic explicitly on a durable surface so the system carries the open question forward without answering it ^c20260711-28u
- the gate opens on evidence — real usage, felt friction, accumulated instances — and the decision is then made from experience, not speculation ^c20260711-52u
- sibling of `Specified.By.Precedence`: both defer authored contracts to accumulated reality; precedence defers the spec, this defers the decision ^c20260711-40u

****

## Index.Ontology

- [DF] `Index.Ontology` is the concept-naming layer of the `Project.Index` — the routed body of `Index.Block`s that names and defines the project's concepts, spanning the `Index.Chapter` folders ^c20260716-68u
- [DC] it is the authoritative name-set: `Index.Appendix` and `Index.Agendix` attach their material to concepts the ontology names ^c20260716-56u
- [DC] fully composed of conceptual blocks under tight `Kernel.Writing` compression, every one routed by `Index.Router`
- [DC] it is the index-level echo of `Kernel.Block.Fundamentals`: the compressed front, depth deferred to `Index.Appendix`
- [DC] with `Index.Appendix`, `Index.Agendix`, and `Index.Router` it composes the `Index.Surface` ^c20260716-64u

### meta

- aliases: `Index.Main`, `Index.Fundamentals`

****

## Index.Surface

- [DF] `Index.Surface` is the file surface of one `Project.Index` — `Index.Router`, `Index.Ontology`, `Index.Appendix`, and `Index.Agendix` taken as a single addressable surface ^c20260716-69u
- [DC] the agendix is part of the surface — its touched, captured, ungated layer ^c20260716-61u
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
- [DC] discovered index depots are peers whose entry `Package.Driver.Router` tables are consumed equally by the running `Batchy.Router` ^c20260731-145u
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
- [DC] the gradient is organization above the `Index.Line` — position in the sequence never changes a line's grounding or authority ^c20260718-47u

****

## Appendix.Default.Block

- `Appendix.Default.Block` is the catch-all block every concept has by default, addressed `Concept.X/Appendix`
- its name is the full path — a child block of the `Concept.X` node, sharing the `Concept.Scoping` container-first notation
- it holds the tail of the concept's `Block.Line.Gradient` — the lines past the index/appendix cut
- it has no space budget — it grows freely, in `Kernel.Writing` style (direct, orthogonal lines)
- it is the landing site for `Writing.Friction.Reduction` capture and `Concept.Explosion` appends — facts filed under a concept without minting a name

****

## Writing.Friction.Reduction

- `Writing.Friction.Reduction` is the principle that the Agentos system lowers the cost of capturing design as it is discussed — by routing capture to the surface whose friction matches it ^c20260705-5u
- friction is a designed gradient, and friction buys stability: `Chat.Surface` (free — talk is capture) → `Index.Agendix` (zero user friction, agent-driven, unstable wording) → `Index.Appendix` (`Kernel.Line`-level approval) → `Index.Ontology` (`Kernel.Block`-level work unit) ^c20260705-6u
- the aim is to capture as much of the user's design as possible before it is lost — structure is deferred, not skipped ^c20260705-11u
- the index keeps a friction floor on purpose — too-cheap writing would flush the hugentic surface; the friction is part of the alignment ^c20260705-12u
- on touched surfaces the approval gate stays — friction drops, the gate does not ^c20260705-10u

****

## Index.Agendix

- `Index.Agendix` is the agent-driven shadow of the Index — the ungated member of the index surface, one file per `Index.Ontology` concept: `agendix/Concept.X-agendix.md`, next to `appendix/` ^c20260705-4u
- it is a cache the agent keeps to aid grounding on stable surfaces — an unreviewed `Touched.Surface.Index` member ^c20260723-20u
- [DC] `Reviewed.Cite.Closure` governs citations into it: unreviewed surfaces may cite it, reviewed surfaces may not — the promotion pressure, an agendix entry must be reviewed before the index can cite it ^c20260723-28u
- [DC] it carries no reviewed wording, so staleness is benign: a stale agendix is a worse cache, never a corrupted source — consumers verify through the anchors, not the agendix line ^c20260713-8u
- the agent cannot mint routed concepts — it attaches lines and candidate blocks under existing routed concepts; the ontology primes the capture, the agent fills the gaps — the index's shadow, not a second index ^c20260716-35u
- hard rule: every line is a grounded summary of chat discussion — a rejection, a constraint, a highlight the index does not yet capture — carrying its `Anchory.Anchor`/`File.Mention` pointer; unsourced agent reasoning does not belong ^c20260705-7u
- writing rules are the appendix's — `Kernel.Writing` discipline, the same block and line forms; only the supervision differs: all work is done and supervised by agents
- capture is user-triggered but not gated — the agent may suggest a capture pass, never start one
- it extends the `Block.Line.Gradient` past the touch cut: fundamentals → `Concept.X/Appendix` (touched tail) → the concept's agendix shadow tail (untouched) ^c20260705-9u
- homeless material lands in a fallback file — misfit pressure is evidence a concept is missing (concept-gap detector) ^c20260705-8u
- it is index-adjacent, not part of the index — it softens the index principles on the fly, replacing the direct user touch with a grounding link to the touch event
- it is self-similar to the appendix — an untouched appendix, same form and rules; it exists because the user gate is the bottleneck: a surface for the agent to run ahead of the gate
- agendix and appendix must not duplicate content — over time the agendix drains: entries reviewed by the user are promoted through the gate or dropped
- agendix lines are typed: every line carries a `Line.Type` from the vocabulary — the validation point applies to agent capture too ^c20260707-5u
- [DC] agendix files follow appendix writing rules with the block headed `Concept.X/Agendix`, one file per concept in `agendix/` next to `appendix/`
- [DC] captures with no routed concept land in `agendix/Unassigned-agendix.md` — the homeless pool, promotion evidence for concepts the index does not yet name, never a dump
- [DC] agendix entries may group into blocks — the appendix's block forms apply; a candidate block attaches as a path-child of a routed concept (`Concept.X/Agendix/Candidate.Name`) or pools in `Unassigned` ^c20260716-45u
- [DC] a candidate block's name is provisional — unrouted, citable from unreviewed surfaces but not reviewed ones (`Reviewed.Cite.Closure`); promotion may rename it ^c20260716-42u
- [DC] blocks promote like lines: copied out through the normal gates into index main or appendix ^c20260716-49u
- [CT] the agendix holds touched but ungated material — every line grounded by a user-turn support set, no line landed through a user-gated capture ^c20260716-40u
- [RJ] assistant-grounded capture (`[AS:XX]`, anchoring assistant turns) is excluded — assistant material enters only through the user turn that touched it ^c20260716-72u
- [PR] the agendix is the agentic path of the alignment workflow the gated edit runs hugentically — same primitives (typed `Kernel.Line`s, anchors, the current concept set), the user gate replaced by hard provenance ^c20260708-20u

****

## Capture.Gradient

- [DF] `Capture.Gradient` is the ladder a touched statement climbs across surfaces: chat → agendix → appendix/ontology ^c20260716-65u
- [DC] chat — touched, uncaptured, volatile ^c20260716-50u
- [DC] agendix — touched, captured, ungated: agent-authored wording, not a `Stable.Surface` — nothing may link into it ^c20260716-46u
- [DC] appendix/ontology — touched, captured, gated: wording passed `User.Attention`, a `Stable.Surface` — citable from other surfaces ^c20260716-47u
- [PR] the gate buys wording stability, not touched authority: a line derives `Touched.Authority` from its `Support.Set`, so strongly supported unreviewed content may outweigh weakly supported reviewed content ^c20260729-352u
- [DC] reading order follows the gradient — ontology and appendix first, agendix later: a prior, not a verdict on any line ^c20260716-58u

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
- [DC] `Index.Line` is its touched-index specialization — a `Kernel.Line` whose grounding standing determines whether it carries `Touched.Authority` or the weaker `Index.Presumption` ^c20260716-41u

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

- [DF] `Context.Grounding` is the active pursuit of relevant evidence to condition an agent's context, reasoning, and action ^c20260729-254u
- [CT] relevant evidence may live on any reachable surface; `Touched.Data` is a primary grounding set, not the whole evidence universe ^c20260729-131u
- [DC] `Index.Grounding` is the cheap first pass through the `Touched.Index` for evidence of historical touch ^c20260729-168u
- [DC] full touch grounding follows each `Support.Reference` through its `Support.Set` to the original `Touch.Authority.Surface` ^c20260729-211u
- [CT] because a qualifying `User.Turn` is presently the only registered authority surface, every current touch-evidence descent terminates on `Chat.Surface` and resolves through Chatlas ^c20260729-75u
- [EX] code, git history, documentation, and runtime state may supply relevant evidence independently of touch provenance ^c20260729-297u
- [CT] context grounding is read-only and ungated; it changes the agent's context, never a surface ^c20260729-81u

****

## Index.Enrichment

- [DF] `Index.Enrichment` is the hugentic drive to always increase the `Touched.Surface` of any block or line — no block is finished ^c20260709-31u
- [DC] grounding and enrichment split by evidence source: grounding is retrospective, mining the existing chat corpus; enrichment is generative, producing new touched surface ^c20260709-26u
- the discussion is the yield: spawning a focused discussion about a block creates the user turns that become its new grounding surface — and, through the gate, possibly new content ^c20260709-23u
- [DC] `Grounding.Density` reads as pipeline position: zero → mine the corpus first (grounding); low → generate (enrichment); high → rest until touched again ^c20260709-24u
- enrichment is block-scoped and gated — a micro design-session one block wide; the block's density delta is the receipt ^c20260709-19u
****

## Git.Dating

- [DF] `Git.Dating` is dating a file or file line by finding its last change in the git history ^c20260709-30u
- the date turns a static artifact into a searchable event: it says where in time to look further about the target — for instance in the chat corpus ^c20260709-22u
- [DC] the commit dates the write; the originating evidence is earlier — search around and before the commit time, not at it ^c20260709-27u
- `git log -L` follows a line's wording past mechanical commits to the content-bearing ones ^c20260709-17u
- it is the entry step of backward grounding: git dates the wording, chatlas finds the session and turns ^c20260709-20u
****

## Skw.Edition.History.Service

- [DF] `Skw.Edition.History.Service` is the canonical Skillware boundary for recording, reading, and checking `Skw.Edition.History`. ^c20260725-126u
- [DC] Git supplies editions, Chatlas supplies possible sessions, Skillware defines their association, and `Agentos.Bloberia` stores and queries the resulting records. ^c20260725-98u
- [CT] the service owns its payload schema, validation, idempotency, history projection, and check findings while Bloberia remains application-agnostic. ^c20260725-92u
- [PR] agents and linters consume the service instead of depending on raw Bloberia records. ^c20260725-156u
- [CT] discovery and reconciliation belong to a specialized developer workflow; the service persists and validates the associations that workflow supplies. ^c20260725-65u
- [DC] Every edition-session association carries a nonempty, resolvable Chat.Support.Set; without it, the association is invalid. ^c20260725-97u
- [CT] Deterministic checking validates support structure and resolution; the maintainer judges whether the resolved fragment proves the edit. ^c20260725-46u
****

## Anchory.System

- `Anchory.System` is the Agentos subsystem for stable symbolic links to contexts on other surfaces
- `Anchory.Anchor` carries compact identity while `Anchory.Register` carries resolution data
- `Anchory.Namespace` partitions anchor keys into independent resolution domains
- Anchory is Agentos-wide rather than project-local ^c20260706-2u
- Anchory is library-first so other subsystems can integrate directly
- integrating subsystems own payload meaning and final traversal to referenced surfaces
- `agentos anchory ...` is a thin CLI over the library contract
- referenced surfaces remain authoritative; Anchory is plumbing, not truth
- keys are composed: the caller supplies meaning (namespace, alloc-prefix, tag), Anchory supplies identity — the counter ^c20260718-32u
- each `Anchory.Namespace` declares its one-letter key prefix and intention in `meta.json` — the resolution fallback context ^c20260718-31u
- a depot registry with `Pwd.Upward.Search` resolves any anchor without prior depot knowledge; every touched depot auto-registers ^c20260718-30u

### meta

- namespace-members: `./Anchory.Anchor`, `./Anchory.Namespace`, `./Anchory.Register`, `./Anchory.Record`, `./Anchory.Depot`, `./Integration`, `./Chat.Application`, `./Open.Design`
****

## Capture.Offer

- [DF] `Capture.Offer` is the practice of proposing an index capture at the moment the content is born — the exact typed line or block, verbatim, user-gated ^c20260718-48u
- [PR] capture is cheapest at the moment for both sides: the agent's context is hot and the anchor mintable on the spot; the user's judgment is hot too — reviewing now beats reconstructing later
- [DC] an offer presents destination options: ontology, appendix, agendix, or decline — the user picks the landing with the gate ^c20260718-40u
- [DC] an offer arrives landing-ready: proposed type carried, target scouted for each destination it offers
- [DC] it is the hugentic sibling of agendix capture — same trigger instinct, the user gate in place of hard provenance
- [DC] offers ride any workflow — impl execution, design, review; declining is cheap and normal, the offer must never block the work
- [DC] destinations generalize with the `Touched.Surface.Index`: an offer may target any member within reach — the project index's landings, a chat's index, an annotation's touched lines ^c20260802-149u
- [DC] it holds block form because it must stay referenceable: downstream surfaces declare dependence on the name, and only blocks are addressable to the resolver ^c20260718-44u

****

## Index.Chat.Capture

- [DF] `Index.Chat.Capture` is transforming material from one or more `Chat.Surface`s into grounded editions of a `Touched.Surface.Index` ^c20260726-38u
- [CT] it separates retrieval from capture judgment: retrieval surfaces candidate turns and authoritative coordinates; capture selects the material, its `Chat.Support.Set`, and its landing ^c20260726-17u
- [CT] every captured line is grounded to an agent-selected `Chat.Support.Set` of user turns before entering a touched index ^c20260726-15u
- [FR] capture may operate over chats already loaded in agent context or mine chats that have not yet been loaded; specializations define the source-access mode ^c20260726-42u
- [RJ] `Index.Chat.Capture` does not depend on one retrieval backend or query heuristic ^c20260726-46u

****

## InContext.Index.Chat.Capture

- [DF] `InContext.Index.Chat.Capture` is an `Index.Chat.Capture` whose source chats are already present in the capturing agent’s active context ^c20260726-37u
- [DC] the capturing agent performs semantic selection of the material and its supporting user turns from that context ^c20260726-28u
- [CT] Chatlas assists by discovering candidate event coordinates and projecting matches from the authoritative `Chatlas.Session.Model`; it does not decide semantic support ^c20260726-14u
- [FR] retrieval may use assistant turns and any useful query heuristic, but only agent-selected user turns enter the captured line’s `Chat.Support.Set` ^c20260726-43u
- [CT] the specialization is defined by context availability, not chat age — an older chat loaded into active context qualifies ^c20260726-21u
- [RJ] it does not cover mining a chat corpus for material whose meaning and support have not yet been loaded ^c20260726-48u

****

## Touched.Index

- [DF] `Touched.Index` is the global system for curating and densely presenting relevant `Touched.Data` ^c20260729-272u
- [DC] it aims to index every relevant region of touched data without reproducing the source data ^c20260729-213u
- [CT] relevance is the coverage boundary; curation governs how the material is presented, organized, and compressed ^c20260729-130u
- [PR] `Kernel.Writing` supplies the density filter: indexed material should change future agent judgment ^c20260729-326u
- [DC] `Index.Line` is its atomic presentation unit ^c20260729-169u
- [CT] every `Index.Line` is intended to link its dense statement to supporting touch evidence; a missing or unresolvable link is a grounding POI, not loss of index membership ^c20260729-95u
- [PR] `Chat.Surface` is the preferred evidence source because it carries the richest Hugentic context ^c20260729-322u
- [CT] support is not restricted to chat when another surface carries direct `User.Touch` ^c20260729-139u
- [DC] the index is the default first-line context for agent action over historical touch ^c20260729-242u
- [DC] each entry is both a trace of previous alignment and a portal to deeper evidence ^c20260729-207u
- [CT] curation does not transfer authority from the underlying `User.Touch` ^c20260729-82u
- [FR] missing index coverage never blocks agent action or direct evidence retrieval ^c20260729-312u
- [DC] `Touched.Surface.Index` is the category of surfaces that materialize this system ^c20260729-175u
- [EX] the Markdown `Agentos.Index.System` is its first implementation ^c20260729-300u
- [PR] by contextualizing prior touched work, the index makes alignment reusable without requiring the user to restate it ^c20260729-328u

****

## Support.Set

- [DF] `Support.Set` is the evidence bundle linking a grounded statement to exact `Touched.Data` materialized on one or more `Touch.Authority.Surface` instances ^c20260729-266u
- [CT] its references address observable data or durable coordinates on those surfaces, never the underlying `User.Touch` directly ^c20260729-116u
- [CT] a support set may reference one or several authority surfaces while preserving the provenance of each member ^c20260729-64u
- [DC] a nonempty resolvable `Support.Set` makes an `Index.Line` a second-order touched projection of its referenced data ^c20260729-186u
- [DC] `Chat.Support.Set` is presently the only implemented specialization because a qualifying `User.Turn` is the only registered `Touch.Authority.Surface` ^c20260729-165u
- [CT] that implementation constraint does not restrict the general support model to chat ^c20260729-141u
- [CT] equivalent `Support.Set` contents may stand behind distinct `Support.Reference` edges; evidence equality does not make those references identical ^c20260802-117u

****

## Touched.Surface.Index

- [DF] `Touched.Surface.Index` is the category of surfaces that materialize `Touched.Index` through `Index.Line`s ^c20260729-274u
- [CT] surface membership does not require every live line to be grounded; missing or unresolvable support leaves the line live under `Index.Presumption` and creates a grounding POI ^c20260729-140u
- [DC] each grounded line is second-order `Touched.Data` linked to first-order touched data on its authority surfaces ^c20260729-208u
- [CT] an indexed surface is a curated projection, not a `Touch.Authority.Surface` merely because it contains touched data ^c20260729-70u
- [DC] touch provenance remains at the authority surfaces referenced by each line's support set ^c20260729-246u
- [FR] a line may restate its supporting data or contextualize why that data supports the indexed statement ^c20260729-304u
- [DC] member surfaces vary independently by attachment point, review, format, and ordering ^c20260729-220u
- [EX] `Agentos.Index` attaches lines to concepts, `Chat.Index` attaches them to chats, and `Skw.Agendix` attaches them to `Skw.Annotation` instances ^c20260802-193u
- [DC] `Reviewed.Cite.Closure` governs citation across members regardless of which member contains a reviewed line ^c20260729-172u

****

## Reviewed.Content

- [DF] `Reviewed.Content` is the protocol state established when materially equivalent content is presented and later explicitly approved by the user ^c20260729-265u
- [CT] the state records protocol completion, not whether the user read, understood, remembered, or evaluated the content ^c20260729-154u
- [CT] review is distinct from `Touched.Authority`, which derives from the content's `Support.Set` rather than approval of its wording ^c20260729-134u
- [DC] review implies touch when the approval is a qualifying authority-surface edition that enters the content's support set ^c20260729-231u
- [DC] a qualifying approval `User.Turn` in `Chat.Support.Set` is the current realization of that review evidence ^c20260729-188u
- [CT] review does not certify factual truth or support strength ^c20260729-133u
- [DC] review partitions grounded touched-index content into touched-unreviewed and touched-reviewed strata; an ungrounded live line remains index content under `Index.Presumption` rather than acquiring touched authority ^c20260729-232u
- [DC] `Verbatim.User.Gated` is presently the sole mechanism that produces `Reviewed.Content` ^c20260729-178u

****

## Reviewed.Cite.Closure

- [DF] `Reviewed.Cite.Closure` is the citation invariant over `Reviewed.Content`: a reviewed line may cite only reviewed lines, so a reviewed line's transitive cite-closure is entirely reviewed ^c20260723-42u
- [CT] one forbidden edge: reviewed→unreviewed; reviewed→reviewed and any unreviewed→anything are legal ^c20260723-23u
- [DC] the boundary is verbatim review specifically: a cite depends on wording, so `Edition.Trigger.User.Gated` (edit-event approval, wording unseen) does not count as reviewed for this rule ^c20260723-38u
- [DC] CPU-lintable per `User.Gate`: resolve each cite's target and check its support set for the review turn; a reviewed line citing an unreviewed target is a linter finding ^c20260723-26u
- [DC] the check is local: a line cite quotes the target verbatim including its anchor, so resolving that embedded anchor reaches the support set directly — no container walk ^c20260723-39u

****

## Index.Edition.Turn

- [DF] `Index.Edition.Turn` is an assistant turn that presents a proposed index edition for explicit user approval ^c20260729-258u
- [PR] its presentation helps the user distinguish added, modified, removed, and unchanged content before approving ^c20260729-337u
- [DC] it identifies the landing surface, ontology target, edit operation, and `Edition.Approval.Token` ^c20260729-215u
- [DC] a modification may present current content under `Before` and proposed content under `After · Verbatim` ^c20260729-185u
- [DC] an addition needs only proposed content, while a removal needs only current content ^c20260729-193u
- [FR] unchanged context may be shown when it improves interpretation and omitted when it adds noise ^c20260729-319u
- [CT] proposed landing lines appear undecorated somewhere in the turn so materially equivalent content can be found without interpreting the presentation layout ^c20260729-126u
- [CT] the presentation format is not gate syntax; no heading, ordering, fence language, or diff notation is required by `Line.Verbatim.Gate` ^c20260729-149u
- [FR] agents may evolve the rendering while preserving clear targets, change distinctions, and approval commands ^c20260729-306u

****

## Line.Verbatim.Gate

- [DF] `Line.Verbatim.Gate` is the per-`Index.Line` certificate that explicit user approval followed presentation of materially equivalent line content ^c20260729-260u
- [DC] its dossier connects the landed line, proposal turn, and approval turn through `Edition.Approval.Token` evidence in `Support.Reference.Metadata` ^c20260729-218u
- [DC] the proposal turn must contain the token and the proposed line before a user turn explicitly approves that token ^c20260729-245u
- [CT] the checker searches the proposal turn without requiring any `Index.Edition.Turn` presentation format ^c20260729-144u
- [DC] the checker requires sufficient evidence that the proposed and landed lines preserve materially equivalent wording rather than byte-for-byte identity ^c20260729-238u
- [CT] presentation differences irrelevant to attention certification do not break the gate; the checker applies a deterministic equivalence policy ^c20260729-125u
- [DC] the gate passes when content correspondence is sufficient and token approval follows its presentation ^c20260729-240u
- [CT] the gate certifies protocol events, not whether the user read, understood, remembered, or evaluated the line ^c20260729-146u
- [DC] a satisfied gate gives the line the `Reviewed.Content` protocol state ^c20260729-189u
- [CT] materially significant wording changes break the gate until equivalent content is presented and explicitly approved again ^c20260729-118u
- [DC] one token may approve several lines while each line retains its own independently checkable gate ^c20260729-222u
- [DC] the gate remains line-local and re-checkable from the line's own support reference ^c20260729-241u
- [PR] format-insensitive comparison protects `User.Attention` from reapproval caused only by presentation noise ^c20260729-333u

****

## Edition.Approval.Token

- [DF] `Edition.Approval.Token` is the mechanism that evidences `Verbatim.User.Gated`: the agent presents materially equivalent line content plus a copy-pasteable token, and the user explicitly approves that token on a later user turn ^c20260726-36u
- [DC] materially equivalent proposed lines appear in an assistant turn — that explicitness is the contract; the token binds them, it does not carry them ^c20260726-25u
- [DC] the token is an opaque nonce: its identity, not its content, does the linking work ^c20260726-32u
- [RJ] the token is not a content hash — deriving it from the edition burdens the producer for no gain, since integrity comes from locate-then-compare, not from the token itself ^c20260726-49u
- [DC] the approving user turn is the review turn entering the line's `Chat.Support.Set`, so the token is how `Reviewed.Content` is evidenced rather than merely asserted ^c20260726-27u
- [DC] the token lives in the line's `Support.Reference.Metadata` — the current external Anchory dossier realization of the audit trail, recoverable from the landed line alone ^c20260726-34u
- [DC] it binds a proposal turn holding materially equivalent line content, the later approval turn carrying the explicit approval command, and the file line whose support reference carries the token; resolving that reference reaches all three ^c20260726-23u
- [DC] the check is flexible over the conversation: materially equivalent landed content may appear in any assistant turn that carries the token and precedes the explicit approval turn, so discussing or re-showing across turns does not break the audit ^c20260726-29u
- [CT] material comparison excludes trailing support references; the proposal may show a placeholder while the landed line carries the minted reference ^c20260726-19u
- [DC] the agent mints a fresh token when the edition's wording changes and reuses it while the wording holds, so every turn bearing a token carries the same edition — the discipline that keeps the flexible check unambiguous without encoding content in the token ^c20260726-26u
- [DC] the token rides `User.Command::Approve` as its Explicit arg: `::approve <token>` is the canonical form, making one user turn both the workflow transition and the review evidence, with the agent pre-filling the token under the resolved copy-pasteable rendering ^c20260726-35u
- [DC] the token is optional and its presence is the upgrade — a bare `::approve` (contextual foreground target) stays edit-event approval (`Edition.Trigger.User.Gated`), while `::approve <token>` binds the reviewed wording and yields `Reviewed.Content` ^c20260726-33u

****

## Touched.Support.Network

- [DF] `Touched.Support.Network` is the network relating `Index.Line`s across touched index surfaces to supporting data on `Touch.Authority.Surface` instances ^c20260729-273u
- [DC] its edges have the form `Support.Set` ↔ `Support.Reference` ↔ `Index.Line` ^c20260729-219u
- [DF] `Support.Reference` is the abstract link connecting one line content to its `Support.Set` ^c20260802-189u
- [CT] different line contents never share a `Support.Reference`, even when their support sets are equivalent ^c20260802-115u
- [DC] repeated materializations of the same line content may retain the same `Support.Reference` across touched index surfaces ^c20260802-167u
- [CT] `Support.Reference.Metadata` may describe that link but is not the link itself ^c20260729-51u
- [DC] an authority surface holds the first-order touched data while an index surface holds its grounded line ^c20260729-195u
- [DC] the network is dynamic: nodes and edges change as authority surfaces and their grounded projections evolve ^c20260729-244u
- [DC] touched surfaces hold the live cut, source surfaces preserve their evidence, and surface history preserves prior network states ^c20260729-247u
- [DC] extending support for unchanged line content evolves its existing evidence relationship; changing the content requires support reevaluation and a new `Support.Reference` ^c20260802-151u
- [PR] `Support.Set` is one line content’s local evidence view; `Touched.Support.Network` is the global object those views compose ^c20260802-203u
- [DC] `Anchory.Anchor` currently realizes `Support.Reference`: it is the link, while its application record carries the support set and reference metadata ^c20260802-137u

### meta

- aliases: `Index.Support.Network`

****

## Live.Index.Line

- [DF] `Live.Index.Line` is an `Index.Line` present in the current live cut of a `Touched.Surface.Index` ^c20260729-261u
- [CT] only a live index line conditions current reasoning through `Touched.Authority` or `Index.Presumption` ^c20260729-123u
- [DC] a `Grounded.Index.Line` carries touched authority while an `Ungrounded.Index.Line` carries index presumption ^c20260729-181u
- [DC] conflict involving a live line becomes a `Point.Of.Interest` while the line retains its current standing ^c20260729-202u
- [FR] gated reconciliation may keep, ground, modify, add, replace, remove, reorganize, or leave the relevant index material unresolved ^c20260729-310u
- [CT] demotion is only one possible reconciliation result ^c20260729-84u

****

## Demoted.Index.Line

- [DF] `Demoted.Index.Line` is a historical `Index.Line` whose live standing was overruled by later `Touched.Data` and retired through gated reconciliation ^c20260729-255u
- [CT] an overrule POI does not demote the line while it remains part of the live index ^c20260729-72u
- [CT] demotion changes index participation, not the touched status of supporting source data ^c20260729-83u
- [DC] surface history preserves the former line, its support state, and the later index edition that displaced it ^c20260729-233u
- [PR] demoted lines trace evolution of the indexed model without acting as current guidance ^c20260729-332u
- [CT] historical recoverability does not restore `Index.Presumption` or live standing ^c20260729-106u

****

## Index.Line

- [DF] `Index.Line` is the atom of `Touched.Surface.Index`: one typed content statement whose support standing is evaluated through its `Support.Reference` ^c20260802-186u
- [DF] an `Index.Line`’s content is its `Line.Type` and body; trailing support references are links and do not belong to that content ^c20260802-192u
- [CT] when an `Index.Line` is attached to an `Index.Block`, block membership supplies context the line need not repeat ^c20260802-136u
- [DC] repeated materializations of identical typed content are the same line for deterministic identity ^c20260802-166u
- [CT] identical line content may carry different meaning through different attachments; this uncommon contextual distinction requires semantic judgment rather than deterministic identity linting ^c20260802-123u
- [PR] lines within a block aim for semantic orthogonality: each contributes a distinct dimension with minimal overlap among sibling lines ^c20260729-340u
- [CT] a line may be fully intelligible by itself, but standalone completeness is not required ^c20260729-60u
- [DC] the line is the unit of grounding, approval, audit, and drift checking ^c20260729-243u
- [DF] `Grounded.Index.Line` is an `Index.Line` whose support reference resolves to a nonempty `Support.Set` linking it to `Touched.Data` ^c20260729-256u
- [DF] `Ungrounded.Index.Line` is a live `Index.Line` whose touched-data support is missing or unresolvable ^c20260729-275u
- [DC] an ungrounded line remains index content and carries `Index.Presumption`; missing grounding is debt, not a deletion trigger ^c20260729-196u
- [DC] each line carries a `Line.Type` classifying its act ^c20260729-209u
- [CT] approval is a member-surface invariant rather than a requirement for `Index.Line` membership itself ^c20260729-73u
- [EX] on a `Verbatim.User.Gated` surface, the support set includes a qualifying approval `User.Turn` through the current `Chat.Support.Set` specialization ^c20260729-299u
- [DC] the current Markdown implementation materializes the line's `Support.Reference` as a trailing `Anchory.Anchor` ^c20260729-239u
- [PR] support references, support sets, and authority data ground the line without replacing the semantic context supplied by its block ^c20260729-349u

****

## Index.Presumption

- [DF] `Index.Presumption` is the defeasible decision weight carried by a live `Ungrounded.Index.Line` because it occupies a gated index surface ^c20260729-259u
- [PR] gated placement makes the line likely to reflect prior user interaction even when its touched-data support is missing ^c20260729-334u
- [CT] index presumption is not `Touched.Authority` and does not certify truth, consistency, or currentness ^c20260729-107u
- [DC] it conditions `Open.Inference` unless stronger applicable evidence overrules it ^c20260729-214u
- [CT] the agent must reason about its applicability rather than obeying it mechanically ^c20260729-142u
- [CT] missing grounding is debt, not a deletion or demotion trigger ^c20260729-119u
- [DC] conflict between index presumption and applicable `Touched.Data` becomes a `Point.Of.Interest` ^c20260729-201u
- [DC] resolving that conflict on the live index is a separate gated reconciliation action ^c20260729-230u

****

## User.Attention

- [DF] `User.Attention` is the scarce human capacity that a Hugentic workflow may request but cannot directly observe ^c20260729-276u
- [DC] a workflow creates an attention opportunity by presenting bounded material and requiring an explicit user response ^c20260729-190u
- [CT] protocol evidence may certify presentation and response, never that the user read, understood, remembered, or evaluated the material ^c20260729-127u
- [PR] Hugentic workflows must economize `User.Attention` as a scarce resource ^c20260729-320u
- [EX] format-insensitive verbatim comparison avoids additional approval checkpoints for immaterial presentation differences ^c20260729-298u
- [DC] `Verbatim.User.Gated` allocates an explicit attention checkpoint before wording lands on a gated surface ^c20260729-177u
- [EX] `Index.Agendix` avoids per-line attention checkpoints by remaining unreviewed and grounding its content through provenance ^c20260729-293u

****

## Skw.Touched.Index

- [DF] `Skw.Touched.Index` is the `Touched.Surface.Index` member attached to `Skw.Annotation`s: `Index.Line`s riding annotations on generated surfaces — file, module, region, construct ^c20260717-27u
- [DC] one mixed surface: gated and ungated lines share the place — a line is gated iff its support set holds the gate-typed turn (`Turn.Type::<Surface>.Gate`); the split is computed, not geographic ^c20260717-18u
- [DF] `Skw.Appendix` and `Skw.Agendix` are its computed strata — the gated and the ungated lines: the appendix and agendix of a block, where the block is the annotation — same mechanics, no file split ^c20260717-26u
- [DC] promotion is a state change, not a relocation: a line passes the gate where it stands — the gate turn joins its set; nothing moves ^c20260717-20u
- [DC] two worlds meet at the annotation: the skw development stack reads it to generate, judge, and evolve the surface; the touched lines ground to the `Chat.Surface` — the user-grounded part of that context ^c20260717-23u
- [DC] syntax: `--supp <line> ^<anchor>` — the construct's own touched lines: the annotation is its own block, deps (`--from`/`--quote`) bind its content while supps ground the annotation itself ^c20260719-34u

****

## Skw.Network

- [DF] `Skw.Network` is the graph of annotated surfaces linked by the relationships the skw system defines between them ^c20260715-25u
- [DC] relationships are explicit or implicit: explicit ones are the declared links a `Skw.Ann.Dependency` carries; implicit ones are derived by the system, such as support-set intersection between chat anchors ^c20260715-18u
- [DC] the network is computed from consumer-side declarations — a target never registers its dependents; followers are derived, so an imported surface stays ignorant of its importers ^c20260715-20u
- [PR] the network's job is notification, not judgment: when a surface changes, the `CPU.Program` notifies every surface the network links to it — a purely mechanical fan-out along the edges ^c20260715-31u
- [DC] an `Agentic.Program` interprets each notification: whether the change is benign or a real change to propagate is a semantic verdict only the agent carries ^c20260715-16u

****

## POI.Line

- [DF] `POI.Line` is a grounded `Index.Line` stating one reviewable maintenance situation about one or more indexed lines ^c20260804-12u
- [DC] it owns its own `Support.Reference` and `Support.Set` for the maintenance claim it makes ^c20260804-13u
- [DC] its support set is constructed from qualifying user turns reached through the subject lines' support sets and any additional authority evidence selected for the claim ^c20260804-11u
- [CT] references to subject lines identify the targets being evaluated without forming a general line-to-line dependency or provenance network ^c20260804-14u
- [EX] “line X is not well supported” and “lines X and Y appear contradictory” are `POI.Line` forms ^c20260804-15u
- [CT] its grounded standing does not make its evaluation indisputable or prescribe how the situation must be resolved ^c20260803-56u

****

## Index.HEAD.Reconciliation

- [DF] `Index.HEAD.Reconciliation` is the POI-driven maintenance of ordinary model-line coverage across `Chat.Index.Delta`, `Chat.Index.HEAD`, and `Projects.HEAD` ^c20260804-16u
- [DF] `Projects.HEAD` is the collection of independently maintained Project HEADs that may consume shared Chat HEADs ^c20260804-18u
- [FR] any participating surface may materialize an ordinary model line first; reconciliation does not impose a transactional writing order ^c20260804-19u
- [CT] an ordinary `Chat.Index.HEAD` line should eventually occur exactly in a `Chat.Index.Delta`; missing Delta coverage raises a `POI.Instance` ^c20260804-17u
- [CT] an ordinary Project HEAD line should eventually occur exactly in at least one registered supporting `Chat.Index.HEAD`; missing Chat HEAD coverage raises a `POI.Instance` ^c20260803-57u
- [CT] upward inclusion is selective: a Delta line need not enter its Chat HEAD, and a Chat HEAD line need not enter every Project HEAD ^c20260804-20u
- [CT] Delta- and HEAD-coverage requirements apply to ordinary model lines; `POI.Line` follows its maintenance lifecycle ^c20260804-22u
- [PR] writing on any participating surface creates reconciliation opportunities in both directions, and agents materialize the same line on missing surfaces when appropriate ^c20260804-21u
- [RJ] reconciliation materializes lines across surfaces rather than moving them; chronological Delta occurrences remain in place ^c20260804-23u
- [CT] coverage is an eventual invariant enforced through POIs, never a write-time development constraint ^c20260804-24u
