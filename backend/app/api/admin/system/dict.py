from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.sys.dict import get_dict_list

router = APIRouter(prefix="/dict", tags=["Dict"])


@router.get("/", response_model=ResponseModel)
def get_dict(page: int = 1, pageSize: int = 10, db: Session = Depends(get_db)):
    data = get_dict_list(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}")
def get_dict_by_id():
    data = {}
    return ResponseSuccessModel(data=data)


@router.post("/")
def create_dict():
    data = {}
    return ResponseSuccessModel(data=data)


@router.put("/{id}")
def update_dict_by_id():
    data = {}
    return ResponseSuccessModel(data=data)


@router.delete("/")
def delete_dict():
    data = {}
    return ResponseSuccessModel(data=data)
