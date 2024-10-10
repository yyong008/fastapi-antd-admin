from app.models.blog import BlogTag
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud

# =====================================GET===================================================
async def get_blog_tag_count(db: AsyncSession):
    count = await base_crud.get_count(db, BlogTag)
    return count


async def get_blog_tag_all(db: AsyncSession):
    sort_column = BlogTag.created_at.desc()
    return db.query(BlogTag).order_by(sort_column).all()


async def get_blog_tag_list(db: AsyncSession, page: int = 1, pageSize: int = 10):
    data = await base_crud.get_list(
        db=db,
        model=BlogTag,
        order_by=None,
        filter=None,
        options=None,
        page=page,
        pageSize=pageSize,
    )
    return data


async def get_blog_tag_by_id(db: AsyncSession, id: int):
    data = await base_crud.get_by_id(db=db, model=BlogTag, id=id)
    return data


async def create_blog_tag(db: AsyncSession, blog_tag):
    data = await base_crud.create(db=db, model=BlogTag, obj_in=blog_tag)
    return data


async def update_blog_tag_by_id(db: AsyncSession, blog_id: int, blog: BlogTag):
    data = await base_crud.update_by_id(db=db, model=BlogTag, id=blog_id, new_data=blog)
    return data


async def delete_blog_tag_by_ids(db: AsyncSession, ids: list[int]):
    data = await base_crud.delete_by_ids(db=db, model=BlogTag, ids=ids)
    return data
