from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from app.models.blog import BlogCategory
from sqlalchemy.ext.asyncio import AsyncSession

import app.dal.blog.blog_category as bc_dals
from ._format import format_blog_category

async def get_blog_category_list_service(db: AsyncSession, page: int, pageSize: int):
    try:
        count = await bc_dals.get_blog_category_count(db)
        blog_category = await bc_dals.get_blog_category_list(db, page, pageSize)

        category_list = [format_blog_category(bc) for bc in blog_category]

        data = {"total": count, "list": category_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def get_blog_category_by_id_service(db: AsyncSession, id: int):
    try:
        data = await bc_dals.get_blog_category_by_id(db, id)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def update_blog_category_by_id_service(
    db: AsyncSession, id: int, bc, current_user_id: int
):
    try:
        bc_in_db = await bc_dals.get_blog_category_by_id(db, id)
        if bc_in_db is None:
            raise HTTPException(status_code=400, detail="Blog category not found")
        bc_in_db.description = bc["description"]
        bc_in_db.name = bc["name"]
        bc_in_db.user_id = current_user_id

        data = await bc_dals.update_blog_category_by_id(db, id, bc_in_db)
        return format_blog_category(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_blog_category_service(db: AsyncSession, bc, current_user_id):
    try:
        bc["user_id"] = current_user_id
        blog_category = BlogCategory(**bc)
        data = await bc_dals.create_blog_category(db, blog_category)
        return format_blog_category(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def delete_blog_category_by_ids_service(db: AsyncSession, ids):
    try:
        data = await bc_dals.delete_news_by_ids(db, ids)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
