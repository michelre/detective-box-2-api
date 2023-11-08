from fastapi import APIRouter

from api.schemas.status import Status
from api.utils.events import new_event

router = APIRouter(prefix='/status')


@router.get('/', summary="Get status")
async def get() -> Status:
    """Send the status of the API"""
    await new_event('OK', 1)
    return {"status": "OK", "description": "API Status"}
