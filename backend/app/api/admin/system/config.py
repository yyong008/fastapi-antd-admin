from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.response import RM, RMS
import app.services.sys.config as cg_services
from app.db.client import get_db
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/config", tags=["Admin System Config"])


@router.get("/", response_model=RM)
async def get_config_list(
    page: int,
    pageSize: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTE_CONFIG_READ)),
):
    data = await cg_services.get_config_list_service(db, page, pageSize)
    return RMS(data=data)


@router.get("/{id}", response_model=RM)
async def get_config_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTE_CONFIG_READ)),
):
    data = await cg_services.get_config_by_id_service(db, id)
    return RMS(data=data)


@router.post("/", response_model=RM)
async def create_config(
    config: dict,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTE_CONFIG_CREATE)),
):
    data = await cg_services.create_config_service(db, config)
    return RMS(data=data)


@router.put("/{id}", response_model=RM)
async def update_config_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTE_CONFIG_UPDATE)),
):
    data = await cg_services.update_config_by_id_service(db, id)
    return RMS(data=data)


@router.delete("/", response_model=RM)
async def delete_config(
    ids: list,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTE_CONFIG_DELETE)),
):
    data = await cg_services.delete_config_by_ids_service(db, ids)
    return RMS(data=data)
