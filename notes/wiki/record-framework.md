# Tarav as a record framework

<!-- tarav.sessions
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

## Evolving code, evidence, and deliberate recovery

The system includes its code as the harness, with the executable branch
supplying much of its semantics. Code is not intended to remain static.
Forgotten Records are drift; Tarav does not prescribe a general procedure for
repairing that drift. Maintainers reason from retained evidence, including
Git histories and references to immutable chat corpora, to recover or migrate
the affected material.
<!-- tarav.breadcrumb 74e72bb0104a5e51f256dd1a46de2f518c47edf669a28d8901da2e2082a09c22 -->

Independent workflows deliberately allow capture before integration is
understood. Workflows, data, and the user's understanding may evolve together;
a workflow may collect useful data and later be abandoned. Agents can use its
data and evidence to migrate to another workflow. Stabilization is a useful
signal from experience, not something Tarav must predict before capture.
<!-- tarav.breadcrumb 7cb99ce5e0f8e779adf947e7337283d8ac1eedbceed4bf07e40ad1a404d985b1 -->

Recovery can be expensive and some situations irrecoverable. Adjacent support
can reduce that risk: the human's memory, independently tracked code and data
repositories, and copies hosted on GitHub or elsewhere. These are recovery
resources, not guarantees. The accepted tradeoff is that high capture friction
loses more than occasional loss or difficult reconstruction; capture and
evolution come first, with efficiency improving through use.
<!-- tarav.breadcrumb 74476d5c1f379d9c97ca25a99dd4f55b2be5962f77d381cff5028d84bf849045 -->

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

## Record projection and runtime state - v002

The Record contract is refined around the Python class as Tarav's primary
semantic and executable surface. A Record is a projection of a `TaravObject`,
not the object's data model or a required copy of its complete state. The class
chooses which facts the projection contains and may retain additional runtime
state in any form its behavior requires.
<!-- tarav.breadcrumb d9051fa302dcf24ebbbd370b2d803e2d206d3a28fa324e10cc47973b341038f5 -->
<!-- tarav.breadcrumb 4b6f6aa1653782f81ea5187e8c7c6e8da569b53cf443b3828578e987e6aedfb4 -->

`RecordInterface` remains required mechanics for `TaravObject`: it declares the
schema Tarav can validate for the selected representation. This requirement
does not impose a common domain schema, storage model, constructor, or
persistence policy. Built-in workflows may define narrower participation
contracts; for example, a Record intended for generic Type dispatch must expose
a usable Type reference through `Type.Resolution.PATH`.
<!-- tarav.breadcrumb 66da9562d54b4118a4f734359aabc3795f6ff9e51624541d64cc60f1310fba02 -->
<!-- tarav.breadcrumb 0ebee0a3ebc79acc7f673e747833941456388ccbbed3adb718ade8703c5fd14f -->

Tarav may keep a private optional `_record` dictionary because it owns the
loading mechanics. Its meaning is deliberately narrow: `_record` is the
representation supplied when Tarav loaded the object. It is not the object's
source of truth, need not mirror later runtime state, and may remain absent on
an object instantiated entirely at runtime.
<!-- tarav.breadcrumb 0489e037b4d0d6df679259643a9c02c9015004006174012cea016d3ce5ab32e3 -->

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
<!-- tarav.breadcrumb ef0700710fbbe090339255510fd9755534b4eb447ff73b772e4c818cbc2e4a0f -->
<!-- tarav.breadcrumb 064d92fcae5e0a75250139ca9ec2d6539c2b78f21df0977b9aa77161c2e7375c -->

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

## TaravObject as the executable ontology unit - v002

Tarav is an executable ontology made from coupled code and data. Its most
general unit is `TaravObject`, including objects that exist only at runtime.
Every `TaravObject` has a Record representation and default Record mechanics,
but persistence is optional. A Record is deliberately partial; the complete
meaning of the object comes from the Record together with its Python class.
<!-- tarav.breadcrumb bfc59a6bcfb2a688e01ce4c0d08bd35287b864d1fe35b7268018043b9e6e0e20 -->
<!-- tarav.breadcrumb ba58ac93d7e70c5e8cfd96c68a21ac8172248886b20e832cc59c953286d23bf5 -->

