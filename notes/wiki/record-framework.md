# Tarav as a record framework

<!-- tarav.sessions
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
1f561f5d = codex:01a0b984-4664-7871-934a-89cf92595b64 @1f561f5d8db849a3a445b83a91a5e94acbb80927f9c332d45322ac70f8705a74
-->

## RecordInterface and representation inheritance

Tarav's Python framework models behavior through classes, while its connected
data is also first-class. Explicit class identity supplies the semantic context
for interpreting an object's JSON representation. `RecordInterface` makes the
representation's structure explicit: required fields, field types, and other
structural constraints belong to an inspectable contract.
<!-- tarav.breadcrumb 2b54bad666232d542391910f8214cad878114f55db5955faf9194885c4b2b583 -->
<!-- tarav.breadcrumb 579f92afc23cb805d9cb86ec93b790d6377fa32875a77c37dc5ba53d9a3f7d0e -->

`RecordInterface` is basic behavior on `TaravObject` itself. Every subclass
therefore has one through inheritance; it is not an optional workflow feature.
<!-- tarav.breadcrumb 4b2886e2bf0da0cad6f0a2e3077d0e93699aae5cadf3018dc3a52b4a7696eadc -->

The discussion selected Pydantic as the machinery for Python field
declarations, validation, and JSON Schema export. The purpose is to express
the data contract alongside the behavioral class, using existing tooling.
Tarav still owns the semantic class identity and its relationship to that
interface. The User requested implementation of this framework.
<!-- tarav.breadcrumb a393a2b5945e0b864a5d359eaf0b7c0642cb731f1579b196f08e747ed8ae3114 -->
<!-- tarav.breadcrumb faa1ee24acc352f667bff7fd3dca273dc181a20ce5061770ac92b525888d282a -->

Class inheritance and representation inheritance are related but distinct.
A class subtype can preserve or extend its parent's representation, or declare
an independent representation while remaining responsible for its inherited
behavior. Tarav representation subtyping requires class inheritance as well
as interface inheritance; interface ancestry alone does not establish the
semantic class relationship.
<!-- tarav.breadcrumb ece8331d0999bb768a01c9e9af2bd8e70cae6c560f1b80780748ba65dcca71aa -->

The interface can be declared as a nested Python class. An extension uses
`class RecordInterface(A.RecordInterface)` inside `class B(A)`. An independent
interface uses different ancestry. No `independent_representation` flag is
needed: the declared interface ancestry already exposes the choice.
<!-- tarav.breadcrumb f3132869b61d5cb6c7f4b068a85e9fb160d49601c476dad27ffaf954887845e1 -->
<!-- tarav.breadcrumb c76f56834b9b306ee0d0b2305dc1843906f12a4345f2646e1201e6939a703258 -->

The predicate API distinguishes the two inheritance dimensions and their
combination. `issubclass(B, A)` checks behavioral inheritance;
`issubrecord(B, A)` checks only whether `B.RecordInterface` inherits
`A.RecordInterface`; and `isrecordsubclass(B, A)` requires both relationships.
`B.preserves_parent_record_interface()` remains the convenience query for all
direct Tarav parents. These are declared-inheritance queries, not proofs that
arbitrary field overrides or method implementations are compatible.
<!-- tarav.breadcrumb 807f9ed50bdda2a36f16ad13cb67bd78d7457bc10802f15c20598af591d274ba -->
<!-- tarav.breadcrumb 3c0001cfd2eb90530cfd21b1b8dc1908402175da114f396f891deeb3ed85fb42 -->
<!-- tarav.breadcrumb b1f1614ef6aba2f86a504dcf9abc993f91104258f00e22066577ab9a34f8375a -->
<!-- tarav.breadcrumb 0da2c639d1ea0c08cb447a5986f9105fddc1b8e5f5de55348c97f3c05abbebf1 -->

The earlier `B.is_record_subtype_of(A)` spelling is replaced outright by the
predicate API. Tarav does not retain a compatibility alias or deprecation
layer: current and near-future development explicitly disallows legacy code.
<!-- tarav.breadcrumb 653a9665466719d9ad020b0555093bc61b7446e5509ef62341ced043c93a8f26 -->

