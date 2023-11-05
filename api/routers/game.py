from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated, List
from sqlalchemy.orm import Session

from api.database import get_db
from api.models import box as box_models
from api.models import quizz as quizz_models
from api.models import help as help_models
from api.models import objective as objective_models
from api.models import history as history_models
from api.models import character as character_models
from api.schemas import box as box_schemas
from api.utils import auth as auth_utils
from api.enums import BoxStatus

from api.schemas.box import Box

router = APIRouter(prefix="/game")


@router.put(path='/reset')
def reset_all(
        user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        db: Session = Depends(get_db),
):
    box = box_models.UserBox()
    box.reset(db, user_id)

    quizz = quizz_models.QuizzUser()
    quizz.reset(db, user_id)

    help = help_models.HelpUser()
    help.reset(db, user_id)

    objective = objective_models.ObjectiveUser()
    objective.reset(db, user_id)

    history = history_models.HistoryUser()
    history.reset(db, user_id)

    character = character_models.RequestCharacter()
    character.reset(db, user_id)

    return 'OK'
