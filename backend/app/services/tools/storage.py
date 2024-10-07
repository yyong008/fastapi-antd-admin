from typing import List
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession 
import app.dal.tools.storage as st_dals
from app.models.tools.storage import Storage
from ._format import format_tools_storage


async def get_tools_storage_list_service(db: AsyncSession, page, paegSize):
    try:
        count = await st_dals.get_storage_count(db)
        storages = await st_dals.get_storage_list(db, page, paegSize)

        storage_list = [format_tools_storage(st) for st in storages]

        data = {"total": count, "list": storage_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def get_tools_storage_by_id_service(db: AsyncSession, user_id: int):
    try:
        user = await st_dals.get_storage_by_id(db, user_id)
        item = format_tools_storage(user)
        return item
    except Exception as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_tools_storage_service(db: AsyncSession, file_info):
    try:
        file_info = Storage(**file_info)
        storage = await st_dals.create_storage(db, file_info)
        return format_tools_storage(storage)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

async def update_tools_storage_by_id_service(db: AsyncSession, user_id: int, item):
    try:
        pass
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")



async def delete_tools_storage_by_ids_service(db: AsyncSession, ids: List[int]):
    try:
        pass
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

