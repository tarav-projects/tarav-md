# Product Mapping

<!-- tarav.sessions
ec6cf584 = codex:01a1563b-2992-7c62-8a38-05c1cc75b1fe @ec6cf5849bb6c4e66f011b015415da94eeb1a17634872aa4fb9e25d8e065ab53
-->

## A shared coordinate system

The User separated Product Mapping from Product Review Tracker. Mapping
identifies chunks of a product surface so independent workflows can address
the same regions. Review coverage and meaningful review batches consume that
map; they do not define the mapping mechanics. The current implementation
request selects Product Mapping only.
<!-- tarav.breadcrumb 8e418fb87586 -->
<!-- tarav.breadcrumb 23d16425f5ff -->

Files and byte ranges are sufficient. The User preferred a target byte size
with boundary flexibility for initial chunks, avoiding a dependency on language
parsers. Existing chunks can grow, shrink or move rather than being forced
back into fixed-size partitions at each version.
<!-- tarav.breadcrumb 77c893602a1a -->
<!-- tarav.breadcrumb 7ac702bd6c22 -->
<!-- tarav.breadcrumb 8f47cde47e9a -->

## Identity is a maintenance decision

The map works entirely on committed states. Git provides exact bytes and diff
evidence; the User and Agent maintain continuity. They decide whether a chunk
keeps its ID, receives new IDs through replacement or splitting, merges with
others, or retires. A matching fingerprint establishes content equality, not
semantic identity. A changed content version can retain the same chunk ID.
<!-- tarav.breadcrumb ec8dd7147539 -->
<!-- tarav.breadcrumb 3d74f9fb7aee -->

Each confirmed map belongs to a particular commit and remains coherent with
its previous map through recorded continuity decisions. There is no requirement
to produce a map for every commit. Maintainers can reconcile endpoint states
many commits apart and inspect intermediate history when useful.
<!-- tarav.breadcrumb 971de9ce3981 -->
<!-- tarav.breadcrumb 9673b6e8f01e -->

## Freshness and on-demand work

The discussion initially considered delaying mapping until code had settled.
The User refined that into a default freshness trigger: request an update when
the latest map is too old and newer committed work exists. This does not
restrict on-demand targets. A workflow may map HEAD, chosen historical commits,
or every commit if needed. Review stability remains a separate consumer policy.
<!-- tarav.breadcrumb 02d3d3f1c0e3 -->

## Initial whole-repository exercise — superseded

The User requested implementation against tarav-py and a historical run at
roughly ten-commit intervals through the current product state.
<!-- tarav.breadcrumb 73f998bb8c06 -->

The [library](../../../tarav-py/src/tarav/l1/product_mapping/mapper.py) separates
editable proposals, exact byte-state auditing and explicit confirmation. Its
standard Record Registry retains confirmed maps and an ordered repository
track. Each chunk state names a blob, range and SHA-256 digest; confirmation
rejects gaps, overlaps, wrong bytes, stale proposals and reused retired IDs.
The [agent guide](../../../tarav-py/src/tarav/l1/product_mapping/README.md)
documents the CLI and state contracts.

The featured Project's selected Mapping manager composes the independent
freshness suite. One stable update action follows the repository's missing or
due map. Checks do not write maps. Implementation policy measures freshness
from confirmation time, ignores working-directory edits, and prevents disabled
scans from falsely closing old findings. This is covered by
[behavioral tests](../../../tarav-py/tests/test_product_mapping.py).

The historical exercise uses an explicitly attributed Agent policy. Exact
content can carry forward; weak or ambiguous candidates receive fresh IDs, and
large edited ranges can split. Matching-byte evidence is a conservative
heuristic, not semantic proof or User review. Decisions and exact coverage audits
are retained separately. See [implementation request 946](../../../tarav-py/notes/live/946-product-mapping-impl-req.md)
and its [run report](../../../tarav-py/notes/live/product-mapping-history-2026-10-22.json).

The fixed historical run produced 127 maps across 1,257 first-parent commits,
ending at `04981e43`. The final historical state covers 1,157 regular files,
4,584 chunks and 16,161,833 bytes; two symlinks are explicitly skipped. The
installed CLI independently audited all 127 states. The Records retain 30,935
Agent decisions, including 2,344 conservative replacements of edited candidate
ranges. The run report records the actual evidence; these counts do not imply
that the User reviewed the product.

## Project-owned scope correction — 2026-10-22

The User rejected the whole-repository selection and restricted tarav-py's
mapping to committed .py files beneath src/ and tests/. File scope is ordinary
workflow configuration owned by the Project, not a Python-specific rule in the
generic mapper. The `product_mapping` section of the Project's
`.tarav/config.json` selects `include: ["src/*.py", "tests/*.py"]` and no
additional exclusions. The patterns include nested paths.
<!-- tarav.breadcrumb d22503ea4d77 -->
<!-- tarav.breadcrumb 8c281dba74c0 -->
<!-- tarav.breadcrumb 984fecb900de -->

The manager, CLI and historical runner share the Project configuration adapter.
Map records retain the effective filters so changing configuration cannot
reinterpret past coverage. The rejected broad run remains preserved separately;
the active historical run and its report are rebuilt with the narrowed scope.
See [request 947](../../../tarav-py/notes/live/947-product-mapping-project-scope-impl-req.md).

The rebuilt historical run through `04981e43` contains 127 maps. Its final
historical state contains 553 files and 1,184 chunks, with zero skipped surfaces.
Every map passed the installed CLI's exact-byte audit, and an independent Git
tree enumeration matched the final src/tests Python file set exactly. The
completion catch-up map is recorded separately in the workflow registry.
