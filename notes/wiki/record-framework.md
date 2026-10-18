# Tarav as a record framework

<!-- tarav.sessions
473c89a0 = codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8 @473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
1f561f5d = codex:01a0b984-4664-7871-934a-89cf92595b64 @1f561f5d8db849a3a445b83a91a5e94acbb80927f9c332d45322ac70f8705a74
-->

## RecordInterface and representation inheritance

Tarav's Python framework models behavior through classes, while its connected
data is also first-class. Explicit class identity supplies the semantic context
for interpreting an object's JSON representation. `RecordInterface` makes the
representation's structure explicit: required fields, field types, and other
structural constraints belong to an inspectable contract.
<!-- tarav.breadcrumb 2b54bad66623 -->
<!-- tarav.breadcrumb 579f92afc23c -->

`RecordInterface` is basic behavior on `TaravObject` itself. Every subclass
therefore has one through inheritance; it is not an optional workflow feature.
<!-- tarav.breadcrumb 4b2886e2bf0d -->

The discussion selected Pydantic as the machinery for Python field
declarations, validation, and JSON Schema export. The purpose is to express
the data contract alongside the behavioral class, using existing tooling.
Tarav still owns the semantic class identity and its relationship to that
interface. The User requested implementation of this framework.
<!-- tarav.breadcrumb a393a2b5945e -->
<!-- tarav.breadcrumb faa1ee24acc3 -->

Class inheritance and representation inheritance are related but distinct.
A class subtype can preserve or extend its parent's representation, or declare
an independent representation while remaining responsible for its inherited
behavior. Tarav representation subtyping requires class inheritance as well
as interface inheritance; interface ancestry alone does not establish the
semantic class relationship.
<!-- tarav.breadcrumb ece8331d0999 -->

The interface can be declared as a nested Python class. An extension uses
`class RecordInterface(A.RecordInterface)` inside `class B(A)`. An independent
interface uses different ancestry. No `independent_representation` flag is
needed: the declared interface ancestry already exposes the choice.
<!-- tarav.breadcrumb f3132869b61d -->
<!-- tarav.breadcrumb c76f56834b9b -->

## Bound object namespaces — 2026-10-07

The User wants explicit paths such as `obj.records.to_record()` for related behavior on an object. This is an object API organization; Kernel remains the home of `TaravObject` and its Record projection, while the TaravRecords workflow owns storage and navigation. Different workflows may add members to one object namespace. Namespace classes may be defined outside the object classes that select them.
<!-- tarav.breadcrumb 60844174f0fd -->
<!-- tarav.breadcrumb 79a1cfd77e8f -->

The simple pattern uses `NamespaceBase` to bind an object. Independent bases can choose `P = PX` and `P = PY`; a combined class chooses `P = PXY` where `PXY(PX, PY)`. An instance property binds `obj.p`. Class creation checks that the selected `P` subclasses each base contribution, since normal Python MRO would silently choose the first. The check does not merge namespaces automatically.
<!-- tarav.breadcrumb 015955f35c52 -->
<!-- tarav.breadcrumb 4f0153cfc68c -->

[Impl.Req 865](../../../tarav-py/notes/live/865-object-namespaces-and-composition-check-impl-req.md) implemented this in Kernel and added `TaravObject.Records` / `obj.records.to_record()` as the first Record path. Existing root Record calls remain because they are widely used; moving class-level loading and callers into the namespace needs a later bounded migration. The full Python suite passed with 175 tests.
<!-- tarav.breadcrumb 80e3d48a50eb -->

### Namespace style heuristic

Namespaces are a common Tarav API style when a capability is used by sufficiently heterogeneous subtypes, or when a large object benefits from clearer paths. `CheckProvider` illustrates the first case: extending it supplies `.checks`. `project.models` currently illustrates the second: it organizes Project's own API rather than marking an extension. These paths can look alike without implying the same ownership. Abstractness alone is not a reason to namespace a method; a central action such as `Check.run()` can remain direct. The readability gained from a qualified path should justify its extra API machinery.
<!-- tarav.breadcrumb 66e331aefab5 -->
<!-- tarav.breadcrumb 489f0748da4e -->

### Class-side Record namespace

The next bounded implementation lets `SomeType.records.from_record(record)` load a concrete Object Type, paired with `obj.records.to_record()` for projecting an instance. `SomeType.Records` remains the selected namespace class; one descriptor binds its lowercase path to a class or instance. The established validation, exact Type check, construction hook, and supplied Record retention now run inside the namespace. The kernel TypeRegistry uses the class path. Existing direct `from_record()` and `to_record()` calls delegate while broader caller migration remains separate. See the [Kernel Record implementation](../../../../tarav-py/src/tarav/l0/kernel/records.py), [registry](../../../../tarav-py/src/tarav/l0/kernel/types.py), [focused tests](../../../../tarav-py/tests/kernel/test_object_namespaces.py), and [Impl.Req 867](../../../../tarav-py/notes/live/867-record-namespace-class-loading-impl-req.md).
<!-- tarav.breadcrumb 61f25d0f2895 -->
<!-- tarav.breadcrumb 5fa9cc048ac1 -->

### Validation and examples through the class path

