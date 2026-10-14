# References: locator, check, and hints

<!-- tarav.sessions
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
-->

## Shared resolution and reusable mechanics

A proposed reference-resolution workflow provides a common entry point, like
a DNS in its lookup role. Workflows creating reference types register them so
others can resolve them. This workflow can provide types imported from other
workflows as well as its own.
<!-- tarav.breadcrumb 302f7be351deb977bbbaf722d7b1eb4f5b2d70f56a039a91e0f985c731f61b19 -->

Tarav should supply common built-in reference types and their mechanics so
individual workflows do not each implement filesystem or Git resolution.
The proposed dependency direction is `tarav.references` imported by
`tarav.archive`, not the reverse. Specialized references such as Archive
references can coexist with the shared types; a base `ref.resolve()` is a
candidate common interface. This supports general subjects for
[external annotations](external-annotations.md).
<!-- tarav.breadcrumb 4ea8085e977e03b850cc4ad8a9280dcd823123b81ef49a3626ac1a2ca57c0527 -->

## Construction defaults

Reference construction should add default hints. The discussed file-reference
usage should not require callers to supply all hints themselves. Archive
reference construction should also offer a version using a default Archive
location, alongside explicit location selection. These are design requirements;
the precise APIs and default-selection mechanics remain to be settled.
<!-- tarav.breadcrumb 91380eb7782e1a9c5948866cdd730e6671563237417d4941c167ad4038e0097e -->

## Typed primitives with common principles

References are typed primitives. Built-in Tarav workflows can supply reference
primitives with their own mechanics while sharing general Tarav reference
principles. The chosen vocabulary is `locator`, `check`, and `hints`.
<!-- tarav.breadcrumb d785bba976da61684240d37b5cfcda67ac829abc8ce0784563cc009c9369fe06 -->
<!-- tarav.breadcrumb 1ac8a7948208f8138ac7ac69291f969f83138bbe4a61ae552c0d46e14e9ba0f1 -->

## Locator and check

The `locator` supplies information used to find the resource, such as a
filesystem path. The `check` supplies information used to assess whether the
located resource is what the reference's producer intended, such as a content
hash. These have mechanical roles governed by the reference type.
<!-- tarav.breadcrumb 599c5b73859a1811408855e93630c702247e5d17fe72e5aa8716a1ee5a7e1f76 -->
<!-- tarav.breadcrumb 0cf891a0df0f88e73c7ad45919ce8a3eaee4692e48202548b42bffc43b1cf829 -->
<!-- tarav.breadcrumb 269e7791990295f2552bf0cef206b5837ffa506ab27d2449b672ec2ccdce9607 -->

The discussion initially called the checking information edition data. The
User broadened the axis to whether we obtained the intended target, rather
than assuming every check concerns an edition, and selected the name `check`.
<!-- tarav.breadcrumb 906bfcf83cc07c5068746302b60e488e2b05852391099aece9cc4ae08d9d7879 -->
<!-- tarav.breadcrumb 1cfc61d03bef38ea0dd1f90a500da68801a6c92dd44e7d601401a28b9d2464d4 -->

## Hints stay outside the mechanics

The `hints` are descriptive information attached to the reference object or
Record as opaque JSON. They provide a small representation of the linked
object that may help when something goes wrong. Hints are recommended to be
very lightweight, following the same preservation principle as descriptive
Records.
<!-- tarav.breadcrumb cbe4887c652268fb7872d8e3f827ba12573cce984a72cd71a36080abc5b9fcf0 -->

Hints have no mechanical role in resolving or checking the reference. Adding
or changing them must not change mechanical resolution. They remain available
for Agent or other consumer investigation without becoming an undocumented
locator or resolver fallback. `WE.LIKE.DUMB.CODE` expresses the preference for
keeping reference resolution simple.
<!-- tarav.breadcrumb 05a88f72b5d563b2907cfe5fc85609dc2f432ada4e0f5244ebd5bba4ea436518 -->

Locator and check data are informative too, but their assigned mechanical
roles make them less flexible. What is called `hints` is specifically data
used only as hints; the distinction concerns its role rather than whether its
content resembles technical resolution information.
<!-- tarav.breadcrumb 0a83259cb58e580d540fc3d4ec242bf51509a6e3ede3a76b6c7652ac8009bfb8 -->
<!-- tarav.breadcrumb a1c95779d84d10b56be1955fe5910372e4b0f05d674c6db75f10be072c5f1a59 -->

## Hints as a general pattern

The hint pattern can be used across any Tarav object, not only references.
Hints are opaque to the mechanics handling that object: those mechanics ignore
them. They do not have to live inside a field named `hints`; the pattern is
defined by that role, not by a required serialization location.
<!-- tarav.breadcrumb a3ba25fb7fa1cea99428135cf51c3e7c3584572f68e4add0de6f69a8682893ff -->

Prefer placing hints in an explicit `hints` field even though the pattern does
not require that location. Naming the field makes the Record self-documenting:
it identifies the content's hint role while leaving it opaque to mechanics.
<!-- tarav.breadcrumb 5ff75b40b8a0021559cb544a8f1a7ef376e6b226e958afa8b3c5884acc7b9481 -->

## Hint production

Hints are intended for agent consumption, not presumed agent authorship.
Prefer code-generated facts, especially information obtained from established
systems such as the operating system and Git. Generated summaries stored as
ordinary hint fields are an antipattern.
<!-- tarav.breadcrumb 539e73712251ba0553181e31e6d5658aebf59d3ae9ffeba1e9a4f3a260638463 -->
<!-- tarav.breadcrumb 9ef5c358bbbd00790a7e7d94d6ee76572f2dbd044d383551a70d55ecc8e3eee3 -->

This follows the general [agent-generated data minimization](agent-generated-data.md)
constraint: use mechanically obtained facts or leave information absent;
introduce agent-generated claims only when necessary and explicitly controlled.
An opaque hint payload does not relax that constraint.
<!-- tarav.breadcrumb cf7477ec34f0bacf59ca7ddfd9f3b4fce0d952defae258e0c6c8a297fe4beed2 -->
<!-- tarav.breadcrumb a2060b34ee451d091f1aab9abc78514855dc3b71cd57b72cf4efe95691741678 -->
