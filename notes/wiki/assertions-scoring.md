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
