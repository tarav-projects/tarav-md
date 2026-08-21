> $kw: ^design-session-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^hugentics-batchy-runtime-contract
> --loading-dep SKILL.skw.md^hugentics-skill-arg-contract
> --loading-dep SKILL.skw.md^hugentics-authority-contract

# Design.Session.Knowledge.Module

> $kw: --from Agentos.Live.Note --from Design.Block --from Design.Req --from Edition.Trigger.User.Gated --from File.Numbering.Protocol --from Hugentic.Capture.Workflow --from Impl.Req --from Index.Line --from Index.Line.Anchor --from Kernel.Writing --from Line.Type --from Product.Design.Session --from Reviewed.Cite.Closure --from Reviewed.Content --from Support.Set --from Touch.Authority.Surface --from Touched.Data --from Touched.Surface.Index --from Volatile.Surface --from Workflow.Neutral
> --dev-from references/index-context-assembly.skw.md

`Design.Session.Knowledge.Module` is the `Workflow.Neutral` landing specialization for using a topic-scoped design session as the durable working target of `Hugentic.Capture.Workflow.Module`, operationalizing `Hugentic.Capture.Workflow`. It changes the target contract, not the capture workflow or router identity.

The artifact maintains the working state of a topic-scoped `Product.Design.Session`; it is not a second design workflow.

`--capture --design-session` selects the shared capture workflow and loads this module. The route defaults to `Alignment.Mode::Autonomous`: the user's invocation is the trigger for one agentic capture pass, without per-line wording review.

## When To Use

Use a `Design.Session` when design deltas should survive the conversation and accumulate around one topic without changing the stable Index.

Use `--design` instead when the user wants the active `Design.Req` codesign lifecycle. Use `--agendix` when the material should enter the concept-routed shadow of the Index rather than remain organized around a design topic.

## Artifact Contract

A `Design.Session` is an `Agentos.Live.Note` under the owning project's `notes/live/` directory:

```text
NNN-<short-topic>-design-session.md
```

Allocate `NNN` through `File.Numbering.Protocol` and the live-surface prefix command; never choose or renumber it by inspection.

Use this minimal shape:

```md
# <Short Title> - design-session

## Session.Abstract

## Design.Index

## Session.Notes

## Session.Log
```

- `Session.Abstract` keeps the topic, settled frame, active concern, and next useful move current.
- `Design.Index` holds compact `Design.Block`s written under `Kernel.Writing`; their typed `Index.Line`s carry the captured design deltas.
- `Session.Notes` preserves unresolved, provisional, or contextual material that should not disappear.
- `Session.Log` records material capture and promotion events, not a transcript.

No required status machine is added. Resolve an existing topic-matching session when unique; if several plausible targets exist, leave landing unresolved rather than choosing silently.

The file is maintained and may be long-lived, but it remains a `Volatile.Surface` in the canonical Agentos sense: a stable surface may not depend on it. Material leaves by promotion and copy into the destination that will own it.

## Grounding Contract

The embedded `Design.Index` is a topic-scoped `Touched.Surface.Index`:

- every captured design line has a `Line.Type`
- every line resolves through its own `Support.Set` to qualifying `Touched.Data`
- the Design.Session realization uses exact Chatlas2 user `Chat.Message.Ref` assertions and a trailing `Index.Line.Anchor`
- assistant material enters only through a qualifying user acceptance, correction, rejection, action, or delegation
- unresolved support is retained in `Session.Notes`; autonomous capture must not mint an unsupported design line

Grounding gives a line touched authority through its support; it does not make the live note stable, reviewed, or a `Touch.Authority.Surface`.

## Chatlas2 Capture Route

> $kw: ^design-session-chatlas2-consumer --note [CT] Design.Session capture understands the live conversation from current agent context and uses Chatlas2 to resolve selected evidence into exact user Chat.Message.Ref assertions ^c20260816-24u ^d20260816-38u

This route uses the same Chatlas2 grounding primitives as the other capture destinations; its distinct behavior is the Design.Session landing surface and ungated bounded pass.

1. **Resolve the session.** Use the exact provider-native session id supplied by the running harness or already present in the active workflow. If none is available, report `SESSION_SELECTOR_UNAVAILABLE` and leave the line unminted; do not fall back to Chatlas1 discovery.
2. **Understand and draft from current context.** The live conversation already loaded for the agent is the default capture source. Identify the settled design deltas, draft their final lines, and select the qualifying user messages already visible in that context. Do not reread the transcript merely to reconstruct understanding the agent already has.
3. **Resolve exact support.** For each selected message, run `tarav chatlas messages find --session-id <id> --side user --contains '<distinctive text>' [--exact] --json`. Refine until the selected message resolves uniquely, then retain its returned `member_ref`; it asserts session, stable message address, and current message hash.
4. **Escalate only when needed.** Refine an ambiguous lookup before reading more. Use `tarav chatlas turns get --session-id <id> --message-address <address> --hydrate --json` when associated turn material is necessary. Read `tarav chatlas views get --session-id <id> --view user --json` or `--view transcript` only when compaction removed necessary context, selected evidence cannot otherwise be resolved, or the caller explicitly requests historical capture. Views and hydrated turns are disposable projections, not authority surfaces.
5. **Author one manifest.** Put every final Design.Index line, its target block, and its ordered support references into one `Capture.Manifest`. Include stable message identity, diagnostic timestamp hints, and conjunctive content checks.
6. **Preview and land.** Preview the manifest, inspect the bounded plan, then run its `land` command. The command attaches each returned anchor, creates the records and Chat.Index projection, and verifies the exact result.

When Chatlas2 cannot recognize the session or resolve qualifying support, preserve the material in `Session.Notes`; inspect the retained raw archive when useful, and leave the design line unminted until Chatlas2 can support it.

## Landing

One explicit `--capture --design-session` invocation satisfies `Edition.Trigger.User.Gated` for the bounded pass. It does not establish per-line `Reviewed.Content`.

1. Resolve or allocate the topic-scoped design-session artifact.
2. Compare the conversation against its existing `Design.Index`, notes, and stable Index context; do not duplicate already captured material.
3. Form-fit settled design deltas as typed, grounded lines under compact `Design.Block`s; keep unresolved material in `Session.Notes`.
4. Preview and land the exact final lines through one `Capture.Manifest`; the Design.Session remains the primary landing surface while the command derives its Anchory, record, and Chat.Index effects.
5. Refresh `Session.Abstract` and append only meaningful lifecycle information to `Session.Log`.
6. Report the captured blocks, unresolved support, head-only backpropagation gaps, and any promotion candidates compactly.

The capture pass may create or maintain only the resolved design session. It does not mutate the stable Index, an `Impl.Req`, or another live artifact.

## Promotion

Promotion copies selected design-session material into its destination through that destination's own route and gates. A stable Index surface never cites the design session as an authority or dependency: `Reviewed.Cite.Closure` also forbids reviewed lines from citing its unreviewed lines. The destination takes ownership of promoted wording and preserves the original touched support where applicable.

Promotion does not delete the source material automatically. Maintain `Session.Abstract` or `Session.Log` so a later reader can distinguish captured working state from material already promoted.
