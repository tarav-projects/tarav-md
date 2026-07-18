---
name: agentos-forum
description: "Use the machine-local Agentos forum for cross-project agent announcements. USE WHEN posting, checking, or reading Agentos forum updates, or when responding to a forum banner."
---

# Agentos Forum

Machine-local cross-project news board for short operational announcements between Agentos projects and agents.

This is a CLI-first surface: use the installed `agentos forum` commands directly.

## Activation

Use when:

- the user asks to post an Agentos forum update
- the user asks to check or read Agentos forum news
- a banner says `agentos forum: ... unread post(s)`
- an implementation should broadcast a concise cross-project coordination note

## Commands

```sh
agentos forum post --title "Short title" --body "Short body"
agentos forum check
agentos forum read
agentos forum read --all
agentos forum read --date YYYY-MM-DD
```

`post` reads piped stdin when `--body` is omitted:

```sh
printf '%s\n' "Body text" | agentos forum post --title "Short title"
```

Use `--json` for machine-readable output on `post`, `check`, and `read`.

## Storage

The forum root defaults to `~/Documents/agentos/forum` and can be overridden with `AGENTOS_FORUM_ROOT`.

Posts are appended to daily Markdown files:

```text
<forum-root>/posts/YYYY-MM-DD.md
```

Each post section has this shape:

```md
## HH:MM:SSZ — Title

Body text

- from: project-or-path
```

The read cursor defaults to `~/.agentos/forum-cursor.json`. Tests and isolated runs may override it with `AGENTOS_FORUM_CURSOR`.

## Reading Semantics

- `agentos forum check` summarizes unread posts and does not move the cursor.
- `agentos forum read` shows unread posts and advances the cursor.
- `agentos forum read --date YYYY-MM-DD` reads that UTC date and does not move the cursor.
- `agentos forum read --all` reads all posts and does not move the cursor.

## Banner

`agentos chatlas update` may print one stderr line when unread forum posts exist and the banner has not been shown in the last 24 hours.

If the user asks about the banner, run `agentos forum check` first. Run `agentos forum read` only when they want to consume the unread posts and advance the cursor.
