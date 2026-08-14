****

## Account.Model

- `Account.Model` is both the concept of an agent account on agentos and its data representation
- an account is an identity owned by a provider, holding one or more `Account.Model::Auth.Method`s
- the identity carries provider-neutral fields: provider, account name, and identity metadata such as email
- the agent normal model references an account by name; credentials live under the auth methods

****

## Account.Model::Auth.Method

- `Account.Model::Auth.Method` is an independent authentication method of an account
- it is a credential class — `auth-json`, `ambient-auth`, `gh-auth-token`
- it models what login the method achieves and how the method works
- its class defines the method's fixed properties
- an account holds several auth methods, each independent
- a call can select which auth method to use
- auth methods are provider-specific

### meta

- aliases: `Auth.Method`

****

## Materializable.Account

- `Materializable.Account` is an account that holds at least one materializable `Account.Model::Auth.Method`
- a materializable auth method can be reconstituted into a logged-in agent from its stored `Auth.Data`
- materializability is a property of the auth method's credential class
- a non-materializable auth method is reference-only — agentos tracks it but cannot stand up a logged-in agent from it
- materializability is orthogonal to validity: stored `Auth.Data` may be present yet no longer accepted by the provider

****

## Home.State

- `Home.State` is the actual authentication state of a home — the provider surface an agent reads to log in
- it is reality: agentos observes it, and never treats a stored record as a substitute for reading it
- its shape is provider-specific — a `CODEX_HOME` `auth.json`, a path-scoped Keychain entry, an ambient provider session
- `Auth.Data` and `Auth.Ref` are constructed by reading it; materialization writes `Auth.Data` back to it
- it is the ground truth a drift check compares against — a registry designation is only intent until matched to a `Home.State`

****

## Auth.Data

- `Auth.Data` is the totality of data agentos's auth system needs for an `Auth.Method`
- it is collected to serve distinct objectives — authentication (tokens, `auth.json` artifacts) and identification (provider, account, credential version) — more may be added
- it is deliberately built to contain a sufficient, unambiguous `Auth.Ref` — its identification projection
- it is the transport object between reality and the registry: `Home.State ↔ Auth.Data ↔ Auth.Registry`
- capture constructs it from a `Home.State`; materialization writes it back to a `Home.State`
- if it cannot be extracted from a `Home.State`, there is no `Auth.Data` — the `Auth.Method` is reference-only (non-materializable), and only its `Auth.Ref` exists
- how the registry stores it is flexible, delegated to the `Auth.Method` — file, content-addressed artifact, token blob, or a bare reference
- it can carry secrets — only `Auth.Registry` holds it; index and log surfaces carry `Auth.Ref`, never raw `Auth.Data`

****

## Auth.Ref

- `Auth.Ref` is the identification-only projection of `Auth.Data` — enough to identify it unambiguously, never enough to materialize
- it names a credential's provenance — provider, account, and the specific artifact/credential version
- `Auth.Data` is deliberately built to contain an unambiguous `Auth.Ref`; for reference-only methods the `Auth.Ref` stands alone
- it is lossy and one-way — `Auth.Data` and `Home.State` cannot be reconstructed from it
- it carries no secret, so it is safe on index, log, and registry surfaces
- it is the key for every identification operation — e.g. "is this already registered?" is `Home.State → Auth.Ref → Auth.Registry`
- in `Logic.Impl`, all identification runs on `Auth.Ref`, never the full secret

****

## Account.Identity

- `Account.Identity` is whatever data in `Auth.Data` lets agentos identify a particular account
- it is provider-specific — each provider carries account identity in its own form (a UUID claim, a numeric user id, an email)
- it is the authoritative anchor binding a captured credential to a `Provider.Account`, independent of the agentos alias or the home it came from
- extracting it from `Auth.Data` is a capability of the `Account.Model::Auth.Method` class
- the account record stores its normalized form as `provider_account_id` when the method yields a stable id
- all auth methods of one account resolve to the same `Account.Identity`; a divergent identity means a different account

****

## Valid.Credentials

