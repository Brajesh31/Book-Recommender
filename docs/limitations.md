# ⚠️ Known Limitations

- Exact, case-sensitive title matching only.
- Unknown or blank title can raise an unhandled index error.
- No user accounts, personalization profiles, or saved preferences.
- No JSON API contract.
- No live retraining or online learning.
- Model artifacts are loaded from pickle at module import.
- Pickle files are executable serialization and require a trusted source.
- No artifact manifest or compatibility validation is currently present.
- No automated test suite is currently present.
- Notebook paths assume a Colab-like `/content/` directory.
- scikit-learn is imported by the notebook but absent from runtime requirements.
- Dependency versions are not pinned.
- Dataset and cover-image rights are not established in this repository.
- No dedicated health, readiness, metrics, or tracing endpoints exist.
- Accessibility has not been formally tested.

These limitations should be updated only after the relevant implementation and verification are complete.
