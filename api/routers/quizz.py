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
        .filter_by(quizz_id=quizz.id)\
        .first()

    if not exists or not exists.status:
        return quizz

    return None


@router.put(path='/reset')
def reset(
        user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        db: Session = Depends(get_db),
):
    quizzs = db.query(quizz_models.QuizzUser)\
        .filter_by(user_id=user_id)\
        .all()

    for q in quizzs:
        db.delete(q)

    db.commit()
    return 'OK'


@router.put(path='/{box_id}')
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
