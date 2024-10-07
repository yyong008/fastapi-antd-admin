from fastapi import HTTPException
from app.models.blog import BlogCategory
from sqlalchemy.ext.asyncio import AsyncSession 
import app.db.base as base_crud

# =====================================GET===================================================
async def get_blog_category_count(db: AsyncSession):
    count = await base_crud.get_count(db, BlogCategory)
    return count


async def get_blog_category_all(db: AsyncSession):
    order_by = BlogCategory.createdAt.desc()
    data = await base_crud.get_all(db, BlogCategory, order_by=order_by)
    return data


async def get_blog_category_list(db: AsyncSession, page: int = 1, pageSize: int = 10):
    data= await base_crud.get_list(db, BlogCategory, page=page, pageSize=pageSize)
    return data

async def get_blog_category_by_id(db: AsyncSession, id: int):
    # filter = BlogCategory.id == id
    # data = await base_crud.get(db, BlogCategory, filter=filter)
    return db.query(BlogCategory).filter(BlogCategory.id == id).first()

# =====================================CREATE===================================================
async def create_blog_category(db: AsyncSession, bc):
    db.add(bc)
    db.commit()
    db.refresh(bc)
    return bc

# =====================================UPDATE===================================================
async def update_blog_category_by_id(db: AsyncSession, bc_id: int, bc):
    db.commit()
    db.refresh(bc)
    return bc

# =====================================DELETE===================================================
async def delete_news_by_ids(db: AsyncSession, ids):
    try:
        count = (
            db.query(BlogCategory).filter(BlogCategory.id.in_(ids)).delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
