# 📚 Documentation Hub

Welcome to the **Bookwish / Book Recommendation System** documentation. This directory explains the current Flask application, its offline collaborative-filtering workflow, data artifacts, deployment requirements, and quality requirements.

> [!IMPORTANT]
> This documentation describes the checked-in implementation. It does not imply that planned validation, authentication, monitoring, accessibility testing, or retraining automation already exists.

## 🧭 Start here

| Goal | Guide |
|---|---|
| Understand the product and limits | [Overview](overview.md) |
| Understand components and data flow | [Architecture](architecture.md) |
| Install and run locally | [Installation](installation.md) |
| Change the Flask app or notebook | [Development](development.md) |
| Understand model generation | [Model methodology](model-methodology.md) |
| Understand CSV and pickle assets | [Data dictionary](data-dictionary.md) |
| Inspect the HTML routes | [HTTP routes](api.md) |
| Deploy behind a WSGI server | [Deployment](deployment.md) |
| Review privacy and data handling | [Privacy](privacy.md) |
| Assess application security | [Security review](security.md) |
| Improve accessible interactions | [Accessibility](accessibility.md) |
| Test code, templates, and artifacts | [Testing](testing.md) |
| Operate and update a deployment | [Operations](operations.md) |
| Diagnose errors | [Troubleshooting](troubleshooting.md) |

## 🗺️ Diagrams

- [System architecture](diagrams/architecture.mmd)
- [Training and inference pipeline](diagrams/recommendation-pipeline.mmd)
- [Request sequence](diagrams/request-sequence.mmd)
- [Data relationships](diagrams/data-lineage.mmd)
- [SVG visual assets](../assets/diagrams/README.md)

## 🧰 Working agreements

- Do not load pickle artifacts from untrusted sources.
- Keep the four runtime pickle files from one compatible model build.
- Verify dataset and image rights independently of the MIT source license.
- Do not expose Flask debug mode to a network.
- Record test evidence for behavior changes.
- Preserve Git LFS attributes for large data and model files.

## 📝 Templates

Reusable issue, pull request, incident, test, and decision templates live in [templates/](templates/README.md).