- `Valid.Credentials` is `Auth.Data` the provider currently accepts as a successful login
- validity is time-bound and external — only a live provider interaction proves it (the `verified` lifecycle state)
- rotation can invalidate previously-valid data with no action by agentos
- orthogonal to materializability: holding the data to set up a home does not mean the provider still accepts it
- `verified` means was valid at capture time, never guarantees is valid now

****

## Auth.Registry

- `Auth.Registry` is the agentos store for captured `Auth.Data`, kept on agentos's own controlled paths
- it is the registry end of the flow `Home.State ↔ Auth.Data ↔ Auth.Registry` — capture extracts `Auth.Data` from a `Home.State` and stores it here; materialization reads it back
- how each credential is stored is delegated to the `Auth.Method`; the registry offers facilities such as a content-addressed artifact store but imposes no single schema
- identification queries resolve against it via `Auth.Ref` — e.g. "is this already registered?"
- it is the access point for auth credential data; account metadata is the concern of `Account.Registry` (whether one nests inside the other is unspecified)
- it is authoritative for what agentos has captured; the live `Home.State` stays authoritative for what is actually in a home

****

## Account.Registry

- `Account.Registry` stores the `Auth.Data` needed to log in any `Materializable.Account`, plus convenience metadata
- append-only immutable history: each captured credential version is its own entry; rotation produces a new entry; one active/current pointer
- history and the active pointer attach per `Account.Model::Auth.Method`, since an account can hold several auth methods
- storage shape is delegated to the provider implementation (`Auth.Method`)
- non-materializable accounts store reference and metadata only — no reconstructible secret
- existing implementation surfaces: `accounts.json` (pointer records), `artifacts.jsonl` + `artifacts/<id>.<kind>.json` (immutable index + payloads, `id = sha256(payload)`), `verifications.jsonl` (success ledger, secrets rejected)

****

## Keep.Up.With.Rotation

- `Keep.Up.With.Rotation` is the registry's responsibility to track provider credential refreshes so stored `Auth.Data` stays current
- providers refresh and rotate tokens under the live home; the home continually advances past the registry
- detecting and storing refreshed credentials is the registry's core job, not an optional optimization
- a registry that misses rotations holds stale snapshots and forces avoidable re-logins
- goal: minimize the need to re-login by capturing refreshed `Auth.Data` as it appears
- mechanism: append-only capture of each new credential version, one current pointer per `Auth.Method`
- standing hazard it answers: two live homes off one account race over single-use refresh tokens; the loser is invalidated and its captured snapshot goes stale

****

## Auth.Data.Artifact

- `Auth.Data.Artifact` is a single captured version of `Auth.Data`, stored immutable and content-addressed
- it is the leaf of the nested structure `Provider.Account` → `Auth.Method` → `Auth.Data.Artifact`
- its identity is the content hash of its payload, so identical captures dedup and any change is a new artifact
- it belongs to one `Auth.Method` of one `Provider.Account`
- it is preserved regardless of validity — kept for recovery even when stale or invalid

****

## Auth.Data.Capture

- `Auth.Data.Capture` is the primitive operation that observes `Auth.Data` from a live source and archives it
- sole writer of the archival layer — the stored artifacts and the capture log
- reads the source to observe; reads prior capture state to classify by `Account.Identity` and dedup
- classifies, never rejects — known `Provider.Account` ⇒ filed under it; identifiable orphan ⇒ `Unknown.Account`
- never touches activation, never touches a home — observation only, non-destructive
- priority 1: it precedes every other operation (`Capture.Over.Materialization`)
- records the capture in the capture log

****

## Auth.Data.Activation

- `Auth.Data.Activation` is the primitive operation that designates which archived `Auth.Data.Artifact` is current for a `Provider.Account`'s `Auth.Method`
- sole writer of the synchronization layer — the activation log
- reads capture state (the artifact must already be archived) and the current activation
- a pure registry move — never writes artifacts, never writes a home
- a designation, not proof — it does not assert the credential is `Valid.Credentials`
- records the activation in the activation log

****

## Auth.Data.Materialization

