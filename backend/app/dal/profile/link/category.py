from app.models.profile.link import LinkCategory
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud


# =====================================GET===================================================
async def get_link_category_by_name(name: str, db: AsyncSession):
    # return db.query(LinkCategory).filter(LinkCategory.name == name).first()
    data = await base_crud.get_by_name(db, LinkCategory, name)
    return data


async def get_link_category_list(db: AsyncSession, page: int = 0, pageSize: int = 10):
    data = await base_crud.get_list(
        db=db,
        model=LinkCategory,
        order_by=None,
        filter=None,
        options=None,
        page=page,
        pageSize=pageSize,
    )
    return data


async def get_link_category_count(db: AsyncSession):
    count = await base_crud.get_count(db, LinkCategory)
    return count


async def get_link_category_all(db: AsyncSession):
    data = await base_crud.get_all(db, LinkCategory)
    return data


async def get_link_category_by_id(db: AsyncSession, id,):
   data = await base_crud.get_by_id(db, LinkCategory, id)
   return data



async def create_link_category(link_category, db: AsyncSession):
    data = await base_crud.create(db, link_category)
    return data


async def update_link_category_by_id(
    link_category_id: int, link_category: LinkCategory, db: AsyncSession
):
    data = await base_crud.update_by_id(
        db, LinkCategory, link_category_id, link_category
    )
    return data


async def delete_link_category_by_ids(db, ids):
    data = await base_crud.delete_by_ids(db, LinkCategory, ids)
    return data
