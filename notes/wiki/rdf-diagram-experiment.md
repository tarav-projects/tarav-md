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
<!-- tarav.context 473c89a0:a25dc4a4402725c7 -->

Existing JSON Records and Pydantic interfaces stay useful: Record → Object →
RDF is the accepted pipeline. Runtime-only and loaded objects use the same
object-to-RDF contribution mechanism.
<!-- tarav.context 473c89a0:26ed8f97ba0dba97 -->

## Progressive Context exploration

The explorer owns a growing RDF graph. Typed views qualify queries over that
graph; loading more context adds triples. The same query can therefore change
its results as exploration progresses. Query composition and graph growth are
separate mechanics. Workflow contributions and discovery still need an
explicit Tarav protocol; RDF supplies their common representation.
<!-- tarav.context 473c89a0:2231281cb94571ae -->
<!-- tarav.context 473c89a0:2a9c92e92b99b1e7 -->

## Isolated experiment

The User proposed `_future` modules and object namespaces, experimental Types
owned by `_FutureWorkflow`, and ordinary workflow Record storage for end-to-end
experiments. A visual Diagram explorer accepts a root identifier and exposes
the navigation available to agents. Existing Tarav behavior continues while
the alternative is evaluated.
<!-- tarav.context 473c89a0:b4ad4b3730008174 -->
<!-- tarav.context 473c89a0:8944495a171e5499 -->

The User authorized autonomous Develop. [Request 913](../../../tarav-py/notes/live/913-future-rdf-diagram-explorer-impl-req.md)
records the implementation plan, implementation choices, verification and gaps.
The synthetic Conversation/UserTurn/Annotation example is an agent-selected
test family, not a new production Chatlas or annotation contract.
<!-- tarav.context 473c89a0:c4ecebaa9007be2e -->

## Implemented experiment

The isolated [implementation](../../../tarav-py/src/tarav/l1/_future/README.md)
uses RDFLib's SPARQL engine over a graph owned by the explorer. Objects,
predicates and statement occurrences have code representations. Built-in
navigation and compatible named requests share typed SPARQL refinement;
queries expose their parameter bindings. Explicit loading adds triples, and
merging another exploration preserves Ships while reconciling runtime objects.
These are implementation choices under the authorized experiment.
<!-- tarav.context 473c89a0:2231281cb94571ae -->
<!-- tarav.context 473c89a0:c4ecebaa9007be2e -->

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
<!-- tarav.context 473c89a0:8944495a171e5499 -->
<!-- tarav.context 473c89a0:c4ecebaa9007be2e -->

## Visual explorer belongs to Tarav Center

The User challenged the HTTP server and asked why the experiment was not
entirely hosted in the extension. The existing Center.Workflow shell is the
appropriate visual host; the HTTP choice was the agent's unnecessary detour.
<!-- tarav.context 473c89a0:944a943d7daaf1ba -->

The corrected implementation adds **Diagram explorer (experimental)** to
Tarav Center. Its left tree lists context steps, its center draws the graph
and SPARQL results, and its right panel inspects represented objects. The
extension owns its Python adapter and versioned JSON shapes. One `tarav run`
child retains runtime objects, the growing graph and navigation history,
communicating through stdin/stdout; the webviews use VS Code messages.
The standalone HTTP package is removed from Tarav. These transport/layout
details are agent implementation choices supporting the corrected placement.
<!-- tarav.context 473c89a0:944a943d7daaf1ba -->

Measured evidence: 353 maintained core tests pass after removing six HTTP
tests; 12 extension tests pass, including the actual Python subprocess and
renderer path. The unchanged Alice-message query produces one result before
runtime loading and two afterward. Extension 0.1.3 packages successfully.
Visual rendering in a VS Code window remains unverified. See extension
[request 012](../../../vscode-tarav-center/notes/live/012-future-diagram-explorer-impl-req.md)
and its [README](../../../vscode-tarav-center/README.md).
