from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.sys.menu import (
    get_all_menu_service,
    get_menu_tree_no_permission_service,
    get_menu_tree_service,
    get_menu_by_id_service,
    create_menu_service,
    update_menu_by_id_service,
    delete_menu_by_ids_service,
)
from app.db.client import get_db
from app.schemas.sys.menu import MenuCreate, MenuDeleteByIds, MenuUpdate
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/menu", tags=["Menu"])


@router.get("/", response_model=ResponseModel)
def get_menu(
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_MENU_READ)),
):
    data = get_all_menu_service(db)
    return ResponseSuccessModel(data=data)


@router.get("/tree", response_model=ResponseModel)
def get_menu_tree(
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_MENU_READ)),
):
    data = get_menu_tree_service(db)
    return ResponseSuccessModel(data=data)


@router.get("/tree/no-permission", response_model=ResponseModel)
def get_menu_tree_no_permission(
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_MENU_READ)),
):
    data = get_menu_tree_no_permission_service(db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}")
def get_menu_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_MENU_READ)),
):
    data = get_menu_by_id_service(id, db)
    return ResponseSuccessModel(data=data)


@router.post("/")
def create_menu(
    menu: MenuCreate,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_MENU_CREATE)),
):
    menu = menu.model_dump()
    data = create_menu_service(menu, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}")
def update_menu_by_id(
    id: int,
    menu: MenuUpdate,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_MENU_UPDATE)),
):
    data = update_menu_by_id_service(id, menu, db)
    return ResponseSuccessModel(data=data)


@router.delete("/")
def delete_menu(
    ids: MenuDeleteByIds,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_MENU_DELETE)),
):
    data = delete_menu_by_ids_service(ids.ids, db)
    return ResponseSuccessModel(data=data)
