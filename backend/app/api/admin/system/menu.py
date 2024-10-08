from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.response import RM, RMS
import app.services.sys.menu as menu_services
from app.db.client import get_db
from app.schemas.sys.menu import MenuCreate, MenuDeleteByIds, MenuUpdate
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/menu", tags=["Menu"])


@router.get("/", response_model=RM)
async def get_menu(
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_MENU_READ)),
):
    data = await menu_services.get_all_menu_service(db)
    return RMS(data=data)


@router.get("/tree", response_model=RM)
async def get_menu_tree(
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_MENU_READ)),
):
    data = await menu_services.get_menu_tree_service(db)
    return RMS(data=data)


@router.get("/tree/no-permission", response_model=RM)
async def get_menu_tree_no_permission(
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_MENU_READ)),
):
    data = await menu_services.get_menu_tree_no_permission_service(db)
    return RMS(data=data)


@router.get("/{id}")
async def get_menu_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_MENU_READ)),
):
    data = await menu_services.get_menu_by_id_service(db, id)
    return RMS(data=data)


@router.post("/")
async def create_menu(
    menu: MenuCreate,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_MENU_CREATE)),
):
    menu = menu.model_dump()
    data = await menu_services.create_menu_service(db, menu)
    return RMS(data=data)


@router.put("/{id}")
async def update_menu_by_id(
    id: int,
    menu: MenuUpdate,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_MENU_UPDATE)),
):
    data = await menu_services.update_menu_by_id_service(db, id, menu)
    return RMS(data=data)


@router.delete("/")
async def delete_menu(
    ids: MenuDeleteByIds,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_MENU_DELETE)),
):
    data = await menu_services.delete_menu_by_ids_service(db, ids.ids)
    return RMS(data=data)
