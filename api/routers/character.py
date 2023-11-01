from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated, List
from sqlalchemy.orm import Session
from sqlalchemy.orm.attributes import flag_modified

from api.database import get_db
from api.models import character as character_models
from api.utils import auth as auth_utils
from api.utils import in_array

from api.schemas.help import Help

router = APIRouter(prefix="/characters")


@router.get(path='/')
def get(
        # user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        db: Session = Depends(get_db),
) -> List[Help]:
    return db.query(character_models.Character).all()


@router.get(path='/{id}')
def get_by_character(
    id: int,
    db: Session = Depends(get_db),
):
    # TODO: Retourne la liste des data
    return db.query(character_models.RequestCharacter) \
        .filter_by(character_id=id) \
        .all()

@router.put(path='/{character_id}/{box_id}')
def update_status(
        character_id: int,
        box_id: int,
        answer: str,
        db: Session = Depends(get_db),
):
    data = db.query(character_models.RequestCharacter) \
        .filter_by(character_id=character_id) \
        .filter_by(box_id=box_id) \
        .first()

    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    for d in data.data:
        if type(d['ask']) == str and d['ask'] == answer:
            d['status'] = True
        if not type(d['ask']) == str and in_array(d['ask'], answer):
            d['status'] = True

    flag_modified(data, "data")
    db.commit()
    return data
