from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.sys.dict import (
    get_dict_lists_service,
    get_dict_by_id_service,
    create_dict_service,
    update_dict_by_id_service,
    delete_dict_by_ids_service,
)

router = APIRouter(prefix="/dict", tags=["Dict"])


@router.get("/", response_model=ResponseModel)
def get_dict(page: int = 1, pageSize: int = 10, db: Session = Depends(get_db)):
    data = get_dict_lists_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}")
def get_dict_by_id(id: int, db: Session = Depends(get_db)):
    data = get_dict_by_id_service(id, db)
    return ResponseSuccessModel(data=data)


@router.post("/")
def create_dict(dict: dict, db: Session = Depends(get_db)):
    data = create_dict_service(dict, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}")
def update_dict_by_id(id: int, dict: dict, db: Session = Depends(get_db)):
    data = update_dict_by_id_service(id, dict, db)
    return ResponseSuccessModel(data=data)


@router.delete("/")
def delete_dict(ids: list, db: Session = Depends(get_db)):
    data = delete_dict_by_ids_service(ids, db)
    return ResponseSuccessModel(data=data)
