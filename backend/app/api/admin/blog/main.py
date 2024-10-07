from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.db.client import get_db
import app.services.blog.blog as bg_services
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.schemas.blog.blog import BlogCreate, BlogUpdate, BlogDeleteByIds
from app.utils.current_user import get_current_user
import app.constant.permission as permissions
from app.deps.permission import get_user_permissions

router = APIRouter(tags=["Admin Blog Main"])


@router.get("/{id}", response_model=ResponseModel)
async def get_blog_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_READ)),
):
    data = await bg_services.get_blog_by_id_service(db, id)
    return ResponseSuccessModel(data=data)


@router.get("/", response_model=ResponseModel)
async def get_blogs(
    page: int = Query(1, description="当前页码"),
    pageSize: int = Query(10, description="每页条数"),
    categoryId: Optional[int] = Query(None, description="按分类 ID 搜索"),
    tagId: Optional[int] = Query(None, description="按标签 ID 搜索"),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_READ)),
):
    data = await bg_services.get_blog_list_service(db, categoryId, tagId, page, pageSize)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
async def create_blog(
    blog: BlogCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_CATEGORY_UPDATE)),
):
    blog = blog.model_dump()
    data = await bg_services.create_blog_service(db, blog, current_user.id)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
async def update_blog(
    id: int,
    blog: BlogUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_UPDATE)),
):
    blog = blog.model_dump()
    data = await bg_services.update_blog_service(db, id, current_user.id, blog)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
async def delete_blog_by_ids(
    ids: BlogDeleteByIds,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_DELETE)),
):
    data = await bg_services.delete_blog_by_ids_service(db, ids)
    return ResponseSuccessModel(data=data)
