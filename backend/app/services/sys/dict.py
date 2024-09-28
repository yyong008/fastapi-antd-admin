from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.sys.dict import get_dictionary_count, get_dictionary_list
from app.services.sys.format import format_dict


def get_dict_lists_service(page, pageSize, db: Session):
    try:
        count = get_dictionary_count(db)
        users = get_dictionary_list(db, page, pageSize)

        dict_list = []
        for user in users:
            item = format_dict(user)
            dict_list.append(item)

        data = {"total": count, "list": dict_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def get_dict_by_id_service():
    try:
        pass
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

def create_dict_service():
    try:
        pass
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

def update_dict_by_id_service():
    try:
        pass
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

def delete_dict_by_ids_service():
    try:
        pass
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
