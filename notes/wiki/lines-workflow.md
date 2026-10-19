# Lines workflow

<!-- tarav.sessions
0f5bad01 = codex:01a15483-94e8-7fe0-86ad-ddd83e2bae52 @0f5bad0131260477b4cf3d712a95871496c3db92d67eaa7910243e312f7b552a
-->

## Authoring context

A Line has a stable Ship and mutable natural-language text. Keeping its Ship
across a revision claims continuity of the same semantic statement; a new
statement gets a new Ship. Every Line is authored in exactly one Block. A
reader interprets it with that Block and its parent Blocks. The writer makes
the intended reading recoverable within this bounded ancestry, without having
to follow every relationship in the larger Diagram.
<!-- tarav.breadcrumb 358d9c218118 -->
<!-- tarav.breadcrumb 79848a7aaa8f -->

A Block is an identified Line context with a human-readable topic. It can hold
Lines and child Blocks in explicit order. Child Blocks inherit their parents'
context. A Block need not represent a concept: it may organize a discussion,
chronology, specification, or another kind of thought. The Python subtype
supplies its Type; the base Lines workflow has no Model layer.
<!-- tarav.breadcrumb c4fea6c08254 -->
<!-- tarav.breadcrumb bea08276330b -->

Within the authoring context, Lines aim to add distinct semantic contributions.
Consistency and redundancy checks can use the Block and its ancestry as their
minimum scope. Language remains interpretive, so these checks surface matters
for agent or human judgment rather than proving meaning mechanically.
<!-- tarav.breadcrumb dcd7923fa280 -->

## Relationships beyond Lines

A Block can have typed relationships to a class, instance, file, workflow, or
other Tarav object through the broader Diagram. For example, a Block may be a
current specification of a class, or merely a discussion about it. Those
relationships can carry maintenance obligations, but they do not enlarge the
Line's bounded authoring context. Searching the broader graph helps choose a
Block; interpreting a Line starts from its own Block ancestry.
<!-- tarav.breadcrumb fd0a94f077a4 -->
<!-- tarav.breadcrumb a58ee500b067 -->

The former Diagram Model, Collection, Draft, View, and Line-grounding code was
retired in favor of these small primitives. Its implementation remains in Git
history. The current Python implementation is in `tarav.l1.lines`; storage,
rendering, external relationships, and alignment mechanics can be composed
separately as their use cases are developed.
<!-- tarav.breadcrumb 444a8024a28e -->

[Implementation request 929](../../../tarav-py/notes/live/929-recursive-lines-blocks-impl-req.md)
records the executed redesign. [Kernel Writing](kernel-writting.md) discusses
the writing style that motivates focused Lines.
