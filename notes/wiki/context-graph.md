# Context Graph

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
1f561f5d = codex:01a0b984-4664-7871-934a-89cf92595b64 @1f561f5d8db849a3a445b83a91a5e94acbb80927f9c332d45322ac70f8705a74
473c89a0 = codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8 @473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f
-->

## Progressive discovery

Tarav should provide a general progressive-discovery workflow for its typed
objects. Type dispatch already gives every Record a dependable route to its
registered Python class. Static `help()` remains the small Type-level entry
point and advertises `context()` as the expandable route to further material.
<!-- tarav.breadcrumb 44e28180e63d -->
<!-- tarav.breadcrumb ab1c76383e0c -->

Both classes and identified objects expose context through the same mechanism.
`Class.context()` concerns the Type itself; `object.context()` concerns that
particular object and may include its Type context. Context is reactive:
systems may contribute material to a class or object, and the owning class may
discover further context from its current state and typed relationships.
<!-- tarav.breadcrumb 516a49ca2f67 -->

## General navigation and later specialization

The base navigation workflow aims at general-purpose semantic coverage, not
an initial claim of efficiency. More specialized workflows can later provide
summaries, bundles, vector databases, or other access paths. The bootstrap
system presents evidence for agents to reason over; prescribing their analysis
requires care, and further workflows can improve how current understanding
is presented.
<!-- tarav.breadcrumb e0689f6022ba -->

The Diagram is a non-compulsory language intended to express any semantics
and connect Tarav's components, including Chatlas, archives, and its own code.
The intended invariant is that anything in the Diagram is connected somehow.
Disconnected components are defects to fix by connecting them. Agents can
also escalate to their own tools; Diagram navigation is not their only means
of investigation. This is a design aim, not a report that every component is
already connected.
<!-- tarav.breadcrumb 072672c882e3 -->

## Virtual directory over a graph

The candidate `Context.Graph.Workflow` presents context as a virtual directory
rooted at its subject. It may contain named entries, nested directories, full
Records, references, text, collections, and computed projections. The backing
data need not be a filesystem directory. Agents progressively navigate with
filesystem-like operations such as listing, bounded head or tail reads, and
full reads.
<!-- tarav.breadcrumb 312c500173ae -->
<!-- tarav.breadcrumb a4f60eab4c66 -->

The directory is a navigation projection over a graph rather than the object's
identity or physical storage. The same node may be reachable through several
paths, references may cross between subtrees, and traversal must tolerate
cycles. Context can be owned by the subject, contributed by registered
systems, or discovered from current graph state.
<!-- tarav.breadcrumb 444689fa8d74 -->
<!-- tarav.breadcrumb 8e63a1cec571 -->

## Durable context roots

Class context has a durable attachment root in the class's `TypeShip`.
Object-level durable context requires an addressed entity, motivating
`TaravEntity(TaravObject)` with a non-rebindable `id: Ship`. Plain
`TaravObject`s may still provide computed or session-local context, but
external systems cannot durably attach context to them without stable
identity.
<!-- tarav.breadcrumb 2987564fe199 -->
<!-- tarav.breadcrumb 853f360bd376 -->

Ships are semantic identity opportunities, not a mandatory bundle of
mechanics. A Ship may support specialized behavior or remain only an invariant
that agents and systems can search for. The non-rebinding rule lets context,
observations, references, and editions accumulate around one semantic point
without changing what its UUID denotes.
<!-- tarav.breadcrumb 913654b4a1a8 -->

Entity identity remains independent of storage shape. The same entity may be
a file-backed or directory-backed Record. Its retained JSON stores the UUID as
a string, while its `RecordInterface` exposes `id` as a `Ship` through an exact
Pydantic round trip.
<!-- tarav.breadcrumb 3220134b4379 -->
<!-- tarav.breadcrumb 77ceef64c159 -->
<!-- tarav.breadcrumb b9d2cc0f78e1 -->

## Context as one graph-building workflow - v001

The broader Tarav graph is not formed by an Entity subsystem or Context alone.
It emerges from the typed relationships contributed by multiple independent
Workflows. The kernel supplies identity, Record, Reference, registration, and
navigation mechanics without owning the vocabulary of those relationships.
<!-- tarav.breadcrumb d07452c4d6a0 -->

