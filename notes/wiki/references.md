# References: locator, check, and hints

<!-- tarav.sessions
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
-->

## Shared resolution and reusable mechanics

A proposed reference-resolution workflow provides a common entry point, like
a DNS in its lookup role. Workflows creating reference types register them so
others can resolve them. This workflow can provide types imported from other
workflows as well as its own.
<!-- tarav.breadcrumb 302f7be351de -->

Tarav should supply common built-in reference types and their mechanics so
individual workflows do not each implement filesystem or Git resolution.
The proposed dependency direction is `tarav.references` imported by
`tarav.archive`, not the reverse. Specialized references such as Archive
references can coexist with the shared types; a base `ref.resolve()` is a
candidate common interface. This supports general subjects for
[external annotations](external-annotations.md).
<!-- tarav.breadcrumb 4ea8085e977e -->

## Construction defaults

Reference construction should add default hints. The discussed file-reference
usage should not require callers to supply all hints themselves. Archive
reference construction should also offer a version using a default Archive
location, alongside explicit location selection. These are design requirements;
the precise APIs and default-selection mechanics remain to be settled.
<!-- tarav.breadcrumb 91380eb7782e -->

## Typed primitives with common principles

References are typed primitives. Built-in Tarav workflows can supply reference
primitives with their own mechanics while sharing general Tarav reference
principles. The chosen vocabulary is `locator`, `check`, and `hints`.
<!-- tarav.breadcrumb d785bba976da -->
<!-- tarav.breadcrumb 1ac8a7948208 -->

## Locator and check

The `locator` supplies information used to find the resource, such as a
filesystem path. The `check` supplies information used to assess whether the
located resource is what the reference's producer intended, such as a content
hash. These have mechanical roles governed by the reference type.
<!-- tarav.breadcrumb 599c5b73859a -->
<!-- tarav.breadcrumb 0cf891a0df0f -->
<!-- tarav.breadcrumb 269e77919902 -->

The discussion initially called the checking information edition data. The
User broadened the axis to whether we obtained the intended target, rather
than assuming every check concerns an edition, and selected the name `check`.
<!-- tarav.breadcrumb 906bfcf83cc0 -->
<!-- tarav.breadcrumb 1cfc61d03bef -->

## Hints stay outside the mechanics

The `hints` are descriptive information attached to the reference object or
Record as opaque JSON. They provide a small representation of the linked
object that may help when something goes wrong. Hints are recommended to be
very lightweight, following the same preservation principle as descriptive
Records.
<!-- tarav.breadcrumb cbe4887c6522 -->

Hints have no mechanical role in resolving or checking the reference. Adding
or changing them must not change mechanical resolution. They remain available
for Agent or other consumer investigation without becoming an undocumented
locator or resolver fallback. `WE.LIKE.DUMB.CODE` expresses the preference for
keeping reference resolution simple.
<!-- tarav.breadcrumb 05a88f72b5d5 -->

Locator and check data are informative too, but their assigned mechanical
roles make them less flexible. What is called `hints` is specifically data
used only as hints; the distinction concerns its role rather than whether its
content resembles technical resolution information.
<!-- tarav.breadcrumb 0a83259cb58e -->
<!-- tarav.breadcrumb a1c95779d84d -->

## Hints as a general pattern

The hint pattern can be used across any Tarav object, not only references.
Hints are opaque to the mechanics handling that object: those mechanics ignore
them. They do not have to live inside a field named `hints`; the pattern is
defined by that role, not by a required serialization location.
<!-- tarav.breadcrumb a3ba25fb7fa1 -->

Prefer placing hints in an explicit `hints` field even though the pattern does
not require that location. Naming the field makes the Record self-documenting:
it identifies the content's hint role while leaving it opaque to mechanics.
<!-- tarav.breadcrumb 5ff75b40b8a0 -->

## Hint production

Hints are intended for agent consumption, not presumed agent authorship.
Prefer code-generated facts, especially information obtained from established
systems such as the operating system and Git. Generated summaries stored as
ordinary hint fields are an antipattern.
<!-- tarav.breadcrumb 539e73712251 -->
<!-- tarav.breadcrumb 9ef5c358bbbd -->

This follows the general [agent-generated data minimization](agent-generated-data.md)
constraint: use mechanically obtained facts or leave information absent;
introduce agent-generated claims only when necessary and explicitly controlled.
An opaque hint payload does not relax that constraint.
<!-- tarav.breadcrumb cf7477ec34f0 -->
<!-- tarav.breadcrumb a2060b34ee45 -->
