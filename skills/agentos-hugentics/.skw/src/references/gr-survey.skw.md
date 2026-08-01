# Grounding.Survey.Workflow.Module

> $kw: --from Gr.Req --from Index.Line --from Support.Set --from Touch.Authority.Surface --from Touched.Data
> --dev-from references/index-context-assembly.skw.md

Use this module to run a grounding campaign's survey phase: sweep a scope, mint anchors, and produce a `Gr.Req` artifact. The grounding analogue of `agentos-hugentics --impl --design` - reconnaissance that reports back and does not act.

Aliases: `--gr-scout`, `--gr-scan`, `--gr-linker` all call this module.

This module NEVER changes `Index.Line` material. Its outputs are previewed anchors, anchor-only metadata maintenance, and the `Gr.Req` live note. Trailing-anchor maintenance is agent-owned and linter-guarded; any material line change remains gated through the normal edit workflow.

The survey locates `Touched.Data` on the current chat `Touch.Authority.Surface` realization and proposes one resolvable `Support.Set` per target.

Engine: `references/back-link.md` (archaeology) and `references/link.md` (edge linking) are the primitives this module drives — load both.

## Inputs

- a scope: a chapter file, a block list, or a whole depot; default depot rules follow `--depot`
- optionally an existing `Gr.Req` to extend (resume a campaign: fill `ambiguous` entries, add newly discovered targets)

## Campaign Loop

1. **Baseline.** `agentos index linter --depot <depot> --coverage all --scope <scope> --json` — record the exact command plus the line and block coverage meters in `Gr.Abstract` (coverage before); use `--coverage line` when a campaign deliberately tracks only inline anchors.
2. **Target selection.** Default selector: `agentos index blocks --depot <depot> --sort gr-density --scope <scope> --json` — the worklist head (zero-density blocks) is the grounding queue. Worked block by block per `back-link.md`'s pipeline (git-date → session tiers → user turn → mint-with-echo). Pick the route per block first:
   - user-originated wording → hunt the qualifying topical user turn
   - agent-drafted wording the user gated through → the qualifying approval or correction turn is the primary route, not a fallback; do not hunt for a topical statement that never existed
3. **Entry per target** in the `Gr.Set`:
   - evidence found → preview (`chatlas anchory preview`), escalate to context only when needed, then mint compactly with `register`; record the anchor, hint, why, and exact supported lines
   - no honest evidence on either route → entry at `status: ambiguous` with what was searched and what is missing — never a weak link
4. **Write the `Gr.Req`** (`notes/live/NNN-<scope>-gr-req.md`, numbering per `agentos-live-surfaces`): `Gr.Abstract` (scope, coverage before + projected-if-landed, status `gated set ready`), the `Gr.Set`, `Gr.Log` (unattached anchors, search dead ends worth recording).
5. **Report** compactly: entries by status, coverage delta on offer, the `Gr.Req` path.

## Discipline

- the current Chatlas specialization registers qualifying user turns only; user authorship alone does not establish subject-relevant touch
- one anchor may serve several entries when they ground on the same neighborhood
- mint after a target firms up, not speculatively; list any orphan mints in `Gr.Log`
- the module is resumable: re-running over the same scope extends the existing `Gr.Req` rather than forking a second one
