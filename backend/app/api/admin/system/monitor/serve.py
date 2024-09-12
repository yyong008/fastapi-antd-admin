from fastapi import APIRouter
from app.schemas.response import ResponseSuccessModel
from app.utils.system_info import get_system_info

router = APIRouter(prefix="/serve")


@router.get("/")
def get_serve():
    system_info = get_system_info()
    return ResponseSuccessModel(data=system_info)
