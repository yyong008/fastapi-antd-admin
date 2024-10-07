from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.profile.link.link import (
    get_link_list_by_id_service,
    create_link_service,
    update_link_by_id_service,
    delete_link_by_ids_service,
)
from app.utils.current_user import get_current_user
from app.schemas.profile.profile_link import LinkCreate, LinkDeleteByIds, LinkUpdate
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/link", tags=["Link"])


# @router.get("/", response_model=ResponseModel)
# async def get_link(id: int, page: int, pageSize: int, db: Session = Depends(get_db)):
#     data = {}
#     return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
async def get_link_by_id(
    id: int,
    page: int,
    pageSize: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.PROFILE_LINK_LIST)),
):
    data = await get_link_list_by_id_service(db, id, page, pageSize)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
async def create_link(
    link: LinkCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.PROFILE_LINK_CREATE)),
):
    link = link.model_dump(mode="json")
    data = await create_link_service(db, link, current_user.id)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
async def update_link_by_id(
    id: int,
    link: LinkUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.PROFILE_LINK_UPDATE)),
):
    link = link.model_dump(mode="json")
    data = await update_link_by_id_service(db, id, link)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
async def delete_link_by_ids(
    ids: LinkDeleteByIds,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.PROFILE_LINK_DELETE)),
):
    ids = ids.model_dump(mode="json")
    data = await delete_link_by_ids_service(db, ids["ids"])
    return ResponseSuccessModel(data=data)
