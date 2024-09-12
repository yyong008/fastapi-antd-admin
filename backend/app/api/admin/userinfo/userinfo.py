from fastapi import APIRouter, Depends

from app.services.userinfo.userinfo import get_user_info
from app.utils.current_user import get_current_user
from app.db.client import get_db
from app.schemas.response import ResponseSuccessModel,ResponseModel

router = APIRouter(tags=["userinfo"])


@router.get("/userinfo", response_model=ResponseModel)
def get_userinfo(current_user: dict = Depends(get_current_user), db = Depends(get_db)):
    data = get_user_info(current_user.id, db)
    return ResponseSuccessModel(data=data)
