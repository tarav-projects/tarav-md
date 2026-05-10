# Design.Session

`Design.Session` is a scoped human-agent convergence surface for design work.

It helps humans and agents move from exploratory discussion toward durable design, TODO design, and implementation requests without pretending the full target is known upfront.

## Development As Convergence

In Agentos, development is a convergence process: humans and agents progressively align `Current.Implementation` with `Design.Target.Model`, while allowing both design understanding and implementation reality to refine each other.

`Design.Session` manages a scoped part of that convergence. It gives the human a place to settle design judgment, gives the agent a place to track open space and sufficiency, and gives implementation a path from design into action.

## Components

A design session is a system of composable convergence surfaces:

- `Design.Session.Core.Design`
- `Design.Session.TODO.Design`
- `Impl.Req`

`Design.Session.Core.Design` is the conceptual design layer. It captures named concepts, meanings, behaviors, relationships, open questions, and settled judgments produced through discussion.

`Design.Session.Core.Design` is like a staged fragment of `Design.Target.Model`: it is not necessarily the whole intended system, but it is the part being shaped inside the session scope.

`Design.Session.TODO.Design` is the task-design layer. It defines what should be done about the core design: objectives, guidance, evidence, validation, boundaries, and open questions for moving `Current.Implementation` closer to the staged target fragment.

`Impl.Req` is the implementation-request artifact that carries execution-facing work out of the session. It contains the concrete scope, constraints, ordered work when useful, vertical slices, validation, risks, review points, and deviation triggers needed to apply TODO design to `Current.Implementation`.

The usual flow is:

```txt
Core.Design -> TODO.Design -> Impl.Req
```

This is not a rigid waterfall. It is an authority and dependency direction: implementation should be downstream of explicit design/alignment material.

The components can be used independently. A session may produce only `Core.Design`, start from `TODO.Design` when core alignment already exists, or produce an `Impl.Req` directly when enough design alignment is already available.

`Core.Design` and `TODO.Design` use item sets. Items are the selected focus set for the session pass, not a registry of every relevant concept or task. `Impl.Req` is not item-focused by default; it follows the implementation-request artifact format.

The usual session rhythm is to move from the big picture into focused item work, consolidate useful convergence into artifacts, and return to the big picture to choose the next focus.

## Alignment State

`Design.Alignment.Core` is the set of design judgments that have been surfaced and explicitly settled with the user.

Material enters `Design.Alignment.Core` only when the user explicitly accepts or requests its inclusion. The material may originate from the user, the agent, source evidence, or another artifact, but surfacing material is not the same as settling it.

`Design.Open.Space` is all design material that has not been settled into `Design.Alignment.Core`. It includes undecided, unexamined, implicit, deferred, or agent-assumed material.

`Design.Open.Space` is not necessarily a problem. It marks what remains unsettled. If implementation is triggered, the agent may need to make pragmatic decisions from open space unless the user gates that decision.

`Delegation.Frontier` is the current boundary between `Design.Alignment.Core` and `Design.Open.Space`. It describes the settled/open shape of the current design state; it is not itself a permission rule, prompt, or workflow gate.

`Alignment.Sufficiency` is the agent's judgment of whether enough relevant human alignment has been settled for the current task. It is an agent-side expectation, not a user gate.

## User Gates

`Design.Session` preserves human authority over settled design judgment.

The agent may propose candidate design material, recommendations, warnings, and draft wording. Only the user can settle material into `Design.Alignment.Core`.

`User.Gated.Trigger` means the write path begins only after an explicit user trigger.

`User.Gated.Writing` means the agent may prepare changes, but must present the exact proposed text or diff before writing.

These gates are separate:

- trigger controls when the write path may begin
- writing controls whether proposed mutations must be previewed and approved
- alignment controls what design material becomes settled core

## Operating Principles

Design work should precede implementation work. The session should make enough design/alignment material explicit before treating implementation as routine execution.

Implementation requests produced from design sessions should prefer vertical slices when possible: thin end-to-end changes that can be verified through a relevant interface, artifact boundary, or observable behavior.

Implementation requests should include feedback loops. Feedback can be tests, type checks, manual QA, artifact inspection, review, user approval, or interface behavior checks.

Human taste and judgment remain part of the system. `Design.Session` does not prescribe one interaction style; discussion, interview, recommendations, and status warnings can all be valid when they fit the task.

Implementation should depend, in principle, on artifact data rather than fragile chat memory. This pressures sessions to produce useful durable surfaces.

Analysis should be evidence-based. If the question is about the codebase, inspect the codebase. If it is about an artifact, inspect the artifact. If it is about a source transcript, inspect the transcript or a trusted working summary.

## Boundaries

`Design.Session` is not a transcript, task tracker, generic meeting note, or implementation dump.

It does not replace `Agentos.Index.Notes`. Durable design truth should still converge into index notes when it becomes broadly reusable steering material.

It does not replace workflow skills. Skills operationalize session behavior, but major design-session semantics should not live only in skill prompts.

It does not require all design questions to be answered before implementation. Open space can remain; the important distinction is whether material has been settled into the core or left for agent judgment.

## Related Concepts

- `Agentos.Hugentic.Flow`
- `Agentos.Index.Notes`
- `Design.Target.Model`
- `Current.Implementation`
- `Progress.Gradient`
- `Design.Implementation.CoEvolution`
- `Agentos.Skills`

## Provenance

Promoted from `../../../../academy/notes/live/500-agentic-development-philosophy-core-design.md` and `../../../../academy/notes/live/501-agentic-development-philosophy-todo-design.md`.
