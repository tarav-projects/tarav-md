# Skw Generalization - design-session

## Session.Abstract

- **Scope**: generalize skw beyond skills — an embedded annotation language for agentic production and maintenance of any surface: language vs backends, annotated surfaces (code first), annotation points, the authority model, POI semantics, satellite indexes.
- **Source**: session 2026-07-11 (this conversation), continuing the Skillware v1/v2/labels thread (Impl.Reqs 584–588); prior art: 107 `Agentos.Skillware` namespace as recast 2026-07-10/11 (`^c20260710-4u`, `^c20260711-0u`, `^c20260711-1u`).
- **Status**: converged and landed — all 8 blocks reviewed, approved, and landed on the real index (2026-07-11, anchors `^c20260711-2u..-9`); implementation pending an Impl.Req.
- **Resolved in-session**: the language name — **skw** names the language and the system; backends are `skw-<surface>` (was a parked `Experience.Gated.Decision`; gate opened by design pressure).

## Design.Index

### Skw.Language

- [DF] skw is an embedded annotation language for the generation of surfaces — an annotation states how a span of content is produced: from which dependencies, under which rule
- the annotation constrains the span: the content must not contradict or drift from its declaration — every annotation is a checkable claim
- everything frames as generation: a copy is deterministic generation (the inlining of a source, itself possibly generated); a derived span is agentic generation under its rule; a literal carries no generation claim; a link's text is a typed generated span, annotated independently of the target it points at
- it annotates any content, but earns most on agent-generated surfaces — where the rule and its current solution living side by side is what makes maintenance checkable
- it is embedded — skw lives inside the host surface's own format, next to the content it governs, and never replaces it
- the language is surface-blind; a `Skw.Backend` binds it to each surface class

### Skw.Backend

- [DF] a `Skw.Backend` binds `Skw.Language` to one surface class, named `skw-<surface>`
- a backend owns four things: the carrier syntax, the build semantics (if any), where check state lives, and its host-native `Annotation.Point` vocabulary
- every backend is annotated; some backends additionally build — annotation + check is the universal layer, build is backend-local
- a building backend generates its runnable form from annotated src and strips the machinery; an annotated-only backend keeps declarations in place on the surface itself, trading surface cleanliness for constraint co-location
- **skw-skills** is the first backend, a building one: annotated src compiles to the skill's runnable files
- **skw-code** is the first annotated-only candidate: declarations ride the host language's comments; the body is the live fragment

#### meta

- index follow-ups at landing: scope `Module.Import` ^c20260709-13u ("declarations live on the `Skill.Build.Surface`") and `Skill.Runnable.Surface` ^c20260627-2u ("kept free of non-runnable artifacts") to building backends; add one containment line relating skw to `Agentos.Skillware`

### Surface.Annotation

- [DF] a `Surface.Annotation` is the skw content of a file — the machinery that states extra things *about* the surface it annotates, next to the content it governs
- it is a deliberate subset: the fragment's fundamentals, never an exhaustive dependency capture
- it answers one question: *what context can't I miss to understand this fragment?*
- it is a satellite index of the design — a leaf citing the canonical index by `Dotted.Name`; the hub stays the center
- it is a local grounding recipe: an agent landing on the fragment loads the declared dependencies and holds the minimal sufficient context by declaration, not by search

#### appendix

- the declaration is documentation that cannot silently rot — the checker watches its targets; understanding and maintenance are the same feature
- two constraint tiers price differently: the declared tier (fragment vs annotation) is the continuously watched inner loop; the ambient tier (fragment vs the whole index and chat) holds as always via rarer agentic sweeps — annotations watch the hot subset, they do not replace the global obligation
- annotation scope is editorial — the author regulates each annotation's size; granularity policy (block-hash vs line-level deps) is a parked `Experience.Gated.Decision`
- `Natural.Placement` circulates content both ways: notes accrete at annotations (the lowest-friction surface nearest the work); what proves general or touched promotes inward to the index, `Cited.Duplication` back out — the index keeps its value as the bag of all curated touched data

#### meta

- rename to `Skw.Annotation` available at landing for cluster prefix consistency

### Annotation.Point

- [DF] an `Annotation.Point` is a named, sanctioned place where annotations attach — a small vocabulary of points so agents do not over-annotate arbitrary fragments
- points come in two families: **host-native** — the natural divisions of the annotated surface — and **skw-native** — the language's own scoping constructs, layered on top
- [PR] prefer the host's natural divisions; reach for skw-native scoping only where the host's divisions do not fit the annotation's true scope
- the file is the universal host point; each backend declares the rest of its host vocabulary — functions, modules, namespaces for code; sections for markdown
- the skw-native points: the **annotation section** (a leveled, end-free divider sectioning a file for annotation purposes only) and the **span** (an explicit construct body — the finest grain)
- the agent attaches at the coarsest point that honestly fits

