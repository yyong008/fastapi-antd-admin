from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db

from app.schemas.response import RM, RMS
import app.services.sys.dept as dp_services
import app.schemas.sys.department as dp_schemas
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/dept", tags=["Dept"])


@router.get("/")
async def get_dept_dept(
    page: int = 1,
    pageSize: int = 10,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DEPT_READ)),
):
    data = await dp_services.get_dept_tree_data_service(db, page, pageSize)
    return RMS(data=data)


@router.get("/list/all")
async def get_dept_dept_list_all(
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DEPT_READ)),
):
    data = await dp_services.get_dept_list_all_service(db)
    return RMS(data=data)


@router.get("/{id}", response_model=RM)
async def get_dept_dept_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DEPT_READ)),
):
    data = await dp_services.get_dept_by_id_service(db, id)
    return RMS(data=data)


@router.post("/", response_model=RM)
async def create_dept(
    dept: dp_schemas.DepartmentCreate,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DEPT_CREATE)),
):
    data = await dp_services.create_dept_service(db, dept)
    return RMS(data=data)


@router.put("/{id}", response_model=RM)
async def update_dept_by_id(
    id: int,
    dept: dp_schemas.DepartmentUpdate,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DEPT_UPDATE)),
):
    data = await dp_services.update_dept_by_id_service(db, id, dept)
    return RMS(data=data)


@router.delete("/", response_model=RM)
async def delete_dept_dept(
    ids: dp_schemas.DepartmentDeleteByIds,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DEPT_DELETE)),
):
    data = await dp_services.delete_dept_by_ids_service(db, ids.ids)
    return RMS(data=data)


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
