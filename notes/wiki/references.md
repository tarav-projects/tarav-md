# References: locator, check, and hints

<!-- tarav.sessions
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
-->

## Typed primitives with common principles

References are typed primitives. Built-in Tarav workflows can supply reference
primitives with their own mechanics while sharing general Tarav reference
principles. The chosen vocabulary is `locator`, `check`, and `hints`.
<!-- tarav.context 5626cd5f:921db862da9ed923 -->
<!-- tarav.context 5626cd5f:53fa6313a047f194 -->

## Locator and check

The `locator` supplies information used to find the resource, such as a
filesystem path. The `check` supplies information used to assess whether the
located resource is what the reference's producer intended, such as a content
hash. These have mechanical roles governed by the reference type.
<!-- tarav.context 5626cd5f:921db862da9ed923 -->
<!-- tarav.context 5626cd5f:e73583493a1ce59c -->
<!-- tarav.context 5626cd5f:53fa6313a047f194 -->

The discussion initially called the checking information edition data. The
User broadened the axis to whether we obtained the intended target, rather
than assuming every check concerns an edition, and selected the name `check`.
<!-- tarav.context 5626cd5f:e73583493a1ce59c -->
<!-- tarav.context 5626cd5f:53fa6313a047f194 -->

## Hints stay outside the mechanics

The `hints` are descriptive information attached to the reference object or
Record as opaque JSON. They provide a small representation of the linked
object that may help when something goes wrong. Hints are recommended to be
very lightweight, following the same preservation principle as descriptive
Records.
<!-- tarav.context 5626cd5f:921db862da9ed923 -->

Hints have no mechanical role in resolving or checking the reference. Adding
or changing them must not change mechanical resolution. They remain available
for Agent or other consumer investigation without becoming an undocumented
locator or resolver fallback. `WE.LIKE.DUMB.CODE` expresses the preference for
keeping reference resolution simple.
<!-- tarav.context 5626cd5f:e73583493a1ce59c -->

Locator and check data are informative too, but their assigned mechanical
roles make them less flexible. What is called `hints` is specifically data
used only as hints; the distinction concerns its role rather than whether its
content resembles technical resolution information.
<!-- tarav.context 5626cd5f:921db862da9ed923 -->
<!-- tarav.context 5626cd5f:e73583493a1ce59c -->

## Hints as a general pattern

The hint pattern can be used across any Tarav object, not only references.
Hints are opaque to the mechanics handling that object: those mechanics ignore
them. They do not have to live inside a field named `hints`; the pattern is
defined by that role, not by a required serialization location.
<!-- tarav.context 5626cd5f:7af5b61e92c70bc7 -->

Prefer placing hints in an explicit `hints` field even though the pattern does
not require that location. Naming the field makes the Record self-documenting:
it identifies the content's hint role while leaving it opaque to mechanics.
<!-- tarav.context 5626cd5f:1f7316b721a323d9 -->

## Hint production

Hints are intended for agent consumption, not presumed agent authorship.
Prefer code-generated facts, especially information obtained from established
systems such as the operating system and Git. Generated summaries stored as
ordinary hint fields are an antipattern.
<!-- tarav.context 5626cd5f:b3ea6e16f244acf4 -->
<!-- tarav.context 5626cd5f:02cf30e0bf590b15 -->

This follows the general [agent-generated data minimization](agent-generated-data.md)
constraint: use mechanically obtained facts or leave information absent;
introduce agent-generated claims only when necessary and explicitly controlled.
An opaque hint payload does not relax that constraint.
<!-- tarav.context 5626cd5f:49b346a342bea570 -->
<!-- tarav.context 5626cd5f:5b55053ee5e909a7 -->
