****

## Normal.Model

- `Normal.Model` is a domain's canonical, JSON-serializable target model — the source-neutral standard a `Normalization.Pipeline` produces
- its `Normal.Model.Namespace` is the controlled set of paths every `Model.Fragment` targets — a datum's canonical path is the path fragments use
- normalized inward — the pipeline knows native source formats and maps into the model; sources know nothing about it
- any field may carry an `Inline.Raw.Source` — its originating raw data packaged beside the normalized value, so the neutral read and its evidence travel together; the normalized value stays canonical
- completeness is a dial, not a type — a lite ref and a full object are the same `Normal.Model` at different depth
- a `Normal.Model` may bundle operations alongside data — its fields and the operations defined over them are one model
- by analogy, a Python class bundles data attributes together with the methods over them
- an operation's declaration and its result live in the `Normal.Model.Namespace`
- executing an operation is the `Raw.Normalizer`'s job at the raw boundary — the model specifies the operation, the normalizer runs it

****

## Inline.Raw.Source

- `Inline.Raw.Source` is originating raw/native data attached inline to a `Model.Fragment` or `Normal.Model` field, beside its normalized value
- packages the neutral value and its evidence together — provenance, audit, and richness the model does not (yet) capture, recoverable in place
- arbitrarily granular — attach at any field or fragment, as fine or coarse as needed
- a normalizer can carry it through: since `Raw.Source → Raw.Normalizer → Model.Fragment`, the normalizer attaches the `Raw.Source` it read into the fragment it emits
- supplementary, never canonical — consumers read the normalized value; the inline raw is for recovery and provenance, not the primary read
- it rides at a defined path in the model namespace, so it does not break `Model.Fragment` compatibility

****

## Model.Fragment

- `Model.Fragment` is a partial, sub-shape slice of a `Normal.Model` — values populated at their canonical model paths
- structurally model-compatible: always a valid subpath of the `Normal.Model.Namespace`, preserving containment and field naming
- topological, not positional — it carries nesting and type shape, never an absolute index into a collection; placement is the assembler's
- partial by definition — an absent path means "not produced here", not "empty"
- composable — fragments over one model overlay by path; the constant-path contract makes the overlay unambiguous
- a free-standing primitive — produced from raw by a `Raw.Normalizer`, or derived from a fuller model by other transforms

****

## Raw.Normalizer

- `Raw.Normalizer` maps a `Raw.Source` to a `Model.Fragment` — the unit of data-normalization in a `Normalization.Pipeline`
- the raw boundary for data — the only stage that reads native formats or knows source structure; nothing downstream reads raw
- the data dual of `Raw.Adapter` — the normalizer maps raw data, the adapter maps raw operations
- additive and free-form — added independently, asymmetric per source kind, implemented however the native format demands
- it may read already-built model objects alongside raw as context — it still touches raw, so it stays a normalizer; a model-only step is `Normal.Assembler` work
- free granularity — it may resolve a thin slice of the source or much of the model; fragments make fine-grained normalizers cheap, they do not require them
- overlap is allowed — multiple normalizers may target the same path; a `Normalizer.Context` keeps shared raw loaded once
- carries no assembly policy — it produces a fragment and stops; need and merge are the `Normal.Assembler`'s concern

****

## Raw.Adapter

- `Raw.Adapter` maps a raw operation to a normal capability — the unit of functionality-normalization in a `Normalization.Pipeline`
- the raw boundary for functionality — the only stage that invokes native operations or knows provider structure; the capability it exposes is provider-neutral
- the functionality dual of `Raw.Normalizer` — the adapter maps raw operations, the normalizer maps raw data
- additive and free-form — added independently, asymmetric per provider, implemented however the native operation demands
- a capability that returns data delegates inward — the adapter maps the functionality, `Raw.Normalizer`s and a `Normal.Assembler` map the resulting data
- it exposes the normal capability and hides its raw dependencies — the encapsulation form of `Normal.Model.Closure`
- a `Raw.Adapter` is a `Model.Fragment` of its `Normal.Model`'s interface — it realizes only the capabilities it supports
- it carries only the configuration those capabilities need — what a capability requires is resolved at its execution boundary
- carries no assembly policy — fallback and precedence across several raw paths to one capability are the `Normal.Assembler`'s concern

