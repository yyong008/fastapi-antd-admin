from fastapi import HTTPException
from app.models.system.menu import Menu
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud


# =====================================GET===================================================
async def get_count(db: AsyncSession):
    count = await base_crud.get_count(db, Menu)
    return count


async def get_menu_all(db: AsyncSession):
    order_by = None
    data = await base_crud.get_all(db, Menu, order_by=order_by)
    return data


async def get_menu_list(db: AsyncSession, page: int = 1, pageSize: int = 10):
    filter = None
    options = None
    order_by = Menu.createdAt.desc()
    data = await base_crud.get_list(
        db=db,
        model=Menu,
        order_by=order_by,
        filter=filter,
        options=options,
        page=page,
        pageSize=pageSize,
    )
    return data


async def create_menu(db: AsyncSession, meun):
    db.add(meun)
    db.commit()
    db.refresh(meun)
    return meun


async def update_menu_by_id(db: AsyncSession, menu_id: int, menu: Menu):
    db.query(Menu).filter(Menu.id == menu_id).update(menu)
    db.commit()
    menu = db.query(Menu).filter(Menu.id == menu_id).first()
    db.refresh(menu)
    return menu


async def delete_menu_by_ids(db: AsyncSession, ids: list[int]):
    try:
        count = (
            db.query(Menu).filter(Menu.id.in_(ids)).delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
