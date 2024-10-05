from pydantic import BaseModel, Field
from typing import Optional



class RoleBase(BaseModel):
    name: str = Field(..., title="Role Name", description="The name of the role")
    value: str = Field(
        ..., title="Role Value", description="The value associated with the role"
    )
    description: Optional[str] = Field(
        None, title="Description", description="A brief description of the role"
    )
    remark: Optional[str] = Field(
        None, title="Remark", description="Any additional remarks"
    )
    status: Optional[int] = Field(
        None, title="Status", description="The status of the role"
    )


class RoleCreate(RoleBase):
    menus: Optional[list[int]] = Field(None, title="Menus", description="The menus associated with the role")


class RoleUpdate(RoleBase):
    menus: Optional[list[int]] = Field(None, title="Menus", description="The menus associated with the role")
    pass

class RoleDeleteByIds(BaseModel):
    ids: list[int] = Field(..., title="Ids", description="The ids of the roles to be deleted")
