from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.profile.link.link import (
    create_link_category,
    get_link_count_by_category_id,
    get_links_by_category_id,
    get_link_by_id,
    delete_link_by_ids,
    update_link_by_id,
)
from app.services.profile.link.format import format_link
from app.models.profile.link import Link


def get_link_list_by_id_service(category_id, page, pageSize, db: Session):
    try:
        count = get_link_count_by_category_id(category_id, db)
        links = get_links_by_category_id(category_id, page, pageSize, db)

        link_list = []
        for link in links:
            item = format_link(link)
            link_list.append(item)

        data = {"total": count, "list": link_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def get_link_list_by_ids_service(ids, db: Session):
    try:
        links = get_links_by_category_id(ids, db)
        return links
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail="Oops, we encountered an error")


def update_link_by_id_service(id, link, db: Session):
    try:
        o_data = get_link_by_id(id, db)
        if not o_data:
            raise HTTPException(status_code=400, detail="Oops, we encountered an error")
        o_data.name = link["name"]
        o_data.url = link["url"]
        o_data.category_id = link["category_id"]
        data = update_link_by_id(id, o_data, db)
        return format_link(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail="Oops, we encountered an error")


def delete_link_by_ids_service(ids, db: Session):
    try:
        data = delete_link_by_ids(ids, db)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail="Oops, we encountered an error")


def create_link_service(link, user_id, db: Session):
    try:
        del link['user_id']
        lk = Link(**link)
        # lk.user_id = user_id
        data = create_link_category(lk, db)
        return format_link(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail="Oops, we encountered an error")
