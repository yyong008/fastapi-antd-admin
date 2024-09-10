import jwt

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordBearer
from app.dal.sys.user import UserDAL
from app.utils.token import jwt_decode

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(
    db: Session,
    token: str = Depends(oauth2_scheme),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt_decode(token)
        user_id: str | None = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception

    user_dal = UserDAL(db)
    user = user_dal.get_user_by_id.get(user_id)
    if user is None:
        raise credentials_exception
    return user
