****

## Normalization.Pipeline::Account.Usage.Model/Agendix

- [DC] the usage registry persists only provider-returned data — estimated limits are computed at monitor refresh time and never reach disk ^20260715-1
- [DC] when a provider drops a limit window (codex burst), the substitution happens at the data layer: a synthesized `Usage.Limit` flowing through the unchanged pipeline, never a parallel rendering path ^20260715-0
- [DC] `AccountLimit` semantics extend to carry estimates — an estimated flag keeps them from being conflated with actual provider data; display prefixes `~` (e.g. `~Burst`) to mark guidance ^20260715-2
- [DC] codex burst-estimate baseline is the nearest registry record at-or-before window start, with no proximity tolerance — a record gap means no monitored activity, so an older baseline stays valid ^20260715-3
- [DC] with no earlier record in the weekly period, the burst estimate shows 0% — "no activity, no usage" ^20260715-2
- [DC] the estimated codex burst window is a fixed-local-5h bucket — a deliberate guidance convention, not a claim about the provider's real (rolling) windows ^20260715-2
- [CT] the burst estimator stays weekly-history based (flat-range deltas → burst % of weekly); improvement iterates in the `dev/burst-detection` testground ^20260715-1