Context is one built-in Workflow within that ecology. It supplies a
filesystem-shaped organization around a Record or Entity: literal Records can
live in the context, References can point elsewhere, and Entity links can lead
to other stable subjects. Agents choose which paths and links to follow, while
the contributing Workflows retain ownership of the attached Records' meaning.
<!-- tarav.breadcrumb e4795a494347 -->

In the minimal `tarav-py` architecture, Context therefore belongs with the
named Workflows. Generic Record, Workflow, registry, identity, Reference, and
space-navigation mechanics belong in the kernel. This preserves Context as a
central reusable workflow without turning it into Tarav's central semantic
authority.
<!-- tarav.breadcrumb c624689f980b -->

## Context as core Diagram navigation - v002

This supersedes the v001 placement of Context as an optional built-in
Workflow. Tarav needs a small explicit bootstrap layer so agents can discover
the available Types and Workflows without an infinite dependency on another
discovery Workflow. Context is therefore a core Diagram operation: it opens a
subject as a progressively navigable view, comparable to opening a filesystem
node as a directory.
<!-- tarav.breadcrumb 7f73ad586de0 -->

The canonical interface is a global function with two specialization hooks:

```python
def context(subject: TaravType | TaravObject) -> Context: ...


class TaravType:
    @classmethod
    def class_context(cls, builder: ContextBuilder) -> None: ...


class TaravObject(TaravType):
    def obj_context(self, builder: ContextBuilder) -> None: ...
```

The function normalizes whether the subject is a class or an instance and
invokes the appropriate hook. This avoids special descriptor or metaclass
machinery solely to overload the same `context()` spelling at both levels.
<!-- tarav.breadcrumb afc71d04e032 -->
<!-- tarav.breadcrumb b32246240652 -->

`context(subject)` returns a lazy `Context` navigation view with operations
such as `ls()` and `open()`. A `Context` instance is not currently a
`TaravObject` or a Diagram subject; it is a view over the Diagram. Its
`Context` class still extends `TaravType`, so the class is reified by
`TaravClass` and agents can navigate documentation and usage context for it.
This cleanly separates class participation from instance participation.
<!-- tarav.breadcrumb f55534adb58f -->
<!-- tarav.breadcrumb 141c2d19566a -->
<!-- tarav.breadcrumb 1141cd37c63f -->

The minimal representative navigation Types are:

```python
class Context(TaravType):
    subject: TaravType | TaravObject

    def ls(self) -> Sequence[ContextEntry]: ...
    def open(self, name: str) -> Context | TaravObject | Reference: ...


class ContextEntry(TaravType): ...
class ContextBuilder(TaravType): ...
```

Their exact schemas and persistence remain intentionally undefined. The first
use case is bounded, progressive navigation; retained context snapshots can be
introduced later if a concrete need appears.
<!-- tarav.breadcrumb 171ca91cb68d -->
<!-- tarav.breadcrumb 2e6ccd42a166 -->
<!-- tarav.breadcrumb 50998722e225 -->

## Context directory and cursor - v003

This advances v002's runtime-only navigation view with durable context
attached to Entities. The proposed retained namespace is
`~/Documents/tarav/contexts/`, with one root directory per Entity identity.
Workflows can contribute Records there. Nested folders are represented by
`DirectoryRecord`s; each level keeps a cheap registry of its immediate entries
so `ls()` does not load the child objects or their full Records. Opening a
retained Record uses trusted Type dispatch.
<!-- tarav.breadcrumb db2a880936c9 -->
<!-- tarav.breadcrumb c97f8df49550 -->

`Context` is read-only with respect to the tree but stateful as a navigation
cursor. `cd()` changes the current directory within the subject's context;
`ls()` reads only cheap directory information. Runtime contributions and
retained entries share the same virtual namespace and navigation operations,
without a separate runtime-versus-disk branch in the public view.
<!-- tarav.breadcrumb 52dcf7c6538d -->
<!-- tarav.breadcrumb 1d7b6c4151a5 -->

