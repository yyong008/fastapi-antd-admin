from fastapi import APIRouter, Depends

from app.utils.current_user import get_current_user
from app.db.client import get_db
from app.schemas.response import ResponseSuccessModel,ResponseModel
from app.services.signin_log import create_signin_log_service

router = APIRouter(prefix="/signin_log",tags=["Sign"])


@router.post("/", response_model=ResponseModel)
async def create_signin_log(current_user: dict = Depends(get_current_user), db = Depends(get_db)):
    data = await create_signin_log_service(current_user.id, db)
    return ResponseSuccessModel(data=data)
