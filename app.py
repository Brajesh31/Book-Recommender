from flask import Flask, render_template, request
import pickle

import numpy as np

# Model files are trusted, precomputed artifacts. Never load visitor-supplied
# pickle files: Python pickle deserialization can execute arbitrary code.
popular_df = pickle.load(open("popular.pkl", "rb"))
pt = pickle.load(open("pt.pkl", "rb"))
books = pickle.load(open("books.pkl", "rb"))
similarity_scores = pickle.load(open("similarity_scores.pkl", "rb"))

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        book_name=list(popular_df["Book-Title"].values),
        author=list(popular_df["Book-Author"].values),
        image=list(popular_df["Image-URL-M"].values),
        votes=list(popular_df["num_ratings"].values),
        rating=list(popular_df["avg_rating"].values),
    )


@app.route("/recommend")
def recommend_ui():
    return render_template("recommend.html", data=[], query="")


@app.route("/recommend_books", methods=["POST"])
def recommend():
    user_input = (request.form.get("user_input") or "").strip()

    if not user_input:
        return (
            render_template(
                "recommend.html",
                data=[],
                query=user_input,
                error="Enter a book title before requesting recommendations.",
            ),
            400,
        )

    if len(user_input) > 200:
        return (
            render_template(
                "recommend.html",
                data=[],
                query=user_input[:200],
                error="Book titles must be 200 characters or fewer.",
            ),
            400,
        )

    matches = np.flatnonzero(pt.index == user_input)
    if matches.size == 0:
        return (
            render_template(
                "recommend.html",
                data=[],
                query=user_input,
                error="No exact title match was found. Check the spelling and try a title from the trained catalogue.",
            ),
            404,
        )

    selected_index = int(matches[0])
    if selected_index >= len(similarity_scores):
        app.logger.error("Model artifact mismatch: similarity row is missing")
        return (
            render_template(
                "recommend.html",
                data=[],
                query=user_input,
                error="Recommendations are temporarily unavailable. Please try again later.",
            ),
            503,
        )

    ranked_items = sorted(
        enumerate(similarity_scores[selected_index]),
        key=lambda item: item[1],
        reverse=True,
    )
    candidate_indices = [
        int(candidate_index)
        for candidate_index, _score in ranked_items
        if candidate_index != selected_index
    ][:4]

    data = []
    for candidate_index in candidate_indices:
        if candidate_index >= len(pt.index):
            continue

        candidate_title = pt.index[candidate_index]
        matching_books = books[books["Book-Title"] == candidate_title]
        matching_books = matching_books.drop_duplicates("Book-Title")

        if matching_books.empty:
            continue

        book = matching_books.iloc[0]
        data.append(
            [
                book["Book-Title"],
                book["Book-Author"],
                book["Image-URL-M"],
            ]
        )

    return render_template(
        "recommend.html",
        data=data,
        query=user_input,
        message=(
            "No recommendation details were available for this title."
            if not data
            else None
        ),
    )


if __name__ == "__main__":
    # Debug mode must remain disabled by default. Use a WSGI server in production.
    app.run(debug=False)
