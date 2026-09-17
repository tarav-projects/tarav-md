# Tarav as a record framework

<!-- tarav.sessions
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
-->

## Lightweight records and distributed participation

Tarav is a framework library heavily based on lightweight JSON Records.
Projects and subsystems can produce Records and participate in the Tarav
network. Storage can be centralized or linked from repositories outside
Tarav's hosting; the initial scope is local to one computer. The framework
leaves room for different implementations over these Records.
<!-- tarav.context 5626cd5f:1a749e3480caa30d -->

## Records and Artifacts

A Record is Tarav's communication package and data unit: Tarav-consumable
JSON that can contain data, describe something, or point to other data.
Records form a common vocabulary for describing the world around Tarav.
An Artifact is the thing being handled or described, such as a file, folder,
repository, or abstract object. The distinction is contextual rather than a
rigid partition: a Record can itself be treated as an Artifact by another
operation. The stronger defining contract is on the Record side.
<!-- tarav.context 5626cd5f:22c3ed848cddf2ce -->
<!-- tarav.context 5626cd5f:05f1cab35e01883a -->

All Records should be lightweight. Archived Records have an especially strong
economy requirement, and Archive-issued Records should be designed for
long-term retention. Preserving knowledge about something need not require
preserving the thing itself; storage commitment can be gradual.
<!-- tarav.context 5626cd5f:22c3ed848cddf2ce -->
<!-- tarav.context 5626cd5f:05f1cab35e01883a -->

## Semantics built on common primitives

Observation times, changing descriptions, and edition histories are semantics
built on Records, not requirements imposed on every Record. The common
primitives must be expressive enough for those different cases. Typed Records
can provide distinct semantics without forcing one universal descriptive or
history model.
<!-- tarav.context 5626cd5f:05f1cab35e01883a -->

## Python is the primary programmatic interface

Tarav's main interface is the Python library. Agents can interact through
Python scripts. The CLI is another interface, providing convenience and
efficiency without defining the limits of what workflows can do.
<!-- tarav.context 5626cd5f:1a749e3480caa30d -->

## Workflows own their implementation and integration

Tarav supplies primitives and a development environment for multiple capture
workflows. Wiki capture and Model building are distinct examples. Each workflow
can implement what its situation requires and is responsible for hooking into
Tarav when it wants interoperability. User/Agent partitions are specifically
part of the Model workflow, not a universal structure for Tarav Records.
<!-- tarav.context 5626cd5f:1a749e3480caa30d -->

The intended framework includes a Workflow object that external workflows
subtype and register. How external workflow types register their classes and
hook their code is an early design problem. Filesystem paths and entry points
were proposed as an opt-in registration surface; the exact registration
contract remains to be defined.
<!-- tarav.context 5626cd5f:9c7bdf8a88beac34 -->

## Navigation through registered Record providers

Records form a graph that Agents should be able to explore through a general
navigation system. The intended experience resembles filesystem navigation:
start at a root listing projects or workflows, enter one, list its contents,
and continue. This is a navigation capability over the Record universe, not
a requirement to store every Record in one physical filesystem.
<!-- tarav.context 5626cd5f:72909b9556531689 -->

Collections become discoverable by registering a subroot rather than
registering every Record individually. A Tarav project, the Tarav Archive,
or a Telegram archive could each expose such an entry point. Navigation is
itself another workflow.
<!-- tarav.context 5626cd5f:72909b9556531689 -->

The navigation workflow provides an interface. A collection registers as a
particular type of Record provider, and navigation treats it according to that
type. Registration makes the entry point discoverable; the provider must
actually expose routes to its Records. Errors in fulfilling the navigation
contract surface as POIs.
<!-- tarav.context 5626cd5f:b1bb54fd54756974 -->

## Interpretation authority and compatibility

The registered Python class interpreting a Record's meaning is an invariant.
A proposed consumer rule permits a workflow to interpret Records only through
classes it owns or imports. A search workflow could use a general opaque
Record class that recognizes only minimal common information.
<!-- tarav.context 5626cd5f:9c7bdf8a88beac34 -->

If workflow A wants compatibility with workflow B, A must make its Records
compatible with B's interface. A supplies the compatibility declaration and
owns conformance. Minimal declarative mappings such as
`A.TypeX.path → B.TypeY.path` may provide flexibility, but interoperability
must not grow into arbitrary conversion code or a web of adapters. A can
change its schema to fit B.
<!-- tarav.context 5626cd5f:9c7bdf8a88beac34 -->
<!-- tarav.context 5626cd5f:b1f11f560186fdb4 -->

## Code and data evolve together

Tarav is both code and data. Record schemas are not immutable and may change
between versions. Developers are responsible for migrating both code and data;
the system does not owe backward compatibility, legacy readers, or automatic
migrations. Schema evolution is ordinary development work.
<!-- tarav.context 5626cd5f:b1f11f560186fdb4 -->
<!-- tarav.context 5626cd5f:be7eb9c3d6d8a1a0 -->

`CODE.NEVER.REPAIR` is an explicit rule, not merely a prohibition on silent
repair. Developer-directed code/data migrations remain part of development.
Archived identity commitments are treated separately in
[Archive as a DOI registry](archive-doi-registry.md).
<!-- tarav.context 5626cd5f:be7eb9c3d6d8a1a0 -->
