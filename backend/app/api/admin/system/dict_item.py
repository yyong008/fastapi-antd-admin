from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.sys.dict_item import (
    get_dict_item_list_service,
    get_dict_item_by_id_service,
    create_dict_item_service,
    update_dict_item_by_id_service,
    delete_dict_item_by_ids_service,
)
from app.db.client import get_db
from app.schemas.sys.dictionary_entry import (
    DictionaryEntryCreate,
    DictionaryEntryUpdate,
    DictinonaryEntryByIds,
)
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/dict-item", tags=["Dict Item"])


@router.get("/", response_model=ResponseModel)
async def get_dict_item(
    dictId: int,
    page: int = 1,
    pageSize: int = 10,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_ITEM_READ)),
):
    data = await get_dict_item_list_service(db, dictId, page, pageSize)
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
async def get_dict_item_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_ITEM_READ)),
):
    data = await get_dict_item_by_id_service(db, id)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
async def create_dict_item(
    dict_item: DictionaryEntryCreate,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_ITEM_CREATE)),
):
    data = await create_dict_item_service(db, dict_item)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
async def update_dict_item_by_id(
    id: int,
    dict_item: DictionaryEntryUpdate,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_ITEM_UPDATE)),
):
    data = await update_dict_item_by_id_service(db, id, dict_item)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
async def delete_dict_item(
    ids: DictinonaryEntryByIds,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_ITEM_DELETE)),
):
    data = await delete_dict_item_by_ids_service(db, ids)
    return ResponseSuccessModel(data=data)
