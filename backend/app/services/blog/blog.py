from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
import app.dal.blog.blog as b_dals
from ._format import format_blog
from app.models.blog import Blog
from sqlalchemy.ext.asyncio import AsyncSession


async def get_blog_list_service(db: AsyncSession, categoryId, tagId, page, pageSize):
    """
    获取博客列表
    """
    try:
        count = await b_dals.get_blog_count(db)
        blogs = await b_dals.get_blog_list(db, categoryId, tagId, page, pageSize)

        blog_list = [format_blog(blog) for blog in blogs]

        data = {"total": count, "list": blog_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def get_blog_by_id_service(db: AsyncSession, id):
    """
    根据id获取博客
    """
    try:
        blog = await b_dals.get_blog_by_id(db, id)
        if blog is None:
            raise HTTPException(status_code=404, detail="Blog not found")
        return format_blog(blog)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def update_blog_service(db: AsyncSession, id, current_user_id, blog):
    """
    更新博客
    """
    try:
        blog_in_db = await b_dals.get_blog_by_id(db, id)
        if blog_in_db is None:
            raise HTTPException(status_code=404, detail="Blog not found")

        for key, value in blog.items():
            setattr(blog_in_db, key, value)
        blog_in_db.user_id = current_user_id
        data = await b_dals.update_blog_by_id(db, blog_in_db, id)
        return format_blog(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_blog_service(db: AsyncSession, blog, current_user_id):
    """
    创建博客
    """
    try:
        blog["user_id"] = current_user_id
        blog = Blog(**blog)
        data = await b_dals.create_blog(db, blog)
        return format_blog(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def delete_blog_by_ids_service(
    db: AsyncSession,
    ids,
):
    """
    根据ids删除博客
    """
    try:
        data = await b_dals.delete_blog_by_ids(
            db,
            ids,
        )
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
