# Chatlas Tagger - design-session

## Session.Abstract

Design a minimal, generic, interactive session-by-session tagger built on top of the chatlas annotations subsystem. The tagger drives human-in-the-loop classification flows: cursor walks sessions newest → oldest, shows session metadata and a short text excerpt, accepts a one-key decision, applies a tag, advances.

First profile: `session-type` (classifies sessions as `hugentic-session` or `agentic-session`). The profile system supports future classification tasks without re-implementing the loop.

A VSCode extension was discussed and rejected for v1 — too much build for a CLI-shaped task. If richer UX is needed later, a localhost web page is the lighter-weight escalation.

## Design.Index

### Tagger.Concept

- Interactive CLI loop: pick the next unreviewed session, display it, read a key, apply the chosen tag, repeat.
- Built on top of the annotations system: each decision is just `add_session_tag(identity_hash, tag)`.
- Generic by virtue of the profile being a tag list; loop logic doesn't know about specific tag meanings.
- Human-in-the-loop is the point. The tagger does not auto-classify.

### Tagger.Profile

- Profile shape (v1, minimum):
  ```json
  { "tags": ["hugentic-session", "agentic-session"] }
  ```
- Everything else is derived or universal:
  - **Unreviewed set**: sessions without any tag from `profile.tags`
  - **Keybindings for tags**: index (`1`, `2`, ...) — sessions get tagged with `tags[i-1]`
  - **Universal navigation keys**: hardcoded (see `Tagger.Keybindings`)
- Profiles deliberately do not carry display config, custom keybindings, or pre-filters in v1. Additive when needed.

### Tagger.Profile.Location

- `~/.agentos/config.json` under `chatlas.taggers.<profile-name>`. Multi-profile in one file. No new file conventions.
- Example:
  ```json
  {
    "chatlas": {
      "taggers": {
        "session-type": { "tags": ["hugentic-session", "agentic-session"] }
      }
    }
  }
  ```

### Tagger.Loop.Iteration

Each iteration:

1. Pick next unreviewed session (newest → oldest, using `agentos chatlas query --sort newest --without-tag <each profile tag>`).
2. Display: basic metadata (provider, project, first/last activity timestamps, turn counts) + `summary.first_user_text_excerpt` from the index row.
3. Read one key from the user.
4. Apply action (tag, advance, etc.).
5. Loop.

If no unreviewed sessions remain: print "all reviewed" and exit.

### Tagger.Display

- **Default screen**: index-row metadata + `summary.first_user_text_excerpt` (one turn, free — already in the index).
- **Escalation on demand**: when the user presses `m` (more), load the full session model and show the next N user turns. Lazy — most decisions are made from the default screen.
- Long turns truncated reasonably; user can request "more" to see full content.

### Tagger.Keybindings

V1 fixed layout:

- `1`, `2`, ... — apply `profile.tags[i-1]` to the current session, advance
- `m` — load and show more user turns from the current session
- `s` — skip this session for now (no tag applied; show again on a later run)
- `b` — back (re-show the previous session; the user can re-decide, overwriting any prior tag from this profile)
- `q` — quit

Tag-keys default to numeric index for simplicity and generality. If a profile defines two-or-three-tag schemes only, this is enough; richer keybinding support is v2.

### Tagger.Back.Navigation

- `b` re-shows the previous session in the iteration order, allowing re-decision.
- Implementation: maintain an in-memory stack of recently visited identity hashes. On `b`, pop and re-display.
- "Re-decide overwrites": when re-classifying, the previous profile-tag is removed and the new one added. At any time, a session carries at most one tag from `profile.tags`.
- Back depth: at least the current session (one level). Multi-level back is nice-to-have.

### Tagger.Resume

- Stateless across runs. Resume = re-run; the iteration naturally picks up at the next unreviewed session because reviewed sessions already carry a profile tag.
- Skipped sessions (no tag applied) come back into the queue on the next run. That's intentional — skip means "decide later".

### Tagger.Unreviewed.Filter

- Requires a `--without-tag TAG` (repeatable) flag on `agentos chatlas query`, parallel to the existing `--tag TAG`.
- Semantics: keep only sessions whose `annotations.tags` does not contain the listed tag (repeat for "without all of these tags").
- "Unreviewed for profile session-type" = `chatlas query --without-tag hugentic-session --without-tag agentic-session`.
- This is a small but real chatlas extension; v1 tagger depends on it.

### Tagger.CLI.Surface

- New subcommand group: `agentos chatlas utils` (general-purpose chatlas utilities).
- Tagger invocation: `agentos chatlas utils tagger --profile <name>`.
- Profile name is required; the tagger reads its tag list from `~/.agentos/config.json`.
- Optional v1 flags: `--limit N` (stop after N decisions), `--provider X` (pre-filter, repeatable).

### Tagger.First.Profile.SessionType

