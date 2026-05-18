# FastAPI Task API

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Docker Compose

## Features

- CRUD Task API
- Filtering
- Environment-based configuration
- Containerized backend

Run locally:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```
