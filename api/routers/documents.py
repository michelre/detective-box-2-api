from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, StreamingResponse

router = APIRouter(prefix='/documents')
from api.utils.storage import Storage


@router.get('/{file_name}', response_class=FileResponse)
def get(
        file_name,
        # token: Annotated[str, Depends(is_connected_admin_query)]
) -> StreamingResponse:
    """Send a document"""
    storage = Storage()
    file = storage.get(file_name)
    if file:
        return StreamingResponse(content=file['Body'].iter_chunks())

    raise HTTPException(status_code=404)
