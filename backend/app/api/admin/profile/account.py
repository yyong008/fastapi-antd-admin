from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.services.profile.account import get_profile_account_service
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.utils.current_user import get_current_user

router = APIRouter(prefix="/account", tags=["Account"])


@router.get("/", response_model=ResponseModel)
def get_account(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    data = get_profile_account_service(current_user.id, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}")
def get_account_by_id():
    return {"success": "ok"}


@router.post("/")
def create_account():
    return {"success": "ok"}


@router.put("/{id}")
def update_account_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_account():
    return {"success": "ok"}
