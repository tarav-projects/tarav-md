> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Project.File.Index

- `Project.File.Index` is the file-level routing section of the `Index.Router`
- describes the project's file system at folder level, with individual files listed only when fundamental
- one sentence description per entry — token budget is tight, it travels with the router whenever the index is loaded
- gives agents a structural map of where to look — not a complete listing, but the important entry points

****

## Unresolved.Index.Name

- `Unresolved.Index.Name` is an unknown `Dotted.Name` that the agent cannot resolve against the index
- parked in the session — available for later resolution if more context emerges
- if the same name recurs 3+ times, suggest capture to the user
- gap detection is passive — don't interrupt conversation flow

****

## BuiltIn.Namespace

- `BuiltIn.Namespace` is an `Explicit.Namespace` that every Agentos project is expected to have
- it's an interface — can be empty, populated as the project evolves
- examples: `Project.Surfaces`

****

## Project.Index.Skill

- `Project.Index.Skill` is the `<project>-index` auxiliary skill for a package index surface
- the canonical public index content lives in the package skill's `Index.Depot`: `000-INDEX.md`, `design/`, and `appendix/`
- it is a `Package.Aux.Skill` for the package's `Package.Skill.Index`
- the auxiliary skill may provide direct index access, research, writing, diagnosis, testing, maintenance, or index workflow framing without becoming a separate package root

****

## Concept.Cite

- `Concept.Cite` is the bracket notation for citing concept origins or materially important related concepts when inline mention is not natural
- format: `[Concept.X, Concept.Y]`; page or source qualifiers may be added when needed, e.g. `[Concept.X, Concept.Y[1]]`
- used when the citation changes how an agent should interpret, verify, maintain, or navigate the line
- not used merely because another concept is loosely related
- complements `Inline.Relatedness`: prefer natural inline `Dotted.Name` mentions, cite only when the relation matters but does not read naturally

****

## Appendix.Discovery

- `Appendix.Discovery` is the protocol for reaching a concept's depth on demand — the appendix is not routed, it is found by naming
- loading appendix depth is an intentional act — the agent goes deeper by choice, never by default
- if a concept's block is not enough, check `appendix/Concept.X-appendix.md`; the naming convention is the discovery mechanism, no outlink needed
- that file holds the concept's path-children — its `Concept.X/Appendix` dump and any scoped `Concept.X/Concept.Y` blocks
- discovery cascades: a block → its appendix → the blocks there → their own appendixes
- the more blocks loaded, the more paths available — agents discover by following related blocks
- hidden blocks are not deleted — just outside the default scope, reached by following the cascade

****

## Index.Pages

- `Index.Pages` is the file dimension of a concept — the pages its content spans, written `Concept.X[N]`
- `Concept.X[0]` is the index block's file; `Concept.X[1]` is the first appendix file (`Concept.X-appendix.md`); `[2]+` are further files
- `Concept.X[:]` means all of a concept's content across its files (slice semantics)
- the notation is usable as inline reference in blocks, chat, and prompts
- it is orthogonal to `Block.Path` — pages address files, paths address the ontology; one page holds many path-blocks
- by default a path block lands in the matching page, but the two axes need not coincide
- the router annotates page presence inline (`Concept.X[+N]`) — lintable, only when appendix files exist; no annotation means no appendix

### meta

- aliases: `Appendix.Pages`

****

## Placement.Heuristic

- `Placement.Heuristic` is the decision framework for where content lives in the system
- design knowledge (what, why, how it connects) → index block + appendix
- executable instructions (do this, run that, follow this loop) → skill references
- if content drift is detected, report it — don't migrate without user approval

****

## Install.Skill

- `Install.Skill` is a convention where a skill package ships guidance for adopting its support into a project
- lives in the package's `references/` as installation instructions
- can be executed agentically (agent follows the steps) or hugentically (human-agent design loop)
- example: installing the index system creates a local `Index.Depot` at `notes/index/` — `000-INDEX.md` router and chapter files
- example: installing the agentos stack sets up `AGENTS.md`, `notes/`, `skills/`

