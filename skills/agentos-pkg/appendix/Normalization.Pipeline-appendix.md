****

## Normal.Model

- `Normal.Model` is a domain's canonical, JSON-serializable target model — the source-neutral standard a `Normalization.Pipeline` produces
- its `Normal.Model.Namespace` is the controlled set of paths every `Model.Fragment` targets — a datum's canonical path is the path fragments use
- normalized inward — the pipeline knows native source formats and maps into the model; sources know nothing about it
- any field may carry an `Inline.Raw.Source` — its originating raw data packaged beside the normalized value, so the neutral read and its evidence travel together; the normalized value stays canonical
- completeness is a dial, not a type — a lite ref and a full object are the same `Normal.Model` at different depth

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

- `Raw.Normalizer` maps a `Raw.Source` to a `Model.Fragment` — the unit of normalization in a `Normalization.Pipeline`
- the raw boundary of the pipeline: it is the only stage that touches native formats or knows source structure; nothing downstream reads raw
- may also take already-built model objects alongside raw (`Raw.Sources + Others → Raw.Normalizer → Model.Fragment`) — to use as context and/or modify in place (e.g. a raw-keyed cross-reference); it still touches raw, so it stays a normalizer; a model-only step is `Normal.Assembler` work
- additive and free-form — added independently, asymmetric per source kind, implemented however the native format demands
- free granularity — it may resolve a thin slice of the source or much of the model; fragments make fine-grained normalizers cheap, they do not require them
- overlap is allowed — multiple normalizers may target the same path; a `Normalizer.Context` keeps shared raw loaded once
- carries no assembly policy — it produces a fragment and stops; need and merge are the assembler's concern

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