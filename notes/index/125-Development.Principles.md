# Development.Principles

## Deep.Modules

- `Deep.Modules` is an architectural principle: small interface, hidden complexity
- a module should do a lot of work behind a simple contract
- the interface is the cost; the functionality behind it is the value

****

## Agent.Navigable.Codebase

- `Agent.Navigable.Codebase` is the structural principle that code should be organized so agents can explore naturally
- clear boundaries, discoverable entry points, self-documenting structure
- agents should be able to orient without reading everything

****

## Vertical.Slice

- `Vertical.Slice` is the preferred shape of implementation work
- a unit of implementation that cuts through the stack as deeply as possible to produce one observable result end-to-end
- the endpoints are chosen by the implementer — a passing test, a CLI command, an artifact output, an API response — but they should be meaningfully far apart in the stack
- the further apart the endpoints, the more real integration is tested — modules exercised as they are actually used, wired together
- design the implementation to reach the first observable endpoint as fast as possible — get to a testable running state first, then expand
- the first slice proves the integration path works; subsequent work extends horizontally: more cases, more features, more edge handling
- each slice should state: what changes, which path through the system it exercises, what observable result should exist, how the result will be checked
- pairs naturally with `Test.At.Boundaries` — test at the outer boundaries of the slice, which are the real system boundaries

****

## No.Legacy.Allowed

- `No.Legacy.Allowed` is an implementation constraint: do not leave stale state behind after implementation
- dead code, outdated artifacts, misleading docs, orphaned config, or superseded surfaces must be cleaned up as part of the implementation
- implementation is not done until the change is clean — no trailing debris
- applies to every `Impl.Req`, not just large refactors
- can only be overridden by an explicit statement — ignoring this is one of the main causes of poor quality implementation results

****

## Test.At.Boundaries

- `Test.At.Boundaries` is the testing guidance for implementation: test through public interfaces, not implementation details
- tests describe observable behavior and survive refactors
- prefer e2e and integration-style tests that exercise the full path of a `Vertical.Slice`
- feedback loops (tests, type checks, manual QA) form the quality ceiling — without them the agent codes blind
- every `Impl.Req` should specify what feedback loops validate the work
