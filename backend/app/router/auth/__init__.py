from fastapi import APIRouter, BackgroundTasks, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.utils.token import create_access_token, verify_refresh_token

import app.services.auth.login as login_service
from app.schemas.response import ResponseModel, ResponseSuccessModel

router = APIRouter(prefix="/auth", tags=["AUTH"])


@router.post("/login", response_model=ResponseModel)
def login(
    request: Request,
    background_tasks: BackgroundTasks,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    data = login_service.login(request, form_data, db, background_tasks)
    return ResponseSuccessModel(data=data)


@router.post("/refresh")
def refresh_token(refresh_token: str):
    payload = verify_refresh_token(refresh_token)
    new_access_token = create_access_token(payload={"user_id": payload.user_id})
    return {"access_token": new_access_token, "token_type": "bearer"}