The directory-like contract is `Context: name -> TaravObject | Context`.
`open(name)` returns either an object or a nested Context; `cd(name)` enters a
nested Context. The name is held by the containing Context, so an object can
appear in a context without knowing its placement. A retained entry resolves
through the Record registry; a runtime entry is supplied by its context
provider. This replaces v002's tentative `open()` return union with the
agreed object-or-context form.
<!-- tarav.breadcrumb 7beba2e1ed51 -->
<!-- tarav.breadcrumb b3f501443dcc -->
<!-- tarav.breadcrumb 4268e797c21f -->

## Archive-backed context organization - v004

This advances v003's retained-directory proposal: the Context workflow uses
Record Archive for durable placement instead of maintaining a separate Context
store and entry index. An identified subject's Ship addresses its logical
context root in the Context workflow's Archive partition. The root's physical
Archive location can remain opaque. Classes use their `TaravClass` Ships;
Entities use their own Ships. Unidentified objects can still contribute
runtime context without a durable root.
<!-- tarav.breadcrumb 38a58bcfe8d4 -->

The Context root is a read-only navigation view that composes runtime hooks
with retained Archive entries. Archive owns storage, placement, and Git
behavior; Context owns the subject-relative view and opening behavior. A
subject-specific typed Archive can retain the subject Ship in its Record so
opening by identity verifies the binding independently of the Archive's own
identity. The existing `ContextDirectoryRecord` and `ContextPlacement` index
would no longer be needed as a parallel storage format.
<!-- tarav.breadcrumb 4b694a679ccf -->

`ContextEntry` is the lazy wrapper around one placement. It can wrap an
`ArchiveEntry` for retained material or an opener for a runtime contribution;
opening yields a `TaravObject` or a nested Context. The target object need not
know its context placement. Dictionary and Vector Context types present named
and positional navigation over the corresponding Archive structures. The root
for `context(obj)` is a dictionary so runtime and retained names can share one
namespace; nested dictionaries and vectors let contributors organize context
as needed.
<!-- tarav.breadcrumb 76b9d3e934c9 -->

A Vector Context position is a mutable placement, not a subject identity.
Insertion may shift positions; Ships and References remain the stable way to
address subjects. Listing should read placement metadata without loading
contained objects, while `open()` resolves only the selected target.
<!-- tarav.breadcrumb 2adbc657ea53 -->

## Context entries and exploration - v005

This revises v004's tentative treatment of `ContextEntry` as a wrapper around
`ArchiveEntry`. The two are independent wrappers. Where context is retained in
an Archive, its `ArchiveEntry` contains a `ContextEntry` Record as cargo; the
`ContextEntry` in turn contains another typed Record as its cargo. Archive
owns storage and placement, while Context owns the meaning of the context
entry. A direct Record and a Reference Record are both possible cargo types.
`ContextEntry.open()` returns the cargo object; if it is a Reference, a caller
may separately call `entry.open().resolve()`.
<!-- tarav.breadcrumb 343f6bd4a7b5 -->
<!-- tarav.breadcrumb d8d776cda81f -->

The runtime `ContextEntry` exposes its name or vector position even when that
placement comes from its containing `ArchiveEntry` and is not duplicated in
the retained Context Record. Context need not subtype Archive: runtime-only
entries have no Archive backing. An Archive-backed entry can expose its
`ArchiveEntry` for Archive operations, while its ordinary Context interface
works for either source. The writer explicitly chooses the cargo Record and
lets Context wrap it before Archive stores the Context entry.
<!-- tarav.breadcrumb 321e4c2856ea -->
<!-- tarav.breadcrumb a690be883fbe -->

Each Entity's context is a separate navigable graph. Opening another Entity
through an entry and calling `context()` on it can cross from one graph to
another; their Records need not share an Archive root. `ContextExplorer` is
the stateful navigation object for moving within a context and remembering
the route across such jumps. Runtime entries encountered through an explorer
carry their placement and navigation origin so backward navigation can return
to the occurrence from which the jump was made.
<!-- tarav.breadcrumb 9ce43b45f8e2 -->
<!-- tarav.breadcrumb 1be53811fcb7 -->

