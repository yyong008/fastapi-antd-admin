from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.blog.blog_category import (
    get_blog_category_list_service,
    get_blog_category_by_id_service,
    create_blog_category_service,
    delete_blog_category_by_ids_service,
    update_blog_category_by_id_service,
)
from app.schemas.blog.blog_category import (
    BlogCategoryCreate,
    BlogCategoryDeleteByIds,
    BlogCategoryUpdate,
)
from app.utils.current_user import get_current_user
import app.constant.permission as permissions
from app.deps.permission import get_user_permissions

router = APIRouter(prefix="/category", tags=["Admin Blog Category"])


@router.get("/", response_model=ResponseModel)
def get_blog_category(
    page: int,
    pageSize: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_CATEGORY_READ)),
):
    data = get_blog_category_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_blog_category_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_CATEGORY_READ)),
):
    data = get_blog_category_by_id_service(id, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_blog_category(
    bc: BlogCategoryCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_CATEGORY_CREATE)),
):
    bc = bc.model_dump()
    data = create_blog_category_service(bc, current_user.id, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_blog_category_by_id(
    id: int,
    bc: BlogCategoryUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_CATEGORY_UPDATE)),
):
    bc = bc.model_dump()
    data = update_blog_category_by_id_service(id, bc, current_user.id, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_blog_category(
    ids: BlogCategoryDeleteByIds,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_CATEGORY_DELETE)),
):
    data = delete_blog_category_by_ids_service(ids.ids, db)
    return ResponseSuccessModel(data=data)
