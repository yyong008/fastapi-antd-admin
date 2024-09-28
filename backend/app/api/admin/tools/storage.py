from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.tools.storage import (
    get_tools_storage_list_service,
    get_tools_storage_by_id_service,
    create_tools_storage_service,
    update_tools_storage_by_id_service,
    delete_tools_storage_by_ids_service,
)

router = APIRouter(prefix="/storage", tags=["Storage"])


@router.get("/", response_model=ResponseModel)
def get_storage_list(
    page: int = Query(1, description="当前页码"),
    pageSize: int = Query(10, description="每页条数"),
    db: Session = Depends(get_db),
):
    data = get_tools_storage_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_storage_by_id(id: int, db: Session = Depends(get_db)):
    data = get_tools_storage_by_id_service(id, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_storage(storage: dict, db: Session = Depends(get_db)):
    data = create_tools_storage_service(storage, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_storage_by_id(id: int, storage: dict, db: Session = Depends(get_db)):
    data = update_tools_storage_by_id_service(id, storage, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_storage(ids: list[int], db: Session = Depends(get_db)):
    data = delete_tools_storage_by_ids_service(ids, db)
    return ResponseSuccessModel(data=data)
