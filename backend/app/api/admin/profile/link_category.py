from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.profile.link.category import (
    get_link_category_list_service,
    get_link_category_by_id_service,
    create_link_category_service,
    update_link_category_service,
    delete_link_category_by_ids_service
)

router = APIRouter(prefix="/link/category", tags=["Link Category"])


@router.get("/", response_model=ResponseModel)
def get_link_category(page: int = 1, per_page: int = 10, db: Session = Depends(get_db)):
    data = get_link_category_list_service(page, per_page, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_link_category_by_id(id: int, db: Session = Depends(get_db)):
    data = get_link_category_by_id_service(id, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_link_category(id: int, db: Session = Depends(get_db)):
    data = create_link_category_service(id, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_link_category_by_id(id: int, db: Session = Depends(get_db)):
    data = update_link_category_service(id, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_link_by_ids_category(ids: list[int], db: Session = Depends(get_db)):
    data = delete_link_category_by_ids_service(ids, db)
    return ResponseSuccessModel(data=data)
