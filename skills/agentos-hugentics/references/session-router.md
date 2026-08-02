# Hugentic.Session.Router.Operation.Module

Use this module for `--session-router` and its `--what-now` and `--what-next` aliases.

The session router evaluates a report-only `Routing.Table` of `Usage.Pattern.Routing` rows over the current chat. It helps a user who is unsure what to do next by exposing a short ranked set of workflow candidates. It may recommend continuing or resuming existing work as well as entering or interrupting with another workflow.

It does not enter a workflow, mutate a surface, or silently change session control. The user routes by running one of the printed commands.

## Activation

Run when:

- the user invokes `--session-router`, `--what-now`, or `--what-next`
- the user asks which workflow fits the current situation
- the user is unsure whether to continue, resume, capture, design, implement, park, or inspect work
- the agent detects a strong workflow opportunity and a brief routing suggestion would reduce confusion

Proactive suggestions are offers, not recurring banners. Do not interrupt ordinary productive conversation or repeat substantially unchanged routes.

## Evidence

Use session-scoped evidence in this order:

1. User requests, corrections, approvals, constraints, goals, and explicit uncertainty.
2. Confirmed assistant responses the user accepted or acted on.
3. Current foreground workflow state and tool results that establish progress or incompleteness.
4. Artifacts explicitly active or mentioned in the chat, inspected only as needed to resolve their workflow state.

Ignore speculative assistant suggestions, abandoned branches, progress chatter, and unrelated repository state. Do not run broad project discovery merely to manufacture candidates.

## Candidate Transitions

Each candidate has one transition:

- `Continue` — advance the current foreground workflow from its next unresolved move.
- `Resume` — re-enter an incomplete earlier workflow or active artifact already established by the session.
- `Enter` — start a workflow that fits the current need and has no existing state to continue.
- `Interrupt` — take an `Alignment.Loop.Interruptions` branch into bounded capture, read-only capture mapping, parking, status, or grounding work while preserving the current return point.

Prefer coherent continuation over unnecessary workflow creation, but do not preserve a workflow merely because it was previously active. Rank applicability, user intent, incompleteness, currentness, and the cost of switching.

An incomplete workflow remains a candidate even when it is not foreground. Several incomplete workflows may coexist; rank rather than erase them.

## Candidate Contract

Return one recommended candidate and at most two alternatives.

Every candidate must contain:

- transition and workflow name
- concise evidence explaining why it fits now
- one fully resolved, copy-pasteable `Route.Command`

`Route.Command` uses the public form `/agentos-hugentics <args>`. It includes the actual scope, artifact, target, or focus inferred from session evidence. Never print placeholders such as `<topic>` or `<path>`.

Commands for `Continue` and `Resume` must reconnect to existing session or artifact state rather than imply a duplicate workflow. Use the established scope for in-chat work and the exact artifact path when one exists.

Do not list a candidate when a safe concrete command cannot be resolved. If no workflow is warranted, report that outside the candidate list instead of inventing a route.

## Output

```md
## Session.Route.Report

### Recommended · Continue Product Design

Why:
- the authority-surface protocol remains unresolved
- the current design session already owns this topic

Command:
/agentos-hugentics --design "continue the Touch.Authority.Surface protocol"

### Alternative · Resume Implementation

Why:
- the active Impl.Req remains incomplete and executable

Command:
/agentos-hugentics --execute "notes/live/601-support-resolver-impl-req.md"

### Alternative · Interrupt With Capture

Why:
- several accepted decisions remain only in chat

Command:
/agentos-hugentics --capture "capture the Touch.Authority.Surface decisions"
```

Adapt headings to the selected transitions and workflows. Keep each reason evidence-backed and compact.

## Boundaries

- `--status` reconstructs the current chat; `--session-router` recommends where session control could go.
- `--workflow-status` reports against one active workflow; `--session-router` compares possible workflow transitions across the session.
- routing is not execution; producing the report does not satisfy any workflow gate.
- ordinary conversation remains valid when no workflow would improve the session.
- do not dump the complete Hugentics command surface; expose only candidates supported by current evidence.
