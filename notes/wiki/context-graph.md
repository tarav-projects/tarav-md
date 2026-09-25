# Context Graph

<!-- tarav.sessions
1f561f5d = codex:01a0b984-4664-7871-934a-89cf92595b64 @1f561f5d8db849a3a445b83a91a5e94acbb80927f9c332d45322ac70f8705a74
-->

## Progressive discovery

Tarav should provide a general progressive-discovery workflow for its typed
objects. Type dispatch already gives every Record a dependable route to its
registered Python class. Static `help()` remains the small Type-level entry
point and advertises `context()` as the expandable route to further material.
<!-- tarav.breadcrumb 44e28180e63da4bf162bdf94cd5c966ef53317e94a377b87d43b390ede405c2b -->
<!-- tarav.breadcrumb ab1c76383e0c5aff548a322ca6b7d497309793b978b8e26d4a415368c7af7461 -->

Both classes and identified objects expose context through the same mechanism.
`Class.context()` concerns the Type itself; `object.context()` concerns that
particular object and may include its Type context. Context is reactive:
systems may contribute material to a class or object, and the owning class may
discover further context from its current state and typed relationships.
<!-- tarav.breadcrumb 516a49ca2f6716bab43cee1cb6c9fe794a8fa859e15bff6281b1b816e01f147f -->

## Virtual directory over a graph

The candidate `Context.Graph.Workflow` presents context as a virtual directory
rooted at its subject. It may contain named entries, nested directories, full
Records, references, text, collections, and computed projections. The backing
data need not be a filesystem directory. Agents progressively navigate with
filesystem-like operations such as listing, bounded head or tail reads, and
full reads.
<!-- tarav.breadcrumb 312c500173ae6b5678e2bf7931ddf35d9628871fab107138721d7a75bdca49a2 -->
<!-- tarav.breadcrumb a4f60eab4c66a1b02add6ae258c4882cc5e342151c5ecb046f85d1f9b3f20e0b -->

The directory is a navigation projection over a graph rather than the object's
identity or physical storage. The same node may be reachable through several
paths, references may cross between subtrees, and traversal must tolerate
cycles. Context can be owned by the subject, contributed by registered
systems, or discovered from current graph state.
<!-- tarav.breadcrumb 444689fa8d74fdc979f66df2793514be4ed04fd7788f870ad30ec4fd1388b6b0 -->
<!-- tarav.breadcrumb 8e63a1cec571fc8519b432ea72b1fab40692cbb184537d296b80fb38a18d8127 -->

## Durable context roots

Class context has a durable attachment root in the class's `TypeShip`.
Object-level durable context requires an addressed entity, motivating
`TaravEntity(TaravObject)` with a non-rebindable `id: Ship`. Plain
`TaravObject`s may still provide computed or session-local context, but
external systems cannot durably attach context to them without stable
identity.
<!-- tarav.breadcrumb 2987564fe199c20651db9ab877248206b3b549d26d37caefd07aaa692ae6db4a -->
<!-- tarav.breadcrumb 853f360bd3762dc4c7515757ffd971df7deab7eef61a4b22f83d894711e10017 -->

Ships are semantic identity opportunities, not a mandatory bundle of
mechanics. A Ship may support specialized behavior or remain only an invariant
that agents and systems can search for. The non-rebinding rule lets context,
observations, references, and editions accumulate around one semantic point
without changing what its UUID denotes.
<!-- tarav.breadcrumb 913654b4a1a8cd0b5d28baf93f9a9f8f993db3c729c5fea57d9887c6f06f5bbc -->

Entity identity remains independent of storage shape. The same entity may be
a file-backed or directory-backed Record. Its retained JSON stores the UUID as
a string, while its `RecordInterface` exposes `id` as a `Ship` through an exact
Pydantic round trip.
<!-- tarav.breadcrumb 3220134b43795b2c7742526c8dad0513219e1f295e1fc50afe5f2295c49949ae -->
<!-- tarav.breadcrumb 77ceef64c159b08f2cb9c6c97ed0205fea09dbd8c99ca07bc2e6f5773159d967 -->
<!-- tarav.breadcrumb b9d2cc0f78e13ea01d916be4847b75dcfde7ef059c55fe0e2a10c5643afcbc15 -->

## Context as one graph-building workflow - v001

The broader Tarav graph is not formed by an Entity subsystem or Context alone.
It emerges from the typed relationships contributed by multiple independent
Workflows. The kernel supplies identity, Record, Reference, registration, and
navigation mechanics without owning the vocabulary of those relationships.
<!-- tarav.breadcrumb d07452c4d6a0313d8d76e04352b0866530e49776817051f21e5007cac34683b5 -->

Context is one built-in Workflow within that ecology. It supplies a
filesystem-shaped organization around a Record or Entity: literal Records can
live in the context, References can point elsewhere, and Entity links can lead
to other stable subjects. Agents choose which paths and links to follow, while
the contributing Workflows retain ownership of the attached Records' meaning.
<!-- tarav.breadcrumb e4795a494347a082c53afbd8d4d63803a6a7f77d56630fe56f07968ed4687f77 -->

