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


@router.get("/{id}", response_model=ResponseModel)
def get_link_category_by_id():
    data = {}
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_link_category():
    data = {}
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_link_category_by_id():
    data = {}
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_link_by_ids_category():
    data = {}
    return ResponseSuccessModel(data=data)
