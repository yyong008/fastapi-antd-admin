from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.blog.blog import (
    get_blog_by_id,
    get_blog_count,
    get_blog_list,
    delete_news_by_ids,
    create_blog_category,
    update_blog_category_by_id,
)
from app.services.blog.format import format_blog

def get_blog_list_service(categoryId, tagId, page, pageSize, db: Session):
    try:
        count = get_blog_count(db)
        blogs = get_blog_list(db, categoryId, tagId, page, pageSize)

        blog_list = []
        for blog in blogs:
            item = format_blog(blog)
            blog_list.append(item)

        data = {"total": count, "list": blog_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def get_blog_by_id_service(id, db: Session):
    try:
        blog = get_blog_by_id(id, db)
        if blog is None:
            raise HTTPException(status_code=404, detail="Blog not found")
        return format_blog(blog)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")


def update_blog_service(id, blog, db: Session):
    try:
        blog = get_blog_by_id(id, db)
        if blog is None:
            raise HTTPException(status_code=404, detail="Blog not found")
        data = update_blog_category_by_id(blog, id, db)
        return format_blog(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")


def create_blog_service(name, db: Session):
    try:
        data = create_blog_category(name, db)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")


def delete_blog_by_ids_service(ids, db: Session):
    try:
        data = delete_news_by_ids(ids, db)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
