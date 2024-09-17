from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.dashboard.dashboard import get_dashboard_data_service
from app.utils.current_user import get_current_user

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/", response_model=ResponseModel)
def get_dict(current_user: dict = Depends(get_current_user),  db: Session = Depends(get_db)):
    data = get_dashboard_data_service(current_user.id, db)
    return ResponseSuccessModel(data=data)
