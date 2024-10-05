from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.blog.blog_tag import get_blog_tag_list_service
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.db.client import get_db
from app.schemas.blog.blog_tag import BlogTagCreate, BlogTagDeleteByIds, BlogTagUpdate
from app.services.blog.blog_tag import (
    create_blog_tag_service,
    update_blog_tag_by_id_service,
    delete_blog_tag_by_ids_service,
)
from app.utils.current_user import get_current_user
import app.constant.permission as permissions
from app.deps.permission import get_user_permissions

router = APIRouter(prefix="/tag", tags=["Admin Blog Category Tag"])


@router.get("/", response_model=ResponseModel)
def get_blog_tag(
    page: int,
    pageSize: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_TAG_READ)),
):
    data = get_blog_tag_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_blog_tag_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_TAG_READ)),
):
    data = get_blog_tag_by_id(id)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_blog_tag(
    blog_tag: BlogTagCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_TAG_CREATE)),
):
    bt = blog_tag.model_dump()
    data = create_blog_tag_service(bt, current_user.id, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_blog_tag_by_id(
    id: int,
    blog_tag: BlogTagUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_TAG_UPDATE)),
):
    bt = blog_tag.model_dump()
    data = update_blog_tag_by_id_service(id, bt, current_user.id, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_blog_tag(
    ids: BlogTagDeleteByIds,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_TAG_DELETE)),
):
    data = delete_blog_tag_by_ids_service(ids.ids, db)
    return ResponseSuccessModel(data=data)
