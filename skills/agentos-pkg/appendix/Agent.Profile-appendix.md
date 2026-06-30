# Agent.Profile — Appendix

****

## Agent.Profile/Carried.Parameters

- carried parameters span account(s), home(s), model, command and arguments, environment, liveness-ping, and timeout
- a loaded `Agent.Profile` bound to a concrete local environment yields a `Provider.Instance`; an `Agentos.Agent.Adapter` then exposes its capabilities on a provider-uniform surface
- related: `Provider.Instance`, `Provider.Family`, `Agentos.Agent.Adapter`

****

## Agent.Profile/Declaration.Not.Reality

- it is declaration, not reality: it names an intended account and home but does not prove the home exists or that the home's `Auth.Data` matches the named account — that is checked downstream
- it bounds legality, not fitness: it constrains which account and home a run may use; whether the named home and account match reality is a separate evaluation
- related: `Auth.Data`, `Account.Management`
