****

## Chatlas.Anchory/Line.Anchor.Dossier

- [DF] `Chatlas.Line.Anchor.Dossier` is the Chatlas-owned record resolved from an `Index.Line.Anchor`, relating its attached line to evidence and assertions on Chat surfaces ^c20260809-116u
- [DC] its schema organizes one attachment guard and independently modeled relationship namespaces ^c20260809-117u
- [DC] `attachment` stores a canonicalization schema and hash of the current `Line.Type + body + Anchor.Id` triplet ^c20260809-118u
- [CT] the attachment guard detects unmaintained drift without duplicating the line’s type or body in the dossier ^c20260809-119u
- [DC] `support`, `gates`, and `provenance` are independent relationship namespaces ^c20260809-120u
- [DC] each namespace owns its relationship shape, referenced coordinates, and validation semantics ^c20260809-121u
- [CT] the same `Normal.Turn.Ref` may occur in several namespaces when each occurrence asserts a different relationship ^c20260809-122u
- [CT] the dossier stores the references and assertions needed to evaluate relationships, not conclusions derived from them ^c20260809-123u
- [RJ] human hints, copied Index content, Line.Type fields, and derived standing do not belong in the dossier ^c20260809-124u
- [FR] Chatlas may add independently modeled relationship namespaces without changing the identity of the attached anchor ^c20260809-125u
- [DF] `app` identifies Chatlas as the application owning the dossier semantics ^c20260809-147u
- [DF] `schema` identifies the versioned `Chatlas.Line.Anchor.Dossier` contract ^c20260809-148u
- [DF] `attachment` carries the canonical triplet-hash assertion ^c20260809-149u
- [DF] `relationships` contains independently modeled relationship namespaces ^c20260809-150u
- [DF] `relationships.support` carries the line’s `Chat.Support.Set` ^c20260809-151u
- [DF] `relationships.gates` carries mechanism-owned `Chat.Gate.Relationship`s ^c20260809-152u
- [DF] `relationships.provenance` carries `Chat.Provenance.Relationship`s ^c20260809-153u

****

## Chatlas.Anchory/Line.Anchor.Resolution

- [DF] `Chatlas.Line.Anchor.Resolution` evaluates a `Chatlas.Line.Anchor.Dossier` against its attached Index line and referenced Chat surfaces ^c20260809-137u
- [DC] resolution verifies the attachment assertion against the current line triplet and resolves each relationship namespace according to its own contract ^c20260809-138u
- [CT] the Index surface remains authoritative for the line triplet and the Chat surfaces remain authoritative for referenced events and turns ^c20260809-139u
- [DC] line drift, grounding standing, gate satisfaction, provenance standing, `Line.Home`, and materialization placement are derived from the dossier and their authoritative surfaces ^c20260809-140u
- [CT] derived conclusions are not persisted as dossier fields ^c20260809-141u
- [CT] a resolution finding does not itself mutate the anchor, its dossier, or any referenced surface ^c20260809-142u
- [PR] the dossier preserves cross-surface coordinates and assertions while stable surfaces preserve the facts they address ^c20260809-143u
