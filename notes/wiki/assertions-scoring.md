# Assertions and scoring

<!-- tarav.sessions
1ae20f8c = codex:01a0ff32-0ec2-7b72-8850-fa795135f3c9 @1ae20f8c8159f12d2402ea702cf49c876ec46a72f71ce12423ae1dbdf2a91871
-->

## Assertable objects and closed cases

An Assertable object can expose several labeled, identified Assertions through
`.assertions`. A label is a durable route to an Assertion, while list order is
only presentation. Each Assertion identifies an exact subject and can produce
more than one typed assessment case for different scoring questions.
<!-- tarav.breadcrumb cd25ccfe7f857ba247e45af7dab414a3301d05c95ad723ee29cfe3595d123310 -->
<!-- tarav.breadcrumb e5b08612e1eabc76590e88d2c2fbbc0f4525fd5d4dac36a49d1e88e29d70d069 -->

A case is a closed scoring packet: it retains an Assertion reference, a question,
and the material presented to the scorer. Case payloads are owned by their
producer and consumer; Tarav does not impose one universal evidence schema.
The scorer judges only the supplied packet. A producer may report that a case
Type is unsupported or that a supported case lacks enough material; those are
different conditions. Scoring results remain separate from Assertion identity.
<!-- tarav.breadcrumb 85c84972b98773bf8f7505b529b2e2c0d1022ecf52035435a11d0e7809f84ca2 -->

Request [846](../../../tarav-py/notes/live/846-assertable-assessment-cases-impl-req.md)
implemented this foundation in `tarav.l2.scoring.assertions`. Its Line-owned
example produces grounding and support-inventory cases from an exact Line
edition and its rendered Support.Set. The runtime registers their Record Types;
the existing Line Assertion identity and ranking adapter were preserved.
`tests/scoring/test_assessment_cases.py` exercises label lookup, closed snapshots,
distinct case payloads, failure modes, and Record round-trips; 47 focused
scoring and architecture tests passed in `tarav-py` commit `230b98a`.

## Pairwise tribunals

A ranking case names its tribunal Type. The tribunal owns its population,
comparison question, instructions, and optional admission check. The common
ranker compares only two cases from the same tribunal, using their retained
presentations and no external research. It accepts A, B, tie, or abstain and
retains the exact prompt, judge, outcome, and rationale for inspection.
<!-- tarav.breadcrumb 4bf188231e01daf06f6051091769c3848c2a28c98f3a94d3179dfcb9a2fae65d -->
<!-- tarav.breadcrumb 6630cabff2d5722bae794f7211969dfed0cc4e0c39143e74e0db7d87b495af2b -->

The first derived measure is relative win/tie support among judged pairs,
accompanied by comparison and opponent counts, abstentions, and population
coverage. One case has no relative score. Sparse or weak support may become
scoring-owned POIs, but a low rank does not establish that an Assertion is
false. Request [848](../../../tarav-py/notes/live/848-pairwise-tribunal-scoring-mvp-impl-req.md)
implemented this path in `tarav.l2.scoring.tribunals` and the existing
ScoringRepository. Two different tribunal Types and case payloads use the same
ranker in its tests; 61 focused tests passed at product commit `bd5be10`.
<!-- tarav.breadcrumb f323afe8896d5439e0a8072c7307347d63e465238f38e60641a25d1929783a18 -->
