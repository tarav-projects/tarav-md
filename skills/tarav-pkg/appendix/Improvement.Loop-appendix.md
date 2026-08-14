> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Improvement.Loop/Candidate.Index.Improvement.Loop

- [DC] the first candidate loop improves an index fragment, with the line bodies and the `Line.Type` definitions as its `Mutable.Set` ^c20260810-11u
- [CT] a line's fidelity to its support set is a judged `Loop.Constraint` rather than a scored term, so nothing the improver gains can be traded against grounding ^c20260810-12u
- [PR] anchors stay outside the `Mutable.Set`, which is what leaves the evidence constant and the grounding constraint checkable ^c20260810-13u
- [DC] the vocabulary is scored on selectivity: a line should peak on one type, and a type ranking near the top everywhere is the vague one ^c20260810-14u
- [CT] selectivity alone is gamed by narrowing types until little fits, so coverage is scored beside it ^c20260810-15u
- [DC] line bodies and type definitions move in alternating phases and never together, so a score change stays attributable ^c20260810-16u
- [DC] the sample is pinned across iterations, and a held-out set is scored only on the final candidate ^c20260810-17u
- [PR] a better `Line.Type` definition is the compounding output: it improves every line written afterward, including ones the sample never contained ^c20260810-18u
- [RJ] the loop is not built before its scorer is calibrated — an uncalibrated instrument makes a loop that hill-climbs on noise ^c20260810-19u
