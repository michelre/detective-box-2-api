from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.database import get_db
from api.models import history as history_models
from api.schemas import history as history_schemas
from api.utils import auth as auth_utils

router = APIRouter(prefix="/history")


@router.get(path='/{box_id}')
def get_by_box(
        user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        box_id: int,
        db: Session = Depends(get_db),
):
    history = db \
        .query(history_models.History) \
        .filter_by(box_id=box_id) \
        .first()

    for d in history.data:
        exists = db\
            .query(history_models.HistoryUser)\
            .filter_by(history_id=history.id)\
            .filter_by(user_id=user_id)\
            .filter_by(ref_data=d['id'])\
            .first()

        if exists:
            d['status'] = exists.status

    return history


@router.put(path='/reset')
def reset(
        user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        db: Session = Depends(get_db),
):
    history = history_models.HistoryUser()
    history.reset(db, user_id)

    return 'OK'


@router.put(path='/{box_id}')
@router.put(path='/{box_id}/')
def update_status(
        user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        box_id: int,
        id: str,
        new_status: history_schemas.HistoryStatus,
        db: Session = Depends(get_db),
):
    data = db.query(history_models.History) \
        .filter_by(box_id=box_id) \
        .first()

    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    found = None
    for idx, d in enumerate(data.data):
        if d['id'] == id:
            found = idx

    if found is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    exists = db.query(history_models.HistoryUser) \
        .filter_by(history_id=data.id) \
        .filter_by(user_id=user_id) \
        .filter_by(ref_data=str(id)) \
        .first()

    if not exists:
        new = history_models.HistoryUser(
            user_id=user_id,
            history_id=data.id,
            ref_data=id,
            status=new_status.status
        )
        db.add(new)
    else:
        exists.status = new_status.status

    db.commit()
    return 'OK'
