# Semantic.Router — Appendix

****

## Semantic.Router/Testability

- a `Semantic.Router` is testable by nature: a key's situation description is the test prompt, and the expected selection (a value, or `None.Is.An.Option`) is the behavior tier
- tests run through the `agentos-testground` system — isolated CLI session, chatlas trace capture, tier evaluation
- because each row already pairs a situation with its intended response, generating a test from a row is nearly mechanical
- results feed back into the router: a wrong or missed selection signals a key that is not discriminative, or a value that needs work
- untested rows are still useful as documentation; tested rows are verified routing
