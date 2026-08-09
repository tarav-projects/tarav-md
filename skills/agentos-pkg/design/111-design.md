> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Agentos.Tournament

- [DF] `Agentos.Tournament` is the Agentos subsystem that accumulates comparative evaluations of arbitrary items by running matches over sets of them and recording every outcome ^c20260806-47u
- [DC] one tournament is one `Tournament.Definition` and its accumulated `Tournament.Match` records over one player pool ^c20260805-21u
- [CT] the system is domain-blind: it records and serves verdicts and never interprets what a `Tournament.Player` represents ^c20260805-22u
- [CT] the durable object is the append-only verdict record; any ranking over a pool is a read-side fold, never a stored value ^c20260805-23u
- [DC] a fold over accumulated verdicts enumerates its players from those verdicts, since the engine holds no declared pool ^c20260806-43u
- [PR] enumerating from verdicts is what keeps a player's accumulated history readable after it leaves the definition's pool ^c20260806-44u
- [CT] every completed match is recorded, including outcomes that score no player ^c20260805-24u
- [PR] the weak tail is the product — consistent low outcomes locate items worth attention, and no single item's score is the point ^c20260805-25u
- [PR] flat accumulation is a finding rather than the absence of one: it says the measurement did not discriminate ^c20260806-136u
- [RJ] the engine does not diagnose why a pool failed to separate; whether the question, the judge, or the pool itself is at fault is a read over the records ^c20260806-137u
- [PR] statelessness at the match boundary is what makes runs parallel, reproducible, and cacheable ^c20260805-26u
- [CT] its output is `Accountable.Assertion` evaluation-record material: confidence, never authority ^c20260805-27u
- [FR] a fold over accumulated verdicts may serve as an `Improvement.Loop` score; nothing in the engine makes that a default ^c20260809-105u
- [RJ] it does not own domain `POI.Class`es or emit domain findings; consumers read the accumulated records and mint their own POIs ^c20260805-28u
- [RJ] it does not decide comparability, pool membership, or judging criteria; `Tournament.Definition` does ^c20260805-29u

****

## Tournament.Definition

- [DF] a `Tournament.Definition` is the consumer-owned specification of one tournament: the question judged, the pool it ranges over, and how a `Tournament.Player` presents itself to a judge ^c20260806-5u
- [CT] pool scope belongs to the definition's identity — the same question over a different pool is a different tournament ^c20260805-31u
- [PR] comparability is the definition's burden: a pool is well formed when its question can discriminate between any two of its players ^c20260805-32u
- [DC] the rendered match prompt is self-contained, carrying everything a judge needs to decide without external lookup ^c20260805-33u
- [CT] the definition presents one player at a time and never the match; `Agentos.Tournament` composes those presentations without interpreting them ^c20260806-6u
- [PR] refusals scattered across a pool indict the definition rather than its players ^c20260805-35u
- [CT] a verdict is interpretable only against the definition that produced it; the records alone do not carry what an ordering licenses ^c20260808-48u
- [RJ] the engine does not validate that a match was well designed — a poorly framed question produces clean records and an empty reading ^c20260808-49u
- [PR] the recorded definition digest is what keeps that reading recoverable: the exact snapshot behind any verdict can be reopened ^c20260808-50u
- [RJ] a definition does not name winners, thresholds, or what is done with the accumulated result ^c20260805-36u

****

## Tournament.Player

- [DF] a `Tournament.Player` is one competing item in a tournament: an opaque identity and the payload its `Tournament.Definition` renders into match prompts ^c20260805-37u
- [CT] the system stores identity and payload without resolving what the player represents ^c20260805-38u
- [DC] player identity is stable across every match of its tournament, so records accumulate against one competitor ^c20260805-39u
- [CT] the same underlying object entered under two definitions is two players; records do not aggregate across tournaments ^c20260805-40u
- [PR] refusals clustered on one player are a sharper finding than a low score — no judge could evaluate it at all ^c20260805-41u
- [RJ] a player carries no domain meaning into the system; consumers own the mapping between players and their objects ^c20260805-42u

