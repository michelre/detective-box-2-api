from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.database import get_db
from api.models import quizz as quizz_models
from api.schemas.quizz import QuizzStatus
from api.utils import auth as auth_utils

router = APIRouter(prefix="/quizz")


@router.get(path='/{box_id}')
def get_by_id(
        user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        box_id: int,
        db: Session = Depends(get_db),
):
    quizz = db.query(quizz_models.Quizz) \
        .filter_by(box_id=box_id) \
        .first()

    if not quizz:
        raise HTTPException(status_code=404)

    exists = db.query(quizz_models.QuizzUser)\
        .filter_by(quizz_id=quizz.id) \
        .filter_by(user_id=user_id) \
        .first()

    if exists:
        quizz.status = exists.status

    return quizz


@router.put(path='/reset')
def reset(
        user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        db: Session = Depends(get_db),
):
    quizz = quizz_models.QuizzUser()
    quizz.reset(db, user_id)

    return 'OK'


@router.put(path='/{box_id}')
@router.put(path='/{box_id}/')
def update_status(
        user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        box_id: int,
        new_status: QuizzStatus,
        db: Session = Depends(get_db),
):
    quizz = db.query(quizz_models.Quizz) \
        .filter_by(box_id=box_id) \
        .first()

    if not quizz:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="quizz_not_exists"
        )

    exists = db.query(quizz_models.QuizzUser)\
        .filter_by(quizz_id=quizz.id)\
        .filter_by(user_id=user_id)\
        .first()

    if not exists:
        new = quizz_models.QuizzUser(
            user_id=user_id,
            quizz_id=quizz.id,
            status=new_status.status
        )
        db.add(new)
    else:
        exists.status = new_status.status

    db.commit()
    return "OK"
