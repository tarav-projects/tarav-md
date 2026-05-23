---
name: hugentics-chat-status
description: "Operational chat realignment workflow — produce a short or medium reconnect report for the current session."
---

# Hugentics Chat Status

Reconnect the user with the current session state.

This is a lightweight Hugentic realignment surface. It helps recover the main topic, active threads, and likely next move when the user has many chats open or explicitly says they are lost. Keep the report short or medium sized; do not turn it into project diagnosis.

## Activation

Use when the user asks "status", "catch me up", "what are we doing?", "what's next?", "anything left?", "what's missing?", "I'm lost", or similar reconnect requests.

If an explicit Hugentic workflow is active, include which workflow appears active and whether `hugentics-workflow-status` would be the more precise status surface.

## What To Load

- Load `agentos-hugentics/references/chat-status.md` for the full protocol.
