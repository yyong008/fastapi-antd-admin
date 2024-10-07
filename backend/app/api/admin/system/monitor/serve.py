from fastapi import APIRouter, Depends
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.utils.system_info import get_system_info
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/serve")


@router.get("/", response_model=ResponseModel)
async def get_serve(_: bool = Depends(get_user_permissions(permissions.SYSTE_CONFIG_READ))):
    system_info = get_system_info()
    return ResponseSuccessModel(data=system_info)
