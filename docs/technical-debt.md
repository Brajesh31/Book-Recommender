# 🧱 Technical Debt Register

This register captures visible engineering work. Priorities are recommendations, not a claim that work has been scheduled.

| ID | Priority | Debt | Impact | Suggested next step |
|---|---|---|---|---|
| TD-01 | Critical | Direct pickle loading | Arbitrary code risk if artifacts are untrusted | Trusted artifact pipeline and safer format evaluation |
| TD-02 | High | Debug enabled in direct entry point | Unsafe if exposed | Separate dev and production startup |
| TD-03 | High | Unvalidated title lookup | User input can crash request | Validate and handle no-match |
| TD-04 | High | No artifact contract checks | Incompatible files may misbehave | Manifest, schema and alignment checks |
| TD-05 | Medium | No tests | Regressions are not caught automatically | Add testable app factory and route tests |
| TD-06 | Medium | Unpinned requirements | Non-reproducible environment | Pin and lock dependencies |
| TD-07 | Medium | Notebook hard-coded paths | Local retraining friction | Parameterize data paths |
| TD-08 | Medium | No provenance register | Rights and privacy unclear | Complete dataset register |
| TD-09 | Medium | Basic accessibility gaps | Barriers for some visitors | Labels, alt text, focus and contrast checks |
| TD-10 | Low | Print-based diagnostics | Noisy or potentially sensitive output | Structured privacy-aware logging |

Review this register during releases and close items only with evidence.
