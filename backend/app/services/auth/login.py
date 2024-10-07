from fastapi import BackgroundTasks, HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession

import app.dal.sys.user as user_dals
from app.services.sys.loginlog import create_loginlog_by_userId_name
import app.utils.token as token_utils


async def login_service(db: AsyncSession, request: Request, form_data, background_tasks: BackgroundTasks):
    """
    登录服务
    
    Args:
        request: 请求
        form_data: 登录表单
        db: 数据库
        background_tasks: 后台任务
    Returns:

    """
    existing_user = await user_dals.get_user_by_name(db, form_data.username)

    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User Name not registered",
        )

    if not token_utils.match_password(form_data, existing_user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User Or Password not match",
        )

    background_tasks.add_task(
        create_loginlog_by_userId_name,
        db,
        request,
        existing_user.name,
        existing_user.id,
    )
    payload = {"user_id": existing_user.id}

    access_token = token_utils.create_access_token(payload)
    refresh_token = token_utils.create_access_token(payload)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }
