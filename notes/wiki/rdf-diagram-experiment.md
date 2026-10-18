# RDF Diagram experiment

<!-- tarav.sessions
473c89a0 = codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8 @473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f
-->

## Shared graph and executable representations

The User selected RDF as the shared Diagram representation and SPARQL as its
query language. Identifiable elements have TaravObject representations,
including relationship kinds and particular relationship occurrences. Classes
participate through objects representing them. Partial class models ground
selected identified concepts in current code paths; Ships identify concepts
independently of their changing names or implementation forms.
<!-- tarav.breadcrumb 930d31f42db9 -->

Existing JSON Records and Pydantic interfaces stay useful: Record → Object →
RDF is the accepted pipeline. Runtime-only and loaded objects use the same
object-to-RDF contribution mechanism.
<!-- tarav.breadcrumb ef85df09c66c -->

## Progressive Context exploration

The explorer owns a growing RDF graph. Typed views qualify queries over that
graph; loading more context adds triples. The same query can therefore change
its results as exploration progresses. Query composition and graph growth are
separate mechanics. Workflow contributions and discovery still need an
explicit Tarav protocol; RDF supplies their common representation.
<!-- tarav.breadcrumb 1f9a943a22ee -->
<!-- tarav.breadcrumb f0b45cab74d3 -->

## Isolated experiment

The User proposed `_future` modules and object namespaces, experimental Types
owned by `_FutureWorkflow`, and ordinary workflow Record storage for end-to-end
experiments. A visual Diagram explorer accepts a root identifier and exposes
the navigation available to agents. Existing Tarav behavior continues while
the alternative is evaluated.
<!-- tarav.breadcrumb ac8a06300311 -->
<!-- tarav.breadcrumb 952ea1e114bd -->

The User authorized autonomous Develop. [Request 913](../../../tarav-py/notes/live/913-future-rdf-diagram-explorer-impl-req.md)
records the implementation plan, implementation choices, verification and gaps.
The synthetic Conversation/UserTurn/Annotation example is an agent-selected
test family, not a new production Chatlas or annotation contract.
<!-- tarav.breadcrumb 23553a435dc3 -->

## Implemented experiment

The isolated [implementation](../../../tarav-py/src/tarav/l1/_future/README.md)
uses RDFLib's SPARQL engine over a graph owned by the explorer. Objects,
predicates and statement occurrences have code representations. Built-in
navigation and compatible named requests share typed SPARQL refinement;
queries expose their parameter bindings. Explicit loading adds triples, and
merging another exploration preserves Ships while reconciling runtime objects.
These are implementation choices under the authorized experiment.
<!-- tarav.breadcrumb 5ecf2a1f4d66 -->
<!-- tarav.breadcrumb e4f7845c4268 -->

The synthetic demo stores Conversation, UserTurn and Annotation Records through
the normal workflow Registry, then contributes their loaded objects to RDF.
Its explicit runtime expansion changes an unchanged Alice-message selection
from one result to two. The first implementation used a local HTTP/SVG UI;
that placement was corrected below. Python callers use the same
explorer. The maintained test run passed 359 tests, including 23 experimental
tests; the actual HTTP parsing/serialization path and UI JavaScript syntax
were checked. A listening server and browser rendering could not be checked
because the implementation sandbox denies TCP binding and has no browser tool.
See [request 913](../../../tarav-py/notes/live/913-future-rdf-diagram-explorer-impl-req.md)
for commands and measured evidence. Durable Breadcrumb registration is pending
under that sandbox's protected data-depot permissions.
<!-- tarav.breadcrumb 865d198f086f -->
<!-- tarav.breadcrumb e8b9ff79b426 -->

## Visual explorer belongs to Tarav Center

The User challenged the HTTP server and asked why the experiment was not
entirely hosted in the extension. The existing Center.Workflow shell is the
appropriate visual host; the HTTP choice was the agent's unnecessary detour.
<!-- tarav.breadcrumb 4cc7b0012df9 -->

