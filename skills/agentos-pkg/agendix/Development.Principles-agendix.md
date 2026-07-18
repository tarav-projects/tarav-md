****

## Development.Principles/Agendix

- [PR] grow interfaces only on what actual workflows demand — speculative surfaces rejected twice this way (anchory `next`, the general time-softener flag) ^20260708-3

****

## Development.Principles/Agendix/Pwd.Upward.Search

- [DF] `Pwd.Upward.Search` is the discovery pattern: resolve a resource by searching `pwd`, then its parents, and last the registered global depots ^20260717-3
- [PR] the proven filesystem idiom — git finding `.git`, node finding `node_modules`: the common case resolves with zero configuration; registries only cover what the tree cannot reach ^20260717-3 ^20260717-4
- [DC] narrowing hints are routing, not identity: a short namespace prefix narrows the search space; collisions are acceptable — the resolver verifies by lookup and falls through on miss ^20260717-3
- [DC] the registry builds itself from use: any depot a query reaches is recorded — completeness by ratchet, not curation ^20260717-3
- [EX] first application: anchor resolution without prior depot knowledge — `agentos anchory resolve <key>` from anywhere ^20260717-3 ^20260717-4
