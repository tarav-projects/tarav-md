---
name: tarav-chatlas-my-session-id
description: Discover the current agent's OWN native session id ("which session am I in?") through a provider-specific direct reader when available, otherwise by refreshing Chatlas and locally matching the agent's own verbatim user turns. Returns the native session id plus the neutral Chatlas identity when resolvable. USE WHEN an agent needs to know which provider session it is running inside. Called like a terminal command — runs with no required args; optional `--provider` selects the provider path and narrows fallback search.
---

# Chatlas My Session Id

Operational `Package.Aux.Skill` under `tarav-chatlas-pkg`.

Answer the question "which session am I in?" for the running agent. Resolve through the current provider's cheapest trustworthy path first. Some harnesses expose the native session id directly to tool processes; when they do, use it. Otherwise refresh Chatlas, pull the recently-active sessions, and match distinctive fragments of the caller's **own** verbatim user turns until exactly one session remains.

The provider-specific paths resolve provider-native identity. Chatlas remains the general fallback and the authority for the neutral `identity_hash`.

This is a `Batchy.Skill` — called like a terminal command. Load `tarav-batchy-skills` for the full convention.

- `-h` / `--help` prints the help into the chat instead of running (`Batchy.Skill.Help`).
- runs with no required arguments; a bare provider name resolves to `--provider`.

## Execution Mode

Run this skill **inline in the caller context** — do not spawn a separate agent. This is the opposite default from sibling Chatlas skills (`chatlas-session-continue`, `chatlas-session-zip-transcript`), and deliberately so:

- A direct provider reader must execute inside the caller's harness-managed tool environment. A spawned agent has a different session identity.
- Fallback match fragments must come from the caller's **own** verbatim user turns. Only the caller can see its own conversation; a spawned agent cannot supply them.
- The expensive payload (the `recents` JSON) is kept out of the model by matching it in a **subprocess** and surfacing only the result. Agent isolation would buy nothing.

## Token Discipline

The direct provider path is tiny. The fallback `recents` payload can be large (tens of thousands of tokens for a wide window). Never read it into the model.

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

### Skill.Arg::Since
- look-back window for the recently-active candidate set
- keep small; the caller's own session is by definition among the most recently active
- required: false
- default: 1d
- help: "recents look-back window as a duration"
- examples: --since 1d

### Skill.Arg::Last.Turns
- how many trailing user turns per candidate to materialize for matching
- raise it only when shallow turns do not disambiguate (escalation)
- required: false
- default: 6
- help: "trailing user turns per candidate to match against"
- examples: --last-turns 6

## Resolution Paths

### Provider Path Router

Use the explicitly configured provider when supplied. Otherwise use the provider family of the running harness when known. Environment-variable presence is only a last local hint; do not let a variable inherited from a parent harness override known caller identity.

| Provider | Direct reader | Path |
|---|---|---|
| `codex` | `CODEX_THREAD_ID` | Read the non-empty value from the caller's tool environment |
| `claude-code` | `CLAUDE_CODE_SESSION_ID` | Read it when exposed by that Claude Code build/environment; otherwise fallback |
| `copilot-cli` | none verified | General Chatlas fallback |
| `gemini-cli` | none verified | General Chatlas fallback |
| `opencode` | none verified | General Chatlas fallback |
| `pi` | none verified | General Chatlas fallback |
| `openclaw` | none verified | General Chatlas fallback |

The table is an explicit provider router, not permission to guess. Add another direct reader only after verifying that the harness places the current native session id in the agent's tool environment. A session id supplied only to lifecycle-hook commands is not directly readable by an arbitrary later tool call unless an Agentos hook integration deliberately carries it forward.

Never infer the current session from the newest transcript file, process recency, cwd alone, a remote-session id, or a parent-session id. Those signals are unsafe under concurrent, nested, resumed, or forked sessions.

### General Chatlas Fallback

The fallback works across all providers:

- **Materialization gap.** `agentos chatlas recents`/`query` read Chatlas's *ingested* copy, not the live provider transcript. There is always a lag between the provider writing a turn and Chatlas ingesting it. The lookup only sees what is ingested, so the skill **must** run an update before pulling recents.
- **Bounded search.** The caller just wrote a turn, so its session is among the most recently active. `recents` (newest-first, small window) bounds the candidate set to a handful — never the full index sweep.
- **Self-grounding fragments.** The safest fragments are the caller's own verbatim USER turns: the agent holds them exactly, they are already persisted (no flush race), and distinctive tokens (rare words, identifiers, typos) collide with almost nothing.

## Workflow

### Step 1: Resolve the provider path

Select the row in `Provider Path Router`. For the two direct readers:

