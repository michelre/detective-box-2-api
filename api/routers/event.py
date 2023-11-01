from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.orm.attributes import flag_modified

from api.database import get_db
from api.models import event as event_models

router = APIRouter(prefix="/events")



@router.get(path='/{box_id}')
def get_by_box_id(
        # user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        box_id: int,
        db: Session = Depends(get_db),
):
    exists = db.query(event_models.Event) \
        .filter_by(box_id=box_id) \
        .first()
    if not exists:
        raise HTTPException(status_code=404)

    return exists


@router.put(path='/reset')
def reset(
        # user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        db: Session = Depends(get_db),
):
    events = db.query(event_models.Event).all()
    for e in events:
        for d in e.data:
            d['status'] = 'closed'

        flag_modified(e, "data")

    db.commit()
    return 'OK'


@router.put(path='/{box_id}')
def update_status(
        # user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        box_id: int,
        id: int,
        db: Session = Depends(get_db),
):
    exists = db.query(event_models.Event) \
        .filter_by(box_id=box_id) \
        .first()

    if not exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    for d in exists.data:
        if d['id'] == id:
            d['status'] = 'open'

    flag_modified(exists, "data")
    db.commit()
    return 'OK'
