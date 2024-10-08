from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession 
from sqlalchemy.exc import SQLAlchemyError

import app.dal.sys.dict_item as di_dals
from app.services.sys._format import format_dict_item
from app.models.system.dictionary import DictionaryEntry


async def get_dict_item_list_service(db: AsyncSession, id, page, pageSize):
    """
    获取字典项目列表
    """
    try:
        count = await di_dals.get_dictionary_entry_count(db, id)
        users = await di_dals.get_dictionary_entry_list(db, id, page, pageSize)

        dict_item_list = [format_dict_item(user) for user in users]

        data = {"total": count, "list": dict_item_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def get_dict_item_by_id_service(db: AsyncSession, id: int):
    """
    通过 id 获取字典项目
    """
    try:
        data = await di_dals.get_dict_item_by_id(db, id)
        return format_dict_item(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_dict_item_service(db: AsyncSession, dict_item):
    """
    创建字典项目
    """
    try:
        data = DictionaryEntry(**dict_item.model_dump())
        di = await di_dals.create_dict_item(db, data)
        return format_dict_item(di)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def update_dict_item_by_id_service(db: AsyncSession, id: int, dict_item):
    """
    更新字典项目
    """
    try:
        dt = dict_item.model_dump(exclude_unset=True)
        di = await di_dals.update_dict_item_by_id(db, id, dt)
        return format_dict_item(di)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def delete_dict_item_by_ids_service(db: AsyncSession, ids: list[int]):
    try:
        data = await di_dals.delete_dict_item_by_ids(db, ids)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