The corrected implementation adds **Diagram explorer (experimental)** to
Tarav Center. Its left tree lists context steps, its center draws the graph
and SPARQL results, and its right panel inspects represented objects. The
extension owns its Python adapter and versioned JSON shapes. One `tarav run`
child retains runtime objects, the growing graph and navigation history,
communicating through stdin/stdout; the webviews use VS Code messages.
The standalone HTTP package is removed from Tarav. These transport/layout
details are agent implementation choices supporting the corrected placement.
<!-- tarav.breadcrumb f7d05cb83141 -->

Measured evidence: 353 maintained core tests pass after removing six HTTP
tests; 12 extension tests pass, including the actual Python subprocess and
renderer path. The unchanged Alice-message query produces one result before
runtime loading and two afterward. Extension 0.1.3 packages successfully.
Visual rendering in a VS Code window remains unverified. See extension
[request 012](../../../vscode-tarav-center/notes/live/012-future-diagram-explorer-impl-req.md)
and its [README](../../../vscode-tarav-center/README.md).

## First principles: code produces the graph

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

Asked for a contrarian review of the experiment, the agent argued that one
RDF store contradicts implementation principles 3 and 5. The User answered
that RDF is only the language the graph is written in: any earlier graph is
expressible as triples, and the graphs themselves keep any structure. What
was normalized is the language, not the graphs.
<!-- tarav.breadcrumb 987bf7bd4311 -->
<!-- tarav.breadcrumb 9d0c67498914 -->

Tarav is not only an ontology: it aims to express both semantics and
operations with precision. Classes and objects model operations; the graph
models relationships between objects. JSON Records are the objects' disk
representation (disk → object), followed by object → RDF graph. The User
wanted these first principles found before scaling the experiment.
<!-- tarav.breadcrumb b434c1df1c92 -->

The User accepted the test that every edge in the graph comes from an
object: a field of some object, or a claim that is itself an object, as an
Annotation is. Then there is one source of truth and one graph. There cannot
be two core graphs; if everything cannot be expressed in the RDF graph, the
approach has failed. The core question is how code relates to the graph,
code being the main interface.
<!-- tarav.breadcrumb 189f3c6b9bec -->
<!-- tarav.breadcrumb 5a5ff0f12341 -->

The principle the User stated: the code is the center, and Tarav code
produces an RDF graph, loading from disk included. Code carries semantics,
mostly of operation; the graph it produces carries more, and graph
technology extracts it. Semantic extraction needs mechanics that already
exist, so Tarav does not build its own graph technology: it defines how code
connects to the Diagram. As before, the Diagram begins with a TaravObject.
<!-- tarav.breadcrumb b7651c9a6193 -->

Code and graph are both tools for expressing semantics, and agents use
either depending on the question. Code provides the graph; where its data
comes from (Records, runtime objects, others) depends on the implementation,
but everything passes through TaravObjects. From there relationships are
discovered with the graph: a complex query asserts relationships that Tarav
code could not state with that convenience. Tarav code implements the
objects' operations and how objects register in the graph; extracting
semantics from the graph is RDF's part.
<!-- tarav.breadcrumb 8cd6d4b6e6ef -->
<!-- tarav.breadcrumb b9beee07fbb1 -->

The graph is not necessarily a static file. For now, one writes into it by
writing and running more code and Records; a static part kept in RDF's own
structures may come later. Code is flexible, data less so: agents use Tarav
to produce more code, which produces more graph, all with clear semantics.
<!-- tarav.breadcrumb a284ee0725f8 -->
<!-- tarav.breadcrumb 17193920bf85 -->

Tarav must let one move back from the graph to code; classes and instances
are coupled to Ships for that. Examples the User gave: given a prompt, an
agent spins the graph for context, finds objects and systems, and learns how
and why to use a given command; given an error, it asks the graph what the
error means in that situation. Tarav documents itself through the Diagram.
<!-- tarav.breadcrumb deb4af7ed7e6 -->

