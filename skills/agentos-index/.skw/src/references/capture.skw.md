# agentos-index --capture

> $kw: --from Agentos.Index.System --from Alignment.Mode --from Capture.Gradient --from Capture.Offer --from Edition.Trigger.User.Gated --from Grounding.Hugentic.Authority --from Hugentic.Concept --from Kernel.Writing --from Not.A.Wall.Of.Text --from User.Command --from User.Command.Arg --from User.Touched --from Verbatim.User.Gated --from Workflow.Neutral

Use this module when the user wants the chat's content worked into kernel writing form and landed on index surfaces — "let's capture".

This module is a workflow module: it takes control of the session and runs the capture loop. The surfaces it lands on are governed by `Workflow.Neutral` knowledge modules — `references/edit.md` for the ontology and appendix, `references/agendix.md` for the agendix.

`Capture.Offer` is the same act at single-candidate scale: agent-initiated, one draft, same destination semantics. This module is the user-initiated, whole-conversation form.

Authority lives in the index: `Agentos.Index.System`, `Hugentic.Concept`, `Kernel.Writing`, `Grounding.Hugentic.Authority`, `Workflow.Neutral` own the concepts.

## The Capture Loop

A pass over the chat's uncaptured content, repeated until the content is exhausted or the user stops:

1. **Ground.** Run `references/search.md` behavior over the conversation with a capture lens: what the index already models is out; gaps, tensions, and fresh `User.Touched` material are candidates.
2. **Propose.** Draft candidates in kernel writing form — new blocks, appended lines, revisions — typed and index-grade by default: user-touched content is index-eligible by right. The destination surface may stay implicit while exploring; approval-ready drafts show the concrete landing target per `references/edit.md`.
3. **Discuss.** Iterate each draft with the user. The goal is to reason while preparing the kernel text — convergence happens in the discussion, not at the write. (`Interactive` only — an `Autonomous` pass skips to landing.)
4. **Approve.** User approval accepts the current form in chat — it is not a write. Approved material accumulates while the discussion rolls to the next item; the natural rhythm is a converging concept cluster, not item-by-item write ceremony. (`Interactive` only.)
5. **Land.** A separate, user-triggered act over approved material — all of it or a specific piece, to whatever surfaces the user names. After landing, re-ground: the index changed, and the next pass computes against it.

## User.Command Checkpoints

- These checkpoints apply the skill's declared `User.Command` transitions and resolve each required `User.Command.Arg` against the foreground capture state.
- When an approval-ready draft becomes foreground, pause with `::approve [target]` (`::approved` equivalent). The command accepts that exact draft and never writes it.
- Approved material accumulates as unlanded workflow state. At a later pause, expose `::land [target]` (`::write` equivalent) whenever at least one approved target is available.
- A bare command may resolve its contextual target only when one foreground target is possible. If several drafts or approved sets could receive it, ask which one and leave every transition unresolved.
- Free-form replies continue the discussion without crossing either gate. If discussion changes an approved draft's wording or landing target, return that draft to approval-ready state.
- Print the available command line only at a real pause or on a status request. Do not append it to ordinary conversational turns.

Example pause footer:

```text
Available User.Commands:
  ::approve [target]  (also ::approved)
  ::land [target]     (also ::write; approved material only)
```

## Mode

- capture accepts `Alignment.Mode` — `Interactive` (default) or `Autonomous`
- `Interactive` runs the full loop: checkpoints are alignment opportunities, discussion and approval happen per item
- `Autonomous` runs without user prompting: the loop collapses to ground → propose → land → report, and it can land only on the agendix — a user gate (`Edition.Trigger.User.Gated`) cannot be resolved autonomously
- `--AUTO` is the extreme case as a flag: the full workflow automatic, chat to agendix, the invocation is the one trigger that covers the pass
- `--agendix` presets the agendix destination and defaults to `Autonomous`; the user engaging mid-pass simply is `Interactive`

## Landing

> $kw: --derived
> --from references/edit.skw.md#Landing Procedure
> --from references/agendix.skw.md#Landing Form
> --intent digest the two landing paths into the routing summary capture needs:
> --cont gate semantics per surface and the form-fit move; do not restate the
> --cont procedures — the knowledge modules own them

Landing form-fits approved material to the named surface, one rung up the `Capture.Gradient`, under that surface's own gate. Approval-ready candidates show the concrete `Landing:` file and `Target:` ontology location before the draft text; the destination can stay loose only while the discussion is still exploratory.

- **ontology / appendix** — gated (`Edition.Trigger.User.Gated`, `Verbatim.User.Gated`): a draft that already matches the surface lands as an approved forward pass through the `references/edit.md` landing procedure; a cluster approved in chat lands under one gate
- **agendix** — ungated, user-triggered: the routing verdict is the whole trigger; material lands in kernel form per `references/agendix.md` — lines under routed concepts, candidate blocks intact as path-children — captured but ungated, promotion-ready, reported at the end
- the grounding anchor for a landed item targets its approval turn — where the user accepted the form; the landing trigger is execution, not evidence

> $kw. end

## Behavior

- the discussion is free: capture is pulled by the user, never a standing obligation on the conversation — not every discussion involves blocks
- `Not.A.Wall.Of.Text` governs the loop: the opening turn may be a larger grounding summary, but it ends landing on the first candidate draft — prime the discussion, the user redirects if they want another; from there stay on target: one to a few drafts per turn, alignment per block, never a re-dump of the full harvest
- know what is approved and unlanded at any moment — the conversation itself is the record; no tracking mechanism is required
- material not worth the full hugentic review can always take the agendix exit rather than staying stranded in chat
- load `references/type.md` before drafting lines and `agentos-pkg/references/index-block-catalog.md` before proposing block wording
