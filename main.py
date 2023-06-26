from fastapi import FastAPI
from schemas import Status
from config import Settings

app = FastAPI()
settings = Settings()


@app.get('/status')
def status() -> Status:
    """Send the status of the API"""
    return {"status": "OK", "description": ""}
