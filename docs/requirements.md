# 📋 Project Requirements

## Functional requirements
- Render the precomputed popular-book collection on `GET /`.
- Render the title submission form on `GET /recommend`.
- Accept a form field named `user_input` on `POST /recommend_books`.
- For an exact title present in the trained pivot index, rank the corresponding similarity vector.
- Resolve candidate title, author, and medium cover URL from book metadata.
- Render up to four recommendation cards.

## Non-functional requirements
- Run on a maintained Python 3 environment compatible with the declared packages.
- Keep model artifact loading and training outside visitor-controlled inputs.
- Preserve artifact row/index alignment.
- Use a production WSGI server outside local development.
- Avoid exposing personal data, debug tracebacks, or secrets.
- Provide usable keyboard navigation, readable contrast, and responsive templates.
- Record reproducible dependency and model build information.

## Current gaps
Unknown-title validation, artifact schema checks, automated route tests, dataset provenance, dependency pinning, and accessibility verification are not implemented or verified in the current repository. Track them as engineering work, not as existing capabilities.

## Acceptance checklist
- [ ] Known title returns relevant candidate cards.
- [ ] Blank and unknown titles fail safely after validation is implemented.
- [ ] Missing/incompatible artifacts produce actionable startup diagnostics.
- [ ] Deployment runs with debug disabled.
- [ ] Dataset rights and retention are documented.
- [ ] Automated checks and manual accessibility checks are recorded.
