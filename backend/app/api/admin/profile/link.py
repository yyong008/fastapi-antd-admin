from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.profile.link.link import get_link_list_by_id_service

router = APIRouter(prefix="/link", tags=["Link"])


# @router.get("/", response_model=ResponseModel)
# def get_link(id: int, page: int, pageSize: int, db: Session = Depends(get_db)):
#     data = {}
#     return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_link_by_id(id: int, page: int, pageSize: int, db: Session = Depends(get_db)):
    data = get_link_list_by_id_service(id, page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.post("/")
def create_link():
    return {"success": "ok"}


@router.put("/{id}")
def update_link_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_link():
    return {"success": "ok"}
