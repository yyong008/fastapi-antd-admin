from fastapi import HTTPException
from app.models.blog import BlogTag
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud

# =====================================GET===================================================
async def get_blog_tag_count(db: AsyncSession):
    count = await base_crud.get_count(db, BlogTag)
    return count


async def get_blog_tag_all(db: AsyncSession):
    sort_column = BlogTag.createdAt.desc()
    return db.query(BlogTag).order_by(sort_column).all()


async def get_blog_tag_list(db: AsyncSession, page: int = 1, pageSize: int = 10):
    data = await base_crud.get_list(db=db,  model=BlogTag, page=page, pageSize=pageSize)
    return data


async def get_blog_tag_by_id(db: AsyncSession, id: int):
    return db.query(BlogTag).filter(BlogTag.id == id).first()


async def create_blog_tag(db: AsyncSession, blog_tag):
    db.add(blog_tag)
    db.commit()
    db.refresh(blog_tag)
    return blog_tag


async def update_blog_tag_by_id(db: AsyncSession, blog_id: int, blog: BlogTag):
    # db.query(BlogTag).filter(BlogTag.id == blog_id).update(blog.dict(), synchronize_session=False)
    db.commit()
    db.refresh(blog)
    return blog


async def delete_blog_tag_by_ids(db: AsyncSession, ids: list[int]):
    try:
        count = (
            db.query(BlogTag)
            .filter(BlogTag.id.in_(ids))
            .delete(synchronize_session=False)
        )
        db.commit()
        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
