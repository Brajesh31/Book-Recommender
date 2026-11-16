# 🧱 Technical Debt Register

This register tracks verified or source-observed engineering debt in Bookwish. Priorities are recommendations, not delivery commitments. Close an item only after implementation and evidence.

| ID | Priority | Area | Current issue | Recommended action |
|---|---|---|---|---|
| TD-01 | Critical | Model loading | Pickle objects are loaded directly at import | Restrict artifact trust and evaluate safer serialization |
| TD-02 | Resolved | Runtime security | Direct app execution previously enabled debug mode | Direct-run entry point now sets debug=False; retain WSGI deployment for production |
| TD-03 | Resolved | Request handling | Unknown or blank title previously raised IndexError | Server now validates blank, oversized, and unknown titles with HTTP 400/404 feedback |
| TD-04 | High | Artifact integrity | No manifest or row-alignment validation | Add versioned manifest, checksums, and shape checks |
| TD-05 | Partially resolved | Testing | Basic route tests use mocked artifacts; artifact contract and model tests remain absent | Expand test coverage for real artifact validation and recommendation quality |
| TD-06 | Medium | Reproducibility | Dependencies are not pinned | Select supported versions and create a lock strategy |
| TD-07 | Medium | Notebook | Data paths assume a Colab directory | Parameterize input paths |
| TD-08 | Medium | Data governance | Dataset rights and provenance are unverified | Complete a source and license register |
| TD-09 | Partially resolved | Accessibility | Labels, skip links, focus styles, and descriptive image alternatives added; contrast and assistive-tech testing remain | Complete manual WCAG-oriented review and record evidence |
| TD-10 | Resolved | Diagnostics | Recommendation handler previously printed result records | Debug print removed; define structured logging if operational needs require it |

## Review process

Review this list during releases and security reviews. Add an item only with a clear impact and affected component. Link the implementation issue, owner, test evidence, and closure commit. See [the detailed technical debt guide](docs/technical-debt.md).