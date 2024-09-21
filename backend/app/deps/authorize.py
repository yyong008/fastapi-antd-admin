from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt

from app.config.config import get_settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

config = get_settings()

def auth_required(token: str = Depends(oauth2_scheme)):
  try:
    payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
    user_id: str | None = payload.get("user_id")
    print(user_id)
    if user_id is None:
      raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return user_id
  except jwt.PyJWTError:  
    raise HTTPException(status_code=401, detail="Invalid token")