In the minimal `tarav-py` architecture, Context therefore belongs with the
named Workflows. Generic Record, Workflow, registry, identity, Reference, and
space-navigation mechanics belong in the kernel. This preserves Context as a
central reusable workflow without turning it into Tarav's central semantic
authority.
<!-- tarav.breadcrumb c624689f980ba649054c8fb051e44207444b951f7aa30a92d09bd1d8b8d12ba2 -->

## Context as core Diagram navigation - v002

This supersedes the v001 placement of Context as an optional built-in
Workflow. Tarav needs a small explicit bootstrap layer so agents can discover
the available Types and Workflows without an infinite dependency on another
discovery Workflow. Context is therefore a core Diagram operation: it opens a
subject as a progressively navigable view, comparable to opening a filesystem
node as a directory.
<!-- tarav.breadcrumb 7f73ad586de01f9b100638a90c49ea6bd9993e3fa7c7edd9f9a45cb79954d0af -->

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
<!-- tarav.breadcrumb afc71d04e03205c96294c164ed33ab5ca37e9c58130075331a45c8331fbfcd1e -->
<!-- tarav.breadcrumb b32246240652261c11140471d7d81f5846241de6c371939571d1621875f8c5bd -->

`context(subject)` returns a lazy `Context` navigation view with operations
such as `ls()` and `open()`. A `Context` instance is not currently a
`TaravObject` or a Diagram subject; it is a view over the Diagram. Its
`Context` class still extends `TaravType`, so the class is reified by
`TaravClass` and agents can navigate documentation and usage context for it.
This cleanly separates class participation from instance participation.
<!-- tarav.breadcrumb f55534adb58fd0fa1c0e8803fde89232c1e669517ace6f9a24574502068c1568 -->
<!-- tarav.breadcrumb 141c2d19566a72b3b98f62059773152e024d626bd42b15874d19c049e7803138 -->
<!-- tarav.breadcrumb 1141cd37c63f3ed885a1d5bada7f4020354b85b3f0883de01e8eac4c5ecf2f2a -->

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
<!-- tarav.breadcrumb 171ca91cb68de6aded76171f8a989d2eb08703ea8f60c0f4a14a349aea3764ae -->
<!-- tarav.breadcrumb 2e6ccd42a166422051c545cddad7e69c99c1a901297292746e9bf7eb4511bcf2 -->
<!-- tarav.breadcrumb 50998722e225353821252152255f06e8ce6cb62eb0ff2df4306d73dd86c9f994 -->

## Context directory and cursor - v003

This advances v002's runtime-only navigation view with durable context
attached to Entities. The proposed retained namespace is
`~/Documents/tarav/contexts/`, with one root directory per Entity identity.
Workflows can contribute Records there. Nested folders are represented by
`DirectoryRecord`s; each level keeps a cheap registry of its immediate entries
so `ls()` does not load the child objects or their full Records. Opening a
retained Record uses trusted Type dispatch.
<!-- tarav.breadcrumb db2a880936c9a7027161034fe77d5653370dbd7fbdf86b57b3f8d5eaeb513d28 -->
<!-- tarav.breadcrumb c97f8df49550ff0285b93a4101a436664826780d764f8c241af2b373473f6d21 -->

`Context` is read-only with respect to the tree but stateful as a navigation
cursor. `cd()` changes the current directory within the subject's context;
`ls()` reads only cheap directory information. Runtime contributions and
retained entries share the same virtual namespace and navigation operations,
without a separate runtime-versus-disk branch in the public view.
<!-- tarav.breadcrumb 52dcf7c6538dfe2f081d4d9938d51b5b3347662b3b3c94863fd83589416049be -->
<!-- tarav.breadcrumb 1d7b6c4151a550b23c96ee1cba74e3a267e368ea18931c09aa2e81302e97a2a2 -->

The directory-like contract is `Context: name -> TaravObject | Context`.
`open(name)` returns either an object or a nested Context; `cd(name)` enters a
nested Context. The name is held by the containing Context, so an object can
appear in a context without knowing its placement. A retained entry resolves
through the Record registry; a runtime entry is supplied by its context
provider. This replaces v002's tentative `open()` return union with the
agreed object-or-context form.
<!-- tarav.breadcrumb 7beba2e1ed513d768c14d5fcb35c94a1bcf5530f7d7d426b98f9300a1ae788b2 -->
<!-- tarav.breadcrumb b3f501443dcc3b046345c2b2c8adb5cde07d6caf14722d9d4ac813dd804799f3 -->
<!-- tarav.breadcrumb 4268e797c21f5ea9efeca69fce7eb5237622ea744cc997bd66154fb3f8d48e4e -->

## Archive-backed context organization - v004

