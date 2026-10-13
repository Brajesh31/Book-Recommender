# Frequently asked questions

## What does this project do?

It displays a ranked popular-books list and offers a form that recommends similar titles from precomputed book-rating similarity data.

## Does it use a database?

No. The Flask app loads pickle artifacts into memory. The CSV files and notebook are used for offline data preparation; there is no database connection or user profile store.

## How do I run it?

Install Git LFS, clone the repository and retrieve its LFS files, create a Python virtual environment, install requirements.txt, then run python app.py from the project root. See installation.md for commands by operating system.

## Why does my title fail?

The current implementation requires an exact title match in the trained index. Blank input or a title with different punctuation or spacing may fail. Input validation is a known improvement area.

## Can I regenerate the recommendation model?

The repository includes a notebook describing the data-preparation workflow. It assumes Colab-style /content paths and imports scikit-learn, which is absent from requirements.txt. Adjust the paths and install notebook dependencies before running it. Preserve the alignment between the pivot-table index and similarity-score rows.

## Is the dataset covered by the MIT license?

The MIT license in this repository applies to the project's source code as stated in LICENSE. It does not establish permissions for the supplied datasets, user information, or third-party cover images. Check their provenance and terms before redistribution or deployment.

## Is the development server suitable for production?

No. python app.py enables Flask debug mode. Use a production WSGI server such as Gunicorn with debug disabled, and configure the host's process, resource, and network settings.

## Does the app read environment variables?

No runtime environment variables are currently read. .env.example documents that fact and does not contain credentials or sample secrets.

## Where should I report a defect or security concern?

Use the repository's GitHub Issues page for ordinary reproducible bugs and feature requests. Follow SECURITY.md for suspected vulnerabilities and do not disclose them in a public issue.
