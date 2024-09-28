from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.sys.dict_item import (
    get_dict_item_list_service,
    get_dict_item_by_id_service,
    create_dict_item_service,
    update_dict_item_by_id_service,
    delete_dict_item_by_ids_service,
)
from app.db.client import get_db

router = APIRouter(prefix="/dict-item", tags=["Dict Item"])


@router.get("/", response_model=ResponseModel)
def get_dict_item(
    id: int, page: int = 1, pageSize: int = 10, db: Session = Depends(get_db)
):
    data = get_dict_item_list_service(id, page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_dict_item_by_id(id: int, db: Session = Depends(get_db)):
    data = get_dict_item_by_id_service(id, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_dict_item(dict_item: dict, db: Session = Depends(get_db)):
    data = create_dict_item_service(dict_item, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_dict_item_by_id(id: int, dict_item: dict, db: Session = Depends(get_db)):
    data = update_dict_item_by_id_service(id, dict_item, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_dict_item(ids: list[int], db: Session = Depends(get_db)):
    data = delete_dict_item_by_ids_service(ids, db)
    return ResponseSuccessModel(data=data)
