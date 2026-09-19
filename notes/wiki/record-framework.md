# Tarav as a record framework

<!-- tarav.sessions
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
-->

## Type dispatch and class responsibility

Tarav's declared record type maps to a registered Python class and integrates
with ordinary Python class relationships. Interpretation belongs to that
class. Changing a record's type to an incompatible class may produce an error,
for example because required fields do not match. Each class performs its own
due diligence; the framework need not enforce universal correctness before
allowing an object to be used.
<!-- tarav.context 5626cd5f:1d97bbe323b7974f -->

The proposed SKW depot specialization applies this same mechanism rather than
introducing a second type loader; see [typed SKW depots](skillware.md#typed-skw-depots-and-skill-objects).
<!-- tarav.context 5626cd5f:15c442160e6aea5b -->
<!-- tarav.context 5626cd5f:17db8b4a84291879 -->

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

## FileRecord and DirectoryRecord

A Record can be serialized as a single file or as a folder. `FileRecord` and
`DirectoryRecord` name these serialization classifications within the same
Record system; they are registered normally and introduce little additional
semantic distinction. This extends the earlier JSON-file description of a
Record to include a directory representation.
<!-- tarav.context 5626cd5f:7b0dd242ba3a787e -->
<!-- tarav.context 5626cd5f:3842f0da2ff59dac -->

A DirectoryRecord represents a class object serialized as a folder, not merely
a package of peer Records. It contains at least one FileRecord and may also
contain ordinary files. For example, an archived object can have typed
identity, location, and description JSON Records alongside a PDF payload.
Every contained file considered a Record must still have its own class;
the enclosing directory's class does not replace file-level class authority.
<!-- tarav.context 5626cd5f:7779f4e4cc7aa812 -->
<!-- tarav.context 5626cd5f:5f01839cc1b5133f -->

## Directory entry discovery and Type.Resolution.PATH

A DirectoryRecord needs a defined entry FileRecord through which its type can
be discovered. The design supports multiple candidate entry filenames through
an ordered PATH-like mechanism, rather than requiring one reserved filename.
This extends the existing Type.Resolution.PATH principle to directory entry
discovery.
<!-- tarav.context 5626cd5f:82212783f2ac9a06 -->
<!-- tarav.context 5626cd5f:367595f8e9b486a3 -->
<!-- tarav.context 5626cd5f:3568973934e561c5 -->

Discovery has two levels: select the directory's entry FileRecord, then find
the type declaration inside it through Type.Resolution.PATH. The existing
field search is ordered as `__tarav__.type`, then `type`; the first present
location wins, and an invalid value reports a problem rather than falling
through. Directory discovery follows the same ordered, first-present
principle. `__tarav.json`, `main.json`, and `type.json` were the example
directory-entry PATH, not an implemented filename list.
<!-- tarav.context 5626cd5f:3568973934e561c5 -->

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

Some workflows are built into the Tarav monolithic Python library.
<!-- tarav.context 5626cd5f:2d1203966ace2257 -->

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

### Multiple solutions and shared semantics

Tarav is a framework for implementing independent workflows, including ones
whose functionality overlaps. It need not assign one workflow to each use
case. The purpose is to accommodate the natural user/agent collaboration with
as little disruption as possible. Navigation and contextualization workflows
later integrate the data and surface the semantics associated with its capture.
<!-- tarav.context 5626cd5f:ddfdef864f5616bc -->

Capture needs include quick prose, ontology or Model maintenance, sidequest
notes, project design, governing Constitutions, and narrative vaults. A vault
of brainstormed ideas is not a prompt to action. Capture and contextualization
workflows must align on the semantics they share and understand about one
another.
<!-- tarav.context 5626cd5f:00c33b05bf9648f0 -->
<!-- tarav.context 5626cd5f:a719f37fffca3700 -->

### Registered collections

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

## Code organization carries semantic provenance

`Tarav → workflow/container → … → Record` is a useful core organization
because it carries semantics. The class and its owning workflow are part of
the same organization, not separate authorities assigning meaning afterward.
The library's organization should reflect the semantic provenance of the data
and its interpretation. This is a design direction, not a rigid rule.
<!-- tarav.context 5626cd5f:52ed13b302622a2f -->
<!-- tarav.context 5626cd5f:69cda876c9283e57 -->

Another workflow may import the class and produce its Records, but that use
must remain semantically coherent with the class's defining context. Code,
documentation, and skills together supply semantics and must align and
integrate with one another.
<!-- tarav.context 5626cd5f:69cda876c9283e57 -->
<!-- tarav.context 5626cd5f:0e16344825f13f70 -->

## Record → registered class → everything

The class is an informative point of identity: it expresses what the object
can do and how other code uses it. Its central role comes from actionability.
For example, a `help()` method could locate or load additional information,
making the class a default documentation entry point analogous to CLI `-h`.
This is an example, not a settled method signature.
<!-- tarav.context 5626cd5f:0e16344825f13f70 -->
<!-- tarav.context 5626cd5f:f8a3b82cc9a2bc44 -->

The intended discovery path is **Record → registered class → everything**
associated with interpreting and using that Record. The class can delegate;
the principle is reachability through the class, not putting every operation,
document, or skill inside its implementation.
<!-- tarav.context 5626cd5f:d0d46dcff9a8ae26 -->
<!-- tarav.context 5626cd5f:fb625ce84e07a395 -->

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

## Tarav objects and JSON representation

The discussion distinguishes a Tarav object, its actionable interpretation in
code, from a record, its serialized representation, particularly in storage.
The preferred semantic root is `TaravObject`, replacing the storage-oriented
`TaravRecord` name. A separate record subclass is not needed merely to express
serialization; loading is one behavior of the semantic object.
<!-- tarav.context 5626cd5f:a9e2ecce8eb580b5 -->

Shared mechanics can include `help()`, a type label, and a Type Ship UUID,
independently of file, directory, or inline placement. An actionable `SkwBlock`
can therefore remain serialized inside its containing document.
<!-- tarav.context 5626cd5f:40aaf63a879481b3 -->

Writing to storage remains the responsibility of the class or producing
workflow. Tarav formalizes reading into the declared registered class; each
class owns producing a representation that it can interpret.
<!-- tarav.context 5626cd5f:a9e2ecce8eb580b5 -->

The proposed common in-memory representation contract adds `to_json()` and a
static `json_example()`. The example serves both agent documentation and a
minimum default round-trip test for registered classes. It represents the
object, not necessarily whether or how it is stored.
<!-- tarav.context 5626cd5f:d13375746bf42765 -->

Add `from_json(value)` alongside the existing `json_load(file)`: construction
from an in-memory representation and loading a JSON stream remain distinct
entry points.
<!-- tarav.context 5626cd5f:f7163a36d8e7eaec -->

The minimum default test follows example JSON → object → JSON → object → JSON,
checking successful conversion and retained information. This is the default
baseline test for the contract.
<!-- tarav.context 5626cd5f:d13375746bf42765 -->
<!-- tarav.context 5626cd5f:f7163a36d8e7eaec -->
