from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.profile.link.link import (
    get_link_list_by_id_service,
    create_link_service,
    update_link_by_id_service,
    delete_link_by_ids_service,
)

router = APIRouter(prefix="/link", tags=["Link"])


# @router.get("/", response_model=ResponseModel)
# def get_link(id: int, page: int, pageSize: int, db: Session = Depends(get_db)):
#     data = {}
#     return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_link_by_id(id: int, page: int, pageSize: int, db: Session = Depends(get_db)):
    data = get_link_list_by_id_service(id, page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_link(link: dict, db: Session = Depends(get_db)):
    data = create_link_service(link, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_link_by_id(id: int, link: dict, db: Session = Depends(get_db)):
    data = update_link_by_id_service(id, link, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_link_by_ids(ids: list[int], db: Session = Depends(get_db)):
    data = delete_link_by_ids_service(ids, db)
    return ResponseSuccessModel(data=data)
