"""Route tests using mocked, trusted in-memory model objects.

The fixture replaces pickle loading before importing app.py, so the tests never
deserialize repository model artifacts.
"""
import builtins
import importlib
import io
import pickle
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def client(monkeypatch):
    popular = pd.DataFrame(
        {
            "Book-Title": ["Popular Book"],
            "Book-Author": ["Popular Author"],
            "Image-URL-M": ["https://example.invalid/popular.jpg"],
            "num_ratings": [100],
            "avg_rating": [4.2],
        }
    )
    titles = ["Seed Book", "Book B", "Book C", "Book D", "Book E"]
    pivot = pd.DataFrame(index=pd.Index(titles))
    metadata = pd.DataFrame(
        {
            "Book-Title": titles,
            "Book-Author": ["Seed Author", "Author B", "Author C", "Author D", "Author E"],
            "Image-URL-M": [f"https://example.invalid/{index}.jpg" for index in range(5)],
        }
    )
    similarity = np.array(
        [
            [1.0, 0.9, 0.8, 0.7, 0.6],
            [0.9, 1.0, 0.7, 0.6, 0.5],
            [0.8, 0.7, 1.0, 0.6, 0.5],
            [0.7, 0.6, 0.5, 1.0, 0.4],
            [0.6, 0.5, 0.4, 0.3, 1.0],
        ]
    )
    artifacts = iter([popular, pivot, metadata, similarity])

    monkeypatch.setattr(pickle, "load", lambda _handle: next(artifacts))
    original_open = builtins.open

    def artifact_only_open(file, *args, **kwargs):
        if Path(file).name in {
            "popular.pkl",
            "pt.pkl",
            "books.pkl",
            "similarity_scores.pkl",
        }:
            return io.BytesIO()
        return original_open(file, *args, **kwargs)

    monkeypatch.setattr(builtins, "open", artifact_only_open)
    sys.modules.pop("app", None)
    spec = importlib.util.spec_from_file_location("app", ROOT / "app.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["app"] = module
    spec.loader.exec_module(module)
    module.app.config.update(TESTING=True)

    yield module.app.test_client()

    sys.modules.pop("app", None)


def test_home_page_renders_popular_books(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Popular Book" in response.data
    assert b"Popular Author" in response.data


def test_recommendation_form_renders_with_label(client):
    response = client.get("/recommend")
    assert response.status_code == 200
    assert b'for="user_input"' in response.data
    assert b"Book title" in response.data


def test_blank_title_returns_validation_error(client):
    response = client.post("/recommend_books", data={"user_input": "   "})
    assert response.status_code == 400
    assert b"Enter a book title" in response.data


def test_unknown_title_returns_not_found_message(client):
    response = client.post("/recommend_books", data={"user_input": "Not in the model"})
    assert response.status_code == 404
    assert b"No exact title match was found" in response.data


def test_known_title_returns_top_similar_books(client):
    response = client.post("/recommend_books", data={"user_input": "Seed Book"})
    assert response.status_code == 200
    assert b"Book B" in response.data
    assert b"Book E" in response.data
    assert b"Seed Book" not in response.data


def test_oversized_title_returns_validation_error(client):
    response = client.post("/recommend_books", data={"user_input": "x" * 201})
    assert response.status_code == 400
    assert b"200 characters or fewer" in response.data
