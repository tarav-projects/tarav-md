# Lines workflow

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
-->

## Scoped statements

A Line is an identifiable, typed natural-language statement expressing one
semantic contribution within an explicit scope. It decomposes larger material
into minimally complex statements that need not stand alone. Scope supplies
the context in which the statement must be interpreted and can itself be
another Line, forming part of a larger semantic graph.
<!-- tarav.breadcrumb ad0eb0285557ba1e630125ec7b468ef25f90d71c50b7207bcb47112ac89b7b68 -->

The base design carries identity, text and scope. Scope accepts `TaravEntity`
for now; no separate Scope type or arbitrary opaque-value contract is required.
<!-- tarav.breadcrumb f944973105df322bc2c35df669cbe0365542c9976a78a49da4fb8717c5eea3c1 -->

## Decomposition without authority

Lines do not model authority. One fact is the authoring aim, not a truth
guarantee. Maximal practical orthogonality and encapsulation aim to make
changes local: a changed car color should require changing one or a few
statements, not rewriting unrelated aspects. Full orthogonality is not required.
<!-- tarav.breadcrumb 67790e596ae7387739acfb6afa4a035b8afd3ce48ec2527bac9bb9d797b51d3a -->

Evidence, editions, approval and scoring remain optional additions. Semantic
scope differs from placement in a collection or display. Block-specific scope
may later be specialized as BlockLine, but is not required of every Line.
<!-- tarav.breadcrumb 0d9639025f15687b5aaac0dbb20bb195aae7b1db8b5b8725c1a72c9b74e9e83e -->

## Implementation design

[Request 829](../../../tarav-py/notes/live/829-scoped-lines-foundation-impl-req.md)
records the proposed first slice: independent construction, entity scope
navigation and explicit record round-tripping. It is a plan, not an assertion
that the legacy implementation has been replaced. The writing principles
remain separately documented in [Kernel.Writing](kernel-writting.md).
<!-- tarav.breadcrumb 83fc807f17943dd729ffa09e68d9e8b0fdd1171b159f70cd229cfb1b9f721d7e -->

## Scope as an interpretive dependency

A Line has exactly one scope. Scope identifies what the statement assumes
exists for its content to have meaning; it is fundamental to the Line, not
a relationship describing where the Line appears. Presentation, storage and
collection relationships are external to this definition. The earlier
discussion of placement is not an additional requirement of the base model.

The accepted base is identity, text and a scope pointing to a `TaravEntity`,
with specialization supplied by the Python type. Another Line may supply
scope, so semantic decomposition can form a graph of interpretive dependencies.

The proposed `line.context(type=LineScope)` exposes that semantic relationship
through a specialized context object. `LineScope` names the requested context
view, not a restriction that the scope target must have that type. See
[typed context views](context-graph.md#typed-read-only-context-views).

Capture evidence pending: these additions record the current discussion in
session `01a0d86c-9538-7be1-af96-014cd4203d61`. Chatlas refresh was denied access
to its cache on 2026-09-30; exact Turn attachments and Breadcrumb registration
remain pending. This captures design, not implemented API behavior.