Calling `context(entry)` follows that entry's cargo context in the *same*
explorer, retaining its route for backward navigation. Calling
`context(entity)` directly starts a new, independent explorer because the
Entity carries no navigation history. Explorer bindings belong to runtime
entry handles, so separate explorers can visit the same retained placement
independently. The exact navigation method names remain open to implementation.
<!-- tarav.breadcrumb ea2147a4b4e1 -->

## Connectivity and specialized contextualization

The current focus is connecting all of Tarav's components so an agent can
find material when it chooses to investigate. Shared contracts do not exhaust
the system's semantics: agents can inspect surrounding code, data, and
evidence. This states the connectivity objective, not a claim that universal
reachability is already implemented.
<!-- tarav.breadcrumb 9d798d43f901 -->

Access to the broader connected material is compatible with controlling the
order in which an agent encounters it. Tarav can shape contextualization by
ordering what it presents, analogous to search-result ordering. Specialized
contextualizing workflows can improve navigation over that foundation;
connectivity and the quality of a particular presentation are separate
concerns.
<!-- tarav.breadcrumb b2531bdef685 -->

## Shared Explorer primitives

Archive and Context have common exploration needs, including navigation
history. A shared Explorer base should provide reusable behavior while their
workflow-specific explorers remain distinct types. The interface should be
inspired by Linux filesystem operations such as `ls`, `cd`, and `open`.
<!-- tarav.breadcrumb 4024720bca2f -->
<!-- tarav.breadcrumb 306b47ab23be -->

The selected minimal vocabulary is `ExplorerEntry`, `ExplorerFolder`,
`ExplorerList`, and `Explorer`. An entry opens a value and carries specialized
data and operations. A Folder exposes entries by name; a List exposes entries
by position. Either container can itself be an entry's value. Explorer
provides the navigation interface and history. `ExplorerList` replaces the
tentative `ExplorerVector` name, and `ExplorerFolder` replaces the proposed
generic Dictionary name.
<!-- tarav.breadcrumb a60a060fbb95 -->
<!-- tarav.breadcrumb 6463be3aedde -->
<!-- tarav.breadcrumb 873c1d56454a -->

The accepted minimal interface uses `ls()` to list entries, `get(key)` to
select an entry, and `open(key)` to obtain its value without navigating.
`cd(key)` enters a navigable value, `pwd()` describes the current location,
and `back()` / `forward()` traverse exploration history. Back and parent are
distinct: back retraces the route taken, while parent belongs to the graph's
relationships and may be absent or non-unique. Concrete graph semantics remain
with the workflow specializations.
<!-- tarav.breadcrumb 24a92a55bc2f -->
<!-- tarav.breadcrumb f12bdc592780 -->
<!-- tarav.breadcrumb 90b99d5f735f -->

A shared Location type was removed from the proposal because no shared
operative semantics justified it. Base types should provide meaningful
behavior or enforce useful contracts, rather than exist only as attractive
names. The four-type interface is a design direction; this capture does not
claim that the common base types or their implementations already exist.
<!-- tarav.breadcrumb 7af4d6f74ae0 -->
<!-- tarav.breadcrumb 78c2ac5b7c20 -->

## Common protocols, independent graphs

The purpose of the Explorer interface is to establish minimal shared mechanics,
method names, and base typings across workflows. Agents reuse their knowledge
of the interface while navigating different graphs; implementing the same
interface does not merge Archive and Context or require cross-workflow traversal.
<!-- tarav.breadcrumb c7690be3dcb6 -->
<!-- tarav.breadcrumb 1a90f3a79e25 -->

Concrete types express which graph is being navigated. `cd(key)` enters a
location navigable within that explorer's graph. Opening an Archive value from
a Context entry does not make the value a Context location: opening the value
and rejecting Context navigation into it are compatible behaviors. This
clarifies the graph-specific meaning of “navigable” in the earlier interface.
<!-- tarav.breadcrumb 04220218921f -->
<!-- tarav.breadcrumb 3c84863a06ff -->

Moving between graphs requires explicit jump points. For example, an agent can
ask for the Workflow owning a Context type, then ask the Archive for that
Workflow's partition. The Workflow provides the explicit connection between
the two explorations; sharing an Explorer interface does not itself supply
that connection.
<!-- tarav.breadcrumb da7186b82e26 -->

