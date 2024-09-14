from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.sys.dict import get_dictionary_count, get_dictionary_list



def format_dict(dict):
    item = {
        "id": dict.id,
        "name": dict.name,
        "code": dict.code,
        "status": dict.status,
        "remark": dict.remark,
        "description": dict.description,
        "createdAt": dict.createdAt,
        "updatedAt": dict.updatedAt,
    }
    return item


def get_dict_list(page, pageSize, db: Session):
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
