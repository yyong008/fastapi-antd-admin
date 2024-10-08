from app.models.system.department import Department
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud


# =====================================GET===================================================
async def get_dept_count(db: AsyncSession):
    count = await base_crud.get_count(db, Department)
    return count


async def get_dept_all(db: AsyncSession):
    order_by = Department.createdAt.desc()
    data = await base_crud.get_all(db, Department, order_by=order_by)
    return data


async def get_dept_list(db: AsyncSession, page: int = 1, pageSize: int = 10):
    order_by = Department.createdAt.desc()
    data = await base_crud.get_list(
        db=db, model=Department, order_by=order_by, page=page, pageSize=pageSize
    )
    return data


async def create_dept(dept, db: AsyncSession):
    data = await base_crud.create(db, Department, dept)
    return data

async def update_dept_by_id(db: AsyncSession, dept_id: int, dept: Department):
    data = await base_crud.update_by_id(db, Department, dept_id, dept)
    return data


async def delete_dept_by_ids(db: AsyncSession, ids: list[int]):
    data = await base_crud.delete_by_ids(db, Department, ids)
    return data
