# Troubleshooting

## The app cannot find a pickle file

Check that popular.pkl, pt.pkl, books.pkl, and similarity_scores.pkl are in the repository root and that the command is being run from that directory. The app loads all four during import, so any missing or mismatched file stops startup.

## A model file contains a short pointer instead of binary data

The repository uses Git LFS for .pkl, .csv, and .ipynb files. Install Git LFS, run git lfs install, then run git lfs pull in the cloned repository. A pointer file is not a usable model artifact.

## Unpickling, pandas, or NumPy reports an error

Use the artifact set produced together by the project's workflow and install the runtime requirements in a clean virtual environment. Pickle compatibility can depend on Python and library versions. Do not try artifacts from unknown sources; deserialization is unsafe for untrusted files.

## The recommendation page returns an error

The current form expects a title that exactly matches an entry in pt.index. Check spelling, punctuation, and whitespace. The handler does not handle blank or unknown titles gracefully and may raise an index error. This is a known application limitation, not a database lookup problem.

## The notebook reports that a file does not exist

The notebook includes Colab-style paths under /content. In a local environment, either put files at those paths where supported or update the notebook to point to the local dataset files. Keep generated artifacts and their source data aligned.

## The notebook cannot import scikit-learn

The current requirements.txt does not include scikit-learn even though the notebook imports it. Install the notebook's required dependency in the active virtual environment, or update the dependency manifest as part of a reviewed project change. Runtime app installation and notebook training dependencies are currently not fully separated.

## Port 5000 is already in use

Stop the other local process using that port or select a different local port in the development startup configuration. For deployment, use the documented WSGI server command and the hosting platform's port/bind settings.

## Cover images are missing

Book covers are loaded from external URLs supplied in the metadata. Check network access and the URL itself; the Flask app does not host or repair remote images.
