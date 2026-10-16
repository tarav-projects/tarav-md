****

## Unassigned/Agendix/Candidate.Chatlas.Output.Contract

- [DF] the `Chatlas.Output.Contract` is the CLI-wide rule that every command builds a JSON-like payload internally and renders it for human reading on output ^c20260803-39u
- [DC] `--json` prints the raw payload and `--text` is the default; every leaf command carries both ^c20260803-40u
- [RJ] a single `--output-mode <value>` flag is rejected for the common modes in favour of explicit flags ^c20260803-41u
- [RJ] `--human` is rejected as a flag name — it does not tell a reader who wrote anything in a chat ^c20260803-42u
