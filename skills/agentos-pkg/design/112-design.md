> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Improvement.Loop

- [DF] an `Improvement.Loop` is a `Run.Workspace` kind that spawns agents to raise a consumer-defined score over a subject, under consumer-defined constraints ^c20260809-94u
- [DC] one loop is one `Loop.Definition` and its accumulated iterations over one seeded subject ^c20260809-95u
- [CT] the system is domain-blind: it calls the definition's hooks and never interprets the subject, the score, or what an improvement is ^c20260809-96u
- [DC] the declared hooks supply the seed, the improver's brief, admission, the score, and which candidate becomes the next parent ^c20260809-97u
- [CT] each iteration names its parent, so the loop's state lives in the recorded lineage rather than in the engine ^c20260809-98u
- [CT] the improver is spawned fresh per iteration and submits through a command, never writing a record itself ^c20260809-99u
- [PR] the improver never receives the score hook — the engine calls it, so blinding is a boundary rather than a policy ^c20260809-100u
- [CT] the workspace is the only writable surface, and the score reads its inputs from outside it ^c20260809-101u
- [PR] the product of a run is the read over its lineage: what was tried, what scored where, and what the best candidate changes ^c20260809-102u
- [RJ] the loop does not adopt its result; taking a candidate onto a `Stable.Surface` is a separate gated act ^c20260809-103u
- [RJ] the engine does not judge whether a score measures anything — a badly chosen metric produces clean iterations and an empty reading ^c20260809-104u