****

## Tournament.Control

- [DF] a `Tournament.Control` is a consumer-supplied player carrying a declared expected standing, present to calibrate the instrument rather than to measure the pool ^c20260806-129u
- [DC] the declared bands are high and low: a control is expected to converge toward the top or toward the bottom across many matches ^c20260806-130u
- [RJ] there is no middle band; mid-pack is where noise lives, so a middle expectation is not falsifiable at any affordable volume ^c20260807-0u
- [FR] a definition may place a control among the players it supplies rather than rely on the engine's mechanism ^c20260809-164u
- [CT] controls are held apart in the read: folded into the pool, a low control sits in the weak tail looking exactly like a finding ^c20260806-134u
- [PR] a control converging to neither band is the instrument reporting on itself ^c20260806-135u
- [RJ] declining the engine's mechanism is not declining calibration; a read over the records remains evidence about the instrument ^c20260809-165u

****

## Tournament.Control::Injected

- [DF] a `Tournament.Control::Injected` is a control the engine draws from a pool and substitutes into a match the definition did not place it in ^c20260809-166u
- [DC] the control hook returns the pool the engine draws from, so which control appears in a match stays engine work ^c20260807-1u
- [DC] the engine substitutes one control for one pool player at a consumer-set rate, and never more than one per match ^c20260806-131u
- [CT] substitution precedes match identity, so a match carrying a control is a different match from the one without ^c20260806-132u
- [DC] the verdict records which of its players were injected controls and the band each declared ^c20260809-167u
- [CT] injection assumes interchangeable players: where a definition builds each match as readings of one subject, replacing one reading with an unrelated one voids the match rather than calibrating it ^c20260809-168u
- [PR] a definition whose players are not interchangeable calibrates from inside its own match construction instead ^c20260809-169u

****

## Tournament.Hook

- [DF] a `Tournament.Hook` is a named function a `Tournament.Definition` supplies and the engine calls at a fixed point to obtain a consumer-owned part of the match ^c20260805-43u
- [DC] the declared hooks supply the match players, the player presentation, the match identity, and the consumer verdict slot ^c20260806-11u
- [CT] hooks return values and never perform effects; spawning, storing, and the engine's own randomizations stay engine-side ^c20260806-127u
- [FR] a definition may choose which players meet however it likes, including randomly; the engine randomizes only presentation order and control substitution ^c20260806-128u
- [DC] the match-players and match-identity hooks are required and have no default; every other hook defaults, so a definition supplies only what its domain forces ^c20260806-21u
- [DC] each call to the match-players hook yields the players of one match, and the definition chooses how many ^c20260806-48u
- [DC] the hook may decline to supply another match, ending a run before the caller's requested match count ^c20260806-14u
- [DC] pairing strategies live in an importable library a definition may call, never in the engine ^c20260806-15u
- [PR] keeping pair choice consumer-side is what lets a pool be unbounded, computed, or streamed rather than enumerated up front ^c20260806-16u
- [CT] identity and the `Match.Verbatim` hash are separate mechanisms: identity is required and consumer-supplied, while the hash is engine-added evidence of what ran ^c20260806-22u
- [FR] a consumer may adopt the verbatim hash as its identity, but nothing in the engine makes that a default ^c20260806-23u
- [CT] the engine validates a hook's return before acting on it ^c20260805-48u
- [DC] hook definitions are snapshotted per tournament, and every match executes the snapshot rather than the live definition ^c20260805-49u
- [PR] snapshotting keeps accumulation honest: a definition edited mid-tournament would silently make later verdicts incomparable with earlier ones ^c20260805-50u
- [CT] hook purity is verified after each call rather than trusted ^c20260805-51u
- [RJ] hooks are not an orchestration extension point; running, retrying, and aggregating matches are engine and caller concerns ^c20260805-52u
- [RJ] a hook does not author the whole match prompt; presentation is per player and the surrounding frame stays engine-owned ^c20260806-10u
- [RJ] the engine holds no pool and enumerates no pairs; declaring a pool up front is not a precondition for running matches ^c20260806-17u

