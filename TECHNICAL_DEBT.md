# 🧱 Technical Debt Register

This register tracks verified or source-observed engineering debt in Bookwish. Priorities are recommendations, not delivery commitments. Close an item only after implementation and evidence.

| ID | Priority | Area | Current issue | Recommended action |
|---|---|---|---|---|
| TD-01 | Critical | Model loading | Pickle objects are loaded directly at import | Restrict artifact trust and evaluate safer serialization |
| TD-02 | High | Runtime security | Direct app execution enables Flask debug mode | Separate development and production startup |
| TD-03 | High | Request handling | Unknown or blank title can raise IndexError | Validate input and render a no-match state |
| TD-04 | High | Artifact integrity | No manifest or row-alignment validation | Add versioned manifest, checksums, and shape checks |
| TD-05 | Medium | Testing | No automated route test suite | Refactor app initialization for dependency injection |
| TD-06 | Medium | Reproducibility | Dependencies are not pinned | Select supported versions and create a lock strategy |
| TD-07 | Medium | Notebook | Data paths assume a Colab directory | Parameterize input paths |
| TD-08 | Medium | Data governance | Dataset rights and provenance are unverified | Complete a source and license register |
| TD-09 | Medium | Accessibility | Form labels and image alternatives need improvement | Implement and test accessible templates |
| TD-10 | Low | Diagnostics | Handler prints recommendation data | Use privacy-aware structured logging |

## Review process

Review this list during releases and security reviews. Add an item only with a clear impact and affected component. Link the implementation issue, owner, test evidence, and closure commit. See [the detailed technical debt guide](docs/technical-debt.md).