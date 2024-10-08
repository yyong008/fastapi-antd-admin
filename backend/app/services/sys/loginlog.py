from datetime import datetime
from typing import List
from fastapi import HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

import app.dal.sys.monitor.loginlog as loginlog_dal
from app.utils.loginlog_info import get_loginlog_info
from app.services.sys._format import format_login_list, format_loginlog


async def get_loginlog_list(db: AsyncSession, page: int = 1, pageSize: int = 10):
    """
    获取登录日志列表
    """
    try:
        count = await loginlog_dal.get_count(db)
        list = await loginlog_dal.get_Loginlog_list(db, page, pageSize)
        data = {"total": count, "list": format_login_list(list)}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_loginlog(db: AsyncSession, request: Request, loginlog):
    """
    创建登录日志
    """
    try:
        loginlog = get_loginlog_info(
            request, name=loginlog.name, userId=loginlog.userId
        )
        data = await loginlog_dal.create_loginlog(db, loginlog)
        return format_loginlog(data)
    except Exception as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_loginlog_by_userId_name(
    db: AsyncSession, request: Request, name: str, userId: int
):
    """
    创建登录日志
    """
    try:
        loginlog = get_loginlog_info(request, name, userId)
        loginlog["login_at"] = datetime.fromisoformat(
            loginlog["login_at"]
        )  # 时间字符串转datetime
        data = await loginlog_dal.create_loginlog(db, loginlog)
        return format_loginlog(data)
    except Exception as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def update_loginlog_by_id(db: AsyncSession, loginlog_id: int, item):
    try:
        data = await loginlog_dal.update_loginlog_by_id(db, loginlog_id, item)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def delete_loginlog_by_ids(db: AsyncSession, ids: List[int]):
    try:
        data = await loginlog_dal.delete_loginlog_by_ids(db, ids)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
