from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated, List
from sqlalchemy.orm import Session

from api.database import get_db
from api.models import objective as objective_models
from api.utils import auth as auth_utils
from sqlalchemy.orm.attributes import flag_modified
from api.utils import in_array

from api.schemas.help import Help

router = APIRouter(prefix="/objectives")


@router.get(path='/')
def get(
        # user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        db: Session = Depends(get_db),
):
    return db.query(objective_models.Objective).all()


@router.put(path='/reset')
def reset(
        # user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        db: Session = Depends(get_db),
) -> str:
    data = db.query(objective_models.Objective).all()

    for d in data:
        for e in d.data:
            if not in_array([11, 12, 13, 22, 31, 32], e['id']):
                e['status'] = 'closed'
            else:
                e['status'] = 'open'

        flag_modified(d, "data")
    db.commit()

    return 'OK'


@router.put(path='/{box_id}')
def update_status(
        box_id: int,
        id: int,
        db: Session = Depends(get_db),
):
    data = db.query(objective_models.Objective) \
        .filter_by(box_id=box_id) \
        .first()

    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    for d in data.data:
        if d['id'] == id:
            d['status'] = 'closed'

    flag_modified(data, "data")
    db.commit()
    return 'OK'
