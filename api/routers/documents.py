from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, StreamingResponse

router = APIRouter(prefix='/documents')
from api.utils.storage import Storage


@router.get('', response_class=FileResponse)
@router.get('/', response_class=FileResponse)
def get(
        name
        # token: Annotated[str, Depends(is_connected_admin_query)]
) -> StreamingResponse:
    """Send a document"""
    storage = Storage()
    file = storage.get(name)
    if file:
        return StreamingResponse(content=file['Body'].iter_chunks())

    raise HTTPException(status_code=404)

@router.get('/list')
def get_list():
    storage = Storage()
    objects = []
    for object in storage.list()['Contents']:
        objects.append(object['Key'])

    return objects