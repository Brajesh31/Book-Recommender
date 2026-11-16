# 🧪 Testing and Quality Strategy

## 1. Current status

The pytest suite checks Jinja rendering and escaping, plus key Flask routes using mocked in-memory artifacts. The route fixture replaces pickle loading before importing `app.py`, so tests do not deserialize production model files. The tests do not verify real artifact integrity, recommendation relevance, or accessibility conformance.

## 2. Test layers

| Layer | Scope | Current state |
|---|---|---|
| Static | Python compilation | CI checks app and test syntax |
| Template | Jinja rendering and escaping | Basic pytest coverage added |
| Unit | Input validation and ranking helpers | Not implemented |
| Integration | Flask test client and route behavior | Basic route coverage with mocked artifacts |
| Artifact contract | Schema, dimensions, hashes, row alignment | Not implemented |
| Model evaluation | Precision@K, Recall@K, NDCG@K, coverage | Not implemented |
| Operations | WSGI startup, memory, readiness | Manual guidance only |
| Accessibility | Keyboard, focus, labels, contrast, screen reader | Manual checklist documented |

## 3. Run checks locally

Install runtime and development dependencies:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Run:

```bash
python -m py_compile app.py tests/test_templates.py tests/test_app.py
pytest -q
```

The quality workflow also compiles the Jinja templates and checks that key documentation and SVG assets exist.

## 4. Existing test scenarios

- Home template renders a representative popular-book card.
- Recommendation template renders a recommendation result.
- Recommendation template escapes HTML-like user-controlled text.\n- Home route renders popular-book data with mocked artifacts.\n- Recommendation form renders its visible label.\n- Blank title returns HTTP 400.\n- Unknown title returns HTTP 404.\n- Known title returns similar-book cards without returning the selected title.

## 5. Additional route and model tests to add

Further tests should cover:
- `GET /` renders the popular-books list.
- `GET /recommend` renders the form.
- valid `POST /recommend_books` returns result cards.
- empty title returns validation feedback.
- unknown title returns no-match feedback, not an exception.
- missing or incompatible artifacts fail with an actionable startup error.
- no raw stack trace is shown to visitors.

## 6. Artifact contract tests

Before deployment, verify that expected files exist and are real Git LFS objects; the popularity table has required columns; the pivot table has a title index; the similarity matrix is two-dimensional; matrix row count equals `len(pt.index)`; values are finite; metadata resolves for candidates; and all artifacts share one build manifest.

Only load pickle files from a trusted source. Do not execute artifact validation against untrusted pickle input.

## 7. Accessibility and security checks

Add browser-level checks for keyboard navigation, visible focus, labels, error announcements, contrast, zoom, and screen-reader behavior. Add dependency and secret scanning. Automated checks complement, but do not replace, manual review.

## 8. Evidence format

For each release, record commit SHA, Python version, platform, dependency install result, commands executed, route results, artifact manifest/checksum results, model evaluation protocol, accessibility review, failures, and skipped checks. Never mark an unexecuted check as passed.
