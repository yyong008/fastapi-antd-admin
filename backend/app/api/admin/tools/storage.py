from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.tools.storage import get_tools_storage_list_service

router = APIRouter(prefix="/storage", tags=["Storage"])


@router.get("/", response_model=ResponseModel)
def get_storage_list(
   page: int = Query(1, description="当前页码"),
    pageSize: int = Query(10, description="每页条数"),
    db: Session = Depends(get_db),
):
    data = get_tools_storage_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}")
def get_storage_by_id():
    return {"success": "ok"}


@router.post("/")
def create_storage():
    return {"success": "ok"}


@router.put("/{id}")
def update_storage_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_storage():
    return {"success": "ok"}
