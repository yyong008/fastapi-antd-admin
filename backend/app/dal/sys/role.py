from fastapi import HTTPException
from sqlalchemy.orm import selectinload
from app.models.system.role import Role
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud


# =====================================GET===================================================
async def get_count(db: AsyncSession):
    count = await base_crud.get_count(db, Role)
    return count


async def get_roles_all(db: AsyncSession):
    order_by = Role.createdAt.desc()
    options = selectinload(Role.menus)
    data = await base_crud.get_all(
        db=db, model=Role, order_by=order_by, options=options
    )
    return data


async def get_role_by_id(db: AsyncSession, role_id: int):
    data = await base_crud.get_by_id(db, Role, role_id)
    return data


async def get_role_list(db: AsyncSession, page: int = 1, pageSize: int = 10):
    order_by = Role.createdAt.desc()
    options = selectinload(Role.menus)
    data = await base_crud.get_list(
        db=db,
        model=Role,
        order_by=order_by,
        options=options,
        page=page,
        pageSize=pageSize,
    )
    return data


# =====================================CREATE===================================================
async def create_role(db: AsyncSession, role):
    db.add(role)
    db.commit()
    db.refresh(role)
    return role


# =====================================UPDATE===================================================
async def update_role_by_id(db: AsyncSession, role_id: int, role: Role):
    # db.query(Role).filter(Role.id == role_id).update(role)
    db.commit()
    db.refresh(role)
    return role


# =====================================DELETE===================================================
async def delete_role_by_ids(db: AsyncSession, ids: list[int]):
    try:
        count = (
            db.query(Role).filter(Role.id.in_(ids)).delete(synchronize_session=False)
        )
        db.commit()
        if count == 0:
            raise HTTPException(status_code=400, detail="No data found")
        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
