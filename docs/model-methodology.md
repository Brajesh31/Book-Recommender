# 🧠 Model Methodology and Reproducibility

## 1. Scope

This guide describes the collaborative-filtering approach documented by the repository notebook and consumed by `app.py`. The running application does not train a model. It loads precomputed Python objects.

## 2. Inputs

- `Books.csv`: ISBN, title, author, publication metadata, publisher, and three cover URL sizes.
- `Ratings.csv`: user ID, ISBN, numeric book rating.
- `Users.csv`: user ID, location, and age fields.

The notebook uses the books and ratings tables for recommendation construction. It reads user data during exploration. Confirm the real dataset source, version, license, privacy basis, and redistribution permissions before using it outside a controlled learning environment.

## 3. Preprocessing described in the notebook

The documented workflow:
1. Loads book metadata and ratings.
2. Filters users with more than 200 ratings.
3. Filters books with at least 50 ratings.
4. Builds a user-by-title pivot table.
5. Fills missing ratings with zero.
6. Computes cosine similarity between book vectors.
7. Builds a popularity ranking from titles with at least 250 ratings.
8. Keeps the top 50 popular entries by average rating.
9. Exports model objects to pickle files.

These thresholds materially affect coverage. A title excluded during filtering cannot be found through the current recommendation index, even if it exists in the source book metadata.

## 4. Runtime artifact contract

| File | Expected role |
|---|---|
| `popular.pkl` | Popularity table used by the home page |
| `pt.pkl` | Pivot table whose index contains recommendation lookup titles |
| `books.pkl` | Metadata table used to render candidate titles |
| `similarity_scores.pkl` | Similarity matrix whose row order corresponds to `pt.index` |

The critical invariant is:

`similarity_scores[i]` must represent the same title as `pt.index[i]`.

If one artifact is regenerated independently, row alignment can break without an obvious startup error. Generate, validate, version, and deploy the full artifact set as one unit.

## 5. Inference behavior

For a submitted title:
1. The handler searches `pt.index` for exact equality.
2. It takes the first matching index position.
3. It reads the corresponding similarity-score row.
4. It sorts candidate positions by score descending.
5. It skips the first ranked item, which is expected to be the input item itself.
6. It selects four positions and resolves metadata from `books.pkl`.
7. It renders result cards.

The app does not currently implement title normalization, fuzzy matching, an explicit minimum similarity threshold, a diversity rule, or a cold-start strategy.

## 6. Quality evaluation

Before describing this as a high-quality recommender, evaluate it on a held-out dataset using an explicit protocol. Useful offline measures may include Precision@K, Recall@K, MAP@K, NDCG@K, catalog coverage, and popularity concentration. Define:
- user and item split strategy,
- temporal leakage prevention,
- minimum history needed,
- treatment of users/items unseen during training,
- candidate universe,
- K value,
- baseline methods,
- confidence intervals or repeated runs.

Do not publish metric values until the evaluation is executed and reproducible. No verified model quality metrics are included in the current repository.

## 7. Reproducible model build record

For every model rebuild, record:
- source dataset identity and checksum,
- rights and access approval,
- Python and dependency versions,
- notebook revision,
- filtering thresholds,
- matrix dimensions and sparsity,
- similarity algorithm and parameters,
- export timestamp and artifact checksums,
- validation results,
- known limitations.

## 8. Safe improvement sequence

1. Parameterize notebook input paths rather than assuming `/content/`.
2. Add a dedicated training dependency set, including scikit-learn.
3. Extract preprocessing into deterministic functions.
4. Add schema and shape checks before export.
5. Write a manifest containing artifact versions, dimensions, and checksums.
6. Validate the manifest and matrix alignment at application startup.
7. Evaluate quality against a baseline before tuning.
8. Consider safer serialization formats for data-only artifacts.

## 9. Important security warning

Python pickle can execute code during deserialization. Never accept a pickle uploaded by a visitor, downloaded from an unverified URL, or supplied by an unknown contributor. Keep model build and deployment permissions restricted.
