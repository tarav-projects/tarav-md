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
<!-- tarav.breadcrumb 8fa0ccfa3f07f81402abc2259424eeb9f52b61dc53b9c8e3802a1458f2d40780 -->

## Work defined as code

Standard usage declares what we are doing and how to validate it. Typed
definitions can carry context, executable operations, and checks that run over
real data, rather than relying only on agent judgments. This is a general Tarav
harness pattern, not a feature exclusive to Programs.
<!-- tarav.breadcrumb 87fe47432af70f1f3d4371fe813a67594913233fc37a1e6ca91706c365c7aef9 -->

Runs distinguish reusable definitions from particular executions, with their
inputs, context, evidence and results. Each Project can define its own Types,
specializing or reusing behavior as useful: the chosen organization of work is
expressed as code. This direction does not yet prescribe a complete run schema.
<!-- tarav.breadcrumb f599adcd438dabe7dd9de92af2c60839129963792db43aa4b4bc60a2cc76f79f -->
<!-- tarav.breadcrumb 01a4c1a22accb0a19d99edecb6fc60c1494e46fc97871951f7fd9ada641ccd98 -->

## Bootstrap general and specific spaces

Start with `TaravProgram` as a general base, potentially with no additional
features, and `ProjectProgram` for the first concrete use case. This gives the
type lineage room to distinguish general concepts from application-specific
behavior before the universal interface is known. Promote behavior already
used by at least two applications into a shared level; further intermediate
levels can emerge as use grows.
<!-- tarav.breadcrumb 5dd5222429a43f0334e009ef6e17ae59a6603996d86050693539e6d9c0feff93 -->

The user selected the plural Workflow name `ProgramsWorkflow` and requested
starting its bootstrap architecture. These are design decisions, not a claim
that the workflow has been implemented.
<!-- tarav.breadcrumb 1f787664455d44d3fff43495ac47d59685c9ca5fde2ee9299c44370965b7404c -->
<!-- tarav.breadcrumb 0e0fa0c0fdc04b33d4792d929a6725a9fc8dc11a5c94e992bfa696d9e3c10d0c -->

## Attachment and later derivation

Prefer an initial tree-shaped organization: Programs and their Types can be
attached to useful subjects, with Project attachment as the current example.
Later, forking can express derivation from another Program. The discussion
raised the distinction between subjects and Context, but did not establish a
mandatory generic `subjects` field or a final attachment/forking schema.
<!-- tarav.breadcrumb 86287d37389a6e53047c082b3c1d7f8030d7cc76aed570282b34339526377704 -->

## Programs and Harnessed Actions — 2026-10-09

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

In the discussion recorded in [Operator Context, Directives and Harnessed
Actions](operator-context.md), the User sees Programs and Harnessed Actions as
the same nature: definitions, particular running instances, tracking, and POIs
to work on. "Action" is the better name for the atomic unit; a Program might
be a root with active Actions. Whether they merge is left for later.
<!-- tarav.breadcrumb 523913d55074e823e516085ec0dab78b588599c5eb0b001f8425c6a06aae8ad3 -->
<!-- tarav.breadcrumb 5b6d366840ed0016fda2a9dd0a7a5135ac9dbcf79a071f88c88bedbe471c4dad -->