****

## Index.Empirical.Placement

- `Index.Empirical.Placement` is evidence-driven placement of content across index layers
- complement to `Placement.Heuristic` — design judgment places initially, empirical data optimizes over time
- evidence source: chat sessions across projects, accessed through `Chatlas.Query.Surface`
- the core signal is comparative — content at the same depth level should have similar usage profiles
- the working unit is flexible — a block, a line within a block, or a group of related blocks
- output is a migration plan — proposed moves with evidence, user approves before execution

****

## Alignment.Surface

- `Alignment.Surface` is a surface where humans and agents build shared understanding
- readable by humans (natural language), operable by agents (structured, loadable)
- neither side owns it alone — both contribute, both consume
- the index is the primary `Alignment.Surface` of an Agentos project

****

## Index.Depot

- `Index.Depot` is a self-contained Index instance — its own `000-INDEX.md`, chapters, and appendix
- it follows `Agentos.Index.System` conventions
- [CT] every `Index.Depot` lives under a `Skw.Package` — it is that package's concept-store data structure, addressed by `Dotted.Name` ^c20260724-2u
- [DC] the owning `Skw.Package` may be dedicated to the index or double as a `Package.Skill` — the same enclosing `.skw/`, one package ^c20260724-2u
- [CT] a depot is engaged like any other — no depot privileged ^c20260724-2u
- the same concept name may exist in two engaged depots; the system surfaces the collision, it does not prevent or resolve it
- it loads with its owner through the `Package.Driver` (`Context.Loading.Path`)

### meta

- aliases: `Agentos.Index.Depot`

****

## Index.Depot.Dependency

- [DF] `Index.Depot.Dependency` is the index-addressing case of `Skw.Pkg.Dependency`: a depot resolves a `Dotted.Name` against another package's depot only through a declared dependency — package-visibility in the software sense ^c20260722-15u ^c20260724-3u
- [PR] visibility is non-transitive: a depot's resolution set is its own concepts plus those of its directly declared dependency depots only — a dependency's own dependencies are not visible through it ^c20260722-16u
- [PR] the depot's `Index.Router` also names its dependency depots, so an agent orienting through `000-INDEX.md` sees the depot's upstreams ^c20260722-15u
- [CT] `Index.Depot.Dependency` directs `Index.Discovery`: engaged-depot composition follows the declared edges (own ∪ direct dependencies), not an undeclared flat union ^c20260722-15u
- [CT] a mention resolving against a name defined in more than one visible depot is a collision `Drift.POI`: the linter reports it and never repairs it — consistent with `Index.Depot` surfacing collisions rather than preventing them; the human resolves by namespacing ^c20260722-16u
- [CT] reachability and privilege are orthogonal — an `Index.Depot.Dependency` grants sight of another depot without ranking them, so it does not overturn "no depot privileged" ^c20260722-16u

### meta

- aliases: `Index.Depot.Visibility`

****

## Agent.Profile

- `Agent.Profile` is the meta-configuration for working with a `runnable` agent — it defines the span of configuration that agent is allowed to run under
- it binds a `Provider.Family` to a permitted set of run parameters: which accounts, which homes, plus model, command, and environment
- it is referenced explicitly by name — never inferred
- every running primitive consumes it as the source of permitted *who* and *how*; a primitive selects within the profile's span, it never authors or widens it

### meta

- aliases: `Profile`, `Run.Profile`

****

## Provider.Instance

- `Provider.Instance` is a fully-specified, runnable agent configuration — a `Provider.Family` bound to all the parameters a run needs
- the OOP analogy holds: `Provider.Family` is the class, `Provider.Instance` is its parameters bound
- the bound parameters are the account, the home, the bound `Agent.Profile`, credentials, and any family-specific configuration
- identity is the full binding — the same provider and account on two different homes are two different instances (claude on home A vs home B)

### meta

- aliases: `Agent.Instance`

****

