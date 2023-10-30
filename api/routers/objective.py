from fastapi import APIRouter, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session

from api.database import get_db
from api.models import objective as objective_models
from api.utils import auth as auth_utils

from api.schemas.help import Help

router = APIRouter(prefix="/objectives")


@router.get(path='/')
def get(
        user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        db: Session = Depends(get_db),
) -> List[Help]:
    return db.query(objective_models.Objective).all()