The graph is not mandatory: agents still read codebases and documentation.
It serves when precision and system matter, and for structured search and
discovery, a classic being "what does the system know about this object".
Tarav needs at least one general entry point to the graph; `tarav context`
already is it.
<!-- tarav.breadcrumb abc4c7fa0e8b -->
<!-- tarav.breadcrumb 7dd2e079fbac -->

Costs the User accepted as valid: a query language, RDFLib's speed, and an
extra dependency. Benefits weighed against them: not reinventing a graph; a
knowledge graph suits an open, heterogeneous database; agents already know
SPARQL, which needs less contextualization; accelerators such as caches can
come later. A growing graph's changing results are not fundamental: each
query runs on a scope, stated transparently. The synthetic experiment gives
a feeling for the approach, not proof.
<!-- tarav.breadcrumb 11b501703e67 -->

Agent proposals raised in the discussion, not decided: one named graph per
workflow, so crossing between graphs stays explicit; default triples derived
from object fields, with hand-written provider edges as the marked
exception; a projection that is a pure function of the objects present; a
static RDF document entering as an object; small resolvers from text,
errors, paths and commands into objects; a built-in "what is known about
this object" view; and a falsifiable test comparing the graph's context for
a real error with grep, `--help` and the Wiki.
<!-- tarav.breadcrumb 83d1c8a4b99d -->
<!-- tarav.breadcrumb 066b6a5d0bfc -->

## The projection contract

The User placed the contract in the `.context` namespace: it returns
something that holds a graph, over which one summarizes and runs queries.
The engine enlarges the graph as objects are opened, collecting more and
more triples from the objects visited. Each object holds how to generate its
context triples; the context engine filters, selects and keeps any cursor.
<!-- tarav.breadcrumb b4bacfac3a50 -->

Tarav code therefore splits into normal objects and their operations
(Assertions, scoring, POIs, and so on) and the context system: the
primitives and engine for the Diagram, how objects hook into it, and how
the graph is manipulated.
<!-- tarav.breadcrumb e14c177263c8 -->

The hook is one method, `obj.context.triplets()`, the standard hook into the
graph for all objects; the engine demands nothing more for now. Its meaning
is what the object contributes about itself to the graph, not how it feeds
other objects in. An object has no complex mechanism for understanding
context: asked for its context, whatever it returns is its contribution,
with any processing it likes, such as loading everything in a folder. The
result need not be the same triples every time. All triples come from some
object.
<!-- tarav.breadcrumb 946351fbd140 -->
<!-- tarav.breadcrumb 3fde3fc6a280 -->

Everything else is ordinary code: how the context engine manipulates the
graph and provides navigation, and the environment Tarav must provide to
find and open an object from its ID. Tarav still needs a basic search system
outside the graph. Workflows can go around checking all objects, so incoming
edges do not require opening every pointing object; a RecordRegistry object
can represent all recorded objects and know how to iterate them, but that is
specialized functionality, not what its own `triplets()` returns.
<!-- tarav.breadcrumb 34b7cdff7fde -->
<!-- tarav.breadcrumb 093761b8d8d8 -->

The User set implementation aside until the design principles are aligned.
The agent noted that the engine can record which object contributed each
triple, as an implementation detail of that ordinary code.
<!-- tarav.breadcrumb c8e1afb2af21 -->

## The context engine, and all of Tarav migrated

All code for the code → graph step belongs to the Context workflow; all that
it requires objects to implement goes in the `.context` namespace. The
usage case the User set first: an object's context returns a navigable
object holding the opened graph, which can be expanded and queried and
grows by asking each visited object for its triplets.
<!-- tarav.breadcrumb 434e6d62008e -->

The User kept the default VERY basic: an object that does not override
`triplets()` returns one triple saying it is of its type. The Explorer is a
TaravObject, which only means it has something to say when asked for its
context; being in the Diagram is not what an object does in general.
History (back and forward) is in, simple and basic; it moves the cursor,
and the graph only grows.
<!-- tarav.breadcrumb fb5d03c5ea12 -->
<!-- tarav.breadcrumb ef54cc037661 -->

