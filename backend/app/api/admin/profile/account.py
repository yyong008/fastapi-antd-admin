from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.services.profile.account import (
    get_profile_account_service,
    update_profile_account_service,
)
from app.schemas.response import RM, RMS
from app.utils.current_user import get_current_user
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/account", tags=["Account"])


@router.get("/", response_model=RM)
async def get_account_by_current_user(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.PROFILE_ACCOUNT_READ)),
):
    data = await get_profile_account_service(db, current_user.id)
    return RMS(data=data)


@router.put("/{id}", response_model=RM)
async def update_account_by_id(
    id: int,
    account: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.PROFILE_ACCOUNT_UPDATE)),
):
    data = await update_profile_account_service(db, id, account)
    return RMS(data=data)
