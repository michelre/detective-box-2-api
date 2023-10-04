from fastapi import APIRouter
from fastapi.responses import FileResponse
from os import getcwd
from fastapi import Depends
from typing import Annotated
from api.utils.auth import is_connected_admin_query

router = APIRouter(prefix='/documents')


@router.get('/{file_name}', response_class=FileResponse)
def get(
        file_name,
        token: Annotated[str, Depends(is_connected_admin_query)]
) -> FileResponse:
    """Send a document"""
    file_path = f'{getcwd()}/assets/{file_name}'
    return file_path