The Diagram emerges from these objects, their executable Types, and the
relationships contributed by code and Records. It is more expressive than a
data-only graph or a code-only object system. The participation rule is:

> A subject belongs to the Diagram when Tarav can represent it as a
> `TaravObject`.

<!-- tarav.breadcrumb c41b1da88bf7ffdb0ec2167003c26b133f6be6fe48bb317bf37edf0120708c2b -->
<!-- tarav.breadcrumb 019c05ad9e0ea4931d7b71324a1c0eb81f3a28d268037c690150a3dd3964584f -->

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
<!-- tarav.breadcrumb de98b15861d6a65f962d74325461fdac88845420495776c69eb041be60f73f1c -->
<!-- tarav.breadcrumb 5a9c95f7ef7a66ef2ebd7164fa85c597d62e6deb1d4ce7acb37b48c4c58cfaaa -->

## Reifying Tarav's own code

`TaravClass(TaravEntity)` is the ordinary Tarav-object representation of a
Python class. Calling `SomeType.entity()` returns that representative object.
The Python class and the `TaravClass` Entity are different graph subjects,
connected by the class's `TypeShip`. This removes the need to give Python
classes exceptional Diagram behavior.
<!-- tarav.breadcrumb c8e2d2230defb7106df27f8fdaa259fa9e9538039f6f4fdfcd1723409d9e1f1e -->
<!-- tarav.breadcrumb 987712e35505971a02965f238050adc56bfe32db50a02b77b2bee4d6a62bb59c -->
<!-- tarav.breadcrumb e8a2e90f4958b2da89a04c63490e2fbcd4f00bfc81fd9c7b6649cb5dca00d5f7 -->

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
<!-- tarav.breadcrumb d76af9d630f96086996c4bc1198bb987ed8bfcaf66e841d263fe85d024675034 -->
<!-- tarav.breadcrumb 52c36b896fad0f62cc6f9577194eb1a5db0f846d40bb7decdc709439705fbe46 -->

## Registry boundary - v002

The Workflow registry is a runtime directory from Workflow name or Ship to a
Workflow instance. It does not own Workflow-to-Type or Type-to-Workflow
semantic relationships. A concrete `TaravObject` Type declares its parent
Workflow directly, giving the minimum semantic path
`Tarav -> Workflow -> Type -> Object`. The Type registry independently maps
Type identity to its Python class.
<!-- tarav.breadcrumb 072123f2178871c90e6d27723dec1b9edea0f15525045bebfe4fc5467dd19646 -->
<!-- tarav.breadcrumb ac85413cfd395b0e13e11e6fb796b62fb7d42c84ad2599c7ca0c4959a921b4b8 -->

## Implemented bootstrap and documentation boundary - v001

The Python implementation now closes the bootstrap path described above.
`TARAV` is the root `TaravSystem` Entity, `KernelWorkflow` owns foundational
Types, and every registered Type exposes its owning `workflow_ship` through
its `TaravClass` representation. Runtime composition verifies that each of
those Ships resolves through the Workflow registry. Workflow identity
constants remain in their owning domains rather than forming another central
ownership catalog.
<!-- tarav.breadcrumb 9ce1e12d71e9769dd8a6a44c050a281eee5b61fe594a02beefabbb58b02bb85f -->

`tarav-py/ARCHITECTURE.md` is intentionally limited to the executable ontology,
bootstrap path, package layers, ownership boundaries, and integration
invariants. Exact schemas and operations belong to code and tests; design
rationale, alternatives, subsystem narratives, and implementation history
belong in topical Project.Wiki Notes such as this one. This prevents the
architecture overview from becoming a second, stale implementation manual.
<!-- tarav.breadcrumb 71b2069e78ef70d59e14e7a9e119b5234cc09f113fa9470b07f99ff899a555da -->
<!-- tarav.breadcrumb 54700f3fc1266ed8c4dff8951c72ed457672ed724dc754ee93c9cf0a705969f4 -->

