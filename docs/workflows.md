# 🔄 Application Workflows

## Visitor workflow
```mermaid
flowchart TD
  A[Open home page] --> B[Browse popular titles]
  B --> C[Open Recommend]
  C --> D[Enter exact book title]
  D --> E[Submit form]
  E --> F{Title in pt.index?}
  F -->|Yes| G[Rank similarity scores]
  G --> H[Resolve book metadata]
  H --> I[Render up to four results]
  F -->|No| J[Current code may raise IndexError]
```

## Offline model workflow
1. Obtain the source CSV files and verify their rights.
2. Run the notebook in an environment with its dependencies.
3. Apply the notebook's activity thresholds and pivot transformation.
4. Compute similarity and popularity outputs.
5. Export the complete artifact set.
6. Validate schema, dimensions, ordering, and checksums.
7. Deploy all artifacts together with the matching code.

## Maintainer workflow
Inspect source and data changes, run available checks, update documentation and diagrams, review privacy/security implications, and record actual verification results. See [operations](operations.md) and [release checklist](templates/release-checklist.md).