#### appendix

- host-native examples: skw-md annotates markdown sections; skw-code annotates functions, classes, modules; every backend has the file
- annotation sections add no content of their own — they exist to give annotations something to scope, and matter most where host divisions are coarse or absent
- end-free sections are a deliberate carve-out from strict owned-end closure: dividers have no body whose extent needs proving — heading-closure semantics apply to them and only them
- landing follow-up: scope the `Skillware.Construct` "closure is fully explicit" line to body-bearing constructs
- the point vocabulary is expected to grow with usage (`Specified.By.Precedence` — the built backends become the soft spec for the next)

### Touched.Authority

- [DF] `Touched.Authority` is the rule that content's authority flows from its grounding, not from its writer — agent-written material carries whatever its evidence supports
- the gradient: **untouched** — agent-generated, user-untouched, no grounding: zero authority of its own, rewritable only within `Open.Space` — the complement of the span of grounded constraints, never against them; **grounded** — linked to a `User.Turn`: second-order authority through the link, and rewriting must answer to that evidence; **`User.Turn`** — the grounding itself: the user's touch, first-order authority
- lower tiers are bound by the span of the higher ones: untouched content moves in what grounded statements leave open; grounded content moves in what its `User.Turn`s leave open
- linkability fences by surface, not by gradient: stable surfaces link only into touched surfaces — grounded content on an untouched surface may be authoritative yet stays unlinkable-into
- no authority status is stored — authority is read from provenance on the surface: types, anchors, the gate trail

#### appendix

- it generalizes the `Index.Agendix` rule already in force: the agendix's "zero authority" was always shorthand for "ungrounded" — its well-anchored lines carried second-order authority all along
- the index itself sits at "grounded": agent-drafted lines anchored to approval turns — only the `Chat.Surface` holds `User.Turn`-grade data (`Context.Grounding`: the index is an index of it)
- instances: agendix lines, `Surface.Annotation`s, index lines, any agent-runs-ahead surface
- second-order authority is what makes the agent's run-ahead useful rather than merely tolerated: grounded hypotheses accumulate real weight before any gate opens

#### meta

- general hugentic concept — natural landing is beside `Touched.Space`/`Grounding.Hugentic.Authority`, not the skw cluster
- landing follow-up: soften `Index.Agendix`'s "zero authority" lines with a cite to this block

### Annotation.Authority

- [DF] `Annotation.Authority` is the authority model of annotations: authority flows from grounding, not from the writer
- annotation lines take the index's own forms: `Line.Type` codes and `Anchory.Anchor`s, with the same validation points
- authority follows `Touched.Authority`: untouched annotation lines are hypotheses bound by the grounded span; grounded ones hold second-order authority; gated ones are first-order touched
- what stays restricted below the gate is linkability, not worth — the `Touched.Authority` fence
- no status is stored: drift is discovered and surfaced by the checker; authority is read from the lines' provenance
- [CT] agent-free insertion is regulated: only the file `Annotation.Point` is open to ungated agentic annotation — every finer point lands user-gated
- finer annotations are therefore born touched: the gating turn is their grounding evidence

#### appendix

- the model is the `Index.Agendix` pattern transplanted twice over: grounding-borne authority with a linkability fence, and a primed insertion surface — the agendix primes by concept set, annotations prime by point coarseness
- a `Capture.Offer` is the gate's natural form: the agent drafts the finer annotation while implementing, offers it, and the approval turn both lands and grounds it
- touched-and-relevant annotation content also promotes into the index, with `Cited.Duplication` back out (circulation owned by `Surface.Annotation`)
- the checker reports by provenance: a POI on grounded or gated content is the loud alarm; on the agent's own untouched file notes, quiet maintenance
- widening the agent-free point vocabulary is a parked `Experience.Gated.Decision` — file-only until usage argues otherwise

### Drift.POI

- [DF] a `Drift.POI` is a point of interest raised by the CPU checker: a span's declared dependencies changed — that, and nothing more
- the CPU never rules on drift: whether the surface actually drifted is an agent's finding — the agent is always the fixer and supervisor
- a POI carries its trigger — which dependency, what changed — so the responding agent starts contextualized
- resolution is agentic: real drift → re-derive the span; benign change → re-bless the dependencies

#### appendix