This advances v003's retained-directory proposal: the Context workflow uses
Record Archive for durable placement instead of maintaining a separate Context
store and entry index. An identified subject's Ship addresses its logical
context root in the Context workflow's Archive partition. The root's physical
Archive location can remain opaque. Classes use their `TaravClass` Ships;
Entities use their own Ships. Unidentified objects can still contribute
runtime context without a durable root.
<!-- tarav.breadcrumb 38a58bcfe8d426f3bcb33f757cca68c4d5224315bc55e4a4f768e7760a5567ea -->

The Context root is a read-only navigation view that composes runtime hooks
with retained Archive entries. Archive owns storage, placement, and Git
behavior; Context owns the subject-relative view and opening behavior. A
subject-specific typed Archive can retain the subject Ship in its Record so
opening by identity verifies the binding independently of the Archive's own
identity. The existing `ContextDirectoryRecord` and `ContextPlacement` index
would no longer be needed as a parallel storage format.
<!-- tarav.breadcrumb 4b694a679ccf66a85c31b3f67fbdec1324ab083a3a30b99e2166baeea122b5ed -->

`ContextEntry` is the lazy wrapper around one placement. It can wrap an
`ArchiveEntry` for retained material or an opener for a runtime contribution;
opening yields a `TaravObject` or a nested Context. The target object need not
know its context placement. Dictionary and Vector Context types present named
and positional navigation over the corresponding Archive structures. The root
for `context(obj)` is a dictionary so runtime and retained names can share one
namespace; nested dictionaries and vectors let contributors organize context
as needed.
<!-- tarav.breadcrumb 76b9d3e934c9261424ca7a05c615b9df396ae0ad7912051f3176c199759a8d04 -->

A Vector Context position is a mutable placement, not a subject identity.
Insertion may shift positions; Ships and References remain the stable way to
address subjects. Listing should read placement metadata without loading
contained objects, while `open()` resolves only the selected target.
<!-- tarav.breadcrumb 2adbc657ea53c39f5c33f9cea220a00f58ab8ff0f6c11758bee7111ffc32dac7 -->

## Context entries and exploration - v005

This revises v004's tentative treatment of `ContextEntry` as a wrapper around
`ArchiveEntry`. The two are independent wrappers. Where context is retained in
an Archive, its `ArchiveEntry` contains a `ContextEntry` Record as cargo; the
`ContextEntry` in turn contains another typed Record as its cargo. Archive
owns storage and placement, while Context owns the meaning of the context
entry. A direct Record and a Reference Record are both possible cargo types.
`ContextEntry.open()` returns the cargo object; if it is a Reference, a caller
may separately call `entry.open().resolve()`.
<!-- tarav.breadcrumb 343f6bd4a7b5a243bdf605941ff08b5554679bde817895da73b6ae94d99f6a25 -->
<!-- tarav.breadcrumb d8d776cda81ffbc50598738b8dd41226d05484ed2270f563f489d8f806cca294 -->

The runtime `ContextEntry` exposes its name or vector position even when that
placement comes from its containing `ArchiveEntry` and is not duplicated in
the retained Context Record. Context need not subtype Archive: runtime-only
entries have no Archive backing. An Archive-backed entry can expose its
`ArchiveEntry` for Archive operations, while its ordinary Context interface
works for either source. The writer explicitly chooses the cargo Record and
lets Context wrap it before Archive stores the Context entry.
<!-- tarav.breadcrumb 321e4c2856ea38bfa8be7cbb1864dc8e424eb22f3925efb5326a74baf31d7333 -->
<!-- tarav.breadcrumb a690be883fbe55f3e50f640024f34f26dea345e6c9586e3f657a18e9383fd823 -->

Each Entity's context is a separate navigable graph. Opening another Entity
through an entry and calling `context()` on it can cross from one graph to
another; their Records need not share an Archive root. `ContextExplorer` is
the stateful navigation object for moving within a context and remembering
the route across such jumps. Runtime entries encountered through an explorer
carry their placement and navigation origin so backward navigation can return
to the occurrence from which the jump was made.
<!-- tarav.breadcrumb 9ce43b45f8e22096a86e2613d9a7f7ad0f3165c95f88ca3109cfa7e6eff72006 -->
<!-- tarav.breadcrumb 1be53811fcb77b3c84c4116f1d1b295e22771cb1ed0d31cdfec7d78a654cd5f9 -->

Calling `context(entry)` follows that entry's cargo context in the *same*
explorer, retaining its route for backward navigation. Calling
`context(entity)` directly starts a new, independent explorer because the
Entity carries no navigation history. Explorer bindings belong to runtime
entry handles, so separate explorers can visit the same retained placement
independently. The exact navigation method names remain open to implementation.
<!-- tarav.breadcrumb ea2147a4b4e1348f4af7b2a94b67d56fbbbf3565f8205056ca3ba65ec8a88a25 -->
