from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.services.news.news_category import (
    create_news_category_service,
    delete_news_category_by_ids_service,
    get_news_category_list_service,
    update_news_category_service,
)
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.schemas.news.news_category import (
    NewsCategoryCreate,
    NewsCategoryDeleteByIds,
    NewsCategoryUpdate,
)
from app.utils.current_user import get_current_user
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/category", tags=["News Category"])


@router.get("/", response_model=ResponseModel)
async def get_news_category(
    page: int,
    pageSize: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.NEWS_CATEGORY_READ)),
):
    data = await get_news_category_list_service(db, page, pageSize)
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
async def get_news_category_by_id(
    _: bool = Depends(get_user_permissions(permissions.NEWS_CATEGORY_READ)),
):
    data = {}
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
async def create_news_category(
    category: NewsCategoryCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.NEWS_CATEGORY_CREATE)),
):
    category_json_data = category.model_dump()
    data = await create_news_category_service(db, category_json_data, current_user.id)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
async def update_news_category_by_id(
    id: int,
    category: NewsCategoryUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.NEWS_CATEGORY_UPDATE)),
):
    category_json_data = category.model_dump()
    data = await update_news_category_service(db, id, category_json_data, current_user.id)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
async def delete_news_category(
    ids_data: NewsCategoryDeleteByIds,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.NEWS_CATEGORY_DELETE)),
):
    data = await delete_news_category_by_ids_service(db, ids_data.ids)
    return ResponseSuccessModel(data=data)
