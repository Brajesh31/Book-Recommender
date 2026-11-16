# 🛣️ Roadmap

This roadmap records possible improvements for Bookwish. It is a planning document, not a promise of delivery dates. Priorities may change as the project evolves.

## 🔴 Priority 1: Safety and reliability
- [x] Validate blank and unknown submitted titles; the HTML field also limits input to 200 characters.
- [x] Return a clear no-match state instead of an unhandled index error.
- [x] Disable debug mode in the direct-run entry point; production still uses WSGI.
- [ ] Validate model artifact schemas, dimensions, and pivot/similarity row alignment.
- [ ] Add a trusted artifact manifest and checksum verification.
- [x] Remove recommendation result debug prints; structured operational logging remains future work.
- [ ] Review whether pickle can be replaced with a safer data serialization format.

## 🟠 Priority 2: Reproducible model workflow
- [ ] Parameterize notebook input paths instead of hard-coding `/content/`.
- [ ] Separate runtime and training dependencies.
- [ ] Pin and lock dependencies after compatibility testing.
- [ ] Record dataset source, version, license, checksums, and permitted use.
- [ ] Record each model build's configuration and artifact checksums.
- [ ] Add repeatable offline recommendation evaluation.

## 🟡 Priority 3: Product and accessibility
- [x] Add a visible form label, validation feedback, and no-results messaging.
- [x] Add descriptive cover-image alternatives, visible focus styles, and a skip link; manual keyboard review remains.
- [ ] Measure text and control contrast.
- [ ] Add responsive and cross-browser verification.
- [ ] Consider title normalization or fuzzy matching with explicit ambiguity handling.
- [ ] Evaluate cold-start and catalog coverage limitations.

## 🟢 Priority 4: Quality and operations
- [x] Add basic Flask route and template tests using mocked model artifacts.
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
