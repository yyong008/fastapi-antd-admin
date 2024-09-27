from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db

from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.sys.dept import get_dept_tree_data

router = APIRouter(prefix="/dept", tags=["Dept"])


@router.get("/")
def get_dict_dept(page: int = 1, pageSize: int = 10, db: Session = Depends(get_db)):
    data = get_dept_tree_data(page, pageSize, db)

    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_dict_dept_by_id():
    data = {}
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_dict_dept():
    data = {}
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_dict_dept_by_id():
    data = {}
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_dict_dept():
    data = {}
    return ResponseSuccessModel(data=data)


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
