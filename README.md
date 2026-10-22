# Network QA Automation Lab (starter)

A small FastAPI service with real TCP and HTTP integration tests. **This starter does not yet implement persistent storage, MinIO, or distributed systems.** Data is held in process memory and lost when the container restarts.

## Requirements
- Docker Desktop with Compose
- Python 3.12+ recommended

## Run (macOS/Linux)
```bash
docker compose up -d --build
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```

Check the service: `curl http://127.0.0.1:8000/health`

Stop: `docker compose down`

## What tests verify
- TCP handshake with the API port
- HTTP 200 health response
- HTTP write/read round trip through the API
- HTTP 404 for a missing item

## Limitations / next milestones
- The round-trip is NOT a storage persistence test. Add MinIO and S3-compatible upload/download APIs.
- Add SHA-256 integrity checks and fault injection for unavailable storage.
- Add separate API, integration, and E2E suites with deterministic test data.
- Review GitHub Actions versions and security settings before production use.