- the economics: the CPU stands watch continuously and agents deploy on alarm rather than on schedule — staling and contradiction become both more visible and cheaper to police
- the verification gradient: test suites (CPU, behavioral verdicts) → skw checker (CPU, POIs over declared semantic dependencies) → ambient agentic sweeps (global non-contradiction with index and chat); each cheap layer triggers the costlier one
- annotations give the checker what tests structurally cannot see: semantic design/impl drift
- reporting weighs provenance (`Touched.Authority`): a POI on grounded content is the loud alarm; a POI on the agent's own untouched notes is quiet maintenance
- implementation follow-up: the shipped checker's `derived-stale` is verdict-flavored naming for what is a POI — rename when the annotated backend lands
- the DF is deliberately narrow (dependency-change POIs only); other checker outputs remain findings — generalize under evidence

### Experience.Gated.Decision

- [DF] `Experience.Gated.Decision` is a design decision deliberately parked until usage experience accumulates — the question is sound, but answering it now would be a mistake
- the failure it prevents is double: deciding early locks in a guess; leaving the question unnamed loses it
- identification is the work: mark the topic explicitly on a durable surface so the system carries the open question forward without answering it
- the gate opens on evidence — real usage, felt friction, accumulated instances — and the decision is then made from experience, not speculation
- sibling of `Specified.By.Precedence`: both defer authored contracts to accumulated reality; precedence defers the spec, this defers the decision

#### appendix

- the gate may also open by design pressure: a later design session can force the question and supply the answer — parking never forbids answering when the answer genuinely arrives
- lifecycle example: the skw language's name was parked, then resolved within a day by the generalization session itself (skw, backends as `skw-<surface>`)
- currently parked under it: annotation dep granularity (block-hash vs line-level ids; trailing anchors a candidate), and widening the agent-free `Annotation.Point` vocabulary beyond the file

#### meta

- destined for the real index (107, beside `Specified.By.Precedence`)

## Session.Notes

- **landing follow-ups accumulated** (index edits riding the cluster's landing, all gated): scope `Skillware.Construct` "closure is fully explicit" to body-bearing constructs; scope `Module.Import` ^c20260709-13u and `Skill.Runnable.Surface` ^c20260627-2u to building backends; one containment line skw ← `Agentos.Skillware`; soften `Index.Agendix` "zero authority" with a `Touched.Authority` cite
- **code-backend lock location**: project-level sidecar (lean) vs hashes embedded in annotations — undecided
- **checker vocabulary rename**: `derived-stale` → POI-flavored; decide with the annotated-backend Impl.Req
- **carrier syntax per host**: comment-prefix tolerance (`#`, `//`, `--`, `<!-- -->`); ends and labels inside docstrings vs line comments
- **promotion mechanics**: how an annotation line's approval anchor is minted/recorded; whether index promotion auto-marks the annotation as `Cited.Duplication`
- **does `derived` on code ever imply build?**: out of scope; annotated backend is check-only until experience argues otherwise
- **index self-annotation** (skw-index): `Cited.Duplication` lines as derived-span declarations — proven in principle by index2's `edit#Block Independence` recipe; sequencing open
- **implementation ripples**: CLI `agentos skillware` vs `agentos skw`; the `agentos-skillware` skill's name/scope under the new split
- **annotation-point syntax**: `file` and leveled `section` commands sketched, not normative

## Session.Log

- 2026-07-11 — session opened in artifact mode; Design.Index initialized from the in-chat convergence (six draft blocks).
- 2026-07-11 — index landing (`--edit`, user-gated): 7 blocks into 107 (skw cluster after `Skillware.Recipe`; `Experience.Gated.Decision` after `Specified.By.Precedence`), `Touched.Authority` into 106 after `Open.Space`; six appendix files; per-block approval anchors `^c20260711-2u..-8`, scoping edits + containment line under `^c20260711-9u` (`Skillware.Construct` closure, `Module.Import`, `Skill.Runnable.Surface`, `Index.Agendix` softening, `Agentos.Skillware` ← skw); routers updated; the landing tripped two `Drift.POI`s in agentos-skillware (`SKILL#What Skillware Is`, `doctrine#The Model`) — re-derived, rebuilt, all-ok; linter clean.
- 2026-07-11 — block-by-block review, all 8 approved: `Skw.Language` reframed around generation annotation (etymology and construct cites dropped); `Skw.Backend` split out of it, naming resolved (skw / `skw-<surface>`), gained host-point ownership; `Annotated.Surface` dissolved into `Skw.Backend` + `Surface.Annotation`; `Surface.Annotation` refounded as "the skw content of a file", fundamentals/appendix split; `Annotation.Point` added mid-review (host-native vs skw-native families, end-free sections, coarsest-fit); `Touched.Authority` extracted as a general hugentic concept (untouched < grounded < `User.Turn`, Open.Space-bounded rewritability, surface-fenced linkability); `Annotation.Authority` slimmed onto it, agent-free insertion regulated to the file point; `Drift.POI` narrowed to dependency-change POIs; `Experience.Gated.Decision` gained its lifecycle example.
