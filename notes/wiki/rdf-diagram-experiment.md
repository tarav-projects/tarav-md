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
<!-- tarav.breadcrumb 930d31f42db9d2e94ec15c6a803e694ce47bdca305f79eb90c29af1ac2cfdb16 -->

Existing JSON Records and Pydantic interfaces stay useful: Record → Object →
RDF is the accepted pipeline. Runtime-only and loaded objects use the same
object-to-RDF contribution mechanism.
<!-- tarav.breadcrumb ef85df09c66cae5a764924c9b94448a65121a9a067e82af64c40c88aa76b64ec -->

## Progressive Context exploration

The explorer owns a growing RDF graph. Typed views qualify queries over that
graph; loading more context adds triples. The same query can therefore change
its results as exploration progresses. Query composition and graph growth are
separate mechanics. Workflow contributions and discovery still need an
explicit Tarav protocol; RDF supplies their common representation.
<!-- tarav.breadcrumb 1f9a943a22ee3caa4bdcb1cf87b8fbbdb39e65905a5197ab68199b4cf96ac7bb -->
<!-- tarav.breadcrumb f0b45cab74d3809bcc2de8988225bbc36d1c6ad9df8c6faa9cb895ac8d3236da -->

## Isolated experiment

The User proposed `_future` modules and object namespaces, experimental Types
owned by `_FutureWorkflow`, and ordinary workflow Record storage for end-to-end
experiments. A visual Diagram explorer accepts a root identifier and exposes
the navigation available to agents. Existing Tarav behavior continues while
the alternative is evaluated.
<!-- tarav.breadcrumb ac8a063003115685df09a79b1cbf22148e98027bf2b2834c7a63b81d826bbdc2 -->
<!-- tarav.breadcrumb 952ea1e114bdbf1f14030b28d5ff37c6e01e341fd1039eb4bca5916b9693bedc -->

The User authorized autonomous Develop. [Request 913](../../../tarav-py/notes/live/913-future-rdf-diagram-explorer-impl-req.md)
records the implementation plan, implementation choices, verification and gaps.
The synthetic Conversation/UserTurn/Annotation example is an agent-selected
test family, not a new production Chatlas or annotation contract.
<!-- tarav.breadcrumb 23553a435dc3d1fa77eeed5f6d6df07862490084db43ff58360be4f80ccd451b -->

## Implemented experiment

The isolated [implementation](../../../tarav-py/src/tarav/l1/_future/README.md)
uses RDFLib's SPARQL engine over a graph owned by the explorer. Objects,
predicates and statement occurrences have code representations. Built-in
navigation and compatible named requests share typed SPARQL refinement;
queries expose their parameter bindings. Explicit loading adds triples, and
merging another exploration preserves Ships while reconciling runtime objects.
These are implementation choices under the authorized experiment.
<!-- tarav.breadcrumb 5ecf2a1f4d66914a3c324a530f638c1ba7bb1f884974e08f090376e9f343430b -->
<!-- tarav.breadcrumb e4f7845c426807ba197c389ca3aa6f56d1bdf22f0a50f09164e662da5302790d -->

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
<!-- tarav.breadcrumb 865d198f086fca594da1cd0a93293ab695f48fb52bb13ad958092d39bd569262 -->
<!-- tarav.breadcrumb e8b9ff79b426fa48dee32ff47e6ecc07f056c20aa83564fd6deacb61cdafd677 -->

## Visual explorer belongs to Tarav Center

The User challenged the HTTP server and asked why the experiment was not
entirely hosted in the extension. The existing Center.Workflow shell is the
appropriate visual host; the HTTP choice was the agent's unnecessary detour.
<!-- tarav.breadcrumb 4cc7b0012df9de4dbf3239ee6561e55738d62638d6d121a7f8f2fb36b84b8a02 -->

The corrected implementation adds **Diagram explorer (experimental)** to
Tarav Center. Its left tree lists context steps, its center draws the graph
and SPARQL results, and its right panel inspects represented objects. The
extension owns its Python adapter and versioned JSON shapes. One `tarav run`
child retains runtime objects, the growing graph and navigation history,
communicating through stdin/stdout; the webviews use VS Code messages.
The standalone HTTP package is removed from Tarav. These transport/layout
details are agent implementation choices supporting the corrected placement.
<!-- tarav.breadcrumb f7d05cb8314144e1ea95f028c4683320bc5833fdf0b3c876bc5931073b418474 -->

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
<!-- tarav.breadcrumb 987bf7bd431165712b432fb1693fdb3fa5e8d86c9b22d24c4454bd68ae3482a0 -->
<!-- tarav.breadcrumb 9d0c674989149359b4300658e4927dc6441534ee6c27af8e8dc351ef70c73d59 -->

