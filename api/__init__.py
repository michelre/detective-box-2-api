from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers.status import router as status_router
from api.routers.users import router as user_router
from api.routers.db import router as db_router
from api.routers.documents import router as document_router
from api.routers.box import router as box_router
from api.routers.quizz import router as quizz_router
from api.routers.help import router as help_router
from api.routers.objective import router as objective_router
from api.routers.history import router as history_router
from api.routers.character import router as character_router
from api.routers.event import router as event_router

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
app.include_router(document_router)
app.include_router(box_router)
app.include_router(quizz_router)
app.include_router(help_router)
app.include_router(objective_router)
app.include_router(history_router)
app.include_router(character_router)
app.include_router(event_router)