## Code execution and Diagram ontology - v003

The earlier executable-ontology framing is refined by a firm layer boundary:
Python code supplies functionality and execution, while the Tarav Diagram
supplies the ontology. The Diagram records identity, meaning, ownership, and
relationships; it does not replace the Python classes that implement domain
behavior. Workflows may add their own subjects and relationships to the same
general Diagram, whose minimal built-in spine begins with
`TARAV -> Workflow -> Type`.
<!-- tarav.breadcrumb fc06d497466fa54642dd838eb23ed52774fa4af71017281176cc45af2f168cd6 -->
<!-- tarav.breadcrumb ed406399d9566bf872af3dc9d11818f437b76aad06cf19899cd81ebe7f632aae -->

A Python class participates in that ontology through a common `TaravClass`
Entity. The representative object describes the class but does not execute or
restrict its behavior:

```text
Python class ── represented-by ──> TaravClass
 executable                         ontological
```

The Python class remains free to expose as much functionality as its domain
requires.
<!-- tarav.breadcrumb b4ad7aa9eb13dd64ca57296fc8567ccdfb25166f3def8417229774c2788d7927 -->

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
<!-- tarav.breadcrumb 97517b1106723f4217c68f7e63acf1bc402bb502b6b1a45594fa32bf40e1995d -->
<!-- tarav.breadcrumb a56732aa19ab9986c586ed6ebe36396b095d7308d45d00f829ccbc3cc8768342 -->
<!-- tarav.breadcrumb 800cb1e285dc9b64d90d7670e804d81f6a0c2e914cf80374076c11c60227a5df -->

This design deliberately leaves execution on the represented class. The
`class_entity()` method is the projection boundary from code into ontology;
the resulting `TaravClass` is an ordinary Diagram subject, not a wrapper around
the class's runtime behavior.
<!-- tarav.breadcrumb 72cd47f7dfeffc9022ded6d3c7851cc2c39b0259c67563e39868a28e70e6b2c5 -->

## Record boundaries and class-owned data interfaces - v003

Record conversion has two symmetric boundary flows. Loading validates a raw
Record before `_from_record()` constructs the object; writing lets
`_to_record()` project the object and then validates and detaches the returned
Record. Validation is what makes both directions coherent. A subtype should
normally extend `super()._to_record()` when its representation extends its
parent's representation, allowing current runtime fields to override loaded
values while preserving compatible extension fields. A Type may instead build
a fresh Record when it deliberately replaces the parent representation.
<!-- tarav.breadcrumb faa6071f18b612639be2e06cd95ff11bb7cd7b768766be1dc9ffcb13b2f807ab -->

`record_data` is rejected as a common `TaravObject` interface. It would imply
that Tarav defines how classes expose or synchronize their data and would
encourage consumers to treat the Record as the object's data model. Tarav owns
only the boundaries: `Type.validate_record(value)` for explicit validation,
`Type.from_record(value)` for validated construction, and `obj.to_record()` for
validated writing. Each class owns its semantic data interface and any
relationship between runtime state and the optional loader-supplied `_record`.
This decision supersedes the earlier proposal that a fresh `record_data` view
should be the general access path.
<!-- tarav.breadcrumb 53d44cd762867e44ff1b3fd72667d4f62598232673ed62ad590e09c76ee6295a -->

Subclasses still define shared semantic interfaces where their meaning
requires one. `TaravEntity` therefore defines `id: Ship` as an object field,
and its implementation wires validated Record input to that field and the
field back to the Record projection. Entity specializations may narrow the
field to `TypeShip`, `WorkflowShip`, or another Ship role. This is a promise
made by the Entity abstraction, rather than a generic Record-backed data
interface imposed on every `TaravObject`.
<!-- tarav.breadcrumb 2d55565838e701685ac70371765ebe4941473c9a25f93a40b13ffc34bf236f5c -->

## Exact Record loading and Python subtyping

