from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers.status import router as status_router
from api.routers.users import router as user_router
from api.routers.db import router as db_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(status_router)
app.include_router(db_router)
