
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.blog.blog import get_blog_by_id, get_blog_count, get_blog_list


def format_blog(blog):
    item = {
        "id": blog.id,
        "title": blog.title,
        "content": blog.content,
        "author": blog.author,
        "source": blog.source,
        "viewCount": blog.viewCount,
        "publishedAt": blog.publishedAt,
        "categoryId": blog.category_id,
        "tagId":blog.tag_id
    }
    return item


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
