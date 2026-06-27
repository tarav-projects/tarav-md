> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Project.File.Index

- `Project.File.Index` is the file-level routing section of the `Index.Router`
- describes the project's file system at folder level, with individual files listed only when fundamental
- one sentence description per entry — token budget is tight, it travels with the router whenever the index is loaded
- gives agents a structural map of where to look — not a complete listing, but the important entry points

****

## Index.Activation

- `Index.Activation` is the process of bootstrapping the `Index.Runtime` for a session
- handled through the `agentos-index` auxiliary skill or directly by an index-capable caller
- collects the relevant routing blocks, concept blocks, appendix material, and references for the current task
- activation is opt-in — triggered by `AGENTS.md`, a `Package.Driver`, or manual invocation; the index has no loading policy of its own
- operational detail: `agentos-pkg/references/launch-runtime.md`

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
- the canonical public index content lives in the package skill, usually `skills/<package>-pkg/index/`
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

## Index.Surface.Layout

- `Index.Surface.Layout` is the expected directory structure for the index system
- public index: `skills/<package>-pkg/index/` — `000-index.md` router + `100-299` flat files inside the package's `Package.Skill.Index`
- public appendix: `skills/<package>-pkg/appendix/` — `Concept.Name-appendix.md`
- local index: `notes/index/` — `001-index.md` router + `300-499` flat files
- local appendix: `notes/appendix/`
- the layout is a protocol — new projects follow this structure to be index-compatible

****

## Appendix.Discovery

- `Appendix.Discovery` is the protocol for loading depth on demand from the appendix
- trigger: when reasoning about a concept and the index block isn't sufficient
- discovery: if working with `Concept.X`, check `appendix/Concept.X-appendix.md`
- no outlink required — the naming convention is the discovery mechanism
- discovery is a cascade: index block → its appendix → hidden blocks → their appendixes
- the more blocks loaded, the more paths available — agents discover by following related blocks
- hidden blocks are not deleted — just not in the starting context
- related blocks cluster under the same appendix file when they extend related concepts

****

## Appendix.Pages

- `Appendix.Pages` extends `Appendix.Discovery` with progressive depth layers
- `Concept.X` is sugar for `Concept.X[0]` — the index block
- `Concept.X[1]` is the first appendix page (`Concept.X-appendix.md`)
- `Concept.X[2]+` are deeper pages (`Concept.X-appendix-2.md`, `Concept.X-appendix-3.md`, etc.)
- `Concept.X[:]` means all content — index block + all appendix pages (JS slice semantics)
- the notation is usable as inline reference in blocks, chat, and prompts
- discovery cascades naturally — if depth is insufficient, go deeper: more pages, or jump to other concepts
- the routing table annotates page count inline: `Concept.X[+2]` — lintable, only present when appendix exists
- no annotation means no appendix — `Concept.X` alone implies `[0]` only

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
- example: installing the index system creates `notes/index/`, `001-index.md`, routing table
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

- `Index.Depot` is a concrete index instance — the set of files with index blocks, their appendix, and a router
- built on the `Agentos.Index.Framework` — follows the same block structure, routing, writing, and discovery conventions
- one depot = public part (skill-packaged, portable) + local part (`notes/index/`, project-specific)
- each depot is self-contained — its own router(s), its own flat files, its own appendix
- a concept lives in exactly one depot — the depot that naturally owns it
- composability: an agent loads multiple depots to build its working index
- an index-capable agent works across all loaded depots by scanning their available routers

### meta

- aliases: `Agentos.Index.Depot`

****

## Provider.Instance

- `Provider.Instance` is a configured binding of a `Provider.Family` to a specific local environment
- the OOP analogy holds: `Provider.Family` is the class, `Provider.Instance` is when its parameters are bound
- parameters include home path, profile, credentials, and any family-specific configuration
- identity is derived from provider family + environment fingerprint — two different homes = two different instances

****

## Agentos.Agent.Adapter

- `Agentos.Agent.Adapter` is the Agentos code design pattern for exposing slices of a `Provider.Instance`'s capabilities on a common surface
- concrete adapters are named `<Something>.Agent` — `<Something>` names the capability surface served, not the full instance
- one `Provider.Instance` may have multiple adapters covering different capability slices
- provider differences are absorbed below the `.Agent` boundary; Agentos sees a uniform interface above it
- adapters may be partially configured — capability execution validates only what the invoked capability needs
- missing configuration is acceptable until a capability needs it
- `.Agent` is the public promise boundary; `<Something>` remains free to vary
- implementations may share stable primitives without inheriting a forced common model

### appendix

- `<Something>` may be provider-shaped, subsystem-shaped, capability-shaped, workflow-shaped, or composed
- examples: `Claude.Runner.Agent`, `Codex.Chatlas.Agent`, `Account.Monitor.Agent`, `Credential.Reconcile.Agent`
- supporting primitives may include `Agent.Profile`, `Provider.Account`, `Provider.Home`, `Provider.Family`, credential artifacts, session references, run requests, and run results
- the design keeps provider-specific and subsystem-specific complexity below the `.Agent` boundary