`Type.records.validate_record(value)` and `Type.records.record_example()` now give class-bound Record validation and examples. Record projection and loading use the namespaced validation entry. Concrete Types still implement and extend the existing classmethods: many examples are specialized, and some validators rely on `super()`. The namespace delegates to those overrides, preserving behavior without migrating each Type's extension mechanism. The [Kernel implementation](../../../../tarav-py/src/tarav/l0/kernel/records.py), [focused tests](../../../../tarav-py/tests/kernel/test_object_namespaces.py), and [Impl.Req 868](../../../../tarav-py/notes/live/868-record-namespace-validation-and-examples-impl-req.md) show the bounded change.
<!-- tarav.breadcrumb b3b4e90c2318 -->



The predicate API distinguishes the two inheritance dimensions and their
combination. `issubclass(B, A)` checks behavioral inheritance;
`issubrecord(B, A)` checks only whether `B.RecordInterface` inherits
`A.RecordInterface`; and `isrecordsubclass(B, A)` requires both relationships.
`B.preserves_parent_record_interface()` remains the convenience query for all
direct Tarav parents. These are declared-inheritance queries, not proofs that
arbitrary field overrides or method implementations are compatible.
<!-- tarav.breadcrumb 807f9ed50bdd -->
<!-- tarav.breadcrumb 3c0001cfd2eb -->
<!-- tarav.breadcrumb b1f1614ef6ab -->
<!-- tarav.breadcrumb 0da2c639d1ea -->

The earlier `B.is_record_subtype_of(A)` spelling is replaced outright by the
predicate API. Tarav does not retain a compatibility alias or deprecation
layer: current and near-future development explicitly disallows legacy code.
<!-- tarav.breadcrumb 653a96654667 -->

The final default retains ordinary Python inheritance: without a new
declaration, `B.RecordInterface` is the same class as `A.RecordInterface`.
Automatically creating an empty interface subclass for every Tarav class was
considered; retaining the inherited interface was preferred for simplicity.
An explicit interface subclass remains available when a distinct or extended
contract is wanted.
<!-- tarav.breadcrumb 60f5c6dd0bd9 -->
<!-- tarav.breadcrumb 5d2b64f8e6c3 -->

## Type dispatch and class responsibility

Tarav's declared record type maps to a registered Python class and integrates
with ordinary Python class relationships. Interpretation belongs to that
class. Changing a record's type to an incompatible class may produce an error,
for example because required fields do not match. Each class performs its own
due diligence; the framework need not enforce universal correctness before
allowing an object to be used.
<!-- tarav.breadcrumb 032c737393a6 -->

