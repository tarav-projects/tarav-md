# Design.Session.Knowledge.Module

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
- the current Chatlas/Anchory realization uses exact user turns and a trailing `Index.Line.Anchor`
- assistant material enters only through a qualifying user acceptance, correction, rejection, action, or delegation
- unresolved support is retained in `Session.Notes`; autonomous capture must not mint an unsupported design line

Grounding gives a line touched authority through its support; it does not make the live note stable, reviewed, or a `Touch.Authority.Surface`.

## Landing

One explicit `--capture --design-session` invocation satisfies `Edition.Trigger.User.Gated` for the bounded pass. It does not establish per-line `Reviewed.Content`.

1. Resolve or allocate the topic-scoped design-session artifact.
2. Compare the conversation against its existing `Design.Index`, notes, and stable Index context; do not duplicate already captured material.
3. Form-fit settled design deltas as typed, grounded lines under compact `Design.Block`s; keep unresolved material in `Session.Notes`.
4. Preview and register exact final line bodies as one anchor batch, then apply the returned line-to-anchor mapping in one patch.
5. Refresh `Session.Abstract` and append only meaningful lifecycle information to `Session.Log`.
6. Report the captured blocks, unresolved support, and any promotion candidates compactly.

The capture pass may create or maintain only the resolved design session. It does not mutate the stable Index, an `Impl.Req`, or another live artifact.

## Promotion

Promotion copies selected design-session material into its destination through that destination's own route and gates. A stable Index surface never cites the design session as an authority or dependency: `Reviewed.Cite.Closure` also forbids reviewed lines from citing its unreviewed lines. The destination takes ownership of promoted wording and preserves the original touched support where applicable.

Promotion does not delete the source material automatically. Maintain `Session.Abstract` or `Session.Log` so a later reader can distinguish captured working state from material already promoted.
