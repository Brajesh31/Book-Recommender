# Installation

This guide covers running the existing Flask demo locally. The repository does not declare a supported Python version in project metadata; use a currently maintained Python 3 release compatible with the listed Flask, NumPy, and pandas packages.

## 1. Clone the project and retrieve large files

The repository tracks CSV, notebook, and pickle files with Git LFS. Install Git LFS and enable it for your account before cloning or pulling the project:

~~~sh
git lfs install
git clone https://github.com/Brajesh31/Book-Recommender.git
cd Book-Recommender
git lfs pull
~~~

On Windows, run the same Git commands in PowerShell or Git Bash. Confirm that popular.pkl, pt.pkl, books.pkl, and similarity_scores.pkl are real files rather than short Git LFS pointer text files. The app needs these artifacts at startup.

## 2. Create an isolated Python environment

Windows PowerShell:

~~~powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
~~~

macOS or Linux:

~~~sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
~~~

The current requirements file lists Flask, NumPy, pandas, and Gunicorn without version pins. Dependency resolution may therefore change over time. If a package installation or pickle loading fails, record the Python and package versions used.

## 3. Start the development server

From the repository root with the virtual environment active:

~~~sh
python app.py
~~~

Open http://127.0.0.1:5000/. The home page displays popular books; use the recommendation form and enter a title that appears in the trained index. The current development entry point enables Flask debug mode. Do not use this command as a production server.

## Notebook and retraining

The notebook is an optional data-preparation workflow, not needed to run the existing artifacts. It contains Colab-style file paths under /content and imports scikit-learn, which is not currently declared in requirements.txt. If you intend to run it, provide the CSV files at the paths expected by the notebook (or update those paths), install the notebook's missing dependencies in your isolated environment, and review the data source terms first. Retraining replaces the model files and should be followed by checks that all four artifacts were generated from the same data and remain mutually compatible.

## Environment settings

The app currently reads no environment variables. .env.example is documentation only; no secret or configuration value is required for the local demo.
