from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated, List
from sqlalchemy.orm import Session

from api.database import get_db
from api.models import quizz as quizz_models
from api.utils import auth as auth_utils

from api.schemas.quizz import Quizz, QuizzStatus

router = APIRouter(prefix="/quizz")


@router.get(path='/')
def get(
        # user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        db: Session = Depends(get_db),
) -> List[Quizz]:
    return db.query(quizz_models.Quizz).all()


@router.get(path='/{id}')
def get_by_id(
        # user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        id: int,
        db: Session = Depends(get_db),
):
    exists = db.query(quizz_models.Quizz) \
        .filter_by(id=id) \
        .first()
    if not exists:
        raise HTTPException(status_code=404)

    if not exists.status:
        return exists

    return None

@router.put(path='/{id}')
def update_status(
        id: int,
        status: QuizzStatus,
        # user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        db: Session = Depends(get_db),
):
    exists = db.query(quizz_models.Quizz) \
        .filter_by(id=id) \
        .first()

    if not exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="quizz_not_exists"
        )

    exists.status = status.status
    db.commit()
    return status
