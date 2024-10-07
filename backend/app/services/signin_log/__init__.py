from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from app.dal.signin.signinlog import create_user_signlog
from app.services.signin_log._format import format_signin_log
from sqlalchemy.ext.asyncio import AsyncSession

async def create_signin_log_service(db: AsyncSession, current_user_id: int):
    try:
        sign_log = {
            "userId": current_user_id,
            "sign_type": 1
        }
        data = await create_user_signlog(db, sign_log)
        return format_signin_log(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
