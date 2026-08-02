****

## Development.Principles/Agendix

- [PR] grow interfaces only on what actual workflows demand — speculative surfaces rejected twice this way (anchory `next`, the general time-softener flag) ^c20260708-3u

****

## Development.Principles/Agendix/Pwd.Upward.Search

- [DF] `Pwd.Upward.Search` is the discovery pattern: resolve a resource by searching `pwd`, then its parents, and last the registered global depots ^c20260717-3u
- [PR] the proven filesystem idiom — git finding `.git`, node finding `node_modules`: the common case resolves with zero configuration; registries only cover what the tree cannot reach ^c20260717-3u ^c20260717-4u
- [DC] narrowing hints are routing, not identity: a short namespace prefix narrows the search space; collisions are acceptable — the resolver verifies by lookup and falls through on miss ^c20260717-3u
- [DC] the registry builds itself from use: any depot a query reaches is recorded — completeness by ratchet, not curation ^c20260717-3u
- [EX] first application: anchor resolution without prior depot knowledge — `agentos anchory resolve <key>` from anywhere ^c20260717-3u ^c20260717-4u

****

## Development.Principles/Agendix/Accuracy.Economics

- [DC] accuracy is an economic decision, not a principled ceiling: 100% would be taken if it were free, but complexity explodes approaching it, so simplicity is traded for error tolerance ^c20260802-11u
- [CT] errors that slip through are accepted as recoverable through their later consequences when they matter ^c20260802-10u
- [CT] revisiting and reblessing as vigilance is a luxury bounded by token budget, while the system is still designed to be capable of it ^c20260802-11u
- [PR] the tooling must be able to do the job while the agent is still trusted to do it ^c20260802-10u
