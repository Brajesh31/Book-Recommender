# 💡 Usage Examples

## Browse popular books
Start the application and open `/`. The page renders the records already stored in `popular.pkl`.

## Request similar titles
1. Open `/recommend`.
2. Enter a title that exactly matches an entry in `pt.index`.
3. Submit the form.
4. Review up to four returned cards.

The exact title is case-sensitive in current code. Do not assume partial matching, spelling correction, or semantic search.

## HTTP form example
```bash
curl -X POST http://127.0.0.1:5000/recommend_books \
  --data-urlencode "user_input=EXACT TITLE FROM MODEL INDEX"
```

Replace the example value with a title verified in the trusted model index. The endpoint returns HTML, not JSON.

## Notebook workflow
The notebook currently contains Colab-style `/content/` paths. Adjust input paths for local use and install notebook dependencies, including scikit-learn, in an isolated environment. Regenerate and validate the full artifact bundle together.
