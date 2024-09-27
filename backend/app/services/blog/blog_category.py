from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.blog.blog_category import get_blog_category_count, get_blog_category_list
from app.services.blog.format import format_blog_category


def get_blog_category_list_service(page, pageSize, db: Session):
    try:
        count = get_blog_category_count(db)
        blog_category = get_blog_category_list(db, page, pageSize)

        category_list = []
        for c in blog_category:
            item = format_blog_category(c)
            category_list.append(item)

        data = {"total": count, "list": category_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

def get_blog_category_by_id_service(id, db: Session):
    pass

def update_blog_category_service(id, name, db: Session):
    pass

def create_blog_category_service(name, db: Session):
    pass

def delete_blog_category_by_ids_service(ids, db: Session):
    pass
