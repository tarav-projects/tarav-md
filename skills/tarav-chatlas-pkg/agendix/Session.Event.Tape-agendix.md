****

## Session.Event.Tape/Agendix/Chat.File.Edition.POI

- [DF] a `Chat.File.Edition.POI` is an ephemeral, on-demand collection of normalized chat events that may evidence an edition of one file ^c20260726-40u
- [CT] its minimal shape carries a stable POI identity, a file, an optional region, and event references ^c20260726-18u
- [RJ] it does not classify the operation, attribution, confidence, or assessment and does not assert that an edition occurred ^c20260726-47u
- [DC] the first query surface returns all file-edition POIs for one session or only those matching one file; the agent judges the returned evidence ^c20260726-30u
- [CT] file-edition heuristics form an extensible stack in which each detector extracts events that may evidence an edition without changing the POI contract ^c20260726-16u
- [DC] the query surface accepts an optional `--limit` cap so callers can bound evidence output ^c20260726-31u
