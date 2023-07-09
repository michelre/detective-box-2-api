from fastapi import APIRouter

from api.schemas.status import Status

router = APIRouter(prefix='/status')


@router.get('/', summary="Get status")
def get() -> Status:
    """Send the status of the API"""
    return {"status": "OK", "description": "API Status"}
