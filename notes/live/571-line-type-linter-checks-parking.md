# Line.Type Linter Checks — Parking.Note — CLOSED (574, executed 2026-07-08; all checks below implemented except the agent-side semantic lints, which stay agent work by design)

CPU-checkable `Line.Type` syntax checks for `agentos index linter` — the cheap mechanical tier under the agent-side semantic lints (`references/type.md`). Slated "later" in the typing implementation ladder (this session); parked so it is not lost.

## Candidate checks

- well-formed leading code: a line starting `- [` must match `- \[[A-Z]{2}\] ` exactly
- known code: the bracket code must be a registered `Line.Type` (`DF DC CT RJ PR FR EX GR` today; source the list from the index, not a hardcode, if cheap)
- `[GR]` lines must carry a trailing anchor token (`\^[0-9]{8}-[0-9]+`)
- a block's first line typed anything other than `[DF]` is a warning (untyped first line is legacy, not an error, until the fence hardens)
- source-axis syntax: `[AS:XX]` is well-formed only with a registered act code; `AS:` anywhere outside `agendix/` files is an ERROR (the index is user-turn-grounded)
- severity: warnings, not errors — untyped lines are pre-fence legacy by design (the `AS:`-outside-agendix check is the exception: error)

## Cross-system check (chatlas-aware, beyond the CPU linter)

- anchored-turn role check: resolve each `^YYYYMMDD-N` through anchory + chatlas and read the landing turn's role — `assistant` role without an `AS:` marker (or any `AS:` in index files) is a violation; first candidate for a chatlas-aware check tier

## Boundary

- semantic lints (contradicting `[DC]`s, violated `[CT]`s, reintroduced `[RJ]`s, overridden `[FR]`s) stay agent-side — never CPU-linter scope
- anchor *resolvability* stays in `anchory scan` (depot-dependent), not the index linter
