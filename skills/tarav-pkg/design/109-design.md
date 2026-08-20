> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Agentos.Bloberia

- [DF] `Agentos.Bloberia` is a type-directed storage system in which every depot declares one `Bloberia.Depot.Type`. ^c20260820-10u
- [DC] each depot type owns its physical format, storage topology, validation rules, and type-specific storage requirements. ^c20260820-11u
- [CT] applications own cargo meaning and lifecycle, while the selected depot type may constrain the representation required for storage. ^c20260820-12u
- [DC] common query operations expose the depot type’s logical cargo projection without exposing its private physical layout. ^c20260820-13u
- [EX] the `files` type stores one JSON cargo value per private file. ^c20260820-14u
- [EX] the `shards` type stores keyed JSON cargo values across digest-selected shard files and requires a declared depot-unique key. ^c20260820-15u
- [CT] a new depot type may introduce a different format and storage solution without redefining the application’s domain model. ^c20260820-16u

****

## Bloberia.Record.Namespace

- [DF] a `Bloberia.Record.Namespace` is a subfolder under a depot's `records/`, addressed as a path prefix of arbitrary depth ^c20260806-31u
- [DC] namespaces organize placement only; they carry no meaning Bloberia enforces and are not part of record identity ^c20260806-32u
- [CT] a namespace is data outside the record: an application that lets a fact live only in the path owns that risk ^c20260806-33u
- [DC] a namespace-less read falls back to iterating every record under `records/`, so an existing flat depot stays readable unchanged ^c20260806-34u
- [DC] addressing a record by identity without its namespace searches every namespace rather than failing ^c20260806-35u
- [DC] locking stays depot-wide; namespaces partition reads, not writes ^c20260806-36u
- [PR] partitioning by namespace is what lets a query touch only the records it needs instead of reading the depot ^c20260806-37u
