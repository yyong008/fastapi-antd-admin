from app.models.blog import Blog
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud


# =====================================GET===================================================
async def get_blog_count(db: AsyncSession):
    count = await base_crud.get_count(db, Blog)
    return count


async def get_blog_all(db: AsyncSession):
    sort_column = Blog.createdAt.desc()
    data = await base_crud.get_all(db, Blog, sort_column)
    return data


async def get_blog_list(
    db: AsyncSession, categoryId: int, tagId: int, page: int = 1, pageSize: int = 10
):
    filter = []
    if categoryId is not None:
        filter.append(Blog.category_id == categoryId)
    if tagId is not None:
        filter.append(Blog.tag_id == tagId)

    data = await base_crud.get_list(
        db,
        Blog,
        filter=filter,
        order_by=None,
        options=None,
        page=page,
        pageSize=pageSize,
    )
    return data


async def get_blog_by_id(db: AsyncSession, blog_id: int):
    data = await base_crud.get_by_id(db, Blog, blog_id)
    return data


async def create_blog(db: AsyncSession, blog: dict):
    data = await base_crud.create(db, Blog, blog)
    return data


async def update_blog_by_id(db: AsyncSession, blog: dict, id: int):
    data = await base_crud.update_by_id(db, Blog, id, blog)
    return data


async def delete_blog_by_ids(db: AsyncSession, ids: list[int]):
    data = await base_crud.delete_by_ids(db, Blog, ids)
    return data
