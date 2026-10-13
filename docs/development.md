# Development

## Project layout

- app.py contains the Flask app, artifact loading, and three route handlers.
- templates/index.html renders the popular-book list.
- templates/recommend.html renders the recommendation form and result list.
- Books.csv, Ratings.csv, and Users.csv are source datasets.
- The Jupyter notebook contains exploratory and offline model preparation work.
- popular.pkl, pt.pkl, books.pkl, and similarity_scores.pkl are generated data objects loaded by the web app.
- requirements.txt lists the current runtime packages.
- docs/ describes the application and its operation.

Large CSV, notebook, and pickle files are configured for Git LFS. Keep that configuration when changing repository attributes.

## Local workflow

1. Create and activate a virtual environment as described in installation.md.
2. Install requirements.txt and retrieve all LFS objects.
3. Run python app.py from the repository root.
4. Test the home page and submit a title known to exist in pt.index.
5. Before changing model-generation logic, inspect the notebook's data filters and artifact ordering, then regenerate the complete compatible artifact set.

There is no automated test suite or CI configuration in the repository at the time of writing. When making changes, manually check the affected browser flow and add focused automated coverage as part of substantive behavior changes.

## Implementation notes

The recommendation form submits the field user_input to POST /recommend_books. Matching is exact against pt.index. The handler assumes that a match exists, so blank or unknown titles currently raise an index error. Prefer validating input and returning a useful template message before changing or relying on this behavior.

Model artifacts are loaded with Python pickle at module import. Pickle can execute code during deserialization; only use trusted artifacts produced by a reviewed workflow. Since loading happens at import, failures occur before Flask can serve an error page.

The application expects to be launched with the repository root as its working directory because artifact paths are relative. Use a managed WSGI server for deployment and keep debug mode disabled outside local development.

## Data handling

The supplied CSVs contain user identifiers and location/age fields as well as ratings. Avoid adding personal data to logs, screenshots, issue reports, or example fixtures. Verify dataset and image rights before sharing changes that redistribute these files.
