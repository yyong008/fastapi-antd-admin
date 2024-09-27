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


@router.get("/{id}", response_model=ResponseModel)
def get_account_by_id():
    data = {}
    return ResponseSuccessModel(data=data)



@router.put("/{id}", response_model=ResponseModel)
def update_account_by_id():
    data = {}
    return ResponseSuccessModel(data=data)

