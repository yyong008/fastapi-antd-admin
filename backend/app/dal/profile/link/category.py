from fastapi import HTTPException
from app.models.profile.link import LinkCategory
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud


# =====================================GET===================================================
async def get_link_category_by_name(name: str, db: AsyncSession):
    return db.query(LinkCategory).filter(LinkCategory.name == name).first()


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
    sort_column = LinkCategory.createdAt.desc()
    return db.query(LinkCategory).order_by(sort_column).all()


async def get_link_category_by_id(link_id, db: AsyncSession):
    return db.query(LinkCategory).filter_by(id=link_id).first()


async def get_link_category_by_ids(ids, db: AsyncSession):
    return db.query(LinkCategory).filter(LinkCategory.id.in_(ids)).all()


async def create_link_category(link_category, db: AsyncSession):
    db.add(link_category)
    db.commit()
    db.refresh(link_category)
    return link_category


async def update_link_category_by_id(
    link_category_id: int, link_category: LinkCategory, db: AsyncSession
):
    # db.query(LinkCategory).filter(LinkCategory.id == link_category_id).update(link_category)
    db.commit()
    db.refresh(link_category)
    return link_category


async def delete_link_category_by_ids(db, ids):
    try:
        count = (
            db.query(LinkCategory)
            .filter(LinkCategory.id.in_(ids))
            .delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
