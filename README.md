# Book Recommendation System

This repository contains a small Flask website for browsing popular books and finding similar titles from a precomputed item-similarity model. The templates brand the site **Bookwish**. The model and app use the supplied book and rating data; there is no user account system or database.

> **Project status:** this is a learning/demo application. Recommendations require an exact book-title match, the app runs Flask's debug server when started directly, and the model artifacts are loaded with Python pickle. Review [Current behavior and limitations](#current-behavior-and-limitations) and [SECURITY.md](SECURITY.md) before exposing it publicly.

## Contents

- [How it works](#how-it-works)
- [Requirements](#requirements)
- [Get the data and install](#get-the-data-and-install)
- [Run locally](#run-locally)
- [Routes](#routes)
- [Model notebook](#model-notebook)
- [Current behavior and limitations](#current-behavior-and-limitations)
- [Data and privacy](#data-and-privacy)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## How it works

- The home page displays the 50 books in `popular.pkl`, with author, cover URL, rating count, and mean rating.
- The recommendation form accepts a book title. The app looks up that exact title in `pt.pkl`, ranks cosine-similarity scores, skips the selected title, and displays up to four similar books.
- `books.pkl`, `pt.pkl`, `popular.pkl`, and `similarity_scores.pkl` are precomputed artifacts loaded when `app.py` starts.

The training notebook builds the popularity table and a user-rating pivot matrix. It filters to users with more than 200 ratings and books with at least 50 ratings, fills missing ratings with zero, and calculates cosine similarity between books. The popularity list filters to titles with at least 250 ratings and keeps the top 50 by average rating.

## Requirements

- Python 3 and pip.
- Git LFS to retrieve the large CSV, notebook, and pickle files tracked by `.gitattributes`.
- For rerunning the notebook: Jupyter and scikit-learn in addition to the packages in `requirements.txt`. `scikit-learn` is used by the notebook but is not currently listed in that file.

## Get the data and install

Clone the repository with Git LFS available, then ensure the LFS objects are downloaded:

```powershell
git lfs install
git clone https://github.com/Brajesh31/Book-Recommender.git
Set-Location Book-Recommender
git lfs pull
```

Create and activate a virtual environment, then install the web app dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

On macOS/Linux, activate the environment with `source .venv/bin/activate` instead. `requirements.txt` currently leaves package versions unpinned, so installs are not guaranteed to be reproducible over time.

The app expects these four pickle files in the current working directory: `popular.pkl`, `pt.pkl`, `books.pkl`, and `similarity_scores.pkl`. Keep the CSV datasets in the repository root if you plan to rerun the notebook.

## Run locally

From the repository root with the virtual environment active:

```powershell
python app.py
```

Open <http://127.0.0.1:5000>. The direct-run path enables Flask debug mode; use it only on a local development machine. See [Deployment](docs/deployment.md) for a WSGI server setup.

## Routes

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/` | Render the top-50 popular books page. |
| `GET` | `/recommend` | Render the book-title recommendation form. |
| `POST` | `/recommend_books` | Find similar titles for the submitted exact book name and render them. |

See [HTTP routes](docs/api.md) for request fields and current error behavior.

## Model notebook

`book_recommendation_model.ipynb` documents the dataset exploration, popularity ranking, rating pivot, cosine similarity, and pickle export. It currently reads CSVs from `/content/`, which is a Google Colab-style path; change those paths for a local Jupyter environment. The notebook also imports scikit-learn, which is not in `requirements.txt`.

The web app consumes the committed pickle artifacts and does not retrain the model at startup. Treat pickle files as trusted executable serialization: only load artifacts from a source you control.

## Current behavior and limitations

- Recommendation lookup is an exact, case-sensitive book-title lookup. A missing or unknown title currently causes an indexing error rather than a friendly validation message.
- The model is item-based and precomputed. It does not personalize results from a current visitor's account or preferences.
- The app uses the development Flask server with `debug=True` when run through `python app.py`; do not use that server for production.
- The app does not validate the pickle artifacts at startup and loads all of them into memory when the module is imported.
- There is no automated test suite or test command in the repository.
- The CSV data, derived artifacts, and cover-image URLs have no provenance or separate license documentation in this repository. Confirm rights and privacy requirements before redistributing or deploying them.

## Data and privacy

The repository includes `Books.csv`, `Ratings.csv`, and `Users.csv`. Their columns include book metadata and cover-image URLs, user IDs and ratings, and user location/age fields. The notebook loads the users table for exploration but the current recommendation calculation uses the ratings and books tables. Handle these files and the derived user-rating matrix as potentially sensitive data; do not publish additional personal data or expose the artifacts through an untrusted pickle source.

Book covers are loaded from URLs in the dataset, so visitors' browsers contact those image hosts. See [Security](SECURITY.md) and [Database and data files](docs/database.md) for handling notes.

## Documentation

- [Architecture](docs/architecture.md)
- [Installation](docs/installation.md)
- [Development](docs/development.md)
- [Deployment](docs/deployment.md)
- [HTTP routes](docs/api.md)
- [Database and data files](docs/database.md)
- [Troubleshooting](docs/troubleshooting.md)
- [FAQ](docs/faq.md)

## Contributing

Bug reports and focused improvements are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Report suspected vulnerabilities privately using [SECURITY.md](SECURITY.md), not in a public issue.

## License

The project source is provided under the MIT License; see [LICENSE](LICENSE). Dataset, model artifact, and book-cover rights may be separate and must be checked with their respective sources.

Last updated: 2026-10-24 05:26 UTC
