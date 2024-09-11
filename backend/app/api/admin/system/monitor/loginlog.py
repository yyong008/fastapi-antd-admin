from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.db.client import get_db

from app.schemas.response import ResponseSuccessModel
from app.schemas.sys.loginlog import LoginlogCreateUpdateSchema
import app.services.sys.loginlog as loginlog_services

router = APIRouter(prefix="/loginlog")


@router.get("/")
def get_loginlog_list(page: int = 1, pageSize: int = 10, db: Session = Depends(get_db)):
    data = loginlog_services.get_loginlog_list(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.post("/")
def create_loginlog(
    request: Request,
    loginlog: LoginlogCreateUpdateSchema,
    db: Session = Depends(get_db),
):
    data = loginlog_services.create_loginlog(request, db, userId="", name="")
    return ResponseSuccessModel(data=data)