Rather than placing the engine beside the old Context, the User chose to
migrate all of Tarav to it: every Type resets to the default triple, and
each one's context is rebuilt later, as it is used. Nothing is reimplemented
now; what is not implemented errors, which shows where to reimplement. The
ObjectGroup is just a query now; `tarav context --id` finds the object and
returns `.context()`; Context code in Actions and elsewhere is cut, kept in
Git history.
<!-- tarav.breadcrumb 2b9541f49348 -->
<!-- tarav.breadcrumb e72e6fe79196 -->

Built as tarav-py [request 914](../../../tarav-py/notes/live/914-graph-context-model-impl-req.md)
(commits `dd3bc9d`, `0ecb616`, `6fcce90`, `85818d7`): Kernel
`TaravType.Context` is `triplets()` plus `__call__()`; `tarav.l1.context`
holds `ContextExplorer` (`open`, `ls`, `follow`, `back`, `forward`, `query`
over an RDFLib graph) and the identifier resolvers; the old views, models,
ObjectGroup, retained storage, every Type's contribution and the `_future`
experiment are deleted; `tarav context --view` fails explicitly; RDFLib is a
core dependency. Measured: 291 tests pass, `tarav context --id Tarav.POI`
prints its type edge to `Tarav.Class`. Left outside: the extension's Diagram
explorer and object group now fail, and agents files embedding the old
System Prompt report it stale.
<!-- tarav.breadcrumb 52dafa7ca630 -->

## ObjectContext construction through ordered hooks

The next discussion replaced the single `triplets()` hook with explicit
construction: `cxt = obj.context.build()`, followed by `cxt.triplets`.
The User wanted the complete ObjectContext returned so it can retain other
data useful for debugging. There is no `.context.triplets()` convenience
path. An object's contribution is assembled through class, instance, then
external hooks; all receive and may mutate the same context, including its
triples and construction options. External workflows can therefore enrich
an object's context without changing its class.

Class access stays uniform: `Document.context.build()` delegates to the
context of `entity(Document)` (called `identity(Document)` in discussion).
The User clarified that this runs TaravClass's class hooks, the particular
class identity's instance hooks, then external hooks. It does not run the
hooks intended for Document instances. The two contribution entry points
are `_class_context_hook(cxt)` and `_obj_context_hook(cxt)`; inherited hooks
compose with ordinary `super()` and the established explicit namespace
composition for multiple inheritance. The builder calls each stage once.

The User's ordering correction was: “class -> instance -> external”. The
last clarification was: “the all hooks just recieve the same context
object”. Source: current codex session
`01a1176b-f14c-7fd0-a97c-b22279c3f8c8`, neutral identity
`473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f`.
Exact Turn grounding is pending: the sandbox blocked Chatlas refresh and
the retained Normal Model ends before this discussion. These quotations
are from the current conversation; no older Turn was substituted as support.

Implemented in [request 916](../../../tarav-py/notes/live/916-object-context-builder-and-hooks-impl-req.md).
Inspected implementation: ObjectContext holds subject, triplets, options,
opaque hints and stage-run diagnostics; each runtime owns an ordered
ContextBuilder registry. Hook failures retain a partial result in
ContextBuildError. The Explorer retains completed contexts and validates
their triples before extending its growing graph. Removing a triple during
construction changes that contribution, without retracting facts already
collected. The [developer guide](../../../tarav-py/src/tarav/l1/context/README.md)
and [runnable example](../../../tarav-py/examples/object_context.py) show the
public surface. Measured: 313 core tests and 13 real-process extension tests
passed. This section supersedes the earlier direct `triplets()` API, while
retaining that discussion as its design history.

## External hooks as configured instances

The User next requested an external ContextHook base class, so a contributor
can bundle the dependencies and configuration needed to contribute. The
discussion settled on explicitly constructing and registering an instance;
the builder calls `hook.run(cxt)` on that same instance across builds.

