---
name: chatlas-work-dashboard
description: In-chat dashboard of recent supported Chatlas sessions — what you were doing, in which project, and where each thread stopped. Uses Chatlas2 Session.Query plus bounded Chat.Query recaps. USE WHEN the user wants to recap recent work, find a prior session, or decide what to resume. Called like a terminal command — `--since 3d`, `--all`, `--session <id>`.
---

# Chatlas Work Dashboard

Operational `Package.Aux.Skill` under `tarav-chatlas-pkg`.

A read-only conversation surface for recent Codex and Claude work. It writes no report or retained product. Refresh once, select sessions by metadata, then read only small verified `Chat.Message` windows from each selected chat.

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

- supports only providers normalized by Chatlas2; ignore unsupported indexed sessions
- never invokes `tarav chatlas`, Chatlas1 Views, Products, file-touch queries, or full-session Chat.Index capture
- does not own task state; use Hugentics status or parking for that
- prints continuation commands but never decides what the user should resume

## Read Plan

### 1. Select a stable session snapshot

Convert `--since` to an ISO timestamp with a small local script. Perform exactly one update on the first read:

```bash
tarav chatlas --update sessions query \
  --project <current-project-root> \
  --active-after <cutoff> --sort newest --limit <limit> --json
```

- omit `--project` for `--all`
- use the parsed `--since-date` as the cutoff when supplied
- redirect JSON to a temporary file; bring only the bounded selected rows into context
- keep this snapshot stable for all recap reads; do not update again during the run

Each row provides `last_activity_at`, provider, instance, project path, native session id, URI, and neutral identity hash. Group by `project_path`; projects and sessions are newest-first.

### 2. Read bounded head and tail windows

Recap no more than eight sessions per run. For each selected identity:

```bash
tarav chatlas chat query --identity-hash <hash> \
  --sort oldest --offset 0 --limit 3 --json

tarav chatlas chat query --identity-hash <hash> \
  --sort newest --offset 0 --limit 8 --json
```

The head usually states the original goal. The tail records the latest state. Reverse the returned newest-first tail before reading it as a chronological window. Do not fetch the whole transcript merely to count turns or classify a session as thin.

### 3. Render the dashboard

For each substantive row show:

- short session id, relative age, and project grouping
- one `recap` sentence with two clauses: what the work is, then where it stands
- `/chatlas-session-continue --session <full-session-id>`

Write recaps in the user's vocabulary, present tense, usually first-person plural. A topic label is insufficient: the row must answer whether there is useful unfinished or completed state to return to. If head and tail concern different topics, say so briefly.

Keep provider, instance, URI, and identity hash out of ordinary rows; show them in drill-in output. End with one line naming sessions beyond the eight-recap cap or unsupported providers excluded by Chatlas2.

## Follow-Up

- **drill-in** — resolve `--session` with `tarav chatlas --update sessions query --session-id ...`; then read oldest 5 and newest 30 messages
- **widen** — rerun with a larger cutoff or `--all`
- **find** — use `tarav chatlas --update chat query --contains '<fragment>' --sort newest --session-limit 50 --limit 20 --json`, then deduplicate candidate sessions
- **jump** — hand the exact session to `chatlas-session-continue`

Preserve the current landscape in conversation during follow-up; do not repeat the update while the user is exploring the same snapshot.

## Notes

- Session content is sensitive prior-session material; render only what the request needs.
- `project_path` is a lossy grouping spine, not a true work-thread identity.
- Git answers what landed; chat answers what participants communicated. This dashboard intentionally reads only chat.
