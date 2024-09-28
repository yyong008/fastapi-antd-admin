from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.sys.role import get_roles_all,get_count
from .format import format_role



def get_role_list(page, pageSize, db: Session):
    pass

def get_all_role_service(db: Session):
    try:
        count = get_count(db)
        roles_list_all = get_roles_all(db)

        user_list = []
        for role in roles_list_all:
            item = format_role(role)
            user_list.append(item)

        data = {"total": count, "list": user_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

def get_role_by_id(role_id: int, db):
    pass

def create_role(user, db: Session):
    pass


def update_role_by_id(role_id: int, item, db: Session):
    pass


def delete_role_by_ids(ids: List[int], db: Session):
    pass
