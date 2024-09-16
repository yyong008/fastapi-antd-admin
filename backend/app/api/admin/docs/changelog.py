from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.client import get_db
from app.schemas.response import ResponseSuccessModel,ResponseModel
from app.services.docs.changelog import get_user_list_service

router = APIRouter(prefix="/changelog", tags=["Admin Docs ChangeLog"])


@router.get("/", response_model=ResponseModel)
def docs_change_log(page: int, pageSize: int, db: Session = Depends(get_db)):
    data = get_user_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.post("/")
def create_docs_change_log():
    return {"success": "ok"}


@router.put("/{id}")
def update_docs_change_log():
    return {"success": "ok"}


@router.delete("/{id}")
def delete_by_ids_docs_change_log():
    return {"success": "ok"}
 