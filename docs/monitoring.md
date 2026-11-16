# 📈 Monitoring and Observability

## Current state
The Flask app does not expose dedicated health, readiness, metrics, or tracing endpoints. Use hosting-platform process state and external HTTP checks for the current deployment.

## Recommended signals
- Process startup success and restart count.
- HTTP status distribution and error rate.
- Request latency percentiles.
- Worker memory and CPU.
- Model artifact load time and validation result.
- Disk space and deployment artifact availability.
- External cover-image failures, where measurable.

## Alert design
Alerts should be actionable, have an owner, include a runbook, and avoid containing visitor-submitted titles or personal data. Set thresholds from observed baseline behavior rather than guessing.

## Future readiness endpoint
If introduced, readiness should only report healthy after all four artifacts have loaded and passed schema/dimension/alignment checks. Do not expose file paths, hashes, stack traces, or sensitive deployment details publicly.
