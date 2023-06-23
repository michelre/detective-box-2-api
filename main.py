from fastapi import FastAPI
from schemas import Status

app = FastAPI()


@app.get('/status')
def status() -> Status:
    """Send the status of the API"""
    return {"status": "OK"}
