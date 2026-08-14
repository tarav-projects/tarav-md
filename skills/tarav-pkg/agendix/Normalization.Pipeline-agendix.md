****

## Normalization.Pipeline/Agendix

- [DF] a `Native.Surface.Normal.Model` is the deliberately small host-language representation produced from raw source before subsystem-specific normalization ^c20260812-1u
- [CT] each host language owns its own native normal model; the shared native layer stops at tiny primitives such as source spans and diagnostics ^c20260812-2u
- [PR] a native normal model grows only when a current subsystem needs the new fact ^c20260812-3u
- [DC] `agentos surfaces normalize --file <path>` exposes a file's native model; `--language` overrides extension inference, unresolved inference errors, and `--json` emits the complete model ^c20260812-4u
- [DF] a `Raw.Normalizer` is a contract between a `Raw.Model.Version` and a `Normal.Model.Version` — the pair it was written against, not an open mapping from whatever raw arrives ^c20260728-46u
- [PR] old normalizers do not become useless when the `Normal.Model` moves: bumping the normal side still requires reparsing old raw, so the capability to read every archived `Raw.Model.Version` is permanent ^c20260728-50u
- [DC] each model carries a version — the raw side and the normal side both — and assigning one is itself a normalization act ^c20260728-34u
- [DF] `Raw.Model.Version` is an internal property of the normalization pipeline: it says these raws are interchangeable *for my normalizers*, never that a provider's format is objectively X ^c20260728-44u
- [DC] the version targets the `Raw.Model`; a harness or CLI version is a hint recorded on the class, never the identity — several releases routinely share one format ^c20260728-43u
- [CT] a normalizer is fenced against the whole `Raw.Model` it consumes, not per fragment: given a stable `Raw.Model.Version` its fragment is stable by construction, and partial acceptance would emit a silently incomplete model ^c20260728-20u
- [DC] the fence is set membership over `Raw.Model.Version`s, and a class is never removed from a normalizer's set — dropping one abandons archived raw the retention design promised to keep readable ^c20260728-42u
- [CT] raw versioning is independent of the `Normal.Model` — deciding whether a provider's format changed is answerable from raw alone, and must stay answerable while the normal side is mid-change ^c20260728-23u

****

## Normalization.Pipeline/Agendix/Version.Classifier

- [DF] `Version.Classifier` maps any `Raw.Model` to a `Raw.Model.Version` or to `NoVersionRegistered` — a total function whose ignorance is a named outcome, not an error ^c20260728-45u
- [CT] it establishes no relationships between versions: no ordering, no compatibility graph — those are settled when the system is updated, not by the classifier ^c20260728-22u
- [FR] it may classify by any means — reading a CLI version cheaply, comparing schemas directly, or built heuristics — and the strategy is free to differ per provider ^c20260728-49u
- [EX] a default Open Classifier assigning one version to every `Raw.Model` is legitimate: it reproduces unversioned behaviour, so adopting the concept costs nothing and the classifier is tightened where experience demands ^c20260728-47u
- [DC] a wrong equivalence is a `Version.Classifier` defect, not a data condition: it leaked a version, so the heuristic is improved — which is what makes auto-registration safe ^c20260728-31u
- [DC] on an unrecognized release the schema is heavy-validated: passing auto-registers the version into the range of the normalizers handling the old `Raw.Model`, failing raises a hard POI ^c20260728-39u
- [PR] the classifier is dumb and the judgement lives in the update act — code is dumb but trustworthy, agents are smart but need strict grounding ^c20260728-53u

****

## Normalization.Pipeline/Agendix/Raw.Model.Namespace

- [DC] the `Raw.Model.Namespace` is realized by accumulating every path and value type observed across raw artifacts, so a new path or a changed type becomes detectable ^c20260728-41u
- [DC] its history is a schema map — how the namespace evolves — and each significant change is what obliges a normalizer to be extended or a new one written ^c20260728-37u
- [CT] significance is defined against the normalizer, never against the raw: a new path nothing reads is coverage debt, while a change to a path something reads is a version boundary ^c20260728-24u
- [CT] the namespace is per provider; only the machinery that accumulates, types, and diffs it is provider-neutral ^c20260728-27u
- [DC] prevalence is measured per CLI version, taking format stability within a version as the working assumption — this is what separates the two signals, since within a version prevalence measures optionality and across versions a step measures format change ^c20260728-40u
- [CT] the namespace history supplies data and decides nothing: the developers of the normalizers and their versioners read it and declare the boundaries ^c20260728-26u
- [PR] the surface is therefore judged on completeness and legibility rather than on being right — a threshold is a lens its reader applies, not a property baked into the data ^c20260728-54u
