# 616 — Structurally Unreachable Index Content

Status: open question, **no policy decided**. Parked for a later decision.
Discovered during the `tarav-pkg` Index.Retrofit campaign (`notes/live/611-agentos-pkg-grounding-campaign.md`), passes 3–5.

## The Observation

Some ungrounded index lines cannot be grounded for reasons that have **nothing to do with whether the user touched the subject**. Research effort does not help; the evidence is not there to find.

This is distinct from ordinary grounding debt. An ordinary ungrounded line is waiting for someone to look. These lines have been looked for, exhaustively, and the corpus cannot answer.

## Two Confirmed Causes

### 1. The vocabulary was never user-spoken

Corpus-wide `--user-contains` queries across every indexed session returned **zero** user turns for:

- `Work.Space` — 0 sessions
- `Source.Space` — 0
- `Design.Space` — 0
- `Constrained.Space` — 0
- `Fixed.Space` — 0
- `QA.Space` — 1 session, and there only inside an auto-generated compaction summary and an agent-authored re-derivation

That is 34 lines across 8 blocks (cluster `C5`). Two packets were dispatched against the two best candidate sessions; both returned essentially nothing, and the two proposals that did come back were rejected at the supervisor gate for resting on a turn that predated the terms.

The most likely explanation: this material is **agent-authored or agent-re-derived** from broader discussion the user conditioned in different words. The concepts may well be correct and wanted — they simply have no line-level user-touch evidence to anchor to.

### 2. The evidence is behind a compaction boundary

See `notes/live/615-compaction-boundary-blocks-retrofit-grounding.md`. Turns before a session's `/compact` boundary are not indexed and cannot serve as `Support.Set` members. Where the authoring conversation sits entirely before the boundary and was never revisited, the evidence is gone from the queryable dataset.

Unlike cause 1, this one **may be recoverable** — the raw provider artifact might still hold those turns even though the session model does not index them. That is open question 1 in note 615.

## Current Handling

Per `Index.Line`, an ungrounded line remains index content and carries `Index.Presumption`; missing grounding is debt, not a deletion trigger. So nothing was deleted, weakened, or force-grounded. Affected lines were left exactly as found.

That is the correct default. It is **not** a decision about what these lines should ultimately be.

## Why This Needs A Decision Later

The retrofit campaign currently reports these lines the same way it reports genuinely-not-yet-researched lines. That conflates two different things:

- "nobody has looked yet" — actionable debt
- "we looked everywhere and the corpus cannot answer" — not actionable by retrofit at all

Consequences of leaving them merged:

- **Coverage metrics mislead.** `gr-density` treats unreachable lines as reachable shortfall, so the depot can never reach a clean number and the metric stops being a useful target.
- **Repeat cost.** Nothing marks these clusters as exhausted. A future campaign will re-nominate, re-dispatch, and re-discover the same emptiness at full worker cost.
- **The real question stays hidden.** If a line has no user-touch evidence anywhere, the interesting question is not "how do we ground it" but "is this line index content at all, or agent-authored material that should be re-touched, demoted, or dropped."

## Options (not decided — listing only)

1. **A terminal state on the line or cluster.** Something like `unreachable` / `exhausted`, distinct from `ambiguous`, recording which queries were run and when. Makes coverage honest and prevents re-dispatch.
2. **Exclude from the coverage denominator.** Report reachable-grounding separately from total-grounding so the target is achievable.
3. **Route to a re-touch workflow.** Treat "agent-authored, never user-touched" as a design-session input: surface the lines to the user, who either touches them (making them groundable) or retires them.
4. **Accept permanently as `Index.Presumption`.** Explicitly declare that some index content is agent-derived and not expected to ground; document the standing rather than chase it.
5. **Recover the corpus first.** Pursue note 615's open question — if pre-boundary turns are recoverable, cause 2 shrinks and only cause 1 needs a policy.

These are not mutually exclusive; (5) is a prerequisite for knowing how big the problem actually is.

## What Is Needed To Decide

- **Scale.** Currently unknown. Only clusters actually dispatched have been tested, so the measured unreachable set (34 lines from C5, plus 9 ambiguous from C4) is a floor, not an estimate. A cheap corpus-wide phrase sweep over all ungrounded concept names would size it properly without spending workers.
- **The `/compact` answer** from note 615, which determines how much of this is recoverable versus structural.

## Related

- `notes/live/611-agentos-pkg-grounding-campaign.md` — campaign report; passes 3 and 5 carry the evidence
- `notes/live/615-compaction-boundary-blocks-retrofit-grounding.md` — the compaction-boundary mechanism
- `Index.Line` / `Index.Presumption` in `tarav-pkg` `design/107-design.md` — why an ungrounded line is still index content
