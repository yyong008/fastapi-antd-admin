from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.profile.link.category import (
    create_link_category,
    delete_link_category_by_ids,
    get_link_category_by_id,
    get_link_category_count,
    get_link_category_list,
    update_link_category_by_id,
)
from app.services.profile.link.format import format_category


def get_link_category_list_service(page, pageSize, db: Session):
    try:
        count = get_link_category_count(db)
        categories = get_link_category_list(db, page, pageSize)

        category_list = []
        for c in categories:
            item = format_category(c)
            category_list.append(item)

        data = {"total": count, "list": category_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def get_link_category_by_id_service(id, db: Session):
    try:
        data = get_link_category_by_id(id, db)
        item = format_category(data)
        return item
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def create_link_category_service(link_category, user_id, db):
    try:
        data = create_link_category(link_category, db)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def update_link_category_service(id, link_category, user_id, db):
    try:
        o_data = get_link_category_by_id(id, db)
        if o_data is None:
            raise HTTPException(status_code=400, detail="Link category not found")
        data = update_link_category_by_id(id, link_category, db)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def delete_link_category_by_ids_service(ids, db):
    try:
        data = delete_link_category_by_ids(ids, db)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
