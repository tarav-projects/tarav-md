# agentos-index --gr-survey

Use this module to run a grounding campaign's survey phase: sweep a scope, mint anchors, and produce a `Gr.Req` artifact. The grounding analogue of `agentos-hugentics-impl --design` — reconnaissance that reports back and does not act.

Aliases: `--gr-scout`, `--gr-scan`, `--gr-linker` all call this module.

This module NEVER writes index or appendix surfaces. Its only outputs are anchors in the register (minting is free) and the `Gr.Req` live note. Landing is the reviewer's job (`references/gr-review.md`), gated per entry.

Engine: `references/back-link.md` (archaeology) and `references/link.md` (edge linking) are the primitives this module drives — load both.

## Inputs

- a scope: a chapter file, a block list, or a whole depot; default depot rules follow `--depot`
- optionally an existing `Gr.Req` to extend (resume a campaign: fill `ambiguous` entries, add newly discovered targets)

## Campaign Loop

1. **Baseline.** `agentos index linter --depot <depot> --warn-unlinked --json` — count `Index.Linter/Line.Unlinked` findings inside the scope; record in `Gr.Abstract` (coverage before).
2. **Target selection.** Unlinked blocks/lines in scope, worked block by block per `back-link.md`'s pipeline (git-date → session tiers → user turn → mint-with-echo).
3. **Entry per target** in the `Gr.Set`:
   - evidence found → mint (`chatlas anchory register`, echo-verified), entry at `status: proposed` with anchor, hint, why, landing form (block-level `[GR]` in `Grounding.Head` when several lines share the evidence; inline anchor for single-line targets)
   - wording originated agent-side → the approval-turn authority rule: anchor the user's acceptance turn, hint it as such
   - no honest evidence → entry at `status: ambiguous` with what was searched and what is missing — never a weak link
4. **Write the `Gr.Req`** (`notes/live/NNN-<scope>-gr-req.md`, numbering per `agentos-live-surfaces`): `Gr.Abstract` (scope, coverage before + projected-if-landed, status `gated set ready`), the `Gr.Set`, `Gr.Log` (unattached anchors, search dead ends worth recording).
5. **Report** compactly: entries by status, coverage delta on offer, the `Gr.Req` path.

## Discipline

- anchors target USER turns only (`Grounding.Hugentic.Authority`); the reviewer's linter pass will mechanically verify every landing — mint accordingly
- one anchor may serve several entries when they ground on the same neighborhood
- mint after a target firms up, not speculatively; list any orphan mints in `Gr.Log`
- the module is resumable: re-running over the same scope extends the existing `Gr.Req` rather than forking a second one