****

## Normalizer.Context

- `Normalizer.Context` is a coordination surface shared across a run's `Raw.Normalizer`s — the relief valve for the repeated work their independence invites
- the pressure it answers: free granularity and independent normalizers naturally re-load, re-parse, or recompute the same source — the context lets them share that work instead
- most common use: a lazy raw cache — a normalizer asks it for a source artifact, loaded on demand, and later normalizers reuse the loaded copy
- general beyond caching: any cross-normalizer coordination for a single run can live here
- scoped to one normalization run / source set — not a cross-domain interface
- optional, not a contract — a normalizer may use it or work alone; correctness never depends on it, only efficiency

****

## Normal.Assembler

- `Normal.Assembler` processes `Model.Fragment`s into an object in the `Normal.Model.Namespace` — the integration stage of a `Normalization.Pipeline`
- named for its typical job of integrating fragments, but it can be any fragment-to-object processing
- typically the caller, not just the consumer — it runs the `Raw.Normalizer`s its target needs and holds their shared `Normalizer.Context`, so each source loads once per assembly
- owns integration — how fragments are merged, placed, and reconciled lives here, never in a normalizer
- may produce a partial or full object over the namespace — assembled depth is its choice

****

## Normal.Model.Namespace

- `Normal.Model.Namespace` is the set of canonical paths a `Normal.Model` defines — its field/structure names and where each datum lives
- the shared coordinate system of a `Normalization.Pipeline`: `Model.Fragment`s are subpaths of it, assembled objects are instances of it
- a controlled vocabulary — only paths the `Normal.Model` defines are valid; nothing introduces a path outside it
- a datum's canonical path is its address everywhere — fragments, assembled objects, and `Inline.Raw.Source` attachments all use it

****

## Normal.Model.Closure

- `Normal.Model.Closure` is the property that every stage of a `Normalization.Pipeline` outputs within the `Normal.Model.Namespace` — data is transformed, never taken outside it
- a `Raw.Normalizer` emits `Model.Fragment`s (subpaths of the namespace); a `Normal.Assembler` emits objects in the namespace — both stay inside
- one of the pipeline's constraints — closure is what makes fragments composable and the model one coordinate system
- even raw does not break it — an `Inline.Raw.Source` rides at a defined namespace path, so evidence stays inside the closure too

****

## Raw.Source

- `Raw.Source` is native, un-normalized source material a `Raw.Normalizer` reads — the left end of a `Normalization.Pipeline`
- more than file content — file metadata (size, mtime), or any native signal, counts as `Raw.Source`
- it lives in a `Raw.Model.Namespace` — the native counterpart of the `Normal.Model.Namespace`
- opaque to the rest of the pipeline — only `Raw.Normalizer`s and `Inline.Raw.Source` attachments ever hold it
- a run has many — `Raw.Normalizer`s map them; a `Normalizer.Context` coordinates loading them once
****

## Projection.Test

- `Projection.Test` evaluates a `Normal.Model` against a corpus of its assembled instances by projecting a canonical path of the `Normal.Model.Namespace` across all instances and judging the resulting column — the model is the test subject, the corpus is the evidence
- the mechanic: a canonical path carries an intended meaning; the projection shows what actually landed there after normalization; comparing the column against the intention detects meaning drift, completeness failures, and shape divergence
- the corpus is its own oracle — the test asserts agreement between column and intention, so it needs no hand-written expected outputs; any accumulated set of assembled instances serves as evidence
- the projection code is variant-free: it reads by canonical path only, with no per-source branching — needing a branch to read a value means a datum lives off its canonical path, a model failure, never a test limitation
- what to judge on a column belongs to the `Normal.Model` under test, not to the framework — the test framework never constrains the model's expressibility; typical judgments: the path resolves, absences are justified, values share one domain, relations hold within an instance and along the column across instances
- failure triage is three-way, which makes the test a convergence engine rather than a gate: an extraction defect — fix the `Raw.Normalizer`; a model gap — change the `Normal.Model` and re-normalize the corpus; a genuine source condition — document it, converting the failure into pass-with-evidence
- `Comparative.Normalization` consults the corpus as precedent while writing; `Projection.Test` consults it as oracle while validating — one corpus, two directions