****

## Tournament.Match

- [DF] a `Tournament.Match` is one evaluation of a set of players against its tournament's question, run by one `Tournament.Judge` in one fresh context ^c20260806-49u
- [DC] match arity is chosen per match by the `Tournament.Definition`; the engine imposes no size and never picks one ^c20260806-50u
- [PR] arity is the resolution knob — a larger match buys more comparisons per judge run, and where that stops paying against a judge's discrimination is empirical rather than designable ^c20260806-51u
- [DC] a match carries no state from any other match ^c20260805-54u
- [DC] match identity is an opaque string supplied by the consumer; the engine requires it and never computes one ^c20260805-55u
- [FR] the consumer decides which content changes make a new match and which do not ^c20260805-56u
- [DC] presentation order is randomized per run and the order actually run is recorded ^c20260805-59u
- [DC] order randomization is default engine normalization rather than `Tournament.Definition` work ^c20260805-60u
- [PR] randomized order neutralizes position bias across repeated runs, so the defense is statistical and needs run volume to hold ^c20260805-61u
- [FR] the same match may be run repeatedly to gather independent verdicts; whether to reuse a prior run is the consumer's choice ^c20260805-62u
- [CT] a match either completes with a `Tournament.Verdict` or fails to run, and a failed run produces no match record ^c20260805-63u

****

## Match.Verbatim

- [DF] a `Match.Verbatim` is the exact rendered text handed to the judge for one run of a `Tournament.Match`, recorded by hash as cheap evidence of what ran ^c20260805-87u
- [DC] the engine composes the `Match.Verbatim` from the consumer's player presentations and its own frame: the question, the position labels, and the answer contract ^c20260806-7u
- [DC] it is rendered from one `Match.Template`: the complete parameterized description of what that run showed its judge ^c20260809-10u
- [DC] the template's parameters are the verbatim's components — the `Match.Brief`, one `Player.Presentation` per player, the `Match.Footnote.Template`, and the order they were presented in ^c20260809-11u
- [DC] the `Match.Brief` is the definition's judge-facing prose: the question and the criteria under it ^c20260809-12u
- [DC] a `Player.Presentation` is one player as its definition rendered it, and is the only part of the verbatim a consumer authors per player ^c20260809-13u
- [DC] the `Match.Footnote.Template` is the engine's trailing frame before its per-run values are bound: the ranking instruction and the submission command ^c20260809-14u
- [CT] position labels are engine-owned frame interleaved between the presentations rather than trailing them, so they belong to neither the brief nor the footnote ^c20260809-15u
- [PR] parameterizing is what makes the parts separately storable — each component is written once and referenced, while the template holds the binding that made one run ^c20260809-16u
- [PR] a template detaches the verbatim from the code that produced it: reassembly needs a renderer that reads templates, not the engine version that ran the match ^c20260809-17u
- [PR] engine-owned framing is what keeps position decoding sound — a consumer free to label the candidates could silently invert every verdict it recorded ^c20260806-8u
- [CT] the verbatim hash is run evidence and not identity; it varies per run because presentation order is randomized ^c20260805-58u
- [CT] the verbatim is derived rather than stored: it is reassembled from its template and checked against the recorded hash ^c20260809-18u

****

## Match.Template

- [DF] a `Match.Template` is the complete parameterized description of one `Match.Verbatim`, structured so a renderer can rebuild that verbatim without the code that first produced it ^c20260809-19u
- [DC] it is data rather than code: no engine version needs to survive for an old verdict to rebuild ^c20260809-20u
- [DC] it names its components by content address rather than inlining them, so the template stays small and its components dedup across matches ^c20260809-21u
- [DC] its sections stay structurally distinct and each records which side supplied it, the definition or the engine ^c20260809-22u
- [PR] origin-marked sections are what make drift attribution mechanical — a reworded question and a changed submission instruction are otherwise the same event ^c20260809-23u
- [DC] the template declares its own shape version, so a renderer knows what it is reading before it reads it ^c20260809-24u
- [CT] per-run values the verdict already carries — the ticket, the depot, the arity — are bound at render time and not restated in the template ^c20260809-25u

