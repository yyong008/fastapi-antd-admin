from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.client import get_db
import app.services.sys.role as r_services
from app.schemas.response import RM, RMS
from app.schemas.sys.role import RoleCreate, RoleUpdate, RoleDeleteByIds
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/role", tags=["Role"])


@router.get("/", response_model=RM)
async def get_all_roles(
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_ROLE_READ)),
):
    data = await r_services.get_all_role_service(db)
    return RMS(data=data)


@router.get("/{id}")
async def get_role_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_ROLE_READ)),
):
    data = await r_services.get_role_by_id_service(db, id)
    return RMS(data=data)


@router.post("/", response_model=RM)
async def create_role(
    role: RoleCreate,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_ROLE_CREATE)),
):
    data = await r_services.create_role_service(db, role)
    return RMS(data=data)


@router.put("/{id}", response_model=RM)
async def update_role_by_id(
    id: int,
    item: RoleUpdate,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_ROLE_UPDATE)),
):
    data = await r_services.update_role_by_id_service(db, id, item)
    return RMS(data=data)


@router.delete("/", response_model=RM)
async def delete_role(
    ids: RoleDeleteByIds,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_ROLE_DELETE)),
):
    data = await r_services.delete_role_by_ids_service(db, ids.ids)
    return RMS(data=data)
