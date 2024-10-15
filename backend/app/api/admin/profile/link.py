from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import RM, RMS
import app.services.profile.link.link as lk_services
from app.utils.current_user import get_current_user
import app.schemas.profile.profile_link as lk_schemas
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/link", tags=["Link"])


@router.get("/{id}", response_model=RM)
async def get_link_by_id(
    id: int,
    page: int,
    pageSize: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.PROFILE_LINK_LIST)),
):
    data = await lk_services.get_link_list_by_id_service(db, id, current_user.id, page, pageSize)
    return RMS(data=data)


@router.post("/", response_model=RM)
async def create_link(
    link: lk_schemas.LinkCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.PROFILE_LINK_CREATE)),
):
    link = link.model_dump(mode="json")
    data = await lk_services.create_link_service(db, link, current_user.id)
    return RMS(data=data)


@router.put("/{id}", response_model=RM)
async def update_link_by_id(
    id: int,
    link: lk_schemas.LinkUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.PROFILE_LINK_UPDATE)),
):
    link = link.model_dump(mode="json")
    data = await lk_services.update_link_by_id_service(db, id, link)
    return RMS(data=data)


@router.delete("/", response_model=RM)
async def delete_link_by_ids(
    ids: lk_schemas.LinkDeleteByIds,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.PROFILE_LINK_DELETE)),
):
    ids = ids.model_dump(mode="json")
    data = await lk_services.delete_link_by_ids_service(db, ids["ids"])
    return RMS(data=data)
