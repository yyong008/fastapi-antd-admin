from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.client import get_db
from app.schemas.response import RM, RMS
from app.deps.permission import get_user_permissions
from app.utils.current_user import get_current_user

import app.services.blog.blog_category as bcs
import app.schemas.blog.blog_category as bcm
import app.constant.permission as permissions

router = APIRouter(prefix="/category", tags=["Admin Blog Category"])


@router.get("/", response_model=RM)
async def get_blog_category(
    page: int,
    pageSize: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_CATEGORY_READ)),
):
    data = await bcs.get_blog_category_list_service(db, page, pageSize)
    return RMS(data=data)


@router.get("/{id}", response_model=RM)
async def get_blog_category_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_CATEGORY_READ)),
):
    data = await bcs.get_blog_category_by_id_service(db, id)
    return RMS(data=data)


@router.post("/", response_model=RM)
async def create_blog_category(
    bc: bcm.BlogCategoryCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_CATEGORY_CREATE)),
):
    bc = bc.model_dump()
    data = await bcs.create_blog_category_service(db, bc, current_user.id)
    return RMS(data=data)


@router.put("/{id}", response_model=RM)
async def update_blog_category_by_id(
    id: int,
    bc: bcm.BlogCategoryUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_CATEGORY_UPDATE)),
):
    bc = bc.model_dump()
    data = await bcs.update_blog_category_by_id_service(db, id, bc, current_user.id)
    return RMS(data=data)


@router.delete("/", response_model=RM)
async def delete_blog_category(
    ids: bcm.BlogCategoryDeleteByIds,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.BLOG_CATEGORY_DELETE)),
):
    data = await bcs.delete_blog_category_by_ids_service(db, ids.ids)
    return RMS(data=data)
