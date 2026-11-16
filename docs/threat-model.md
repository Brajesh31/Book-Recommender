# 🕵️ Threat Model

## 1. Scope and assumptions
This threat model covers the current browser-facing Flask app, its source CSVs, pickle artifacts, notebook workflow, and deployment boundary. It is a design review, not a penetration test.

## 2. Assets to protect
- Application source and deployment integrity.
- Trusted pickle artifacts and their row alignment.
- User IDs, locations, ages, and rating histories in source data.
- Deployment credentials and repository write access.
- Visitor request metadata and operational logs.
- Dataset and image licensing obligations.

## 3. Trust boundaries
1. Visitor browser to Flask request handler.
2. CSV source files to notebook transformations.
3. Notebook output to runtime pickle loading.
4. GitHub repository and Git LFS storage to deployment environment.
5. Visitor browser to third-party cover-image hosts.

## 4. Threat scenarios

| Threat | Possible impact | Current exposure | Mitigation |
|---|---|---|---|
| Malicious pickle artifact | Code execution at import | Direct `pickle.load` calls | Trusted build pipeline, restricted writes, safer serialization |
| Unknown title input | Request error / availability degradation | Server now returns HTTP 404 for no-match; exact matching remains | Keep validation and regression tests |
| Debugger exposed | Interactive code execution / information disclosure | Direct-run entry point now sets debug=False | Continue using WSGI and network controls |
| Artifact mismatch | Wrong or broken recommendations | No compatibility manifest | Hash, schema, dimension, and alignment checks |
| Dataset disclosure | Personal data exposure | User attributes and ratings in repository | Verify rights, minimize, restrict access |
| Dependency compromise | Runtime compromise | Unpinned dependencies | Lock, audit, update with review |
| External image tracking | Third-party receives browser metadata | Remote image URLs | Document, proxy/cache only if rights permit |
| Log leakage | Data disclosure | Recommendation data printed | Remove prints, sanitize structured logs |

## 5. Abuse cases
- A contributor replaces a model pickle with a malicious file.
- A deployment downloads LFS pointer text rather than full model objects.
- A visitor submits malformed or excessively long input.
- A maintainer exposes debug mode on a public interface.
- A dataset copy is redistributed without permission.
- A dependency update changes pickle compatibility unexpectedly.

## 6. Mitigation priorities
**Immediate:** trusted artifacts only, debug disabled in production, safe input validation, data rights review, restricted repository write access.

**Next:** artifact manifest and validation, pinned dependencies, route tests, privacy-aware logging, template accessibility checks.

**Later:** safer model serialization, automated model evaluation, operational monitoring, and formal security testing.

## 7. Residual risk
The project is a learning/demo application and has not been penetration-tested. Documentation and CI checks do not by themselves make the application production secure.
