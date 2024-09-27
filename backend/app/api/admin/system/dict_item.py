from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.sys.dict_item import get_dict_item_list
from app.db.client import get_db

router = APIRouter(prefix="/dict-item", tags=["Dict Item"])


@router.get("/{id}", response_model=ResponseModel)
def get_dict_item(id: int, page: int = 1, pageSize: int = 10, db: Session = Depends(get_db)):
    data = get_dict_item_list(id, page, pageSize, db)
    return ResponseSuccessModel(data=data)

@router.post("/", response_model=ResponseModel)
def create_dict_item():
    data = {}
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_dict_item_by_id():
    data = {}
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_dict_item():
    data = {}
    return ResponseSuccessModel(data=data)
