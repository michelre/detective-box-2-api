from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated, List
from sqlalchemy.orm import Session
from sqlalchemy.orm.attributes import flag_modified

from api.database import get_db
from api.models import history as history_models
from api.utils import auth as auth_utils

from api.schemas.history import History

router = APIRouter(prefix="/history")


@router.get(path='/{box_id}')
def get_by_box(
        # user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        box_id: str,
        db: Session = Depends(get_db),
):
    return db.query(history_models.History) \
        .filter_by(box_id=box_id) \
        .all()


@router.put(path='/reset')
def reset(
        db: Session = Depends(get_db),
):
    data = db.query(history_models.History).all()

    for d in data:
        for e in d.data:
            e['status'] = False

        flag_modified(d, "data")
    db.commit()
    return "OK"


@router.put(path='/{box_id}')
def update_status(
        box_id: int,
        id: str,
        db: Session = Depends(get_db),
):
    data = db.query(history_models.History) \
        .filter_by(box_id=box_id) \
        .first()

    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    for d in data.data:
        if d['id'] == id:
            d['status'] = True

    flag_modified(data, "data")
    db.commit()
    return data
