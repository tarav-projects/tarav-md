---
name: chatlas-work-dashboard
description: In-chat dashboard of recent work across Chatlas sessions — what you were doing, in which project, and where each thread stopped. Renders a landscape from `agentos chatlas recents`, then recaps sessions from the head and tail of their zip-transcript. USE WHEN the user wants to recap the last days of work, find a prior session, or decide what to resume. Called like a terminal command — `--since 3d`, `--all`, `--session <id>`.
---

# Chatlas Work Dashboard

Operational `Package.Aux.Skill` under `tarav-chatlas-pkg`.

A chat tool, not a report generator. It renders a working view of recent sessions so the user can explore what they were doing, find the session they half-remember, and decide what to resume. Nothing is written to disk.

This is a `Batchy.Skill` — called like a terminal command. Load `tarav-batchy-skills` for the full convention.

- `-h` / `--help` prints the help into the chat instead of running (`Batchy.Skill.Help`).
- a bare duration (`3d`, `10m`, `2w`) resolves to `--since`.
- a bare session id resolves to `--session`.

## Skill.Arg.Section

### Skill.Arg::Since
- look-back window as a duration: `30s`, `10m`, `4h`, `3d`, `2w`
- required: false
- default: `3d`
- flags: --since
- examples: --since 2w

### Skill.Arg::SinceDate
- absolute look-back start; naive values are local time
- required: false
- flags: --since-date
- examples: --since-date 2026-07-28, --since-date 2026-07-28T14:00

### Skill.Arg::Scope
- which projects to include
- required: false
- default: the current project
- flags: --all
- examples: --all

### Skill.Arg::Limit
- maximum sessions to place in the landscape
- required: false
- default: 10
- flags: --limit

### Skill.Arg::Session
- drill into one session instead of rendering the landscape
- required: false
- flags: --session
- examples: --session 019fb5c1-7d23-7332-8654-2e863e4e7ef0

### Skill.Arg::Files
- add the touched-file signal to a drill-in
- required: false
- default: off
- flags: --files

## Boundary

- read-only; never produces, commits, or stages a Chatlas product
- never writes a note, digest, or artifact — the dashboard lives in the chat
- does not own task state; it reads history and navigates it. Pending-work tracking belongs to `tarav-hugentics --status` and parking notes
- routing is limited to printing jump commands; it does not decide what the user should work on

## Cost Model

Three tiers. Never skip ahead — each tier is roughly an order of magnitude more expensive than the one above it.

| Tier | Source | Cost |
|---|---|---|
| Landscape | `chatlas recents` | one call, all sessions |
| Recap | `zip-transcript` head + tail | ~3KB per session |
| Escalation | touched files, wide tail, full transcript | seconds per session |

Recap is capped at **8 sessions** per run. Above the cap, render the landscape alone and say which sessions were left un-recapped, so the user can narrow the window or point at rows.

## Step 1: Landscape

Always start here. One call.

```bash
agentos chatlas recents --since 3d --last-turns 3 --limit 10 --project --json
```

- omit `--project` when `--all` is set
- use `--since-date <value>` in place of `--since` when the user gave an absolute date
- pass `--update` only when the user says results look stale

Each entry carries `last_activity_at`, `created_at`, `provider`, `instance`, `project_path`, `session_id`, `uri`, `user_turn_count`, and `last_user_turns` (each `{at, text}`).

Group by `project_path`. Sort projects by most recent activity, sessions newest-first within each.

## Step 2: Recap

For each session in the landscape, up to the cap, read both ends of the compressed transcript.

Skip sessions whose `user_turn_count` is under 2 — they hold no recoverable recap. Skipping them does not consume the cap, so the budget goes to sessions that can actually be recapped.

```bash
agentos chatlas views get --view zip-transcript --session-id <id> --range=:3
agentos chatlas views get --view zip-transcript --session-id <id> --range=-8:
```

**The `=` is required.** Bare `--range -8:` makes the leading `-` parse as a flag and the call fails. `--range` is supported on `zip-transcript` only — not `user`, `full`, `transcript`, `replay`, or `events`.

- the **head** is where the user states the goal, and often names a predecessor session being continued
- the **tail** carries the assistant's closing report — usually the sentence saying whether the work landed

