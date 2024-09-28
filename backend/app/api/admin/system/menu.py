from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.sys.menu import (
    get_all_menu_service,
    get_menu_tree_service,
    get_menu_by_id_service,
    create_menu_service,
    update_menu_by_id_service,
    delete_menu_by_ids_service,
)
from app.db.client import get_db

router = APIRouter(prefix="/menu", tags=["Menu"])


@router.get("/", response_model=ResponseModel)
def get_menu(db: Session = Depends(get_db)):
    data = get_all_menu_service(db)
    return ResponseSuccessModel(data=data)


@router.get("/tree", response_model=ResponseModel)
def get_menu_tree(db: Session = Depends(get_db)):
    data = get_menu_tree_service(db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}")
def get_menu_by_id(id: int, db: Session = Depends(get_db)):
    data = get_menu_by_id_service(id, db)
    return ResponseSuccessModel(data=data)


@router.post("/")
def create_menu(menu: dict, db: Session = Depends(get_db)):
    data = create_menu_service(menu, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}")
def update_menu_by_id(id: int, menu: dict, db: Session = Depends(get_db)):
    data = update_menu_by_id_service(id, menu, db)
    return ResponseSuccessModel(data=data)


@router.delete("/")
def delete_menu(ids: list[int], db: Session = Depends(get_db)):
    data = delete_menu_by_ids_service(ids, db)
    return ResponseSuccessModel(data=data)
