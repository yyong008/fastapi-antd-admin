import jwt

from fastapi import Depends, HTTPException, status

from fastapi.security import OAuth2PasswordBearer
from app.dal.sys.user import get_user_by_id
from app.utils.token import jwt_decode
from app.db.client import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Depends = Depends(get_db),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt_decode(token)
        user_id: str | None = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception

    user = get_user_by_id(user_id, db)
    if user is None:
        raise credentials_exception
    return user
