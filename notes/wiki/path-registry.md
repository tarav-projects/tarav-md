# PathRegistry: computed structure, maintained identity

<!-- tarav.sessions
0f5bad01 = codex:01a15483-94e8-7fe0-86ad-ddd83e2bae52 @0f5bad0131260477b4cf3d712a95871496c3db92d67eaa7910243e312f7b552a
-->

## Design

While discussing documentation in the extension's JSON object inspector, the
User proposed a shared registry of JSON positions. Each position has a Ship;
documentation and other identified objects attach to that identity. Every active
identity declares a path. When a View changes, maintainers explicitly preserve,
create or retire identities. Git retains the map's history.
<!-- tarav.breadcrumb 9695a9e36353 -->

The User confirmed the separation between computed structure and maintained
identity: introspection detects change, while agents and users maintain the map
through ordinary Project Actions. A Project owns its PathRegistry. Project Type
enumeration is a separate capability, using the existing Type registry and
Project interfaces rather than another discovery mechanism.
<!-- tarav.breadcrumb 7420b563ed63 -->

## Implementation — request 948

[Request 948](../../../tarav-py/notes/live/948-project-path-registry-impl-req.md)
implements the first Python surface:

- `TaravObject.view_schemas()` exports the RecordInterface JSON Schema and a
  partial instance schema. Default instance inspection reads declarations and
  signatures without constructing instances, evaluating annotation strings or
  invoking property getters. Types can override the producer.
- `project.types.all()` selects already registered classes by their defining
  source file under the Project root. Project Types can override membership.
- `project.paths` manages explicit enrollment, storage at `.tarav/paths.json`,
  computation and checks. An absent registry stays absent on reads and checks.
- JSONView has a stable owning Type/name identity. Path entries have independent
  Ships, declared positions and active state. Request 948 originally also stored
  attachment Ships and defined `PathDocumentation`; request 950 removes those
  responsibilities, following the User's clarification below.
- Paths are RFC 6901 pointers into the finite View JSON: for example,
  `/properties/text` in a schema. Recursive JSON Schema references remain literal
  references; this implementation does not expand them into an object graph.
- Maintenance explicitly enrolls, adds, reassigns, retires or accepts structure.
  Reassigning a path retains its Ship. Checks never infer a
  semantic rename or rewrite the registry.

These implementation facts are described in the
[workflow guide](../../../tarav-py/src/tarav/l1/path_registry/README.md),
[Project integration](../../../tarav-py/src/tarav/l2/project/paths.py) and
[behavior tests](../../../tarav-py/tests/test_path_registry.py).

Typed findings cover changed schemas, missing/new positions, duplicate
declarations, undeclared active identities, repeated Ships and missing Views.
Project status integrates them into normal Actions. An unavailable scan does not
certify that an old finding disappeared. Enrollment is opt-in; the initial
implementation adds no extension UI or independent history database.

The full Python run passed 66 test suites. All 389 currently selected registered
Types produced their default Views in a read-only probe. Instance schemas still
declare themselves partial: neither that probe nor introspection proves a
complete description of arbitrary runtime attributes.

See also [Projects](projects.md) and [Record framework](record-framework.md).

## Identity ownership — request 950

The User clarified that PathRegistry provides and tracks schema and path
identities. The registry identifies a schema, rather than an instance, and
positions inside that schema. Documentation is one use case for those Ships;
other workflows own their relationships to the Ships. PathRegistry need not
contain or know about those relationships.
<!-- tarav.breadcrumb c6e2922b7812 -->

The User requested this separation and authorized execution of the follow-up
implementation request.
<!-- tarav.breadcrumb 9a3dd836251e -->
<!-- tarav.breadcrumb 40e5303f46fd -->

[Request 950](../../../tarav-py/notes/live/950-path-registry-identity-boundary-impl-req.md)
removes attachment fields, `attach()` and the registry-owned documentation Line
Type. It retains existing schema/path Type Ships, explicit identity maintenance,
Project checks, storage and Git history. The
[consumer association test](../../../tarav-py/tests/test_path_registry.py)
uses a regular Line and a separately held mapping keyed by Path Ship: rename and
save/load preserve the reference, while no consumer data enters the registry.
The [architecture test](../../../tarav-py/tests/test_architecture.py) also checks
that the registry no longer imports Lines. No new documentation workflow is
defined by this change.

The subsequent [LabelFormats](label-formats.md) implementation shares the JSON
Pointer validation rule with PathRegistry. Path Ships still identify schema
positions independently of their current text; the shared Label vocabulary does
not add attachment storage to this registry.
