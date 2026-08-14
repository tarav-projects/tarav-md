# Test: hugentics-session-router-01

## Purpose

Evaluate whether `tarav-hugentics --session-router` ranks evidence-backed workflow continuations and resumptions, with a fully resolved public route command for every candidate.

## Entry Path

`AGENTS.md -> load tarav-pkg -> load tarav-hugentics -> references/session-router.md`

## How To Run

Run from `agentos-pkg-testground/` in a fresh session. Give the tested agent only the `Subagent Prompt` plus normal project context. Do not provide the behavior tiers.

## Subagent Prompt

Use `tarav-hugentics --session-router` for this hypothetical chat. Do not edit files or enter a workflow.

The foreground discussion is a product-design session about `Touch.Authority.Surface`. Its qualification protocol remains unresolved. Earlier in the same chat, the user approved `notes/live/601-support-resolver-impl-req.md`; execution started but two slices remain incomplete. The chat also contains several accepted design decisions that may need capture.

Produce the in-chat routing report.

## Behavior Tiers

### Minimal Pass

- Recommends continuing the foreground product-design session.
- Retains the incomplete implementation as a resumable candidate.
- Gives every candidate a `/tarav-hugentics ...` command.
- Does not enter or execute any candidate.

### Expected Behavior

- Uses `Continue`, `Resume`, and optionally `Interrupt` as transition labels.
- Prints one recommendation and no more than two alternatives.
- Resolves the design scope and exact Impl.Req path into commands without placeholders.
- Gives compact session evidence for every route.
- Uses `--capture` only if the accepted uncaptured decisions justify it.

### Above Expected

- Explains why coherent continuation outranks switching to implementation.
- Makes continuation and resumption reconnect to existing state rather than describe new duplicate workflows.

### Overwork

- Dumps every Hugentics workflow or command.
- Scans the repository for unrelated candidates.
- Produces a general status report instead of ranking routes.

### Failure Signs

- Suggests only new workflows and omits incomplete existing work.
- Prints a candidate without a command.
- Uses placeholders such as `<topic>` or `<path>`.
- Mutates files, starts execution, or treats the report as workflow authorization.

## Navigation Trace

Expected: `tarav-pkg -> tarav-hugentics -> session-router -> answer`.
