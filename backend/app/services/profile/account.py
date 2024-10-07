from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.sys.user import get_user_by_id
from app.services.sys.user import format_user

async def get_profile_account_service(db: Session, current_user_id):
    try:
        user_in_db = await get_user_by_id(db, current_user_id)
        data = format_user(user_in_db)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

async def update_profile_account_service(db: Session, current_user_id, user):
    pass
