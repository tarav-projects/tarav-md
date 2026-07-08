# agentos-pkg 107 back-linking report

Date: 2026-07-08
Target: `skills/agentos-pkg/design/107-design.md`
Chapter: `107-design.md`
Status: first backlink pass complete; report-only, no index writes applied

## Scope

- Worked one chapter only: `agentos-pkg/design/107-design.md`.
- Followed the `agentos-index --back-link` path: block -> git time -> Chatlas session/turn -> anchor.
- Kept index mutation gated. This pass only collected evidence and minted anchors.

## Minted anchors

- `@20260627-0`
  - turn: 2026-06-27T17:06:31.682Z
  - user: asks `Agentos.Skillware` to add tooling support like linters/builders/compilers
- `@20260705-2`
  - turn: 2026-07-05T15:00:17.475Z
  - user: confirms agendix as an untouched index member, hard grounded-summary rule, and a fallback place next to `appendix/`
- `@20260707-2`
  - turn: 2026-07-07T20:05:57.218Z
  - user: separates `Line.Type` from `User.Touched`
- `@20260708-5`
  - turn: 2026-07-08T06:12:45.416Z
  - user: proposes `agentos-index --agendix` as an automatic appendix-scoped capture module
- `@20260627-1`
  - turn: 2026-06-27T20:08:12.369Z
  - user: defines `Skill.Build.Surface` as builder workspace and as the place for anything that should not be on a runnable surface
- `@20260627-2`
  - turn: 2026-06-27T21:18:03.122Z
  - user: says a runnable surface must not pay bookkeeping noise for builder addressing

## Strong candidates

- [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:9)
  - line: `it is supported by a development toolchain ...`
  - proposed grounding: inline anchor `@20260627-0`
  - why: direct user request to add tooling support under `Agentos.Skillware`
  - git: `52a6f84` restored the block on 2026-07-05, but the content-bearing discussion is earlier on 2026-06-27

- [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:176)
  - line: friction gradient with `Index.Agendix`
  - proposed grounding: inline anchor `@20260705-2`
  - why: user explicitly accepts the agendix as the cheap capture layer and approves it as an untouched index member
  - git: introduced in `52a6f84`, renamed from `Agendix` to `Index.Agendix` in `4d957cc`

- [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:185)
  - line: `Index.Agendix` as an untouched member of the index surface
  - proposed grounding: inline anchor `@20260705-2`
  - why: user says the agendix is a member of the index, untouched, and should live next to `appendix/`

- [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:188)
  - line: hard rule that every agendix line is a grounded summary of chat discussion
  - proposed grounding: inline anchor `@20260705-2`
  - why: user explicitly says it must be summaries of chat discussions, covering rejections/constraints/highlights

- [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:192)
  - line: homeless material lands in a fallback file
  - proposed grounding: inline anchor `@20260705-2`
  - why: user explicitly accepts a fallback place for material that has no routed concept
  - note: this supports the fallback concept, not yet the exact `Unassigned-agendix.md` filename

- [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:197)
  - line: agendix lines are typed; validation point applies to agent capture
  - proposed grounding: inline anchor `@20260707-2`
  - why: user explicitly rejects tying `Line.Type` to `User.Touched`, which is the direct authority behind typed agendix lines

- [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:28)
  - line: `Skill.Build.Surface` complements `Skill.Runnable.Surface` and holds runnable-maintenance artifacts
  - proposed grounding: inline anchor `@20260627-1`
  - why: user directly defines `Skill.Build.Surface` as the builder workspace and the home for anything that should not be on a runnable surface

- [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:29)
  - line: home for derivation context, dependency declarations, lineage, dev material
  - proposed grounding: inline anchor `@20260627-1`
  - why: same turn directly supports the "anything it needs for doing its job" part of the current wording

- [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:21)
  - line: runnable surface stays free of non-runnable artifacts
  - proposed grounding: inline anchor `@20260627-2`
  - why: user explicitly says the runnable surface must not pay bookkeeping noise for builder addressing

## Partial / still ambiguous

- [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:20)
  - `Skill.Runnable.Surface` line 0 still lacks a direct user-side authority turn for the exact "purpose is to be run" definition wording.

- [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:22)
  - the "context being executable" rationale is well represented in [559-skillware-design-session.md](/Users/pereiro/projects/agentos-project/agentos-md/notes/live/559-skillware-design-session.md:24), but I have not yet isolated a direct user turn tight enough for inline grounding.

- [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:31)
  - the exact `build/` folder convention is present in the discussion, but the strongest wording I have so far is assistant-side. I have not yet isolated the matching user-side authority turn.

- [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:198)
  - `Concept.X/Agendix` file-shape rule likely comes from the 2026-07-08 module design discussion, but I have not yet isolated the exact user turn for the file heading rule.

- [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:199)
  - `agendix/Unassigned-agendix.md` is weaker than the general fallback concept.
  - current evidence: `@20260705-2` supports fallback existence; the exact `Unassigned-agendix.md` name appears in assistant proposal text, not in a confirming user turn I can cite yet.
  - finding: this is currently proposal-level, not strongly user-grounded.

## Next gated edit set

- If the user approves index mutation, the first safe inline-grounding patch is:
  - add `@20260627-0` to line 9
  - add `@20260627-2` to line 21
  - add `@20260627-1` to lines 28 and 29
  - add `@20260705-2` to lines 176, 185, 188, and likely 192
  - add `@20260707-2` to line 197

- Keep these out of the first patch:
  - line 20
  - line 22
  - line 31
  - line 198
  - line 199

## Commands / evidence used

- `git log -L` on blocks in `skills/agentos-pkg/design/107-design.md`
- `agentos chatlas query --tool-contains 107-design.md --tool-name Bash`
- `agentos chatlas views inline --identity-hash ... --around ... --filter turns --format json`
- `agentos chatlas anchory register --identity-hash ... --at ... --hint ...`
