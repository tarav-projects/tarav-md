---
name: hugentics-chat-status
description: "Compatibility entry for the current-chat status workflow owned by agentos-hugentics."
---

# Hugentics Chat Status

> $kw: --derived
> --from @<agentos-hugentics>/references/chat-status.skw.md
> --intent preserve the former chat-status entry as a thin compatibility
> --cont projection while the canonical command surface is agentos-hugentics

Resolve this invocation directly to `agentos-hugentics --status`, preserving any report direction supplied by the user. Use the canonical internal module and do not create separate status state or load another workflow skill.

> $kw. end
