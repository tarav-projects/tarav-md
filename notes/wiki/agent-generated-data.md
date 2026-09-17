# Agent-generated data minimization

<!-- tarav.sessions
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
-->

## A general design constraint

Tarav uses mechanically obtained facts wherever possible, especially data
from established systems such as the operating system and Git. Otherwise,
absence is preferable to filling the gap with agent-generated content. This
is a general design constraint, not merely a preference about hints.
<!-- tarav.context 5626cd5f:02cf30e0bf590b15 -->
<!-- tarav.context 5626cd5f:49b346a342bea570 -->

Agent-generated claims are used only when necessary for an explicitly defined
purpose and must be treated with care. Their production, provenance,
evaluation, and retention must be controlled by the workflow. The amount of
agent-generated data must remain deliberate and bounded: every such field or
artifact needs a reason to exist. Agent generation is not the default way to
populate missing information. The design must actually follow this constraint,
not merely state it.
<!-- tarav.context 5626cd5f:49b346a342bea570 -->
<!-- tarav.context 5626cd5f:5b55053ee5e909a7 -->

## Agent consumption does not imply agent authorship

[Reference hints](references.md) are for agents to consume; that does not mean
agents should generate them. Prefer mechanically extracted information. A
generated summary stored as an ordinary descriptive field is an antipattern,
not a default use of the opaque hint payload.
<!-- tarav.context 5626cd5f:b3ea6e16f244acf4 -->
<!-- tarav.context 5626cd5f:02cf30e0bf590b15 -->

Defining and controlling agent-generated data belongs to the Tarav harness
framework. The discussion used “agentic variables” for this concern; their
precise vocabulary and contracts remain to be developed.
<!-- tarav.context 5626cd5f:02cf30e0bf590b15 -->
