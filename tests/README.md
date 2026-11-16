# 🧪 Template Tests

The current test suite intentionally avoids importing `app.py`, because module import deserializes the production pickle artifacts. Tests create a Jinja environment directly and exercise the two checked-in HTML templates.

## Run

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
pytest -q
```

## Coverage
- Popular books template renders representative data.
- Recommendation template renders a result card.
- Jinja autoescaping protects HTML-like title text.

## Current exclusions
These tests do not validate Flask route behavior, model artifact integrity, recommendation quality, deployment startup, or WCAG conformance. Add those tests after application initialization and model loading are separated so trusted test fixtures can be injected safely.