The minimum Record loading hook is `Type.from_record()`: Tarav validates the
incoming representation, then calls the class-owned `_from_record()` hook to
construct the object. A Type may offer other construction paths independently.
Dynamic loading is a separate convenience: `load_object(path)` locates a
Record, resolves its Type through trusted registration, and invokes that
concrete Type's loading path. The registry serves dispatch rather than
becoming the required public entry point for callers.
<!-- tarav.breadcrumb 8aea71e904bbf3a46a5bdbde66c8c65c0fdd77f8dd19641172dcafb4512c86f2 -->
<!-- tarav.breadcrumb db448fac783164661cf60272531112c708896ea9b36f54083cf2ba56a03c40b6 -->
<!-- tarav.breadcrumb a1810783107b50e21421e4420d88326cfc73feedf4adeee31fa5ac1691b7f54f -->

`load_object(path, expected_type=SomeType)` combines loading with an assertion:
the resolved class must be exactly `SomeType`. The argument is keyword-only
and does not select construction or accept a subclass as a match. A child
Record therefore fails an expectation of its parent Type. Loading produces
the concrete class named by the Record; it does not perform an upcast.
<!-- tarav.breadcrumb 9106315feb9b5bd75eb65c8ce4a737644bf133255b1ecf62efc62065dd6a2810 -->
<!-- tarav.breadcrumb 733ebc61f02c0124f14e5f2d36fc31b37cf002f64b510766719c4d9f5f9a47a4 -->
<!-- tarav.breadcrumb c2b61d17514c5425e3feab9d48c3c5447ec5f470fd2c05303dc08674225457aa -->

The loader-supplied `_record` should correspond to that concrete class. Once
the object has been delivered, Tarav's Type dispatch has no further role in
subtyping. Classes use ordinary Python inheritance and own the behavior of
their parent-child relationships; the Record Type system does not mediate
those relationships.
<!-- tarav.breadcrumb 006720a52c424af38c7ce76c87196b438d3ad1e3b8e50efec90c9588453e7188 -->
<!-- tarav.breadcrumb 7c702794a99124c3d5c5cd7b5ac2cd4fcfcb241f7deb2a10a93247ba5a5a5379 -->
<!-- tarav.breadcrumb bc86e3ede818cd1c613d31425c6c1069deaec9fedba596474239548ec5aef3a6 -->

## Code, represented classes, and custom graph nodes

A Python class is an executable artifact declaring a Type. Its extracted
class Entity represents that artifact in the Diagram and supplies operations
on the representation; it is not the Python class that defines instance
behavior. Instances of the represented class may themselves be TaravObjects
participating in the Diagram. These are distinct roles to keep visible when
reasoning about code as Tarav's main interface.
<!-- tarav.breadcrumb bfdb14d0c9c36645176902d1c8ac2d11b41bb104c46edac3e10198aa0d4c9f88 -->

Archive and Context each define a custom graph. An ArchiveEntry or
ContextEntry is a typed node through which its workflow attaches data and
operations to a value. That value need not be native to the workflow: the
entry lets the workflow establish its own graph around independently
meaningful values. The shared pattern motivates reusable graph primitives.
<!-- tarav.breadcrumb 7fec5255e73246e7dbacb2e48bc05378cc2345ce37b8b1fcde70483f0d5ad3d3 -->

## Optional primitives for custom graphs

Tarav should offer useful primitives for workflows building custom graphs,
including basic dictionaries and vectors, so adopting graphs share familiar
structure. Adoption is optional, and the general foundation should accommodate
multiple parents and cycles rather than require trees. `graph-std` was an
illustrative name for this direction; the User rejected the name, not the
idea. The precise primitive set and interfaces remain to be designed.
<!-- tarav.breadcrumb 32f3c97d243d2b05fe17c5822d76999155d952684fd9ee694fffe363fcc17449 -->
<!-- tarav.breadcrumb 24778c258384ba600e45dfcbe8359d6560be999e26ed79e4cd874c77f13ed9ab -->

