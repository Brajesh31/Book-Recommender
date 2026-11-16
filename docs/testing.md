# 🧪 Testing and Quality Strategy

## 1. Current status

The repository does not currently include a test directory or a declared test command. The application can be syntax-checked, but that alone does not verify route behavior, templates, artifact compatibility, or recommendation quality.

## 2. Test layers to add

| Layer | Scope | Example checks |
|---|---|---|
| Static | Python source | Compilation, lint, dependency checks |
| Unit | Input and ranking helpers | Blank title, exact match, no match, score ordering |
| Integration | Flask test client | Home, form page, POST success, POST error |
| Template | Jinja rendering | Escaping, missing images, accessible labels |
| Artifact contract | Pickle objects | Required columns, row counts, dimensions, alignment |
| Model evaluation | Offline recommender | Precision@K, Recall@K, NDCG@K, coverage |
| Operations | Deployment | WSGI startup, worker memory, model availability |
| Accessibility | Browser flow | Keyboard, focus, labels, contrast, screen reader |

## 3. Immediate smoke checks

Run from the project root after installing dependencies and retrieving Git LFS objects:

```bash
python -m py_compile app.py
python -c "import flask, numpy, pandas; print('runtime imports ok')"
```

These checks do not execute a valid recommendation request or validate untrusted artifacts. Only import the app after confirming pickle files are trusted.

## 4. Flask test scenarios

After refactoring app initialization to permit injected test artifacts, cover:
- `GET /` renders the popular-books list.
- `GET /recommend` renders the form.
- valid `POST /recommend_books` returns result cards.
- empty title returns validation feedback.
- unknown title returns no-match feedback, not an exception.
- malformed metadata rows do not crash template rendering.
- missing or incompatible model artifacts fail with an actionable startup error.
- no raw stack trace is shown to visitors.

## 5. Model artifact contract checks

Before deployment, assert:
- the expected files exist and are not Git LFS pointer text,
- the popularity table contains required columns,
- the pivot table has a title index,
- the similarity matrix is two-dimensional,
- matrix row count equals `len(pt.index)`,
- all values are finite and valid for sorting,
- title metadata can be resolved for selected candidates,
- all artifacts share one build manifest.

## 6. Dependency and security checks

A CI workflow should install the declared dependencies, compile Python files, compile Jinja templates, and scan for accidentally committed secrets. Add dependency vulnerability scanning and a lockfile once a supported dependency policy is selected.

## 7. Test evidence format

For each release, record:
- commit SHA,
- Python version and platform,
- dependency installation result,
- commands executed,
- route test results,
- artifact manifest/checksum results,
- model evaluation protocol and results if relevant,
- known failures and skipped checks.

Do not represent a check as passing unless it was actually run.
