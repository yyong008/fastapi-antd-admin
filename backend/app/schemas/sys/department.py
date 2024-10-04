from pydantic import BaseModel, Field
from typing import Optional


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


class DepartmentDeleteByIds(BaseModel):
    ids: list[int]
