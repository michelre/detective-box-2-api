# Detective Box API

## Requirements

- Python >= 3.11
- PIP >= 22
- Postgres

## Technical specifications

- FastAPI: Web framework
- SQLAlchemy: Python ORM
- Alembic: Database migration tool

## Installation

- Create a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
- Install dependencies
```
pip install -r requirements.txt
```
- Running migrations
```
alembic upgrade head
```

## Start in dev mode
Two apps can be loaded:
- app with the main API
- app_stream with the real time API

Just start the following commands:
```
uvicorn api:app --reload
uvicorn api:app_stream --reload --port 8001
```

## Start in production mode
```
python -m api
```