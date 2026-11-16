# 📖 Product and System Overview

## 1. What this project does

Book Recommender is a small server-rendered Flask application. Its templates use the product name **Bookwish**. The home page displays a precomputed popular-books list. A visitor can submit a book title and receive up to four similar titles from a precomputed item-item similarity matrix.

The application is intentionally simple: model preparation happens offline in a notebook, while web requests read in-memory Python objects created from pickle files.

## 2. User-facing capabilities

| Capability | Current implementation | Important boundary |
|---|---|---|
| Popular books page | Renders rows from `popular.pkl` | Expects the model's existing columns |
| Similar-title form | POSTs `user_input` | Exact title lookup, no fuzzy search |
| Similar-title results | Ranks one similarity-score row | Up to four items, title/author/image only |
| Model training | Jupyter notebook | Not run during a web request |
| User profiles | Not implemented | No login or persisted preferences |
| JSON API | Not implemented | Routes return HTML |
| Database | Not implemented | Files and memory only |

## 3. Main actors

- **Visitor:** views popular titles and submits a title.
- **Maintainer:** manages code, dataset provenance, model artifacts, and deployment.
- **Offline model workflow:** reads the source CSV files, applies notebook filters, and exports pickle artifacts.
- **Web process:** loads artifacts at startup and serves rendered HTML.

## 4. Application lifecycle

1. A deployment obtains the Python code, templates, and complete Git LFS objects.
2. The WSGI process imports `app.py`.
3. The module loads four pickle artifacts into memory.
4. Flask dispatches a request to one of three routes.
5. The route reads the relevant in-memory object and renders a Jinja template.
6. The browser renders the page and requests remote book-cover URLs where present.

See [architecture](architecture.md) and the [pipeline diagram](diagrams/recommendation-pipeline.mmd).

## 5. Recommendation method at a glance

The notebook constructs a user-by-book rating pivot table after filtering users and titles by activity. Missing cells are filled with zero, and cosine similarity is computed between book vectors. At inference time, the web app uses the title's pivot-table row position to retrieve the matching similarity-score row.

This is item-based collaborative filtering, not a language model, semantic embedding search, or individualized profile system.

## 6. Known constraints and risks

- Matching is case-sensitive and exact.
- Empty and unknown titles currently reach an unsafe array index operation.
- All four pickle files load during module import.
- Pickle is executable serialization and must be trusted.
- Direct execution enables Flask debug mode.
- Model artifact order must remain aligned with the pivot-table index.
- Dataset provenance, license, consent, and image rights are not established by this repository.
- No automated tests are currently shipped.

## 7. Success criteria for future improvements

A production-ready iteration should have predictable invalid-input behavior, reproducible model builds, validated artifact compatibility, automated route tests, documented data rights, a secure WSGI deployment, accessible templates, and operational checks. These are targets, not claims about the current implementation.
