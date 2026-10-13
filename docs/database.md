# Data and persistence

## Database status

This project does not connect to a relational database or a database service. It has no schema migrations, ORM models, or persistent account/preference storage. Flask reads static CSV inputs in the offline notebook workflow and reads derived pickle files in the running web app.

## Supplied CSV inputs

The checked-in CSV datasets describe the training inputs. Their current columns are:

| File | Fields | Role |
| --- | --- | --- |
| Books.csv | ISBN, Book-Title, Book-Author, Year-Of-Publication, Publisher, Image-URL-S, Image-URL-M, Image-URL-L | Book metadata and external cover-image links |
| Ratings.csv | User-ID, ISBN, Book-Rating | User-to-book ratings used for collaborative filtering |
| Users.csv | User-ID, Location, Age | User attributes included in the source dataset |

The notebook filters and aggregates these records to produce the popular-books list and user-title rating matrix. The running Flask app does not query these CSV files for each request.

## Runtime artifacts

| Artifact | Runtime use |
| --- | --- |
| popular.pkl | Popular-book metadata and aggregate rating fields for the home page |
| pt.pkl | Indexed title-to-user rating pivot table used to locate an input title |
| books.pkl | Book metadata used to build recommendation cards |
| similarity_scores.pkl | Similarity values aligned by row with pt.pkl |

Keep all four artifacts together and from a compatible training run. Loading uses Python pickle; only load artifacts from a trusted source because unpickling can execute code. Git LFS is configured for CSV, notebook, and pickle files.

## Rights, privacy, and future persistence

The repository does not establish the data's source, license, or redistribution permissions. The source-code MIT license does not grant rights to datasets, ratings, user attributes, or images. Verify their terms and provenance before publishing or deploying them. User IDs, age, location, and rating history may be sensitive; minimize access and avoid unnecessary logging.

If persistent user profiles or ratings are introduced, document the new storage service, schema, retention, access controls, migrations, and deletion behavior before collecting data.
