# ⌨️ Useful Commands

Run commands from the repository root unless stated otherwise.

## Clone with Git LFS
```bash
git lfs install
git clone https://github.com/Brajesh31/Book-Recommender.git
cd Book-Recommender
git lfs pull
```

## Create environment
Windows PowerShell:
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

macOS/Linux:
```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run locally
```bash
python app.py
```
Open `http://127.0.0.1:5000`. The direct-run entry point enables debug mode, so use only on a local development machine.

## Production WSGI example
```bash
gunicorn --workers 2 --bind 0.0.0.0:8000 app:app
```
Tune workers for memory and configure TLS/network policy at the hosting layer.

## Basic verification
```bash
python -m py_compile app.py
```
This does not validate pickle safety, model compatibility, or route behavior.
