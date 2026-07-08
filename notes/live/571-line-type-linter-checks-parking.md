# Line.Type Linter Checks — Parking.Note

CPU-checkable `Line.Type` syntax checks for `agentos index linter` — the cheap mechanical tier under the agent-side semantic lints (`references/type.md`). Slated "later" in the typing implementation ladder (this session); parked so it is not lost.

## Candidate checks

- well-formed leading code: a line starting `- [` must match `- \[[A-Z]{2}\] ` exactly
- known code: the bracket code must be a registered `Line.Type` (`DF DC CT RJ PR FR EX GR` today; source the list from the index, not a hardcode, if cheap)
- `[GR]` lines must carry a trailing anchor token (`@[0-9]{8}-[0-9]+`)
- a block's first line typed anything other than `[DF]` is a warning (untyped first line is legacy, not an error, until the fence hardens)
- severity: warnings, not errors — untyped lines are pre-fence legacy by design

## Boundary

- semantic lints (contradicting `[DC]`s, violated `[CT]`s, reintroduced `[RJ]`s, overridden `[FR]`s) stay agent-side — never CPU-linter scope
- anchor *resolvability* stays in `anchory scan` (depot-dependent), not the index linter
