# 🪵 Logging Guidance

The current handler prints recommendation data to standard output. There is no configured structured logging policy.

## Recommended logging principles
- Log application lifecycle and operational failures.
- Do not log raw visitor input unless strictly necessary.
- Never log passwords, tokens, secrets, or raw user-level training records.
- Use stable event names and severity levels.
- Include request correlation identifiers only when introduced safely.
- Keep retention and access controls aligned with operational need.

## Events worth recording
- Application startup and artifact validation result.
- WSGI worker termination or restart.
- Request completion status and duration, without submitted title.
- Unexpected exceptions with sanitized context.
- Deployment and model build identifiers.

## Future implementation
Replace debug prints with Python's `logging` module, configure handlers through the hosting environment, and test that sensitive values are not emitted. This is guidance, not a claim that structured logging is already configured.
