from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.sys.dict_item import get_dictionary_entry_count, get_dictionary_entry_list



def format_dict_item(dict_item):
    item = {
        "id": dict_item.id,
        "key": dict_item.key,
        "value": dict_item.value,
        "orderNo": dict_item.order_no,
        "status": dict_item.status,
        "remark": dict_item.remark,
        "createdAt": dict_item.createdAt,
        "updatedAt": dict_item.updatedAt,
    }
    return item


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
