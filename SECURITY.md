# Security Policy

## Supported versions

This repository does not publish a version support matrix or security release schedule. The `main` branch is the active development line.

## Reporting a vulnerability

Please do not publish vulnerability details in a public issue, pull request, discussion, or social post. Use GitHub's private vulnerability reporting page for this repository:

<https://github.com/Brajesh31/Book-Recommender/security/advisories/new>

If private reporting is unavailable, contact maintainer Brajesh Kumar through the [GitHub profile](https://github.com/brajesh31) and ask for a private reporting channel. Do not include exploit details or sensitive data in a public message.

Include, where possible, the affected commit or file, impact, sanitized reproduction steps, and relevant logs with secrets and personal data removed. The maintainer will investigate as time permits; there is no guaranteed response or remediation timeline. Please allow a reasonable opportunity to prepare a fix before public disclosure.

## Security-sensitive implementation notes

- `app.py` loads `popular.pkl`, `pt.pkl`, `books.pkl`, and `similarity_scores.pkl` with Python `pickle` when the module is imported. Pickle deserialization can execute code. Load only trusted artifacts from a controlled source; never accept a user-supplied pickle.
- The direct-run entry point now uses `debug=False`. Do not expose Flask's development server; use a production WSGI server such as Gunicorn with production network controls.
- The recommendation route validates blank and unknown titles and returns HTTP 400/404 feedback. Matching remains exact and case-sensitive; retain tests for malformed and boundary inputs.
- `Users.csv` contains user IDs, location, and age fields, and the rating data is linked to user IDs. Handle the source data and derived rating artifacts as potentially sensitive. Verify provenance, rights, and privacy requirements before republishing or deploying them.
- Cover images use URLs from the dataset, so requests go to external image hosts. Account for those third-party requests in privacy and deployment decisions.
- The handler no longer prints recommendation result records. Do not commit secrets, local environment files, personal dataset extracts, logs, or production data. The current app does not require an application secret for its read-only routes; add secret configuration only when a real feature needs it.

See [Deployment](docs/deployment.md) for production setup and [Database and data files](docs/database.md) for dataset handling notes.
