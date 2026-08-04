****

## Normalization.Pipeline::Chatlas.Session.Model/Agendix

- [DC] harness versions are usable as the raw model version here — codex stamps `cli_version` in `session_meta`, claude stamps `version` per record — and every existing normalizer is to be fenced with a version compatibility test ^c20260728-36u
- [CT] version checking is loud but not fatal on its own: an unrecognized release is validated before it is trusted, and only a validation failure is a hard POI ^c20260728-29u
- [PR] the archive is what makes the capability accumulate — the reach of raw-model mapping grows as `Raw.Archive` collects more versions, so archive and versioner are worth only as much as each other ^c20260728-51u