## Linked.Home

- `Linked.Home` is a home that shares selected subcomponents with another home by linking to them instead of owning independent copies
- it combines shared subcomponents with home-local state
- the shared subcomponents remain owned by one home and reused from the others
- it is a partial-home pattern — only some subcomponents are linked, not the whole home

****

## Agentos.Agent.Adapter

- `Agentos.Agent.Adapter` is the agent-domain `Raw.Adapter` — a provider's realization of `Agent.Normal.Model`'s capabilities on a common surface
- concrete adapters are named `<Something>.Agent` — `<Something>` names the capability surface served, not the full instance
- one `Provider.Instance` may carry multiple adapters covering different capability slices

### appendix

- `<Something>` may be provider-shaped, subsystem-shaped, capability-shaped, workflow-shaped, or composed
- examples: `Claude.Runner.Agent`, `Codex.Chatlas.Agent`, `Account.Monitor.Agent`, `Credential.Reconcile.Agent`
- supporting primitives may include `Agent.Profile`, `Provider.Account`, `Provider.Home`, `Provider.Family`, credential artifacts, session references, run requests, and run results

### meta

- aliases: `Something.Agent`, `Agent.Surface`, `Agent.Capability.Object`

****

## Agent.Normal.Model

- `Agent.Normal.Model` is an instantiation of `Normalization.Pipeline` whose `Normal.Model` is a runnable agent — normalized state bundled with the capabilities defined over it
- its `Raw.Adapter` is the `Agentos.Agent.Adapter` — each provider realizes the capabilities from its native operations
- the canonical capabilities are run, ping, profile-check, and account-status — the operations every agent exposes irrespective of provider
- it is scoped to run-time capabilities; account-lifecycle operations are their own `Normal.Model`
- state is shared, not owned — its fields may coincide with `Agent.Profile` and `Provider.Instance` where reuse fits
- the typed signatures — state fields, capability arguments, and result sub-models — are specified in this concept's appendix

****

## Normalization.Pipeline::Account.Usage.Model

- `Normalization.Pipeline::Account.Usage.Model` is the account-usage instantiation of `Normalization.Pipeline` — native provider usage artifacts normalized into `Account.Usage.Status`
- `Normal.Model` = `Account.Usage.Status`, modeled as a list of `Usage.Limit`s
- `Raw.Source`s are native provider usage artifacts (codex `rateLimits`, claude statusline JSON, copilot usage); `Raw.Normalizer`s are per-provider and per-native-variant
- the many-normalizers freedom covers native drift — claude statusline `rate_limits` and the legacy `seven_day` shape are separate `Raw.Normalizer`s, not one branching function
- a `Model.Fragment` is a partial `Account.Usage.Status` — a subset of `Usage.Limit`s; an absent limit is "not carried", never fabricated as empty or zero
- `Normalizer.Context` is provider-scoped — a provider's raw usage artifact loaded once per assembly
- the `Normal.Assembler` merges fragments by `Usage.Limit` identity into a full or partial `Account.Usage.Status`, and owns precedence when fragments carry the same limit

****

## Harness.Injected.ENV

- `Harness.Injected.ENV` is environment state injected by Agentos to enable provider functionality
- it exists because the provider exposes required functionality through environment variables
- it translates explicit Agentos runtime state into the provider's execution mechanism
- it is mechanical provider enablement, not launch policy
- the injected value must be necessary for the requested provider functionality
- provider adapters may know which env variable enables the provider mechanism
- provider adapters must not use harness injection to add behavioral preferences
- command-build tests should allow only named harness env keys when config env is empty

****

## Config.Injected.ENV

- `Config.Injected.ENV` is environment state declared by configuration and injected into provider execution
- it exists because a configuration surface declares environment state for execution
- it carries launch policy
- it is passed through to the provider process as configured
- `Agentos.Agent.Adapter` may transport config env
- `Agentos.Agent.Adapter` must not author config env
- it is distinct from `Harness.Injected.ENV`

****

## Index.Linter

