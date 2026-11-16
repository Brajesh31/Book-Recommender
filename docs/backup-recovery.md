# 💾 Backup and Recovery

## 1. What must be backed up
A usable release requires a coherent set of:
- application source revision,
- templates and runtime configuration,
- four compatible pickle artifacts,
- artifact manifest and checksums when introduced,
- source dataset snapshot only where rights and retention permit.

The CSV files and model artifacts may contain or encode personal information. Backups require access controls and retention limits.

## 2. Consistency rule
Do not restore `pt.pkl` from one model build with `similarity_scores.pkl` from another. Restore all four artifacts from the same trusted build. Record source commit and model build identifier together.

## 3. Backup procedure
1. Identify the current deployed code SHA.
2. Identify the model build and artifact checksums.
3. Copy the complete artifact bundle to access-controlled storage.
4. Record creation time, storage location, and retention deadline.
5. Verify file sizes and checksums.
6. Restrict access to maintainers who need model deployment access.

## 4. Recovery procedure
1. Stop the rollout or affected service.
2. Select a known-good code and model bundle.
3. Verify checksums before loading any pickle.
4. Restore all four artifacts as a single unit.
5. Restore the matching code revision.
6. Start the WSGI service with debug disabled.
7. Smoke-test the home page and a known title.
8. Record recovery time, selected release, and remaining issues.

## 5. Recovery testing
Test restoration periodically in an isolated environment. A backup is not proven until it has been restored and the application can load and use the artifacts.

## 6. Current limitations
The repository does not define a backup service, retention schedule, recovery point objective, recovery time objective, or automated restore workflow. These must be decided for the actual hosting environment.
