---
name: tarav-chatlas-my-session-id
description: Discover the current agent's OWN native session id ("which session am I in?") through a provider-specific direct reader when available, otherwise through bounded Chatlas2 Session.Query and Chat.Query matching over the agent's own verbatim user turns. Returns the native session id plus the neutral Chatlas identity when resolvable. USE WHEN an agent needs to know which provider session it is running inside. Called like a terminal command — runs with no required args; optional `--provider` selects the provider path and narrows fallback search.
---

# Chatlas My Session Id

Operational `Package.Aux.Skill` under `tarav-chatlas-pkg`.

Answer the question "which session am I in?" for the running agent. Resolve through the current provider's cheapest trustworthy path first. Some harnesses expose the native session id directly to tool processes; when they do, use it. Otherwise use Chatlas2 to select a bounded recent session set and match distinctive fragments of the caller's **own** verbatim user turns until exactly one session remains.

The provider-specific paths resolve provider-native identity. Chatlas2 Session.Query is the authority for the neutral `identity_hash`; Chat.Query supplies message evidence for fallback disambiguation. The first Chatlas2 read uses `--update` once so the archive and Session.Index see the current provider delta. Never use Chatlas1 query, recents, views, or content filters in this workflow.

This is a `Batchy.Skill` — called like a terminal command. Load `tarav-batchy-skills` for the full convention.

- `-h` / `--help` prints the help into the chat instead of running (`Batchy.Skill.Help`).
- runs with no required arguments; a bare provider name resolves to `--provider`.

## Execution Mode

Run this skill **inline in the caller context** — do not spawn a separate agent. This is the opposite default from sibling Chatlas skills (`chatlas-session-continue`, `chatlas-session-zip-transcript`), and deliberately so:

- A direct provider reader must execute inside the caller's harness-managed tool environment. A spawned agent has a different session identity.
- Fallback match fragments must come from the caller's **own** verbatim user turns. Only the caller can see its own conversation; a spawned agent cannot supply them.
- The multi-session Chat.Query payload is kept out of the model by matching it in a **subprocess** and surfacing only the result. Agent isolation would buy nothing.

## Token Discipline

The direct provider path is tiny. A fallback Chat.Query payload can still be large. Never read it into the model.

- Always redirect Session.Query and Chat.Query JSON to files.
- Always intersect fragment matches in a **subprocess** (a short Python script).
- Only the final result line (a single session row) enters the conversation.

This is what makes the skill cheap: a bounded candidate set is reduced to one row without the set ever touching context.

## Skill.Arg.Section

### Skill.Arg::Provider
- narrow the candidate set to the caller's own provider family (currently `claude-code` or `codex` for Chatlas2 lookup)
- the running agent usually knows its provider; setting it is cheaper and avoids cross-provider collisions
- required: false
- help: "restrict the search to one provider family"
- examples: --provider claude-code

### Skill.Arg::Since
- look-back window for the recently-active candidate set
- keep small; the caller's own session is by definition among the most recently active
- required: false
- default: 1d
- help: "recent-session look-back window as a duration"
- examples: --since 1d

## Resolution Paths

### Provider Path Router

Use the explicitly configured provider when supplied. Otherwise use the provider family of the running harness when known. Environment-variable presence is only a last local hint; do not let a variable inherited from a parent harness override known caller identity.

| Provider | Direct reader | Path |
|---|---|---|
| `codex` | `CODEX_THREAD_ID` | Read the non-empty value from the caller's tool environment |
| `claude-code` | `CLAUDE_CODE_SESSION_ID` | Read it when exposed by that Claude Code build/environment; otherwise fallback |
| `copilot-cli` | none verified | Chatlas2 lookup unavailable |
| `gemini-cli` | none verified | Chatlas2 lookup unavailable |
| `opencode` | none verified | Chatlas2 lookup unavailable |
| `pi` | none verified | Chatlas2 lookup unavailable |
| `openclaw` | none verified | Chatlas2 lookup unavailable |

The table is an explicit provider router, not permission to guess. Add another direct reader only after verifying that the harness places the current native session id in the agent's tool environment. A session id supplied only to lifecycle-hook commands is not directly readable by an arbitrary later tool call unless an Agentos hook integration deliberately carries it forward.

Never infer the current session from the newest transcript file, process recency, cwd alone, a remote-session id, or a parent-session id. Those signals are unsafe under concurrent, nested, resumed, or forked sessions.

### General Chatlas2 Fallback

The fallback works for the provider families Chatlas2 currently normalizes: Codex and Claude Code. For another provider, return `CHATLAS2_PROVIDER_UNSUPPORTED` rather than invoking Chatlas1.

- **One freshness boundary.** The first lookup uses `tarav chatlas --update ...`. The update refreshes supported provider artifacts and Session.Index once; subsequent fragment queries reuse that stable snapshot.
- **Bounded search.** The caller just wrote a turn, so its session is among the most recently active. Session.Query (newest-first, small time window) bounds the candidate set before message content is read.
- **Self-grounding fragments.** The safest fragments are the caller's own verbatim USER turns: the agent holds them exactly, they are already persisted (no flush race), and distinctive tokens (rare words, identifiers, typos) collide with almost nothing.
- **Authoritative matching.** Chat.Query returns only decoded, verified `Chat.Message` records from the current Chatlas2 Normal Model cache. Candidate scans never establish a match.

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

