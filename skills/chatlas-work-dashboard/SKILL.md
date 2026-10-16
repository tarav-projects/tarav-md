---
name: chatlas-work-dashboard
description: In-chat dashboard of recent supported Chatlas sessions — what you were doing, in which project, and where each thread stopped. Uses the retained Session Index plus exact-session Chatlas Query reads. USE WHEN the user wants to recap recent work, find a prior session, or decide what to resume. Called like a terminal command with `--since 3d`, `--all`, or `--session SESSION_ID`.
---

# Chatlas Work Dashboard

Operational `Package.Aux.Skill` under `tarav-chatlas-pkg`.

A conversation surface for recent Codex and Claude Code work. It writes no
report or product, but performs one explicit Chatlas update before reading its
derived Session Index. It then uses bounded exact-session Query reads.

This is a `Batchy.Skill` — called like a terminal command. Load `tarav-batchy-skills` for the full convention.

- `-h` / `--help` prints help instead of running.
- a bare duration (`3d`, `10m`, `2w`) resolves to `--since`.
- a bare session id resolves to `--session`.

## Skill.Arg.Section

### Skill.Arg::Since
- look-back duration: `30s`, `10m`, `4h`, `3d`, `2w`
- required: false
- default: `3d`
- flags: --since

### Skill.Arg::SinceDate
- absolute look-back start; naive values are local time
- required: false
- flags: --since-date

### Skill.Arg::Scope
- include every project instead of the current project
- required: false
- default: current project
- flags: --all

### Skill.Arg::Limit
- maximum sessions in the landscape
- required: false
- default: 10
- flags: --limit

### Skill.Arg::Session
- drill into exactly one session instead of rendering a landscape
- required: false
- flags: --session

## Boundary

- supports only providers normalized by current Chatlas; ignore unsupported
  indexed sessions
- uses only current `tarav chatlas` commands and the retained Session Index;
  never invokes retired Views, Products, or Chat.Index machinery
- does not own task state; use Hugentics status or parking for that
- prints continuation commands but never decides what the user should resume

## Read Plan

### 1. Select a stable session snapshot

Convert `--since` to an ISO timestamp with a small local script. Perform exactly
one update on the first read and retain its JSON outside model context:

```bash
tarav chatlas update > <tmp>/update.json
```

Then read the sharded JSONL rows under
`~/Documents/tarav/chatlas/index/sessions/`. With a small local `jq` or Python
projection:

- retain rows whose `last_activity_at` is at or after the cutoff;
- unless `--all` is present, retain rows whose `project_path` matches the
  current project root;
- sort by `last_activity_at` newest-first and keep at most `--limit`; and
- bring only those bounded fields into context: `last_activity_at`, `provider`,
  `instance`, `project_path`, `session_id`, `uri`, and `identity_hash`.

Use the parsed `--since-date` as the cutoff when supplied. Keep this selected
snapshot stable for all recap reads; do not update again during the run. The
Session Index is a derived selection surface, not transcript authority.

Each row provides `last_activity_at`, provider, instance, project path, native session id, URI, and neutral identity hash. Group by `project_path`; projects and sessions are newest-first.

### 2. Read bounded head and tail windows

Recap no more than eight sessions per run. Use the timestamped ledger to inspect
small Turn windows for each selected identity:

```bash
tarav chatlas render --identity-hash <hash> \
  --order oldest --limit 5 \
  --renderer Chatlas.Turn.Ledger.Renderer

tarav chatlas render --identity-hash <hash> \
  --order newest --limit 30 \
  --renderer Chatlas.Turn.Ledger.Renderer
```

The head usually identifies the original goal and the tail the latest state.
Select only the promising Turn hash prefixes, then render those exact Turns in
full through the default Renderer. Do not add `--update`: the initial update is
the workflow's sole freshness boundary. Exact Query findings and their resolved
Messages are the authoritative recap input; the ledger is only navigation.

### 3. Render the dashboard

For each substantive row show:

- short session id, relative age, and project grouping
- one `recap` sentence with two clauses: what the work is, then where it stands
- `/chatlas-session-continue --session <full-session-id>`

Write recaps in the user's vocabulary, present tense, usually first-person plural. A topic label is insufficient: the row must answer whether there is useful unfinished or completed state to return to. If head and tail concern different topics, say so briefly.

Keep provider, instance, URI, and identity hash out of ordinary rows; show them in drill-in output. End with one line naming sessions beyond the eight-recap cap or unsupported providers excluded by Chatlas2.

## Follow-Up

- **drill-in** — locate the sole Session Index row matching `session_id` (and
  provider/instance when needed), then inspect its oldest 5 and newest 30 Turns
  through the ledger before rendering selected Turns in full
- **widen** — rerun with a larger cutoff or `--all`
- **find** — select at most 50 recent Session Index candidates, then run
  exact-session `tarav chatlas query --identity-hash <hash> --text-contains
  '<fragment>' --order newest --limit 20 --json` over each; deduplicate matching
  sessions without performing another update
- **jump** — hand the exact session to `chatlas-session-continue`

Preserve the current landscape in conversation during follow-up; do not repeat the update while the user is exploring the same snapshot.

## Notes

- Session content is sensitive prior-session material; render only what the request needs.
- `project_path` is a lossy grouping spine, not a true work-thread identity.
- Git answers what landed; chat answers what participants communicated. This dashboard intentionally reads only chat.
