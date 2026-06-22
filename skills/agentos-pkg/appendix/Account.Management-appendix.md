****

## Account.Model

- `Account.Model` is both the concept of an agent account on agentos and its data representation
- an account is an identity owned by a provider, holding one or more `Account.Model:Auth.Method`s
- the identity carries provider-neutral fields: provider, account name, and identity metadata such as email
- the agent normal model references an account by name; credentials live under the auth methods

****

## Account.Model:Auth.Method

- `Account.Model:Auth.Method` is an independent authentication method of an account
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

- `Materializable.Account` is an account that holds at least one materializable `Account.Model:Auth.Method`
- a materializable auth method can be reconstituted into a logged-in agent from its stored `Auth.Data`
- materializability is a property of the auth method's credential class
- a non-materializable auth method is reference-only — agentos tracks it but cannot stand up a logged-in agent from it
- materializability is orthogonal to validity: stored `Auth.Data` may be present yet no longer accepted by the provider

****

## Auth.Data

- `Auth.Data` is the local data a provider reads to authenticate a login
- shape is provider-specific — the `Auth.Method` seam (codex `auth.json`, claude Keychain entry, copilot gh-token reference)
- pipeline: `Raw.Credential.Data` (as read from a live source) → `Registered.Data` (normalized and stored in the registry)
- what to store and how is delegated to the provider/agent implementation
- payloads can contain secrets; index and ledger surfaces must never carry raw tokens

****

## Account.Identity

- `Account.Identity` is whatever data in `Auth.Data` lets agentos identify a particular account
- it is provider-specific — each provider carries account identity in its own form (a UUID claim, a numeric user id, an email)
- it is the authoritative anchor binding a captured credential to a `Provider.Account`, independent of the agentos alias or the home it came from
- extracting it from `Auth.Data` is a capability of the `Account.Model:Auth.Method` class
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

## Account.Registry

- `Account.Registry` stores the `Auth.Data` needed to log in any `Materializable.Account`, plus convenience metadata
- append-only immutable history: each captured credential version is its own entry; rotation produces a new entry; one active/current pointer
- history and the active pointer attach per `Account.Model:Auth.Method`, since an account can hold several auth methods
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

## Account.State.Tape

- `Account.State.Tape` is an append-only registry that records `Account.Management` state as a sequence of events
- each primitive operation owns one tape — capture, activation, materialization
- operations only append; a tape is never rewritten or hand-edited
- current state is read back as the last relevant record on the tape
- it holds state only — config is a separate, declarative surface

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

## Active.Auth.Artifact

- `Active.Auth.Artifact` is the registry-designated current `Auth.Data.Artifact` for an `Auth.Method`
- it is a registry state — the registry asserting which artifact is current, not a property of the credential
- distinct from `Valid.Credentials` and from freshness: active marks the designated pointer, not a checked or proven property
- the registry does not verify freshness when setting it — that active should be freshest-and-valid is policy, not a guarantee of the state
- one active pointer per `Auth.Method`

****

## Active.Auth.Artifact.Rotation

- `Active.Auth.Artifact.Rotation` is the registry operation that moves the `Active.Auth.Artifact` to another `Auth.Data.Artifact`
- it is a registry operation, never a home write — same family as `Capture.Over.Materialization`
- it answers rolling auth: a refresh under one home can get a later home's credential refused, so the active pointer must follow the current credential
- capture and activation are orthogonal axes — a path may couple them or keep them independent
- activation modes: explicit (set any artifact active), capture-coupled (promote on capture), conditional (promote when a condition holds), automatic (resolve the active artifact from the credentials themselves)
- automatic resolution needs a self-describing auth-method — one whose `Auth.Data` exposes freshness without a provider call; otherwise promotion needs verification

****

## Active.Auth.Drift

- `Active.Auth.Drift` is a read-only check that an agent/home is using the `Active.Auth.Artifact`
- it compares a home's `Auth.Data` against the registry's active pointer, with no provider call
- a mismatch flags likely-stale auth, aiding stale detection
- it is the inverse of materialization — reads and compares rather than writes the home
