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
from app.utils.current_user import get_current_user
from app.schemas.docs.changelog import ChangeLogCreate, ChangeLogUpdate

router = APIRouter(prefix="/changelog", tags=["Admin Docs ChangeLog"])


@router.get("/", response_model=ResponseModel)
def docs_change_log(page: int, pageSize: int, db: Session = Depends(get_db)):
    data = get_user_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_docs_change_log(
    changelog: ChangeLogCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    changelog = changelog.model_dump()
    data = create_change_log_service(changelog, current_user.id, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_docs_change_log(
    id: int,
    changelog: ChangeLogUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    changelog = changelog.model_dump()
    data = update_change_log_service(id, changelog, current_user.id, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_by_ids_docs_change_log(ids: list[int], db: Session = Depends(get_db)):
    data = delete_change_log_by_ids_service(ids, db)
    return ResponseSuccessModel(data=data)
