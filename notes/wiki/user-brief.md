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
<!-- tarav.breadcrumb 39c0715942a1 -->

Sufficient context means the Agent links what it is talking about to actual
conversations the User has had. It need not surface the chats themselves;
following Breadcrumbs is enough. The link brings the User naturally to the
problem and the point. The presentation should be economical in characters.
<!-- tarav.breadcrumb ede9b7f588c7 -->

## Relation to grounding

Agent proposal, accepted by the User: grounding (`--ground`) builds context
for the Agent; User Brief builds context for the User. It reuses the same
Breadcrumb and Chatlas lookups in the other direction, so it lives as a
module of `tarav-hugentics` and not as a separate skill.
<!-- tarav.breadcrumb a2a891b87939 -->

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
<!-- tarav.breadcrumb 0a16696abdd3 -->

## Name

The User named the route `--user-brief` to emphasize that the briefing is
directed to the User. `--brief` is its shortcut.
<!-- tarav.breadcrumb de517236e584 -->

## Implementation

`skills/tarav-hugentics/references/user-brief.md`, authored in
`.skw/src/references/user-brief.skw.json` and routed from `SKILL.md`.
<!-- tarav.breadcrumb fb87ce16cbf2 -->

The questions the Agent left open were settled by Agent default in the first
module: the route is read-only and leaves no record of the briefing; the
budget is about 15 lines and under about 30; without a subject it briefs the
most recent Agent message or POI. The User has not reviewed these defaults.
<!-- tarav.breadcrumb 0cf7a86093dd -->

## Topic generality

User correction: the POI was only an example. The general semantic is to
find the last thing discussed with the User about the topic, then explain the
topic from first principles; "from first principles" is the important part.
The topic is whatever the User asks to be briefed about. The skill must not
treat a POI as a different kind of object. A POI is a typical case, and the
Agent must understand what it is about to explain it correctly, like any
other topic.
<!-- tarav.breadcrumb 5b26ea9a0cd9 -->

The module now takes a `TOPIC`, adds an explicit "understand the topic
yourself first" step, and names the POI only as an example.
<!-- tarav.breadcrumb 7b37ced849e2 -->