- Profile name: `session-type`
- Tags: `hugentic-session`, `agentic-session`
- "Hugentic" = user-and-agent design or work session (the user provided substantive input, not just kicked off automation)
- "Agentic" = agents only, or highly automated runs

### Tagger.Auto.Tagging

- High-precision auto-classification integrated into the tagger loop. Optimized for **zero false positives**, accepting reduced recall.
- Configured per-tag under `profile.auto.<tag>`. Absence of an `auto` block = no auto-classification for that tag.
- v1 method: `regex`. Method is pluggable for future strategies (canonicalize+hash, structural match, etc.) selected via `method` field.
- Patterns are an array of `{turn, regex}` objects:
  - `turn`: 1-indexed user-turn number to match against. Default 1 if omitted.
  - `regex`: pattern to apply to that turn's full text. Caller is responsible for anchoring (`^...`) when prefix-matching is intended.
  - Multiple patterns are OR'd; first match triggers the auto-tag.
- Loop integration: when iterating, the tagger checks the current session against each auto-tag's patterns; on hit, the tag is applied and the cursor advances silently (no display, no key press).
- Performance: turn-1 matches use the free `summary.first_user_text_excerpt` from the index row. Turn ≥2 matches require loading the session model — accepted slowdown for those patterns.
- Example block (under `profile.auto`):
  ```json
  "auto": {
    "agentic-session": {
      "method": "regex",
      "patterns": [
        {"turn": 1, "regex": "^Use md-library-pkg \\(including references/transcript-spec\\.md\\)"},
        {"turn": 1, "regex": "^Use paperson-pkg"},
        {"turn": 2, "regex": "^Run: iterante execute"}
      ]
    }
  }
  ```

### Tagger.Auto.Validation

- Trust-but-verify mechanic: periodically the tagger **skips** the auto for a sampled session and presents it to the user for blind classification.
- Purpose: detect rule drift / false positives before they compound silently.
- Sampling: `auto_test_rate` (float in `[0, 1]`) per profile, configurable, plus runtime override `--auto-test-rate <r>`.
  - Default profile rate: `0.1` (10% — useful enough to catch errors, doesn't defeat speed gain).
  - When introducing a new rule, crank temporarily to `0.5`+ until trusted, then drop.
- **Blind mode**: when the test fires, the session is shown like a regular interactive tag with no hint of what auto would have chosen. After the user's pick, the system records whether the pick matched the auto's prediction.
- Reporting: end-of-run summary includes `auto_tagged`, `auto_test_count`, `auto_test_agreements`, and a list of `auto_test_disagreements` (identity_hash + tag-auto-would-have-picked + tag-user-picked). Disagreements are the signal to refine the regex.

### Out.Of.Scope

- VSCode extension (parked; web page is the lighter escalation if needed)
- Custom per-profile keybindings (v2 if profiles get diverse)
- Pre-filters in the profile (use CLI flags for now)
- Multi-tag per session per profile (current shape: at most one profile-tag at a time)
- Auto-classification *suggestions* in interactive mode ("auto would pick X; press to confirm"). v1 auto is silent-tag, not suggestion; blind-sample test mode replaces this.
- Tag value validation
- Web/TUI front-ends

## Session.Notes

- The `--without-tag` flag on `agentos chatlas query` is a small but real chatlas extension; its impl-req can be folded into the tagger impl-req or kept separate.
- Display layout (how many lines per session, truncation) is a usability concern best decided once we see real screens.
- "Skip" sessions reappearing every run can become annoying if a session is genuinely undecidable. v2: a `pending-review` tag that suppresses re-asking until explicitly retried.
- The `summary.first_user_text_excerpt` is short (~240 chars). For sessions where one turn isn't enough, the `m` key loads the full session model — fine for occasional escalation; if it becomes the default action, reconsider always-load.

## Session.Log

- 2026-06-01: session opened. Decisions captured: generic-but-simple profile system (`{tags: [...]}`), profile location (`~/.agentos/config.json::chatlas.taggers.<name>`), CLI surface (`agentos chatlas utils tagger --profile <name>`), keybindings (numeric for tags + universal `m`/`s`/`b`/`q`), display (summary excerpt by default, escalate on `m`), resume (stateless, derived from absence of profile tags), back navigation (re-show + re-decide overwriting). First profile defined: `session-type` with `hugentic-session` / `agentic-session`. VSCode extension rejected for v1.
- 2026-06-05: added auto-tagging extension. Integrated into the tagger profile under `auto.<tag>`. v1 method: regex with `{turn, regex}` patterns OR'd. Match field: `summary.first_user_text_excerpt` for turn 1, session-model load for turn ≥2. Trust-but-verify via blind-sample test mode (`auto_test_rate`, default 0.1, runtime overridable). End-of-run reports auto-tag counts and test agreement/disagreement details for rule refinement.
