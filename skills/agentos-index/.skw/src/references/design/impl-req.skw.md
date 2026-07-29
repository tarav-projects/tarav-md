# Impl.Req Component

This detailed product-design module is owned by `agentos-index --design`.

> $kw: --dev-from references/index-context-assembly.skw.md

`Impl.Req` is the implementation-request handoff produced by a `Design.Session`.

When a session produces implementation work, load `agentos-hugentics-impl --design`, which defines the full `Impl.Req` artifact format, vertical slice protocol, and design process.

## Role

`Impl.Req` translates the current design-session state into implementation-ready guidance. The artifact format and writing rules are owned by the `agentos-hugentics-impl` design module — this reference only covers the handoff from the design session side.

## Relationship To Design Session

`Design.Index` defines the conceptual background: concept fundamentals, appendix material, and concept-level session meta. `Session.Notes` may contain task-shaped observations, readiness questions, validation hints, and boundaries that are not yet execution-ready.

`Impl.Req` is the handoff surface for doing the work. It should not reopen design silently. If implementation planning reveals that the session design does not fit reality, surface the mismatch and return to the relevant section before proceeding.

## Boundaries

Do not create an `Impl.Req` automatically. Propose it when the session reaches implementation handoff, then wait for explicit user approval.

> $kw: --from Impl.Req
