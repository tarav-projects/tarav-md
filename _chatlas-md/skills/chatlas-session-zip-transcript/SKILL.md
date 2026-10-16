---
name: chatlas-session-zip-transcript
description: PARKED legacy Chatlas1 Product workflow. Its retained zip-transcript-summary design is deferred while Chatlas2 continuation matures.
---

# PARKED — Chatlas Session Zip Transcript

This public workflow is retired, not redirected through compatibility plumbing.

Do not invoke Chatlas1 Views or Products and do not produce a `zip-transcript-summary` artifact. For continuation, use `chatlas-session-continue`, which refreshes once and traverses Chatlas2 `Chat.Message` records in bounded pages while preserving every user message verbatim.

Retained summary products remain an open design question in `tarav-chatlas-pkg/issues/100-issues.md`. Mine this workflow's Git history only when that issue is deliberately revisited.