Tarav is not only an ontology: it aims to express both semantics and
operations with precision. Classes and objects model operations; the graph
models relationships between objects. JSON Records are the objects' disk
representation (disk → object), followed by object → RDF graph. The User
wanted these first principles found before scaling the experiment.
<!-- tarav.breadcrumb b434c1df1c92a7c03a150824ffef2bc8e5be19e8392c09acd5bda8e5839eea82 -->

The User accepted the test that every edge in the graph comes from an
object: a field of some object, or a claim that is itself an object, as an
Annotation is. Then there is one source of truth and one graph. There cannot
be two core graphs; if everything cannot be expressed in the RDF graph, the
approach has failed. The core question is how code relates to the graph,
code being the main interface.
<!-- tarav.breadcrumb 189f3c6b9becd9ed3d42107c19f7755337b15adf17af734dc04a2a1058500c7b -->
<!-- tarav.breadcrumb 5a5ff0f12341c13cda5f992f8450c9e5db9ca7d79f593cb08e80f2a011614f51 -->

The principle the User stated: the code is the center, and Tarav code
produces an RDF graph, loading from disk included. Code carries semantics,
mostly of operation; the graph it produces carries more, and graph
technology extracts it. Semantic extraction needs mechanics that already
exist, so Tarav does not build its own graph technology: it defines how code
connects to the Diagram. As before, the Diagram begins with a TaravObject.
<!-- tarav.breadcrumb b7651c9a61931dbde0a2849b381dc53f1f36722747ab91a5c6e3709ef1750a46 -->

Code and graph are both tools for expressing semantics, and agents use
either depending on the question. Code provides the graph; where its data
comes from (Records, runtime objects, others) depends on the implementation,
but everything passes through TaravObjects. From there relationships are
discovered with the graph: a complex query asserts relationships that Tarav
code could not state with that convenience. Tarav code implements the
objects' operations and how objects register in the graph; extracting
semantics from the graph is RDF's part.
<!-- tarav.breadcrumb 8cd6d4b6e6ef96341bc5b33e5dabf955019f08a72dbd3eff48db84dc7042b3ba -->
<!-- tarav.breadcrumb b9beee07fbb17250be26684b0f759da3bfcb43970a112a4174e2c536487959de -->

The graph is not necessarily a static file. For now, one writes into it by
writing and running more code and Records; a static part kept in RDF's own
structures may come later. Code is flexible, data less so: agents use Tarav
to produce more code, which produces more graph, all with clear semantics.
<!-- tarav.breadcrumb a284ee0725f881162b2ecfcc7a6570b03e1d61f404ab053b716fbb71ff4aec1a -->
<!-- tarav.breadcrumb 17193920bf853fc7d293168f694873ef39e3d4612b4e1d1a42541397d2d92ecc -->

Tarav must let one move back from the graph to code; classes and instances
are coupled to Ships for that. Examples the User gave: given a prompt, an
agent spins the graph for context, finds objects and systems, and learns how
and why to use a given command; given an error, it asks the graph what the
error means in that situation. Tarav documents itself through the Diagram.
<!-- tarav.breadcrumb deb4af7ed7e60a3c02053290d1c719a560c6cbb41985ec7a2bd1bfe0b68020b6 -->

The graph is not mandatory: agents still read codebases and documentation.
It serves when precision and system matter, and for structured search and
discovery, a classic being "what does the system know about this object".
Tarav needs at least one general entry point to the graph; `tarav context`
already is it.
<!-- tarav.breadcrumb abc4c7fa0e8bcc4ef016e6d48808599174d3db5342aa23e3f2eb853d13948582 -->
<!-- tarav.breadcrumb 7dd2e079fbac1f26c64d7d036175a5f1463dc180b5c426a801098e82f75fe6b9 -->

Costs the User accepted as valid: a query language, RDFLib's speed, and an
extra dependency. Benefits weighed against them: not reinventing a graph; a
knowledge graph suits an open, heterogeneous database; agents already know
SPARQL, which needs less contextualization; accelerators such as caches can
come later. A growing graph's changing results are not fundamental: each
query runs on a scope, stated transparently. The synthetic experiment gives
a feeling for the approach, not proof.
<!-- tarav.breadcrumb 11b501703e67a89140802fe015d60bb77930786ba526666b2d8fa02a7aaa4894 -->

Agent proposals raised in the discussion, not decided: one named graph per
workflow, so crossing between graphs stays explicit; default triples derived
from object fields, with hand-written provider edges as the marked
exception; a projection that is a pure function of the objects present; a
static RDF document entering as an object; small resolvers from text,
errors, paths and commands into objects; a built-in "what is known about
this object" view; and a falsifiable test comparing the graph's context for
a real error with grep, `--help` and the Wiki.
<!-- tarav.breadcrumb 83d1c8a4b99db5d91772af1409ee3ba22b2db3326eef775e1f6c6c42764a1717 -->
<!-- tarav.breadcrumb 066b6a5d0bfc91d08596bae502edf2936431d6da324d49e44193fa7c2dd38c43 -->