- `Index.Linter` is the deterministic CLI checker for index and appendix surfaces
- [DC] `Index.Linter` is a `POI.Linter` over the index AST ^c20260724-5u
- normal use is depot-first: lint an `Index.Depot` through its `000-INDEX.md`, chapter folders, and appendix
- finding and check codes are scoped concept names under `Index.Linter/...`
- each code names an appendix block that explains meaning, gating, or expected remediation
- agents resolve linter code meaning through normal `agentos-pkg` index and `Appendix.Discovery`
- router entries use `[+N]` to expose discovered appendix page depth for routed concepts
- the linter reports errors, warnings, blocked checks, and summary counts

****

## User.Gate

- [DF] a `User.Gate` is an `Accountable.Assertion` whose claim is about the `Chat.Surface`: evidence of a declared kind can be found in the gated object's dossier ^c20260719-12u ^c20260719-15u
- [DC] one declaration, two systems read it — **flow** (pre-evidence): the declaration shapes agent behavior before any evidence exists — stop, surface the thing, spend `User.Attention`, wait; runtime conversation control, honored in-session; **audit** (post-evidence): the recomputable assert over the dossier — checker territory, run any time, by anyone ^c20260719-13u
- [DC] the predicate family — existence: a turn of the declared `Turn.Type` is in the support set; correspondence: the turn's content matches the surface content; order: the evidence sequence is right — an approval that predates the current wording gates nothing ^c20260719-12u
- [DC] gate strength is predicate composition: `Verbatim.User.Gated` = existence + correspondence + order; `Edition.Trigger.User.Gated` = existence only ^c20260719-15u
- [DC] gate state is computed from evidence, never stored — invalidation is not an operation, it is recomputation returning failed ^c20260719-14u
- [PR] the robustness: enforcing the flow is hard; auditing it is cheap — the system does not prevent flow violations, it detects them and the gate invalidates retroactively; design for audit, not for enforcement ^c20260719-14u ^c20260719-15u
- [DC] graded checkability: turn-exists, turn-typed, timestamp-order are CPU; "this turn really approves this content" is the agent floor ^c20260719-15u
- [DC] gates attach to any assertable object — index lines, blocks, skw annotations: gates-as-skw-primitive is this concept applied there, not a separate design ^c20260719-15u

****

## Edition.Trigger.User.Gated

- [DF] `Edition.Trigger.User.Gated` is the convenience gate: the user explicitly initiates the edit workflow — the agent never starts writing mid-conversation on its own ^c20260716-6u
- [PR] its value is workflow control: the user owns the conversation tempo; capture does not interrupt discussion ^c20260716-6u
- [DC] auditable but low value: the triggering turn is on the chat like any other, but nothing rides on checking it — a skip's worst case is a premature draft ^c20260716-6u
- [DC] distinct from `Verbatim.User.Gated`, which gates what is written rather than when
- [DC] an instance of `User.Gate` — its assert composes existence only, the weak gate ^c20260719-15u
- asking "should I write this?" is allowed; opening an editor without approval is not
- a surface can apply one or both gates independently

### meta

- aliases: `Edit.Trigger.Gated`

****

## Verbatim.User.Gated

- [DF] `Verbatim.User.Gated` is the authority gate: the user approves the exact wording before it is committed — content passes through `User.Attention` ^c20260716-5u
- [PR] this is the gate's value: the touched index moves at user speed because the user actually saw every line land ^c20260716-5u
- [DC] approval is per line: each line's `Chat.Support.Set` holds a `Turn.Type::Project.Index.Gate` turn — the evidence the user saw it ^c20260716-5u ^c20260716-10u
- [DC] approving a block is approving all its lines — one user act, every line grounded to that approval turn ^c20260716-5u
- [DC] the gate is auditable state: presence of the gate turn is CPU-lintable; correspondence of text to turn is an agent check ^c20260716-5u
- [DC] the verbatim evidence precedes or is contained in the approval turn: the agent shows the exact line in chat, the user approves — the lint searches at-or-before the approval turn, and a miss is a linter POI for agent judgment, not a failure ^c20260716-7u
- [PR] the gate aligns both directions: user → index carries authority; system → user shows the user every line, refreshing their model of the system bit by bit ^c20260716-7u
- [DC] implies `Edition.Trigger.User.Gated` — gated content necessarily has a gated trigger
- [DC] an instance of `User.Gate` — its assert composes existence + correspondence + order, the strong gate ^c20260719-15u
- the agent proposes; the user settles — no silent rewrites or unreviewed content
- supports `Hugentic.Alignment` — the review point is where human judgment shapes the surface

