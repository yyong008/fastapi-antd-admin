from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.db.client import get_db
from app.services.news.news import (
    create_news_service,
    get_news_by_id_service,
    get_news_list_service,
    update_news_service,
)
from app.schemas.news.news import NewsCreate, NewsUpdate
from app.utils.current_user import get_current_user
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(tags=["News Main"])


@router.get("/{id}")
def get_news_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.NEWS_READ)),
):
    data = get_news_by_id_service(id, db)
    return ResponseSuccessModel(data=data)


@router.get("/", response_model=ResponseModel)
def get_news(
    category_id: int,
    page: int,
    pageSize: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.NEWS_READ)),
):
    data = get_news_list_service(category_id, page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_news(
    data: NewsCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.NEWS_CREATE)),
):
    news = data.model_dump()
    data = create_news_service(news, current_user.id, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_news(
    id: int,
    data: NewsUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.NEWS_UPDATE)),
):
    news = data.model_dump()
    data = update_news_service(id, news, current_user.id, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_news_by_ids(
    ids: List[int],
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.NEWS_DELETE)),
):
    data = delete_news_by_ids(ids, db)
    return ResponseSuccessModel(data=data)
