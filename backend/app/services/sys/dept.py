from fastapi import HTTPException, status

from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy.ext.asyncio import AsyncSession 
from app.models.system.department import Department
from app.services.sys._format import format_dept, build_dept_list_to_tree
import app.dal.sys.dept as dept_dals

async def get_dept_list_all_service(db: AsyncSession):
    """
    获取所有部门列表
    """
    try:
        res = await dept_dals.get_dept_list(db)
        total = await dept_dals.get_dept_count(db)
        list = [format_dept(item) for item in res]
        data = {"list": list, "total": total}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )

async def get_dept_tree_data_service(db, page, pageSize):
    """
    获取部门树形结构
    """
    try:
        res = await dept_dals.get_dept_all(db)
        total = await dept_dals.get_dept_count(db)
        list = []

        for item in res:
            list.append(format_dept(item))
        data = {"list": build_dept_list_to_tree(list, None), "total": total}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )

async def get_dept_by_id_service(db: AsyncSession, id):
    """
    根据id获取部门
    """
    try:
        pass
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

async def create_dept_service(db: AsyncSession, dept):
    """
    创建部门
    """
    try:
        dp = Department(**dept)
        data = await dept_dals.create_dept(db, dp)
        return format_dept(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

async def update_dept_by_id_service(db: AsyncSession, id, dp):
    """
    更新部门
    """
    try:
        dp = dp.model_dump(exclude_unset=True)
        data = await dept_dals.update_dept_by_id(db, id, dp)
        return format_dept(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

async def delete_dept_by_ids_service(db: AsyncSession, ids):
    """
    根据id删除部门
    """
    try:
        count = await dept_dals.delete_dept_by_ids(db, ids)
        return count
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
