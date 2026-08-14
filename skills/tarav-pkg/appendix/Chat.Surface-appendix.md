****

## Chat.Surface/Appendix

- `Projects.Chats` is the chat set attributed to a project — its own sessions plus its ancestors': for `A/B/C`, the union of `A/B/C`, `A/B`, `A` (walk the path via `chatlas query --project`, one query per level — match is exact, no prefix)
- `Chat.Retrieval` is the user-triggered "where did we last discuss X", over `Projects.Chats`, cheapest-path-first:
  - tier 1 index — digested → a named block (cache hit)
  - tier 1.5 agendix — agent-cached grounded lines pointing into the chats (`Index.Agendix`)
  - tier 2 git-anchored — `git log` on touched files → date range → `chatlas query --active-after` → sessions (precise, cheap)
  - tier 3 direct — `chatlas query --user-contains` / `chatlas recents` over the turns (broad, complete)
  - read a hit via Chatlas views: `summary` as the cheap filter, `zip-transcript` as the trusted raw turns (`We.Distrust.Summaries`)
- two situations: chat-only work (worst case, but the data is there) vs work with file consequences (best — git bridges files→sessions)
- digestion gradient (extends the `Block.Line.Gradient` capture axis): index block → appendix line (`Index.Edit.Append.Line`) → agendix line (ungated, grounded) → chat-in-place, retrieved on demand (the zero-digestion floor)
- firing is user-triggered by default; the trigger mechanism is secondary to the retrieval design
- open: `chatlas query --active-after` is a lower bound only; a true date range needs an upper bound (client-side trim or an `--active-before`)
- [DC] `Chat.Retrieval` composes Chatlas `query`/`recents`/`views` with Git history ^c20260806-18u
