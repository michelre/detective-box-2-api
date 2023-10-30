from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated, List
from sqlalchemy.orm import Session

from api.database import get_db
from api.models import box as box_models
from api.utils import auth as auth_utils
from api.enums import BoxStatus

from api.schemas.box import Box

router = APIRouter(prefix="/box")


@router.get(path='/')
def get(
        # user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        db: Session = Depends(get_db),
):
    return db.query(box_models.Box).all()


@router.put(path='/{id}')
def update(
        id: int,
        box: Box,
        # user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        db: Session = Depends(get_db),
) -> Box:
    exists = db.query(box_models.Box) \
        .filter_by(id=id) \
        .first()

    if not exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user_not_exists"
        )

    exists.status = box.status
    db.commit()
    return exists


@router.put(path='/reset')
def reset(
        # user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        db: Session = Depends(get_db),
):
    boxes = db.query(box_models.Box).all()
    for box in boxes:
        if box.id == 1:
            box.status = BoxStatus.open
        else:
            box.status = BoxStatus.closed

    db.commit()
    return boxes
