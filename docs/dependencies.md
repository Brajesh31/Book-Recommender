# 📦 Dependency Inventory

## Declared runtime dependencies
| Package | Current purpose |
|---|---|
| Flask | HTTP routing and Jinja rendering |
| NumPy | Similarity array indexing and ranking |
| pandas | DataFrame and pickle artifact handling |
| Gunicorn | Production WSGI server |

The current `requirements.txt` uses unpinned package names. The notebook also imports scikit-learn, which is not declared in that file.

## Dependency maintenance
- Choose and test a supported Python version.
- Pin or lock dependencies for repeatable deployments.
- Separate runtime and notebook/training dependencies where practical.
- Review package licenses and security advisories.
- Update in a controlled cadence.
- Test pickle artifact compatibility after pandas/NumPy upgrades.
- Keep dependency changes and test evidence in the same change.

Do not claim dependency scanning or a lockfile exists until configured.
