> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Improvement.Loop

- [DF] an `Improvement.Loop` is a `Run.Workspace` kind that spawns agents to raise a consumer-defined score over a subject, under consumer-defined constraints ^c20260809-94u
- [DC] one loop is three things: the `Mutable.Set` it may change, the `Loop.Constraint`s that must hold, and the `Loop.Score`s it is judged by ^c20260810-0u
- [RJ] there is no loop engine — a loop is its definition and its own tooling, living in its workspaces ^c20260810-1u
- [CT] the improver changes only the `Mutable.Set`; everything outside it, the scorer and the constraints included, is fixed and may be understood but never altered ^c20260810-2u
- [PR] fixing everything outside the `Mutable.Set` prevents wasted execution rather than invalid results — a score is recomputable, so verification is the gate and the loop never has to be trusted ^c20260810-3u
- [CT] the workspace is the only writable surface, and the score reads its inputs from outside it ^c20260809-101u
- [DC] a `Loop.Constraint` may be mechanical or judged, and failing any of them zeroes the `Loop.Score` rather than trading against its other tests ^c20260810-4u
- [FR] a `Loop.Score` may be a vector of tests rather than one number; the improver is shown the results and reasons about the tradeoff itself ^c20260810-5u
- [CT] each candidate names its parent, so a loop's state lives in its lineage rather than in anything holding it ^c20260810-6u
- [PR] the product of a run is the read over its lineage: what was tried, what scored where, and what the best candidate changes ^c20260809-102u
- [PR] a disappointing run indicts exactly one of the three: no admitted candidate means the `Mutable.Set` is too narrow, a higher `Loop.Score` on worse work means a `Loop.Constraint` is missing, and no movement at all means the instrument did not discriminate ^c20260810-7u
- [PR] the `Loop.Constraint`s are the durable output: the improved subject is one artifact, while the constraint set is what the run taught about the subject ^c20260810-8u
- [CT] the domain stays consumer-owned: nothing interprets the subject, the score, or what an improvement is ^c20260810-9u
- [RJ] the loop does not adopt its result; taking a candidate onto a `Stable.Surface` is a separate gated act ^c20260809-103u
- [RJ] nothing judges whether a score measures anything — a badly chosen metric produces clean iterations and an empty reading ^c20260810-10u
