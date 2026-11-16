# ⚙️ Configuration

The current Flask app reads no environment variables. The checked-in `.env.example` explicitly documents that no runtime setting is currently consumed. Do not invent settings or add secrets to the repository.

## Runtime configuration
- Working directory: repository root, because artifact paths are relative.
- Flask application import target: `app:app`.
- Local development port: Flask's default 5000.
- Production example: Gunicorn binds to a configured interface and port.
- Model files: `popular.pkl`, `pt.pkl`, `books.pkl`, and `similarity_scores.pkl` in the root.

## Deployment guidance
Configure host-specific values in the hosting platform. Keep debug disabled, restrict filesystem access, use HTTPS termination, and select worker count based on memory. Each worker may load its own artifact copies.

## Future configuration contract
If configuration is introduced, document each key with purpose, required/optional status, safe default, example, secret classification, and validation behavior. Add startup validation and update `.env.example` with placeholders only.
