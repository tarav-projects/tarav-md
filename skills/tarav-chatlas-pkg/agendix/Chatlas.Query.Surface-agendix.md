****

## Chatlas.Query.Surface/Agendix/Candidate.Event.Pattern

- [DF] an `Event.Pattern` is the provider-independent logical query model for predicates, tape relations, selection, projection, and cardinality over a `Session.Event.Tape` ^c20260725-141u
- [CT] the pattern vocabulary supports compound heuristics such as self-session discovery and an assistant candidate turn followed by its user approval turn ^c20260725-91u
- [CT] `Event.Pattern` defines what the caller asks independently of the backend that accelerates candidate discovery ^c20260725-51u
- [RJ] an `Event.Pattern` does not make a derived query projection authoritative ^c20260725-168u

****

## Chatlas.Query.Surface/Agendix/Candidate.Chatlas.Query.Backend

- [DF] a `Chatlas.Query.Backend` is a candidate-discovery implementation that evaluates an `Event.Pattern` enough to return session and event coordinates ^c20260725-134u
- [CT] backend output contains candidate references, never authoritative event payloads ^c20260725-62u
- [EX] backends may include an authoritative normal-model scan, a disposable SQLite projection, and later specialized indexes ^c20260725-146u
- [CT] every candidate is loaded from the current `Chatlas.Session.Model` and the complete pattern is re-evaluated there before a match is established ^c20260725-70u
- [CT] every public result is projected from the authoritative normal model; a backend row never becomes the output object ^c20260725-71u
- [CT] a backend whose freshness or query-scope coverage cannot be established is refreshed or replaced by an authoritative scan ^c20260725-54u
- [PR] the logical-pattern/backend boundary permits several execution technologies without changing query meaning or output authority ^c20260725-162u