The final default retains ordinary Python inheritance: without a new
declaration, `B.RecordInterface` is the same class as `A.RecordInterface`.
Automatically creating an empty interface subclass for every Tarav class was
considered; retaining the inherited interface was preferred for simplicity.
An explicit interface subclass remains available when a distinct or extended
contract is wanted.
<!-- tarav.breadcrumb 60f5c6dd0bd9211932b5f12a1c816245f098ffb8e1a2aac2cf743ee57378a7ad -->
<!-- tarav.breadcrumb 5d2b64f8e6c3fad529e1daa7ffc1e838af15a6c950043131ff2dff28d50de4be -->

## Type dispatch and class responsibility

Tarav's declared record type maps to a registered Python class and integrates
with ordinary Python class relationships. Interpretation belongs to that
class. Changing a record's type to an incompatible class may produce an error,
for example because required fields do not match. Each class performs its own
due diligence; the framework need not enforce universal correctness before
allowing an object to be used.
<!-- tarav.breadcrumb 032c737393a69dd842bbfb1a8fcb6ee63a18e0b2a5cd66109e7184378cb2b58c -->

The proposed SKW depot specialization applies this same mechanism rather than
introducing a second type loader; see [typed SKW depots](skillware.md#typed-skw-depots-and-skill-objects).
<!-- tarav.breadcrumb 9f4293fc3438db5fb3156f1fdf1df812cbd9c4e2814c59480d3c2a0a37d7ab73 -->
<!-- tarav.breadcrumb 1f3fdc89e2b06b01c5622966906439c38d150935ce6e7cbfb078e8a2460b15c7 -->

## Lightweight records and distributed participation

Tarav is a framework library heavily based on lightweight JSON Records.
Projects and subsystems can produce Records and participate in the Tarav
network. Storage can be centralized or linked from repositories outside
Tarav's hosting; the initial scope is local to one computer. The framework
leaves room for different implementations over these Records.
<!-- tarav.breadcrumb ded77359c490e31502883c360b16cd08307f1530bc683e5fbf9f36065067d071 -->

## Records and Artifacts

A Record is Tarav's communication package and data unit: Tarav-consumable
JSON that can contain data, describe something, or point to other data.
Records form a common vocabulary for describing the world around Tarav.
An Artifact is the thing being handled or described, such as a file, folder,
repository, or abstract object. The distinction is contextual rather than a
rigid partition: a Record can itself be treated as an Artifact by another
operation. The stronger defining contract is on the Record side.
<!-- tarav.breadcrumb 4abd01ea224088ac39fcf52d969bae6ed8990b1dd29dd7eb1b31e1b54e8f9a4d -->
<!-- tarav.breadcrumb a50b7312c6df48bed2d9123e1a1a18c7df7567d9f8cb156a2a012984b7835d4b -->

All Records should be lightweight. Archived Records have an especially strong
economy requirement, and Archive-issued Records should be designed for
long-term retention. Preserving knowledge about something need not require
preserving the thing itself; storage commitment can be gradual.
<!-- tarav.breadcrumb 24b9a08ad0f38392e6cb3fec01622e7fd16ae098e039d34ea41ab0cb82fec1ce -->
<!-- tarav.breadcrumb 81d22f1a896c8596ac439ff25a21407af140cdc404df7da1c094cec2b3a603fa -->

## FileRecord and DirectoryRecord

A Record can be serialized as a single file or as a folder. `FileRecord` and
`DirectoryRecord` name these serialization classifications within the same
Record system; they are registered normally and introduce little additional
semantic distinction. This extends the earlier JSON-file description of a
Record to include a directory representation.
<!-- tarav.breadcrumb efe1fccd5bbd7234da82f031f4226fbbee0c15fb4a92e529e7b6af2b3204c0b7 -->
<!-- tarav.breadcrumb 048ad92564fced981e173b076fa180fd3f2aec385dadaa8fcaaf147050358f7f -->

A DirectoryRecord represents a class object serialized as a folder, not merely
a package of peer Records. It contains at least one FileRecord and may also
contain ordinary files. For example, an archived object can have typed
identity, location, and description JSON Records alongside a PDF payload.
Every contained file considered a Record must still have its own class;
the enclosing directory's class does not replace file-level class authority.
<!-- tarav.breadcrumb d9dc2548f8844cee9658138914ac25df0cfa7d0608a80b8eb31bc64be4808fe1 -->
<!-- tarav.breadcrumb 383fa20d5464342f10e1e482390f186509413021168e7ac936857c8a821eb67c -->

## Directory entry discovery and Type.Resolution.PATH

A DirectoryRecord needs a defined entry FileRecord through which its type can
be discovered. The design supports multiple candidate entry filenames through
an ordered PATH-like mechanism, rather than requiring one reserved filename.
This extends the existing Type.Resolution.PATH principle to directory entry
discovery.
<!-- tarav.breadcrumb e08f56daabd112ed06f1cfabb28ee9a1fe055a29504a0ad1bc373441c6317f52 -->
<!-- tarav.breadcrumb ff5ec9591d957fb9681033601ed0309e820ca0325715ae090150ea1c464b6fd8 -->
<!-- tarav.breadcrumb 2cd45bbd4d89a4feab5e75ef9e3427782a34292515c1c2fe85e1607ff25c9e89 -->

Discovery has two levels: select the directory's entry FileRecord, then find
the type declaration inside it through Type.Resolution.PATH. The existing
field search is ordered as `__tarav__.type`, then `type`; the first present
location wins, and an invalid value reports a problem rather than falling
through. Directory discovery follows the same ordered, first-present
principle. `__tarav.json`, `main.json`, and `type.json` were the example
directory-entry PATH, not an implemented filename list.
<!-- tarav.breadcrumb d240690ece8e20a156fe629cbf7c35c3ac9c8c517a2ea448609c6d50b1033d2e -->

## Semantics built on common primitives

Observation times, changing descriptions, and edition histories are semantics
built on Records, not requirements imposed on every Record. The common
primitives must be expressive enough for those different cases. Typed Records
can provide distinct semantics without forcing one universal descriptive or
history model.
<!-- tarav.breadcrumb 562816dc6c718b0d1e943a72e0237320d80a98f4a02eaa4550c44220de392798 -->

## Python is the primary programmatic interface

Tarav's main interface is the Python library. Agents can interact through
Python scripts. The CLI is another interface, providing convenience and
efficiency without defining the limits of what workflows can do.
<!-- tarav.breadcrumb d605a18ba62862b5c613413de2377bb689ade9824442ac6ba8d076b49af9402f -->

## Workflows own their implementation and integration

Some workflows are built into the Tarav monolithic Python library.
<!-- tarav.breadcrumb 1ac139c78a5151569f5992c18788f90235329be375dc75e49815c65366ee1552 -->

Tarav supplies primitives and a development environment for multiple capture
workflows. Wiki capture and Model building are distinct examples. Each workflow
can implement what its situation requires and is responsible for hooking into
Tarav when it wants interoperability. User/Agent partitions are specifically
part of the Model workflow, not a universal structure for Tarav Records.
<!-- tarav.breadcrumb bb26dc53b3bfa1d2928cf421eb65d551b816e2ae100afa9d129e42ed24a08cbf -->

The intended framework includes a Workflow object that external workflows
subtype and register. How external workflow types register their classes and
hook their code is an early design problem. Filesystem paths and entry points
were proposed as an opt-in registration surface; the exact registration
contract remains to be defined.
<!-- tarav.breadcrumb 830262ac036d236f0127e5880d9d84abeda928e9f0029c5bf4f23c26fda9e06a -->

## Navigation through registered Record providers

### Multiple solutions and shared semantics

Tarav is a framework for implementing independent workflows, including ones
whose functionality overlaps. It need not assign one workflow to each use
case. The purpose is to accommodate the natural user/agent collaboration with
as little disruption as possible. Navigation and contextualization workflows
later integrate the data and surface the semantics associated with its capture.
<!-- tarav.breadcrumb cc5096da4bf9aa8beedf19dfd985cc83c35ed105feb708f53e64aa0010309549 -->

Capture needs include quick prose, ontology or Model maintenance, sidequest
notes, project design, governing Constitutions, and narrative vaults. A vault
of brainstormed ideas is not a prompt to action. Capture and contextualization
workflows must align on the semantics they share and understand about one
another.
<!-- tarav.breadcrumb 67b3636e82a873361c9cc95ebafbaa68499d2c5847f790c0e2b910e206fe5ba8 -->
<!-- tarav.breadcrumb 4b39c2637e72cf4b1abf2ae3d54a6def52eeb1d131906c4d82816ce854541415 -->

### Registered collections

Records form a graph that Agents should be able to explore through a general
navigation system. The intended experience resembles filesystem navigation:
start at a root listing projects or workflows, enter one, list its contents,
and continue. This is a navigation capability over the Record universe, not
a requirement to store every Record in one physical filesystem.
<!-- tarav.breadcrumb 60e752b38217e1d45c57c4c286b526760557fbb469274170ec03a20f502a5381 -->

Collections become discoverable by registering a subroot rather than
registering every Record individually. A Tarav project, the Tarav Archive,
or a Telegram archive could each expose such an entry point. Navigation is
itself another workflow.
<!-- tarav.breadcrumb 672433158e47f93600c73b3120149e782c7bae791b7429bf5ae024d855575aaa -->

The navigation workflow provides an interface. A collection registers as a
particular type of Record provider, and navigation treats it according to that
type. Registration makes the entry point discoverable; the provider must
actually expose routes to its Records. Errors in fulfilling the navigation
contract surface as POIs.
<!-- tarav.breadcrumb 5cf7be9170f1ab197122bb88ff892edb0f587d45e1721ff6e5bc11f20c449909 -->

## Interpretation authority and compatibility

The registered Python class interpreting a Record's meaning is an invariant.
A proposed consumer rule permits a workflow to interpret Records only through
classes it owns or imports. A search workflow could use a general opaque
Record class that recognizes only minimal common information.
<!-- tarav.breadcrumb e9279b9061bcaba087066429bbe37d970311cb3c536101f7d8b03fb911ea7728 -->

If workflow A wants compatibility with workflow B, A must make its Records
compatible with B's interface. A supplies the compatibility declaration and
owns conformance. Minimal declarative mappings such as
`A.TypeX.path → B.TypeY.path` may provide flexibility, but interoperability
must not grow into arbitrary conversion code or a web of adapters. A can
change its schema to fit B.
<!-- tarav.breadcrumb 54f706b827a47afb8cd3693a238ca4937bdf298a30c535b281c43965bc3e4901 -->
<!-- tarav.breadcrumb d72cc98bcb343d420ebaec65df1f6996c4069cc38a4c229b64d31b77bc299e60 -->

## Code organization carries semantic provenance

`Tarav → workflow/container → … → Record` is a useful core organization
because it carries semantics. The class and its owning workflow are part of
the same organization, not separate authorities assigning meaning afterward.
The library's organization should reflect the semantic provenance of the data
and its interpretation. This is a design direction, not a rigid rule.
<!-- tarav.breadcrumb bcea27b136229621dcb732840bf589804e0ff81857bcefd0b1ee6e9e18194567 -->
<!-- tarav.breadcrumb 468636208723f7100b2cfc5ce0c281ac4f9691a554574f89bedf9645d8e569fa -->

Another workflow may import the class and produce its Records, but that use
must remain semantically coherent with the class's defining context. Code,
documentation, and skills together supply semantics and must align and
integrate with one another.
<!-- tarav.breadcrumb 431cf2ce0f086e6e8248674dc711e13490edb9e44b369f54b79d899e81ba0623 -->
<!-- tarav.breadcrumb 788c979bc1c0f3798fcadcc1bcc2711adc5d7e6a6c381ae06b5380686f48b05d -->

## Record → registered class → everything

The class is an informative point of identity: it expresses what the object
can do and how other code uses it. Its central role comes from actionability.
For example, a `help()` method could locate or load additional information,
making the class a default documentation entry point analogous to CLI `-h`.
This is an example, not a settled method signature.
<!-- tarav.breadcrumb ee5e353c3dab05b6a104cc25f1c64c269fb99ceb959c8a3f3d52abadbddc69f0 -->
<!-- tarav.breadcrumb 9eff54c779426b2f7a6425b486a13c7f1972ebb6edd9b11e747b6d800b7cf70c -->

The intended discovery path is **Record → registered class → everything**
associated with interpreting and using that Record. The class can delegate;
the principle is reachability through the class, not putting every operation,
document, or skill inside its implementation.
<!-- tarav.breadcrumb c05d4ccd6df470fe865ad0a09047c8d29898c5d175e8a3c93b20d650bc6ac356 -->
<!-- tarav.breadcrumb 655db50e2f2de032ad85b6416f163dec0770b298b14407a90e14311abeec4da7 -->

## Code and data evolve together

Tarav is both code and data. Record schemas are not immutable and may change
between versions. Developers are responsible for migrating both code and data;
the system does not owe backward compatibility, legacy readers, or automatic
migrations. Schema evolution is ordinary development work.
<!-- tarav.breadcrumb 33ccf41024cbb7a783f97c92d8e935d0fdb4c308e1654082414ae15c5616f603 -->
<!-- tarav.breadcrumb 0f3c422e53be9d174543815c2074531bf1d4c6f91edb36be08f71fb0a487fa28 -->

`CODE.NEVER.REPAIR` is an explicit rule, not merely a prohibition on silent
repair. Developer-directed code/data migrations remain part of development.
Archived identity commitments are treated separately in
[Archive as a DOI registry](archive-doi-registry.md).
<!-- tarav.breadcrumb f712edae76e4bd0568b789ecd64fccd7aed48bb96f32427f98c8e2bbda4ca0d7 -->

## Tarav objects and JSON representation

The discussion distinguishes a Tarav object, its actionable interpretation in
code, from a record, its serialized representation, particularly in storage.
The preferred semantic root is `TaravObject`, replacing the storage-oriented
`TaravRecord` name. A separate record subclass is not needed merely to express
serialization; loading is one behavior of the semantic object.
<!-- tarav.breadcrumb df77671786deec9e98222a13cc5a4c7b5e00c4a5033ce934ed8af09c61b60ce3 -->

Shared mechanics can include `help()`, a type label, and a Type Ship UUID,
independently of file, directory, or inline placement. An actionable `SkwBlock`
can therefore remain serialized inside its containing document.
<!-- tarav.breadcrumb 241ac81c5e16be65c94162a2c52f879fbe5f0b57c3a20b0846c5fdabe9d18abf -->

Writing to storage remains the responsibility of the class or producing
workflow. Tarav formalizes reading into the declared registered class; each
class owns producing a representation that it can interpret.
<!-- tarav.breadcrumb 204fd53f6e0a045b82f474cbfa8200db04f4672b58a6a4c9ea0f1792b91cd3aa -->

The proposed common in-memory representation contract adds `to_json()` and a
static `json_example()`. The example serves both agent documentation and a
minimum default round-trip test for registered classes. It represents the
object, not necessarily whether or how it is stored.
<!-- tarav.breadcrumb b4664956df581c5c7209ecffe2abbf4c30dad34282580e80ddb704038c958e92 -->

Add `from_json(value)` alongside the existing `json_load(file)`: construction
from an in-memory representation and loading a JSON stream remain distinct
entry points.
<!-- tarav.breadcrumb 865c35d72785011e65ccc1bcdfc336571e60ff7a8252db9986905de0145f456f -->

The minimum default test follows example JSON → object → JSON → object → JSON,
checking successful conversion and retained information. This is the default
baseline test for the contract.
<!-- tarav.breadcrumb 287a6730964db738a305daca57b51c5750ae3dfc02aa4ec899f997457c880116 -->
<!-- tarav.breadcrumb 18707ec335faf77e7a09b70cf449810e4b819af838e24abb992ba1475c04d4a8 -->

## TaravEntity and durable object identity

`TaravObject` correctly does not require an instance identity. The proposed
`TaravEntity(TaravObject)` adds a durable, non-rebindable identity for objects
that need to serve as external attachment points. Its `id` is a `Ship`; a
plain `TaravObject` may expose computed or session-local context but cannot
receive durable external object-context attachments without a stable address.
<!-- tarav.breadcrumb e39752fae42b4815b13cfd21a19ef636ec366c908c3fcffa70f609fa90fe912b -->
<!-- tarav.breadcrumb 932229330f4d8c2a2a6bcdad8367c0d66b1c5b80432ad8fd718821e6e56f5b0b -->

Entity identity and storage shape are independent axes. An entity may also be
a `FileRecord` or `DirectoryRecord`, for example through
`Breadcrumb(TaravEntity, DirectoryRecord)`, without making identity mandatory
for every stored Tarav object.
<!-- tarav.breadcrumb d7d003f91cb02a8fb1567f3ad4a8e877fe8d69b5c670c64c5c5e026f138c3cb8 -->

A Ship is first the invariant that one UUID continues to denote the same
semantic point. Some Ships may have resolution or other mechanics, while
others remain searchable invariants. Classes explicitly recognize UUID fields
as Ships; Tarav does not infer Ship semantics merely from UUID-shaped data.
<!-- tarav.breadcrumb 61430e7e064f9344d4c03532f52ddb54db144c027604f996eb0ef9983ce3b51f -->

`TaravEntity.RecordInterface` should type `id` directly as `Ship`. The raw
Record continues to store the UUID as an ordinary JSON string, while the fresh
validated `record_data` view exposes a `Ship`. This requires exact Pydantic
parse-and-serialize support on `Ship`: JSON string → `Ship` → identical JSON
string. Live `Ship` objects remain invalid inside the raw JSON dictionary.
<!-- tarav.breadcrumb a9c9ccdd14b0be4ca55ecfb4565c8109096ec4de066074f52b19e2fcdee39bbc -->
<!-- tarav.breadcrumb 8eada3c320a324bcb6cc8db81e90835fcc3d25d8b929c10d3a03220c030e9a12 -->

## The Diagram as an emergent graph

The Diagram is Tarav's semantic glue: the graph emerging from Records, their
registered Types and classes, Workflows, References, Ships, Entities, and the
relationships declared by individual workflows. It is not limited to objects
retained by a dedicated `tarav.diagram` package. A Record occurrence being
typed by a registered class is already a Diagram relationship.
<!-- tarav.breadcrumb 2e726d799ee679547b9f88dd0122adbf3629ef22692b29f898b213b0755397dd -->

Tarav Records are lightweight, text-based statements primarily consumed by
Tarav. Tarav owns their schemas and executable semantics while keeping their
common requirements small. Native Artifacts remain separate: workflows may
read or mutate Markdown, code, repositories, chat sessions, and other surfaces
whose storage and lifecycle Tarav does not control. References bridge these
surfaces and may also point to Records, Entities, relationships, or any other
resolvable target inside The Diagram.
<!-- tarav.breadcrumb 12c3d78dcd80d5753b5e6dcba712c80e59bad2cd171b00c73d04b0141fc4962e -->
<!-- tarav.breadcrumb 26b610a7b294b25298754cf27693992a2eeb3748f43c034bfe7fbaa75720346c -->

Every meaningful Entity should have a representative Record in The Diagram.
A native `TaravEntity` supplies that representation directly; an external
object or Artifact can be represented by an Entity Record that references it.
Workflows naturally operate on both surfaces, maintaining native material and
adding the Records that explain, connect, and contextualize it. Breadcrumbs
are one example of that two-surface operation.
<!-- tarav.breadcrumb 20ac683ab349eb6a8cb663eafe2c51db16995ebf8135560ad7874011846721a5 -->

## Workflow-centered tarav-py architecture - v001

A Workflow is a named bundle of functionality analogous to an application.
Workflows may overlap and consume one another's public Types while retaining
ownership of their own vocabulary and behavior. Exposing Records and defining
relationships are common capabilities, not the complete definition of a
Workflow.
<!-- tarav.breadcrumb 72ed8af50216a16dd83c4bbdbcb623f9e4a9b4d383b3c2913ab55110163fa007 -->

The minimal package split places Tarav's common language and mechanics in
`tarav.kernel`: Records, identity, References, Types, the Workflow base and
registry, and the common space-navigation contract. Named applications live
under `tarav.workflows`; `tarav.runtime` selects and composes them; CLI and
daemon are consumers of the public Python library. Context belongs among the
built-in Workflows rather than forming its own architectural layer.
<!-- tarav.breadcrumb dadb0bb2ca81d85491fd78a4d7a5c89f16d7a639f7b05d6db3faef4b3a192218 -->
<!-- tarav.breadcrumb eba27ce53dd22756218ee1cf4269db4fbbaacb2f091be2f1bfc007778fe016c1 -->

`TaravSpace` is the conceptual space produced by registered Workflows, not a
required loaded object. Each Workflow owns how its Records are enumerated and
loaded and may compose reusable general storage mechanics. The Python library
is Tarav's primary interface; agent-written code may query and manipulate it
directly, while CLI and daemon adapt the same library operations.
<!-- tarav.breadcrumb 3598788c9a3ae8a5f609dd2109ed03cab78f89bb0ac0f32d7bf9d55ed3a4e553 -->
<!-- tarav.breadcrumb d44022ba29f67ee89b87373c289a953a42f9aa2640f975176a2b5ac41ea6a347 -->
