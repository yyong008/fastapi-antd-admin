from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.profile.link.category import get_link_category_count, get_link_category_list
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
