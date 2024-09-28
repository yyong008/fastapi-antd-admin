# TODO: register

from fastapi import BackgroundTasks, HTTPException, status
from sqlalchemy.orm import Session

import app.dal.sys.user as user_dal
from app.services.sys.loginlog import create_loginlog_by_userId_name
import app.utils.token as token_utils


def register_service(request, form_data, db: Session, background_tasks: BackgroundTasks):
    pass
    # existing_user = user_dal.get_user_by_name(form_data.username, db)

    # if not existing_user:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="User Name not registered",
    #     )

    # if not token_utils.match_password(form_data, existing_user):
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="User Or Password not match",
    #     )

    # background_tasks.add_task(
    #     create_loginlog_by_userId_name,
    #     request,
    #     existing_user.name,
    #     existing_user.id,
    #     db,
    # )
    # payload = {"user_id": existing_user.id}

    # access_token = token_utils.create_access_token(payload)
    # refresh_token = token_utils.create_access_token(payload)

    # return {
    #     "access_token": access_token,
    #     "refresh_token": refresh_token,
    #     "token_type": "bearer",
    # }
