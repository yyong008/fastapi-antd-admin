from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.response import RM, RMS
from app.db.client import get_db
import app.services.news.news as ns
from app.schemas.news.news import NewsCreate, NewsUpdate
from app.utils.current_user import get_current_user
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(tags=["News Main"])


@router.get("/{id}")
async def get_news_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.NEWS_READ)),
):
    data = await ns.get_news_by_id_service(db, id)
    return RMS(data=data)


@router.get("/", response_model=RM)
async def get_news(
    category_id: int,
    page: int,
    pageSize: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.NEWS_READ)),
):
    data = await ns.get_news_list_service(db, category_id, page, pageSize)
    return RMS(data=data)


@router.post("/", response_model=RM)
async def create_news(
    data: NewsCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.NEWS_CREATE)),
):
    news = data.model_dump()
    data = await ns.create_news_service(db, news, current_user.id)
    return RMS(data=data)


@router.put("/{id}", response_model=RM)
async def update_news(
    id: int,
    data: NewsUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.NEWS_UPDATE)),
):
    news = data.model_dump()
    data = await ns.update_news_service(db, id, news, current_user.id)
    return RMS(data=data)


@router.delete("/", response_model=RM)
async def delete_news_by_ids(
    ids: List[int],
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.NEWS_DELETE)),
):
    data = await ns.delete_news_by_ids_service(db, ids)
    return RMS(data=data)
