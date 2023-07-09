import os

from fastapi import APIRouter, HTTPException, status, Depends
from alembic import command
from alembic.config import Config
from alembic.util.exc import CommandError
from api.utils.auth import is_connected_admin
from typing import Annotated


router = APIRouter(prefix='/db')


@router.post(path='/migrate', summary="Run database migration")
def run_db_migration(is_connected_admin: Annotated[bool, Depends(is_connected_admin)]):
    """Database migration restrected to super admin"""
    try:
        config = Config('alembic.ini')
        command.upgrade(config=config, revision="head")
        return 'OK'
    except CommandError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error executing migration"
        )