****

## Under.Normalization

- `Under.Normalization` is the design failure where a `Raw.Normalizer` passes raw structure through instead of finishing the mapping — equivalent data from different `Raw.Source`s lands on different paths of the `Normal.Model.Namespace`, split by source
- resembling a raw namespace is legal — a `Normal.Model` may copy whatever shape it wants from a raw source, even adopting one source's shape wholesale and normalizing every other source to it; the failure is branching, never resemblance
- the signature: one meaning, several canonical paths, partitioned by raw source — instances from one source populate path A, instances from another populate path B, and the paths never co-occur in one instance
- the cost: a consumer must carry per-source knowledge to read the model — the cost a `Normalization.Pipeline` exists to pay once, centrally
- detection is mechanical over a corpus of assembled instances: find path pairs with disjoint populated-instance sets partitioned by source, ranked by role similarity — shared value domain, same structural position, similar name; the detector emits candidates, the meaning judgment stays with the model
- triage: one meaning — converge onto one canonical path and re-normalize the corpus; genuinely distinct meanings — document the distinction as pass-with-evidence; sometimes the meaning deserves a path neither source suggested
- raw riding along deliberately is not under-normalization — `Inline.Raw.Source` carries raw labeled as raw at a defined path; under-normalized data arrives unlabeled, posing as canonical
- `Path.Source.Split.Test` is its cheap screen — the source distribution of every path, computed in one pass, feeds the review queue the pair detection judges
- the dual of `Projection.Test`: projection judges one path across many instances; under-normalization detection judges one meaning across many paths — the same corpus serves both

****

## Path.Source.Split.Test

- `Path.Source.Split.Test` is a corpus test over a `Normal.Model`: for every path of the `Normal.Model.Namespace`, measure the distribution of `Raw.Source`s across the instances that populate it — paths populated mostly or only from one source form the review queue
- it is the cheap screen for `Under.Normalization`: a source-split path is a candidate leak, reviewed by the pair-matching detection; a source-split path with no counterpart anywhere may instead mark a meaning other normalizers silently drop
- the output is a review queue, never a verdict — source-exclusive paths are legal, since sources genuinely carry exclusive concepts
- each reviewed path gets a remembered verdict: converge it onto a shared path, or document it as source-specific by design — pass-with-evidence; without the memory the queue re-fills identically every run and the test drowns in noise
- the mostly-one-source case outranks the only-one-source case: a dominant-but-not-exclusive split can mean one normalizer converged and another only partially — a half-fixed leak
- one histogram per path in a single pass — no pairwise comparison; it scales with the namespace, not with its square

****

## Normalization.Coverage

- `Normalization.Coverage` scores how much of a `Raw.Source` a `Normal.Model` expresses — the analogue of code coverage for a `Normalization.Pipeline`, quantifiable and easily discoverable over any corpus
- unit: raw leaf fields — a raw record scores consumed leaves over total leaves; consumed means recoverable from the assembled instance, not merely visited during normalization
- aggregation makes it comparable: records aggregate into an instance score, instances average into a per-source score — sources can then be compared against each other
- the per-record-type breakdown is the actionable surface; a blended total only trends
- the target is not any fraction in particular — how much to encode is a design decision; the signal is the delta from the designed baseline, not the absolute
- score movement on recent instances is format-drift detection for free: new raw fields the `Raw.Normalizer`s do not know lower the score as they appear
- it is the expressiveness measure of the pipeline — it makes visible what raw the model chose not to say, the counterweight to convergence pressure, which alone can be satisfied by collapsing meaning into opaque blobs
