# Contributing

Thanks for helping improve Book Recommendation System. Keep changes focused, describe what visitors or maintainers gain, and document behavior that changes.

## Before you start

1. Search existing repository issues for a related report or request. Discuss substantial changes before investing in a new feature.
2. Review [Current behavior and limitations](README.md#current-behavior-and-limitations) so an existing placeholder or input limitation is not mistaken for a finished workflow.
3. Verify the source and redistribution rights for datasets, derived model files, and book-cover images before adding or republishing them. See [Database and data files](docs/database.md).
4. For a suspected security vulnerability, do not open a public issue. Follow [SECURITY.md](SECURITY.md).

## Development setup

Follow [Installation](docs/installation.md) to create a virtual environment, install requirements, and obtain the Git LFS-managed files. The recommender expects its pickle files in the repository root. The notebook currently uses a Colab `/content/` path and requires scikit-learn, which is not listed in `requirements.txt`.

Create a focused branch, for example:

```text
feature/friendly-unknown-book-error
fix/production-debug-mode
docs/dataset-provenance
```

## Implementation guidance

- Keep request handling in `app.py` and rendering in the Jinja templates under `templates/` unless a larger application structure is introduced deliberately.
- Validate form input and handle missing or unknown book titles with a useful response rather than an uncaught exception.
- Do not enable Flask debug mode in a deployed environment. Use a production WSGI server and keep its process configuration outside the development entry point.
- Treat CSV data and image URLs as externally sourced input. Avoid exposing user-level data in pages, logs, or error responses.
- Only load pickle artifacts produced by a trusted, reviewed process. Pickle deserialization can execute code; do not accept user-provided model files.
- If regenerating the model, record the data source/version, filtering rules, dependency versions, and commands. Update related artifacts as a coherent change and verify the expected files are synchronized.
- Preserve the Git LFS attributes for the large CSV, notebook, and pickle files. Avoid committing virtual environments, temporary notebook outputs, or unrelated large files.
- Keep `requirements.txt` aligned with actual application and notebook dependencies, and prefer reviewed/pinned versions for reproducible environments.
- Update routes, installation, privacy, and deployment docs when behavior changes.

## Verification

The repository currently has no automated test suite or test command. For a change, at minimum inspect the relevant Flask route/template and run the app locally with representative valid and invalid book titles. If you add automated tests, include the test dependency and documented command.

The app can be syntax-checked with `python -m py_compile app.py`; this command does not verify template rendering, model artifacts, or route behavior. State what you checked in the pull request.

## Pull requests

Include:

- The problem and expected behavior.
- A summary of code, data, and model changes.
- Any route, dependency, input, privacy, or deployment impact.
- Checks run and their results.
- Screenshots for visible template changes.
- Dataset/model provenance and rights information if files or training inputs changed.

Keep each change focused and respond to review feedback. `CODEOWNERS` identifies the repository review owner.

## Commit messages

Use a short imperative summary, optionally with a conventional prefix, such as `fix: handle unknown book titles` or `docs: document model inputs`.

## License

By contributing, you agree that your contribution is submitted under the project's [MIT License](LICENSE). This project license does not automatically relicense third-party datasets or images.
