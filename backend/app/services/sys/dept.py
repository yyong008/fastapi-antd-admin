from fastapi import HTTPException, status

from sqlalchemy.exc import SQLAlchemyError


from app.models.system.department import Department
from app.services.sys.format import format_dept
from app.dal.sys.dept import create_dept, update_dept_by_id, delete_dept_by_ids

def build_dept_list_to_tree(items: list, parent_id: int = None) -> list:
    return [
        {
            **item,
            "children": build_dept_list_to_tree(
                items, item["id"]
            ),  # Recursively build child tree
        }
        for item in items
        if item.get("parent_department_id") == parent_id
    ]


async def get_dept_list_all_service(db):
    try:
        res = db.query(Department).all()
        total = db.query(Department).count()
        list = []

        for item in res:
            list.append(format_dept(item))
        data = {"list": list, "total": total}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )

async def get_dept_tree_data_service(page, pageSize, db):
    try:
        res = db.query(Department).offset(page).limit(pageSize).all()
        total = db.query(Department).count()
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

async def get_dept_by_id_service(id, db):
    try:
        pass
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

async def create_dept_service(dept, db):
    try:
        dp = Department(**dept)
        data = await create_dept(dp, db)
        return format_dept(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

async def update_dept_by_id_service(id, dp, db):
    try:
        dp = dp.model_dump(exclude_unset=True)
        data = await update_dept_by_id(db, id, dp)
        return format_dept(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

async def delete_dept_by_ids_service(ids, db):
    try:
        count = await delete_dept_by_ids(ids, db)
        return count
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
