from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.client import get_db
from app.schemas.response import RMS, RM
from app.services.docs.changelog import (
    get_user_list_service,
    create_change_log_service,
    update_change_log_service,
    delete_change_log_by_ids_service,
)
from app.utils.current_user import get_current_user
from app.schemas.docs.changelog import ChangeLogCreate, ChangeLogUpdate
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/changelog", tags=["Admin Docs ChangeLog"])


@router.get("/", response_model=RM)
async def docs_change_log(
    page: int,
    pageSize: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.DOCS_CHANGELOG_READ)),
):
    data = await get_user_list_service(db, page, pageSize)
    return RMS(data=data)


@router.post("/", response_model=RM)
async def create_docs_change_log(
    changelog: ChangeLogCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DEPT_CREATE)),
):
    changelog = changelog.model_dump()
    data = await create_change_log_service(db, changelog, current_user.id)
    return RMS(data=data)


@router.put("/{id}", response_model=RM)
async def update_docs_change_log(
    id: int,
    changelog: ChangeLogUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.DOCS_CHANGELOG_UPDATE)),
):
    changelog = changelog.model_dump()
    data = await update_change_log_service(db, id, changelog, current_user.id)
    return RMS(data=data)


@router.delete("/", response_model=RM)
async def delete_by_ids_docs_change_log(
    ids: list[int],
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.DOCS_CHANGELOG_DELETE)),
):
    data = await delete_change_log_by_ids_service(db, ids)
    return RMS(data=data)
