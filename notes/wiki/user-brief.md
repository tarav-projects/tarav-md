# User Brief

<!-- tarav.sessions
f5845518 = claude-code:4ee3b84e-14fa-4aa9-9c6f-8d139954fe18 @f5845518e808c6cf0496f867fc656fdad9063980a184f7c3f15c54adf8fcb31f
-->

## Motivation

Most of the system is implemented by Agents, so the User's knowledge of it is
partial. When an Agent surfaces a POI or reports a state, it tends to speak in
situation-specific detail without the context needed to follow it. The User
needs a way to ask for an explanation from first principles with sufficient
context.
<!-- tarav.breadcrumb 39c0715942a141b8df200345a99975ffc45d09a05da7019ad2e39f048fb93976 -->

Sufficient context means the Agent links what it is talking about to actual
conversations the User has had. It need not surface the chats themselves;
following Breadcrumbs is enough. The link brings the User naturally to the
problem and the point. The presentation should be economical in characters.
<!-- tarav.breadcrumb ede9b7f588c704769956f38c253acbe86b832daf79749fec228d55274fb698c5 -->

## Relation to grounding

Agent proposal, accepted by the User: grounding (`--ground`) builds context
for the Agent; User Brief builds context for the User. It reuses the same
Breadcrumb and Chatlas lookups in the other direction, so it lives as a
module of `tarav-hugentics` and not as a separate skill.
<!-- tarav.breadcrumb a2a891b87939fc559915015f084be943ff0ce31838e709e3e62b0a89f28d9aae -->

## Workflow

Agent proposal, accepted by the User without changes:

1. Decompose the subject into the concepts needed to follow it.
2. Anchor each concept in the User's own Turns, through Wiki Breadcrumbs or
   Chatlas, and cite it briefly with date, short quote, and locator.
3. Mark concepts with no User Turn behind them as Agent-introduced. That gap
   is itself useful information.
4. Present in a fixed order: what the User already knows, what changed since,
   the point, and what is being asked of the User.
5. Keep a character budget and offer details on request.
<!-- tarav.breadcrumb 0a16696abdd3e76d3e3b7a0bdf15a68f9dd99c8c44126185981db2ad225de661 -->

## Name

The User named the route `--user-brief` to emphasize that the briefing is
directed to the User. `--brief` is its shortcut.
<!-- tarav.breadcrumb de517236e5848e289ea5b04c7b1e0ba278fef216f1754bcc9db7078f6eae82f4 -->

## Implementation

`skills/tarav-hugentics/references/user-brief.md`, authored in
`.skw/src/references/user-brief.skw.json` and routed from `SKILL.md`.
<!-- tarav.breadcrumb fb87ce16cbf2862d2da6eff9b6132a879ab36661eb4c2c7d0e53857f09598740 -->

The questions the Agent left open were settled by Agent default in the first
module: the route is read-only and leaves no record of the briefing; the
budget is about 15 lines and under about 30; without a subject it briefs the
most recent Agent message or POI. The User has not reviewed these defaults.
<!-- tarav.breadcrumb 0cf7a86093dd70c5b9745f61141354d4d3a1ac9c0d835ead0c9c81b220269f29 -->
