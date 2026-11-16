# 🔐 Security Review and Hardening Plan

## 1. Review scope

This is a source-based review of the current repository structure and visible application code. It is not a penetration test, dependency audit, or certification. Findings below are actionable observations, not proof that an exploit has occurred.

## 2. Current risk register

| Priority | Finding | Current evidence | Recommended control |
|---|---|---|---|
| Critical | Untrusted pickle execution | Four pickle files loaded at import | Load only trusted, reviewed artifacts; consider non-executable formats |
| High | Debug server exposure | `app.run(debug=True)` | Keep debug off; use Gunicorn/managed WSGI |
| High | Unhandled unknown title | `np.where(...)[0][0]` | Validate blank and unknown input, return a safe message |
| High | No artifact integrity validation | Direct pickle loads, no manifest | Verify trusted checksums, schema, dimensions, and alignment |
| Medium | Sensitive source attributes | Users CSV includes location and age | Minimize, restrict access, verify lawful basis and retention |
| Medium | External image requests | Templates load dataset cover URLs | Document third-party requests; consider proxy/cache and CSP |
| Medium | Unpinned dependencies | Requirements have no version constraints | Lock and audit runtime and notebook dependencies |
| Medium | No automated test suite | No tests present in tree | Add tests for routes, malformed inputs, and artifacts |
| Low | Console output of recommendations | Handler prints result data | Remove debug prints; use privacy-aware structured logs |

## 3. Trust boundaries

- Browser-submitted form data is untrusted.
- CSV data and cover URLs are untrusted until validated.
- Pickle files cross a code-execution trust boundary.
- The deployment platform and artifact storage must be access-controlled.
- Remote cover-image providers receive visitor requests and network metadata.

## 4. Immediate deployment checklist

- [ ] Use a maintained Python runtime and reviewed dependency set.
- [ ] Deploy through Gunicorn or a managed WSGI server.
- [ ] Disable Flask debug mode and interactive debugger.
- [ ] Load artifacts only from a trusted, controlled release.
- [ ] Verify artifact checksums and model compatibility before serving.
- [ ] Validate title input and handle missing titles.
- [ ] Avoid exposing raw exception details to visitors.
- [ ] Restrict filesystem permissions and deployment credentials.
- [ ] Review CSV rights, personal-data obligations, and image rights.
- [ ] Configure HTTPS, request size limits, and platform-level rate limiting.
- [ ] Keep logs free of user-level data and secrets.
- [ ] Maintain tested backups of model artifacts and code releases.

## 5. Input handling requirements

The recommendation form should:
- require a non-empty title,
- impose a reasonable maximum length,
- normalize whitespace without silently changing title identity,
- reject control characters,
- verify membership in the title index,
- return a clear no-match message,
- never expose a Python traceback to the visitor.

A later fuzzy-search feature should use a deliberate matching strategy and avoid returning arbitrary results for ambiguous titles.

## 6. Artifact handling requirements

- Treat pickle files as executable content.
- Keep artifact creation separate from serving requests.
- Restrict who can write artifacts in production.
- Store a manifest containing artifact version, source revision, dimensions, and hashes.
- Confirm `len(pt.index)` matches the first dimension of the similarity matrix.
- Check expected columns and types before registering the app as ready.

## 7. Security change process

Security reports must be sent through the private reporting channel in [SECURITY.md](../SECURITY.md). Do not publish exploit details, raw personal data, or production secrets in issues.

## 8. Scope limitation

No claim is made that the application is production hardened. The current code has known issues listed above. Address the critical and high-priority items before public exposure.
