from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db

from app.schemas.response import ResponseSuccessModel
from app.services.sys.dept import get_dept_tree_data

router = APIRouter(prefix="/dept", tags=["Dept"])


@router.get("/")
def get_dict_dept(page: int = 1, pageSize: int = 10, db: Session = Depends(get_db)):
    data = get_dept_tree_data(page, pageSize, db)

    return ResponseSuccessModel(data=data)


@router.get("/{id}")
def get_dict_dept_by_id():
    return {"success": "ok"}


@router.post("/")
def create_dict_dept():
    return {"success": "ok"}


@router.put("/{id}")
def update_dict_dept_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_dict_dept():
    return {"success": "ok"}


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
