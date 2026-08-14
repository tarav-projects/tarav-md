****

## Chatlas.View/Agendix

- [DC] a view is a named normal-model artifact produced from one session, by an agent or by a program ^c20260802-144u
- [DC] `Chatlas.View` is the view system to build; the `Chatlas.View.Model` named-view framework does not survive the rework ^c20260802-138u
- [DC] the MVP is `zip-transcript-summary`: an agent summarizes the chat under a system prompt and returns an artifact that is kept ^c20260802-172u
- [DC] a stale view is warned about, never re-derived automatically — the caller decides whether to redo it ^c20260802-142u
- [CT] freshness stays minimal: the check exists so the warning can fire, not to manage re-production ^c20260802-121u
- [CT] a view operates on exactly one session; the multi-session view generalization is not built ^c20260802-214u
- [DC] views are fixed and hardcoded in Chatlas — no caller-supplied driving prompt enters view identity ^c20260802-215u

****

## Chatlas.View/Agendix/View.Catalog

- [DF] `View.Catalog` is a `views` chapter of the chatlas-pkg index holding one block per registered view, the shape `POI.Catalog` gives `POI.Class` ^c20260802-191u
- [DC] a view's documentation root is its index block, and the Chatlas CLI resolves it through the same Wayfinder mechanism the agentos linter uses ^c20260802-145u
- [PR] indexing the registrations is what makes registering further views cheap later ^c20260802-206u

****

## Chatlas.View/Agendix/Candidate.Chatlas.Product

- [DF] a `Chatlas.Product` is a retained agent production over one named input view, materialized per (product, session) ^c20260803-30u
- [CT] views and products split: a view stays a cheap unmaterialized projection while only a product is retained ^c20260803-31u
- [DC] product freshness compares two fingerprints — the input view payload and the product definition including its producer reference content ^c20260802-216u

****

## Chatlas.View/Agendix/Candidate.Product.Maintenance.Pass

- [DF] `Product.Maintenance.Pass` is a batch route that produces or refreshes one product across every session a query selector returns ^c20260803-32u
- [DC] the default selector takes sessions with more than ten user turns and runs only where the product is missing or stale ^c20260803-33u
- [DC] settled sessions get priority — a session must have been inactive for two days before the pass touches it ^c20260803-34u
- [CT] sessions are independent, so the pass may run them concurrently and reports failures per session instead of aborting the batch ^c20260803-35u
- [CT] the run's agent provider, profile, and model are depot configuration, not flag defaults ^c20260803-36u
- [EX] the configured default run agent is codex / codex-main / gpt-5.6-luna ^c20260803-37u
- [DC] the agent profile is the account handle — one pass binds one provider account and home, and concurrent workers share it ^c20260803-38u
