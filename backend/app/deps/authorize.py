from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def auth_required():
    return {}


# def auth_required(token: str = Depends(oauth2_scheme)):
#   try:
#     payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
#     user_id: str | None = payload.get("sub")
#     print(user_id)
#     if user_id is None:
#       raise HTTPException(status_code=401, detail="Invalid authentication credentials")
#     return user_id
#   except jwt.PyJWTError:  # 捕获 JWT 解码错误
#     raise HTTPException(status_code=401, detail="Invalid token")
