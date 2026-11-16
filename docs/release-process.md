# 🚢 Release Process

## 1. Release principles
A release consists of application code and a compatible four-file model artifact set. Do not deploy model files independently from one another.

## 2. Pre-release
- Review code and data changes.
- Verify dataset rights and model provenance.
- Record source commit and model build identifier.
- Validate artifact hashes, expected columns, matrix dimensions, and row alignment.
- Run syntax, template, route, and manual accessibility checks.
- Review security findings and dependency changes.
- Update README, changelog, roadmap, and diagrams where behavior changed.

## 3. Deploy
- Build from a clean checkout with Git LFS enabled.
- Install reviewed dependencies.
- Start with Gunicorn or managed WSGI.
- Keep debug disabled.
- Confirm worker memory and startup health.
- Smoke-test home and known-title recommendation routes.

## 4. Rollback
Restore the last known-good code and its matching complete artifact bundle. Restart workers and repeat smoke tests. Never mix pivot and similarity artifacts from different builds.

## 5. Release record
Record tag, commit, deployment time, artifact manifest/checksums, verification results, known issues, and rollback reference. Do not fabricate release notes for changes that did not occur.
