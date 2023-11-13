import asyncio
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from sse_starlette.sse import EventSourceResponse
from starlette.concurrency import run_in_threadpool

from api.utils.events import event_generator, create_client_queue

from api.database import get_db
from api.models import event as event_models
from api.schemas import event as event_schemas
from api.utils import auth as auth_utils

router = APIRouter(prefix="/stream")


@router.get('')
async def stream(
        request: Request,
        token: str
):
    user_id = auth_utils.get_connected_user_id(token)
    create_client_queue(user_id)
    return EventSourceResponse(event_generator(request, user_id))
