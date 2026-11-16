# 🤝 Contributing to Book Recommendation System

Thank you for considering a contribution to Bookwish. This project is a Flask-based educational book recommendation demo with an offline collaborative-filtering notebook and precomputed pickle artifacts. Contributions should improve correctness, usability, reproducibility, safety, or maintainability without overstating what the application currently does.

## 🧭 Before opening a change

1. Search existing issues and pull requests for related work.
2. Read the [README](README.md), [project limitations](docs/limitations.md), and relevant guide under [docs](docs/README.md).
3. For data or model changes, verify provenance, license, privacy requirements, and artifact compatibility first.
4. For security vulnerabilities, do not create a public issue. Follow [SECURITY.md](SECURITY.md).
5. For behavior-changing proposals, describe the problem and acceptance criteria before implementing a broad redesign.

## 🧰 Development environment

The project uses Python, Flask, NumPy, pandas, Jinja templates, and Git LFS-managed data/model files.

```bash
git lfs install
git clone https://github.com/Brajesh31/Book-Recommender.git
cd Book-Recommender
git lfs pull
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

On Windows, create the environment with `py -m venv .venv` and activate it using `.venv\\Scripts\\Activate.ps1`.

The notebook currently assumes a Colab-style `/content/` path and imports scikit-learn, which is not declared in the runtime requirements. Adjust notebook paths and install training dependencies in an isolated environment before retraining.

## 🧱 Branch and change conventions

Use a focused branch name, for example:

```text
feature/friendly-unknown-book-error
fix/production-debug-mode
docs/dataset-provenance
test/template-accessibility
```

Keep changes scoped. Avoid mixing unrelated application refactors, dataset replacements, and documentation-only updates in one pull request.

## 💻 Implementation guidance

- Keep Flask route behavior and template responsibilities clear.
- Validate submitted titles and handle missing/unknown values safely.
- Do not expose Flask debug mode outside local development.
- Treat visitor input, CSV values, image URLs, and model artifacts as untrusted until validated.
- Never load pickle files from an untrusted source. Deserialization can execute code.
- Regenerate all related artifacts together and preserve pivot/similarity row alignment.
- Record dataset identity, source revision, filters, dependency versions, checksums, and model evaluation when rebuilding.
- Preserve Git LFS configuration for large CSV, notebook, and pickle files.
- Avoid committing virtual environments, local data copies, notebook scratch outputs, secrets, or user-level records.
- Update diagrams and docs when routes, data, artifacts, configuration, or deployment behavior changes.
- Add useful docstrings and comments where they clarify non-obvious behavior. Avoid comments that merely restate a line of code.

## 🧪 Verification

Install development dependencies and run:

```bash
python -m py_compile app.py tests/test_templates.py
pytest -q
```

The current pytest suite covers Jinja rendering and HTML escaping only. It does not import the Flask application or validate the pickle artifacts. Route and model tests should be added as the app is refactored for safe test initialization.

State exactly which commands were run and whether they passed. A syntax check is not proof that the full application works.

## 📚 Documentation and visuals

For a meaningful change:
- update README when user-visible behavior changes,
- update the relevant detailed guide under `docs/`,
- update Mermaid source and SVG visuals if architecture or workflow changes,
- update the project structure guide when files or directories change,
- update CHANGELOG and ROADMAP when appropriate,
- use templates under `docs/templates/` for significant decisions, tests, incidents, data registers, or releases.

Do not add empty placeholder docs, fabricated screenshots, fake badges, imaginary APIs, or unverified performance claims.

## 🔐 Data, privacy, and security

The source CSV files include user IDs, location, age, and rating data. Avoid placing personal records in issues, screenshots, test fixtures, or logs. The repository does not establish the dataset or cover-image licenses. The MIT source license does not automatically cover those materials.

## 🔍 Pull request requirements

Use the repository pull request template. Include:
- problem and expected behavior,
- implementation summary,
- affected routes, templates, data, and artifacts,
- security/privacy/accessibility implications,
- tests and commands actually run,
- screenshots or diagrams for visible changes,
- dataset provenance and rights evidence if data changed,
- known limitations and follow-up work.

## 🧾 Commit messages

Use concise imperative messages, optionally with a conventional prefix:

- `fix: handle unknown book titles`
- `docs: document model artifact contract`
- `test: cover recommendation template rendering`

## 📄 License

By contributing, you agree that your contribution is submitted under the repository's [MIT License](LICENSE). That source-code license does not automatically relicense third-party datasets, ratings, or cover images.
