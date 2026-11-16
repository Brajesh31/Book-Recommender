# 🛣️ Roadmap

This roadmap records possible improvements for Bookwish. It is a planning document, not a promise of delivery dates. Priorities may change as the project evolves.

## 🔴 Priority 1: Safety and reliability
- [ ] Validate blank, oversized, and unknown submitted titles.
- [ ] Return a clear no-match state instead of an unhandled index error.
- [ ] Remove debug mode from production startup paths.
- [ ] Validate model artifact schemas, dimensions, and pivot/similarity row alignment.
- [ ] Add a trusted artifact manifest and checksum verification.
- [ ] Replace debug prints with privacy-aware structured logging.
- [ ] Review whether pickle can be replaced with a safer data serialization format.

## 🟠 Priority 2: Reproducible model workflow
- [ ] Parameterize notebook input paths instead of hard-coding `/content/`.
- [ ] Separate runtime and training dependencies.
- [ ] Pin and lock dependencies after compatibility testing.
- [ ] Record dataset source, version, license, checksums, and permitted use.
- [ ] Record each model build's configuration and artifact checksums.
- [ ] Add repeatable offline recommendation evaluation.

## 🟡 Priority 3: Product and accessibility
- [ ] Add useful form labels, validation feedback, and no-results messaging.
- [ ] Improve image alternatives, focus visibility, and keyboard usability.
- [ ] Measure text and control contrast.
- [ ] Add responsive and cross-browser verification.
- [ ] Consider title normalization or fuzzy matching with explicit ambiguity handling.
- [ ] Evaluate cold-start and catalog coverage limitations.

## 🟢 Priority 4: Quality and operations
- [ ] Add unit and Flask route tests.
- [ ] Add artifact-contract tests.
- [ ] Add browser-level accessibility tests.
- [ ] Add health/readiness checks only after defining safe semantics.
- [ ] Define monitoring, backup, and rollback procedures for a real deployment.

## ✅ Documentation and repository foundation
- [x] Expanded README and documentation index.
- [x] Added project-specific model, data, security, privacy, accessibility, testing, and operations guides.
- [x] Added Mermaid source diagrams and SVG visual assets.
- [x] Added GitHub issue forms, pull request template, Dependabot, and quality/security workflows.
- [x] Added reusable engineering and release templates.

## 📌 Prioritization rule
Close a roadmap item only after implementation, tests, documentation, and verification evidence are available. A documentation description does not mean the underlying product feature exists.
