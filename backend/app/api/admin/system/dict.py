from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.schemas.sys.dictionary import (
    DictionaryDeleteByIds,
    DictionaryCreate,
    DictionaryUpdate,
)
from app.services.sys.dict import (
    get_dict_lists_service,
    get_dict_by_id_service,
    create_dict_service,
    update_dict_by_id_service,
    delete_dict_by_ids_service,
)
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/dict", tags=["Dict"])


@router.get("/", response_model=ResponseModel)
async def get_dict(
    page: int = 1,
    pageSize: int = 10,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_READ)),
):
    data = await get_dict_lists_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}")
async def get_dict_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_READ)),
):
    data = await get_dict_by_id_service(id, db)
    return ResponseSuccessModel(data=data)


@router.post("/")
async def create_dict(
    dict: DictionaryCreate,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_CREATE)),
):
    data = await create_dict_service(dict, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}")
async def update_dict_by_id(
    id: int,
    dict: DictionaryUpdate,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_UPDATE)),
):
    data = await update_dict_by_id_service(id, dict, db)
    return ResponseSuccessModel(data=data)


@router.delete("/")
async def delete_dict(
    ids: DictionaryDeleteByIds,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_DELETE)),
):
    data = await delete_dict_by_ids_service(ids.ids, db)
    return ResponseSuccessModel(data=data)
