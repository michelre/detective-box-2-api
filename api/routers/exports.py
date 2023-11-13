from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from mailjet_rest import Client
from sqlalchemy.orm import Session
import csv

from api.config import settings
from api.database import get_db
from api.utils import auth as auth_utils
from api.models import users as users_model
from api.utils.auth import is_connected_admin_query
import base64

router = APIRouter(prefix="/exports")


@router.get('/users')
def user(
        token: Annotated[str, Depends(is_connected_admin_query)],
        db: Session = Depends(get_db),
):
    users = db.\
        query(users_model.User).\
        order_by(users_model.User.end_box3).\
        all()

    with open('/tmp/users.csv', 'w+') as f:
        writer = csv.writer(f)
        header = ['id', 'email', 'name', 'end_box1', 'end_box2', 'end_box3']
        writer.writerow(header)
        writer.writerows([[u.id, u.email, u.name, u.end_box1, u.end_box2, u.end_box3] for u in users])
        f.close()

    return FileResponse('/tmp/users.csv', filename='users.csv')

