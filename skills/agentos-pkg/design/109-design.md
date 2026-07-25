> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Agentos.Bloberia

- [DF] `Agentos.Bloberia` is the Agentos subsystem providing query:value storage for JSON-serializable data and metadata associated with agent work. ^c20260724-31u
- [PR] Agentos applications use it as a common machine-readable data substrate instead of independently implementing persistence and query mechanics. ^c20260724-31u
- [DC] Bloberia is an importable library; `agentos bloberia ...` is its first consumer and a thin CLI over the same library contract. ^c20260724-31u
- [DF] a `Bloberia.Record` consists of a reserved read-only Bloberia envelope and an application-owned JSON value. ^c20260724-31u
- [DC] structural queries select records; opaque immutable record identity addresses one record for reading or mutation. ^c20260724-31u
- [CT] Bloberia owns mechanical storage concerns; integrating applications own payload meaning, schema, mutability, and dataflow. ^c20260724-31u
- [DC] storage is depot-scoped and every initial operation receives one explicit `Bloberia.Depot`. ^c20260724-31u
