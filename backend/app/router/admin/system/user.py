import app.services.sys.user as user_services

from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.schemas.sys.user import UserCreate, UserUpdate

router = APIRouter(prefix="/user", tags=["Admin System User"])


@router.get(
    "/", response_model=ResponseModel, summary="get all user", description="All user"
)
def get_user(db: Session = Depends(get_db)):
    data = user_services.get_user_list(db)
    return ResponseSuccessModel(data=data)


@router.get(
    "/{user_id}",
    response_model=ResponseModel,
    summary="get user by id",
    description="get user by id",
)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    data = user_services.get_user_by_id(user_id, db)
    return ResponseSuccessModel(data=data)


@router.post(
    "/", response_model=ResponseModel, summary="get all user", description="All user"
)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    data = user_services.create_user(user, db)
    return ResponseSuccessModel(data=data)


@router.put(
    "/{user_id}",
    response_model=ResponseModel,
    summary="get all user",
    description="All user",
)
def update_user_by_id(user_id: int, item: UserUpdate, db: Session = Depends(get_db)):
    data = user_services.update_user_by_id(user_id, item, db)
    return ResponseSuccessModel(data=data)


@router.delete(
    "/",
    response_model=ResponseModel,
    summary="delete by user ids",
    description="delete by user ids",
)
def delete_users_by_ids(ids: List[int], db: Session = Depends(get_db)):
    data = user_services.delete_users_by_ids(ids, db)
    return ResponseSuccessModel(data=data)


@router.delete(
    "/{user_id}",
    response_model=ResponseModel,
    summary="delete by user_id",
    description="delete by user_id",
)
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    data = user_services.delete_user_by_id(user_id, db)
    return ResponseSuccessModel(data=data)