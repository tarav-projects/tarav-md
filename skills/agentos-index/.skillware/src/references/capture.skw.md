# agentos-index --capture

Use this module when the user wants the chat's content worked into kernel writing form and landed on index surfaces — "let's capture".

This module is a workflow module: it takes control of the session and runs the capture loop. The surfaces it lands on are governed by `Workflow.Neutral` knowledge modules — `references/edit.md` for index main and appendix, `references/agendix.md` for the agendix.

`Capture.Offer` is the same act at single-candidate scale: agent-initiated, one draft, same destination semantics. This module is the user-initiated, whole-conversation form.

Authority lives in the index: `Agentos.Index.System`, `Hugentic.Concept`, `Kernel.Writing`, `Grounding.Hugentic.Authority`, `Workflow.Neutral` own the concepts.

## The Capture Loop

A pass over the chat's uncaptured content, repeated until the content is exhausted or the user stops:

1. **Ground.** Run `references/ground.md` behavior over the conversation with a capture lens: what the index already models is out; gaps, tensions, and fresh `User.Touched` material are candidates.
2. **Propose.** Draft candidates in kernel writing form — new blocks, appended lines, revisions — typed and index-grade by default: user-touched content is index-eligible by right. The destination surface stays implicit; do not force it in advance — it is usually already present in the discussion.
3. **Discuss.** Iterate each draft with the user. The goal is to reason while preparing the kernel text — convergence happens in the discussion, not at the write.
4. **Approve.** User approval accepts the current form in chat — it is not a write. Approved material accumulates while the discussion rolls to the next item; the natural rhythm is a converging concept cluster, not item-by-item write ceremony.
5. **Land.** A separate, user-triggered act over approved material — all of it or a specific piece, to whatever surfaces the user names. After landing, re-ground: the index changed, and the next pass computes against it.

## Landing

> $kw: derived
> $kw. --from references/edit.skw.md#Landing Procedure
> $kw. --from references/agendix.skw.md#Landing Form
> $kw. --intent digest the two landing paths into the routing summary capture needs:
> $kw. gate semantics per surface and the form-fit move; do not restate the
> $kw. procedures — the knowledge modules own them

Landing form-fits approved material to the named surface, under that surface's own gate:

- **index main / appendix** — gated (`Edit.Trigger.Gated`, `Content.Verbatim.Gated`): a draft that already matches the surface lands as an approved forward pass through the `references/edit.md` landing procedure; a cluster approved in chat lands under one gate
- **agendix** — trigger-gated, not content-gated: the user's routing verdict is the whole gate; the agent refactors the material into agendix form per `references/agendix.md` and lands it, reporting at the end — a would-be-new-concept block has no agendix home, so its lines pool as promotion evidence
- the grounding anchor for a landed item targets its approval turn — where the user accepted the form; the landing trigger is execution, not evidence

> $kw. end-derived

## Behavior

- the discussion is free: capture is pulled by the user, never a standing obligation on the conversation — not every discussion involves blocks
- know what is approved and unlanded at any moment — the conversation itself is the record; no tracking mechanism is required
- material not worth the full hugentic review can always take the agendix exit rather than staying stranded in chat
- load `references/type.md` before drafting lines and `agentos-pkg/references/index-block-catalog.md` before proposing block wording