### meta

- aliases: `Content.Verbatim.Gated`

****

## Kernel.Note

- `Kernel.Note` is a portable markdown file made to contain `Kernel.Block` sections
- it is a collection surface for blocks, not a block type
- it captures or develops the fundamental structure of a subject by grouping named blocks in one file
- source material can be any inspectable thing: chat, skill, codebase, document, argument, or observed system behavior
- it can be produced from an existing corpus or maintained during an active conversation
- unlike `Index.Block`, a `Kernel.Note` is not necessarily part of an index or routing table
- its purpose is portable block collection, conceptual extraction, and argument substrate
- a `Kernel.Note` can later be promoted into index blocks, appendix material, design artifacts, or implementation guidance

****

## Account.Management

- `Account.Management` is the agentos subsystem that models provider login across all providers and account types under one shared lifecycle
- one lifecycle, never per-provider: provider differences are absorbed by the `Account.Model::Auth.Method` class — it owns how `Auth.Data` is read, stored, identity-extracted, and materialized per provider
- the three `Auth.Data` primitive operations — `Auth.Data.Capture`, `Auth.Data.Activation`, `Auth.Data.Materialization` — are the atomic, composable units; each is the sole writer of one state layer (archival / synchronization / home), and workflows like rotation compose them
- a `Materializable.Account` can be reconstituted into a logged-in agent from stored `Auth.Data`; non-materializable accounts are reference-only
- the `Account.Registry` stores `Auth.Data` as append-only immutable history with one active pointer per account
- `Keep.Up.With.Rotation` — capturing refreshed credentials before they are lost is the registry's core duty, so re-login is minimized
- `Auth.Data.Capture` is the robust core — additive and content-addressed; by `Capture.Over.Materialization` it has strict priority over the home-writing direction
- capture never rejects — `Auth.Data` that binds to no known account is preserved in a fallback `Unknown.Account` for later adoption; errors over unknown credentials happen downstream, not at capture
- `Active.Auth.Data` is a registry pointer (not an auth property); `Auth.Data.Aligned` is the desired home↔active match and `Auth.Data.Drift` its read-only negation, with `Auth.Data.Rotation` (capture+activate) the response to refresh-drift
- `Account.Identity` is provider-specific data in `Auth.Data` that binds a captured credential to the right account — the authoritative anchor, not the alias or the home
- home-write invariant: a live home is mutated only by explicit, user-invoked `Auth.Data.Materialization` — never automatically, because a home write is destructive
- active-pointer invariant: the `Active.Auth.Data` pointer may move automatically (e.g. `Auth.Data.Rotation` tracking provider refreshes), because the `Account.Registry` is append-only immutable history and the pointer is reversible selection — moving it destroys nothing; observation → archive (capture) is likewise always non-destructive
- relates to `Provider.Instance` (a bound home+profile+credentials), `Agentos.Agent.Adapter` (which lists `Provider.Account`/`Provider.Home`/credential artifacts as supporting primitives), and `Normalization.Pipeline::Account.Usage.Model` (usage, downstream of login)

### appendix