- `Auth.Data.Materialization` is the primitive operation that writes a `Provider.Account`'s active `Auth.Data` into a home so an agent can log in
- the only primitive operation that mutates a home — sole writer of the home/system layer
- reads the active artifact and the home↔account binding; writes the home via the `Auth.Method`
- a pure write — it does not capture, activate, or verify
- capture-first by composition: a `Auth.Data.Capture` precedes the overwrite, so no credential is lost
- records the write in the materialization log

****

## Capture.Over.Materialization

- `Capture.Over.Materialization` is the priority rule that capture wins when capture and materialization conflict
- the directions oppose: capture reads a credential out of a home; materialization writes a credential into a home
- the conflict: materializing risks overwriting a live credential the registry has not yet captured
- the rule: capture first, materialize second — never write over un-captured `Auth.Data`
- rationale: a lost credential may be unrecoverable; a deferred materialization is merely inconvenient
- it is the home-mutation invariant seen from the data side — capture stays always-safe, materialization is the path that yields

****

## Unknown.Account

- `Unknown.Account` is the fallback `Provider.Account` where `Auth.Data.Capture` stores `Auth.Data` it cannot bind to a known account
- capture never rejects — an unmatched credential is preserved, never discarded, because it may still be needed
- the `Account.Identity` check classifies (known vs unknown); it does not gate capture
- the `Auth.Data` must be recognizable — capture extracts an `Account.Identity`, so the fallback holds identifiable orphans, not anonymous data
- it keeps the extracted identity, so an orphan can be adopted into a real account once that account is registered
- hard errors over unknown credentials belong downstream — activation, materialization, use — never at capture
- structurally a reserved `Provider.Account` per provider, reusing the `Provider.Account → Auth.Method → Auth.Data.Artifact` nesting

****

## Active.Auth.Data

- `Active.Auth.Data` is the registry-designated current `Auth.Data.Artifact` for an `Auth.Method`
- it is a registry state — the registry asserting which artifact is current, not a property of the credential
- distinct from `Valid.Credentials` and from freshness: active marks the designated pointer, not a checked or proven property
- the registry does not verify freshness when setting it — that active should be freshest-and-valid is policy, not a guarantee of the state
- one active pointer per `Auth.Method`

****

## Auth.Data.Aligned

- `Auth.Data.Aligned` is the desired state where a `Home.State`'s `Auth.Data` is the `Active.Auth.Data` for its `Provider.Account`'s `Auth.Method`
- it is the single good state the system steers toward — the home holds exactly the credential the registry has designated current
- it is evaluated read-only, on `Auth.Ref`, with no provider call and no home mutation — a designation match, not a `Valid.Credentials` proof
- it is the reference against which `Auth.Data.Drift` is defined as the negation
- alignment is intent satisfied, not freshness proven — an aligned home can still hold expired credentials

****

## Auth.Data.Drift

- `Auth.Data.Drift` is the negation of `Auth.Data.Aligned` — a `Home.State` whose `Auth.Data` is not the `Active.Auth.Data`
- whatever the reason — unregistered, registered-but-not-active, or otherwise — any non-match is drift
- it is a state, evaluated by a read-only operation — it compares home against the active pointer on `Auth.Ref`, with no provider call and no home mutation
- it is a diagnosis, never a writer — detecting drift mutates nothing
- it is directional — the home can be behind the registry or ahead of it — and the direction is what a response keys on

****

## Auth.Data.Rotation

- `Auth.Data.Rotation` is the response to refresh-drift — the home-ahead case of `Auth.Data.Drift`, where the provider refreshed the home's `Auth.Data` past the registry
- it is not a primitive operation but a composition: `Auth.Data.Capture` then `Auth.Data.Activation`
- capture first preserves the new credential (`Capture.Over.Materialization`); activation then moves the `Active.Auth.Data` to follow it
- it answers rolling auth — `Keep.Up.With.Rotation`: the active pointer must track the credential the provider now accepts
- it is a registry move only, never a home write — the home already advanced on its own
- because it is a reversible registry-only move (append-only history, pointer reselection), it is safe to run automatically and unattended, while home writes stay user-gated under the home-write invariant
