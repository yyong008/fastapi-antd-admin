from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.system.user import UserSignLog
from app.dal.signin.signinlog import create_user_signlog
from app.services.signin_log.format import format_signin_log

# from app.models
def signin_log_service(username: str, password: str, db: Session):
    pass

async def create_signin_log_service(current_user_id: int, db: Session):
    try:
        user_sign_in_log = UserSignLog(userId=current_user_id, sign_type = 1)
        data = await create_user_signlog(user_sign_in_log, db)
        return format_signin_log(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