Python's type hierarchy is a primary means of expressing semantics. A
workflow may define a class for each relationship type, or use a class with
a relationship field whose value is text or another object. These approaches
may coexist. The desired library supplies sensible initial options without
requiring one general encoding of meaning.
<!-- tarav.breadcrumb b6c7bf2bc88116b857ec2d42c0fd3e22f6547bad844832138c9ae9e7bfb8a99d -->
<!-- tarav.breadcrumb eb171d346f5b8cd119235a1ffbf257a6619c820b21376f762db07060bacd54b8 -->

Semantics can also be implicit in how fields such as `ArchiveEntry.value`
are used across code and retained data; that association need not become a
separate relationship object. Code is an expressive, precise semantic
language. Tarav may be opinionated about the primitives it provides without
prescribing how semantics must be codified in general.
<!-- tarav.breadcrumb 9d7e783d88d3ae3f236f68a7a6ae58e0b968123b92d7d148256eff5012c20075 -->

Generic tooling may rely on exposed contracts, but those contracts do not
exhaust a workflow's meaning. Agents must be able to inspect surrounding
code, data, and evidence for further understanding. This is a fundamental
boundary of the shared primitives, not a requirement to encode all meaning
in their generic interfaces.
<!-- tarav.breadcrumb e8fc9ed0ec065997a6f784745a2a380c04789782dc55cf8f9a7188071d8c84a5 -->

## Workflow type families and the Type Graph

Workflows can specialize Tarav's own type/object distinction. The proposed
Archive family includes both `ArchiveType` and `ArchiveObject`, rather than
requiring every Archive-owned type to acquire the object contract. This is a
design direction for workflow-specific implementations, not a claim that these
bases have already landed.
<!-- tarav.breadcrumb c1267635ff8ced126983e12fc36de77466f59b391beea939122f3f2383d4658d -->

`ArchiveObject` denotes Archive-owned objects, not every value retained by
Archive. Storing a value does not make that value a member of the Archive
workflow's object family.
<!-- tarav.breadcrumb 942cfc967e97564204ebef386402c1e1ded899d99e127cb1a853776bfe28f1a5 -->

Tarav is also building an ontology of its own types. The discussion uses
“Type Graph” for this graph of Tarav types. Each class has an entity, making
the class itself an attachment point for contextual material rather than only
an implementation of operations.
<!-- tarav.breadcrumb 64a9f039edd87162df3ee3aac86d85d96d9de97bb0cf819da84a63d263fded61 -->
<!-- tarav.breadcrumb ec3caaf95ad044cbb47d1db64d7c8eae4de5eddb4ab975d7865cdb6f248aa010 -->

Context attached to a class should be inherited by its descendants. This adds
a contextual role to the type relationships themselves; the exact mechanics
of presentation and inheritance are not fixed by this capture. See
[inherited class context](context-graph.md#inherited-class-context).
<!-- tarav.breadcrumb fe90bda0aa299fa5d3f910bd93911e91738db0416e4161c8b70b39d96b55a3d3 -->

## Explicit Type Workflow

The Type Graph should have an explicit `TypeWorkflow`. The User accepted
`entity(TaravClass).workflow` identifying that workflow: it owns the type
representation, rather than leaving that responsibility under the broad
Kernel workflow. This records a design decision, not a completed code change.
<!-- tarav.breadcrumb 03a33e668980b7387eaca3ba20bbb525877cb7279c574de6a91708269cb30578 -->

Foundational implementation may remain in `tarav.kernel` while its types
belong to more specific workflows. Code location and semantic ownership are
different boundaries; organizing the implementation in Kernel does not
require modeling all of its semantics as one graph.
<!-- tarav.breadcrumb 65d0a876f7db6ccbd9a93f4e68af685269a320e1efc9fb0a2f7f443d44ec2cdd -->

The Type Graph expresses semantics made explicit by types and their declared
relationships. It does not exhaust all system meaning: the User explicitly
accepted the distinction between explicit type semantics and all semantics.
<!-- tarav.breadcrumb 283124bcb33a02fab1c40afb5a15484298967f3f157dd936e69e25c4ad45b6bf -->
<!-- tarav.breadcrumb 2b7fdfa72a4c8d092b22d2f828decba573e968ffa82ed07e8deaf0425347e761 -->
