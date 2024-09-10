from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class RefreshToken(BaseModel):
    access_token: str
    token_type: str


class Tokens(BaseModel):
    access_token: str
    refersh_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: Optional[int] = None
