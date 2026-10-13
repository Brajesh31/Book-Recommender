# Architecture

## System overview

Book Recommender is a server-rendered Flask application. It reads precomputed Python pickle artifacts from the repository root when app.py is imported, uses in-memory pandas and NumPy objects to answer requests, and renders HTML from templates. The checked-in Jupyter notebook and CSV datasets document the offline data-preparation workflow. There is no database, authentication service, separate API service, or background worker.

~~~text
Books.csv + Ratings.csv + Users.csv
             |
             v
  Jupyter training/analysis notebook
             |
             v
popular.pkl + pt.pkl + books.pkl + similarity_scores.pkl
             |
             v
Flask app.py -> index.html / recommend.html -> browser
~~~

## Data preparation

The notebook loads book metadata and ratings, applies filtering and aggregation, then generates the objects consumed by the app. The popular-books view is based on titles with at least 250 ratings and selects a limited top list. The collaborative filtering preparation filters users with more than 200 ratings and titles with at least 50 ratings, creates a user-title pivot table, fills missing ratings with zero, and calculates cosine similarity. These thresholds describe the current notebook; changing them requires regenerating compatible artifacts.

The CSV files are source data. The pickle files are derived runtime artifacts. Their index ordering and row ordering must remain aligned: app.py finds a title's position in pt.index and uses that integer to select the same row of similarity_scores.

## Request flow

- GET / renders the popular list using columns from popular.pkl.
- GET /recommend renders the recommendation form.
- POST /recommend_books reads the form field user_input, looks for an exact match in pt.index, ranks that row's similarity scores, skips the matching title, and renders up to four similar books using books.pkl metadata.

The routes return HTML templates; they do not return a documented JSON API. A missing or unknown title currently produces an unhandled index lookup error. The app also prints recommendation data to standard output.

## Runtime and constraints

All four pickle files are loaded when the module is imported, so a missing, incompatible, or untrusted artifact can prevent startup or execute unsafe deserialization code. Keep the files from one trusted training run together. The app expects the working directory to contain the artifacts and templates. The displayed cover images use remote URLs from the book metadata; image availability and third-party hosting are outside this app's control.

The current application has no explicit persistence layer or user accounts. Do not treat transient form submissions as stored preferences. Review the supplied dataset's provenance, license, privacy terms, and image rights before redistribution or public deployment.
