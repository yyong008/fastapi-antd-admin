from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

import app.dal.sys.dict as dt_dals
from app.services.sys._format import format_dict
from app.models.system.dictionary import Dictionary
from app.schemas.sys.dictionary import DictionaryCreate, DictionaryUpdate


async def get_dict_lists_service(db: AsyncSession, page: int, pageSize: int):
    try:
        count = await dt_dals.get_dictionary_count(db)
        users = await dt_dals.get_dictionary_list(db, page, pageSize)
        dict_list = [format_dict(user) for user in users]

        data = {"total": count, "list": dict_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def get_dict_by_id_service(db: AsyncSession):
    try:
        pass
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_dict_service(db: AsyncSession, dt: DictionaryCreate):
    try:
        dt = dt.model_dump()
        dt = Dictionary(**dt)
        data = await dt_dals.create_dict(db, dt)
        return format_dict(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def update_dict_by_id_service(db: AsyncSession, id: int, dt: DictionaryUpdate):
    try:
        dt = dt.model_dump(exclude_unset=True)
        data = await dt_dals.update_dict_by_id(db, id, dt)
        return format_dict(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def delete_dict_by_ids_service(db: AsyncSession, ids: list[int]):
    try:
        count = await dt_dals.delete_dict_by_ids(db, ids)
        return count
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
