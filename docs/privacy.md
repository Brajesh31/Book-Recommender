# 🛡️ Privacy and Data Handling

## 1. Current data footprint

The repository includes book metadata, ratings, and user attributes. The supplied user dataset includes user identifiers, location, and age. The ratings data links user identifiers with book identifiers and rating values.

The running Flask app reads precomputed model artifacts. It does not implement user accounts, persistent visitor profiles, a database, or a history of visitor searches.

## 2. Visitor interactions

The visitor submits a book title using a standard HTML form. The route processes the submitted title in memory and renders recommendations. The recommendation handler no longer prints result records to standard output. Hosting infrastructure may still record ordinary request metadata, so review its logging and retention settings.

The templates request cover images from URLs contained in the book metadata. A browser contacting those image hosts may disclose network metadata to third parties. This is outside the application's direct control.

## 3. Data minimization

For the current recommendation method, the notebook uses ratings and book metadata to produce the collaborative-filtering artifacts. User demographic data should not be used or redistributed merely because it is present in the source dataset.

Recommended handling:
- restrict access to raw data and derived files,
- avoid copying user-level rows into documentation or screenshots,
- do not log raw user identifiers or demographic values,
- remove unnecessary personal fields during preprocessing,
- set retention periods for temporary training data,
- document deletion and access procedures where applicable.

## 4. Dataset rights and lawful use

This repository does not establish the original provider, license, consent basis, or permitted redistribution of the CSV files and book cover images. The MIT source license does not grant those rights.

Before external deployment or redistribution, establish:
- source and acquisition date,
- license and terms of use,
- whether personal data is present,
- lawful basis and any consent requirements,
- restrictions on derived datasets,
- attribution requirements,
- deletion or retention conditions.

## 5. Future privacy features

If user accounts, saved books, or explicit preference history are introduced, document:
- what is collected and why,
- storage location and access roles,
- retention and deletion behavior,
- export and correction workflow,
- security controls,
- user-facing privacy notice.

None of these account or preference features exists in the current implementation.

## 6. Incident response

If personal data is exposed:
1. Restrict access and stop further disclosure.
2. Preserve minimal diagnostic evidence securely.
3. Identify affected files, systems, and data categories.
4. Rotate credentials if any were exposed.
5. Follow applicable organizational and legal notification requirements.
6. Record the remediation and prevent recurrence.

Report security issues privately as described in the root [SECURITY.md](../SECURITY.md).
