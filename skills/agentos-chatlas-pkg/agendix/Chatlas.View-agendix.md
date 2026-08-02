****

## Chatlas.View/Agendix

- [DC] a view is a named normal-model artifact produced from one session, by an agent or by a program ^c20260802-5u
- [DC] `Chatlas.View` is the view system to build; the `Chatlas.View.Model` named-view framework does not survive the rework ^c20260802-5u
- [DC] the MVP is `zip-transcript-summary`: an agent summarizes the chat under a system prompt and returns an artifact that is kept ^c20260802-5u
- [DC] a stale view is warned about, never re-derived automatically — the caller decides whether to redo it ^c20260802-5u
- [CT] freshness stays minimal: the check exists so the warning can fire, not to manage re-production ^c20260802-5u

****

## Chatlas.View/Agendix/View.Catalog

- [DF] `View.Catalog` is a `views` chapter of the chatlas-pkg index holding one block per registered view, the shape `POI.Catalog` gives `POI.Class` ^c20260802-5u
- [DC] a view's documentation root is its index block, and the Chatlas CLI resolves it through the same Wayfinder mechanism the agentos linter uses ^c20260802-5u
- [PR] indexing the registrations is what makes registering further views cheap later ^c20260802-5u
