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