****

## Match.Component.Registry

- [DF] a `Match.Component.Registry` is the content-addressed store holding each distinct part a `Match.Template` names, once for a whole `Tournament.Depot` ^c20260809-26u
- [DC] a component is written under the hash of its own content, and writing one already present is a no-op ^c20260809-27u
- [DC] registration happens as a verdict is written, so no separate pass maintains the registry ^c20260809-28u
- [DC] the template is registered the same way as its components, so a verdict carries one address and that address resolves the whole run ^c20260809-29u
- [PR] dedup is what makes the store affordable at volume: one player meets many opponents, and its presentation is written once rather than per verdict ^c20260809-30u
- [CT] the registry stores only what cannot be recomputed; the `Match.Verbatim` is rebuilt on demand and never kept ^c20260809-31u
- [DC] the verdict's recorded verbatim hash is the reassembly check: rebuilding from the registered template must reproduce it ^c20260809-32u
- [PR] a component address that changes mid-tournament is the only visible sign that a player's rendering moved under an accumulating pool ^c20260809-33u
- [CT] the registry lives inside its own `Tournament.Depot`; a verdict read without it resolves to addresses rather than text ^c20260809-34u

****

## Tournament.Judge

- [DF] a `Tournament.Judge` is the agent spawned to decide one `Tournament.Match` and return its verdict ^c20260805-64u
- [DC] one judge run serves one match, and no judge carries state between matches ^c20260805-65u
- [DC] a judge answers by position rather than by player, and the engine decodes that position back through the order it ran ^c20260806-9u
- [CT] the judge is the tournament's only semantic actor; the engine around it stays a `CPU.Program` ^c20260805-66u
- [DC] a refusal requires a stated reason, so declining is an answer rather than an abstention ^c20260805-67u
- [DC] a judge submits its verdict through a command rather than by printing it, so the engine validates the answer before anything is recorded ^c20260806-62u
- [PR] submitting is what puts a contract violation in front of the judge that made it, while the context that could still fix it is alive ^c20260806-63u
- [PR] refusal rate reads as a judge metric as much as a pool metric — a rate drifting across unrelated tournaments indicts the judge prompt ^c20260805-68u
- [FR] the model, provider, and prompt behind a judge are consumer choices ^c20260805-69u
- [RJ] a judge does not rank a pool or compare beyond the players it was given ^c20260806-52u

****

## Judge.Blinding

- [DF] `Judge.Blinding` is the separation between what a `Match.Verbatim` may tell its judge and what only a reader of the accumulated verdicts may know ^c20260809-35u
- [CT] the judge-facing surface is enumerable by construction: only the `Match.Brief` and the `Player.Presentation`s carry consumer content into the prompt ^c20260809-36u
- [RJ] a judge is not told which of its players are controls, or what band each declared ^c20260809-37u
- [RJ] a judge is not told the hypothesis under test, since stating the expected direction is most of the way to producing it ^c20260809-38u
- [RJ] a judge is not told how verdicts are folded, since a stated aggregation rule invites playing one match against the fold ^c20260809-39u
- [RJ] a judge is not told that its match has run before, or what any earlier run decided ^c20260809-40u
- [PR] the boundary has a falsifiable test: content belongs on the reader side when its presence in the prompt would invalidate the verdict ^c20260809-41u

****

## Tournament.Ticket

