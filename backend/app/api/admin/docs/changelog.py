from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.client import get_db
from app.schemas.response import ResponseSuccessModel, ResponseModel
from app.services.docs.changelog import (
    get_user_list_service,
    create_change_log_service,
    update_change_log_service,
    delete_change_log_by_ids_service,
)

router = APIRouter(prefix="/changelog", tags=["Admin Docs ChangeLog"])


@router.get("/", response_model=ResponseModel)
def docs_change_log(page: int, pageSize: int, db: Session = Depends(get_db)):
    data = get_user_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_docs_change_log(changelog: dict, db: Session = Depends(get_db)):
    data = create_change_log_service(changelog, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_docs_change_log(id: int, changelog: dict, db: Session = Depends(get_db)):
    data = update_change_log_service(id, changelog, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_by_ids_docs_change_log(ids: list[int], db: Session = Depends(get_db)):
    data = delete_change_log_by_ids_service(ids, db)
    return ResponseSuccessModel(data=data)
