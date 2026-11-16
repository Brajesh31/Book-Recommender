"""Template-level checks that do not import app.py or deserialize pickle files."""
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / "templates"


def make_environment():
    return Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
    )


def test_index_template_renders_popular_books():
    template = make_environment().get_template("index.html")
    html = template.render(
        book_name=["Example Book"],
        author=["Example Author"],
        image=["https://example.invalid/cover.jpg"],
        votes=[42],
        rating=[4.5],
    )
    assert "Example Book" in html
    assert "Example Author" in html
    assert "42" in html


def test_recommend_template_renders_results():
    template = make_environment().get_template("recommend.html")
    html = template.render(
        data=[["Recommended Title", "Recommended Author", "https://example.invalid/book.jpg"]]
    )
    assert "Recommend Books" in html
    assert "Recommended Title" in html
    assert "Recommended Author" in html


def test_recommend_template_escapes_untrusted_text():
    template = make_environment().get_template("recommend.html")
    html = template.render(data=[["<script>alert(1)</script>", "Author", ""]])
    assert "&lt;script&gt;" in html
    assert "<script>alert(1)</script>" not in html
