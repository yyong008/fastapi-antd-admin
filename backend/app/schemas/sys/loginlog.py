from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# Schema for reading a Loginlog record (output schema)
class LoginlogReadSchema(BaseModel):
    id: int
    name: str
    ip: Optional[str] = None
    address: Optional[str] = None
    login_at: datetime
    system: Optional[str] = None
    browser: Optional[str] = None
    userId: int

    class Config:
        from_attributes = True


# Schema for creating/updating a Loginlog record (input schema)
class LoginlogCreateUpdateSchema(BaseModel):
    name: str = Field(..., description="Login username")
    ip: Optional[str] = Field(None, description="Login IP address")
    login_at: datetime = Field(..., description="Login address")
    address: Optional[str] = Field(None, description="Login address")
    system: Optional[str] = Field(None, description="Operating system")
    browser: Optional[str] = Field(None, description="Browser information")
    userId: int = Field(..., description="Associated user ID")

    class Config:
        from_attributes = True
