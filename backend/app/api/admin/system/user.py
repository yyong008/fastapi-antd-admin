import app.services.sys.user as user_services

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.schemas.sys.user import UserCreate, UserDeleteByIds, UserUpdate
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/user", tags=["Admin System User"])


@router.get(
    "/", response_model=ResponseModel, summary="get all user", description="All user"
)
async def get_user(db: AsyncSession = Depends(get_db)):
    data = await user_services.get_user_list(db)
    return ResponseSuccessModel(data=data)


@router.get(
    "/{user_id}",
    response_model=ResponseModel,
    summary="get user by id",
    description="get user by id",
)
async def get_user_by_id(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_USER_READ)),
):
    data = await user_services.get_user_by_id(db, user_id)
    return ResponseSuccessModel(data=data)


@router.post(
    "/", response_model=ResponseModel, summary="get all user", description="All user"
)
async def create_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_USER_CREATE)),
):
    data = await user_services.create_user(db, user)
    return ResponseSuccessModel(data=data)


@router.put(
    "/{user_id}",
    response_model=ResponseModel,
    summary="get all user",
    description="All user",
)
async def update_user_by_id(
    user_id: int,
    item: UserUpdate,
    db: AsyncSession = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_USER_UPDATE)),
):
    data = await user_services.update_user_by_id(db, user_id, item)
    return ResponseSuccessModel(data=data)


@router.delete(
    "/",
    response_model=ResponseModel,
    summary="delete by user ids",
    description="delete by user ids",
)
async def delete_users_by_ids(
    ids: UserDeleteByIds,
    db: AsyncSession = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_USER_DELETE)),
):
    data = await user_services.delete_users_by_ids(db, ids.ids)
    return ResponseSuccessModel(data=data)


@router.delete(
    "/{user_id}",
    response_model=ResponseModel,
    summary="delete by user_id",
    description="delete by user_id",
)
async def delete_user_by_id(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_USER_DELETE)),
):
    data = await user_services.delete_user_by_id(db, user_id)
    return ResponseSuccessModel(data=data)
