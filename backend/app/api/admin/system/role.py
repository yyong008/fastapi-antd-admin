from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.client import get_db
from app.services.sys.role import (
    get_all_role_service,
    get_role_by_id_service,
    create_role_service,
    update_role_by_id_service,
    delete_role_by_ids_service,
)
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.schemas.sys.role import RoleCreate, RoleUpdate, RoleDeleteByIds
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/role", tags=["Role"])


@router.get("/", response_model=ResponseModel)
def get_all_roles(
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_ROLE_READ)),
):
    data = get_all_role_service(db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}")
def get_role_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_ROLE_READ)),
):
    data = get_role_by_id_service(id, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_role(
    role: RoleCreate,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_ROLE_CREATE)),
):
    data = create_role_service(role, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_role_by_id(
    id: int,
    item: RoleUpdate,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_ROLE_UPDATE)),
):
    data = update_role_by_id_service(id, item, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_role(
    ids: RoleDeleteByIds,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_ROLE_DELETE)),
):
    data = delete_role_by_ids_service(ids.ids, db)
    return ResponseSuccessModel(data=data)
