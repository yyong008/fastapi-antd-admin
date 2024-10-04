from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db

from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.sys.dept import (
    get_dept_tree_data_service,
    get_dept_by_id_service,
    create_dept_service,
    update_dept_by_id_service,
    delete_dept_by_ids_service,
)
from app.schemas.sys.department import (
    DepartmentCreate,
    DepartmentUpdate,
    DepartmentDeleteByIds,
)

router = APIRouter(prefix="/dept", tags=["Dept"])


@router.get("/")
async def get_dept_dept(
    page: int = 1, pageSize: int = 10, db: Session = Depends(get_db)
):
    data = await get_dept_tree_data_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
async def get_dept_dept_by_id(id: int, db: Session = Depends(get_db)):
    data = await get_dept_by_id_service(id, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
async def create_dept(dept: DepartmentCreate, db: Session = Depends(get_db)):
    data = await create_dept_service(dept, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
async def update_dept_by_id(
    id: int, dept: DepartmentUpdate, db: Session = Depends(get_db)
):
    data = await update_dept_by_id_service(id, dept, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
async def delete_dept_dept(ids: DepartmentDeleteByIds, db: Session = Depends(get_db)):
    data = await delete_dept_by_ids_service(ids.ids, db)
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
