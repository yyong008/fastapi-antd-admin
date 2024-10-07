from fastapi import HTTPException
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
    db.add(dept)
    db.commit()
    db.refresh(dept)
    return dept


async def update_dept_by_id(db: AsyncSession, dept_id: int, dept: Department):
    db.query(Department).filter(Department.id == dept_id).update(dept)
    db.commit()
    dept = db.query(Department).filter(Department.id == dept_id).first()
    db.refresh(dept)
    return dept


async def delete_dept_by_ids(db: AsyncSession, ids: list[int]):
    try:
        count = (
            db.query(Department)
            .filter(Department.id.in_(ids))
            .delete(synchronize_session=False)
        )

        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
