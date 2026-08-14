> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Agentos.Bloberia

- [DF] `Agentos.Bloberia` is the Agentos subsystem providing query:value storage for JSON-serializable data and metadata associated with agent work. ^c20260724-80u
- [PR] Agentos applications use it as a common machine-readable data substrate instead of independently implementing persistence and query mechanics. ^c20260724-107u
- [DC] Bloberia is an importable library; `agentos bloberia ...` is its first consumer and a thin CLI over the same library contract. ^c20260724-58u
- [DF] a `Bloberia.Record` consists of a reserved read-only Bloberia envelope and an application-owned JSON value. ^c20260724-85u
- [DC] structural queries select records; opaque immutable record identity addresses one record for reading or mutation. ^c20260724-74u
- [CT] Bloberia owns mechanical storage concerns; integrating applications own payload meaning, schema, mutability, and dataflow. ^c20260724-39u
- [DC] storage is depot-scoped and every initial operation receives one explicit `Bloberia.Depot`. ^c20260724-73u

****

## Bloberia.Record.Namespace

- [DF] a `Bloberia.Record.Namespace` is a subfolder under a depot's `records/`, addressed as a path prefix of arbitrary depth ^c20260806-31u
- [DC] namespaces organize placement only; they carry no meaning Bloberia enforces and are not part of record identity ^c20260806-32u
- [CT] a namespace is data outside the record: an application that lets a fact live only in the path owns that risk ^c20260806-33u
- [DC] a namespace-less read falls back to iterating every record under `records/`, so an existing flat depot stays readable unchanged ^c20260806-34u
- [DC] addressing a record by identity without its namespace searches every namespace rather than failing ^c20260806-35u
- [DC] locking stays depot-wide; namespaces partition reads, not writes ^c20260806-36u
- [PR] partitioning by namespace is what lets a query touch only the records it needs instead of reading the depot ^c20260806-37u
