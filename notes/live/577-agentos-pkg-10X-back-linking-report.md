# agentos-pkg 10X back-linking report

Date: 2026-07-08
Target: `skills/agentos-pkg/design/10X-design.md`
Chapter set: `100`-`107`
Status: report-only; no index or appendix files changed

## Scope

- Baseline run: `agentos index linter --depot skills/agentos-pkg --warn-unlinked --json`
- Chapter-set baseline (`100`-`107` only): `1202` `Index.Linter/Line.Unlinked` findings
- Dominant evidence session for this pass: `99144906-781e-43cc-9d27-b40f166e2acf` (`identity_hash` `9d194db7...`)
- Truth-tier note:
  - `--file-write 105-design.md` and `--file-write 107-design.md` did not give usable hits here
  - `--tool-contains ... --tool-name Bash` did

## Minted anchors

- `@20260708-8`
  - turn: `2026-07-08T13:07:52.462Z`
  - hint: user says chat/index anchors should always target user turns; approval-turn authority rule
  - intended landing: `Grounding.Hugentic.Authority`

- `@20260706-1`
  - turn: `2026-07-06T13:04:26.833Z`
  - hint: user says Anchory is an Agentos subsystem, not per-project, and connects with Chatlas
  - intended landing: `Anchory.System`

- `@20260705-3`
  - turn: `2026-07-05T14:34:37.575Z`
  - hint: user lays out the friction gradient: chat, agendix, appendix, index main
  - intended landing: `Writing.Friction.Reduction`

## Strong candidates

- [105-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/105-design.md:81)
  - block: `Grounding.Hugentic.Authority`
  - proposed anchor: `@20260708-8`
  - why: exact user-side authority for the “anchors target user turns” rule; this is stronger than an assistant-side explanation and fits the approval-turn authority judgment

- [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:324)
  - block: `Anchory.System`
  - proposed anchor: `@20260706-1`
  - why: exact user correction that the register is not project-local and should connect with Chatlas

- [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:173)
  - block: `Writing.Friction.Reduction`
  - proposed anchor: `@20260705-3`
  - why: exact user-side statement of the friction gradient and the “do not flush the index” floor

- [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:183)
  - block: `Index.Agendix`
  - proposed anchor: existing `@20260705-2`
  - why: already-supported agendix authority turn remains the strongest fit for the untouched-member / grounded-summary core of the block

## Partial-ambiguous

- [105-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/105-design.md:59)
  - `Grounding.Retrieval.Boundary` is probably supportable from the 2026-07-05 grounding redesign turn, but I did not isolate a clean user quote narrower than the giant redesign summary/replay neighborhood

- [105-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/105-design.md:69)
  - `Chat.Grounding.Target.Block` likely has authority in the survivor-revisit thread, but I do not yet have a crisp user turn tight enough for a no-weak-link landing

- [105-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/105-design.md:5)
  - `Kernel.Block.Grounding` already has a `Grounding.Head` line in its appendix, but the linter still reports lines 7-15 as unlinked; I am not projecting meter movement from more block-level `[GR]` landings until that behavior is clarified

- [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:183)
  - `Index.Agendix` has more support than one anchor can comfortably summarize; the block is strong semantically, but a clean backlink batch would likely want more than one landing if the user later chooses inline cleanup

## Next gated edit set

- Block-level `[GR]` entries
  - `appendix/Grounding.Hugentic.Authority-appendix.md`
    - add one `Grounding.Head` line using `@20260708-8`
  - `appendix/Anchory.System-appendix.md`
    - add one `Grounding.Head` line using `@20260706-1`
  - `appendix/Writing.Friction.Reduction-appendix.md`
    - either add a second `Grounding.Head` line with `@20260705-3`, or decide the existing `@20260705-0` already covers the block strongly enough

- Inline anchors
  - optional, meter-moving subset only
  - `107-design.md:175,177,178,179` with `@20260705-3`
  - `107-design.md:326-333` with `@20260706-1`
  - `105-design.md:83-87` with `@20260708-8`

## Coverage numbers

- Before: `1202`
- Projected after, recommended block-level-only landing: still `1202` on the current linter meter
  - evidence: `Kernel.Block.Grounding` already has a block-level `Grounding.Head` line, but lines `7-15` in `105-design.md` still report as `Line.Unlinked`
- Projected after, if the optional inline subset also lands: `1185`

## Unattached minted anchors

- none in this pass

## Commands used

- `agentos --help`
- `agentos index linter --help`
- `agentos index linter --depot skills/agentos-pkg --warn-unlinked --json`
- `git log -L ...`
- `agentos chatlas query --project-base agentos-project --file-write ...`
- `agentos chatlas query --project-base agentos-project --tool-contains ... --tool-name Bash`
- `agentos chatlas query --project-base agentos-project --message-contains ...`
- `agentos chatlas views inline --identity-hash ... --contains ... --role user --around ... --radius 6 --filter turns --format json`
- `agentos chatlas anchory register --identity-hash ... --at ... --hint ...`
