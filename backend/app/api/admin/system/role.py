from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.client import get_db
from app.services.sys.role import get_all_role_service
from app.schemas.response import ResponseModel, ResponseSuccessModel

router = APIRouter(prefix="/role", tags=["Role"])


@router.get("/", response_model=ResponseModel)
def get_all_roles(db: Session = Depends(get_db)):
    data = get_all_role_service(db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}")
def get_role_by_id():
    data = {}
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_role():
    data = {}
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_role_by_id():
    data = {}
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_role():
    data = {}
    return ResponseSuccessModel(data=data)
