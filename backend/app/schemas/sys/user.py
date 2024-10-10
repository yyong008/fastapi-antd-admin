from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime


class UserBase(BaseModel):
    avatar: Optional[str] = None
    email: Optional[EmailStr] = None
    name: str
    nickname: Optional[str] = None
    lang: str = Field(default="en-US")
    theme: str = Field(default="light")
    phone: Optional[str] = None
    remark: Optional[str] = None
    status: Optional[int] = None
    department_id: Optional[int] = None


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserDeleteByIds(BaseModel):
    ids: List[int]


class Dept(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

    class Config:
        from_attributes = True


class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    department: Optional[Dept] = (
        None  # Adjust based on how you want to represent the department in the response
    )
    roles: Optional[List[str]]

    class Config:
        from_attributes: True
