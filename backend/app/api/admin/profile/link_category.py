from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.profile.link.category import get_link_category_list_service

router = APIRouter(prefix="/link/category", tags=["Link Category"])


@router.get("/", response_model=ResponseModel)
def get_link_category(page: int = 1, per_page: int = 10, db: Session = Depends(get_db)):
    data= get_link_category_list_service(page, per_page, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}")
def get_link_category_by_id():
    return {"success": "ok"}


@router.post("/")
def create_link_category():
    return {"success": "ok"}


@router.put("/{id}")
def update_link_category_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_link_category():
    return {"success": "ok"}
