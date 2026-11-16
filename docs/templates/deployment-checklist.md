# 🚀 Deployment Checklist

## Build inputs
- [ ] Commit SHA recorded
- [ ] Python/runtime version recorded
- [ ] Dependencies installed from reviewed set
- [ ] Git LFS objects retrieved
- [ ] Four pickle artifacts belong to one trusted build
- [ ] Checksums and manifest reviewed

## Application
- [ ] Working directory is repository root
- [ ] Templates included
- [ ] Gunicorn/managed WSGI configured
- [ ] Debug mode disabled
- [ ] Worker count sized for model memory
- [ ] HTTPS and network policy configured externally

## Validation
- [ ] Home route smoke-tested
- [ ] Recommendation route smoke-tested with known title
- [ ] Invalid input behavior checked
- [ ] Startup and logs reviewed
- [ ] Artifact alignment validated
- [ ] Accessibility smoke test completed

## Recovery
- [ ] Previous code revision available
- [ ] Matching previous artifact bundle available
- [ ] Rollback steps documented
- [ ] Backup restoration tested

## Record
- Deployment owner:
- Environment:
- Timestamp:
- Commit:
- Model build:
- Known exceptions:
