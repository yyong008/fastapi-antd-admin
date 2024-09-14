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



@router.post("/")
def create_dict_item():
    return {"success": "ok"}


@router.put("/{id}")
def update_dict_item_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_dict_item():
    return {"success": "ok"}
