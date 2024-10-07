from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.dashboard.dashboard import get_dashboard_data_service
from app.utils.current_user import get_current_user
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/", response_model=ResponseModel)
async def get_dashboard_data(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.DASHBOAR_READ)),
):
    data = await get_dashboard_data_service(db, current_user.id)
    return ResponseSuccessModel(data=data)