A session may already have a `zip-transcript-summary` product. Use it when it is free:

```bash
agentos chatlas products status --product zip-transcript-summary --session-id <id> --json
```

If `state` is `fresh`, read the artifact at `products path` instead of the head and tail. If it is `missing` or stale, fall back to head and tail. **Never produce or commit the product** — that spawns billed agents and is the user's explicit call, not the dashboard's.

## Step 3: Render

```md
## Work Dashboard · last 3d · agentos-project

### agentos-project · 4 sessions · 16h ago → 2m ago

▸ 019fb5c1 · 2m ago · 103 turns
  recap  We're implementing cross-skill Context.Loading reachability in the skw
         graph; `--reachable-from` and the typed `--load` edges landed, all 13
         managed skills resolve from tarav-pkg, 632 tests pass, and the changes
         are still uncommitted.
  jump   /chatlas-session-continue --session 019fb5c1-7d23-7332-8654-2e863e4e7ef0

▸ 019fb4d0 · 28m ago · 33 turns
  recap  We're processing TODO orders against a randomly picked PaperSON package;
         the session stalled — the last three user turns repeat the same request
         and nothing reports back as finished.
  jump   /chatlas-session-continue --session 019fb4d0-18ee-7e52-b0bb-c4062b5f9017

thin · 4 sessions under 2 user turns · 019fc858 019fc685 019fc4ac 019fc857
```

### The recap line

This is the whole point of the dashboard. Get it right and the rest is decoration.

`recap` is a **sentence**, never a label. It carries two clauses:

1. **what the work is** — from the head, where the user states the goal
2. **where it stands** — from the tail, usually the assistant's closing report

Write it the way the user would describe the session to a colleague: present tense, first person plural, their own vocabulary and named concepts. Two to four lines. A reader who was not in that session should understand both the subject and the state.

```text
bad    recent  Hugentics capture and Agendix work
bad    recent  integrate the new Chatlas view/product into this dashboard design
good   recap   We're building a Chatlas-backed work dashboard skill for recapping
               recent sessions; the draft SKILL.md is written, symlinked, and its
               commands verified working.
```

The bad lines are topic labels. They name a subject and say nothing about state, so they cannot answer "should I go back to this?" — which is the only question the dashboard exists to answer.

Both ends are required. The tail alone gives state with no subject; the head alone gives a goal that may have been abandoned six hours ago.

### Other render rules

- always show the relative age; it is the primary orientation cue
- every substantive row carries one runnable jump command
- collapse sessions with under 2 user turns into a single `thin` line at the end of the project block. They have no recoverable recap and must not each consume a row
- do not pad rows with metadata the user did not ask for. Provider, instance, and URI belong in a drill-in, not the landscape
- when head and tail disagree about the topic, say so in one clause rather than picking one — that mismatch usually means the session ended on a tangent
- close with one line naming what was not covered: sessions past the recap cap, or the projects excluded by the default scope

## Step 4: Follow-Up

The dashboard is a conversation surface. After rendering, stay available for:

- **drill-in** — `--session <id>`: widen the tail (`--range=-30:`), and with `--files` add the touched-file signal
- **widen** — re-run with a larger `--since`, or `--all` for the cross-project view
- **find** — the user describes a session they half-remember; resolve it with `agentos chatlas query --user-contains "<fragment>"` rather than re-reading transcripts
- **jump** — hand off to `chatlas-session-continue` for resuming, or `chatlas-session-zip-transcript` for full recall

Keep the working set in the conversation: which sessions are in view, which have been drilled into, what the user concluded about each. Do not re-run Step 1 when the user is still exploring the current landscape.

### Touched files (escalation)

```bash
agentos chatlas file-edition-pois --session <id> --json
```

Rank by frequency and show the top few paths. The raw list runs to dozens of files and is noise unranked. Touched files often cross project boundaries — that is signal, not error, and it is a truer indicator of what the work was about than `project_path`.

## Notes

- Session content is sensitive prior-session material; render only what the current request needs.
- `project_path` is a lossy spine — one thread often spans sessions and one session often spans threads. Say so when it matters rather than implying the grouping recovers true work threads.
- Git evidence is deliberately out of scope for this version. When it arrives it answers a different question: git says what landed, chat says what was intended.
