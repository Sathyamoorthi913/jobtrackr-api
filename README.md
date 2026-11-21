# JobTrackr API

A REST API to track job applications, built with FastAPI and SQLAlchemy.

## Features
- Create, read, update and delete job applications (CRUD)
- Pagination with `skip` and `limit`
- Filter by status and company (case-insensitive)
- Input validation with Pydantic (422 on bad data, 404 on missing records)
- Interactive API docs with Swagger UI

## Tech stack
Python, FastAPI, SQLAlchemy 2.0, Pydantic, SQLite (PostgreSQL-ready via `DATABASE_URL`), Uvicorn

## Run locally
```bash
git clone https://github.com/Sathyamoorthi913/jobtrackr-api.git
cd jobtrackr-api
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash; use venv/bin/activate on Linux/Mac
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000/docs

## Endpoints
| Method | Endpoint | Description |
|---|---|---|
| POST | /applications | Add an application |
| GET | /applications?skip=0&limit=10&status=interview&company=infosys | List with pagination and filters |
| GET | /applications/{id} | Get one application |
| PATCH | /applications/{id} | Update fields (e.g. status) |
| DELETE | /applications/{id} | Delete an application |

## Project structure
```
app/
  database.py   # DB engine and session
  models.py     # SQLAlchemy table
  schemas.py    # Pydantic request/response models
  main.py       # API endpoints
```