from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.sys.dict_item import get_dictionary_entry_count, get_dictionary_entry_list
from app.services.sys.format import format_dict_item

def get_dict_item_list(id, page, pageSize, db: Session):
    try:
        count = get_dictionary_entry_count(id, db)
        users = get_dictionary_entry_list(id, db, page, pageSize)

        dict_item_list = []
        for user in users:
            item = format_dict_item(user)
            dict_item_list.append(item)

        data = {"total": count, "list": dict_item_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

def get_dict_item_by_id(id, db: Session):
    pass

def create_dict_item():
    pass


def update_dict_item_by_id():
    pass


def delete_dict_item_by_ids():

    pass