### meta

- aliases: `Something.Agent`, `Agent.Surface`, `Agent.Capability.Object`
- status: current — implemented in `agentos-py`. It implements `Provider.Instance` at the code level; the concept is not superseded.
- resolved: capability contracts are small typed protocols a concrete adapter may satisfy (`AgentAdapter` base + `RunCapable`/`AccountStatusCapable`/`SessionDiscoveryCapable`); run behavior is a `RunnableMixin` on runnable adapters only. Concrete adapters subclass the single `AgentConfig` field surface and stay named `<Provider>.Agent`.

****

## Normalization.Pipeline:Account.Usage.Model

- `Normalization.Pipeline:Account.Usage.Model` is the account-usage instantiation of `Normalization.Pipeline` — native provider usage artifacts normalized into `Account.Usage.Status`
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
- finding and check codes are scoped concept names under `Index.Linter/...`
- each code names an appendix block that explains meaning, gating, or expected remediation
- agents resolve linter code meaning through normal `agentos-pkg` index and `Appendix.Discovery`
- router entries use `[+N]` to expose discovered appendix page depth for routed concepts
- the linter reports errors, warnings, blocked checks, and summary counts

****

## Write.Trigger.Gated

- `Write.Trigger.Gated` is a gating constraint: the user must explicitly initiate the write — the agent never starts writing on its own
- asking "should I write this?" is allowed; opening an editor without approval is not
- applies to any surface that wants human control over when mutation happens
- distinct from `Content.Verbatim.Gated`, which gates what is written rather than when
- a surface can apply one or both gates independently
- operational detail: `agentos-index --write`

****

## Content.Verbatim.Gated

- `Content.Verbatim.Gated` is a gating constraint: the user must approve the exact wording before it is committed
- the agent proposes; the user settles — no silent rewrites or unreviewed content
- implies `Write.Trigger.Gated` — if content is gated, the trigger is necessarily gated too
- supports `Hugentic.Alignment` — the review point is where human judgment shapes the surface
- operational detail: `agentos-index --write`

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
- one lifecycle, never per-provider: provider differences are absorbed by the `Account.Model:Auth.Method` class — it owns how `Auth.Data` is read, stored, identity-extracted, and materialized per provider
- the three `Auth.Data` primitive operations — `Auth.Data.Capture`, `Auth.Data.Activation`, `Auth.Data.Materialization` — are the atomic, composable units; each is the sole writer of one state layer (archival / synchronization / home), and workflows like rotation compose them
- a `Materializable.Account` can be reconstituted into a logged-in agent from stored `Auth.Data`; non-materializable accounts are reference-only
- the `Account.Registry` stores `Auth.Data` as append-only immutable history with one active pointer per account
- `Keep.Up.With.Rotation` — capturing refreshed credentials before they are lost is the registry's core duty, so re-login is minimized
- `Auth.Data.Capture` is the robust core — additive and content-addressed; by `Capture.Over.Materialization` it has strict priority over the home-writing direction
- capture never rejects — `Auth.Data` that binds to no known account is preserved in a fallback `Unknown.Account` for later adoption; errors over unknown credentials happen downstream, not at capture
- `Active.Auth.Data` is a registry pointer (not an auth property); `Auth.Data.Aligned` is the desired home↔active match and `Auth.Data.Drift` its read-only negation, with `Auth.Data.Rotation` (capture+activate) the response to refresh-drift
- `Account.Identity` is provider-specific data in `Auth.Data` that binds a captured credential to the right account — the authoritative anchor, not the alias or the home
- home-mutation invariant: only explicit, user-invoked operations mutate a live home or active pointer; observation → archive is always allowed because it is non-destructive
- relates to `Provider.Instance` (a bound home+profile+credentials), `Agentos.Agent.Adapter` (which lists `Provider.Account`/`Provider.Home`/credential artifacts as supporting primitives), and `Normalization.Pipeline:Account.Usage.Model` (usage, downstream of login)

### appendix

- full sub-concept blocks in `appendix/Account.Management-appendix.md`: `Auth.Data.Capture`, `Auth.Data.Activation`, `Auth.Data.Materialization`, `Account.Model`, `Account.Model:Auth.Method`, `Account.Identity`, `Materializable.Account`, `Home.State`, `Auth.Data`, `Auth.Ref`, `Auth.Data.Artifact`, `Valid.Credentials`, `Auth.Registry`, `Account.Registry`, `Keep.Up.With.Rotation`, `Capture.Over.Materialization`, `Unknown.Account`, `Active.Auth.Data`, `Auth.Data.Aligned`, `Auth.Data.Drift`, `Auth.Data.Rotation`

### meta

- status: current design capture (2026-06) — redesign in progress; the credential machinery exists in `agentos-py` but was previously un-indexed
- open: the freeze/suspension of non-explicit home-mutating paths is decided in principle; exact write taxonomy still being settled
- open: the `Account.Model` field set carried by every account regardless of type
- pending merge: `Account.Registry` needs reworking for the config/state split
