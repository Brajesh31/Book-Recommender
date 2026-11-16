# 🚦 Error Handling

## Current behavior
- Missing pickle files can prevent module import and app startup.
- Incompatible or malformed pickle objects can fail during startup or request handling.
- Blank or unknown titles can trigger an index lookup error.
- Missing metadata for a selected candidate can produce incomplete result cards.
- Remote cover images may fail independently of Flask.

## Desired behavior
- Validate request fields before model lookup.
- Return a user-friendly no-match state for unknown titles.
- Keep stack traces out of visitor responses.
- Log diagnostic context without raw personal data or secrets.
- Validate artifact schemas and dimensions before serving traffic.
- Provide a controlled startup failure when the model set is incompatible.

## Error categories to document
| Category | Example | Recovery |
|---|---|---|
| Configuration | Missing model file | Restore trusted artifact bundle |
| Artifact | Wrong matrix dimensions | Rebuild complete artifact set |
| Input | Empty or unknown title | Show validation feedback |
| Metadata | Candidate metadata missing | Skip safely and record diagnostic |
| External asset | Cover image unavailable | Render text and fallback image |
