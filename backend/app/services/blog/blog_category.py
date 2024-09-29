from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.blog import BlogCategory

from app.dal.blog.blog_category import (
    delete_news_by_ids,
    get_blog_category_by_id,
    get_blog_category_count,
    get_blog_category_list,
    create_blog_category,
    update_blog_category_by_id,
)
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
    try:
        data = get_blog_category_by_id(id, db)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def update_blog_category_by_id_service(id, bc, current_user_id, db: Session):
    try:
        bc_in_db = get_blog_category_by_id(id, db)
        if bc_in_db is None:
            raise HTTPException(status_code=400, detail="Blog category not found")
        bc_in_db.description = bc['description']
        bc_in_db.name = bc['name']
        bc_in_db.user_id = current_user_id

        data = update_blog_category_by_id(id, bc_in_db, db)
        return  format_blog_category(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def create_blog_category_service(bc, current_user_id, db: Session):
    try:
        bc['user_id'] = current_user_id
        blog_category = BlogCategory(**bc)
        data = create_blog_category(blog_category, db)
        return format_blog_category(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def delete_blog_category_by_ids_service(ids, db: Session):
    try:
        data = delete_news_by_ids(ids, db)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
