from fastapi import FastAPI
from schemas import Status
from config import Settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
settings = Settings()

origins = [
    "https://api.detectivebox.remimichel.fr",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/status')
def status() -> Status:
    """Send the status of the API"""
    return {"status": "OK", "description": "API Status"}
