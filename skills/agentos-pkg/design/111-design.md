> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Agentos.Tournament

- [DF] `Agentos.Tournament` is the Agentos subsystem that accumulates comparative evaluations of arbitrary items by running pairwise matches and recording every outcome ^c20260805-20u
- [DC] one tournament is one `Tournament.Definition` and its accumulated `Tournament.Match` records over one player pool ^c20260805-21u
- [CT] the system is domain-blind: it records and serves verdicts and never interprets what a `Tournament.Player` represents ^c20260805-22u
- [CT] the durable object is the append-only verdict record; any ranking over a pool is a read-side fold, never a stored value ^c20260805-23u
- [DC] a fold over accumulated verdicts enumerates its players from those verdicts, since the engine holds no declared pool ^c20260806-43u
- [PR] enumerating from verdicts is what keeps a player's accumulated history readable after it leaves the definition's pool ^c20260806-44u
- [CT] every completed match is recorded, including outcomes that score no player ^c20260805-24u
- [PR] the weak tail is the product — consistent low outcomes locate items worth attention, and no single item's score is the point ^c20260805-25u
- [PR] statelessness at the match boundary is what makes runs parallel, reproducible, and cacheable ^c20260805-26u
- [CT] its output is `Accountable.Assertion` evaluation-record material: confidence, never authority ^c20260805-27u
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

## Tournament.Hook

- [DF] a `Tournament.Hook` is a named function a `Tournament.Definition` supplies and the engine calls at a fixed point to obtain a consumer-owned part of the match ^c20260805-43u
- [DC] the declared hooks supply the match players, the player presentation, the match identity, and the consumer verdict slot ^c20260806-11u
- [CT] hooks return values and never perform effects; spawning, presentation-order randomization, and storing stay engine-side ^c20260806-19u
- [FR] a definition may choose which players meet however it likes, including randomly; only presentation order is engine business ^c20260806-20u
- [DC] the match-players and match-identity hooks are required and have no default; every other hook defaults, so a definition supplies only what its domain forces ^c20260806-21u
- [DC] each call to the match-players hook yields the two competitors of one match, and nothing wider ^c20260806-13u
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

- [DF] a `Tournament.Match` is one evaluation of a player pair against its tournament's question, run by one `Tournament.Judge` in one fresh context ^c20260805-53u
- [DC] a match carries no state from any other match ^c20260805-54u
- [DC] match identity is an opaque string supplied by the consumer; the engine requires it and never computes one ^c20260805-55u
- [FR] the consumer decides which content changes make a new match and which do not ^c20260805-56u
- [DC] the `Match.Verbatim` is the exact rendered text handed to the judge, recorded by hash as cheap evidence of what ran ^c20260805-57u
- [DC] the engine composes the `Match.Verbatim` from the consumer's player presentations and its own frame: the question, the position labels, and the answer contract ^c20260806-7u
- [PR] engine-owned framing is what keeps position decoding sound — a consumer free to label the candidates could silently invert every verdict it recorded ^c20260806-8u
- [CT] the verbatim hash is run evidence and not identity; it varies per run because presentation order is randomized ^c20260805-58u
- [DC] presentation order is randomized per run and the order actually run is recorded ^c20260805-59u
- [DC] order randomization is default engine normalization rather than `Tournament.Definition` work ^c20260805-60u
- [PR] randomized order neutralizes position bias across repeated runs, so the defense is statistical and needs run volume to hold ^c20260805-61u
- [FR] the same match may be run repeatedly to gather independent verdicts; whether to reuse a prior run is the consumer's choice ^c20260805-62u
- [CT] a match either completes with a `Tournament.Verdict` or fails to run, and a failed run produces no match record ^c20260805-63u

****

## Tournament.Judge

- [DF] a `Tournament.Judge` is the agent spawned to decide one `Tournament.Match` and return its verdict ^c20260805-64u
- [DC] one judge run serves one match, and no judge carries state between matches ^c20260805-65u
- [DC] a judge answers by position rather than by player, and the engine decodes that position back through the order it ran ^c20260806-9u
- [CT] the judge is the tournament's only semantic actor; the engine around it stays a `CPU.Program` ^c20260805-66u
- [DC] a refusal requires a stated reason, so declining is an answer rather than an abstention ^c20260805-67u
- [PR] refusal rate reads as a judge metric as much as a pool metric — a rate drifting across unrelated tournaments indicts the judge prompt ^c20260805-68u
- [FR] the model, provider, and prompt behind a judge are consumer choices ^c20260805-69u
- [RJ] a judge does not rank a pool or compare beyond the pair it was given ^c20260805-70u

****

## Tournament.Verdict

- [DF] a `Tournament.Verdict` is the recorded outcome of one completed `Tournament.Match` ^c20260805-71u
- [DC] a verdict has two zones: an engine-written envelope and an opaque consumer slot, following `Bloberia.Record` ^c20260805-72u
- [DC] the envelope records the match identity, the judge, the outcome, the presentation order actually run, and the `Match.Verbatim` hash ^c20260805-73u
- [CT] the engine stores the consumer slot and never reads it ^c20260805-74u
- [CT] slot content never shadows an envelope field; the slot carries analysis material, not a restatement of what the envelope owns ^c20260805-75u
- [CT] an outcome is either a preferred player or `Tournament.Verdict::No.Contest` ^c20260805-76u
- [RJ] there is no draw outcome; equally good players converge through split records across repeated matches ^c20260805-77u
- [CT] verdicts are append-only, and a later verdict never replaces an earlier one ^c20260805-78u
- [PR] one verdict is noise; signal lives only in accumulation ^c20260805-79u

****

## Tournament.Verdict::No.Contest

- [DF] `Tournament.Verdict::No.Contest` is the outcome of a match its judge completed but declined to decide ^c20260805-80u
- [CT] it scores no player and enters no ranking fold ^c20260805-81u
- [DC] it carries a reason attributing the refusal to the question, to a player, or to the prompt it was given ^c20260805-82u
- [PR] its distribution is the read: scattered across a pool indicts the `Tournament.Definition`, clustered on one player indicts that player ^c20260805-83u
- [CT] it is a completed match record, and a match that failed to run is not a no-contest ^c20260805-84u
- [PR] it is the only outcome that evaluates the tournament rather than its players ^c20260805-85u

****

## Tournament.Depot

- [DF] a `Tournament.Depot` is one rooted directory holding every tournament's frozen definition and its accumulated records ^c20260806-25u
- [DC] the depot resolves to a canonical global location by default and accepts an explicit root ^c20260806-26u
- [DC] a depot separates `definitions/` from `records/`: the first holds each tournament's frozen definition, the second its `Agentos.Bloberia` record store ^c20260806-27u
- [DC] records are namespaced by tournament, so one tournament's records are reachable without reading another's ^c20260806-28u
- [CT] `Agentos.Bloberia` owns record storage and query; the depot owns only the surrounding layout ^c20260806-29u
- [PR] namespacing by tournament is what makes listing tournaments a directory read rather than a record scan ^c20260806-30u