```bash
case "$chatlas_provider" in
  codex) chatlas_native_session_id="${CODEX_THREAD_ID:-}" ;;
  claude-code) chatlas_native_session_id="${CLAUDE_CODE_SESSION_ID:-}" ;;
  *) chatlas_native_session_id="" ;;
esac
```

- Treat an unset or empty value as unavailable and continue to Step 2.
- A non-empty value resolves the native `session_id`; continue to Step 5.
- Do not print the complete environment or probe unrelated variables.

### Step 2: Choose self-fragments

From the caller's **own** recent USER turns, pick distinctive verbatim fragments — prefer rare words, identifiers, paths, or unusual phrasings over common ones. One strong fragment often suffices; collect several for ANDing.

- Use exact substrings as they appear in the user's turns.
- Prefer fragments from **later** turns of the conversation: forked or continued sessions share early turns, so late content disambiguates a fork from its parent.
- If this is the very first turn (nothing of the caller is materialized yet), the skill cannot self-locate — report that and stop.

### Step 3: Pull fresh recents to a file (never into context)

`recents --update` closes the materialization gap and pulls the candidate set in one call: it refreshes the recently-active sessions of the scoped provider before reading, so the just-written turns are ingested. Redirect to a file — the payload must never enter the model.

```bash
agentos chatlas recents --provider <provider> --since <since> --last-turns <last-turns> \
  --full --json --limit 15 --update 2>/dev/null > /tmp/chatlas-recents.json
```

- `--update` runs the tiered refresh scoped by `--provider`/`--since`, escalating only until the read is non-empty. This makes freshly-written turns visible without selecting a separate update path.
- Omit `--provider` only if the caller's provider is unknown.

### Step 4: Local fragment-match in a subprocess

Count candidates whose materialized user turns contain **all** chosen fragments (case-insensitive). Surface only the outcome:

```bash
python3 - <<'PY'
import json
frags = ["<fragment-1>", "<fragment-2>"]   # caller's own verbatim user-turn fragments
d = json.load(open("/tmp/chatlas-recents.json"))
matches = []
for e in d.get("entries", []):
    blob = " ␟ ".join(t.get("text", "") for t in e.get("last_user_turns", [])).lower()
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

- **Exactly 1** → that row is the caller. Go to Step 5.
- **More than 1** → escalate: add more / rarer fragments, or raise `--last-turns`, and re-match. Repeat until exactly one survives.
- **0** → the caller's turns are not yet materialized or fall outside the window: re-run the update, widen `--since`/`--last-turns`, and retry once. If still zero and this is an early turn, report that the session cannot be self-located yet.

### Step 5: Enrich and return the identity

When a direct provider reader resolved `session_id`, ask Chatlas for its neutral identity with one exact, provider-scoped query:

```bash
agentos chatlas query --provider <provider> --session-id <session-id> \
  --limit 2 --update --json
```

- Exactly one row supplies `identity_hash`, `last_activity_at`, and the canonical provider family.
- Zero rows do not invalidate the provider-native result. Return `session_id` and `provider`, with Chatlas fields reported as unavailable.
- More than one row means the native id is not unique across configured provider instances. Use the Step 2–4 fragment fallback, additionally constrained by `--session-id`, to resolve the current Chatlas identity; never choose one arbitrarily.

Return a single small object:

```text
session_id:      <native provider session id>
identity_hash:   <neutral Chatlas identity>
provider:        <provider family>
last_activity_at: <iso timestamp>
```

- `session_id` is the provider-native id. It may come from the direct provider reader or the matched Chatlas row.
- `identity_hash` is the neutral Chatlas identity and always comes from Chatlas. It may be unavailable briefly even when direct native resolution succeeded.
- If the caller also needs the `agentos://chat-session/...` URI, resolve it with a single `agentos chatlas query` filtered by that `session_id` — do not pull it by default.

## Failure Shapes

- **First turn / nothing materialized:** "Cannot self-locate yet — no materialized turns for this session. Retry after at least one user turn is ingested."
- **Persistent ambiguity:** return the surviving candidate rows (session_id + provider + last_user_turns) and ask the caller for a more distinctive fragment, rather than guessing.
- **Direct native id, Chatlas not ready:** return the native `session_id` and provider, mark `identity_hash` unavailable, and do not downgrade to failure.

## Notes

- Keep the fallback `recents` payload out of the model at all times; the subprocess match is mandatory, not optional.
- Fragments are matched case-insensitively as substrings, mirroring `agentos chatlas query --user-contains` (repeating which is the equivalent built-in AND-escalation if a query-based path is preferred over local match).
- This skill reads the caller's own ingested turns only; it does not broaden into unrelated session content.
