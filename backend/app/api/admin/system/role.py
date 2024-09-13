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
    return {"success": "ok"}


@router.post("/")
def create_role():
    return {"success": "ok"}


@router.put("/{id}")
def update_role_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_role():
    return {"success": "ok"}
