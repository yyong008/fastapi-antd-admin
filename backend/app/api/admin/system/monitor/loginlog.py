from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.db.client import get_db

from app.schemas.response import RM, RMS
from app.schemas.sys.loginlog import LoginlogCreateUpdateSchema
import app.services.sys.loginlog as loginlog_services
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/login-log")


@router.get("/", response_model=RM)
async def get_loginlog_list(
    page: int = 1,
    pageSize: int = 10,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_MONITOR_LOGIN_LOG_LIST)),
):
    data = await loginlog_services.get_loginlog_list(db, page, pageSize)
    return RMS(data=data)


@router.post("/", response_model=RM)
async def create_loginlog(
    request: Request,
    loginlog: LoginlogCreateUpdateSchema,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_MONITOR_LOGIN_LOG_CREATE)),
):
    data = await loginlog_services.create_loginlog(db,request,  userId="", name="")
    return RMS(data=data)
