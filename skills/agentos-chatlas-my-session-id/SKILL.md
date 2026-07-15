---
name: agentos-chatlas-my-session-id
description: Discover the current agent's OWN native session id ("which session am I in?") by refreshing Chatlas, pulling the recently-active candidate set, and locally matching the agent's own verbatim user turns against it until exactly one candidate remains. Returns the native session id plus the neutral Chatlas identity. USE WHEN an agent needs to know which provider session it is running inside. Called like a terminal command — runs with no required args; optional `--provider` narrows the search.
---

# Chatlas My Session Id

Operational `Package.Aux.Skill` under `agentos-chatlas-pkg`.

Answer the question "which session am I in?" for the running agent. The agent has no direct read of its provider session id, but its own turns are recorded in the provider transcript, so it can find itself: refresh Chatlas, pull the recently-active sessions, and match distinctive fragments of its **own** verbatim user turns against that set until exactly one session remains. That session is the caller.

This is a `Batchy.Skill` — called like a terminal command. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints the help into the chat instead of running (`Batchy.Skill.Help`).
- runs with no required arguments; a bare provider name resolves to `--provider`.

## Execution Mode

Run this skill **inline in the caller context** — do not spawn a separate agent. This is the opposite default from sibling Chatlas skills (`chatlas-session-continue`, `chatlas-session-zip-transcript`), and deliberately so:

- The match fragments must come from the caller's **own** verbatim user turns. Only the caller can see its own conversation; a spawned agent is in a different session and cannot supply them.
- The expensive payload (the `recents` JSON) is kept out of the model by matching it in a **subprocess** and surfacing only the result. Agent isolation would buy nothing.

## Token Discipline

The `recents` payload is large (tens of thousands of tokens for a wide window). Never read it into the model.

- Always redirect `recents` output to a file.
- Always match fragments against that file in a **subprocess** (a short Python/grep script).
- Only the final result line (a single session row) enters the conversation.

This is what makes the skill cheap: a wide candidate set is reduced to one row without the set ever touching context.

## Skill.Arg.Section

### Skill.Arg::Provider
- narrow the candidate set to the caller's own provider family (e.g. `claude-code`, `codex`, `copilot-cli`)
- the running agent usually knows its provider; setting it is cheaper and avoids cross-provider collisions
- required: false
- help: "restrict the search to one provider family"
- examples: --provider claude-code

### Skill.Arg::Days
- look-back window in days for the recently-active candidate set
- keep small; the caller's own session is by definition among the most recently active
- required: false
- default: 1
- help: "recents look-back window in days"
- examples: --days 1

### Skill.Arg::Last.Turns
- how many trailing user turns per candidate to materialize for matching
- raise it only when shallow turns do not disambiguate (escalation)
- required: false
- default: 6
- help: "trailing user turns per candidate to match against"
- examples: --last-turns 6

## Why This Works (Constraints)

- **Materialization gap.** `agentos chatlas recents`/`query` read Chatlas's *ingested* copy, not the live provider transcript. There is always a lag between the provider writing a turn and Chatlas ingesting it. The lookup only sees what is ingested, so the skill **must** run an update before pulling recents.
- **Bounded search.** The caller just wrote a turn, so its session is among the most recently active. `recents` (newest-first, small window) bounds the candidate set to a handful — never the full index sweep.
- **Self-grounding fragments.** The safest fragments are the caller's own verbatim USER turns: the agent holds them exactly, they are already persisted (no flush race), and distinctive tokens (rare words, identifiers, typos) collide with almost nothing.

## Workflow

### Step 1: Choose self-fragments

From the caller's **own** recent USER turns, pick distinctive verbatim fragments — prefer rare words, identifiers, paths, or unusual phrasings over common ones. One strong fragment often suffices; collect several for ANDing.

- Use exact substrings as they appear in the user's turns.
- Prefer fragments from **later** turns of the conversation: forked or continued sessions share early turns, so late content disambiguates a fork from its parent.
- If this is the very first turn (nothing of the caller is materialized yet), the skill cannot self-locate — report that and stop.

### Step 2: Pull fresh recents to a file (never into context)

`recents --update` closes the materialization gap and pulls the candidate set in one call: it refreshes the recently-active sessions of the scoped provider before reading, so the just-written turns are ingested. Redirect to a file — the payload must never enter the model.

```bash
agentos chatlas recents --provider <provider> --days <days> --last-turns <last-turns> \
  --full --json --limit 15 --update 2>/dev/null > /tmp/chatlas-recents.json
```

- `--update` runs the tiered refresh scoped by `--provider`/`--days` (a recent-window scan), not the full sweep — fast, and it is what makes the freshly-written turns visible.
- Omit `--provider` only if the caller's provider is unknown.

### Step 3: Local fragment-match in a subprocess

Count candidates whose materialized user turns contain **all** chosen fragments (case-insensitive). Surface only the outcome:

```bash
python3 - <<'PY'
import json
frags = ["<fragment-1>", "<fragment-2>"]   # caller's own verbatim user-turn fragments
d = json.load(open("/tmp/chatlas-recents.json"))
matches = []
for e in d.get("entries", []):
    blob = " ␟ ".join(e.get("last_user_turns", [])).lower()
    if all(f.lower() in blob for f in frags):
        matches.append(e)
if len(matches) == 1:
    m = matches[0]
    print("SESSION", m["session_id"], m["provider"], m.get("identity_hash"), m.get("last_activity_at"))
else:
    print("AMBIGUOUS" if matches else "NONE", "candidates=", len(matches), "of", d.get("entry_count"))
PY
```

Resolve by the count:

- **Exactly 1** → that row is the caller. Go to Step 4.
- **More than 1** → escalate: add more / rarer fragments, or raise `--last-turns`, and re-match. Repeat until exactly one survives.
- **0** → the caller's turns are not yet materialized or fall outside the window: re-run the update, widen `--days`/`--last-turns`, and retry once. If still zero and this is an early turn, report that the session cannot be self-located yet.

### Step 4: Return the identity

Return a single small object:

```text
session_id:      <native provider session id>
identity_hash:   <neutral Chatlas identity>
provider:        <provider family>
last_activity_at: <iso timestamp>
```

- `session_id` is the provider-native id; `identity_hash` is the neutral Chatlas identity. Both come straight from the matched `recents` row.
- If the caller also needs the `agentos://chat-session/...` URI, resolve it with a single `agentos chatlas query` filtered by that `session_id` — do not pull it by default.

## Direct-Read Fast Path (optional)

When the provider exposes its native session id cheaply (an env var, the cwd, or a known session-file path), read it directly and skip the probe entirely — then optionally confirm against Chatlas with one `agentos chatlas query` by that id. The fragment workflow above is the universal fallback that works on every provider, including those that expose nothing.

## Failure Shapes

- **First turn / nothing materialized:** "Cannot self-locate yet — no materialized turns for this session. Retry after at least one user turn is ingested."
- **Persistent ambiguity:** return the surviving candidate rows (session_id + provider + last_user_turns) and ask the caller for a more distinctive fragment, rather than guessing.

## Notes

- Keep the `recents` payload out of the model at all times; the subprocess match is mandatory, not optional.
- Fragments are matched case-insensitively as substrings, mirroring `agentos chatlas query --user-contains` (repeating which is the equivalent built-in AND-escalation if a query-based path is preferred over local match).
- This skill reads the caller's own ingested turns only; it does not broaden into unrelated session content.
