from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.db.client import get_db
from app.schemas.blog.blog_tag import BlogTagCreate, BlogTagDeleteByIds, BlogTagUpdate
import app.services.blog.blog_tag as bt_dals

from app.utils.current_user import get_current_user
import app.constant.permission as permissions
from app.deps.permission import get_user_permissions

router = APIRouter(prefix="/tag", tags=["Admin Blog Category Tag"])


@router.get("/", response_model=ResponseModel)
async def get_blog_tag(
    page: int,
    pageSize: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_TAG_READ)),
):
    data = await bt_dals.get_blog_tag_list_service(db, page, pageSize)
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
async def get_blog_tag_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_TAG_READ)),
):
    data = await get_blog_tag_by_id(id)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
async def create_blog_tag(
    blog_tag: BlogTagCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_TAG_CREATE)),
):
    bt = blog_tag.model_dump()
    data = await bt_dals.create_blog_tag_service(db, bt, current_user.id)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
async def update_blog_tag_by_id(
    id: int,
    blog_tag: BlogTagUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_TAG_UPDATE)),
):
    bt = blog_tag.model_dump()
    data = await bt_dals.update_blog_tag_by_id_service(db, id, bt, current_user.id)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
async def delete_blog_tag(
    ids: BlogTagDeleteByIds,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_TAG_DELETE)),
):
    data = await bt_dals.delete_blog_tag_by_ids_service(db, ids.ids)
    return ResponseSuccessModel(data=data)
