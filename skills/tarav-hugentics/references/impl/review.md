# Implementation Review Workflow

Load this module for `--impl --review` or `--review` with an `Impl.Req` input.

Review the live-note `Impl.Req` from outside its design context. Verify its
claims against current product evidence, resolve and inspect its
`Impl.Req.Diagram`, and report whether a context-free executer can follow it.

This workflow is read-only. It writes neither the artifact nor the Diagram and
does not execute the plan.

## Review Loop

1. **Cold read** — read the live note completely before opening cited files,
   design sources, or the associated Block. Record first-pass confusion; it is
   evidence of what a fresh executer will experience.
2. **Diagram audit** — resolve the Namespace, Model, and `Impl.Req.Block` named
   by `Impl.Req.Diagram`. Check that its Lines are relevant to this request,
   typed, supported, and not Agent-only coordination material presented as
   User-Touched authority.
3. **Product evidence audit** — verify load-bearing claims about files,
   symbols, commands, tests, and current behavior. Grade each checked claim as
   `verified`, `stale`, or `unverifiable`.
4. **Readiness audit** — rerun the Design readiness checkpoint from the cold
   executer's perspective.
5. **Report** — lead with `ready`, `ready-with-notes`, or `not-ready`; then give
   severity-ranked findings, cold-read friction, and evidence coverage.

Sample proportionally to risk: verify every load-bearing claim and avoid
spending attention on incidental prose.

## Boundaries

- Report only. Acting on findings requires a new instruction.
- Check groundedness and executability; do not reopen the accepted design as a
  general preference review.
- Use non-mutating inspection commands only. Test collection or documented dry
  paths are acceptable when they do not alter the product.
- Findings cite the concrete evidence checked; the review's authority is
  evidence, not confidence.

