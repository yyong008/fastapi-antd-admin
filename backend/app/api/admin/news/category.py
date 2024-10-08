from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
import app.services.news.news_category as nc_services
from app.schemas.response import RM, RMS
import app.schemas.news.news_category as nc_schemas
from app.utils.current_user import get_current_user
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/category", tags=["News Category"])


@router.get("/", response_model=RM)
async def get_news_category(
    page: int,
    pageSize: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.NEWS_CATEGORY_READ)),
):
    data = await nc_services.get_news_category_list_service(db, page, pageSize)
    return RMS(data=data)


@router.get("/{id}", response_model=RM)
async def get_news_category_by_id(
    _: bool = Depends(get_user_permissions(permissions.NEWS_CATEGORY_READ)),
):
    data = {}
    return RMS(data=data)


@router.post("/", response_model=RM)
async def create_news_category(
    category: nc_schemas.NewsCategoryCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.NEWS_CATEGORY_CREATE)),
):
    category_json_data = category.model_dump()
    data = await nc_services.create_news_category_service(db, category_json_data, current_user.id)
    return RMS(data=data)


@router.put("/{id}", response_model=RM)
async def update_news_category_by_id(
    id: int,
    category: nc_schemas.NewsCategoryUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.NEWS_CATEGORY_UPDATE)),
):
    category_json_data = category.model_dump()
    data = await nc_services.update_news_category_service(db, id, category_json_data, current_user.id)
    return RMS(data=data)


@router.delete("/", response_model=RM)
async def delete_news_category(
    ids_data: nc_schemas.NewsCategoryDeleteByIds,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.NEWS_CATEGORY_DELETE)),
):
    data = await nc_services.delete_news_category_by_ids_service(db, ids_data.ids)
    return RMS(data=data)
