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
