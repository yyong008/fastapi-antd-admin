import app.dal.sys.user as user_dal

from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.constant import NORMAL_USER
from app.models.system.role import Role
from app.models.system.user import User
from app.schemas.sys.user import UserCreate


def sign_in_service(username: str, password: str, db: Session):
    pass
