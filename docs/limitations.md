# ⚠️ Known Limitations

- Title matching remains exact and case-sensitive. No fuzzy matching or spelling correction exists.
- No user accounts, personalization profiles, or saved preferences.
- No JSON API contract.
- No live retraining or online learning.
- Model artifacts are loaded from pickle at module import.
- Pickle files are executable serialization and require a trusted source.
- No artifact manifest or compatibility validation is currently present.
- Automated tests cover key Flask routes with mocked artifacts and Jinja template rendering, but do not validate real model files or recommendation quality.
- Notebook paths assume a Colab-like `/content/` directory.
- scikit-learn is imported by the notebook but absent from runtime requirements.
- Dependency versions are not pinned.
- Dataset and cover-image rights are not established in this repository.
- No dedicated health, readiness, metrics, or tracing endpoints exist.
- Accessibility improvements have been added to the templates, but formal WCAG conformance has not been verified.
- No verified model-quality metrics or production performance benchmarks are published.

These limitations should be updated only after the relevant implementation and verification are complete.
