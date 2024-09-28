from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.services.profile.account import get_profile_account_service, update_profile_account_service
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.utils.current_user import get_current_user

router = APIRouter(prefix="/account", tags=["Account"])


@router.get("/", response_model=ResponseModel)
def get_account_by_current_user(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    data = get_profile_account_service(current_user.id, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_account_by_id(id:int, account: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    data = update_profile_account_service(id, account, db)
    return ResponseSuccessModel(data=data)

