from fastapi import HTTPException
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
    # limit = pageSize
    # offset = (page - 1) * pageSize
    # sort_column = Blog.createdAt.desc()

    # 构造基础查询
    filter = []

    # 动态添加过滤条件
    if categoryId is not None:
        # query = query.filter(Blog.category_id == categoryId)
        filter.append(Blog.category_id == categoryId)
    if tagId is not None:
        # query = query.filter(Blog.tag_id == tagId)
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
    return db.query(Blog).filter(Blog.id == blog_id).first()


async def create_blog(db: AsyncSession, blog):
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


async def update_blog_by_id(db: AsyncSession, blog: Blog, id: int):
    db.commit()
    db.refresh(blog)
    return blog


async def delete_blog_by_ids(db: AsyncSession, ids: list[int]):
    try:
        count = (
            db.query(Blog).filter(Blog.id.in_(ids)).delete(synchronize_session=False)
        )
        db.commit()
        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
