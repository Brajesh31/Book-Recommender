# Application routes

The current project exposes HTML pages through Flask. It does not define a versioned JSON API, API authentication, or a formal compatibility guarantee.

## GET /

Renders the popular-books page from popular.pkl. The template receives book titles, authors, medium cover image URLs, rating counts, and average ratings. This route requires a valid popular.pkl with the expected columns.

## GET /recommend

Renders the recommendation form. The route does not currently provide a JSON response or populate a server-side list of valid title values.

## POST /recommend_books

Submits the recommendation form as standard form data.

| Field | Required by current handler | Description |
| --- | --- | --- |
| user_input | Yes in practice | Exact book title to look up in the collaborative-filtering index |

Example form request:

~~~sh
curl -X POST http://127.0.0.1:5000/recommend_books \
  --data-urlencode "user_input=The title as indexed"
~~~

When the title matches pt.index, the handler ranks its similarity-score row, skips the input title, selects up to four results, looks up each result's title, author, and image in books.pkl, and renders recommend.html with the data. Results are server-rendered HTML, not JSON.

## Current error behavior

The handler does not validate blank or unknown titles before indexing the match array. Such input can raise an IndexError and produce a server error. Missing or malformed pickle artifacts can also prevent the application from starting. A future behavior change should return a user-friendly validation message and document any API contract before adding non-browser clients.

## Operational notes

The app currently prints recommendation data to standard output. Do not send personal or confidential information in submitted titles, and review logging before operating the service publicly.