The proposed SKW depot specialization applies this same mechanism rather than
introducing a second type loader; see [typed SKW depots](skillware.md#typed-skw-depots-and-skill-objects).
<!-- tarav.breadcrumb 9f4293fc3438 -->
<!-- tarav.breadcrumb 1f3fdc89e2b0 -->

## Lightweight records and distributed participation

Tarav is a framework library heavily based on lightweight JSON Records.
Projects and subsystems can produce Records and participate in the Tarav
network. Storage can be centralized or linked from repositories outside
Tarav's hosting; the initial scope is local to one computer. The framework
leaves room for different implementations over these Records.
<!-- tarav.breadcrumb ded77359c490 -->

## Records and Artifacts

A Record is Tarav's communication package and data unit: Tarav-consumable
JSON that can contain data, describe something, or point to other data.
Records form a common vocabulary for describing the world around Tarav.
An Artifact is the thing being handled or described, such as a file, folder,
repository, or abstract object. The distinction is contextual rather than a
rigid partition: a Record can itself be treated as an Artifact by another
operation. The stronger defining contract is on the Record side.
<!-- tarav.breadcrumb 4abd01ea2240 -->
<!-- tarav.breadcrumb a50b7312c6df -->

All Records should be lightweight. Archived Records have an especially strong
economy requirement, and Archive-issued Records should be designed for
long-term retention. Preserving knowledge about something need not require
preserving the thing itself; storage commitment can be gradual.
<!-- tarav.breadcrumb 24b9a08ad0f3 -->
<!-- tarav.breadcrumb 81d22f1a896c -->

## FileRecord and DirectoryRecord

A Record can be serialized as a single file or as a folder. `FileRecord` and
`DirectoryRecord` name these serialization classifications within the same
Record system; they are registered normally and introduce little additional
semantic distinction. This extends the earlier JSON-file description of a
Record to include a directory representation.
<!-- tarav.breadcrumb efe1fccd5bbd -->
<!-- tarav.breadcrumb 048ad92564fc -->

A DirectoryRecord represents a class object serialized as a folder, not merely
a package of peer Records. It contains at least one FileRecord and may also
contain ordinary files. For example, an archived object can have typed
identity, location, and description JSON Records alongside a PDF payload.
Every contained file considered a Record must still have its own class;
the enclosing directory's class does not replace file-level class authority.
<!-- tarav.breadcrumb d9dc2548f884 -->
<!-- tarav.breadcrumb 383fa20d5464 -->

## Directory entry discovery and Type.Resolution.PATH

A DirectoryRecord needs a defined entry FileRecord through which its type can
be discovered. The design supports multiple candidate entry filenames through
an ordered PATH-like mechanism, rather than requiring one reserved filename.
This extends the existing Type.Resolution.PATH principle to directory entry
discovery.
<!-- tarav.breadcrumb e08f56daabd1 -->
<!-- tarav.breadcrumb ff5ec9591d95 -->
<!-- tarav.breadcrumb 2cd45bbd4d89 -->

Discovery has two levels: select the directory's entry FileRecord, then find
the type declaration inside it through Type.Resolution.PATH. The existing
field search is ordered as `__tarav__.type`, then `type`; the first present
location wins, and an invalid value reports a problem rather than falling
through. Directory discovery follows the same ordered, first-present
principle. `__tarav.json`, `main.json`, and `type.json` were the example
directory-entry PATH, not an implemented filename list.
<!-- tarav.breadcrumb d240690ece8e -->

## Semantics built on common primitives

Observation times, changing descriptions, and edition histories are semantics
built on Records, not requirements imposed on every Record. The common
primitives must be expressive enough for those different cases. Typed Records
can provide distinct semantics without forcing one universal descriptive or
history model.
<!-- tarav.breadcrumb 562816dc6c71 -->

## Python is the primary programmatic interface

Tarav's main interface is the Python library. Agents can interact through
Python scripts. The CLI is another interface, providing convenience and
efficiency without defining the limits of what workflows can do.
<!-- tarav.breadcrumb d605a18ba628 -->

## Workflows own their implementation and integration

Some workflows are built into the Tarav monolithic Python library.
<!-- tarav.breadcrumb 1ac139c78a51 -->

Tarav supplies primitives and a development environment for multiple capture
workflows. Wiki capture and Model building are distinct examples. Each workflow
can implement what its situation requires and is responsible for hooking into
Tarav when it wants interoperability. User/Agent partitions are specifically
part of the Model workflow, not a universal structure for Tarav Records.
<!-- tarav.breadcrumb bb26dc53b3bf -->

The intended framework includes a Workflow object that external workflows
subtype and register. How external workflow types register their classes and
hook their code is an early design problem. Filesystem paths and entry points
were proposed as an opt-in registration surface; the exact registration
contract remains to be defined.
<!-- tarav.breadcrumb 830262ac036d -->

## Navigation through registered Record providers

### Multiple solutions and shared semantics

Tarav is a framework for implementing independent workflows, including ones
whose functionality overlaps. It need not assign one workflow to each use
case. The purpose is to accommodate the natural user/agent collaboration with
as little disruption as possible. Navigation and contextualization workflows
later integrate the data and surface the semantics associated with its capture.
<!-- tarav.breadcrumb cc5096da4bf9 -->

Capture needs include quick prose, ontology or Model maintenance, sidequest
notes, project design, governing Constitutions, and narrative vaults. A vault
of brainstormed ideas is not a prompt to action. Capture and contextualization
workflows must align on the semantics they share and understand about one
another.
<!-- tarav.breadcrumb 67b3636e82a8 -->
<!-- tarav.breadcrumb 4b39c2637e72 -->

### Registered collections

Records form a graph that Agents should be able to explore through a general
navigation system. The intended experience resembles filesystem navigation:
start at a root listing projects or workflows, enter one, list its contents,
and continue. This is a navigation capability over the Record universe, not
a requirement to store every Record in one physical filesystem.
<!-- tarav.breadcrumb 60e752b38217 -->

Collections become discoverable by registering a subroot rather than
registering every Record individually. A Tarav project, the Tarav Archive,
or a Telegram archive could each expose such an entry point. Navigation is
itself another workflow.
<!-- tarav.breadcrumb 672433158e47 -->

The navigation workflow provides an interface. A collection registers as a
particular type of Record provider, and navigation treats it according to that
type. Registration makes the entry point discoverable; the provider must
actually expose routes to its Records. Errors in fulfilling the navigation
contract surface as POIs.
<!-- tarav.breadcrumb 5cf7be9170f1 -->

## Interpretation authority and compatibility

The registered Python class interpreting a Record's meaning is an invariant.
A proposed consumer rule permits a workflow to interpret Records only through
classes it owns or imports. A search workflow could use a general opaque
Record class that recognizes only minimal common information.
<!-- tarav.breadcrumb e9279b9061bc -->

If workflow A wants compatibility with workflow B, A must make its Records
compatible with B's interface. A supplies the compatibility declaration and
owns conformance. Minimal declarative mappings such as
`A.TypeX.path → B.TypeY.path` may provide flexibility, but interoperability
must not grow into arbitrary conversion code or a web of adapters. A can
change its schema to fit B.
<!-- tarav.breadcrumb 54f706b827a4 -->
<!-- tarav.breadcrumb d72cc98bcb34 -->

## Code organization carries semantic provenance

`Tarav → workflow/container → … → Record` is a useful core organization
because it carries semantics. The class and its owning workflow are part of
the same organization, not separate authorities assigning meaning afterward.
The library's organization should reflect the semantic provenance of the data
and its interpretation. This is a design direction, not a rigid rule.
<!-- tarav.breadcrumb bcea27b13622 -->
<!-- tarav.breadcrumb 468636208723 -->

Another workflow may import the class and produce its Records, but that use
must remain semantically coherent with the class's defining context. Code,
documentation, and skills together supply semantics and must align and
integrate with one another.
<!-- tarav.breadcrumb 431cf2ce0f08 -->
<!-- tarav.breadcrumb 788c979bc1c0 -->

## Record → registered class → everything

The class is an informative point of identity: it expresses what the object
can do and how other code uses it. Its central role comes from actionability.
For example, a `help()` method could locate or load additional information,
making the class a default documentation entry point analogous to CLI `-h`.
This is an example, not a settled method signature.
<!-- tarav.breadcrumb ee5e353c3dab -->
<!-- tarav.breadcrumb 9eff54c77942 -->

The intended discovery path is **Record → registered class → everything**
associated with interpreting and using that Record. The class can delegate;
the principle is reachability through the class, not putting every operation,
document, or skill inside its implementation.
<!-- tarav.breadcrumb c05d4ccd6df4 -->
<!-- tarav.breadcrumb 655db50e2f2d -->

## Code and data evolve together

Tarav is both code and data. Record schemas are not immutable and may change
between versions. Developers are responsible for migrating both code and data;
the system does not owe backward compatibility, legacy readers, or automatic
migrations. Schema evolution is ordinary development work.
<!-- tarav.breadcrumb 33ccf41024cb -->
<!-- tarav.breadcrumb 0f3c422e53be -->

`CODE.NEVER.REPAIR` is an explicit rule, not merely a prohibition on silent
repair. Developer-directed code/data migrations remain part of development.
Archived identity commitments are treated separately in
[Archive as a DOI registry](archive-doi-registry.md).
<!-- tarav.breadcrumb f712edae76e4 -->

## Evolving code, evidence, and deliberate recovery

The system includes its code as the harness, with the executable branch
supplying much of its semantics. Code is not intended to remain static.
Forgotten Records are drift; Tarav does not prescribe a general procedure for
repairing that drift. Maintainers reason from retained evidence, including
Git histories and references to immutable chat corpora, to recover or migrate
the affected material.
<!-- tarav.breadcrumb 74e72bb0104a -->

Independent workflows deliberately allow capture before integration is
understood. Workflows, data, and the user's understanding may evolve together;
a workflow may collect useful data and later be abandoned. Agents can use its
data and evidence to migrate to another workflow. Stabilization is a useful
signal from experience, not something Tarav must predict before capture.
<!-- tarav.breadcrumb 7cb99ce5e0f8 -->

Recovery can be expensive and some situations irrecoverable. Adjacent support
can reduce that risk: the human's memory, independently tracked code and data
repositories, and copies hosted on GitHub or elsewhere. These are recovery
resources, not guarantees. The accepted tradeoff is that high capture friction
loses more than occasional loss or difficult reconstruction; capture and
evolution come first, with efficiency improving through use.
<!-- tarav.breadcrumb 74476d5c1f37 -->

## Tarav objects and JSON representation

The discussion distinguishes a Tarav object, its actionable interpretation in
code, from a record, its serialized representation, particularly in storage.
The preferred semantic root is `TaravObject`, replacing the storage-oriented
`TaravRecord` name. A separate record subclass is not needed merely to express
serialization; loading is one behavior of the semantic object.
<!-- tarav.breadcrumb df77671786de -->

Shared mechanics can include `help()`, a type label, and a Type Ship UUID,
independently of file, directory, or inline placement. An actionable `SkwBlock`
can therefore remain serialized inside its containing document.
<!-- tarav.breadcrumb 241ac81c5e16 -->

Writing to storage remains the responsibility of the class or producing
workflow. Tarav formalizes reading into the declared registered class; each
class owns producing a representation that it can interpret.
<!-- tarav.breadcrumb 204fd53f6e0a -->

The proposed common in-memory representation contract adds `to_json()` and a
static `json_example()`. The example serves both agent documentation and a
minimum default round-trip test for registered classes. It represents the
object, not necessarily whether or how it is stored.
<!-- tarav.breadcrumb b4664956df58 -->

Add `from_json(value)` alongside the existing `json_load(file)`: construction
from an in-memory representation and loading a JSON stream remain distinct
entry points.
<!-- tarav.breadcrumb 865c35d72785 -->

The minimum default test follows example JSON → object → JSON → object → JSON,
checking successful conversion and retained information. This is the default
baseline test for the contract.
<!-- tarav.breadcrumb 287a6730964d -->
<!-- tarav.breadcrumb 18707ec335fa -->

## Record projection and runtime state - v002

The Record contract is refined around the Python class as Tarav's primary
semantic and executable surface. A Record is a projection of a `TaravObject`,
not the object's data model or a required copy of its complete state. The class
chooses which facts the projection contains and may retain additional runtime
state in any form its behavior requires.
<!-- tarav.breadcrumb d9051fa302dc -->
<!-- tarav.breadcrumb 4b6f6aa16537 -->

`RecordInterface` remains required mechanics for `TaravObject`: it declares the
schema Tarav can validate for the selected representation. This requirement
does not impose a common domain schema, storage model, constructor, or
persistence policy. Built-in workflows may define narrower participation
contracts; for example, a Record intended for generic Type dispatch must expose
a usable Type reference through `Type.Resolution.PATH`.
<!-- tarav.breadcrumb 66da9562d54b -->
<!-- tarav.breadcrumb 0ebee0a3ebc7 -->

Tarav may keep a private optional `_record` dictionary because it owns the
loading mechanics. Its meaning is deliberately narrow: `_record` is the
representation supplied when Tarav loaded the object. It is not the object's
source of truth, need not mirror later runtime state, and may remain absent on
an object instantiated entirely at runtime.
<!-- tarav.breadcrumb 0489e037b4d0 -->

The public projection operation follows a template-method boundary:

```python
class TaravObject(TaravType):
    _record: dict[str, JsonValue] | None

    def to_record(self) -> dict[str, JsonValue]:
        candidate = self._to_record()
        # Validate through RecordInterface, detach, and return.

    def _to_record(self) -> dict[str, JsonValue]:
        # Default to the loaded Record or the minimal Type representation.
        ...
```

`to_record()` owns Tarav's validation and detachment workflow. `_to_record()`
is the protected class override point that chooses the current projection from
the loaded Record, runtime state, external state, or a combination. The class
therefore controls representation content while Tarav retains a dependable
integration boundary.
<!-- tarav.breadcrumb ef0700710fbb -->
<!-- tarav.breadcrumb 064d92fcae5e -->

## TaravEntity and durable object identity

`TaravObject` correctly does not require an instance identity. The proposed
`TaravEntity(TaravObject)` adds a durable, non-rebindable identity for objects
that need to serve as external attachment points. Its `id` is a `Ship`; a
plain `TaravObject` may expose computed or session-local context but cannot
receive durable external object-context attachments without a stable address.
<!-- tarav.breadcrumb e39752fae42b -->
<!-- tarav.breadcrumb 932229330f4d -->

Entity identity and storage shape are independent axes. An entity may also be
a `FileRecord` or `DirectoryRecord`, for example through
`Breadcrumb(TaravEntity, DirectoryRecord)`, without making identity mandatory
for every stored Tarav object.
<!-- tarav.breadcrumb d7d003f91cb0 -->

A Ship is first the invariant that one UUID continues to denote the same
semantic point. Some Ships may have resolution or other mechanics, while
others remain searchable invariants. Classes explicitly recognize UUID fields
as Ships; Tarav does not infer Ship semantics merely from UUID-shaped data.
<!-- tarav.breadcrumb 61430e7e064f -->

`TaravEntity.RecordInterface` should type `id` directly as `Ship`. The raw
Record continues to store the UUID as an ordinary JSON string, while the fresh
validated `record_data` view exposes a `Ship`. This requires exact Pydantic
parse-and-serialize support on `Ship`: JSON string → `Ship` → identical JSON
string. Live `Ship` objects remain invalid inside the raw JSON dictionary.
<!-- tarav.breadcrumb a9c9ccdd14b0 -->
<!-- tarav.breadcrumb 8eada3c320a3 -->

## The Diagram as an emergent graph

The Diagram is Tarav's semantic glue: the graph emerging from Records, their
registered Types and classes, Workflows, References, Ships, Entities, and the
relationships declared by individual workflows. It is not limited to objects
retained by a dedicated `tarav.diagram` package. A Record occurrence being
typed by a registered class is already a Diagram relationship.
<!-- tarav.breadcrumb 2e726d799ee6 -->

Tarav Records are lightweight, text-based statements primarily consumed by
Tarav. Tarav owns their schemas and executable semantics while keeping their
common requirements small. Native Artifacts remain separate: workflows may
read or mutate Markdown, code, repositories, chat sessions, and other surfaces
whose storage and lifecycle Tarav does not control. References bridge these
surfaces and may also point to Records, Entities, relationships, or any other
resolvable target inside The Diagram.
<!-- tarav.breadcrumb 12c3d78dcd80 -->
<!-- tarav.breadcrumb 26b610a7b294 -->

Every meaningful Entity should have a representative Record in The Diagram.
A native `TaravEntity` supplies that representation directly; an external
object or Artifact can be represented by an Entity Record that references it.
Workflows naturally operate on both surfaces, maintaining native material and
adding the Records that explain, connect, and contextualize it. Breadcrumbs
are one example of that two-surface operation.
<!-- tarav.breadcrumb 20ac683ab349 -->

## Workflow-centered tarav-py architecture - v001

A Workflow is a named bundle of functionality analogous to an application.
Workflows may overlap and consume one another's public Types while retaining
ownership of their own vocabulary and behavior. Exposing Records and defining
relationships are common capabilities, not the complete definition of a
Workflow.
<!-- tarav.breadcrumb 72ed8af50216 -->

The minimal package split places Tarav's common language and mechanics in
`tarav.kernel`: Records, identity, References, Types, the Workflow base and
registry, and the common space-navigation contract. Named applications live
under `tarav.workflows`; `tarav.runtime` selects and composes them; CLI and
daemon are consumers of the public Python library. Context belongs among the
built-in Workflows rather than forming its own architectural layer.
<!-- tarav.breadcrumb dadb0bb2ca81 -->
<!-- tarav.breadcrumb eba27ce53dd2 -->

`TaravSpace` is the conceptual space produced by registered Workflows, not a
required loaded object. Each Workflow owns how its Records are enumerated and
loaded and may compose reusable general storage mechanics. The Python library
is Tarav's primary interface; agent-written code may query and manipulate it
directly, while CLI and daemon adapt the same library operations.
<!-- tarav.breadcrumb 3598788c9a3a -->
<!-- tarav.breadcrumb d44022ba29f6 -->

## TaravObject as the executable ontology unit - v002

Tarav is an executable ontology made from coupled code and data. Its most
general unit is `TaravObject`, including objects that exist only at runtime.
Every `TaravObject` has a Record representation and default Record mechanics,
but persistence is optional. A Record is deliberately partial; the complete
meaning of the object comes from the Record together with its Python class.
<!-- tarav.breadcrumb bfc59a6bcfb2 -->
<!-- tarav.breadcrumb ba58ac93d7e7 -->

The Diagram emerges from these objects, their executable Types, and the
relationships contributed by code and Records. It is more expressive than a
data-only graph or a code-only object system. The participation rule is:

> A subject belongs to the Diagram when Tarav can represent it as a
> `TaravObject`.

<!-- tarav.breadcrumb c41b1da88bf7 -->
<!-- tarav.breadcrumb 019c05ad9e0e -->

The participation hierarchy separates what exists at class level from what
may be instantiated as a Tarav object:

```python
class TaravType:
    type_name: ClassVar[str]
    type_ship: ClassVar[TypeShip]
    workflow: ClassVar[WorkflowShip]

    @classmethod
    def entity(cls) -> TaravClass: ...

    @classmethod
    def class_context(cls, builder: ContextBuilder) -> None: ...


class TaravObject(TaravType):
    class RecordInterface: ...
    record: dict[str, JsonValue]

    @classmethod
    def from_record(cls, record: Mapping[str, JsonValue]) -> Self: ...

    def to_record(self) -> dict[str, JsonValue]: ...
    def obj_context(self, builder: ContextBuilder) -> None: ...


class TaravEntity(TaravObject):
    id: Ship
```

All maintained Tarav classes should normally extend `TaravType`. This lets
agents discover and accumulate context about Tarav's implementation classes,
including classes whose instances are not `TaravObject`s.
<!-- tarav.breadcrumb de98b15861d6 -->
<!-- tarav.breadcrumb 5a9c95f7ef7a -->

## Reifying Tarav's own code

`TaravClass(TaravEntity)` is the ordinary Tarav-object representation of a
Python class. Calling `SomeType.entity()` returns that representative object.
The Python class and the `TaravClass` Entity are different graph subjects,
connected by the class's `TypeShip`. This removes the need to give Python
classes exceptional Diagram behavior.
<!-- tarav.breadcrumb c8e2d2230def -->
<!-- tarav.breadcrumb 987712e35505 -->
<!-- tarav.breadcrumb e8a2e90f4958 -->

Workflows and Tarav itself follow the same model:

```python
class TaravClass(TaravEntity):
    target: type[TaravType]


class TaravWorkflow(TaravEntity):
    workflow_name: str
    workflow_ship: WorkflowShip


class TaravSystem(TaravEntity): ...


TARAV = TaravSystem(...)
```

A Workflow Entity Ship identifies one Workflow in the Diagram; the Workflow
class's TypeShip identifies its Python Type. The `TARAV` Entity represents the
semantic system, while the `tarav` Python package remains an implementation
Artifact.
<!-- tarav.breadcrumb d76af9d630f9 -->
<!-- tarav.breadcrumb 52c36b896fad -->

## Registry boundary - v002

The Workflow registry is a runtime directory from Workflow name or Ship to a
Workflow instance. It does not own Workflow-to-Type or Type-to-Workflow
semantic relationships. A concrete `TaravObject` Type declares its parent
Workflow directly, giving the minimum semantic path
`Tarav -> Workflow -> Type -> Object`. The Type registry independently maps
Type identity to its Python class.
<!-- tarav.breadcrumb 072123f21788 -->
<!-- tarav.breadcrumb ac85413cfd39 -->

## Implemented bootstrap and documentation boundary - v001

The Python implementation now closes the bootstrap path described above.
`TARAV` is the root `TaravSystem` Entity, `KernelWorkflow` owns foundational
Types, and every registered Type exposes its owning `workflow_ship` through
its `TaravClass` representation. Runtime composition verifies that each of
those Ships resolves through the Workflow registry. Workflow identity
constants remain in their owning domains rather than forming another central
ownership catalog.
<!-- tarav.breadcrumb 9ce1e12d71e9 -->

`tarav-py/ARCHITECTURE.md` is intentionally limited to the executable ontology,
bootstrap path, package layers, ownership boundaries, and integration
invariants. Exact schemas and operations belong to code and tests; design
rationale, alternatives, subsystem narratives, and implementation history
belong in topical Project.Wiki Notes such as this one. This prevents the
architecture overview from becoming a second, stale implementation manual.
<!-- tarav.breadcrumb 71b2069e78ef -->
<!-- tarav.breadcrumb 54700f3fc126 -->

## Code execution and Diagram ontology - v003

The earlier executable-ontology framing is refined by a firm layer boundary:
Python code supplies functionality and execution, while the Tarav Diagram
supplies the ontology. The Diagram records identity, meaning, ownership, and
relationships; it does not replace the Python classes that implement domain
behavior. Workflows may add their own subjects and relationships to the same
general Diagram, whose minimal built-in spine begins with
`TARAV -> Workflow -> Type`.
<!-- tarav.breadcrumb fc06d497466f -->
<!-- tarav.breadcrumb ed406399d956 -->

A Python class participates in that ontology through a common `TaravClass`
Entity. The representative object describes the class but does not execute or
restrict its behavior:

```text
Python class ── represented-by ──> TaravClass
 executable                         ontological
```

The Python class remains free to expose as much functionality as its domain
requires.
<!-- tarav.breadcrumb b4ad7aa9eb13 -->

Class projection uses one explicit code hook and one public normalization
operation:

```python
class ChatTurn(ChatlasObject):
    @classmethod
    def class_entity(cls) -> TaravClass:
        return TaravClass(...)


entity(ChatTurn)  # delegates to ChatTurn.class_entity()
```

`class_entity()` directly constructs the `TaravClass`; a separate declaration
object or nested `from_class()` factory has no established role. Diagram-facing
consumers use the returned `TaravObject` rather than reading `type_ship`, name,
Workflow ownership, or related ontology fields directly from the Python class.
<!-- tarav.breadcrumb 97517b110672 -->
<!-- tarav.breadcrumb a56732aa19ab -->
<!-- tarav.breadcrumb 800cb1e285dc -->

This design deliberately leaves execution on the represented class. The
`class_entity()` method is the projection boundary from code into ontology;
the resulting `TaravClass` is an ordinary Diagram subject, not a wrapper around
the class's runtime behavior.
<!-- tarav.breadcrumb 72cd47f7dfef -->

## Record boundaries and class-owned data interfaces - v003

Record conversion has two symmetric boundary flows. Loading validates a raw
Record before `_from_record()` constructs the object; writing lets
`_to_record()` project the object and then validates and detaches the returned
Record. Validation is what makes both directions coherent. A subtype should
normally extend `super()._to_record()` when its representation extends its
parent's representation, allowing current runtime fields to override loaded
values while preserving compatible extension fields. A Type may instead build
a fresh Record when it deliberately replaces the parent representation.
<!-- tarav.breadcrumb faa6071f18b6 -->

`record_data` is rejected as a common `TaravObject` interface. It would imply
that Tarav defines how classes expose or synchronize their data and would
encourage consumers to treat the Record as the object's data model. Tarav owns
only the boundaries: `Type.validate_record(value)` for explicit validation,
`Type.from_record(value)` for validated construction, and `obj.to_record()` for
validated writing. Each class owns its semantic data interface and any
relationship between runtime state and the optional loader-supplied `_record`.
This decision supersedes the earlier proposal that a fresh `record_data` view
should be the general access path.
<!-- tarav.breadcrumb 53d44cd76286 -->

Subclasses still define shared semantic interfaces where their meaning
requires one. `TaravEntity` therefore defines `id: Ship` as an object field,
and its implementation wires validated Record input to that field and the
field back to the Record projection. Entity specializations may narrow the
field to `TypeShip`, `WorkflowShip`, or another Ship role. This is a promise
made by the Entity abstraction, rather than a generic Record-backed data
interface imposed on every `TaravObject`.
<!-- tarav.breadcrumb 2d55565838e7 -->

## Exact Record loading and Python subtyping

The minimum Record loading hook is `Type.from_record()`: Tarav validates the
incoming representation, then calls the class-owned `_from_record()` hook to
construct the object. A Type may offer other construction paths independently.
Dynamic loading is a separate convenience: `load_object(path)` locates a
Record, resolves its Type through trusted registration, and invokes that
concrete Type's loading path. The registry serves dispatch rather than
becoming the required public entry point for callers.
<!-- tarav.breadcrumb 8aea71e904bb -->
<!-- tarav.breadcrumb db448fac7831 -->
<!-- tarav.breadcrumb a1810783107b -->

`load_object(path, expected_type=SomeType)` combines loading with an assertion:
the resolved class must be exactly `SomeType`. The argument is keyword-only
and does not select construction or accept a subclass as a match. A child
Record therefore fails an expectation of its parent Type. Loading produces
the concrete class named by the Record; it does not perform an upcast.
<!-- tarav.breadcrumb 9106315feb9b -->
<!-- tarav.breadcrumb 733ebc61f02c -->
<!-- tarav.breadcrumb c2b61d17514c -->

The loader-supplied `_record` should correspond to that concrete class. Once
the object has been delivered, Tarav's Type dispatch has no further role in
subtyping. Classes use ordinary Python inheritance and own the behavior of
their parent-child relationships; the Record Type system does not mediate
those relationships.
<!-- tarav.breadcrumb 006720a52c42 -->
<!-- tarav.breadcrumb 7c702794a991 -->
<!-- tarav.breadcrumb bc86e3ede818 -->

## Code, represented classes, and custom graph nodes

A Python class is an executable artifact declaring a Type. Its extracted
class Entity represents that artifact in the Diagram and supplies operations
on the representation; it is not the Python class that defines instance
behavior. Instances of the represented class may themselves be TaravObjects
participating in the Diagram. These are distinct roles to keep visible when
reasoning about code as Tarav's main interface.
<!-- tarav.breadcrumb bfdb14d0c9c3 -->

Archive and Context each define a custom graph. An ArchiveEntry or
ContextEntry is a typed node through which its workflow attaches data and
operations to a value. That value need not be native to the workflow: the
entry lets the workflow establish its own graph around independently
meaningful values. The shared pattern motivates reusable graph primitives.
<!-- tarav.breadcrumb 7fec5255e732 -->

## Optional primitives for custom graphs

Tarav should offer useful primitives for workflows building custom graphs,
including basic dictionaries and vectors, so adopting graphs share familiar
structure. Adoption is optional, and the general foundation should accommodate
multiple parents and cycles rather than require trees. `graph-std` was an
illustrative name for this direction; the User rejected the name, not the
idea. The precise primitive set and interfaces remain to be designed.
<!-- tarav.breadcrumb 32f3c97d243d -->
<!-- tarav.breadcrumb 24778c258384 -->

Python's type hierarchy is a primary means of expressing semantics. A
workflow may define a class for each relationship type, or use a class with
a relationship field whose value is text or another object. These approaches
may coexist. The desired library supplies sensible initial options without
requiring one general encoding of meaning.
<!-- tarav.breadcrumb b6c7bf2bc881 -->
<!-- tarav.breadcrumb eb171d346f5b -->

Semantics can also be implicit in how fields such as `ArchiveEntry.value`
are used across code and retained data; that association need not become a
separate relationship object. Code is an expressive, precise semantic
language. Tarav may be opinionated about the primitives it provides without
prescribing how semantics must be codified in general.
<!-- tarav.breadcrumb 9d7e783d88d3 -->

Generic tooling may rely on exposed contracts, but those contracts do not
exhaust a workflow's meaning. Agents must be able to inspect surrounding
code, data, and evidence for further understanding. This is a fundamental
boundary of the shared primitives, not a requirement to encode all meaning
in their generic interfaces.
<!-- tarav.breadcrumb e8fc9ed0ec06 -->

## Workflow type families and the Type Graph

Workflows can specialize Tarav's own type/object distinction. The proposed
Archive family includes both `ArchiveType` and `ArchiveObject`, rather than
requiring every Archive-owned type to acquire the object contract. This is a
design direction for workflow-specific implementations, not a claim that these
bases have already landed.
<!-- tarav.breadcrumb c1267635ff8c -->

`ArchiveObject` denotes Archive-owned objects, not every value retained by
Archive. Storing a value does not make that value a member of the Archive
workflow's object family.
<!-- tarav.breadcrumb 942cfc967e97 -->

Tarav is also building an ontology of its own types. The discussion uses
“Type Graph” for this graph of Tarav types. Each class has an entity, making
the class itself an attachment point for contextual material rather than only
an implementation of operations.
<!-- tarav.breadcrumb 64a9f039edd8 -->
<!-- tarav.breadcrumb ec3caaf95ad0 -->

Context attached to a class should be inherited by its descendants. This adds
a contextual role to the type relationships themselves; the exact mechanics
of presentation and inheritance are not fixed by this capture. See
[inherited class context](context-graph.md#inherited-class-context).
<!-- tarav.breadcrumb fe90bda0aa29 -->

## Explicit Type Workflow

The Type Graph should have an explicit `TypeWorkflow`. The User accepted
`entity(TaravClass).workflow` identifying that workflow: it owns the type
representation, rather than leaving that responsibility under the broad
Kernel workflow. This records a design decision, not a completed code change.
<!-- tarav.breadcrumb 03a33e668980 -->

Foundational implementation may remain in `tarav.kernel` while its types
belong to more specific workflows. Code location and semantic ownership are
different boundaries; organizing the implementation in Kernel does not
require modeling all of its semantics as one graph.
<!-- tarav.breadcrumb 65d0a876f7db -->

The Type Graph expresses semantics made explicit by types and their declared
relationships. It does not exhaust all system meaning: the User explicitly
accepted the distinction between explicit type semantics and all semantics.
<!-- tarav.breadcrumb 283124bcb33a -->
<!-- tarav.breadcrumb 2b7fdfa72a4c -->

## Type-bound conformance contracts

Behavioral tests can be embedded in the type hierarchy and shipped with the
types. A base type defines a suite that its subtypes must satisfy. These
checks exercise behavior, not merely the existence of interface methods or
test-support hooks. “Type-bound Conformance Contracts” names this design
pattern in the discussion; it is not yet a claim of implementation.
<!-- tarav.breadcrumb 59f892891698 -->

Test support belongs to the implementation interface too: subtypes must
provide what is necessary for the inherited tests to exercise them. The
hierarchy therefore supplies attachment points for specific tests and the
support those tests require, rather than leaving all testing knowledge in a
separate repository-local suite.
<!-- tarav.breadcrumb 6290a90b71c3 -->
<!-- tarav.breadcrumb a3df25528ce5 -->

The User explicitly affirmed the combined role of the hierarchy: operational
capabilities, contextual knowledge, and executable behavioral obligations.
The Type Graph makes that structure discoverable. This extends its purpose
beyond representing executable inheritance alone.
<!-- tarav.breadcrumb ba570865c883 -->

## Record namespace extension migration — 2026-10-08

The User then chose to migrate the extension mechanism itself. Each specializing Type now defines a nested `Records` subclass; its `validate_record()` and `record_example()` methods operate on the bound concrete Type. Namespace inheritance preserves the same `super()` relationship that the earlier classmethod overrides used. Maintained Object callers use `Type.records` or `obj.records`, and `TaravObject` no longer exposes the duplicate direct Record methods. `_record`, `_from_record()`, and `_to_record()` remain object state and protected hooks. The [Kernel implementation](../../../../tarav-py/src/tarav/l0/kernel/records.py), [architecture contract](../../../../tarav-py/ARCHITECTURE.md), and [Impl.Req 870](../../../../tarav-py/notes/live/870-record-namespace-extension-migration-impl-req.md) show the migration scope.
<!-- tarav.breadcrumb e06f472c6ea1 -->
<!-- tarav.breadcrumb c52f427a9b74 -->