Target-class registration was considered and then withdrawn. The User's
decision was: “the hook itself can do the checking and ignore what it wants
to ignore”. Every registered hook therefore receives the shared context in
registration order, and each implementation decides whether to return
unchanged or contribute. Applicability can depend on type, identity,
options, or workflow-owned state. The registry does not route by class.

Implemented by [request 917](../../../tarav-py/notes/live/917-context-hook-instances-impl-req.md):
the public `ContextHook` is an abstract Python interface with `run(cxt)`;
registration requires a concrete instance. Free functions, classes and duck
typed substitutes are rejected. The existing class/instance namespace hooks,
registration snapshots, shared mutation and diagnostics remain intact.
The guide and runnable example now use a configured hook instance. Measured:
68 Context/CLI/architecture tests pass, including dependency/state and
self-filtering cases; the installed-tool example retains its expected graph
and SPARQL result.

Conversational grounding is pending for codex session
`01a1176b-f14c-7fd0-a97c-b22279c3f8c8`, neutral identity
`473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f`.
The exact-session Chatlas refresh cannot write its protected cache. The
quotation is preserved from the current discussion; no older Turn was used
as a substitute and no new Breadcrumb was fabricated.

## Discovering Tarav through its graph

<!-- tarav.sessions
70c6a1bb = codex:01a14701-3013-7260-87b8-01ee30e64454 @70c6a1bb0295ba16d25b874e624decc291c1aa70c23ee355038c2a0cb72e953c
-->

The User clarified that an incomplete connection to Tarav.Archive is not the
main question at this stage. Current references concentrate on Chatlas
transcripts. Any Tarav subsystem, including an Archive workflow, can be
represented by Tarav objects and classes; their Context namespace lets their
own hooks or external contributors supply triples. This couples Python's
expressivity with a graph through which an agent can discover both the harness
and the world it describes.
<!-- tarav.breadcrumb 976f2fd9935e -->

The graph can describe Tarav code itself, in the same way it can describe an
external document. When an agent encounters an unfamiliar path or object, it
can ask what the system knows about it, follow typed relationships, and then
open the relevant source code or documentation. A known operation, such as
getting and displaying an object's documentation, can also have a direct
Python path. There is no exclusive assignment of a relationship to code or
graph: code supplies operations and graph contributions, while the graph
communicates semantics and lets agents find relationships they did not know
to ask for directly. Exploration must lead back from graph objects to their
code and resources.
<!-- tarav.breadcrumb a3bc51cd1387 -->
<!-- tarav.breadcrumb 18036892fa9f -->

A documentation relationship illustrates the distinction. The graph can
identify the relationship's predicate and expose what that predicate means.
An edge can lead to a documentation object that points to a resource; the
graph need not contain the document text. An object's Type may itself supply
the documentation relation. A documentation workflow could offer an entry
point to such resources for any object, while code provides the operation
that opens or renders one. The exact documentation workflow and representation
remain to be designed.
<!-- tarav.breadcrumb f7b2fd004761 -->
<!-- tarav.breadcrumb 0e217f92e2b9 -->

The User proposed another usage case: a script or operation involving several
Types and objects could be recorded or annotated with relationships to them.
An agent searching for a usage example could query those relationships, open
the example, discover further objects, and repeat this research cycle. A
future recorder or contextualizer might derive some contributions from code
or records and expose them through Context hooks. This is a proposed workflow,
not a claim that automatic extraction or global example search exists now.
<!-- tarav.breadcrumb 44aa792a6f30 -->

The User then withdrew the initial framing of a rule for deciding which part
of Tarav should implement each thing. Write useful code as code; use the graph
as an available semantic and discovery capability, including for descriptions
of that code. The code and graph can be traversed repeatedly in either
direction as agents investigate the system.
<!-- tarav.breadcrumb 6681c1e6a09c -->
<!-- tarav.breadcrumb 4d0d1ae6fb00 -->