### Step 3: Select recent sessions to a file (never into context)

Compute the `--since` cutoff as an ISO timestamp, then ask Session.Query for a newest-first bounded candidate set. Redirect the payload; it must never enter the model.

```bash
tarav chatlas --update sessions query --provider <provider> --active-after <cutoff> \
  --sort newest --limit 15 --json > /tmp/chatlas2-self-sessions.json
```

- Use a short local Python calculation for duration-to-cutoff conversion; do not depend on platform-specific `date` flags.
- Omit `--provider` only if the caller's provider is unknown.
- If no sessions are returned, report that Chatlas2 could not discover the current supported session after its update. Do not fall back to Chatlas1.

### Step 4: Query each fragment and intersect locally

For each fragment, run the same bounded Chat.Query and redirect its JSON. Then intersect the message results by neutral session identity in a subprocess. Surface only the outcome:

```bash
tarav chatlas chat query --provider <provider> --active-after <cutoff> \
  --side user --contains '<fragment>' --session-limit 15 --limit 1000 --json \
  > /tmp/chatlas2-self-fragment-1.json

python3 - <<'PY'
import json
sessions = json.load(open("/tmp/chatlas2-self-sessions.json"))["sessions"]
rows = {row["identity_hash"]: row for row in sessions}
paths = ["/tmp/chatlas2-self-fragment-1.json", "/tmp/chatlas2-self-fragment-2.json"]
matched = None
for path in paths:
    payload = json.load(open(path))
    identities = {item["session"]["identity_hash"] for item in payload["messages"]}
    matched = identities if matched is None else matched & identities
matches = [rows[identity] for identity in sorted(matched or ()) if identity in rows]
if len(matches) == 1:
    m = matches[0]
    print("SESSION", m["session_id"], m["provider"], m["identity_hash"], m.get("last_activity_at"))
else:
    print("AMBIGUOUS" if matches else "NONE", "candidates=", len(matches), "of", len(rows))
PY
```

Resolve by the count:

- **Exactly 1** → that row is the caller. Go to Step 5.
- **More than 1** → escalate: add a rarer later fragment and re-intersect. Repeat until exactly one survives.
- **0** → the caller's turns are not archived or fall outside the window: widen `--since` and retry once. If still zero, report that Chatlas2 cannot self-locate this session yet.

### Step 5: Enrich and return the identity

When the Step 3–4 fallback resolved one row, return that row directly; it already carries the neutral identity from the updated Session.Query snapshot.

When a direct provider reader resolved `session_id`, ask Chatlas2 Session.Query for its neutral identity with one exact, provider-scoped query. This is the direct path's single update:

```bash
tarav chatlas --update sessions query --provider <provider> --session-id <session-id> \
  --limit 2 --json
```

- Exactly one row supplies `identity_hash`, `last_activity_at`, and the canonical provider family.
- Zero rows do not invalidate the provider-native result. Return `session_id` and `provider`, with Chatlas2 fields reported as unavailable.
- More than one row means the native id is not unique across configured provider instances. Use the Step 2–4 Chat.Query fallback, additionally constrained by `--session-id`, to resolve the current Chatlas identity; never choose one arbitrarily.

Return a single small object:

```text
session_id:      <native provider session id>
identity_hash:   <neutral Chatlas identity>
provider:        <provider family>
last_activity_at: <iso timestamp>
```

- `session_id` is the provider-native id. It may come from the direct provider reader or the matched Chatlas row.
- `identity_hash` is the neutral Chatlas identity and always comes from Chatlas2 Session.Query. It may be unavailable briefly even when direct native resolution succeeded.
- If the caller also needs the `agentos://chat-session/...` URI, read it from the same Session.Query row — do not pull it by default.

## Failure Shapes

- **First turn / nothing discoverable:** "Cannot self-locate yet — the current supported session was not discoverable after one Chatlas2 update. Retry after at least one user turn exists."
- **Persistent ambiguity:** return the surviving candidate rows (`session_id`, provider, and `identity_hash`) and ask the caller for a more distinctive fragment, rather than guessing.
- **Unsupported provider:** return `CHATLAS2_PROVIDER_UNSUPPORTED` with any directly resolved native `session_id`; never cross into Chatlas1.
- **Direct native id, Chatlas2 archive not ready:** return the native `session_id` and provider, mark `identity_hash` unavailable, and do not downgrade to failure.

## Notes

- Keep every fallback Session.Query and Chat.Query payload out of the model; subprocess intersection is mandatory, not optional.
- `Chat.Query --contains` matches `Chat.Message.text` case-insensitively and verifies every candidate after decode.
- This skill reads the caller's own ingested turns only; it does not broaden into unrelated session content.
- A run of this skill must contain no `tarav chatlas ...` or `agentos chatlas ...` command. Chatlas2 is the complete query dependency.