- [DF] a `Tournament.Ticket` authorizes one submission for one run of one `Tournament.Match` ^c20260806-64u
- [DC] the engine mints a ticket and records the match's whole context before spawning, so a submission supplies only the outcome ^c20260806-65u
- [CT] a judge cannot name a match it was not given: the ticket resolves the match, and the submission never carries it ^c20260806-66u
- [DC] a rejected submission is counted on its ticket against a cap, so a judge cannot retry without bound ^c20260806-67u
- [DC] tickets are mutable staging outside the record store, so the append-only rule over verdicts stays untouched ^c20260806-68u

****

## Tournament.Verdict

- [DF] a `Tournament.Verdict` is the recorded outcome of one completed `Tournament.Match` ^c20260805-71u
- [DC] a verdict has two zones: an engine-written envelope and an opaque consumer slot, following `Bloberia.Record` ^c20260805-72u
- [DC] the envelope records the match identity, the judge, the ordering the judge returned, the presentation order actually run, and the `Match.Verbatim` hash ^c20260806-53u
- [DC] it also records the address of the `Match.Template` that produced the run, so the exact text its judge saw is reassemblable without the engine that composed it ^c20260809-43u
- [DC] it records the per-run values bound into that template which the envelope does not otherwise carry, so reassembly never depends on the environment it runs in ^c20260809-106u
- [CT] the engine stores the consumer slot and never reads it ^c20260805-74u
- [CT] slot content never shadows an envelope field; the slot carries analysis material, not a restatement of what the envelope owns ^c20260805-75u
- [CT] an outcome is either a strict total ordering of the match's players or `Tournament.Verdict::No.Contest` ^c20260806-54u
- [CT] the ordering is strict: a judge places no two players at equal rank, and equivalence emerges from orderings that disagree across repeated matches ^c20260806-55u
- [CT] pairwise comparisons are extracted from a stored ordering at read time and are never themselves stored ^c20260806-56u
- [PR] keeping the match whole is what leaves a later fold free to see which comparisons shared one judgment ^c20260806-57u
- [RJ] there is no draw outcome; equally good players converge through split records across repeated matches ^c20260805-77u
- [CT] verdicts are append-only, and a later verdict never replaces an earlier one ^c20260805-78u
- [PR] one verdict is noise; signal lives only in accumulation ^c20260805-79u

****

## Tournament.Verdict::No.Contest

- [DF] `Tournament.Verdict::No.Contest` is the outcome of a match its judge completed but declined to decide ^c20260805-80u
- [CT] it scores no player and enters no ranking fold ^c20260805-81u
- [DC] it carries a stated reason for the refusal, in the judge's own words ^c20260806-60u
- [RJ] a judge is not asked to attribute its own refusal; scattered-versus-clustered is read from the records, which already carry which players were in which refused match ^c20260806-61u
- [PR] its distribution is the read: scattered across a pool indicts the `Tournament.Definition`, clustered on one player indicts that player ^c20260805-83u
- [CT] it is a completed match record, and a match that failed to run is not a no-contest ^c20260805-84u
- [PR] it is the only outcome that evaluates the tournament rather than its players ^c20260805-85u

****

## Tournament.Depot

- [DF] a `Tournament.Depot` is one rooted directory holding every tournament's frozen definition and its accumulated records ^c20260806-25u
- [DC] the depot resolves to a canonical global location by default and accepts an explicit root ^c20260806-26u
- [DC] a depot separates `definitions/`, `records/`, `tickets/`, and `components/`: each tournament's frozen definition, its `Agentos.Bloberia` record store, the mutable submission staging, and the `Match.Component.Registry` every run was rendered from ^c20260809-44u
- [DC] tickets are swept by age rather than on completion, and a run sweeps before it mints, so no run depends on cleanup having happened ^c20260806-70u
- [CT] the sweep horizon is far longer than any match can run, which is what keeps collection from racing a live submission ^c20260806-71u
- [DC] records are namespaced by tournament, so one tournament's records are reachable without reading another's ^c20260806-28u
- [CT] `Agentos.Bloberia` owns record storage and query; the depot owns only the surrounding layout ^c20260806-29u
- [PR] namespacing by tournament is what makes listing tournaments a directory read rather than a record scan ^c20260806-30u
