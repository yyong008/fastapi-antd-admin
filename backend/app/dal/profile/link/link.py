from fastapi import HTTPException
from app.models.profile.link import Link
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud


# =====================================GET===================================================
async def get_link_by_name(db: AsyncSession, name: str, ):
    return db.query(Link).filter(Link.name == name).first()


async def get_link_by_email(db: AsyncSession, email: str, ):
    return db.query(Link).filter(Link.email == email).first()


async def get_link_list(db: AsyncSession, page: int = 0, pageSize: int = 10):
    data = await base_crud.get_list(db, Link, page, pageSize)
    return data


async def get_count(db: AsyncSession):
    count = await base_crud.get_count(db, Link)
    return count


async def get_link_count_by_category_id(db: AsyncSession, category_id):
    filter = Link.category_id == category_id
    count = await base_crud.get_count(db=db, model=Link, filter=filter)
    return count


async def get_link_all(db: AsyncSession):
    sort_column = Link.createdAt.desc()
    return db.query(Link).order_by(sort_column).all()


async def get_link_by_id(db: AsyncSession, link_id):
    return db.query(Link).filter_by(id=link_id).first()


async def get_links_by_ids(db: AsyncSession, ids, ):
    return db.query(Link).filter(Link.id.in_(ids)).all()


async def get_links_by_category_id(db: AsyncSession,category_id, page, pageSize, ):
    filter = Link.category_id == category_id
    data = await base_crud.get_list(
        db=db,
        model=Link,
        order_by=None,
        filter=filter,
        options=None,
        page=page,
        pageSize=pageSize,
    )
    return data
    # return db.query(Link).filter(Link.category_id == category_id).offset(skip).limit(limit).all()


async def create_link_category(db: AsyncSession, link, ):
    db.add(link)
    db.commit()
    db.refresh(link)
    return link


async def update_link_by_id(db: AsyncSession, blog_id: int, link: Link):
    # db.query(Link).filter(Link.id == blog_id).update(link)
    db.commit()
    db.refresh(link)
    return link


async def delete_link_by_ids(db: AsyncSession, ids):
    try:
        count = (
            db.query(Link).filter(Link.id.in_(ids)).delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
