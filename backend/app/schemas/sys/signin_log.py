import datetime
from pydantic import BaseModel, Field

class SigninLogBase(BaseModel):
    """SigninLog Base"""
    userId: str = Field(..., description="用户名")
    sign_type: int = Field(..., description="密码")
    sign_time: datetime = Field(..., description="密码")


class SigninLogCreate(SigninLogBase):
    """SigninLog Create Schema"""
    pass

class SigninLogUpdate(BaseModel):
    """SigninLog Update Schema"""
    pass

