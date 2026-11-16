# ⚙️ Operations and Release Runbook

## 1. Service shape

The current service is a single Flask WSGI application that loads four large pickle artifacts into process memory. There is no database, queue, cache, authentication service, health endpoint, or metrics endpoint.

## 2. Startup requirements

Before deployment:
- source checkout is complete,
- Git LFS objects are downloaded,
- all four model files come from one trusted build,
- dependencies are installed,
- template directory is present,
- working directory is repository root,
- debug mode is disabled,
- memory capacity accounts for each WSGI worker's model copy.

## 3. Release procedure

1. Review the code and model changes together.
2. Confirm data rights and model provenance.
3. Validate the artifact manifest and checksums.
4. Run syntax, template, route, and artifact contract checks.
5. Stage the release in a non-public environment.
6. Start the WSGI service and verify startup logs.
7. Test the home route and a known in-index recommendation.
8. Verify invalid input behavior after that feature is implemented.
9. Route traffic only after the smoke test passes.
10. Record the deployed commit and model build identifiers.

## 4. Rollback

Keep the previous known-good code and matching artifact set available. Roll back the code and all associated model files together. Do not mix a new pivot table with old similarity scores or metadata. Confirm the process has restarted and can serve a known request.

## 5. Monitoring

The current app has no built-in health or metrics endpoint. Use hosting platform process state and HTTP monitoring. Monitor:
- startup and import failures,
- worker restarts,
- memory pressure,
- HTTP 4xx/5xx rates,
- response latency,
- missing external image assets where practical.

Do not log visitor input or user-level training data by default.

## 6. Backup requirements

Back up code revision, model artifact files, and the model manifest as a consistent set. Protect backups with access controls and retention limits. Test restoration rather than assuming successful upload implies recoverability.

## 7. Incident handling

For startup or model mismatch:
1. stop rollout,
2. capture the deployed revision and artifact identifiers,
3. compare against the last known-good release,
4. restore a coherent release set,
5. restart and smoke-test,
6. document root cause and prevention.

For suspected personal-data or security incidents, follow [Privacy](privacy.md) and [SECURITY.md](../SECURITY.md).
