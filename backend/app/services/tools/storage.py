from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.tools.storage import get_storage_by_id, get_storage_count, get_storage_list

from .format import format_tools_storage


def get_tools_storage_list_service(page, paegSize, db: Session):
    try:
        count = get_storage_count(db)
        storages = get_storage_list(db, page, paegSize)

        storage_list = [format_tools_storage(st) for st in storages]

        data = {"total": count, "list": storage_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def get_tools_storage_by_id_service(user_id: int, db):
    try:
        user = get_storage_by_id(user_id, db)
        item = format_tools_storage(user)
        return item
    except Exception as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def create_tools_storage_service(item, db: Session):
    try:
        pass
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")



def update_tools_storage_by_id_service(user_id: int, item, db: Session):
    try:
        pass
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")



def delete_tools_storage_by_ids_service(ids: List[int], db: Session):
    try:
        pass
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

