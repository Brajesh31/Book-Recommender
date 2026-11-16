# 🔐 Security Review and Hardening Plan

## 1. Review scope
This is a source-based review of the current repository and recent application changes. It is not a penetration test, dependency audit, or certification. Findings below distinguish mitigated issues from remaining risks.

## 2. Current risk register

| Priority | Finding | Current evidence | Status / recommended control |
|---|---|---|---|
| Critical | Untrusted pickle execution | Four pickle files are loaded at import | Open risk: load only trusted, reviewed artifacts; evaluate non-executable formats |
| High | Artifact integrity not validated | Direct pickle loads; no manifest | Open risk: verify hashes, schema, dimensions, and row alignment |
| Medium | Sensitive source attributes | Users CSV includes location and age | Open risk: minimize, restrict access, verify lawful basis and retention |
| Medium | External image requests | Templates load dataset cover URLs | Open risk: document third-party requests and review CSP |
| Medium | Unpinned dependencies | Requirements have no version constraints | Open risk: lock and audit runtime and notebook dependencies |
| Medium | Limited test depth | Route tests use mocked artifacts | Partial: add artifact-contract, real deployment, and model-quality tests |
| Medium | Accessibility not formally verified | Improved templates, no assistive-technology evidence | Partial: perform manual keyboard, screen-reader, zoom, and contrast review |
| Low | No structured logging policy | Recommendation print statement removed | Partial: define privacy-aware logging only if operational needs require it |

## 3. Mitigations already applied

- Blank titles return HTTP 400 with a user-facing validation message.
- Unknown titles return HTTP 404 rather than raising an array index error.
- The recommendation handler no longer prints recommendation records to standard output.
- The direct-run entry point uses `debug=False`.
- The recommendation form has a visible label, required field, and length limit.
- Templates include a skip link, main landmark, visible focus styles, and descriptive book-cover alternatives.
- Route and template tests run with mocked model artifacts, avoiding production pickle deserialization in CI.

These changes reduce specific risks but do not make the application production-hardened.

## 4. Trust boundaries

- Browser-submitted form values are untrusted.
- CSV values and cover URLs are untrusted until validated.
- Pickle files cross a code-execution trust boundary.
- The deployment platform and artifact storage must be access-controlled.
- Remote cover-image providers receive visitor requests and network metadata.

## 5. Remaining deployment checklist

- [ ] Use a maintained Python runtime and reviewed dependency set.
- [ ] Deploy through Gunicorn or a managed WSGI server.
- [ ] Load artifacts only from a trusted, controlled release.
- [ ] Verify artifact checksums and model compatibility before serving.
- [ ] Add artifact schema, dimension, and alignment validation.
- [ ] Restrict filesystem and deployment credential access.
- [ ] Review CSV rights, personal-data obligations, and image rights.
- [ ] Configure HTTPS, request size limits, and platform-level rate limiting.
- [ ] Keep logs free of user-level data and secrets.
- [ ] Maintain tested backups of model artifacts and code releases.
- [ ] Complete manual accessibility testing.

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

No claim is made that the application is production hardened. Pickle trust, artifact integrity, dataset rights, dependency reproducibility, and formal accessibility review remain open work.
