from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.blog.blog_tag import (
    get_blog_tag_by_id,
    get_blog_tag_count,
    get_blog_tag_list,
    update_blog_tag_by_id,
    create_blog_tag,
    delete_blog_tag_by_ids,
)
from app.services.blog.format import format_blog_tag


def get_blog_tag_list_service(page, pageSize, db: Session):
    try:
        count = get_blog_tag_count(db)
        blog_tag = get_blog_tag_list(db, page, pageSize)

        blog_tag_list = []
        for tag in blog_tag:
            item = format_blog_tag(tag)
            blog_tag_list.append(item)

        data = {"total": count, "list": blog_tag_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def update_blog_tag_by_id_service(id, bt, db: Session):
    try:
        o_data = get_blog_tag_by_id(id, db)
        if o_data is None:
            raise HTTPException(status_code=400, detail="Tag not found")
        data = update_blog_tag_by_id(id, bt, db)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def create_blog_tag_service(bt, db: Session):
    try:
        data = create_blog_tag(bt, db)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def delete_blog_tag_by_ids_service(ids, db: Session):
    try:
        data = delete_blog_tag_by_ids(ids, db)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
