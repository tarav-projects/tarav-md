# Tarav.Harness

<!-- tarav.sessions
33afe59c = codex:01a07228-313a-7ab3-b6e0-aedcb5216b3c @33afe59c2f13ac5d4b59e56f7a3761d3d91c1206a1b6287b0872036739b370fd
-->

## Purpose

`tarav.harness` is the reusable core for making arbitrary systems legible,
operable, and self-evaluating for Agents. It provides the primitives needed to
build domain-specific harnesses; Diagram is one consumer, and PaperSON can be
another. Tarav may remain one project, but Harness must remain independent of
Diagram, Archive, Chatlas, Skillware, and CLI semantics.
<!-- tarav.context 33afe59c:3f8b1a8709d76020 -->

The intended operating loop is:

```text
inspect state -> choose an allowed action -> process -> validate -> emit POIs
    -> fix or bless -> reevaluate
```
<!-- tarav.context 33afe59c:6eb7ba37e1c4e576 -->

Prompts, tools, schemas, and transition constraints form the *a priori* quality
front. Deterministic checks, linters, Agent audits, and human review form the
*posterior* front. The promise is not that errors become impossible, but that
the probability of a bad result remaining unnoticed decreases as work and
tooling accumulate. No POIs means only that nothing was detected.
<!-- tarav.context 33afe59c:6eb7ba37e1c4e576 -->

## Records and semantic authority

A registered class is the authoritative interpreter of its serialized Record.
The JSON representation remains publicly inspectable, but its semantics belong
to the registered class hierarchy. Generic machinery may read or search the
representation; code that assigns meaning to it must use that class or an
appropriate supertype.
<!-- tarav.context 33afe59c:0628764bbc1b9f44 -->
<!-- tarav.context 33afe59c:5daf5047ba070c43 -->

`Type.Resolution.PATH` is the universal, deliberately simple mechanism for
selecting a class from an opaque retained Record. Every independently loadable
JSON object, including each JSONL line, declares its Type at its serialized
root. Once dispatch has selected the registered class, ordinary code owns the
representation and may construct nested objects directly; disk layout should
otherwise be irrelevant to most behavior.
<!-- tarav.context 33afe59c:003d526f71305a78 -->
<!-- tarav.context 33afe59c:d8265058f73aa1fd -->

Opaque JSON does not need a Tarav wrapper. General callers use the JSON library;
typed callers use a Registry or a compatible registered class. A Registry load
returns the authoritative registered class, while a class load is valid only
when the caller is that registered class or one of its descendants.
<!-- tarav.context 33afe59c:a16bc9533149329a -->
<!-- tarav.context 33afe59c:6974e7c808177a3e -->

## Ship identity

A Ship UUID is a semantic landmark with almost no intrinsic meaning. The same
identity primitive can identify a class Type, a retained Record, or domain
cargo. Its containing class and relationship supply the semantics.
<!-- tarav.context 33afe59c:95f9a85775c2cc57 -->
<!-- tarav.context 33afe59c:1254267dbe77ab6d -->

Therefore a class can both *have a Ship* as a semantic Type and *model Ships*
inside its Records. Harness should not infer Ship roles from UUID shapes or
serialized paths. A `TaravRecord` exposes its semantic projection through
`ships()`, returning Ship instances selected by the authoritative class.
<!-- tarav.context 33afe59c:95f9a85775c2cc57 -->
<!-- tarav.context 33afe59c:0628764bbc1b9f44 -->

## Evaluation growth

The next shared capabilities to consolidate are `assertions()` and
`findings()` on an evaluation-bearing `TaravRecord` subtype such as
`TaravObject`. `actions()` and explicit `state()` remain later discoveries,
introduced only when real workflows establish their useful common shape.
<!-- tarav.context 33afe59c:1d4b8adac2c8397d -->
