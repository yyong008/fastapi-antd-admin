from fastapi import HTTPException, status

from sqlalchemy.exc import SQLAlchemyError


from app.models.system.department import Department
from app.services.sys.format import format_dept


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


def get_dept_tree_data_service(page, pageSize, db):
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

def get_dept_by_id_service(id, db):
    pass

def create_dept_service():
    pass

def update_dept_by_id_service():
    pass

def delete_dept_by_ids_service():
    pass
