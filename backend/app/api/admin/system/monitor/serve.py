from fastapi import APIRouter
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.utils.system_info import get_system_info

router = APIRouter(prefix="/serve")


@router.get("/", response_model=ResponseModel)
def get_serve():
    system_info = get_system_info()
    return ResponseSuccessModel(data=system_info)
