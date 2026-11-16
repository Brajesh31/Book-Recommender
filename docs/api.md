# 🌐 Application Routes and Request Contract

The application exposes three server-rendered HTML routes. It does not define a versioned JSON API, API authentication, or a formal compatibility guarantee.

## GET /

Renders the popular-books page using columns from `popular.pkl`: title, author, medium cover URL, rating count, and average rating. A missing or incompatible artifact can prevent application startup or page rendering.

## GET /recommend

Renders the recommendation form. The form includes a required title field and a visible label. It explains that matching is exact and case-sensitive.

## POST /recommend_books

Submits standard form data.

| Field | Required | Validation | Description |
|---|---|---|---|
| `user_input` | Yes | Trimmed, non-empty, maximum 200 characters in the HTML form | Exact title in the trained pivot index |

Example:

```bash
curl -X POST http://127.0.0.1:5000/recommend_books \
  --data-urlencode "user_input=EXACT TITLE FROM MODEL INDEX"
```

For a match, the handler ranks the similarity row, excludes the selected title by index, resolves metadata, and renders up to four cards.

## Status and error behavior

| Condition | Current response |
|---|---|
| Blank title | HTTP 400 with an accessible validation message |
| Unknown title | HTTP 404 with an exact-match explanation |
| Similarity row missing | HTTP 503 with a generic availability message |
| Known title | HTTP 200 with recommendation cards |
| No candidate metadata | HTTP 200 with a no-results message |

The endpoint returns HTML, not JSON. The application does not currently normalize title case or perform fuzzy matching. The browser's required/max-length attributes improve form validation, while the server also checks for blank and unknown titles.

## Operational and security notes

The four pickle artifacts are still loaded during module import. Missing or malformed artifacts can prevent startup, and untrusted pickle files can execute code. The direct-run development entry point now disables debug mode by default; production should still use Gunicorn or a managed WSGI server. See [Security](security.md) and [Deployment](deployment.md).
