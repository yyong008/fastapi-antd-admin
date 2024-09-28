from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.profile.link.link import get_link_count_by_category_id, get_links_by_category_id
from app.services.profile.link.format import format_link

def get_link_list_by_id_service(category_id,page, pageSize, db: Session):
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
    pass

def delete_link_by_ids_service(ids, db: Session):
    pass


def create_link_service(link, user_id, db: Session):
    pass