## Shared conformance support

A general test suite should exercise the common Explorer contracts. New
implementations can register their classes, and the classes must also provide
what is required to test them, including their implementation-specific fixture
or factory support. The shared interface and the support needed to verify it
are both part of the intended implementation participation.
<!-- tarav.breadcrumb 40828ea2c25c -->
<!-- tarav.breadcrumb 821fe44d4eda -->

## Membership and navigation capabilities

The User brought forward a design discussion separating workflow membership
from navigation capabilities: an Archive-specific base identifies Archive
membership, while shared Explorer mechanics check whether the current value
supports folder or list operations. That discussion places capability checking
at the Explorer level rather than duplicating it in each workflow explorer.
<!-- tarav.breadcrumb 6ac3d1f32341 -->

The subsequent proposal distinguishes `ArchiveType` and `ArchiveObject`,
mirroring Tarav's own levels. Workflow membership need not collapse the
distinction between a type with executable behavior and an object with a
Record representation.
<!-- tarav.breadcrumb ac8d1acaab95 -->

## Inherited class context

Each class has an entity to which contextual material can be attached. The
User wants that class context to be inherited by child classes. Tarav's own
Type Graph therefore provides a structure for contextual inheritance as well
as describing the types of the system itself.
<!-- tarav.breadcrumb 4d742b647c41 -->
<!-- tarav.breadcrumb b718e2b810f8 -->

This captures the inheritance objective, not a settled implementation of
copying, traversal, eager loading, ordering, or conflict resolution. The
discussion establishes inherited class context without selecting those
mechanics.
<!-- tarav.breadcrumb 1d38b4616418 -->

## Layered Context implementation

The user requested execution of the [822 Context split](../../../tarav-py/notes/live/822-context-layer-split-impl-req.md).
Standalone Types, folders, entries, explorers, and `explore()` remain in
`tarav.l1.context`; the current-runtime `context()` helper and Archive-backed
Context storage now live in `tarav.l2.context`. Runtime constructs the storage
service directly, while the same Context Workflow retains its identity in l1.
The focused and full test suites passed, including fresh-import isolation and
retained Context behavior. This placement separates the two uses of Context
without changing its Record labels or stored data.
<!-- tarav.breadcrumb 735d09239790 -->

## Typed read-only context views

The accepted design extends the shared context entry point with explicit
typed selection. `.context()` returns the general view;
`line.context(type=LineScope)` returns a context object specialized for the
Line's interpretive scope. Workflows can define their own context types and
the semantics those views expose without flattening them into one generic
representation.

An unsupported context type fails explicitly rather than silently returning
the general view. Context retrieval is read-only. These are design contracts,
not a claim that the typed selector is already implemented; dispatch and
registration mechanics were not settled in this discussion.

For Lines, the underlying scope identifies what the statement assumes for
its meaning. The typed context view exposes that relationship. The scope
target remains a `TaravEntity`, potentially another Line; the requested
`LineScope` type describes the view rather than the target's class.

Capture evidence pending: current-session discussion
`01a0d86c-9538-7be1-af96-014cd4203d61`, including the user's explicit acceptance
of general/default context, typed selection, unsupported-type failure and
read-only operation. Chatlas refresh was blocked by cache filesystem
permissions on 2026-09-30; exact Turn Breadcrumbs remain to be registered.

## Context queries from an identifier — 2026-10-08

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

The User asked for one general entry point through which an agent that holds an identifier asks Tarav for its context, not a command for POIs only. It is the existing `.context` system reached from the command line: the CLI finds the identity, possibly through search, and lets the agent navigate. A surface that showed the identifier can recommend a qualified context suited to how the agent arrived there.
<!-- tarav.breadcrumb 8082251a4b0a -->

The request is a query object in the manner of Search. By default an identifier is looked up as the identity of something; the query system is typed and can grow. Scripts using `.context` and the CLI are two doors to the same mechanic. The qualifier is a context view type.
<!-- tarav.breadcrumb 2131252c67ed -->
<!-- tarav.breadcrumb 6ec59f222551 -->

