****

## Anchory.System/Appendix

- `Anchory.System` is the Agentos subsystem for stable symbolic links to contexts on other surfaces
- it separates the small identity carried by a citing surface from the data needed to resolve that identity
- it is an Agentos-wide subsystem, not a per-project facility
- the referenced surfaces remain authoritative for their information
- Anchory is plumbing, not a source of truth

****

## Anchory.System/Anchory.Anchor

- `Anchory.Anchor` is a stable token standing for a context on another surface
- an anchor identifies an evidence neighborhood, not necessarily one exact record or turn
- the token remains small because resolution data lives in `Anchory.Register`
- an anchor's meaning is immutable
- an anchor is never reused for a different context
- an incorrect identity hint requires a new anchor
- a register entry may be amended only to correct an error or improve resolution
- anchor keys may carry application-specific hints without making those hints the generic identity contract

****

## Anchory.System/Anchory.Namespace

- `Anchory.Namespace` partitions anchor keys into independent resolution domains
- a namespace prevents equal local keys from colliding across domains
- each namespace is represented by one anchor-to-record dictionary
- namespace selection and management are deferred from the initial Anchory implementation
- the initial implementation exposes only the default namespace named `global`
- `global` remains explicit in storage so later namespace support does not require a format migration

****

## Anchory.System/Anchory.Register

- `Anchory.Register` is the set of anchor dictionaries stored in an `Anchory.Depot`
- each dictionary maps an `Anchory.Anchor` to an `Anchory.Record`
- registration checks that the qualified key is free
- duplicate-key attempts are normal operational collisions, not a condition requiring preventive uniqueness machinery
- a caller handles a collision by querying, disambiguating, or minting another key
- desynchronization is detected by agents reading the referenced surfaces, not by treating the register as truth

****

## Anchory.System/Anchory.Record

- `Anchory.Record` is the value stored under an `Anchory.Anchor`
- a record carries the application-owned data needed to resolve the anchor
- Anchory persists the record without owning the meaning of its application-specific payload
- the integrating application owns traversal from the record to the referenced surface

****

## Anchory.System/Anchory.Depot

- `Anchory.Depot` is a folder containing one self-contained Anchory store
- an application owns and selects the depot
- every Anchory operation receives a depot scope
- anchor uniqueness is scoped to the depot and namespace
- a bare anchor resolves against the active depot
- only the Anchory interface may mutate depot files
- Anchory owns locking and atomic file mutation inside the depot
- Anchory performs no Git operations
- the owning application decides whether and how depot changes are versioned

****

## Anchory.System/Integration

- Anchory is library-first so other Agentos subsystems can integrate with it directly
- the library owns anchor identity, depot persistence, registration, lookup, query, and amendment
- the library interface is the exclusive writer of Anchory files
- every library action is scoped to a caller-selected `Anchory.Depot`
- applications must not modify Anchory files directly
- the Anchory CLI is a thin interface over the same library contract
- the umbrella command surface is `agentos anchory ...`
- CLI behavior must not become a second implementation of Anchory

****

## Anchory.System/Chat.Application

- chat anchoring is one application of Anchory rather than part of its generic contract
- date-based keys fit chat and index linking because human information arrives sequentially through time
- a daily position suffix keeps chat keys small, as in `20260630-0`
- the first Anchory integration is the Chatlas anchory at `<chatlas-depot>/anchory/`
- every Chatlas Anchory action uses the active Chatlas depot
- Chatlas owns traversal from an `Anchory.Record` to the session and evidence neighborhood
- the reading rule after resolution: the anchor lands in an evidence neighborhood — read the landing turn and around it
- `Index.Linking` writes anchors into grounding lines instead of embedding provider-coupled chat addresses
- full `Context.Grounding` follows those anchors through Anchory and then through Chatlas
- `Index.Agendix` can use anchors for its hard provenance rule

****

## Anchory.System/Open.Design

- open: dictionary file format and sharding
- open: whether `File.Mention` becomes an Anchory application or retains its independent resolution model

****

## Anchory.System/Grounding.Head

- [GR] the user corrects Anchory's scope — an Agentos subsystem rather than per-project, coupled with Chatlas ^c20260706-1u
