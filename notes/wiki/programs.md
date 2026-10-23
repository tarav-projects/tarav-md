# Programs

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
-->

## An operational tool, not an absolute account

Programs organize work through participation in a workflow. We enter it and
use it to track chosen work, query its records and logs, and inspect changes.
Its declarations are not an absolute account of everything we are doing or
intending. It is another tool for organizing life, not a universal view imposed
on activity outside it.
<!-- tarav.breadcrumb 8fa0ccfa3f07 -->

## Work defined as code

Standard usage declares what we are doing and how to validate it. Typed
definitions can carry context, executable operations, and checks that run over
real data, rather than relying only on agent judgments. This is a general Tarav
harness pattern, not a feature exclusive to Programs.
<!-- tarav.breadcrumb 87fe47432af7 -->

Runs distinguish reusable definitions from particular executions, with their
inputs, context, evidence and results. Each Project can define its own Types,
specializing or reusing behavior as useful: the chosen organization of work is
expressed as code. This direction does not yet prescribe a complete run schema.
<!-- tarav.breadcrumb f599adcd438d -->
<!-- tarav.breadcrumb 01a4c1a22acc -->

## Bootstrap general and specific spaces

Start with `TaravProgram` as a general base, potentially with no additional
features, and `ProjectProgram` for the first concrete use case. This gives the
type lineage room to distinguish general concepts from application-specific
behavior before the universal interface is known. Promote behavior already
used by at least two applications into a shared level; further intermediate
levels can emerge as use grows.
<!-- tarav.breadcrumb 5dd5222429a4 -->

The user selected the plural Workflow name `ProgramsWorkflow` and requested
starting its bootstrap architecture. These are design decisions, not a claim
that the workflow has been implemented.
<!-- tarav.breadcrumb 1f787664455d -->
<!-- tarav.breadcrumb 0e0fa0c0fdc0 -->

## Attachment and later derivation

Prefer an initial tree-shaped organization: Programs and their Types can be
attached to useful subjects, with Project attachment as the current example.
Later, forking can express derivation from another Program. The discussion
raised the distinction between subjects and Context, but did not establish a
mandatory generic `subjects` field or a final attachment/forking schema.
<!-- tarav.breadcrumb 86287d37389a -->

## Programs and Harnessed Actions — 2026-10-09

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

In the discussion recorded in [Operator Context, Directives and Harnessed
Actions](operator-context.md), the User sees Programs and Harnessed Actions as
the same nature: definitions, particular running instances, tracking, and POIs
to work on. "Action" is the better name for the atomic unit; a Program might
be a root with active Actions. Whether they merge is left for later. Actions
now exist in code (`tarav.l1.actions`, request 891); the Program bootstrap is
unchanged and the two are not yet related.
<!-- tarav.breadcrumb 523913d55074 -->
<!-- tarav.breadcrumb 5b6d366840ed -->

## Project-defined checked Programs — 2026-10-23

<!-- tarav.sessions
ec6cf584 = codex:01a1563b-2992-7c62-8a38-05c1cc75b1fe @ec6cf5849bb6c4e66f011b015415da94eeb1a17634872aa4fb9e25d8e065ab53
-->

The User chose a Program as an ordinary Tarav class in a Project's trusted
Python code. The shared base supplies execution and storage tooling; concrete
classes define States, Actions and their allowed connections. Python logic can
build connections and select available choices without requiring every Program
to implement a state-dispatch tree. An external script loader is unnecessary.
The Iterante history remains evidence, rather than a runtime to restore.
<!-- tarav.breadcrumb e8f916eefd03 -->
<!-- tarav.breadcrumb feaa5f105c8e -->
<!-- tarav.breadcrumb f3fd4bc0e0a8 -->

A State produces checks. A StateAction adds its prompt and prerequisites and
uses that same destination State to check arrival. Successful completion closes
the action and issues a fresh State token. Contextualized Project status reruns
the State's checks to detect subsequent drift: the token expresses the State
the agent is responsible for maintaining, rather than an unconditional claim
about the product. Arrival and maintenance therefore share their conditions.
<!-- tarav.breadcrumb 3709084ebb16 -->
<!-- tarav.breadcrumb e676573e8f8f -->
<!-- tarav.breadcrumb 9f52b6ed381c -->
<!-- tarav.breadcrumb 676441e72af5 -->

The User requested an implementation request and execution together. The chosen
scope keeps Program runs and their data outside the Project and exposes overall
executions and active StateActions through the existing Action registry.
Project Monitor reorganization is deferred; this work concerns Programs.
<!-- tarav.breadcrumb 0b8238bb9c27 -->
<!-- tarav.breadcrumb 7fb81ef4bd35 -->

Implementation observation: [request 955](../../../tarav-py/notes/live/955-project-program-runtime-impl-req.md)
adds graph declarations, JSON run data, checked start/choose/step, current-token
validation, cycle arrivals, terminal closure and explicit Action projection
recovery. `Project.programs` selects owned registered classes; `tarav program`
uses the normal Project harness. `tarav status --program-token` adds a per-run
coherence check. Runs retain action snapshots as the recovery authority; current
trusted class code supplies checks. The [operating guide](../../../tarav-py/src/tarav/l1/programs/README.md)
records commands and limits. These mechanics refine the earlier bootstrap;
they do not establish a universal subject/forking schema.

## Programs as Action graphs — 2026-10-23

The later discussion replaces the explicit State abstraction above. The User
wants all execution positions represented as Actions: NodeActions occupy nodes,
and EdgeActions traverse connections. A Program defines the graph and a run
records its active Action occurrences. The existing Action publication and
registry machinery should expose both roles.
<!-- tarav.breadcrumb a7724223cee5 -->
<!-- tarav.breadcrumb f7f39d4edaf8 -->

The Program owns its checks and their use. The User rejects mandatory check
ownership by a node or edge, and fixed meanings for acceptance checks. Check
classes may be reused across Actions as the Program author chooses. Therefore
the earlier automatic reuse of destination-State checks and source-State
validation is superseded as an engine rule; such reuse can remain a particular
Program's policy.
<!-- tarav.breadcrumb d373572af2c5 -->
<!-- tarav.breadcrumb 7b4861d9a7c2 -->

The mandatory mechanics stay small: a token identifies the current Action
occurrence, and a genuine node token cannot authorize an edge that node does
not permit. Moving onto an edge changes the active Action and its check
context; moving to its destination changes it again. The User requested a
new implementation request and execution of this revised design.
<!-- tarav.breadcrumb 07bb77dcb4e7 -->
<!-- tarav.breadcrumb 2c3a072da71c -->

Implementation observation: [request 958](../../../tarav-py/notes/live/958-program-action-graph-impl-req.md)
removes State/StateAction/StateReached and uses explicit three-part Transition
declarations. The Program selects checks through enter/status/complete slots;
none has built-in product validation semantics. Runs store an active collection
with occurrence tokens, independent of the source-node/edge distinction.
Terminal nodes are Actions completed explicitly. Real harness tests exercise
edge-specific checks and isolation between active occurrences, including two
in one run. The [guide](../../../tarav-py/src/tarav/l1/programs/README.md) explains
the measured API, token consumption and retained storage/recovery limits.

