from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.services.news.news_category import (
    create_news_category_service,
    delete_news_category_by_ids_service,
    get_news_category_list_service,
    update_news_category_service
)
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.schemas.news.news_category import NewsCategoryCreate, NewsCategoryDeleteByIds, NewsCategoryUpdate
from app.utils.current_user import get_current_user

router = APIRouter(prefix="/category", tags=["News Category"])


@router.get("/", response_model=ResponseModel)
def get_news_category(page: int, pageSize: int, db: Session = Depends(get_db)):
    data = get_news_category_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_news_category_by_id():
    data = {}
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_news_category(
    category: NewsCategoryCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    category_json_data = category.model_dump()
    data = create_news_category_service(category_json_data, current_user.id, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_news_category_by_id(
    id: int,
    category: NewsCategoryUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    category_json_data = category.model_dump()
    data = update_news_category_service(id, category_json_data, current_user.id, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_news_category(ids_data: NewsCategoryDeleteByIds, db: Session = Depends(get_db)):
    data = delete_news_category_by_ids_service(ids_data.ids, db)
    return ResponseSuccessModel(data=data)