Implemented in `tarav-py` commit `4289796`: `tarav.l1.context.query` holds `ContextQuery`, `IdentityContextQuery` and a `ContextQueryService` whose resolvers are Search engines and whose named views are `Context` subclasses; `tarav context --id <identifier> [--view <name>] [--path a/b]` is the adapter. Identifiers resolve for POIs reported by `tarav check --project` and for Tarav Types by name or Ship. Reusing Search for resolution and resolving Types were agent choices. [Impl.Req 876](../../../tarav-py/notes/live/876-context-command-and-reported-poi-impl-req.md) has the detail.
<!-- tarav.breadcrumb 611aae0300ee -->

## The ObjectGroup view — 2026-10-15

The extension's action page showed Workflow trees for three Types it picked
by hand, the action's, the POI's and the check's. The User asked why those
and not the check and other objects, and wanted it formalized: an object
declares the objects related to it, in a context view the extension uses,
with proper names and a model.
<!-- tarav.breadcrumb 48150dee3ba2 -->

No method is added on top of objects: it is a Context workflow, reached as
`obj.context(SomeView)`, still extended through inheritance. The object
returns the whole chain, Situation → Check → POI → Action, peeking at the
other objects as needed. "related" is too broad a word.
<!-- tarav.breadcrumb 48ad4bb0b606 -->

The User accepted the agent's model, in which each workflow contributes
direct links for its own Types and the view follows them until nothing new
appears, with the suites and closing records included and the Project left
out, and named it `ObjectGroup` until a better name comes.
<!-- tarav.breadcrumb 45bdca4b80ea -->

Built as request
[908](../../../tarav-py/notes/live/908-object-group-context-view-impl-req.md):
[`tarav.l1.context.groups`](../../../tarav-py/src/tarav/l1/context/groups.py)
holds `Member`, `Link`, `register_links` and the view; the POI, Checks and
Actions workflows register their links through the runtime, and `tarav
context --id <id> --view object-group` lists the group. A member that is not
a live object is its Type and key, so a group never runs checks. The
extension's Object group section replaces the Workflow trees. Ordering by
link direction, with ties broken by role, Type, id and key, was an agent
choice.
<!-- tarav.breadcrumb 58cbd5cae598 -->

## Callable namespace and partial Type models — 2026-10-15

The User accepted a Context namespace with a named exploration operation and
callable shorthand: `obj.context.explore(type=ObjectGroup)` and
`obj.context(type=ObjectGroup)`. Both use the same `explore()` override.
`SomeType.context.model` organizes the Type model under Context. Callable
namespaces must preserve the earlier namespace decisions: stateless binding,
normal inheritance and `super()`, external namespace classes, and explicit
composition when independent bases contribute to one namespace. Callability
is local to Context; NamespaceBase remains noncallable.
<!-- tarav.context 473c89a0:8cf85c979321cdcf -->
<!-- tarav.context 473c89a0:52d399e8d65f61fc -->

The Type's existing Ship is its model root. Additional Ships are the model
nodes; their current Type-relative paths are labels and lookup information.
Relationships concern these identified subjects. Each node has its own
Context for documentation, external annotations and supporting conversations.
This is a Type model, not an instance model, and a root-only model is valid.
Both the Type's class and outside workflows may contribute nodes without
requiring edits to the class. Checking correspondence to code is useful later;
the model need not enumerate every Python member.
<!-- tarav.context 473c89a0:7ef12f9536d4a790 -->
<!-- tarav.context 473c89a0:3fea6e90a968360c -->
<!-- tarav.context 473c89a0:0dfbeaeb402e0305 -->

