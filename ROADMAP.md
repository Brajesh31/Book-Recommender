# Roadmap

This roadmap records possible improvements for the Book Recommender. It is a planning document, not a promise of delivery dates. Priorities may change as the project evolves.

## Planned foundations

- Validate submitted titles and show a helpful message when a title is missing or is not present in the trained index.
- Load model artifacts through a controlled startup path and document that Python pickle files must only come from a trusted source.
- Make production startup settings explicit: keep Flask debug mode disabled outside local development and document the WSGI command.
- Declare and pin a reproducible dependency set, including the scikit-learn dependency used by the notebook if it remains part of the workflow.
- Replace or parameterize notebook paths that currently assume a Google Colab `/content` directory.

## Data and model improvements

- Record the source, version, license, and permitted use of the book, rating, and user datasets and the cover-image URLs before redistributing them.
- Document the training filters, popularity thresholds, collaborative-filtering inputs, and artifact regeneration steps alongside generated artifacts.
- Review whether user demographic fields are needed; avoid collecting, exposing, or logging information that is not required for recommendations.
- Add a clear model artifact compatibility/version check so stale or mismatched files fail with actionable errors.

## Product and quality improvements

- Add automated checks for the home page, recommendation form, valid title result, and invalid title handling.
- Improve accessibility, form feedback, and behavior on small screens.
- Consider a documented deployment example with resource requirements and a safe update procedure for model files.
- Evaluate recommendation quality with a repeatable offline metric and representative, properly licensed data.

## Completed in this documentation pass

- Added repository overview, setup, architecture, data, route, deployment, support, and troubleshooting documentation.
- Added contribution, security, and community conduct guidance and standard repository metadata/configuration.