- full sub-concept blocks in `appendix/Account.Management-appendix.md`: `Auth.Data.Capture`, `Auth.Data.Activation`, `Auth.Data.Materialization`, `Account.Model`, `Account.Model::Auth.Method`, `Account.Identity`, `Materializable.Account`, `Home.State`, `Auth.Data`, `Auth.Ref`, `Auth.Data.Artifact`, `Valid.Credentials`, `Auth.Registry`, `Account.Registry`, `Keep.Up.With.Rotation`, `Capture.Over.Materialization`, `Unknown.Account`, `Active.Auth.Data`, `Auth.Data.Aligned`, `Auth.Data.Drift`, `Auth.Data.Rotation`

****

## Agentos.Daemon

- [DF] `Agentos.Daemon` is a single long-lived background process that runs registered `Background.Job`s, extending Agentos beyond one-shot CLI invocation ^c20260725-41u
- [DC] its process lifecycle is owned by the OS service manager (`launchd` on macOS) — start-at-login, keep-alive, and restart-on-crash come from the platform, not from hand-written daemonization ^c20260725-41u
- [DC] exactly one global instance runs per machine, making it the sole owner of background work and the sole writer of the shared state its jobs maintain ^c20260725-41u
- [DC] work reaches the daemon from two feeds — the internal scheduler firing jobs on their natural frequency, and external run-now triggers from the CLI (`Daemon.Trigger`) ^c20260725-41u
- [DC] both feeds converge on one serialized work lane: a single worker running one job to completion at a time ^c20260725-41u
- [DC] the single lane is what makes single-writer serialization and trigger coalescing fall out for free — without locks, a job queue, or async state ^c20260725-41u
- [DC] the daemon and the CLI are peer consumers of one core library; the daemon holds only scheduling and the trigger interface, never the work logic itself ^c20260725-41u
- [DC] each command is either daemon-path or CLI-local — exactly one path per command, chosen once ^c20260725-41u
- [RJ] v1 adds no inline fallback when a daemon-path command finds the daemon down — dual-path redundancy is deferred, so daemon-path availability rests entirely on the service manager ^c20260725-41u
- [EX] concrete hosted jobs: continuous Chatlas index refresh over active sessions, and `Account.Management` rotation and usage monitoring — work that today runs only while a foreground command stays open ^c20260725-41u

****

## Background.Job

- [DF] `Background.Job` is a named unit of recurring work an `Agentos.Daemon` hosts — a name, a natural frequency, and a `run()` body ^c20260725-43u
- [DC] the `run()` body lives in the core library — the same function the CLI would invoke directly — so the daemon carries scheduling, never a second copy of the work logic ^c20260725-43u
- [DC] the job registry is the shared interface between daemon and CLI: the daemon schedules jobs by it, the CLI names a job through it to trigger a run ^c20260725-43u
- [CT] a job must be safe to run more often than its natural frequency, because an external trigger can fire it between scheduled runs ^c20260725-43u
- [PR] a job stays incremental and cheap when nothing changed, so both frequent ticks and burst triggers stay affordable ^c20260725-43u
- [EX] Chatlas refresh is a job — each run re-ingests only sessions touched since the last run (`chatlas update --since`), keyed off recently active sessions detected at minute granularity ^c20260725-43u

****

## Daemon.Trigger

- [DF] `Daemon.Trigger` is the interface by which a CLI force-runs a registered `Background.Job` now and receives its completion ^c20260725-44u
- [DC] its transport is a local unix domain socket — local-only, with filesystem permissions as the sole authorization; no TCP port or network surface ^c20260725-44u
- [DC] the submitting connection stays open for the request's lifetime and is at once the request, the wait, and the completion signal — one JSON line in, one JSON line out, then close ^c20260725-44u
- [DC] a trigger is satisfied by a job run that completes at or after the request moment; concurrent triggers arriving during one in-flight run all resolve off that single run (the coalescing rule) ^c20260725-44u
- [CT] the interface can fire only pre-registered jobs, never arbitrary operations — the trigger surface is the job registry, not remote code execution ^c20260725-44u
- [EX] failure detection falls out of the open connection: a daemon crash surfaces as EOF on the waiting read, and a CLI exit surfaces as a peer close to the daemon ^c20260725-44u
