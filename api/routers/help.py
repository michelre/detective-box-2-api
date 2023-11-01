from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.database import get_db
from api.models import help as help_models
from api.schemas.help import Help, Status
from api.utils import auth as auth_utils
from api.utils import in_array
from sqlalchemy.orm.attributes import flag_modified

router = APIRouter(prefix="/help")


@router.get(path='/')
def get(
        # user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        db: Session = Depends(get_db),
) -> List[Help]:
    return db.query(help_models.Help).all()


@router.get(path='/{box_id}')
def get_by_box(
        box_id: int,
        # user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        db: Session = Depends(get_db),
):
    return db \
        .query(help_models.Help) \
        .filter_by(box_id=box_id) \
        .all()


@router.put(path='/reset')
def reset(
        # user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        db: Session = Depends(get_db),
) -> str:
    data = db.query(help_models.Help).all()

    for d in data:
        for e in d.data:
            if not in_array([
                'box1help1', 'box1help2', 'box1help3',
                'box2help1',
                'box3help1', 'box3help2',
            ], e['id']):
                e['status'] = 'closed'
            else:
                e['status'] = 'open'

        flag_modified(d, "data")
    db.commit()

    return 'OK'

@router.put(path='/{id}')
def update(
        id: int,
        new_status: Status,
        # user_id: Annotated[int, Depends(auth_utils.get_connected_user_id)],
        db: Session = Depends(get_db),
) -> Status:
    exists = db.query(help_models.Help) \
        .filter_by(id=id) \
        .first()

    if not exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user_not_exists"
        )

    exists.status = new_status.status
    db.commit()
    return exists
