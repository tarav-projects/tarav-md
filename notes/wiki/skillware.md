# Skillware

<!-- tarav.sessions
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
-->

## Generation as source code

Skillware (`skw`) is a proposed generation programming language: reusable,
composable generation functions interpreted by an agent. A function has a
name, arguments that may be typed, a body, and context. Arguments and bodies
can contain arbitrary text. The purpose is to treat generation prompts as
source code and give structured skills and surfaces supporting tooling.
<!-- tarav.context 5626cd5f:7d31ec0b467c5769 -->
<!-- tarav.context 5626cd5f:c9883973bbe5abf7 -->

Generation typically produces a surface: a file or file fragment. Any file
can be harnessed in this way; the conceptual relationship is
`src.skw → generation → output`.
<!-- tarav.context 5626cd5f:ab2f0bce8f08eb6c -->

## Context dependencies and output assertions

Two distinct obligations surround generation:

- Generation dependencies declare what must be available in the generator
  agent's context at generation time.
- Output assertions declare what the produced surface must satisfy, evaluated
  through checks or Tarav's scoring system.
<!-- tarav.context 5626cd5f:5168b60329ac174e -->
<!-- tarav.context 5626cd5f:f94c9f480b948078 -->

Context connects Skillware to Tarav's contextualization workflows. Skillware
can declare how to obtain context through those workflows; more generally,
context acquisition can itself be expressed as another prompt.
<!-- tarav.context 5626cd5f:5168b60329ac174e -->

What a function declares it needs is distinct from what a particular
invocation received. Tracking the producing chat can supply evidence for
later audits of whether the required context was present.
<!-- tarav.context 5626cd5f:5a5f65e3e8d7fb29 -->

## Tracked outputs and reasoned POIs

Generated outputs can be tracked and become dependencies of other
generations. Changes can raise POIs for review of the dependency tree.
Adding a context requirement can likewise invalidate an output's previous
standing and prompt review or regeneration.
<!-- tarav.context 5626cd5f:c9883973bbe5abf7 -->
<!-- tarav.context 5626cd5f:5a5f65e3e8d7fb29 -->

Invalidation surfaces evidence rather than adjudicating the output. A POI
may report that generation context dependencies changed; this does not prove
that the generated content is wrong. POIs carry the reasons the harness
raised them.
<!-- tarav.context 5626cd5f:f78ed16c912e6afc -->

## Computing with agents

Skillware gives a concrete purpose to
[minimizing uncontrolled agent-generated data](agent-generated-data.md): when
generation is necessary, make it an identifiable, assessable activity.
Defined rules guide generation, and checks or scoring assess compliance.
The ambition is to make computing with agents scale through reusable
structure and tooling, as software does.
<!-- tarav.context 5626cd5f:5168b60329ac174e -->
<!-- tarav.context 5626cd5f:f94c9f480b948078 -->

An unassessed generated claim is not necessarily false or useless, but its
reliability is unknown. The measurement-without-uncertainty analogy motivates
surrounding generation with a mechanically tracked structure, deterministic
checks, scored assertions, and audits. These extend the
[Tarav harness](tarav-harness.md) progressively: the examples illustrate
capabilities to develop and learn from, rather than a requirement to build
every mechanism at once.
<!-- tarav.context 5626cd5f:f94c9f480b948078 -->
<!-- tarav.context 5626cd5f:f78ed16c912e6afc -->