[Request 911](../../../tarav-py/notes/live/911-callable-context-namespace-and-type-model-impl-req.md)
implements the namespace on TaravType and introduces
[`TypePath` and `TypeModel`](../../../tarav-py/src/tarav/l1/context/models.py).
Agent implementation choices: an object's `.context.model` opens its Type's
model; class declarations use `Context.model_nodes()`; a runtime-specific
[`ContextService`](../../../tarav-py/src/tarav/l2/context/storage.py) registers
external model providers and offers `put_model_node(Type, node)` for the default
retained location. That writer keeps Archive's existing create-only policy.
The model folder composes all sources with entries keyed by Ship. Matching
declarations deduplicate; conflicting declarations and ambiguous path lookups
are reported. Reads neither mint Ships nor create storage. These mechanics
prepare identified subjects for contextual enrichment; an external-annotation
workflow and code-path correspondence checks are not implemented here.
The behavior is exercised by the
[model tests](../../../tarav-py/tests/kernel/test_type_models.py) and
[namespace tests](../../../tarav-py/tests/kernel/test_context_namespace.py).

## Context as cumulative contextualization — 2026-10-15

The User clarified that Context presents a graph through folder-like key/value
entries. Both entries and values are typed; the Entry Type can communicate the
relationship of a local step. Generic entries and grouping nodes remain valid,
and the same value can be reached by paths expressing different relationships.
A typed workflow-contribution node can explain the provenance of one branch.
<!-- tarav.context 473c89a0:ba32e41d46ab46db -->
<!-- tarav.context 473c89a0:5696389e9d36d4fc -->

A view adds a qualification to the current context. Begin with a subject and
accumulate typed qualifications; the result respects all of them. `.ls()` offers
supported next contextualization steps. Opening an entry returns a further view
or a direct node. Direct view selection and a corresponding entry use the same
operation. Repeated relationships across views are allowed; contextualization
may reveal material or narrow a selection.
<!-- tarav.context 473c89a0:926997d41da95b26 -->
<!-- tarav.context 473c89a0:9b167562b00b0279 -->

The accepted interface is `obj.context(views=(SomeView, Request(...)))`, or
`obj.context.explore(views=(...))`, applying views left to right. The returned
folder base is ContextView; SomeType.Context remains the bound namespace class.
ContextEntry, ContextExplorer, `.ls()` and `.open()` keep their names. The User
delegated implementation choices under autonomous Develop.
<!-- tarav.context 473c89a0:818e903fec5c70c5 -->
<!-- tarav.context 473c89a0:4c4bb8bf8f117d07 -->
<!-- tarav.context 473c89a0:3cae519d8e79ad5b -->

[Request 912](../../../tarav-py/notes/live/912-cumulative-context-views-and-typed-steps-impl-req.md)
implements this in [l1 Context](../../../tarav-py/src/tarav/l1/context/__init__.py).
Implementation choices: ContextScope holds the subject and ordered active
qualifications, exposed as `context_scope` to avoid domain-name collisions.
Static view classes declare `accepts(scope)` and `for_context(current)`;
parameterized ContextViewRequest objects declare `accepts(scope)` and
`apply(current)`. Discovery and dispatch use the same compatibility hook.
Views define supported combinations; unsupported requests fail explicitly.

`ContextBuilder.add_view(name, views=(...))` offers a typed ContextViewEntry.
Availability checks do not run view factories. Registered next-step
contributions follow derived views; generic same-subject grouping folders
inherit scope. Entering another subject starts a fresh scope while the explorer
retains the route. TypeModel's accessor, `model` entry and explicit selection
share its qualification. ObjectGroup and LineScope currently accept only
unqualified inputs. See the
[pipeline tests](../../../tarav-py/tests/kernel/test_context_views.py).

Retained specialized ContextEntry Types and metadata survive write, reload,
listing and explorer binding through ContextService.put_entry/write_entry.
Scope and computed view steps are navigation-local; no persisted request schema
was introduced. Named queries accept ordered view names; repeated CLI `--view`
options use the same pipeline. Listings expose entry Types, and JSON exposes
active qualifications and available next views. Ontology Ships and Record
labels remain stable. The old Python Context view-class name and `type=` selector
were removed. See the
[retained-entry tests](../../../tarav-py/tests/kernel/test_context_entry_storage.py)
and [CLI tests](../../../tarav-py/tests/cli/test_context_views.py).

The User separately clarified that documentation representation was not
designed. Earlier tutorial uses of a `documentation` key and FileReference
were examples from existing mechanics; they establish no schema or standard
key. The external-annotation workflow remains separate design work.
<!-- tarav.context 473c89a0:4cc56a88bd2425f3 -->

