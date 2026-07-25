****

## Agentos.Bloberia/Agendix/Candidate.Skw.Edition.History

- [DF] `Skw.Edition.History` is an `Agentos.Bloberia` application collecting metadata for every discoverable chat session that edited a configured managed source file. ^c20260724-32u
- [CT] edition-session membership is orthogonal to touch: an editing session may or may not carry touch support for the file. ^c20260724-33u
- [DC] historical recovery searches full Git file history and Chatlas for all editor chats it can find. ^c20260724-34u
- [DC] edition history retains the chat session start date as a temporal reference. ^c20260724-35u
- [DC] the initial linter floor requires at least one edition-session association for each configured target. ^c20260724-36u

****

## Agentos.Bloberia/Agendix/Candidate.Anchory.Relationship

- [DF] `Anchory.System` and `Agentos.Bloberia` organize flexible application-owned cargo around different access primitives: an embeddable anchor string and a query-selected record. ^c20260724-37u
- [FR] how `Anchory.System` and `Agentos.Bloberia` integrate remains open. ^c20260724-38u
