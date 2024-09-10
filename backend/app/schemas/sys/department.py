from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

from app.schemas.sys.user import UserResponse


class DepartmentBase(BaseModel):
    name: str = Field(
        ..., title="Department Name", description="The name of the department"
    )
    description: Optional[str] = Field(
        None, title="Description", description="A brief description of the department"
    )
    order_no: Optional[int] = Field(
        None, title="Order No", description="The order number of the department"
    )


class DepartmentCreate(DepartmentBase):
    parent_department_id: Optional[int] = Field(
        None,
        title="Parent Department ID",
        description="The ID of the parent department",
    )


class DepartmentUpdate(DepartmentBase):
    parent_department_id: Optional[int] = Field(
        None,
        title="Parent Department ID",
        description="The ID of the parent department",
    )


class DepartmentInDBBase(DepartmentBase):
    id: int
    createdAt: datetime
    updatedAt: Optional[datetime]

    class Config:
        orm_mode = True


class Department(DepartmentInDBBase):
    parent: Optional["Department"] = (
        None  # Use forward reference for self-referential relationship
    )
    children: List["Department"] = (
        []
    )  # Use forward reference for list of child departments
    users: List[UserResponse] = (
        []
    )  # Use forward reference for list of users in the department


class DepartmentInDB(DepartmentInDBBase):
    pass
