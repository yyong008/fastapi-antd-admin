from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import RM, RMS
import app.services.profile.link.category  as lc_services
from app.schemas.profile.profile_link_category import (
    LinkCategoryCreate,
    LinkCategoryUpdate,
    LinkCategoryDeleteByIds,
)
from app.utils.current_user import get_current_user
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/link/category", tags=["Link Category"])


@router.get("/", response_model=RM)
async def get_link_category(
    page: int = 1,
    pageSize: int = 10,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.PROFILE_LINK_CATEGORY_READ)),
):
    data = await lc_services.get_link_category_list_service(db, page, pageSize)
    return RMS(data=data)


@router.get("/{id}", response_model=RM)
async def get_link_category_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.PROFILE_LINK_CATEGORY_READ)),
):
    data = await lc_services.get_link_category_by_id_service(db, id)
    return RMS(data=data)


@router.post("/", response_model=RM)
async def create_link_category(
    lc: LinkCategoryCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.PROFILE_LINK_CATEGORY_CREATE)),
):
    lc = lc.model_dump()
    data = await lc_services.create_link_category_service(db, lc, current_user.id)
    return RMS(data=data)


@router.put("/{id}", response_model=RM)
async def update_link_category_by_id(
    id: int,
    lc: LinkCategoryUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.PROFILE_LINK_CATEGORY_UPDATE)),
):
    lc = lc.model_dump()
    data = await lc_services.update_link_category_service(db, id, lc, current_user.id)
    return RMS(data=data)


@router.delete("/", response_model=RM)
async def delete_link_by_ids_category(
    ids: LinkCategoryDeleteByIds,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.PROFILE_LINK_CATEGORY_DELETE)),
):
    ids = ids.model_dump()
    data = await lc_services.delete_link_category_by_ids_service(db, ids["ids"])
    return RMS(data=data)
