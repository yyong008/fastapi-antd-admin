from fastapi import HTTPException, Request
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

import app.dal.sys.monitor.loginlog as loginlog_dal
from app.utils.loginlog_info import get_loginlog_info


def format_loginlog(log):
    item = {
        "id": log.id,
        "name": log.name,
        "ip": log.ip,
        "address": log.address,
        "login_at": log.login_at,
        "system": log.system,
        "browser": log.browser,
        "userId": log.userId,
    }
    return item


def format_login_list(loginlogs):
    list = []
    for log in loginlogs:
        item = format_loginlog(log)
        list.append(item)
    return list


def get_loginlog_list(page, pageSize, db: Session):
    try:
        count = loginlog_dal.get_count(db)
        list = loginlog_dal.get_Loginlog_list(db, page, pageSize)
        data = {"total": count, "list": format_login_list(list)}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_loginlog(request: Request, loginlog, db: Session):
    try:
        loginlog = get_loginlog_info(
            request, name=loginlog.name, userId=loginlog.userId
        )
        data = loginlog_dal.create_loginlog(loginlog, db)
        return format_loginlog(data)
    except Exception as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_loginlog_by_userId_name(request: Request, name, userId, db: Session):
    try:
        loginlog = get_loginlog_info(request, name, userId)
        data = loginlog_dal.create_loginlog(loginlog, db)
        return format_loginlog(data)
    except Exception as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
