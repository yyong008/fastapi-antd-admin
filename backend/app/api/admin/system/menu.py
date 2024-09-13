from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.sys.menu import get_all_menu_service
from app.db.client import get_db

router = APIRouter(prefix="/menu", tags=["Menu"])


@router.get("/", response_model=ResponseModel)
def get_menu(db: Session = Depends(get_db)):
    data = get_all_menu_service(db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}")
def get_menu_by_id():
    return {"success": "ok"}


@router.post("/")
def create_menu():
    return {"success": "ok"}


@router.put("/{id}")
def update_menu_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_menu():
    return {"success": "ok"}
